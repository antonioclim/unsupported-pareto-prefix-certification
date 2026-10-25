#!/usr/bin/env python3
"""Reproduce frozen exact checks in temporary copies, without changing evidence.

Python standard library only; run without -O. The optional --legacy switch
also executes the declared 26-program P24 replay. No network or install is used.
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

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / 'frozen_manifest.json'
JOBS = [
    ('upper/check_improved_upper.py', 'upper/Improved_Upper_Exact_Certificate.json', 'exact_bytes'),
    ('upper/check_improved_upper_independent.py', 'upper/Improved_Upper_Independent_Check.json', 'exact_bytes'),
    ('ordinal/check_full_ordinal_game.py', 'ordinal/full_ordinal_game_results.json', 'exact_bytes'),
    ('reductions/check_reduction_obstructions.py', 'reductions/Reduction_Obstructions_Exact_Check.json', 'exact_bytes'),
    ('check_verifier_rejections.py', 'Verifier_Rejection_Check.json', 'exact_bytes'),
    ('candidate/check_candidate_census_obstruction.py', 'candidate/Candidate_Census_Exact_Check.json', 'scientific_json'),
    ('structure/check_finite_transfer.py', 'structure/finite_transfer_check.json', 'exact_bytes_from_stdout'),
]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def scientific_payload(data):
    """Only the candidate check's two declared runtime fields may differ."""
    value = json.loads(data)
    for key in ('elapsed_seconds', 'python_version'):
        if key not in value:
            raise ValueError('Candidate output omitted declared metadata: ' + key)
        del value[key]
    return value


