#!/usr/bin/env python3
"""One-command P46 replay: retained science, new exact checks and prefix demo.

Standard library only. Sources and retained results are copied to temporary
workspaces. Fresh outputs must match the retained scientific content; only the
explicit runtime fields listed below may differ. No network or installation.
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
from run_checks import safe_record_path, write_record, utc_now, verify_frozen, sha

ROOT = Path(__file__).resolve().parent
JOBS = [
 ('audit_p39/ramsey/check_ramsey_continuations.py', 'audit_p39/ramsey/Ramsey_Continuation_Check.json',
  ['python', 'finished_at_utc']),
 ('audit_p39/bands/independent_band_audit.py', 'audit_p39/bands/Independent_Band_Audit.json',
  ['elapsed_seconds', 'python']),
 ('audit_p39/bernstein/check_analytic_reduction.py', 'audit_p39/bernstein/Analytic_Reduction_Finite_Check.json',
  ['elapsed_seconds', 'python']),
 ('audit_p39/transfer/check_transfer_profiles.py', 'audit_p39/transfer/Transfer_Profiles_Independent_Check.json',
  ['elapsed_seconds']),
 ('audit_p39/extremal/check_extremal_verifier.py', 'audit_p39/extremal/Extremal_Verifier_Check_P39.json', []),
 ('prefix_demo/run_demo.py', 'prefix_demo/results/Demo_Execution_P44.json',
  ['started_at_utc', 'finished_at_utc', 'elapsed_seconds', 'python', 'platform']),
 ('economics/check_certificate_utility.py', 'economics/Certificate_Utility_Check.json',
  ['finished_at_utc', 'python']),
 ('triangle_12_11/upper_check/verify_upper_certificate.py',
  'triangle_12_11/upper_check/Upper_Independent_Check.json', ['elapsed_seconds']),
 ('triangle_12_11/upper_check/verify_high_analytic.py',
  'triangle_12_11/upper_check/High_Analytic_Independent_Check.json', []),
 ('public_blocks/check_public_blocks.py',
  'public_blocks/Public_Block_Dependence_Check.json', ['elapsed_seconds', 'finished_at_utc']),
]


def scientific_payload(payload, ignored):
    value = json.loads(payload)
    for key in ignored:
        if key not in value:
            raise ValueError('Missing declared runtime field: ' + key)
        del value[key]
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--record', type=Path, default=ROOT / 'results/Full_Local_P46.json')
    parser.add_argument('--verify-only', action='store_true', help='Verify frozen input identities; execute no science.')
    args = parser.parse_args()
    try:
        destination = safe_record_path(args.record)
    except (OSError, ValueError) as error:
        parser.error(str(error) + ' No new report was written.')
    started = time.monotonic()
    report = {'schema': 'p46-all-checks-replay-v1', 'run_id': str(uuid4()),
              'status': 'RUNNING', 'started_at_utc': utc_now(), 'finished_at_utc': None,
              'mode': 'verify_only' if args.verify_only else 'complete',
              'additional_checks': [], 'base_replay': None}
    write_record(destination, report)
    try:
        if not __debug__:
            raise ValueError('Run without -O')
        manifest_path = ROOT / 'frozen_manifest.json'
        manifest_hash = sha(manifest_path)
        expected = verify_frozen(json.loads(manifest_path.read_text()))
        if not args.verify_only:
            with TemporaryDirectory(prefix='sicomp_p46_all_checks_') as temporary:
                work = Path(temporary)
                base_report = work / 'Base_Replay.json'
                process = subprocess.run([sys.executable, str(ROOT / 'run_checks.py'), '--legacy',
                                          '--record', str(base_report)], cwd=ROOT,
                                         capture_output=True, text=True, timeout=1800)
                if process.returncode or not base_report.is_file():
                    raise RuntimeError('Base replay failed: ' + process.stderr[-4000:])
                base = json.loads(base_report.read_text())
                if base.get('status') != 'PASS':
                    raise RuntimeError('Base replay did not pass')
                report['base_replay'] = base
                print(json.dumps({'base_replay': 'PASS',
                                  'current_scientific_checks': base['current_scientific_checks_executed'],
                                  'rejection_control': base['current_malformed_certificate_controls_executed'],
                                  'legacy_programs': base['legacy']['scientific_programs_executed'],
                                  'legacy_outputs_matching': base['legacy']['scientific_outputs_matching'],
                                  'legacy_outputs_byte_identical': base['legacy']['scientific_outputs_byte_identical']}), flush=True)
                checks = work / 'checks'
                shutil.copytree(ROOT / 'checks', checks)
                for script, output, ignored in JOBS:
                    item = {'script': 'checks/' + script, 'output': 'checks/' + output,
                            'script_sha256': sha(ROOT / 'checks' / script),
                            'excluded_runtime_fields': ignored}
                    report['additional_checks'].append(item)
                    actual = checks / output
                    actual.unlink(missing_ok=True)
                    item['output_absent_before_execution'] = not actual.exists()
                    command = [sys.executable, str(checks / script)]
                    if script == 'prefix_demo/run_demo.py':
                        command.extend(['--output', str(actual)])
                    begin = time.monotonic()
                    result = subprocess.run(command, cwd=checks, capture_output=True, text=True, timeout=1800)
                    item.update(returncode=result.returncode, elapsed_seconds=round(time.monotonic()-begin, 6))
                    if result.returncode or not actual.is_file():
                        raise RuntimeError('New check failed: ' + script + '\n' + result.stderr[-4000:])
                    current = json.loads(actual.read_text())
                    if current.get('status') != 'PASS':
                        raise RuntimeError('New check did not report PASS: ' + script)
                    executed_source_hash = sha(checks / script)
                    if executed_source_hash != item['script_sha256']:
                        raise RuntimeError('Copied checker source changed: ' + script)
                    source_fields = [key for key in ('script_sha256', 'source_sha256')
                                     if isinstance(current.get(key), str)]
                    for key in source_fields:
                        if current[key] != executed_source_hash:
                            raise RuntimeError('Reported checker source hash differs: ' + script)
                    item['validated_source_hash_fields'] = source_fields
                    reference = ROOT / 'checks' / output
                    if scientific_payload(actual.read_bytes(), ignored) != scientific_payload(reference.read_bytes(), ignored):
                        raise RuntimeError('Scientific payload differs: ' + output)
                    item.update(status='PASS', scientific_match=True,
                                retained_sha256=sha(reference), reproduced_sha256=sha(actual),
                                byte_identical=actual.read_bytes()==reference.read_bytes(), fresh_result=current)
                    print(json.dumps({'check': script, 'status': 'PASS'}), flush=True)
        unchanged = all((ROOT / n).is_file() and sha(ROOT / n) == h for n, h in expected.items())
        if not unchanged or sha(manifest_path) != manifest_hash:
            raise RuntimeError('Frozen input mutation during replay')
        base = report['base_replay']
        base_science = 0 if args.verify_only else base['current_scientific_checks_executed']
        legacy_science = 0 if args.verify_only else base['legacy']['scientific_programs_executed']
        rejection_controls = 0 if args.verify_only else base['current_malformed_certificate_controls_executed']
        historical_mutations = [] if args.verify_only else json.loads((ROOT / 'checks/Verifier_Rejection_Check.json').read_text())['mutations']
        current_mutations = [control for item in report['additional_checks']
                             for control in item['fresh_result'].get('negative_controls', [])]
        rejected_historical = sum(item.get('rejected') is True for item in historical_mutations)
        rejected_current = sum(item.get('status') == 'REJECTED' for item in current_mutations)
        report.update(status='PASS', frozen_files_verified=len(expected), frozen_manifest_sha256=manifest_hash,
                      frozen_files_unchanged=True, frozen_manifest_unchanged=True,
                      current_scientific_checks_executed=base_science,
                      legacy_programs_executed=legacy_science,
                      additional_scientific_checks_executed=len(report['additional_checks']),
                      rejection_control_executed=bool(rejection_controls),
                      malformed_algebraic_mutations_rejected=rejected_historical+rejected_current,
                      historical_malformed_mutations_rejected=rejected_historical,
                      current_malformed_mutations_rejected=rejected_current,
                      scientific_program_entries_executed=base_science+legacy_science+len(report['additional_checks']),
                      scope='Exact polynomial identities and finite Bernstein certificates support the analytic 12/11 proof; finite model enumerations corroborate declared instances. Universal domain reduction, all-size theorems and historical priority require separate arguments.')
    except (OSError, ValueError, KeyError, TypeError, RuntimeError, subprocess.TimeoutExpired) as error:
        report.update(status='FAIL', error=str(error))
    report.update(finished_at_utc=utc_now(), total_elapsed_seconds=round(time.monotonic()-started, 6),
                  python=platform.python_version(), platform=platform.platform(),
                  network_calls=False, installs=False, new_physical_measurements=0)
    write_record(destination, report)
    print(json.dumps({k: report.get(k) for k in ['status', 'run_id', 'finished_at_utc',
                     'scientific_program_entries_executed', 'additional_scientific_checks_executed',
                     'total_elapsed_seconds', 'error']}), flush=True)
    return 0 if report['status'] == 'PASS' else 1

if __name__ == '__main__':
    raise SystemExit(main())
