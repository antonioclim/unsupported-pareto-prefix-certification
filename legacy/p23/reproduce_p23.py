#!/usr/bin/env python3
"""Replay exactly eight P23 scientific programs in an isolated temporary tree.

Python standard library only; no network, installation or external code.
Run from any directory. Both the full dossier and scientific companion must
retain the four legacy proof inputs at the paths listed in LEGACY_INPUTS.
The universal-upper independent checker runs after its producer succeeds.
"""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from tempfile import TemporaryDirectory
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
BASE = ROOT.parent
JOBS = [
    ('lower/check_minimal_alphabet.py', 'lower/Minimal_Alphabet_Exact_Check.json'),
    ('lower/check_collinear_family_barrier.py', 'lower/Collinear_Family_Barrier_Exact_Check.json'),
    ('upper/check_universal_upper.py', 'upper/Universal_Upper_Exact_Check.json'),
    ('finite/check_n6_exact.py', 'finite/N6_Exact_Check.json'),
    ('foundation/check_ordinal_foundation.py', 'foundation/Ordinal_Foundation_Exact_Check.json'),
    ('foundation/check_three_symbol_independent.py', 'foundation/Three_Symbol_Independent_Check.json'),
    ('review/check_n6_independent.py', 'review/N6_Independent_Check.json'),
    ('review/check_universal_upper_independent.py', 'review/Universal_Upper_Independent_Check.json'),
]
CURRENT_PROOFS = [
    'lower/Minimal_Alphabet_Persistent_Overhead_P23.md',
    'lower/Collinear_Two_Chain_Family_Barrier_P23.md',
    'upper/Universal_Triangle_Upper_Bounds_P23.md',
    'finite/N6_Deterministic_Exact_and_Randomised_Lower_P23.md',
]
LEGACY_INPUTS = [
    'p21/article/Manuscript_Paid_Prefix_Certification_P21_v10.md',
    'p22/general_k/Triangular_General_K_Embedding.txt',
    'p22/structure/Band_Domain_Theorems_P22.md',
    'p22/lower/Fixed_Alphabet_Constant_Overhead_P22.md',
]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def source_paths():
    return ([ROOT/script for script, output in JOBS]
            + [ROOT/name for name in CURRENT_PROOFS]
            + [BASE/name for name in LEGACY_INPUTS]
            + [Path(__file__).resolve()])

def snapshot(paths):
    return {path.relative_to(BASE).as_posix(): sha(path) for path in paths}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--record', type=Path, help='Write a new local replay report.')
    args = parser.parse_args()
    sources = source_paths()
    outputs = [ROOT/name for script, name in JOBS]
    missing = [str(path) for path in sources+outputs if not path.is_file()]
    if missing:
        parser.error('Required packaged inputs are missing: '+', '.join(missing))
    # Never overwrite a packaged source or retained scientific result.
    if args.record and args.record.resolve() in {path.resolve() for path in sources+outputs}:
        parser.error('--record must name a separate report, not a source or retained result.')
    before_sources = snapshot(sources)
    before_outputs = snapshot(outputs)
    started = time.monotonic()
    with TemporaryDirectory(prefix='p23_exact_replay_') as temporary:
        work = Path(temporary)
        for path in sources:
            target = work/path.relative_to(BASE)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, target)

        def run(job):
            script, output = job
            beginning = time.monotonic()
            result = {'script': script, 'output': output,
                      'retained_sha256': before_outputs['p23/'+output]}
            try:
                process = subprocess.run(
                    [sys.executable, str(work/'p23'/script)], cwd=work,
                    capture_output=True, text=True, timeout=300)
                result['exit_code'] = process.returncode
                generated = work/'p23'/output
                if generated.is_file():
                    result['reproduced_sha256'] = sha(generated)
                    result['result_status'] = json.loads(generated.read_text())['status']
                result['byte_identical'] = (
                    process.returncode == 0
                    and result.get('result_status') == 'PASS'
                    and result.get('reproduced_sha256') == result['retained_sha256'])
                if not result['byte_identical']:
                    result['stdout'] = process.stdout
                    result['stderr'] = process.stderr
            except (subprocess.TimeoutExpired, OSError, ValueError, KeyError) as error:
                result.update(exit_code=None, byte_identical=False, error=str(error))
            result['elapsed_seconds'] = round(time.monotonic()-beginning, 3)
            print(json.dumps({key: result[key] for key in
                              ('script', 'exit_code', 'byte_identical', 'elapsed_seconds')}), flush=True)
            return result

        # These seven jobs have independent outputs. None consumes another
        # job's generated file. The eighth binds the universal producer JSON.
        with ThreadPoolExecutor(max_workers=3) as pool:
            results = list(pool.map(run, JOBS[:-1]))
        if results[2]['byte_identical']:
            results.append(run(JOBS[-1]))
        else:
            script, output = JOBS[-1]
            results.append({'script': script, 'output': output, 'exit_code': None,
                            'elapsed_seconds': 0, 'byte_identical': False,
                            'retained_sha256': before_outputs['p23/'+output],
                            'skipped': 'Universal producer failed exact reproduction.'})
    after_sources = snapshot(sources)
    after_outputs = snapshot(outputs)
    source_unchanged = before_sources == after_sources
    retained_unchanged = before_outputs == after_outputs
    passed = source_unchanged and retained_unchanged and all(x['byte_identical'] for x in results)
    record = {
        'status': 'PASS' if passed else 'FAIL',
        'program_count': len(JOBS),
        'programs_executed': sum('skipped' not in x for x in results),
        'byte_identical_output_count': sum(x['byte_identical'] for x in results),
        'max_parallel_jobs': 3,
        'dependency_order': 'Universal producer completes successfully before universal independent checker.',
        'jobs': results,
        'source_input_count': len(sources),
        'source_inputs_unchanged': source_unchanged,
        'retained_outputs_unchanged': retained_unchanged,
        'source_sha256': before_sources,
        'retained_output_sha256': before_outputs,
        'total_elapsed_seconds': round(time.monotonic()-started, 3),
        'scope': ('Own standard-library scientific programs replayed in a temporary tree. '
                  'The two universal-upper programs reproduce exact Bernstein certificates '
                  'covering a continuous parameter cube, conditional on the analytic policy '
                  'and polynomial reduction. The other programs perform declared finite '
                  'exact checks. This does not execute an infinite Ramsey argument, '
                  'exhaust a continuous archive class or constitute external peer review '
                  'or proof-assistant verification.'),
    }
    if args.record:
        args.record.parent.mkdir(parents=True, exist_ok=True)
        args.record.write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({key: record[key] for key in
                      ('status', 'program_count', 'programs_executed',
                       'byte_identical_output_count', 'source_inputs_unchanged',
                       'retained_outputs_unchanged', 'total_elapsed_seconds')}))
    if not passed:
        raise SystemExit(1)

if __name__ == '__main__':
    main()
