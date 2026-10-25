# Results, proofs and reproduction

Reader-facing map by named result. Historical directory names retain input identities; they are not the reading order.

Run commands from the directory containing `run_checks.py`. The separate manuscript and Supplementary Materials provide analytic proofs. All listed scripts, direct inputs and expected outputs are bound by `frozen_manifest.json`; finite cases without separate data are defined in source. Nested historical evidence is identified explicitly and is not counted as freshly executed.

## Exact acquisition value and ordinal reduction

**Proof:** Main Section 3, complete proof A2–A9 and finite-prior argument.

**Checks:** `checks/ordinal/check_full_ordinal_game.py`.

**Inputs:** Exact cases and formulas embedded in the checker source..

**Outputs:** `checks/ordinal/full_ordinal_game_results.json`.

**Command:**

```sh
python3 run_checks.py --record results/Current_Local.json
```

**Scope:** Nine finite ordinal games solved by posterior dynamic programming. The all-size reduction, Ramsey argument and measurable-kernel argument remain analytic proofs.

## Diagonal-band geometry and priced transitions

**Proof:** Main: Diagonal-band geometry and priced transitions (Section 4).

**Checks:** `legacy/p22/structure/check_band_geometry.py`, `legacy/p22/review/check_band_independent.py`, `legacy/p22/review/check_general_k_band_independent.py`.

**Inputs:** `legacy/p22/structure/Band_Domain_Theorems_P22.md`, `legacy/p22/general_k/Triangular_General_K_Embedding.txt`.

**Outputs:** `legacy/p22/structure/Band_Geometry_Exact_Check.json`, `legacy/p22/review/Band_Independent_Checks.json`, `legacy/p22/review/General_K_Band_Independent_Check.json`.

**Command:**

```sh
python3 run_checks.py --legacy --record results/Full_Local.json
```

**Scope:** Exact finite geometry and transition corroboration. The general formula and feasibility claims are proved analytically in the current manuscript.

## Fixed-alphabet persistent overhead and minimal alphabet

**Proof:** Main Section 5 (persistent overhead); Supplementary Section S2.3 (minimal alphabet).

**Checks:** `legacy/p22/lower/check_fixed_alphabet_chain.py`, `legacy/p23/lower/check_minimal_alphabet.py`, `legacy/p23/foundation/check_three_symbol_independent.py`.

**Inputs:** `legacy/p22/lower/Fixed_Alphabet_Constant_Overhead_P22.md`, `legacy/p23/lower/Minimal_Alphabet_Persistent_Overhead_P23.md`.

**Outputs:** `legacy/p22/lower/Fixed_Alphabet_Constant_Overhead_Check.json`, `legacy/p23/lower/Minimal_Alphabet_Exact_Check.json`, `legacy/p23/foundation/Three_Symbol_Independent_Check.json`.

**Command:**

```sh
python3 run_checks.py --legacy --record results/Full_Local.json
```

**Scope:** Finite witnesses and exact rational recurrence checks; the all-length family statement and its limiting ratio require the analytic proof.

## Candidate-observation obstruction and priced counterexample

**Proof:** Main: Candidate-observation barrier (Section 5).

**Checks:** `checks/candidate/check_candidate_census_obstruction.py`.

**Inputs:** Exact cases and formulas embedded in the checker source..

**Outputs:** `checks/candidate/Candidate_Census_Exact_Check.json`.

**Command:**

```sh
python3 run_checks.py --record results/Current_Local.json
```

**Scope:** 332,235 finite prefix states and 2,197 priced prefix states; runtime metadata alone may differ. The q=1 adverse control is negative. No universal proof is inferred from enumeration.

## Uniform triangle policy upper bound

**Proof:** Main Section 6 (complete analytic reduction and 48-box certificate); Supplementary Section S3.2 (coefficient audit expansion).

**Checks:** `checks/upper/check_improved_upper.py`, `checks/upper/check_improved_upper_independent.py`.

**Inputs:** Exact cases and formulas embedded in the checker source..

