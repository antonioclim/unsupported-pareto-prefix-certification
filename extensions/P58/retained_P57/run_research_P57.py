#!/usr/bin/env python3
"""Reproduce the P57 addendum in an isolated run; preserve delivered evidence."""
import argparse,hashlib,json,shutil,subprocess,sys,time,uuid,zipfile
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parent
COMPANION_SHA='19b24d6f9e3cb4f4417fb554988e9d5dbefd8180792bc02ea47790287a9a37ff'
SAT_SHA='dfdf1d515fc95e95d3b76f907a2ce67932af1f8905f90c3dd7f743ea6c2b751a'
CORE=['upper_87_80_certificate.py','root_verify_87_80.py','upper_87_80_operational.py',
 'lower_audit_mixed_policy.py','geo_comparator.py','gen_endpoint_margin_checks.py',
 'gen_crosscheck_geo.py','lit_finite_oracle.py']
APEX=['practical_negative_stopping.py','root_check_apex.py']
SAT=['practical_sat2024_replay.py','root_check_sat.py']
OUTPUTS={
 'upper_87_80_certificate.py':'upper_87_80_certificate.json',
 'root_verify_87_80.py':'Root_87_80_Independent_P56.json',
 'upper_87_80_operational.py':'upper_87_80_operational.json',
 'lower_audit_mixed_policy.py':'Lower_Independent_Mixed_Policy_Audit_P56.json',
 'geo_comparator.py':'Geometry_Comparator_P56.json',
 'gen_endpoint_margin_checks.py':'Generalization_Checks_P56.json',
 'gen_crosscheck_geo.py':'Generalization_Crosscheck_Geometry_P56.json',
 'lit_finite_oracle.py':'Literature_Finite_Oracle_P56.json',
 'practical_negative_stopping.py':'practical_negative_stopping_P56.json',
 'root_check_apex.py':'Root_APEX_Verification_P56.json',
 'practical_sat2024_replay.py':'practical_sat2024_replay_P56.json',
 'root_check_sat.py':'Root_SAT_Verification_P56.json',
 'practical_cpu_diagnostic.py':'practical_cpu_diagnostic_P56.json'}
# Timing, system strings and generated-report hashes are not scientific outcomes.
VOLATILE={'seconds_observed','elapsed_seconds','process_cpu_ns_single_sequential_pass',
 'wall_seconds','python','platform','source_report_sha256','source_certificate_sha256'}
LINKS={'Root_87_80_Independent_P56.json':('source_certificate_sha256','upper_87_80_certificate.json'),
 'Root_APEX_Verification_P56.json':('source_report_sha256','practical_negative_stopping_P56.json'),
 'Root_SAT_Verification_P56.json':('source_report_sha256','practical_sat2024_replay_P56.json')}

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def scientific(value):
 if isinstance(value,dict):return {k:scientific(v) for k,v in value.items() if k not in VOLATILE}
 if isinstance(value,list):return [scientific(v) for v in value]
 return value
def safe_path(base,name):
 p=Path(name)
 if p.is_absolute() or '..' in p.parts:raise RuntimeError('Unsafe relative member: '+name)
 return base/p

