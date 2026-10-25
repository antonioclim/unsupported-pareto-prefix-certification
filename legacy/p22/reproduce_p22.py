#!/usr/bin/env python3
"""Replay own P22 exact-arithmetic programs in an isolated temporary tree.
Python3 standard library only; no install, network or source mutation.
Run from any directory: python /absolute/path/p22/reproduce_p22.py
"""
from pathlib import Path
from tempfile import TemporaryDirectory
from concurrent.futures import ThreadPoolExecutor
import argparse,hashlib,json,shutil,subprocess,sys,time
ROOT=Path(__file__).resolve().parent
JOBS=[
 ('structure/check_band_geometry.py','structure/Band_Geometry_Exact_Check.json'),
 ('lower/check_nonvanishing_triangle.py','lower/Nonvanishing_Triangular_Lower_Check.json'),
 ('upper/check_n5_upper.py','upper/N5_Upper_Exact_Check.json'),
 ('three_tail/check_triangle_n5_pair.py','three_tail/Triangle_N5_Two_World_Exact_Check.json'),
 ('review/check_band_independent.py','review/Band_Independent_Checks.json'),
 ('review/check_n5_upper_independent.py','review/N5_Upper_Independent_Check.json'),
 ('review/check_general_k_band_independent.py','review/General_K_Band_Independent_Check.json'),
 ('review/check_n5_independent.py','review/N5_Independent_Checks.json'),
 ('upper/check_long_chain_independent.py','upper/Long_Chain_Independent_Check.json'),
 ('lower/check_fixed_alphabet_chain.py','lower/Fixed_Alphabet_Constant_Overhead_Check.json'),
 ('upper/check_candidate_chain_independent.py','upper/Candidate_Chain_Independent_Check.json'),
]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 parser=argparse.ArgumentParser();parser.add_argument('--record',type=Path);args=parser.parse_args()
 inputs=[p for name in ('structure','lower','upper','three_tail','review','general_k') for p in (ROOT/name).glob('*') if p.is_file() and p.suffix in ('.py','.md','.txt')]
 before={str(p.relative_to(ROOT)):sha(p) for p in inputs}
 with TemporaryDirectory(prefix='p22_exact_replay_') as tmp:
  base=Path(tmp);dest=base/'p22'
  for p in inputs:
   q=dest/p.relative_to(ROOT);q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q)
  def run(job):
   script,out=job;t=time.monotonic()
   r=subprocess.run([sys.executable,str(dest/script)],cwd=base,capture_output=True,text=True,timeout=300)
   got=dest/out;expected=ROOT/out
   record={'script':script,'output':out,'exit_code':r.returncode,'elapsed_seconds':round(time.monotonic()-t,3),'byte_identical':r.returncode==0 and got.exists() and sha(got)==sha(expected)}
   if got.exists():record['reproduced_sha256']=sha(got)
   record['retained_sha256']=sha(expected)
   if not record['byte_identical']:record['stdout']=r.stdout;record['stderr']=r.stderr
   print(json.dumps({k:record[k] for k in ('script','exit_code','byte_identical','elapsed_seconds')}),flush=True)
   return record
  with ThreadPoolExecutor(max_workers=3) as pool:results=list(pool.map(run,JOBS))
 after={str(p.relative_to(ROOT)):sha(p) for p in inputs}
 record={'status':'PASS' if before==after and all(x['byte_identical'] for x in results) else 'FAIL','jobs':results,'program_count':len(results),'source_inputs_unchanged':before==after,'source_sha256':before,'scope':'Own exact-arithmetic synthetic checks replayed, not continuous-domain exhaustive verification or external review.'}
 if args.record:args.record.parent.mkdir(parents=True,exist_ok=True);args.record.write_text(json.dumps(record,indent=2)+'\n')
 print(json.dumps({k:record[k] for k in ('status','program_count','source_inputs_unchanged')}))
 if record['status']!='PASS':raise SystemExit(1)
if __name__=='__main__':main()
