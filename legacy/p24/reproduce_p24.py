#!/usr/bin/env python3
"""Replay selected P21-P23 science and the preserved-data wireless control.

Python standard library only. Run from any directory; sources and retained
outputs are never overwritten. All execution occurs in temporary copies.
This orchestrates the unchanged earlier replayers, retaining their own
dependency ordering, and executes one unchanged own wireless replay script.
"""
from pathlib import Path
from tempfile import TemporaryDirectory
import argparse
import hashlib
import json
import platform
import shutil
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parent
BASE=ROOT.parent
MANIFEST=ROOT/'reproducibility/Replay_Input_Manifest.json'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--record',type=Path,default=ROOT/'review/P24_Clean_Replay_Validation.json',
                        help='A separate local execution report; defaults to the P24 review directory.')
    args=parser.parse_args()
    manifest=json.loads(MANIFEST.read_text())
    if manifest.get('schema')!='p24-selected-scientific-replay-inputs-v1':parser.error('Unrecognised input manifest.')
    entries=manifest['files'];expected={}
    for entry in entries:
        rel=Path(entry['path'])
        if rel.is_absolute() or '..' in rel.parts:parser.error('Unsafe manifest path.')
        path=BASE/rel
        if not path.is_file():parser.error('Required packaged file is missing: '+entry['path'])
        if path.stat().st_size!=entry['size_bytes'] or sha(path)!=entry['sha256']:
            parser.error('Frozen input hash/size mismatch: '+entry['path'])
        expected[entry['path']]=entry['sha256']
    protected={str((BASE/n).resolve()) for n in expected}|{str(MANIFEST.resolve())}
    if str(args.record.resolve()) in protected:parser.error('--record cannot overwrite an input or retained result.')
    manifest_hash=sha(MANIFEST);started=time.monotonic();stage_results=[];all_jobs=[]
    outputs_expected={name:expected[name] for stage in manifest['stages'] for job in stage['jobs'] for name in job['outputs']}
    with TemporaryDirectory(prefix='p24_final_replay_') as temporary:
        work=Path(temporary)
        for name in expected:
            target=work/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(BASE/name,target)
        (work/'_p24_stage_reports').mkdir()
        for stage in manifest['stages']:
            begin=time.monotonic();result={'id':stage['id'],'entrypoint':stage['entrypoint'],
                'declared_program_count':stage['program_count'],'declared_output_count':stage['output_count']}
            jobs=[]
            try:
                process=subprocess.run([sys.executable,str(work/stage['entrypoint'])]+stage['arguments'],
                    cwd=work,capture_output=True,text=True,timeout=stage['timeout_seconds'])
                result['exit_code']=process.returncode
                record_path=work/stage['report_path']
                if process.returncode!=0 or not record_path.is_file():
                    raise RuntimeError('Stage failed or omitted its expected report. '+process.stderr[-5000:])
                report=json.loads(record_path.read_text())
                if stage['kind']=='unchanged_phase_replayer':
                    if report['status']!='PASS':raise RuntimeError('Earlier phase replayer reported failure.')
                    reported=report['jobs']
                    if len(reported)!=len(stage['jobs']):raise RuntimeError('Phase job count changed.')
                    for declared,actual in zip(stage['jobs'],reported):
                        phase=stage['entrypoint'].split('/')[0]
                        actual_script=phase+'/'+actual.get('script',actual.get('program',''))
                        actual_output=phase+'/'+actual['output']
                        actual_hash=actual.get('reproduced_sha256',actual.get('output_sha256'))
                        if actual_script!=declared['script'] or [actual_output]!=declared['outputs']:
                            raise RuntimeError('Earlier job ordering/identity changed.')
                        if actual.get('byte_identical') is not True or actual_hash!=outputs_expected[actual_output]:
                            raise RuntimeError('Earlier phase scientific output did not reproduce exactly.')
                        jobs.append({'script':actual_script,'outputs':[{'path':actual_output,
                            'sha256':actual_hash,'byte_identical':True}],'status':'PASS'})
                    source_flag=report.get('source_inputs_unchanged',report.get('original_inputs_unchanged'))
                    if source_flag is not True:raise RuntimeError('Earlier phase source mutation detected.')
                    result['earlier_replayer_source_inputs_unchanged']=True
                    if 'retained_outputs_unchanged' in report and report['retained_outputs_unchanged'] is not True:
                        raise RuntimeError('Earlier phase retained output mutation detected.')
                else:
                    if report['status']!='PASS_EXACT_APEX_FIXED_SUBCATALOGUE_REPLAY':raise RuntimeError('Wireless replay failed.')
                    matches=[]
                    for output in stage['jobs'][0]['outputs']:
                        digest=sha(work/output)
                        if digest!=outputs_expected[output]:raise RuntimeError('Wireless scientific output mismatch: '+output)
                        matches.append({'path':output,'sha256':digest,'byte_identical':True})
                    jobs.append({'script':stage['entrypoint'],'outputs':matches,'status':'PASS'})
                    result['wireless_evidence']={k:report[k] for k in ('all_source_rows','task_count','prefix_states','policy_paths','summary')}
                    result['wireless_evidence']['new_physical_measurements']=0
                result.update(status='PASS',programs_executed=len(jobs),outputs_byte_identical=sum(len(j['outputs']) for j in jobs))
            except (OSError,ValueError,KeyError,RuntimeError,subprocess.TimeoutExpired) as error:
                result.update(status='FAIL',error=str(error),programs_executed=len(jobs),outputs_byte_identical=sum(len(j['outputs']) for j in jobs))
            result['elapsed_seconds']=round(time.monotonic()-begin,3)
            result['jobs']=jobs;stage_results.append(result);all_jobs.extend(jobs)
            print(json.dumps({k:result[k] for k in ('id','status','programs_executed','outputs_byte_identical','elapsed_seconds')}),flush=True)
            if result['status']!='PASS':break
    unchanged=all((BASE/name).is_file() and sha(BASE/name)==h for name,h in expected.items())
    manifest_unchanged=sha(MANIFEST)==manifest_hash
    passed=(len(stage_results)==manifest['stage_count'] and all(s['status']=='PASS' for s in stage_results)
            and unchanged and manifest_unchanged and len(all_jobs)==manifest['selected_scientific_program_count']
            and sum(s['outputs_byte_identical'] for s in stage_results)==manifest['selected_scientific_output_count'])
    report={'schema':'p24-selected-scientific-replay-validation-v1','status':'PASS' if passed else 'FAIL',
        'selected_scientific_program_count':manifest['selected_scientific_program_count'],
        'scientific_programs_executed':sum(s['programs_executed'] for s in stage_results),
        'selected_scientific_output_count':manifest['selected_scientific_output_count'],
        'scientific_outputs_byte_identical':sum(s['outputs_byte_identical'] for s in stage_results),
        'stages':stage_results,'input_file_count_verified':len(entries),'input_manifest_sha256':manifest_hash,
        'orchestrator_sha256':sha(Path(__file__)),'original_inputs_and_retained_outputs_unchanged':unchanged,
        'input_manifest_unchanged':manifest_unchanged,'input_sha256':expected,
        'python_version':platform.python_version(),'platform_system':platform.system(),
        'total_elapsed_seconds':round(time.monotonic()-started,3),
        'network_calls':False,'installs':False,'external_project_code_executions':0,'new_physical_measurements':0,
        'selection':manifest['selection'],'retained_history_scope':manifest['retained_history_scope'],
        'limitations':manifest['scientific_limits']}
    args.record.parent.mkdir(parents=True,exist_ok=True)
    args.record.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('status','scientific_programs_executed','scientific_outputs_byte_identical',
        'original_inputs_and_retained_outputs_unchanged','total_elapsed_seconds')}),flush=True)
    if not passed:raise SystemExit(1)

if __name__=='__main__':main()
