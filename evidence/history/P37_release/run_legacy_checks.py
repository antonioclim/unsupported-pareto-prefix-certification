#!/usr/bin/env python3
"""P33 current replay of the frozen finite checks and wireless control.

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
from uuid import uuid4
from run_checks import safe_record_path, write_record, utc_now

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'legacy'
MANIFEST=BASE/'p24/reproducibility/Replay_Input_Manifest.json'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--record',type=Path,default=ROOT/'results/Legacy_Local_Replay.json',
                        help='Separate JSON evidence. Normally invoked by run_checks.py.')
    parser.add_argument('--wireless-only',action='store_true',help='Execute only the unchanged wireless producer from absent outputs.')
    args=parser.parse_args()
    try: args.record=safe_record_path(args.record)
    except (OSError,ValueError) as error:parser.error(str(error)+' No new report was written.')
    run_id=str(uuid4());started_at=utc_now()
    write_record(args.record,{'schema':'p33-clean-legacy-replay-validation-v1','status':'RUNNING','run_id':run_id,'started_at_utc':started_at,'phase':'preflight'})
    started=time.monotonic();stage_results=[];all_jobs=[]
    try:
        if not __debug__:raise ValueError('Run without -O: frozen checks use assertions.')
        manifest=json.loads(MANIFEST.read_text())
        if manifest.get('schema')!='p24-selected-scientific-replay-inputs-v1':raise ValueError('Unrecognised input manifest.')
        entries=manifest['files'];expected={}
        for entry in entries:
            rel=Path(entry['path'])
            if rel.is_absolute() or '..' in rel.parts:raise ValueError('Unsafe manifest path.')
            path=BASE/rel
            if not path.is_file():raise ValueError('Required packaged file is missing: '+entry['path'])
            if path.stat().st_size!=entry['size_bytes'] or sha(path)!=entry['sha256']:
                raise ValueError('Frozen input hash/size mismatch: '+entry['path'])
            expected[entry['path']]=entry['sha256']
        protected={str((BASE/n).resolve()) for n in expected}|{str(MANIFEST.resolve())}
        if str(args.record.resolve()) in protected:raise ValueError('--record cannot overwrite an input or retained result.')
        manifest_hash=sha(MANIFEST)
        stages=manifest['stages']
        if args.wireless_only:
            stages=[stage for stage in stages if stage['kind']!='unchanged_phase_replayer']
            if len(stages)!=1:raise ValueError('Expected one wireless stage.')
        selected_programs=sum(stage['program_count'] for stage in stages)
        selected_outputs=sum(stage['output_count'] for stage in stages)
    except (OSError,ValueError,KeyError,TypeError) as error:
        failure={'schema':'p33-clean-legacy-replay-validation-v1','status':'FAIL',
            'run_id':run_id,'started_at_utc':started_at,'finished_at_utc':utc_now(),
            'phase':'preflight','error':str(error),'scientific_programs_executed':0,
            'total_elapsed_seconds':round(time.monotonic()-started,3)}
        write_record(args.record,failure)
        print(json.dumps(failure),file=sys.stderr,flush=True)
        raise SystemExit(2)
    outputs_expected={name:expected[name] for stage in stages for job in stage['jobs'] for name in job['outputs']}
    with TemporaryDirectory(prefix='p24_final_replay_') as temporary:
        work=Path(temporary)
        for name in expected:
            target=work/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(BASE/name,target)
        (work/'_p24_stage_reports').mkdir()
        for stage in stages:
            begin=time.monotonic();result={'id':stage['id'],'entrypoint':stage['entrypoint'],
                'declared_program_count':stage['program_count'],'declared_output_count':stage['output_count']}
            jobs=[]
            try:
                # Frozen inputs were verified before copying. Remove only outputs
                # in this disposable workspace; retain references in BASE. Phase
                # replayers already create source-only inner workspaces.
                report_path=work/stage['report_path']
                report_path.unlink(missing_ok=True)
                if stage['kind']!='unchanged_phase_replayer':
                    output_paths=[work/name for job in stage['jobs'] for name in job['outputs']]
                    for output_path in output_paths:output_path.unlink(missing_ok=True)
                    result['outputs_absent_before_execution']=all(not p.exists() for p in output_paths)
                    if not result['outputs_absent_before_execution']:
                        raise RuntimeError('Wireless output cleanup failed.')
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
    passed=(len(stage_results)==len(stages) and all(s['status']=='PASS' for s in stage_results)
            and unchanged and manifest_unchanged and len(all_jobs)==selected_programs
            and sum(s['outputs_byte_identical'] for s in stage_results)==selected_outputs)
    report={'schema':'p33-clean-legacy-replay-validation-v1','status':'PASS' if passed else 'FAIL',
        'run_id':run_id,'started_at_utc':started_at,'finished_at_utc':utc_now(),
        'selected_scientific_program_count':selected_programs,
        'scientific_programs_executed':sum(s['programs_executed'] for s in stage_results),
        'selected_scientific_output_count':selected_outputs,
        'scientific_outputs_byte_identical':sum(s['outputs_byte_identical'] for s in stage_results),
        'stages':stage_results,'input_file_count_verified':len(entries),'input_manifest_sha256':manifest_hash,
        'orchestrator_sha256':sha(Path(__file__)),'original_inputs_and_retained_outputs_unchanged':unchanged,
        'input_manifest_unchanged':manifest_unchanged,'input_sha256':expected,
        'python_version':platform.python_version(),'platform_system':platform.system(),
        'total_elapsed_seconds':round(time.monotonic()-started,3),
        'network_calls':False,'installs':False,'external_project_code_executions':0,'new_physical_measurements':0,
        'selection':'Wireless stage only' if args.wireless_only else manifest['selection'],'retained_history_scope':manifest['retained_history_scope'],
        'legacy_p24_source_preserved':True,'wireless_outputs_verified_absent_before_producer':all(s.get('outputs_absent_before_execution') is True for s in stage_results if s['id']=='P17_WIRELESS'),
        'limitations':manifest['scientific_limits']}
    write_record(args.record,report)
    print(json.dumps({k:report[k] for k in ('status','scientific_programs_executed','scientific_outputs_byte_identical',
        'original_inputs_and_retained_outputs_unchanged','total_elapsed_seconds')}),flush=True)
    if not passed:raise SystemExit(1)

if __name__=='__main__':main()
