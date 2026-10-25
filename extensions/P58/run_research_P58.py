#!/usr/bin/env python3
"""Verify and replay the P58 addendum without changing delivered evidence."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import time
import uuid

ROOT = Path(__file__).resolve().parent
PROGRAMS = {
    "verify_reduction.py": "RESULTS.json",
    "verify_support_decomposition.py": "support_decomposition_checks.json",
    "check_three_alternative_projection.py": "three_alternative_projection_control.json",
    "check_approximation.py": "approximation_checks.json",
}
STDOUT_REPORTS = {"verify_support_decomposition.py", "check_approximation.py"}
VOLATILE = {"elapsed_seconds", "python", "scipy"}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def scientific(value):
    if isinstance(value, dict):
        return {k: scientific(v) for k, v in value.items() if k not in VOLATILE}
    if isinstance(value, list):
        return [scientific(v) for v in value]
    return value


def verify_manifest():
    manifest = json.loads((ROOT / "MANIFEST_P58.json").read_text())
    for name, expected in manifest["sha256"].items():
        relative = Path(name)
        if relative.is_absolute() or ".." in relative.parts:
            raise RuntimeError("Unsafe manifest member: " + name)
        path = ROOT / relative
        if not path.is_file() or digest(path) != expected:
            raise RuntimeError("Delivered file differs from manifest: " + name)
    return len(manifest["sha256"])


def dimensions(verified):
    import numpy
    import scipy

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "_" + uuid.uuid4().hex[:8]
    work = ROOT / "reruns" / stamp
    scripts = work / "dimension_reduction"
    scripts.mkdir(parents=True)
    logs = work / "logs"
    logs.mkdir()
    for name in PROGRAMS:
        shutil.copy2(ROOT / "dimension_reduction" / name, scripts / name)
    executions = []
    comparisons = []
    for program, output in PROGRAMS.items():
        print("Running " + program, flush=True)
        started = time.monotonic()
        result = subprocess.run([sys.executable, str(scripts / program)], cwd=work,
                                capture_output=True, text=True)
        (logs / (program + ".stdout.log")).write_text(result.stdout)
        (logs / (program + ".stderr.log")).write_text(result.stderr)
        produced = scripts / output
        if result.returncode == 0 and program in STDOUT_REPORTS:
            parsed = json.loads(result.stdout)
            produced.write_text(json.dumps(parsed, indent=2) + "\n")
        entry = {"program": program, "exit_code": result.returncode,
                 "seconds_observed": time.monotonic() - started,
                 "fresh_output_created": produced.is_file(),
                 "stderr_empty": not result.stderr}
        if result.returncode == 0 and produced.is_file():
            original = json.loads((ROOT / "dimension_reduction" / "evidence" / output).read_text())
            current = json.loads(produced.read_text())
            before, after = scientific(original), scientific(current)
            fields = [{"field": name, "match": name in before and name in after
                       and before[name] == after[name]}
                      for name in sorted(set(before) | set(after))]
            comparisons.append({"report": output, "fields": fields,
                                "all_scientific_fields_match": all(x["match"] for x in fields)})
        executions.append(entry)
        if result.returncode or not produced.is_file():
            break
    success = (len(executions) == len(PROGRAMS) and len(comparisons) == len(PROGRAMS)
               and all(x["exit_code"] == 0 and x["fresh_output_created"] for x in executions)
               and all(x["all_scientific_fields_match"] for x in comparisons))
    report = {
        "status": "PASS" if success else "FAIL", "mode": "dimensions",
        "utc_started": stamp, "python": platform.python_version(),
        "numpy": numpy.__version__, "scipy": scipy.__version__,
        "delivered_files_verified": verified,
        "programs": executions, "comparisons": comparisons,
        "scientific_field_comparison_count": sum(len(x["fields"]) for x in comparisons),
        "excluded_scientific_comparison_fields": sorted(VOLATILE),
        "arithmetic": "Logical checks use fractions.Fraction. SciPy/HiGHS LP comparisons are floating-point cross-checks, not exact proofs.",
        "scope": "Finite synthetic corroboration. No universal theorem, historical novelty, deployment performance or economic benefit is established by these tests.",
        "earlier_P57_programs_rerun_in_this_mode": False,
        "delivered_evidence_overwritten": False,
    }
    destination = work / "Replay_P58.json"
    destination.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "programs": len(executions),
                      "scientific_field_comparisons": report["scientific_field_comparison_count"],
                      "report": str(destination)}))
    return 0 if success else 1


def main():
    if not __debug__:
        raise RuntimeError("Run without -O: the scientific checks use assertions.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=["dimensions", "core", "apex", "sat", "all"],
                        default="dimensions")
    parser.add_argument("--sat-source", type=Path)
    parser.add_argument("--cpu", action="store_true")
    args = parser.parse_args()
    if args.cpu and args.mode not in ("apex", "all"):
        parser.error("--cpu requires --mode apex or all")
    if args.mode in ("sat", "all") and (args.sat_source is None or not args.sat_source.is_file()):
        parser.error("--sat-source must point to the official detailed_results.zip")
    verified = verify_manifest()
    if args.mode in ("dimensions", "all"):
        code = dimensions(verified)
        if code or args.mode == "dimensions":
            return code
    command = [sys.executable, str(ROOT / "retained_P57" / "run_research_P57.py"),
               "--mode", args.mode]
    if args.sat_source is not None:
        command.extend(["--sat-source", str(args.sat_source.resolve())])
    if args.cpu:
        command.append("--cpu")
    return subprocess.run(command, cwd=ROOT).returncode


if __name__ == "__main__":
    sys.exit(main())
