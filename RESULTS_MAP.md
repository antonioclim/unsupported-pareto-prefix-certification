# Result maps for release 1.1.0

The new dimensional map is [extensions/P58/RESULTS_MAP_P58.md](extensions/P58/RESULTS_MAP_P58.md). The P57 additions, including the 87/80 certificate and archive replays, are mapped in [extensions/P58/retained_P57/RESULTS_MAP.md](extensions/P58/retained_P57/RESULTS_MAP.md).

The remaining map below is the retained 1.0.0-era map, with its historical scope and identifiers.

# Result-to-check map

The principal command is `python3 run_all_checks.py --record results/Full_Local_P52.json`. It generates fresh outputs in temporary copies, checks retained scientific payloads, validates reported source hashes and verifies that frozen inputs remain unchanged.

The retained P24 manifest declares 26 historical programs and 27 outputs. The public adapter reproduces 26 outputs byte-for-byte and one with scientifically identical content and explicitly migrated provenance. Ten added audit/demo checks run through run_all_checks.py. Together with six core scientific programs, the full replay executes 42 scientific program entries and one separately counted malformed-certificate control.

Mathematical proofs are read, not executed. Exact polynomial identities and Bernstein coefficients are computational proof steps after the analytic domain reduction. Finite catalogue enumeration is corroboration of declared cases and does not prove all-size statements. The current uniform triangle bound is 12/11; 873/800 and 35/32 certificates remain unchanged historical controls.

Only the runtime fields explicitly declared in the runner may differ. Source digests, certificate inputs, coefficients, finite-case counts and scientific conclusions remain part of the equality check.

## Exact acquisition value and ordinal reduction

Proof location: Main Section 3, complete proof A2–A9 and finite-prior argument.

Checks: `checks/ordinal/check_full_ordinal_game.py`.

Outputs: `checks/ordinal/full_ordinal_game_results.json`.

Command:

```text
python3 run_all_checks.py --record results/Full_Local_P52.json
```

Scope: Nine finite ordinal games solved by posterior dynamic programming. The all-size reduction, Ramsey argument and measurable-kernel argument remain analytic proofs.

## Diagonal-band geometry and priced transitions

Proof location: Main: Diagonal-band geometry and priced transitions (Section 4).

Checks: `legacy/p22/structure/check_band_geometry.py`; `legacy/p22/review/check_band_independent.py`; `legacy/p22/review/check_general_k_band_independent.py`.

Direct inputs: `legacy/p22/structure/Band_Domain_Theorems_P22.md`; `legacy/p22/general_k/Triangular_General_K_Embedding.txt`.

Outputs: `legacy/p22/structure/Band_Geometry_Exact_Check.json`; `legacy/p22/review/Band_Independent_Checks.json`; `legacy/p22/review/General_K_Band_Independent_Check.json`.

Command:

```text
python3 run_all_checks.py --record results/Full_Local_P52.json
```

Scope: Exact finite geometry and transition corroboration. The general formula and feasibility claims are proved analytically in the current manuscript.

## Fixed-alphabet persistent overhead and minimal alphabet

Proof location: Main Section 5 (persistent overhead); Supplementary Section S2.3 (minimal alphabet).

Checks: `legacy/p22/lower/check_fixed_alphabet_chain.py`; `legacy/p23/lower/check_minimal_alphabet.py`; `legacy/p23/foundation/check_three_symbol_independent.py`.

Direct inputs: `legacy/p22/lower/Fixed_Alphabet_Constant_Overhead_P22.md`; `legacy/p23/lower/Minimal_Alphabet_Persistent_Overhead_P23.md`.

Outputs: `legacy/p22/lower/Fixed_Alphabet_Constant_Overhead_Check.json`; `legacy/p23/lower/Minimal_Alphabet_Exact_Check.json`; `legacy/p23/foundation/Three_Symbol_Independent_Check.json`.

Command:

