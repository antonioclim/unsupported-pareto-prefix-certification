<a name="heading-reproducibility-baseline_replay-baseline-replay-entry-points-and-exact-coverage"></a>


# Baseline replay entry points and exact coverage
<a name="s9-1-baseline"></a>

[Documentation index](../README.md)

**Role:** Technical reproduction commands and exact coverage inventory for the frozen baseline; retaining evidence does not imply fresh execution. **Source:** UPPC P61, S9.1, Antonio Clim. Documentation for companion version 1.2.0. Source prose retains its existing manuscript/supplement rights; moving it to MD grants no additional licence.

**Path convention:** scientific commands and scientific-file paths below start at the frozen companion's `reproduction/` root unless a different working directory is expressly stated. In a GitHub source checkout, the equivalent working directory is the repository root; the command paths are identical. Run commands from that software root, not from this `docs/` directory. Retained results are not a claim of a fresh execution. References to manuscript sections and statements use their scientific identifiers; the separately supplied review documents contain the essential proofs.

<a name="heading-reproducibility-baseline_replay-s9-1-retained-baseline-entry-points-and-evidence-classes"></a>

**Reading context.** Section and statement identifiers refer to their original research stages. This note preserves the stated arguments, evidence and limitations. The article and Essential Supplement form a separate review package.


### S9.1. Retained baseline: entry points and evidence classes
Paths in Sections S9.1–S9.3 are relative to the published version 1.1.0 companion's `reproduction/` directory, or equivalently to its GitHub repository root. The scientific programs and evidence described here are retained from version 1.0.0; Section S9.4 maps the research extensions now included in the same release. The full standard-library baseline entry point is:

```sh
python3 run_all_checks.py --record results/Full_Local_User.json
```

The full command executes 42 scientific program entries: six core checks, 26 historical programs and ten additional checks. A separate verifier-control job tests four malformed algebraic mutations; the current 12/11 certificate checker rejects four further malformed certificates. These are program entries with distinct declared roles, not 42 independent confirmations of every theorem. The underlying `run_checks.py` retains its seven-entry core workflow, comprising the six scientific checks and the verifier control; its `--legacy` option adds the historical stage. The full runner invokes that stage and then the ten additional checks. It verifies frozen inputs, works in temporary copies and records the new attempt separately from retained outputs. The execution report determines whether a particular run completed successfully. Python optimisation must remain disabled because the scientific scripts use assertions.

The historical stage produces 27 declared outputs. In the public release, 26 preserve the original bytes. One ordinal-foundation output preserves the scientific fields while recording a provenance migration: `checks/ordinal/check_ordinal_foundation_public.py` recomputes the original finite counts and verifies three public proof inputs. It retains an earlier manuscript digest as historical provenance, explicitly marked `freshly_verified=false`; the earlier manuscript is not included in the public payload. Matching scientific content must therefore be distinguished from byte identity for that output.

The principal result-to-code links are:

