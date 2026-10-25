"""Replay the six new own scientific checks in isolated temporary copies.

Python standard library only. No installation, network, external code or radio
measurements. Historical P20 replay is retained separately and is not repeated.
"""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parent
JOBS = [
    ('theory/check_triangle_extension.py', 'theory/Triangle_Extension_Exact_Check.json'),
    ('review/check_triangle_n4_worlds.py', 'review/Triangle_N4_Independent_World_Check.json'),
    ('review/check_ordinal_worlds.py', 'review/Ordinal_World_Enumeration.json'),
    ('review/check_triangle_feasibility_construction.py', 'review/Triangle_Feasibility_Construction_Check.json'),
    ('review/check_dependent_domain_independent.py', 'review/Dependent_Domain_Independent_Checks.json'),
    ('practical/check_lipschitz_certificate.py', 'practical/Lipschitz_Certificate_Checks.json'),
]
SUPPORT = ['theory/triangle_four_rows_exact.md']

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    records = []
    original = {s: sha(ROOT/s) for pair in JOBS for s in pair}
    original.update({s: sha(ROOT/s) for s in SUPPORT})
    with tempfile.TemporaryDirectory(prefix='p21_exact_replay_') as tmp:
        work = Path(tmp)
        for rel in [s for s, _ in JOBS] + SUPPORT:
            destination = work/rel
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT/rel, destination)
        for program, output in JOBS:
            started = time.monotonic()
            completed = subprocess.run([sys.executable, str(work/program)],
                cwd=work, capture_output=True, text=True, timeout=600)
            if completed.returncode:
                raise RuntimeError(program+' failed: '+completed.stderr[-4000:])
            result = work/output
            assert result.is_file(), output
            assert sha(result) == original[output], 'Scientific output mismatch: '+output
            assert json.loads(result.read_text())['status'] == 'PASS'
            records.append({'program': program, 'output': output,
                'program_sha256': original[program], 'output_sha256': sha(result),
                'returncode': completed.returncode, 'byte_identical': True,
                'elapsed_seconds': round(time.monotonic()-started, 6)})
            print(json.dumps({'completed': program, 'byte_identical': True}), flush=True)
    assert all(sha(ROOT/rel) == h for rel, h in original.items())
    report = {'status':'PASS', 'scientific_programs_executed':len(JOBS),
        'scientific_outputs_byte_identical':len(JOBS), 'jobs':records,
        'input_hashes':original, 'original_inputs_unchanged':True,
        'scope':'New P21 finite exact checks; analytic universal proofs are not executed.',
        'installs':False, 'network_calls':False, 'new_measurements':0}
    target = ROOT/'review/P21_Clean_Replay_Validation.json'
    target.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({'status':'PASS','programs':len(JOBS),'outputs':len(JOBS)}))

if __name__ == '__main__':
    main()