**Outputs:** `checks/upper/Improved_Upper_Exact_Certificate.json`, `checks/upper/Improved_Upper_Independent_Check.json`.

**Command:**

```sh
python3 run_checks.py --record results/Current_Local.json
```

**Scope:** Exact rational positivity across 48 boxes and 4,644 coefficients, conditional on the analytic reduction. The second checker recovers coefficients by a distinct interpolation method. No optimality or external independent review is claimed.

## Malformed-certificate rejection control

**Proof:** Companion validation control supporting the uniform triangle certificate.

**Checks:** `checks/check_verifier_rejections.py`.

**Inputs:** `checks/upper/check_improved_upper.py`.

**Outputs:** `checks/Verifier_Rejection_Check.json`.

**Command:**

```sh
python3 run_checks.py --record results/Current_Local.json
```

**Scope:** Four malformed algebraic certificates must be rejected. This control is counted separately from the six current scientific checks.

## Certificate-preserving policy transfer

**Proof:** Main: Certificate-preserving policy transfer (Section 7).

**Checks:** `checks/structure/check_finite_transfer.py`.

**Inputs:** Exact cases and formulas embedded in the checker source..

**Outputs:** `checks/structure/finite_transfer_check.json`.

**Command:**

```sh
python3 run_checks.py --record results/Current_Local.json
```

**Scope:** Three-bit finite model: 58,975 function/restriction cases, 131,072 positive instances, 10,937 certificate-preserving cases and 48,038 certificate-changing cases. Does not execute the general policy theorem.

## Obstructions to two simple reductions

**Proof:** Main Section 8 (comparison); Supplementary Section S4.3 (explicit constructions).

**Checks:** `checks/reductions/check_reduction_obstructions.py`.

**Inputs:** Exact cases and formulas embedded in the checker source..

**Outputs:** `checks/reductions/Reduction_Obstructions_Exact_Check.json`.

**Command:**

```sh
python3 run_checks.py --record results/Current_Local.json
```

**Scope:** 128 exact prefix states for the two stated simple-reduction examples. This is not a universal non-reducibility theorem.

## Secondary APEX fixed-subcatalogue replay

**Proof:** Main Section 9 and Supplementary Section S5.4.

**Checks:** `legacy/p17/apex_replay/apex_subcatalogue_replay_v1.py`.

**Inputs:** `legacy/p17/apex_replay/FREEZE_v1.json`, `legacy/p17/apex_replay/PROTOCOL_v1.txt`, `legacy/p9/licence/apex_dataset/Crystal_results.json`, `legacy/p9/licence/apex_dataset/RPL_results.json`.

**Outputs:** `legacy/p17/apex_replay/results_v1.json`, `legacy/p17/apex_replay/comparison_v1.csv`.

**Command:**

```sh
python3 run_checks.py --legacy --record results/Full_Local.json
```

**Scope:** 312 source rows, 1,536 overlapping tasks, 98,304 prefix states and 9,216 policy paths. All 41 positive tasks require nine observations; no disclosure saving is observed. Both outputs are regenerated from absent files. No new physical trial or full-framework execution.

## Four-, five- and six-row triangle cases

**Proof:** Supplementary Sections S2.1, S2.2 and S2.4.

**Checks:** `legacy/p21/review/check_triangle_n4_worlds.py`, `legacy/p22/three_tail/check_triangle_n5_pair.py`, `legacy/p22/upper/check_n5_upper.py`, `legacy/p22/review/check_n5_upper_independent.py`, `legacy/p22/review/check_n5_independent.py`, `legacy/p23/finite/check_n6_exact.py`, `legacy/p23/review/check_n6_independent.py`.

**Inputs:** Exact cases and formulas embedded in the checker source..

**Outputs:** `legacy/p21/review/Triangle_N4_Independent_World_Check.json`, `legacy/p22/three_tail/Triangle_N5_Two_World_Exact_Check.json`, `legacy/p22/upper/N5_Upper_Exact_Check.json`, `legacy/p22/review/N5_Upper_Independent_Check.json`, `legacy/p22/review/N5_Independent_Checks.json`, `legacy/p23/finite/N6_Exact_Check.json`, `legacy/p23/review/N6_Independent_Check.json`.