def main():
 if not __debug__:raise RuntimeError('Run without -O: checks require assertions.')
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--mode',choices=['core','apex','sat','all'],default='core')
 p.add_argument('--sat-source',type=Path)
 p.add_argument('--cpu',action='store_true',help='Optional environment-specific APEX CPU diagnostic; timings need not reproduce')
 args=p.parse_args()
 if args.cpu and args.mode not in ('apex','all'):p.error('--cpu requires --mode apex or all')
 manifest=json.loads((ROOT/'MANIFEST_P57.json').read_text())
 for name,sha in manifest['sha256'].items():
  q=safe_path(ROOT,name)
  if not q.is_file() or digest(q)!=sha:raise RuntimeError('Delivered file changed: '+name)
 if args.mode in ('sat','all'):
  if args.sat_source is None or not args.sat_source.is_file():p.error('--sat-source must point to official detailed_results.zip')
  if digest(args.sat_source)!=SAT_SHA:raise RuntimeError('SAT ZIP hash does not match the frozen protocol')
 stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'_'+uuid.uuid4().hex[:8]
 work=ROOT/'reruns'/stamp;work.mkdir(parents=True)
 dst=work/'p56_work';shutil.copytree(ROOT/'p56_work/scripts',dst/'scripts')
 shutil.copytree(ROOT/'p56_work/evidence',dst/'evidence')
 (dst/'research').mkdir()
 shutil.copy2(ROOT/'p56_work/research/practical_SAT2024_protocol.txt',dst/'research/practical_SAT2024_protocol.txt')
 commands=[]
 if args.mode in ('core','all'):commands+=CORE
 if args.mode in ('apex','all'):
  archive=ROOT/'dependencies/unsupported-pareto-prefix-certification-v1.0.0.zip'
  if digest(archive)!=COMPANION_SHA:raise RuntimeError('Published companion checksum mismatch')
  dest=work/'p55_work/replay';dest.mkdir(parents=True)
  with zipfile.ZipFile(archive) as z:
   for member in z.infolist():
    safe_path(dest,member.filename)
    if (member.external_attr>>16)&0o170000==0o120000:raise RuntimeError('Symlink archive member')
   z.extractall(dest)
  commands+=APEX
  if args.cpu:commands+=['practical_cpu_diagnostic.py']
 if args.mode in ('sat','all'):
  shutil.copy2(args.sat_source,dst/'research/SAT2024_detailed_results.zip')
  commands+=SAT
 for name in commands:(dst/'evidence'/OUTPUTS[name]).unlink(missing_ok=True)
 logs=work/'logs';logs.mkdir();results=[];comparisons=[];linkage=[]
 for name in commands:
  print('Running '+name,flush=True);started=time.monotonic()
  with (logs/(name+'.stdout.log')).open('w') as out,(logs/(name+'.stderr.log')).open('w') as err:
   c=subprocess.run([sys.executable,str(dst/'scripts'/name)],cwd=work,stdout=out,stderr=err)
  produced=dst/'evidence'/OUTPUTS[name]
  result={'program':name,'exit_code':c.returncode,'seconds_observed':time.monotonic()-started,'output_created':produced.is_file()}
  if c.returncode==0 and produced.is_file() and name!='practical_cpu_diagnostic.py':
   old=json.loads((ROOT/'p56_work/evidence'/OUTPUTS[name]).read_text())
   new=json.loads(produced.read_text())
   if OUTPUTS[name] in LINKS:
    field,target=LINKS[OUTPUTS[name]]
    linkage.append({'file':OUTPUTS[name],'field':field,'target':target,'match':new[field]==digest(dst/'evidence'/target)})
   a,b=scientific(old),scientific(new)
   for field in sorted(set(a)|set(b)):
    comparisons.append({'file':OUTPUTS[name],'field':field,'match':field in a and field in b and a[field]==b[field]})
  results.append(result)
  if c.returncode or not produced.is_file():break
 status='PASS' if len(results)==len(commands) and all(r['exit_code']==0 and r['output_created'] for r in results) and all(c['match'] for c in comparisons+linkage) else 'FAIL'
 report={'status':status,'mode':args.mode,'delivered_input_files_verified':len(manifest['sha256']),
  'programs':results,'scientific_field_comparisons':comparisons,'comparison_count':len(comparisons),
  'regenerated_report_linkage':linkage,
  'excluded_comparison_fields':sorted(VOLATILE),'all_stderr_empty':all(p.stat().st_size==0 for p in logs.glob('*.stderr.log')),
  'cpu_diagnostic_requested':args.cpu,'cpu_timings_compared':False,
  'sat_source_in_delivered_addendum':False,
  'notes':'Fresh outputs are inside this rerun only. PASS records exact program results and agreement with shipped scientific fields; it is not proof-assistant verification, external peer review, or evidence of deployed economic benefit.'}
 (work/'Replay_P57.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({'status':status,'programs':len(results),'scientific_field_comparisons':len(comparisons),'report':str(work/'Replay_P57.json')}))
 return 0 if status=='PASS' else 1
if __name__=='__main__':sys.exit(main())
