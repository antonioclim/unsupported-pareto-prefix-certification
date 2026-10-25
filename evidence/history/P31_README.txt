RESEARCH COMPANION FOR REVIEW
The Cost of Certifying Unsupported Pareto Points from Prefix Observations
Antonio Clim | P31 preparation | 23 October 2026

Purpose

This package supplies the exact computational evidence accompanying the
separate manuscript and Supplementary Materials. The current checks reproduce
the rational polynomial certificate, selected ordinal games, reduction
examples, candidate-observation obstruction and finite transfer checks. A
preserved optional replay reproduces the selected earlier scientific evidence,
including the secondary APEX data analysis. Complete analytic proofs are in
the separate Supplementary Materials; this code does not execute them.

The publication companion contains no submission letter or internal editorial
audit. Historical proof texts required by frozen older source hashes remain
under legacy/; they are dependencies of those checks, not the current article.
The main delivery separately preserves the full P30 research record.

Requirements

Use Python 3.12 on Linux, or a comparable Python 3 installation. Python 3.12.14
on Linux is the recorded P30 environment; other platforms are not represented
as natively tested. Only the Python standard library is needed. There is no
package installation, network call, hardware access or LaTeX dependency for
the scientific checks. Do not use python -O: frozen mathematical checks use
assertions. Native Windows text conversion can defeat byte comparisons; use
Linux or Windows Subsystem for Linux for the declared reproduction route.

Quick run

1. Extract the companion into a new directory. Keep its internal paths intact.
   Open a terminal in the directory containing this README and run_checks.py.

2. Check the frozen files without running scientific programs:

   python3 run_checks.py --verify-only --record results/Integrity_Local.json

   Expected: status PASS, zero checker entries executed, and unchanged frozen
   files. Do not edit the manifest to make a changed file appear valid.

3. Reproduce the seven current checker entries:

   python3 run_checks.py --record results/Current_Local.json

   Expected: seven PASS lines and a final status PASS. These comprise six
   scientific checks plus one control that rejects four malformed algebraic
   certificates. The original P30 runs took approximately 2.75 seconds in
   total; local timings vary. The wrapper verifies all frozen inputs, runs in
   temporary copies and leaves the delivered source and evidence unchanged.

4. To reproduce both the current checks and the selected earlier replay:

   python3 run_checks.py --legacy --record results/Full_Local.json

   Expected: seven current checker entries PASS, followed by legacy PASS with
   26 scientific programs and 27 deterministic outputs byte-identical. The
   historical P24 execution took approximately 35 seconds in its recorded
   environment; it is distinct from the current seven-check execution.
   Running this option locally creates a new measured record. Merely including
   the old record in a package is not a new execution.

5. Read status after the command has finished:

   python3 -c "import json; print(json.load(open('results/Current_Local.json'))['status'])"

   Replace Current_Local.json with Full_Local.json if step 4 was used. Commands
   are synchronous; their final line and exit code report completion. A report
   contains complete current-check stdout/stderr, comparison results, source
   hashes, runtime metadata and the legacy report when requested. Relative
   --record paths are resolved from the terminal's current directory; an
   absolute report path is also accepted. A report cannot overwrite a frozen
   file. Additional local reports belong under results/, not evidence/.

On failure

Stop at the first FAIL. Read the named checker entry and its captured error in
the JSON report. If frozen bytes differ, restore a clean extraction. Do not
change expected numerical outputs, assertions or hashes to suppress a failure.
When requesting help, send the exact command, Python version, operating system
and complete failing report. No new upload or publication is performed by a
replay command.

Layout and comparison rules

run_checks.py                    The current orchestrator.
frozen_manifest.json             SHA-256 and size of every frozen kit file.
checks/                          Unchanged P30 programs and expected outputs.
evidence/                        Preserved P30 execution records and provenance.
legacy/p24/reproduce_p24.py       Unchanged earlier replay orchestrator.
legacy/p24/reproducibility/       Original 88-input manifest and replay guide.
legacy/p9/licence/               APEX data, original README and licence notice.
results/                         New local reports; not frozen source evidence.

The upper-bound producer runs before its separate interpolation checker.
Every declared output is deleted from the temporary copy before its producing
program runs, so a retained output cannot masquerade as regenerated evidence.
Six current outputs must match the frozen bytes exactly. The candidate check
contains elapsed_seconds and python_version: only those two declared metadata
fields are excluded from its exact JSON comparison. All scientific values,
case lists and source hashes must still agree. A successful process exit is
insufficient when the output itself has a status field other than PASS.

The legacy subtree contains exactly the 88 immutable dependencies listed by
the original manifest, plus that manifest, its README and the retained P24
execution report. Its original relative paths and bytes are preserved. The
nested P20 archive and older proof texts are included because the frozen
dependency manifest binds them; they are not additional current claims. The
legacy runner's own preservation checks remain active.

Scientific scope

The upper-bound certificate covers 48 boxes and 4,644 rational coefficients,
conditional on the analytic reduction in Supplementary Materials C4.3. The
independent checker uses a separate coefficient-recovery method, not an
independent external research team or a proof assistant. The nine small ordinal
games, 128 reduction prefix states and finite candidate/transfer cases support
their stated finite claims. They do not prove the general Ramsey/minimax or
certificate-transfer theorems.

The APEX replay is a secondary analysis of existing trial summaries. Its
1,536 tasks are not independent new physical trials. The retained adverse
result is 41 positive tasks, each requiring all nine observations; no
disclosure saving was observed. The other 1,495 tasks are negative. No new
radio measurement, 6G/7G or WPT validation is supplied by this companion.

Rights and release status

This prepared review copy assigns no new blanket licence. Author-owned newly
prepared code and text have no public release licence recorded in this kit;
the author should select one before an open archival release. This statement
does not alter the rights granted for any separately licensed component.

The two unchanged APEX data files and original README have retained CC BY 4.0
attribution and licence evidence in legacy/p9/licence/. The dataset is:
Mohamed Hydher, M. H. (2026). APEX Dataset: Testbed Traces and Evaluation
Results, version 1.0. Graz University of Technology.
https://doi.org/10.3217/3dhx0-2k125
Retain its attribution, licence link and description of the secondary
transformations when redistributing source data or derived material.

The associated APEX software deposit has separate MIT terms; its firmware
and framework are not run here. The cited scientific article's licence is not
used to infer data rights. No downloaded third-party scientific full text is
included as a new P31 component. No public deposit or DOI is claimed for this
prepared companion, and no external submission is carried out by its scripts.