```text
python3 run_all_checks.py --record results/Full_Local_P52.json
```

Scope: Finite witnesses and exact rational recurrence checks; the all-length family statement and its limiting ratio require the analytic proof.

## Candidate-observation obstruction and priced counterexample

Proof location: Main Theorem 17 and the matching upper in Theorem 19 (candidate-census class).

Checks: `checks/candidate/check_candidate_census_obstruction.py`.

Outputs: `checks/candidate/Candidate_Census_Exact_Check.json`.

Command:

```text
python3 run_all_checks.py --record results/Full_Local_P52.json
```

Scope: 332,235 finite prefix states and 2,197 priced prefix states corroborate the candidate-census obstruction; runtime metadata alone may differ. The q=1 adverse control is negative. The analytic all-length lower construction and current 12/11 upper establish the exact asymptotic optimum only for policies completing the candidate before TRUE; unrestricted policies retain the interval [23/22, 12/11].

## Current uniform 12/11 triangle policy and exact candidate-census asymptote

Proof location: Main Theorem 19 and its full Section 6 proof; lower construction in Theorem 17.

Checks: `checks/triangle_12_11/upper_check/verify_upper_certificate.py`; `checks/triangle_12_11/upper_check/verify_high_analytic.py`.

Direct inputs: `checks/triangle_12_11/upper_check/low_g_bernstein.json`; `checks/triangle_12_11/upper_check/low_gtlow_bernstein.json`; `checks/triangle_12_11/upper_check/low_gtcut_bernstein.json`; `checks/triangle_12_11/upper_check/low_h_bernstein.json`; `checks/triangle_12_11/upper_primary/high_h_bernstein.json`; `checks/triangle_12_11/upper_primary/high_middlecut_bernstein.json`; `checks/triangle_12_11/upper_primary/high_middlefull_bernstein.json`.

Outputs: `checks/triangle_12_11/upper_check/Upper_Independent_Check.json`; `checks/triangle_12_11/upper_check/High_Analytic_Independent_Check.json`.

Optional producers: `checks/triangle_12_11/upper_check/low_bernstein.py`; `checks/triangle_12_11/upper_primary/high_bernstein.py`; `checks/triangle_12_11/upper_primary/check_high_identities.py`.

Command:

```text
python3 run_all_checks.py --record results/Full_Local_P52.json
```

Scope: The independent standard-library certificate verifier derives polynomial degrees, verifies the rational domain boxes, prefix-free full coverage, and all 4,824 coefficients on 58 boxes; it rejects four malformed certificates. The companion analytic checker verifies nine named algebraic/coefficient identities and seven exact univariate coefficients. These are algebraic proof steps conditional on the written analytic reduction and full domain argument, not a sampling grid. The theorem is for K=3, every N, unit row prices, and permits a common nonnegative information-free setup charge. The candidate-census asymptotic equality is at zero setup; the unrestricted asymptotic interval [23/22,12/11] and gap 1/22 remain open.

Optional construction uses SymPy 1.14.0. Producers are not imported or executed by the full standard-library replay and dependencies are not bundled.

## Public constant-block dependence and sharp comparator distortion

Proof location: Supplementary Proposition S11 and its analytic proof; main Section 9 discussion.

Checks: `checks/public_blocks/check_public_blocks.py`.

Outputs: `checks/public_blocks/Public_Block_Dependence_Check.json`.

Command:

```text
python3 run_all_checks.py --record results/Full_Local_P52.json
```

Scope: Independent truth-table intersection and finite-alphabet completion enumeration verify 1,329,000 prefix states over 11 partition families and 7,140 exact price/setup comparisons. The explicit sharp-family negative predecessor completions are checked for N=1,...,30. The general certificate identity TRUE_D(b)=TRUE_Q(R(b)), unit-price factor m, weighted factor rho_B(w), and all-size sharpness are proved analytically. Public consecutive constant blocks and independent block values are assumptions; statistical correlation does not imply them.

