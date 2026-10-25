# Reproducibility addendum to the P58 working submission

Antonio Clim — *The Price of Finding a Certificate: Unsupported Pareto Points under Prefix Queries*.

This addendum accompanies the selective integration of dimensional results into the working manuscript and supplement. It is not a public software release, has no new DOI, and does not modify GitHub or Zenodo. The immutable companion remains version 1.0.0 at <https://github.com/antonioclim/unsupported-pareto-prefix-certification/releases/tag/v1.0.0> and <https://doi.org/10.5281/zenodo.23632859>.

The complete P57 addendum is preserved byte for byte under `retained_P57/`, including its own manifest, licences, evidence, runner and the unchanged published ZIP. Its internal historical paths are relative to that directory. The new `dimension_reduction/` directory supplies four scientific checks, their previously delivered results and the research derivations. `VALIDATION_P58.json` records the fresh P58 replay and preservation checks.

## Reproduce the dimensional checks

Use Python 3 without `-O`. The actual validation environment used Python 3.12.14, NumPy 2.3.5 and SciPy 1.17.0; the numerical packages are recorded in `dimension_reduction/requirements.txt`. From this extracted root:

```bash
python3 -m pip install -r dimension_reduction/requirements.txt
python3 run_research_P58.py --mode dimensions
```

The runner checks the P58 manifest and copies only the four scripts into a fresh `reruns/<timestamp>_<id>/` directory. It runs each script, captures stdout/stderr, writes the two stdout-only JSON reports, and compares every scientific field with the supplied result. Delivered evidence remains unchanged. The generated `Replay_P58.json` records exit codes, comparisons and environment versions. Elapsed time and Python/SciPy version strings are excluded from scientific equality, but remain in the report. These are reproducibility controls, not portable runtime benchmarks.

`verify_reduction.py` and `check_three_alternative_projection.py` write JSON beside their copied scripts. `verify_support_decomposition.py` and `check_approximation.py` print JSON; the runner saves it. Manual invocation inside the delivered tree may overwrite two reports, so use the runner to preserve the archive.

The logical controls use exact rational arithmetic (`fractions.Fraction`). Two scripts additionally use SciPy/HiGHS floating-point linear programming as an independent numerical cross-check. Numerical agreement does not replace a proof or turn those LP runs into exact certificates. NumPy/SciPy are required for the complete dimensional replay; the retained P57 programs use the Python standard library.

## Retained P57 checks

The wrapper passes these modes to the unchanged historical runner:

```bash
python3 run_research_P58.py --mode core
python3 run_research_P58.py --mode apex
python3 run_research_P58.py --mode sat --sat-source /path/to/detailed_results.zip
```

To run the new dimensional checks followed by all retained scientific checks:

```bash
python3 run_research_P58.py --mode all --sat-source /path/to/detailed_results.zip
```

The external SAT source must be downloaded separately as described in `retained_P57/README.md`; no SAT source ZIP or CSV is redistributed. `--cpu` remains an optional APEX timing diagnostic for `--mode apex` or `--mode all`. The P58 integration reran the four dimensional programs; it did not rerun unchanged P57 computations or reinterpret historical timings as current measurements. The P57 runner continues to verify its original manifest.

## Claims, evidence and limits

See `RESULTS_MAP_P58.md` for the dimensional claim-to-code map and `retained_P57/RESULTS_MAP.md` for earlier results. The integrated article and supplement provide the canonical statements and proofs. `dimension_reduction/Research_Note.md` and its companion notes preserve the preceding research snapshot; their statements that the manuscript had not yet changed refer to that earlier phase. Some research results were deliberately not promoted to formal manuscript statements.

The dimensional checks cover 2,000 three-alternative support instances, nine strict-interval boundary controls, 57,963 prefix comparisons, twelve positive hindsight-comparator comparisons, 400 approximate-transfer instances and four approximation boundary/tie controls. A separate full-information control inspects 41,664 three-alternative catalogues, of which 423 are positive; it is retained research evidence, not a claim of an online reduction.

A single universal two-dimensional nonnegative affine reduction is impossible for general catalogues. Exact three-alternative verification in arbitrary dimension does not imply a reduction in purchased rows or a new competitive ratio. Paid-prefix transfer requires the stated public raw-row/completion correspondence, equal observation rules and equal prices. The 87/80 bound transfers only if all hypotheses of the existing latent triangle theorem hold. Approximate reconstruction tests require valid deterministic error bounds and strict margins; failure is inconclusive. The unrestricted triangle optimum remains open.

All new checks are finite synthetic author-side, AI-assisted controls. They are not external peer review, proof-assistant verification, deployed benchmarks or measured economic benefits. This addendum includes no main-article/supplement source, cover letter, author contact form, or GitHub Actions. No command submits or publishes material remotely.

Component terms and source attribution are specified in `LICENSING_P58.md` and `LICENSE_SCOPE_P58.json`; the retained archive's own notices continue to govern its files.
