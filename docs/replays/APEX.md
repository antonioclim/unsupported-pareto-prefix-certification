<a name="heading-replays-apex-apex-transformations-adverse-controls-and-wrapped-replay"></a>


# APEX transformations, adverse controls and wrapped replay
<a name="apex-retained-review"></a>

[Documentation index](../README.md)

**Role:** Complete retained APEX replay note; the Essential Supplement contains the condensed method, adverse outcomes and required soundness argument. **Source:** UPPC P61, S11, Antonio Clim. Documentation for companion version 1.2.0. Source prose retains its existing manuscript/supplement rights; moving it to MD grants no additional licence.

**Path convention:** scientific commands and scientific-file paths below start at the frozen companion's `reproduction/` root unless a different working directory is expressly stated. In a GitHub source checkout, the equivalent working directory is the repository root; the command paths are identical. Run commands from that software root, not from this `docs/` directory. Retained results are not a claim of a fresh execution. References to manuscript sections and statements use their scientific identifiers; the separately supplied review documents contain the essential proofs.

<a name="heading-replays-apex-s11-1-retained-apex-transformations-and-unaugmented-replay"></a>

**Reading context.** Section and statement identifiers refer to their original research stages. This note preserves the stated arguments, evidence and limitations. The article and Essential Supplement form a separate review package.