## Historical 873/800 triangle policy certificate

Proof location: Supplementary Section S3.2 (retained earlier policy and certificate).

Checks: `checks/upper/check_improved_upper.py`; `checks/upper/check_improved_upper_independent.py`.

Outputs: `checks/upper/Improved_Upper_Exact_Certificate.json`; `checks/upper/Improved_Upper_Independent_Check.json`.

Command:

```text
python3 run_all_checks.py --record results/Full_Local_P52.json
```

Scope: Retained exact rational positivity across 48 boxes and 4,644 coefficients for the earlier 873/800 rule. Both historical checker sources and retained outputs are unchanged. This is not the current 12/11 certificate.

## Malformed-certificate rejection control

Proof location: Companion validation control for the historical 873/800 triangle certificate.

Checks: `checks/check_verifier_rejections.py`.

Direct inputs: `checks/upper/Improved_Upper_Exact_Certificate.json`; `checks/upper/check_improved_upper_independent.py`.

Outputs: `checks/Verifier_Rejection_Check.json`.

Certificate producer: `checks/upper/check_improved_upper.py`.

Command:

```text
python3 run_all_checks.py --record results/Full_Local_P52.json
```

Scope: Four malformed historical algebraic certificates must be rejected. This entry is separate from the 42 scientific program entries. The current 12/11 checker additionally includes four inline malformed-certificate rejection tests.

Provenance of the unmodified source certificate; not executed by this rejection control.

## Certificate-preserving policy transfer

Proof location: Main: Certificate-preserving policy transfer (Section 7).

Checks: `checks/structure/check_finite_transfer.py`.

Outputs: `checks/structure/finite_transfer_check.json`.

Command:

```text
python3 run_all_checks.py --record results/Full_Local_P52.json
```

Scope: Three-bit finite model: 58,975 function/restriction cases, 131,072 positive instances, 10,937 certificate-preserving cases and 48,038 certificate-changing cases. Does not execute the general policy theorem.

## Obstructions to two simple reductions

Proof location: Main Section 8 (comparison); Supplementary Section S4.3 (explicit constructions).

Checks: `checks/reductions/check_reduction_obstructions.py`.

Outputs: `checks/reductions/Reduction_Obstructions_Exact_Check.json`.

Command:

```text
python3 run_all_checks.py --record results/Full_Local_P52.json
```

Scope: 128 exact prefix states for the two stated simple-reduction examples. This is not a universal non-reducibility theorem.

## Secondary APEX fixed-subcatalogue replay

Proof location: Main Section 9 and Supplementary Section S5.4.

Checks: `legacy/p17/apex_replay/apex_subcatalogue_replay_v1.py`.

Direct inputs: `legacy/p17/apex_replay/FREEZE_v1.json`; `legacy/p17/apex_replay/PROTOCOL_v1.txt`; `legacy/p9/licence/apex_dataset/Crystal_results.json`; `legacy/p9/licence/apex_dataset/RPL_results.json`.

Outputs: `legacy/p17/apex_replay/results_v1.json`; `legacy/p17/apex_replay/comparison_v1.csv`.

Command:

```text
python3 run_all_checks.py --record results/Full_Local_P52.json
```

Scope: 312 source rows, 1,536 overlapping tasks, 98,304 prefix states and 9,216 policy paths. All 41 positive tasks require nine observations; no disclosure saving is observed. Both outputs are regenerated from absent files. No new physical trial or full-framework execution.

## Four-, five- and six-row triangle cases

Proof location: Supplementary Sections S2.1, S2.2 and S2.4.

Checks: `legacy/p21/review/check_triangle_n4_worlds.py`; `legacy/p22/three_tail/check_triangle_n5_pair.py`; `legacy/p22/upper/check_n5_upper.py`; `legacy/p22/review/check_n5_upper_independent.py`; `legacy/p22/review/check_n5_independent.py`; `legacy/p23/finite/check_n6_exact.py`; `legacy/p23/review/check_n6_independent.py`.