- **Retained $12/11$ triangle upper bound, main Theorem 19:** `checks/triangle_12_11/upper_check/verify_upper_certificate.py` produces `Upper_Independent_Check.json` in the same directory. It verifies 4,824 multivariate coefficients in 58 boxes and four malformed-certificate rejections. `verify_high_analytic.py` produces `High_Analytic_Independent_Check.json` and checks nine polynomial identities and seven univariate coefficients. Both use exact arithmetic and Python's standard library. The analytic domain reduction remains part of the proof. Optional symbolic producers in the sibling `upper_primary/` directory require SymPy and are separate from the full standard-library replay.
- **Public-block dependence, Proposition S11:** `checks/public_blocks/check_public_blocks.py` produces `Public_Block_Dependence_Check.json`. Its declared finite audit covers 11 partition families, 1,329,000 prefix states, 7,140 price/setup comparisons and 30 sharp-family instances. Exhaustive finite controls supplement the general proof; they do not cover arbitrary dependencies.
- **Historical 873/800 upper bound, Section S3.2 and Table S7:** `checks/upper/check_improved_upper.py` produces `checks/upper/Improved_Upper_Exact_Certificate.json`. The independent collocation implementation `checks/upper/check_improved_upper_independent.py` produces `checks/upper/Improved_Upper_Independent_Check.json`. Both verify exact polynomial evidence; the analytic reduction remains part of the proof.
- **Ordinal game, main Section 3:** `checks/ordinal/check_full_ordinal_game.py` produces `checks/ordinal/full_ordinal_game_results.json`. Its finite game controls do not prove the causal Ramsey reduction or its continuum quantifiers.
- **Full-candidate obstruction, main Section 5 and Section S3.5:** `checks/candidate/check_candidate_census_obstruction.py` produces `checks/candidate/Candidate_Census_Exact_Check.json`. Its two declared runtime metadata fields may vary; the scientific payload is compared exactly.
- **Geometric reduction obstructions, Section S4.3:** `checks/reductions/check_reduction_obstructions.py` produces `checks/reductions/Reduction_Obstructions_Exact_Check.json`.
- **Policy-transfer examples, main Section 7:** `checks/structure/check_finite_transfer.py` produces `checks/structure/finite_transfer_check.json` from its exact JSON standard output. The general extension theorem is analytic.
- **Malformed-certificate controls:** `checks/check_verifier_rejections.py` produces `checks/Verifier_Rejection_Check.json` and tests four malformed algebraic mutations. These are rejection tests for the supplied verifiers, not an assertion that all possible implementation faults are excluded.
- **Additional finite proof controls:** `checks/audit_p39/ramsey/check_ramsey_continuations.py`, `checks/audit_p39/bands/independent_band_audit.py`, `checks/audit_p39/bernstein/check_analytic_reduction.py`, `checks/audit_p39/transfer/check_transfer_profiles.py` and `checks/audit_p39/extremal/check_extremal_verifier.py` test their stated continuation, geometry, analytic-reduction, transfer and extremal-verifier claims. Their finite scope does not execute the infinite Ramsey proof.
- **Independent-comparator disclosure demonstrator, Section S10:** `checks/prefix_demo/run_demo.py` produces `checks/prefix_demo/results/Demo_Execution_P44.json`. The online service and the independent comparator are separate implementations in the same directory. The full runner removes its temporary output before execution and compares the regenerated scientific payload with the retained result.
- **Certificate-utility counterexample, Section S5.4:** `checks/economics/check_certificate_utility.py` produces `checks/economics/Certificate_Utility_Check.json`, exhaustively checking the 125-archive example and its conditional marginal gains.
- **N4 and band constructions, main Section 4 and Section S2.1:** the historical stage includes `legacy/p21/theory/check_triangle_extension.py`, `legacy/p21/review/check_triangle_n4_worlds.py`, `legacy/p21/review/check_triangle_feasibility_construction.py` and `legacy/p22/structure/check_band_geometry.py`, with separately written band controls in `legacy/p22/review/`.
- **N5, Section S2.2:** `legacy/p22/three_tail/check_triangle_n5_pair.py`, `legacy/p22/upper/check_n5_upper.py` and the independently written N5 checks under `legacy/p22/review/` supply the retained fixed-world and policy controls.
- **Alphabet and N6, Sections S2.3–S2.4:** `legacy/p23/lower/check_minimal_alphabet.py` and `legacy/p23/finite/check_n6_exact.py` have additional independent checks in `legacy/p23/foundation/check_three_symbol_independent.py` and `legacy/p23/review/check_n6_independent.py`.
- **Restricted two-chain family, Section S2.5:** `legacy/p23/lower/check_collinear_family_barrier.py` checks the declared exact algebraic controls.
- **Earlier 35/32 certificate and adverse threshold control, Section S3:** `legacy/p23/upper/check_universal_upper.py` and `legacy/p23/review/check_universal_upper_independent.py` retain the earlier certificate and its exact checks.
- **Expanded APEX replay, Section S11:** `legacy/p17/apex_replay/apex_subcatalogue_replay_v1.py` regenerates `legacy/p17/apex_replay/results_v1.json` and `legacy/p17/apex_replay/comparison_v1.csv`. The current `run_legacy_checks.py` removes these output copies before executing the producer, so retained files cannot stand in for regeneration.

`frozen_manifest.json` identifies the current frozen inputs. `legacy/p24/reproducibility/Replay_Input_Manifest.json` identifies each historical program, expected output and execution stage. The current `RESULTS_MAP.md` and `RESULTS_MAP.json` connect results, figures and code. The command above creates a fresh full report at its specified destination; `evidence/Execution_P33.json` is a retained historical execution record. These manifests, maps, the current README and the execution report determine the covered computations; filenames alone do not establish that a check was run.
