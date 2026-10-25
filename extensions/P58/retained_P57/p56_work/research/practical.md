# P56 practical track: sound negative stopping, two real-archive replays, and an auditable break-even condition

Research date: 25 October 2026. Private exploratory work; no P55 manuscript, published software, or remote record changed. All scientific costs below count disclosed records. A monetary, radio-energy or deployed-service saving was not measured.

## Concrete result and why it matters

The practical limitation can be reduced substantially, although it cannot honestly be deleted. There is now an implemented, sound acquisition improvement with measured disclosure savings on the existing real APEX archive, and a second exploratory replay of public SAT Competition 2024 scores. The mechanism is to stop when the verdict is already certainly FALSE. It preserves every positive execution of the original algorithm, so its existing positive-input competitive theorem survives unchanged. It is not a new improvement to the triangle constant.

The old APEX replay had required all negative tasks to run to census. That fallback was correct but operationally wasteful. The improvement uses two elementary negative certificates; it does not choose the best policy or stop time after inspecting hidden data. All existing P17 policies are reported, including a branch that scarcely improves, and a fairer census baseline receives exactly the same stopping rule.

## A sound negative-certificate lemma

Let each possible completed mean lie coordinatewise between known corners L_g and U_g, including the candidate A. The corners need only be valid bounds; they need not be attainable. Arbitrary dependencies between actual completions are harmless to the following sufficient tests.

1. Certain domination: for some rival g, U_g <= L_A coordinatewise with at least one strict coordinate. Then every actual rival mean <= U_g <= L_A <= every candidate mean, and the strict coordinate remains strict. The candidate is dominated, so GOOD is FALSE.
2. Certain support: there is a nonzero vector w >= 0 with w.U_A <= w.L_g for every rival g. Then, in every legal completion, w.p_A <= w.U_A <= w.L_g <= w.p_g for every g. The candidate is supported under the permitted ties/axis convention, so GOOD is FALSE.

For two objectives normalize w=(a,1-a), 0<=a<=1. Every rival gives a closed linear interval in a. Intersect these intervals exactly. A nonempty interval exports an explicit rational supporting weight. Cost is O(K) rational comparisons per check; for K=3 it is constant-size. Negative certificates remain sound for a tighter physical domain even if its endpoints are missing. This does NOT identify its cheapest certificate or establish a positive competitive ratio for that tighter domain.

These two conditions are sufficient, not necessary; no claim of a complete FALSE oracle or historical novelty is made.

### Stopping-wrapper proposition

Let A be any correct terminating acquisition policy under an observation contract, with arbitrary positive public query prices. Run A using the same private seed. After every acquired record, evaluate any sound FALSE-certificate test; return FALSE immediately when one is present. Otherwise continue A.

For every fixed positive archive and seed on which A is correct, the wrapper cannot trigger. Its entire paid transcript, verdict and acquisition charges equal those of A. On every negative archive the wrapper either uses a prefix of A's paid transcript or all of it. Hence its acquisition charge is at most A's pathwise, for every nonnegative additive query-charge schedule and identical common setup. The policy remains zero-error and terminating. In particular every established positive-input competitive guarantee is preserved exactly.

Internal computation, latency and infrastructure costs are separate. The proposition does not say that total runtime or money always falls. It also does not compare two different base policies on each archive; the domination statement compares one base policy with its own wrapper.

## Fresh exact APEX replay

Implementation: `p56_work/scripts/practical_negative_stopping.py`.
Evidence: `p56_work/evidence/practical_negative_stopping_P56.json`.

It imports the unchanged frozen P17 replay definitions and calls neither their main function nor their file-writing code. The frozen data/fixture hashes are checked before and after. The source includes the same 312 real trial rows, latency/(latency+100 ms) objective, closed independent-square audit relaxation, SHA-selected 128 triples per protocol, every designated candidate and two disjoint three-row blocks. Thus exactly the same 1,536 tasks are retained. Selection and schedule were not retuned from outcomes. The new wrapper is exploratory rather than a preregistered new experiment.

Each policy receives records only through `next_row`; it cannot inspect future records. Every enhanced trace is asserted to be a prefix of the original trace. All positive traces are asserted identical. Exact negative witnesses and terminal prefixes are recorded. Mixture expectations enumerate the fixed probabilities (8/23,8/23,7/23), with no Monte Carlo estimate.

| Fixed policy | Original disclosures | With FALSE stopping | Saved | Saving relative to original |
|---|---:|---:|---:|---:|
| P17 A_LR | 13,824 | 11,515 | 2,309 | 16.7028% |
| P17 A_RL | 13,824 | 11,515 | 2,309 | 16.7028% |
| P17 B | 13,824 | 13,816 | 8 | 0.05787% |
| P17 deterministic screened policy | 13,824 | 11,515 | 2,309 | 16.7028% |
| P17 observed-value greedy | 13,824 | 11,515 | 2,309 | 16.7028% |
| Groupwise census | 13,824 | 12,365 | 1,459 | 10.5541% |
| P17 random mixture | 13,824 | 280952/23 = 12,215.3043 | 37000/23 | 11.6370% |