Outputs: `legacy/p21/review/Triangle_N4_Independent_World_Check.json`; `legacy/p22/three_tail/Triangle_N5_Two_World_Exact_Check.json`; `legacy/p22/upper/N5_Upper_Exact_Check.json`; `legacy/p22/review/N5_Upper_Independent_Check.json`; `legacy/p22/review/N5_Independent_Checks.json`; `legacy/p23/finite/N6_Exact_Check.json`; `legacy/p23/review/N6_Independent_Check.json`.

Command:

```text
python3 run_all_checks.py --record results/Full_Local_P52.json
```

Scope: Exact declared finite cases and policy controls; the N=6 randomised result is an interval, not an exact optimum.

## Restricted two-chain family barrier

Proof location: Supplementary Section S2.5.

Checks: `legacy/p23/lower/check_collinear_family_barrier.py`.

Outputs: `legacy/p23/lower/Collinear_Family_Barrier_Exact_Check.json`.

Command:

```text
python3 run_all_checks.py --record results/Full_Local_P52.json
```

Scope: Exact controls for the explicitly restricted family; no upper bound on all admissible lower-bound constructions.

## Earlier 35/32 policy and adverse threshold controls

Proof location: Supplementary Sections S3.1 and S3.3.

Checks: `legacy/p23/upper/check_universal_upper.py`; `legacy/p23/review/check_universal_upper_independent.py`.

Outputs: `legacy/p23/upper/Universal_Upper_Exact_Check.json`; `legacy/p23/review/Universal_Upper_Independent_Check.json`.

Command:

```text
python3 run_all_checks.py --record results/Full_Local_P52.json
```

Scope: Retained earlier 35/32 certificate and adverse controls. The current uniform triangle bound is 12/11; the later historical 873/800 certificate is also retained unchanged.

## Completion-domain and Lipschitz controls

Proof location: Supplementary Sections S5.3–S5.4.

Checks: `legacy/p21/review/check_dependent_domain_independent.py`; `legacy/p21/practical/check_lipschitz_certificate.py`.

Outputs: `legacy/p21/review/Dependent_Domain_Independent_Checks.json`; `legacy/p21/practical/Lipschitz_Certificate_Checks.json`.

Command:

```text
python3 run_all_checks.py --record results/Full_Local_P52.json
```

Scope: Finite declared model-boundary controls; no noise, dependence or hardware generalisation.

## Square cases, setup and earlier adverse replay

Proof location: Supplementary Sections S1, S4, S5.2 and S5.4; archive guide in S6.2.

Direct inputs: `legacy/p20/output/Research_Companion_Paid_Prefix_v1.zip`.

Command:

```text
Historical evidence only: nested programs are not additional executions of the principal command.
```

Scope: Explicit nested paths and failed/corrected coverage histories are listed in Supplementary Section S6.2. Preserved evidence is distinguished from fresh execution.

## Analytic manuscript figures

Proof location: Main figure captions and the associated exact constructions.

Checks: `figures/rebuild_figures.py`; `figures/check_figure_values.py`.

Outputs: `results/regenerated_figures/Figure_Exact_Values.json`; `results/regenerated_figures/Fig1.pdf`; `results/regenerated_figures/Fig2.pdf`; `results/regenerated_figures/Fig3.pdf`.

Command:

```text
python3 figures/rebuild_figures.py --output-dir results/regenerated_figures
python3 figures/check_figure_values.py results/regenerated_figures/Figure_Exact_Values.json
```

Scope: Rebuilds all three figures. Optional plotting dependencies are in figures/requirements-figures.txt; LibreOffice (soffice) is also required for Figure 1. Exact constants, three policy classes, integer-N domains and geometry are checked separately; images do not measure performance.