def verify_frozen(manifest):
    if manifest.get('schema') != 'p31-review-companion-frozen-v1':
        raise ValueError('Unrecognised frozen manifest.')
    expected = {}
    for row in manifest['files']:
        relative = Path(row['path'])
        if relative.is_absolute() or '..' in relative.parts:
            raise ValueError('Unsafe frozen input path.')
        path = ROOT / relative
        if not path.is_file() or path.stat().st_size != row['bytes'] or sha(path) != row['sha256']:
            raise ValueError('Frozen input differs or is missing: ' + row['path'])
        expected[row['path']] = row['sha256']
    return expected


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--legacy', action='store_true',
                        help='Also execute the preserved 26-program, 27-output historical replay.')
    parser.add_argument('--verify-only', action='store_true',
                        help='Check all frozen bytes and paths without executing scientific programs.')
    parser.add_argument('--record', type=Path, default=ROOT / 'results/Local_Replay.json',
                        help='New JSON report; a relative path is relative to the current directory.')
    args = parser.parse_args()
    if not __debug__:
        parser.error('Run without -O: the frozen mathematical checks use assertions.')
    if args.verify_only and args.legacy:
        parser.error('--verify-only and --legacy cannot be combined.')
    started = time.perf_counter()
    manifest = json.loads(MANIFEST.read_text())
    try:
        expected = verify_frozen(manifest)
    except (OSError, ValueError, KeyError) as error:
        parser.error(str(error))
    protected = {(ROOT / path).resolve() for path in expected} | {MANIFEST.resolve()}
    if args.record.resolve() in protected:
        parser.error('--record cannot overwrite frozen source or evidence.')
    manifest_hash = sha(MANIFEST)
    records = []
    legacy_record = None
    error = None
    if not args.verify_only:
        with TemporaryDirectory(prefix='prefix_certification_checks_') as temporary:
            work = Path(temporary)
            checks = work / 'checks'
            shutil.copytree(ROOT / 'checks', checks)
            for script, output, mode in JOBS:
                begin = time.perf_counter()
                record = {'script':script, 'output':output, 'comparison':mode,
                          'source_sha256':sha(ROOT / 'checks' / script)}
                try:
                    actual = checks / output
                    actual.unlink(missing_ok=True)
                    process = subprocess.run([sys.executable, str(checks / script)],
                                             cwd=checks, capture_output=True, text=True,
                                             timeout=120)
                    record.update(returncode=process.returncode,
                                  stdout=process.stdout, stderr=process.stderr)
                    if process.returncode:
                        raise RuntimeError('Checker returned a nonzero exit code.')
                    if mode == 'exact_bytes_from_stdout':
                        actual.write_text(process.stdout)
                    if not actual.is_file():
                        raise RuntimeError('Checker did not produce its declared output.')
                    payload = json.loads(actual.read_text())
                    if 'status' in payload and payload['status'] != 'PASS':
                        raise RuntimeError('Checker output status is not PASS.')
                    reference = ROOT / 'checks' / output
                    if mode == 'scientific_json':
                        equal = scientific_payload(actual.read_bytes()) == scientific_payload(reference.read_bytes())
                        record['metadata_excluded_from_comparison'] = ['elapsed_seconds', 'python_version']
                    else:
                        equal = actual.read_bytes() == reference.read_bytes()
                    record.update(expected_output_sha256=sha(reference),
                                  reproduced_output_sha256=sha(actual),
                                  scientific_output_matches=equal)
                    if not equal:
                        raise RuntimeError('Scientific output differs from frozen evidence.')
                    record['status'] = 'PASS'
                except (OSError, ValueError, KeyError, RuntimeError, subprocess.TimeoutExpired) as failure:
                    record.update(status='FAIL', error=str(failure))
                    error = str(failure)
                record['elapsed_seconds'] = round(time.perf_counter() - begin, 4)
                records.append(record)
                print(json.dumps({k:record[k] for k in ('script','status','elapsed_seconds')}), flush=True)
                if error:
                    break
            if args.legacy and not error:
                legacy = work / 'legacy'
                shutil.copytree(ROOT / 'legacy', legacy)
                legacy_output = work / 'Legacy_Local_Replay.json'
                begin = time.perf_counter()
                try:
                    process = subprocess.run([sys.executable, str(legacy / 'p24/reproduce_p24.py'),
                                              '--record', str(legacy_output)], cwd=legacy,
                                             capture_output=True, text=True, timeout=300)
                    if process.returncode or not legacy_output.is_file():
                        raise RuntimeError('Legacy replay failed: ' + process.stderr[-4000:])
                    legacy_record = json.loads(legacy_output.read_text())
                    if not (legacy_record.get('status') == 'PASS'
                            and legacy_record.get('scientific_programs_executed') == 26
                            and legacy_record.get('scientific_outputs_byte_identical') == 27
                            and legacy_record.get('original_inputs_and_retained_outputs_unchanged') is True):
                        raise RuntimeError('Legacy replay did not meet its stated contract.')
                    legacy_record['captured_stdout'] = process.stdout
                    print(json.dumps({'legacy':'PASS','scientific_programs_executed':26,
                                      'scientific_outputs_byte_identical':27}), flush=True)
                except (OSError, ValueError, KeyError, RuntimeError, subprocess.TimeoutExpired) as failure:
                    error = str(failure)
                    legacy_record = {'status':'FAIL','error':error,
                                     'elapsed_seconds':round(time.perf_counter()-begin,4)}
    unchanged = all((ROOT/path).is_file() and sha(ROOT/path)==digest for path,digest in expected.items())
    manifest_unchanged = MANIFEST.is_file() and sha(MANIFEST)==manifest_hash
    passed = (not error and unchanged and manifest_unchanged
              and (args.verify_only or len(records)==len(JOBS)))
    report = {
        'schema':'p31-review-companion-replay-v1', 'status':'PASS' if passed else 'FAIL',
        'mode':'verify_only' if args.verify_only else ('current_and_legacy' if args.legacy else 'current'),
        'python_version':sys.version, 'platform':platform.platform(), 'assertions_enabled':__debug__,
        'frozen_files_verified':len(expected), 'frozen_manifest_sha256':manifest_hash,
        'current_checker_entries_executed':len(records),
        'current_scientific_checks_executed':sum(r['script']!='check_verifier_rejections.py' for r in records),
        'current_malformed_certificate_controls_executed':sum(r['script']=='check_verifier_rejections.py' for r in records),
        'executions':records, 'legacy_executed':bool(args.legacy and legacy_record),
        'legacy':legacy_record, 'frozen_files_unchanged':unchanged,
        'frozen_manifest_unchanged':manifest_unchanged,
        'total_elapsed_seconds':round(time.perf_counter()-started,4),
        'network_calls':False, 'installs':False, 'new_physical_measurements':0,
        'scope':'Exact computational corroboration of the declared cases and algebraic certificate; universal analytic proofs, scientific priority and external review are not executed.'
    }
    if error:
        report['error'] = error
    args.record.parent.mkdir(parents=True, exist_ok=True)
    args.record.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('status','mode','current_checker_entries_executed',
                    'legacy_executed','frozen_files_unchanged','total_elapsed_seconds')}),flush=True)
    if not passed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