Fairer comparison: the existing deterministic screened policy with the wrapper uses **850 fewer records than groupwise census with the same wrapper**, a 6.8742% reduction from 12,365. The mixture with the wrapper also beats this improved census baseline, but it remains worse than the screened deterministic policy on this dataset. Nothing selects a different policy per task after observing outcomes.

| Protocol | Tasks | Positive | Negative | Full census | Wrapped census | Wrapped screened deterministic | Positive cost, every policy |
|---|---:|---:|---:|---:|---:|---:|---:|
| Crystal | 768 | 33 | 735 | 6,912 | 6,229 | 5,825 | 297 |
| RPL | 768 | 8 | 760 | 6,912 | 6,136 | 5,690 | 72 |
| Total | 1,536 | 41 | 1,495 | 13,824 | 12,365 | 11,515 | 369 |

The deterministic wrapper stops 915 negative tasks before nine disclosures: 408 Crystal and 507 RPL. All 41 positive tasks still require full census. Its negative total is 11,146; wrapped census uses 11,996 on negatives. This improves the operational treatment of negative verdicts, not the previously negative finding about positive certificates.

Independent finite soundness control enumerates all 5^6 = 15,625 N=2 archives over {(0,0),(0,1),(1,0),(1,1),(3/5,3/5)}, including 142 positive archives. It aggregates every compatible completion for 29,791 distinct observed-prefix states. All 23,728 reported negative certificates are sound: 13,858 fixed-support and 9,870 domination. Another 4,705 states are universally negative in this finite alphabet but are not detected. This confirms both finite soundness and incompleteness; the lemma above proves the general sufficient tests.

These tasks overlap heavily and are not independent experimental replications. Percentages are exact finite-cohort accounting, not population estimates or confidence intervals. The controlled blind replay withholds a public archive from the client, so it does not demonstrate a real paid gateway or actual savings in radio traffic.

## CPU diagnostic and the cost threshold

`practical_cpu_diagnostic.py` ran each of three implementations once to warm up and nine measured repetitions over the same 1,536 tasks, rotating and reversing execution order. CPU process time includes rational arithmetic, local next-row calls and bookkeeping; archive loading and transport are excluded. Measured medians for this container:

| Implementation | Median CPU seconds for cohort | Minimum | Maximum |
|---|---:|---:|---:|
| Full groupwise census | 0.087615668 | 0.080700124 | 0.286775860 |
| Groupwise census + FALSE stopping | 0.762751566 | 0.680230609 | 4.018544470 |
| Screened deterministic + FALSE stopping | 0.956054590 | 0.868180009 | 1.585645396 |

Thus saving record acquisitions did not eliminate computational overhead. The high outliers and shared container are reasons to treat this as a diagnostic, not a stable hardware benchmark. The difference of medians for screened versus improved census is 0.193303024 seconds. In a hypothetical additive sequential model with equal external access latency per record and no batching, overlap or caching, the break-even access latency would be 0.193303024/850 seconds, approximately **0.2274 ms per saved disclosure**. No actual access latency was measured; this is a conditional model calculation, not an observed end-to-end speedup.

For money, let c be a common monetary price per record and H the additional total compute/setup/service cost of the screened implementation over the improved-census baseline on this same cohort. The monetary advantage is exactly

    850 c - H.

A net monetary saving exists iff 850 c > H. For per-task mean additional overhead h this becomes c > (1536/850)h. With heterogeneous prices, replace 850 c by the exact sum of prices of the respective omitted records; unlike comparison to its own base, two different policies need not have nested transcripts, so weighted benefits must be recomputed from their actual disclosed locations.

More generally, for a workload with positive frequency pi, conditional expected disclosure differences d_plus and d_minus between a declared baseline and policy, and expected extra overhead h, expected net gain is c[pi d_plus+(1-pi)d_minus]-h. This is an accounting identity, not a stochastic assumption of the manuscript. The observed 41/1536 is not claimed to estimate future prevalence. For a wrapper against its own base d_plus=0 and d_minus>=0, whereas a comparison between two distinct wrapped policies does not automatically have those properties.

## New public-data lead and second executed replay: SAT Competition 2024

The official 2024 main track uses a 5,000-second limit and PAR-2 penalties for unsolved instances. Official source pages:

- https://satcompetition.github.io/2024/tracks.html (time limit and PAR-2 convention; root web ref `turn59search2`).
- https://satcompetition.github.io/2024/ (official detailed-results link; `turn67view0`).
- https://satcompetition.github.io/2024/results.html (published score/solved counts; `turn62view0`).
- https://satcompetition.github.io/2024/downloads/detailed_results.zip (downloaded 86,068 bytes; four CSVs).

