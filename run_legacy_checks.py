#!/usr/bin/env python3
"""P41 replay of 26 historical scientific jobs with explicit source retirement.

Twenty-six outputs retain exact bytes. One ordinal output retains all scientific
fields but records the omitted P21 manuscript digest as unverified provenance.
The original programs, outputs and manifests remain historical evidence.
"""
from pathlib import Path
from tempfile import TemporaryDirectory
import argparse
import json
import platform
import shutil
import subprocess
import sys
import time
from uuid import uuid4
from run_checks import safe_record_path, write_record, utc_now, sha

ROOT = Path(__file__).resolve().parent
BASE = ROOT / 'legacy'
MANIFEST = BASE / 'p24/reproducibility/Replay_Input_Manifest.json'
RETIREMENT = ROOT / 'provenance/Retired_Manuscript_P21.json'
ADAPTED = ROOT / 'checks/ordinal/check_ordinal_foundation_public.py'
ORDINAL_OLD = 'p23/foundation/check_ordinal_foundation.py'
ORDINAL_NEW = 'p23/foundation/check_ordinal_foundation_public.py'
ORDINAL_OUTPUT = 'p23/foundation/Ordinal_Foundation_Exact_Check.json'


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify_migrated_output(actual, retained, retired, adapted_hash):
    # Compare the complete old payload after explicitly separating provenance.
    a = dict(actual); b = dict(retained)
    history = a.pop('retained_historical_source')
    require(history == {'path': retired['path_in_legacy'], 'sha256': retired['sha256'],
                        'freshly_verified': False,
                        'status': 'digest retained as provenance; omitted source bytes not checked'},
            'Retired-source provenance was changed or mislabelled')
    require(a.pop('script_sha256') == adapted_hash, 'Adapted script hash mismatch')
    require(b.pop('script_sha256') == sha(BASE / ORDINAL_OLD), 'Original script provenance mismatch')
    actual_sources = a.pop('source_sha256'); old_sources = b.pop('source_sha256')
    require(old_sources.pop(retired['path_in_legacy']) == retired['sha256'], 'Historical source digest mismatch')
    require(actual_sources == old_sources, 'Remaining proof-source identities changed')
    for name, digest in actual_sources.items():
        require(sha(BASE / name) == digest, 'Public proof-source bytes changed')
    require(a == b, 'Ordinal scientific content differs after provenance migration')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--record', type=Path, default=ROOT / 'results/Legacy_Local_Replay.json')
    parser.add_argument('--wireless-only', action='store_true')
    args = parser.parse_args()
    try:
        destination = safe_record_path(args.record)
    except (OSError, ValueError) as error:
        parser.error(str(error) + ' No new report was written.')
    report = {'schema': 'p41-public-legacy-replay-v1', 'status': 'RUNNING',
              'run_id': str(uuid4()), 'started_at_utc': utc_now(), 'jobs': []}
    write_record(destination, report)
    started = time.monotonic()
    expected = {}
    try:
        require(__debug__, 'Run without -O')
        manifest = json.loads(MANIFEST.read_text())
        retired = json.loads(RETIREMENT.read_text())
        require(retired['omitted_from_public_snapshot'] is True, 'Invalid retirement record')
        require(retired['fresh_public_replay_verifies_source_bytes'] is False, 'Invalid retirement verification claim')
        omitted = retired['path_in_legacy']
        require(not (BASE / omitted).exists(), 'Retired manuscript must be absent from public snapshot')
        omitted_entries = []
        for entry in manifest['files']:
            relative = Path(entry['path'])
            require(not relative.is_absolute() and '..' not in relative.parts, 'Unsafe manifest path')
            if entry['path'] == omitted:
                require(entry['sha256'] == retired['sha256'] and entry['size_bytes'] == retired['size_bytes'],
                        'Retirement is inconsistent with original manifest')
                omitted_entries.append(entry)
                continue
            path = BASE / relative
            require(path.is_file() and path.stat().st_size == entry['size_bytes']
                    and sha(path) == entry['sha256'], 'Retained input differs: ' + entry['path'])
            expected[entry['path']] = entry['sha256']
        require(len(omitted_entries) == 1, 'Exactly one declared historical source must be omitted')
        before_aux = {str(p.relative_to(ROOT)): sha(p) for p in [MANIFEST, RETIREMENT, ADAPTED, Path(__file__)]}
        jobs = [(stage['id'], job) for stage in manifest['stages'] for job in stage['jobs']
                if not args.wireless_only or stage['id'] == 'P17_WIRELESS']
        require(len(jobs) == (1 if args.wireless_only else 26), 'Unexpected selected job count')
        byte_count = 0; matching_count = 0; migration_count = 0
        with TemporaryDirectory(prefix='sicomp_p41_legacy_') as temporary:
            work = Path(temporary)
            for name in expected:
                target = work / name; target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(BASE / name, target)
            (work / 'provenance').mkdir()
            shutil.copy2(RETIREMENT, work / 'provenance' / RETIREMENT.name)
            (work / ORDINAL_NEW).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ADAPTED, work / ORDINAL_NEW)
            all_outputs = [name for _, job in jobs for name in job['outputs']]
            for name in all_outputs:
                (work / name).unlink(missing_ok=True)
            report['all_selected_outputs_absent_before_execution'] = all(not (work / name).exists() for name in all_outputs)
            require(report['all_selected_outputs_absent_before_execution'], 'Output cleaning failed')
            for stage, job in jobs:
                original_script = job['script']
                executed = ORDINAL_NEW if original_script == ORDINAL_OLD else original_script
                begin = time.monotonic()
                process = subprocess.run([sys.executable, str(work / executed)], cwd=work,
                                         capture_output=True, text=True, timeout=1800)
                item = {'stage': stage, 'historical_job': original_script,
                        'executed_script': 'checks/ordinal/check_ordinal_foundation_public.py'
                        if executed == ORDINAL_NEW else 'legacy/' + executed,
                        'executed_script_sha256': sha(work / executed), 'returncode': process.returncode,
                        'elapsed_seconds': round(time.monotonic() - begin, 6), 'outputs': []}
                report['jobs'].append(item)
                require(process.returncode == 0, 'Job failed: ' + executed + '\n' + process.stderr[-4000:])
                for name in job['outputs']:
                    generated = work / name
                    require(generated.is_file(), 'Job omitted output: ' + name)
                    actual_hash = sha(generated)
                    exact = actual_hash == expected[name]
                    if name == ORDINAL_OUTPUT:
                        verify_migrated_output(json.loads(generated.read_text()),
                                               json.loads((BASE / name).read_text()), retired, sha(ADAPTED))
                        comparison = 'all_scientific_fields_equal_explicit_provenance_migration'
                        migration_count += 1
                        item['migrated_output'] = json.loads(generated.read_text())
                    else:
                        require(exact, 'Historical output differs: ' + name)
                        comparison = 'exact_bytes'
                        byte_count += 1
                    matching_count += 1
                    item['outputs'].append({'path': name, 'generated_sha256': actual_hash,
                                            'retained_sha256': expected[name], 'byte_identical': exact,
                                            'comparison': comparison, 'scientific_match': True})
                item['status'] = 'PASS'
                print(json.dumps({'script': item['executed_script'], 'status': 'PASS',
                                  'outputs': len(item['outputs'])}), flush=True)
        unchanged = all(sha(BASE / n) == h for n, h in expected.items())
        require(unchanged and all(sha(ROOT / n) == h for n, h in before_aux.items()), 'Replay input mutation')
        report.update(status='PASS', scientific_programs_executed=len(jobs),
                      scientific_outputs_matching=matching_count, scientific_outputs_byte_identical=byte_count,
                      provenance_migrated_outputs=migration_count, input_file_count_verified=len(expected),
                      input_sha256=expected, auxiliary_sha256=before_aux,
                      original_inputs_and_retained_outputs_unchanged=True,
                      input_manifest_unchanged=True, omitted_historical_source=retired,
                      omitted_source_bytes_verified_in_public_replay=False,
                      wireless_outputs_verified_absent_before_producer=True,
                      scope='Finite scientific replay. Original source retirement changes provenance only; universal proofs are not executed.')
    except (OSError, ValueError, KeyError, TypeError, RuntimeError, subprocess.TimeoutExpired) as error:
        report.update(status='FAIL', error=str(error))
    report.update(finished_at_utc=utc_now(), total_elapsed_seconds=round(time.monotonic() - started, 6),
                  python_version=platform.python_version(), platform=platform.platform(),
                  network_calls=False, installs=False, new_physical_measurements=0)
    write_record(destination, report)
    print(json.dumps({k: report.get(k) for k in ['status', 'scientific_programs_executed',
                     'scientific_outputs_matching', 'scientific_outputs_byte_identical',
                     'provenance_migrated_outputs', 'total_elapsed_seconds', 'error']}))
    return 0 if report['status'] == 'PASS' else 1

if __name__ == '__main__':
    raise SystemExit(main())