**Command:**

```sh
python3 run_checks.py --legacy --record results/Full_Local.json
```

**Scope:** Exact declared finite cases and policy controls; the N=6 randomised result is an interval, not an exact optimum.

## Restricted two-chain family barrier

**Proof:** Supplementary Section S2.5.

**Checks:** `legacy/p23/lower/check_collinear_family_barrier.py`.

**Inputs:** Exact cases and formulas embedded in the checker source..

**Outputs:** `legacy/p23/lower/Collinear_Family_Barrier_Exact_Check.json`.

**Command:**

```sh
python3 run_checks.py --legacy --record results/Full_Local.json
```

**Scope:** Exact controls for the explicitly restricted family; no upper bound on all admissible lower-bound constructions.

## Earlier 35/32 policy and adverse threshold controls

**Proof:** Supplementary Sections S3.1 and S3.3.

**Checks:** `legacy/p23/upper/check_universal_upper.py`, `legacy/p23/review/check_universal_upper_independent.py`.

**Inputs:** Exact cases and formulas embedded in the checker source..

**Outputs:** `legacy/p23/upper/Universal_Upper_Exact_Check.json`, `legacy/p23/review/Universal_Upper_Independent_Check.json`.

**Command:**

```sh
python3 run_checks.py --legacy --record results/Full_Local.json
```

**Scope:** Retained earlier certificate and adverse controls. The current main bound is 873/800.

## Completion-domain and Lipschitz controls

**Proof:** Supplementary Sections S5.3–S5.4.

**Checks:** `legacy/p21/review/check_dependent_domain_independent.py`, `legacy/p21/practical/check_lipschitz_certificate.py`.

**Inputs:** Exact cases and formulas embedded in the checker source..

**Outputs:** `legacy/p21/review/Dependent_Domain_Independent_Checks.json`, `legacy/p21/practical/Lipschitz_Certificate_Checks.json`.

**Command:**

```sh
python3 run_checks.py --legacy --record results/Full_Local.json
```

**Scope:** Finite declared model-boundary controls; no noise, dependence or hardware generalisation.

## Square cases, setup and earlier adverse replay

**Proof:** Supplementary Sections S1, S4, S5.2 and S5.4; archive guide in S6.2.

**Checks:** See the explicitly retained evidence below..

**Inputs:** `legacy/p20/output/Research_Companion_Paid_Prefix_v1.zip`.

**Outputs:** Retained within the historical archive; not newly generated in this phase..

**Execution status:** Historical evidence only: consult internal REPLAY_JOBS.json and README.txt after extracting the retained archive. These programs are not part of the current 7+26 run.

**Scope:** Explicit nested paths and failed/corrected coverage histories are listed in Supplementary Section S6.2. Preserved evidence is distinguished from fresh execution.

## Both analytic manuscript figures

**Proof:** Main Sections 4–6 and Figure 1/Figure 2 captions.

**Checks:** `figures/make_figures.py`, `figures/check_figure_values.py`.

**Inputs:** Exact cases and formulas embedded in the checker source..

**Outputs:** `figures/generated/Figure_Exact_Values.json`, `figures/generated/Fig1.pdf`, `figures/generated/Fig2.pdf`.

**Command:**

```sh
python3 figures/make_figures.py --output-dir results/regenerated_figures
python3 figures/check_figure_values.py results/regenerated_figures/Figure_Exact_Values.json
```

**Scope:** Optional plotting dependencies are in figures/requirements-figures.txt. Exact constants, three policy classes, integer-N domains and geometry are checked separately; images do not measure performance.

## Interpretation

The full recorded run is `evidence/Execution_P33.json`: six current scientific checks, one malformed-certificate control and 26 historical programs. The final package also contains optional, separately verified figure generation. `legacy/p24/reproducibility/Replay_Input_Manifest.json` gives the complete selected legacy program/output inventory. A successful replay does not execute universal analytic proofs, establish priority or constitute external review.
