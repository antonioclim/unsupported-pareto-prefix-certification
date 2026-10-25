# Dimensional claim-to-code map

Theorem identifiers refer to the P58 working supplement. The canonical proofs take precedence over historical research-note numbering.

| Claim | Executable control | Evidence and interpretation |
| --- | --- | --- |
| Theorem S16: supporting weights with few nonzero criteria; exact three-alternative interval verification | `dimension_reduction/verify_support_decomposition.py` | 2,000 instances in dimensions 2, 3, 5, 20 and 50; exact pair tests and an independently coded exact interval calculation agree; separate full-dimensional floating-point LP agrees. Nine interval boundary controls are exact. The finite check does not prove the general sparse-support statement. |
| Proposition S17: no universal nonnegative affine compression | `dimension_reduction/verify_reduction.py` | 687 explicit matrices in dimensions 3, 5, 20 and 50; the proof covers every matrix, while the executable control covers only the listed family. |
| Theorem S18: anchors, raw-row correspondence and paid-prefix preservation | `dimension_reduction/verify_reduction.py` | 2,187 full-archive verdict comparisons, 57,963 prefix comparisons, 893 nonpositive/infinite-comparator comparisons and twelve positive comparisons. The positive controls have a strict saving from census. These finite checks do not establish the universal policy-simulation theorem. |
| Proposition S19: deterministic reconstruction-error certificate | `dimension_reduction/check_approximation.py`, plus `verify_reduction.py` | 400 exact two-anchor examples and four boundary/tie controls. The strict `2 epsilon` boundary is tested. The checks do not validate statistical or empirically fitted error bounds. |
| Retained full-information representation result, not a new online guarantee | `dimension_reduction/check_three_alternative_projection.py` | Exact enumeration of 41,664 unordered catalogues from `{0,1,2,3}^3`, with 423 containing a GOOD candidate and zero representation failures. |

Delivered prior results are under `dimension_reduction/evidence/`. Fresh P58 outputs are under `validation_P58/`; the replay report compares scientific fields. The archive uses exact fractions except for the explicitly labelled SciPy/HiGHS comparisons. Constants such as 87/80 and the original triangle proof remain covered by the retained P57 evidence and the existing canonical proof, not by the new synthetic controls.

Earlier code and evidence are unchanged under `retained_P57/`; see that directory's `RESULTS_MAP.md` and `README.md` for the original claims and commands.