Source ZIP SHA256: `dfdf1d515fc95e95d3b76f907a2ce67932af1f8905f90c3dd7f743ea6c2b751a`.
Main CSV SHA256: `a00f623691e3aa4e10adc85ee0d15b63fbaa25a3cef9c5787d81650ea9d821c6`.

The new protocol was written before computing complete outcomes. It retains all 14 main-track solvers and all 400 rows in the supplied hash order, uses every unordered solver triple and every candidate, and performs no outcome-based filtering. There are 364 triples and **1,092 tasks**. All 5,600 cells are present; 1,827 are the exact 10,000 unsolved penalty. Every other recorded score was verified to lie in [0,5000]. The published score/solved table agrees with the resulting means and counts at its printed precision.

Define a row as (c,f)=(PAR2_score/10000, indicator{PAR2_score=10000}). These exact reported-decimal penalty objectives satisfy the triangle inequality 0<=f<=c<=1. They are not actual elapsed CPU and physical energy. The declared independent closed triangle is a conservative audit completion contract; the tighter observed data image and missing zero-runtime endpoint do not inherit a minimax equality. Known public aggregate scores and alternate public access are intentionally withheld in the replay, not asserted unavailable in reality.

The code implements the existing candidate-census triangle policy from main Theorem 19, enumerating NW/SE continuations with their exact rational p(G), with and without the same negative wrapper. It also evaluates census with and without the wrapper. The candidate gap used by the mixture is available before any branch can diverge: differing wrapped branch traces are explicitly checked to have completed the candidate. There is no use of the future archive to select an online schedule.

**Adverse result:** none of the 1,092 tasks is GOOD. No candidate is GOOD in the full 14-solver catalogue either. This dataset supplies no empirical validation of positive certificates or positive competitive ratios. It is retained as a negative-verdict stress test instead of searching for favorable subsets.

| Fixed policy | Disclosures over all 1,092 tasks |
|---|---:|
| Full census | 1,310,400 |
| Census + FALSE stopping | 1,050,896 |
| Existing triangle mixture without added wrapper | 1,098,086 |
| Existing triangle mixture + FALSE stopping | 1,012,540.2985934708 (exact rational expectation in JSON) |
| NW-first + FALSE stopping | 1,012,537 |
| SE-first + FALSE stopping | 1,012,606 |

The fixed triangle mixture with the wrapper uses 22.7304% fewer disclosures than full census, 3.64981% fewer than census with the same wrapper, and 7.79044% fewer than the unwrapped triangle mixture. These finite-replay results do not establish a general advantage over every competing negative policy. No cost-optimal negative comparator was computed.

Implementation and complete exact output: `practical_sat2024_replay.py`, `practical_sat2024_replay_P56.json`. The downloaded ZIP contains no licence file, and a reuse licence has not been confirmed. Do not redistribute its ZIP or CSV bytes with an artifact. Keep the public URL, hashes, retrieval recipe, code and derived results. The script expects the ZIP in `p56_work/research/`; it does not download it automatically.

## Other dataset searches and why they were not treated as evidence

- NATS-Bench is a primary-source candidate for frozen model configurations: https://github.com/D-X-Y/NATS-Bench (`turn68view1`) offers trial diagnostics, accuracy/loss/time and latency queries. Its repository displays MIT licensing, but that alone should not be used to infer all underlying dataset rights. Aggregate latency versus training/evaluation losses, multiple trials/epochs, public aggregate information and a completion contract must be reconciled. No NATS data replay or benefit is claimed here.
- COCO bbob-biobj: https://numbbo.github.io/coco-doc/bbob-biobj/perf-assessment/ (`turn67view2`) measures function evaluations to hypervolume targets. It is valuable multiobjective benchmarking, but those trajectories are not automatically fixed, paired per-configuration row means with this predicate. No direct transfer or replay claim is made.

These searches favour an actual matching data contract over attaching a fashionable application label.

## Recommended manuscript change and remaining honest limit

A small negative-stopping proposition and the new APEX table can strengthen the practical evidence immediately after independent review. Keep the original no-saving result as the unaugmented policy control and state explicitly that all positive tasks still need census. Add the improved-census baseline, the adverse B branch, and the fact that the random mixture remains worse than the deterministic screened policy here. The SAT experiment is an optional compact supplementary negative-only test; its zero-positive result is scientifically important.

A defensible revised limitation is: "The work now demonstrates reductions in disclosed records in controlled replays of archived data, including comparison with baselines equipped with the same sound negative stopping. These reductions concern an explicit audit completion contract and predominantly negative verdicts; monetary or energy benefits and a deployed evidence service remain unmeasured."

This makes the limitation narrower through new evidence, without turning record counts into invented euros, joules, new radio experiments, or a universal economic claim.