### S11.1. Retained APEX transformations and unaugmented replay
**Archived data and objective transformations.** The APEX dataset contains six trials for each of 16 Crystal and 36 RPL configurations [[34](../REFERENCES.md#ref-34), [33](../REFERENCES.md#ref-33)]. We retain all 312 previously inspected rows and minimise mean latency and mean failure. No new radio experiment is performed. The creator README supplies no trusted universal numerical upper bound on row latency; the observed maximum is insufficient to establish one.

For each predeclared $\tau\in\{10,100,1000\}$ ms, compare positive affine scaling, the point transformation $g_\tau(\bar\ell)$, and the row transformation $\overline{g_\tau(\ell)}$, where $g_\tau(\ell)=\ell/(\ell+\tau)$. With the original objective, this gives ten scenarios per protocol. Exact independent checks find no P2, P4 or GOOD label changes in all 520 candidate classifications.

Table S14. Full-archive classification counts for Crystal and RPL.

| Protocol | Configurations | P2 | P4 | GOOD |
|---|---:|---:|---:|---:|
| Crystal | 16 | 5 | 12 | 1 |
| RPL | 36 | 4 | 33 | 1 |

Nevertheless, every one of the 156 Jensen comparisons is strict: $\overline{g_\tau(\ell)}<g_\tau(\bar\ell)$. The objectives differ. Positive affine scaling preserves geometry but creates no physical cap. The point transformation preserves Pareto order of complete means but can change unsupportedness. The row transformation supplies a bound of one by changing the objective and can change both properties. Frozen synthetic examples demonstrate both failures. Concavity can reward dispersion at a fixed arithmetic mean, requiring an application-specific justification. Here rows contain trial latency summaries, not complete packet distributions or service guarantees.

**Retained replay and adverse tariff controls.** An earlier archive-order comparison is retained as adverse evidence: across 18 positive controls, the evaluated randomised policy costs 1511 expected accesses, versus 1310 for adaptive policy S and 2448 for census. Eight controls lose to S and ten tie. Rotations of six archived rows are not independent physical replications. Neither minimax improvement nor unchanged transformed labels establish empirical superiority.

A further frozen replay selects 128 configuration triples per protocol by a public SHA ranking of fixed labels, independently of outcomes. Every selected triple uses all three designated candidates and both nonoverlapping three-row blocks, with row latency transformed as $\ell/(\ell+100\,\mathrm{ms})$. This yields 1,536 tasks, 98,304 prefix states and 9,216 complete policy paths. The closed independent square is an explicitly declared audit relaxation of the transformed objective, whose exact cost image excludes one. It is not identified with the physical completion domain.

Table S15. Disclosure costs in positive tasks of the archived wireless replay. The last three columns give returned records per positive task, not cumulative costs.

| Protocol | Tasks | GOOD tasks | Positive certificate cost | Positive mixture cost | Positive census cost |
|---|---:|---:|---:|---:|---:|
| Crystal | 768 | 33 | 9 | 9 | 9 |
| RPL | 768 | 8 | 9 | 9 | 9 |

All 41 positive tasks require census. Mixture, deterministic, observed-value greedy and census policies each use 369 disclosures over those tasks. In this unaugmented replay, all 1,495 negative tasks terminate correctly at census. Each policy therefore uses 13,824 disclosures over all 1,536 tasks, comprising 369 on positives and 13,455 on negatives. No disclosure saving is observed in that retained unaugmented replay; Section S11.3 gives the separate augmented replay with sound negative stopping. These 41 tasks are overlapping subcatalogue and block evaluations, not 41 distinct configurations or full-catalogue positive labels. The selection uses every original configuration and trial somewhere but does not create independent replications, a held-out experiment or a population estimate. Public source data can also provide an alternate access route; the controlled blind replay is not itself an operational metered service.

A separate frozen suite balances 32 positive and 32 negative synthetic archives in each of a square and a quarter-grid triangle domain. It checks 8,192 prefixes and 2,560 archive-tariff-policy comparisons across five public fixed schedules. This outcome-balanced design is a stress test, not population sampling. In one square archive, assigning price 12 to the third left row makes the unchanged unit-price mixture cost $252/23$ against a weighted certificate of seven, a ratio $36/23$. Its unit-price $25/23$ guarantee therefore cannot be exported unchanged to general tariffs. The componentwise-minimum triangular policy avoids this particular accounting problem under its own endpoint and independence contract, because its componentwise minimum certificate is also price-optimal.

The operational interpretation developed in Section S12 is a proposed audit service over a frozen archive. Accepted disclosures count returned records; they do not automatically count radio transmissions, experiments, joules or failed retries.

Table S13 in Section S9.2 summarises the retained finite proof controls, their coverage and the preserved failed discovery-stage attempt. These controls support their stated arithmetic and implementation claims; the analytic proofs establish the general results.

APEX data are reused under CC BY 4.0; software licensing is separate. Derived transformations are identified and original bytes retained. Section S9 gives the exact current and nested paths for the evidence, source-version notes and component-specific licence notice. Historical priority is not established by these checks.

The acquisition results concern exact archived observations with independent attainable completions and uncharged arithmetic. Noise, temporal dependence, population inference and physically constrained domains require their own completion and cost models. A returned record need not correspond to one transmission or a fixed energy cost. Within-row endpoint transfer does not remove cross-row constraints. Exact finite-symbol coding likewise does not justify rounding continuous measurements at equality or strict boundaries.


<a name="heading-replays-apex-s11-3-additional-apex-replay-with-the-same-negative-stopping-baseline"></a>


### S11.3. Additional APEX replay with the same negative stopping baseline
This exploratory replay retains exactly the previous 312 APEX trial rows, the transformation $\ell/(\ell+100\,\mathrm{ms})$, the independent-square audit contract, SHA-selected triples, designated candidates and disjoint three-row blocks. The task set and existing policy schedules were not retuned using the new outcomes. Each client obtains rows only through a next-row interface. Every wrapped trace is checked to be a prefix of its own unaugmented trace, and every positive trace is checked to be identical. Mixture expectations enumerate the fixed probabilities $8/23,8/23,7/23$ exactly.

Table S16. Disclosures over the same 1,536 APEX replay tasks. Each unaugmented policy uses 13,824 records. The census baseline receives exactly the same FALSE tests.

| Fixed policy | With FALSE stopping | Saved from its unaugmented version |
|---|---:|---:|
| Left-then-right branch $A_{LR}$ | 11,515 | 2,309 |
| Right-then-left branch $A_{RL}$ | 11,515 | 2,309 |
| Branch $B$ | 13,816 | 8 |
| Existing screened deterministic policy | 11,515 | 2,309 |
| Existing observed-value greedy policy | 11,515 | 2,309 |
| Groupwise census | 12,365 | 1,459 |
| Fixed random mixture | $280952/23\simeq12,215.3043$ | $37000/23$ |

The wrapped screened deterministic policy saves 850 disclosures against census with the same wrapper, a reduction of $850/12365=170/2473$, approximately $6.8742\%$. Its comparison with full census gives 2,309 fewer disclosures, approximately $16.7028\%$. The fixed mixture also improves on wrapped census, but remains worse than the wrapped deterministic policy here. Branch $B$ saves only eight disclosures. These adverse comparisons are retained; no best policy is selected retrospectively for each task.

Crystal contributes 768 tasks, with 33 positive and 735 negative verdicts: wrapped census uses 6,229 disclosures and wrapped deterministic screening 5,825. RPL contributes 768 tasks, with eight positive and 760 negative verdicts: the corresponding costs are 6,136 and 5,690. The screened wrapper stops 915 negative tasks before census (408 Crystal and 507 RPL). All 41 positive tasks still require all nine rows, totalling 369 disclosures under every policy. The improvement therefore concerns negative verdicts; it leaves the earlier positive-certificate no-saving result intact.

These are overlapping tasks, not independent physical replications. Percentages describe exact accounting on the fixed cohort rather than population effects or confidence intervals. The new wrapper replay is exploratory, not a preregistered new experiment. Public data and aggregate knowledge are withheld from the simulated client; no metered gateway, monetary saving or reduction in radio traffic is demonstrated.
