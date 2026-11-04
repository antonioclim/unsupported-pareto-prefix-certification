[Documentation index](../README.md)

<a name="constructive-policies"></a>

<a name="heading-implementation-constructive_policies-complete-operational-specification-of-the-constructive-policies"></a>


# Complete operational specification of the constructive policies
> Rights: this is manuscript-derived material. Existing manuscript/supplement rights are reserved; moving it under `docs/` does not grant the companion's CC BY documentation licence. Existing component terms govern this reading view.

This is the P61 operational walkthrough, retained with its access restrictions, fallback, negative-stopping scope and verification boundary. The Essential Supplement retains a concise contract and the mixed-policy probability needed by its implementation proof. Main Sections 3.3 and 6 are authoritative for the policies and guarantees. No execution or practical deployment is claimed by this documentation migration.

<a name="heading-implementation-constructive_policies-s7-operational-specification-of-the-constructive-policies"></a>

**Current reader role:** Complete operational walkthrough; the core supplement retains the causal policy contract and implementation proof.

**Reading context.** Section and statement identifiers refer to their original research stages. This note preserves the stated arguments, evidence and limitations. The article and Essential Supplement form a separate review package.


## S7. Operational specification of the constructive policies
This section makes the information available to the constructive policies explicit. Main Sections 3.3 and 6 specify the acquisition rules and their principal guarantees; Sections S3.6 and S6 complete the triangle proof details, while Section S8 gives the arithmetic, storage and sampling bounds. The description below is an implementation guide to those policies.

**Input and access contract.** Public input comprises the labelled configurations, the designated candidate, the common archive length $N$, the fixed row order and the applicable completion domain. The unbounded policy uses $\mathcal U=[0,\infty)\times[0,1]$ and $K\ge3$; the triangle policies use $\mathcal T=\{(c,f):0\le f\le c\le1\}$ and $K=3$. Missing rows admit the stated Cartesian-product completions. A request names a configuration and purchases its next whole row. Candidate records are charged in the same way as rival records. Unit disclosure prices apply to the stated numerical guarantees; main Section 6 also permits an identical compulsory information-free setup charge. Public heterogeneous tariffs require the separately proved priced results.

**State and answer.** Maintain each observed prefix length and its two exact coordinate sums, together with the policy's schedule and private random choices. The complete archive and the cheapest realised certificate are unavailable to the acquiring policy. TRUE means that the observations force both candidate nondomination and unsupportedness for every legal completion. FALSE means that GOOD does not hold. Full census permits exact evaluation of either answer. Scalarisation ties and coordinate-axis weights count as support, so replacing strict comparisons by non-strict or tolerance-based tests changes the predicate.

**Unbounded-domain acquisition, main Section 3.3.**

1. Read the entire candidate and compute its mean. For each rival, acquire consecutive rows until its lower mean corner is P2-safe against that known candidate, or the rival is complete. A completed dominating rival permits FALSE.
2. Classify the useful safe rivals by their northwest or southeast lower-corner orientation. Treat rivals already complete during screening as immediately available witnesses. Independently permute the labels within each useful side and fix a balanced side word before revealing residual values, as specified in main Section 3.3.
3. Visit configurations in that order, purchasing each visited residual chain through its end. After screening and after every subsequent completion, test whether the available complete rivals contain a strict witness pair. Return TRUE at the first such certificate. Empty-side, supported or other unresolved cases use the full-census fallback and exact final evaluation.

**Candidate-census triangle acquisition, main Sections 6.1–6.3.**

1. Read the entire candidate, compute $G=p_c-p_f$ and screen the two rivals to their first P2-safe lower corners. On a positive archive these identify opposite crossing sides. Noncrossing or degenerate cases use exact census fallback.
2. For the deterministic policy, select northwest first when $G\le6-4\sqrt2$, using the exact rational test in main Section 6.2. For the randomised policy, select southeast first with probability $p(G)$ from main equation (C11b), and northwest otherwise. Sample this choice once, after observing $G$.
3. Complete the selected side, then extend the other only until the endpoint criterion of main Theorem 1 certifies TRUE or census is reached. Evaluate unresolved census states exactly. The $12/11$ guarantee applies to the randomised policy under the stated contract and compares with certificates that may leave the candidate partly unread.

**Mixed triangle acquisition, main Theorem 20.** Before purchasing any row, choose the rival-first branch $Q$ with probability $1/12$. On this branch, read both rivals in a fixed public order, then read candidate rows only until the exact endpoint criterion certifies TRUE or census is reached. Evaluate unresolved census states exactly. On the remaining branch, use the candidate-census screening procedure above, but replace its southeast-first probability by

$$
p_{\mathrm{mix}}(G)=\frac{12}{11}\alpha(G),\qquad
\alpha(G)=
\begin{cases}
\displaystyle\frac{(19/3)G-2G^2}{4+G},&0\leq G\leq3/4,\\[4pt]
\displaystyle\frac{87}{80}-\frac{21}{80G},&3/4<G\leq1.
\end{cases}
$$

The first branch choice is independent of the archive. The conditional choice involving $G$ occurs only after candidate census on the candidate-first branch. Thus $Q$ needs no unavailable candidate gap. The high expression is used only when its denominator is nonzero. Both branches use the same exact positive stopping criterion and an exact census fallback for either answer. Theorem 20 proves the $87/80$ positive-input guarantee for this fixed mixture, including comparison with certificates that leave the candidate incomplete. The finite acquisition checks in Section S10 implement all three resulting deterministic branches; the Bernstein certificate is separate proof evidence.

**Optional negative stopping.** The sound tests in Lemma S15 may be checked after every disclosure. They preserve every positive paid path and can shorten negative paths. The archived-data experiments in Section S11 identify exactly which base policies were wrapped: the APEX policies and the earlier Theorem 19 triangle policy, rather than the new Theorem 20 mixture.

**Implementation and verification boundary.** The published companion version 1.1.0 retains the earlier proof-checking programs and the square-domain disclosure demonstrator of Section S10. Its `extensions/P58/` directory supplies the new exact mixed-policy and negative-stopping replay implementations. These programs are finite verification and replay tools; the companion does not constitute a deployed acquisition service. Section S8 assumes rational disclosed coordinates and implements exact comparisons and rational random sampling. The bit bound on those coordinates describes the realised encoding; it does not narrow the public class of unread completions. The policies neither optimise the retrospective comparator nor evaluate the Bernstein proof certificate during acquisition. Those tasks belong to the separate verification procedures and evidence described in Sections S9–S10. All policies must be correct on positive and negative inputs and terminate almost surely; competitive ratios are evaluated on fixed positive archives. Disclosure counts, arithmetic complexity and the independently computed certificate cost consequently have separate meanings in an execution record.

