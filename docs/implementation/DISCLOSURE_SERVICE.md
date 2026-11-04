<a name="heading-implementation-disclosure_service-exact-disclosure-demonstrators-and-controls"></a>


# Exact disclosure demonstrators and controls
<a name="s10-demonstrators"></a>

[Documentation index](../README.md)

**Role:** Detailed software demonstrators, finite controls and verification boundaries; the core supplement retains the required methodological synopsis. **Source:** UPPC P61, S10, Antonio Clim. Documentation for companion version 1.2.0. Source prose retains its existing manuscript/supplement rights; moving it to MD grants no additional licence.

**Path convention:** scientific commands and scientific-file paths below start at the frozen companion's `reproduction/` root unless a different working directory is expressly stated. In a GitHub source checkout, the equivalent working directory is the repository root; the command paths are identical. Run commands from that software root, not from this `docs/` directory. Retained results are not a claim of a fresh execution. References to manuscript sections and statements use their scientific identifiers; the separately supplied review documents contain the essential proofs.

<a name="heading-implementation-disclosure_service-s10-exact-disclosure-demonstrators-and-verification-protocol"></a>

**Reading context.** Section and statement identifiers refer to their original research stages. This note preserves the stated arguments, evidence and limitations. The article and Essential Supplement form a separate review package.


## S10. Exact disclosure demonstrators and verification protocol
**Exact local disclosure demonstrators.** A historical prefix-disclosure simulator implements the finite fifteen-pair domain with a public decoder. Client policies inspect only revealed records and request the next record of a selected configuration. Exact branch enumeration gives expected costs $200/23$ on A and $175/23$ on D, each a ratio $25/23$ against its own certificate. Codec round-trips, invalid-code rejection, prefix order, negative controls and terminal certificates are checked. This simulator recomputes the disclosure transcript and its cost but compares that cost with the fixture's analytically established comparator, identified in its output as `analytically_declared_C_star`. It does not independently optimise over certificates.

A separate demonstrator computes each comparator independently of the policy's stopping test. It uses the fifteen-pair alphabet, exact fractions and ten case configurations built from eight distinct synthetic archives. For each configuration, a separate comparator implementation enumerates all 64 prefix vectors and the possible completed group sums. Rejecting a prefix requires an explicit legal FALSE completion; accepting it requires that every distinct compatible triple of completed sums satisfy GOOD. Across the ten configurations this checks 640 prefixes and examines 1,058 such triples. The latter count records triples actually examined, including early rejection after a counterexample; it is not the size of the full unpruned completion space. Endpoint attainment identifies these finite-alphabet certificates with the square certificates, as proved in Section S5.1.

All three policy branches are enumerated with exact probabilities $8/23,8/23,7/23$, giving 30 branch executions without Monte Carlo estimation. The independently computed minima on A and D are respectively eight and seven, recovering the costs $200/23$ and $175/23$ and ratio $25/23$. The suite also includes the other positive certificate classes and four negative controls. An adverse tariff configuration prices A's last candidate row at 25 and all other rows at one. Its weighted certificate remains eight, whereas the unchanged unit-price mixture costs $584/23$, a ratio $73/23$. With a common setup charge ten on D, the same unchanged mixture costs $405/23$ against comparator 17, a ratio $405/391$. This setup check does not use the retuned optimal probability $q_F$ of Section S5.2. These are exact local software checks of access, decisions and accounting, rather than a deployed service, security proof or measurement of communication benefit.

**Additional mixed-policy and comparator controls.** The new triangle implementation was checked on 1,816 ordinary archives (141 positive and 1,675 negative) and 224 hard-family archives, with 6,120 deterministic-branch executions in total. The ordinary comparator enumeration inspected 68,309 prefixes and the hard-family enumeration a further 8,788. In 112 hard-family cases the rival-first branch actually terminated with the candidate incomplete. These checks include the new probability cut at $3/4$ and preserve exact rational arithmetic; they do not establish a worst-case constant by sampling.

The merged-threshold comparator matched exhaustive prefix enumeration on 2,966 archives (566 positive and 2,400 negative), covering 695,812 prefix states. A separate exact linear-feasibility implementation checked 100 further archives and 15,516 prefix states, including 40 cases with unequal lengths and nonuniform aggregation weights. These controls test an offline optimiser separately from online acquisition. The generalisation checks additionally covered 30 weighted archives and 2,972 prefix vectors, along with finite sharp-witness and margin examples; their exact scope is recorded in the outputs mapped in Section S9.4.

**Negative-certificate controls.** An exhaustive finite-alphabet control enumerated all $5^6=15,625$ three-configuration, two-row archives, including 142 positive archives, over the alphabet

$$
\{(0,0),(0,1),(1,0),(1,1),(3/5,3/5)\}.
$$

 It aggregated compatible completions for 29,791 observed-prefix states. All 23,728 negative certificates reported by the two tests in Lemma S15 were sound on this finite control: 13,858 used fixed support and 9,870 used domination. A further 4,705 states were universally negative on this finite alphabet but were not detected. The tests are thus explicitly sufficient and incomplete. Lemma S15, rather than finite enumeration, establishes their soundness for every legal completion in the stated general model.

The independently written APEX verifier checked all 9,216 policy-task records and 8,970 exported negative witnesses. The independent SAT verifier checked all 6,552 deterministic branch-task records and the exact mixture probabilities. These counts identify verification work on overlapping tasks; they are not counts of independent physical replications. Every claimed saving in Section S11 is an accounting result for the declared fixed replay cohort.