## Positive/negative continuations and integer embeddings

Proof location: Main numerical lower-bound and compres­sion argument.

Checks: `checks/audit_p39/ramsey/check_ramsey_continuations.py`.

Outputs: `checks/audit_p39/ramsey/Ramsey_Continuation_Check.json`.

Command:

```text
python3 run_all_checks.py --record results/Full_Local_P52.json
```

Scope: Finite exact continuation constructions; does not execute Ramsey or minimax.

## Independent endpoint and diagonal-band audit

Proof location: Main endpoint criterion and band theorems.

Checks: `checks/audit_p39/bands/independent_band_audit.py`.

Outputs: `checks/audit_p39/bands/Independent_Band_Audit.json`.

Command:

```text
python3 run_all_checks.py --record results/Full_Local_P52.json
```

Scope: Exact finite states and legal constructions, including strict boundaries and positive candidate-partial cases.

## Archive-state projection for the analytic upper reduction

Proof location: Main uniform-policy proof.

Checks: `checks/audit_p39/bernstein/check_analytic_reduction.py`.

Outputs: `checks/audit_p39/bernstein/Analytic_Reduction_Finite_Check.json`.

Command:

```text
python3 run_all_checks.py --record results/Full_Local_P52.json
```

Scope: Synthetic finite archive states and cube points; separate from coefficient replay and analytic domain-coverage proof.

## Certificate and positive-transcript transfer profiles

Proof location: Main certificate-preserving transfer criterion.

Checks: `checks/audit_p39/transfer/check_transfer_profiles.py`.

Outputs: `checks/audit_p39/transfer/Transfer_Profiles_Independent_Check.json`.

Command:

```text
python3 run_all_checks.py --record results/Full_Local_P52.json
```

Scope: Finite deterministic transcript-profile enumeration with precedence; no exhaustive treatment of continuous random seeds.

## Slope-extrema implementation criterion

Proof location: Constructive implementation discussion.

Checks: `checks/audit_p39/extremal/check_extremal_verifier.py`.

Outputs: `checks/audit_p39/extremal/Extremal_Verifier_Check_P39.json`.

Command:

```text
python3 run_all_checks.py --record results/Full_Local_P52.json
```

Scope: 168000 complete rational catalogues; verifies finite agreement of two predicates, not acquisition ratios.

## Paid-prefix service and independently computed comparator

Proof location: Supplement synthetic disclosure demonstrator.

Checks: `checks/prefix_demo/run_demo.py`.

Direct inputs: `checks/prefix_demo/fixtures.json`; `checks/prefix_demo/prefix_service.py`; `checks/prefix_demo/independent_comparator.py`.

Outputs: `checks/prefix_demo/results/Demo_Execution_P44.json`.

Command:

```text
python3 run_all_checks.py --record results/Full_Local_P52.json
```

Scope: 10syntheticcases,30exactbranches,640prefixes; finite completion enumeration computes C*. Four negative cases and adverse tariff behaviour retained.

## Failure of adaptive submodularity for the naive certificate indicator

Proof location: Information-economics discussion.

Checks: `checks/economics/check_certificate_utility.py`.

Outputs: `checks/economics/Certificate_Utility_Check.json`.

Command:

```text
python3 run_all_checks.py --record results/Full_Local_P52.json
```

Scope: 125complete finite archives; marginal0versus1/5 counterexample for this reward only; not a general non-reducibility result.

## Historical provenance and statement numbering

Historical source identities and the explicit public provenance migration remain unchanged. The selected historical replay has 27 scientifically matching outputs: 26 byte-identical and one with explicitly adapted provenance. See `docs/Provenance_Migration_P41.md` and the fresh execution record.

The historical statement crosswalk is `docs/Statement_Crosswalk_P41.json`. Current result locations above identify Theorem 19 and Supplementary Proposition S11 directly; historical filenames and checker fields retain their original meanings.
