<a name="heading-research-access_models_and_implementation_boundaries-secondary-access-model-and-implementation-research-notes"></a>

# Secondary access-model and implementation research notes
[Documentation index](../README.md)

These complete passages are routed out of the Essential Supplement. They are
secondary research notes rather than premises required for main Propositions
22–24. The current S4.5 proof, S3.4 barrier and S3.6 threshold proof remain in
the essential supplement. Original section and statement labels below are
historical locators; their nonconsecutive order is intentional. The current
main article determines which claims are promoted for central evaluation.

Prose is derived from the P61 supplementary manuscript. Its existing rights
remain reserved: repository placement grants no new CC BY licence.

<a name="history-and-adverse-scope"></a>

**Current reader role:** Complete secondary access-model and implementation notes; the core supplement retains the arguments needed for main Propositions 22–24.

**Reading context.** Section and statement identifiers refer to their original research stages. This note preserves the stated arguments, evidence and limitations. The article and Essential Supplement form a separate review package.

<a name="heading-research-access_models_and_implementation_boundaries-s3-history"></a>

## S3 History
Exact source lines 1072–1085; SHA-256 `4088c4c5521a78293dfa60a2b8e73dfc494c4aa1cad80b0bc86c8b5801e105aa`.

<a name="supp-s3"></a>

## S3. Upper-bound certificates and adverse analytical controls
<a name="heading-research-access_models_and_implementation_boundaries-s3-1-the-earlier-35-32-randomised-certificate"></a>

### S3.1. The earlier 35/32 randomised certificate
The earlier rule chooses southeast first with probability $2G/(1+G)$ and has a uniform $35/32$ bound. Its complete derivation, equations (C10)–(C11), Table S6 and exact Bernstein data are retained in `docs/history/TRIANGLE_UPPER_BOUND_CONTROLS.md`, under “Earlier 35/32 certificate”. The 4 and 7 leaves verify 288 and 735 coefficients. This is a historical control for a different rule, rather than a premise of the current $12/11$ or $87/80$ proofs. The latter proofs remain in Section S6.

<a name="heading-research-access_models_and_implementation_boundaries-s3-2-retained-exact-certificate-for-the-earlier-873-800-bound"></a>

### S3.2. Retained exact certificate for the earlier 873/800 bound
The former policy $p_{\mathrm{old}}(G)=5G/(4+G)$ has an exact $873/800$ certificate. The complete polynomials, Table S7, 48 leaf boxes and 4,644 coefficients remain in `docs/history/TRIANGLE_UPPER_BOUND_CONTROLS.md`, under “Earlier 873/800 certificate”, with the two original verifier outputs identified there. This certificate is separate from the current candidate-census and mixed policies. Its historical polynomial alias (C11f) must not be confused with the current low-branch polynomial in Section S6.1; both meanings are distinguished in the archived note.

<a name="heading-research-access_models_and_implementation_boundaries-s3-3-the-unsuccessful-9-8-threshold-argument"></a>

### S3.3. The unsuccessful 9/8 threshold argument
The threshold $1/3$ fails the attempted $9/8$ excess-envelope argument: a feasible point of (C9) gives $17/133>1/8$. Its exact parameters are retained in `docs/history/TRIANGLE_UPPER_BOUND_CONTROLS.md`, under “Unsuccessful 9/8 threshold argument”. This disproves that argument, rather than every possible $9/8$ policy or the rule's realised guarantee. The current deterministic proof is Section S3.6.


<a name="historical-control-tail"></a>

<a name="heading-research-access_models_and_implementation_boundaries-s3-controls"></a>

## S3 Controls
Exact source lines 1119–1124; SHA-256 `c692895489ecb7d7cb41eff3e147cf902e8c89b595c03bd3eace748ca4facec7`.

A separate retained control shows that $p(G)=6G/(5+G)$ does not prove $131/120$ through (C8)–(C9): its feasible witness gives excess $1223710/13336987>11/120$. The full exact witness is in `docs/history/TRIANGLE_UPPER_BOUND_CONTROLS.md`, under “Unsuccessful 131/120 envelope”. This is a failure of that envelope bound, not a lower bound on every policy or on the rule's realised worst-case cost.

<a name="heading-research-access_models_and_implementation_boundaries-s3-5-full-candidate-restriction-and-tariff-controls"></a>

### S3.5. Full-candidate restriction and tariff controls
Main Theorem 17 and Corollary 18, proved in Section S2.7, give the full-candidate obstruction, necessary partial-observation probability and positive-tariff extension. In the $N=12$ tariff control, a final candidate row priced at $M>0$ leaves a TRUE certificate of cost $34$, while every candidate-census certificate costs at least $34+M$. These restrictions concern a specified policy class, not a stronger unrestricted lower bound. The 332,235-prefix, seven-instance checker inventory is retained in `docs/history/TRIANGLE_UPPER_BOUND_CONTROLS.md`, under “Full-candidate and tariff controls”.


<a name="access-model-controls"></a>

<a name="heading-research-access_models_and_implementation_boundaries-s4-access-controls"></a>

## S4 Access Controls
Exact source lines 1167–1332; SHA-256 `4052a403e3227d1b6b5329f56e936d0cef4637745edac41a2cda0cca0dc8da9f`.

<a name="supp-s4"></a>

## S4. Access rules, legal simulation and reduction obstructions
<a name="heading-research-access_models_and_implementation_boundaries-s4-1-whole-row-encoding-does-not-preserve-prefix-certificates"></a>

### S4.1. Whole-row encoding does not preserve prefix certificates
A complete row from a known finite alphabet can be encoded as one integer-valued variable, with its whole pair returned by a public decoder. Such an encoding preserves bundling and a fixed row price. It does not enforce prefix access. The following continuous-triangle example shows that the resulting retrospective certificate can be strictly cheaper.

Let $K=N=3$, with independent missing rows in $\mathcal T=\{(c,f):0\leq f\leq c\leq1\}$. The candidate has three identical rows $(99/100,299/1000)$. The northwest group has rows $(0,0),(9/10,9/10),(9/10,9/10)$, and the southeast group has three copies of $(1,0)$. All observations have unit cost.

**Proposition S7.** On this archive, the minimum positive prefix certificate costs eight, whereas the minimum certificate using arbitrary whole-row subsets costs seven.

First, any certificate must reveal all candidate rows. If at most two are revealed, complete its missing rows with $(0,0)$ and leave the rivals at their actual values. Under weights $(1,1)$, the candidate's scalar value is at most $2(1289/1000)/3<1$. The actual rivals have scalar values $6/5$ and one, so this completion supports the candidate and is FALSE. After candidate census, every southeast row is mandatory: fill its unobserved rows with $(0,0)$; with at most two observed rows its mean $(r/3,0)$ strictly dominates the candidate. Finally, some northwest row equal to $(9/10,9/10)$ must be observed; otherwise all its unknown rows can be zero, again giving domination.

These necessities require at least seven arbitrary whole-row observations. Conversely, reveal the candidate and southeast group completely and only the northwest group's second row. Its attainable lower and upper corners are $(3/10,3/10)$ and $(29/30,29/30)$. The former has failure $3/10>299/1000$, so it cannot dominate the candidate; the southeast cost one is also safely above the candidate cost. A mixture with northwest weight $61/200$ and southeast weight $139/200$ gives

$$
\frac{61}{200}(29/30,29/30)+\frac{139}{200}(1,0)
=(5939/6000,1769/6000).
$$

The candidate is $(5940/6000,1794/6000)$, so both mixture gaps are strictly positive: $1/6000$ and $1/240$. This proves a robust TRUE certificate of cost seven. Monotonicity under further observations shows that precisely the six northwest subsets containing at least one of its two nonzero rows work, together with the compulsory six candidate and southeast rows.

Under prefix access, obtaining either nonzero northwest row first requires its preceding zero row. Thus at least eight queries are necessary. The prefix $(3,2,3)$ is sufficient: its northwest lower corner is still $(3/10,3/10)$, while its upper corner decreases to $(19/30,19/30)$. The same strict witness remains valid. The only TRUE prefixes are $(3,2,3)$ and $(3,3,3)$.

This example concerns the continuous triangle, not either fifteen-symbol alphabet. It defeats immediate equality of the unrestricted-variable and prefix comparators. It does not exclude a more sophisticated reduction or a one-way competitive upper bound from a legally simulated unrestricted policy. Both the legal simulation and its denominator comparison require proof.

The same classification holds analytically on the known five-symbol joint alphabet

$$
\mathcal S_{\mathrm{free}}=\{(0,0),(1,1),(99/100,299/1000),(9/10,9/10),(1,0)\}.
$$

Every actual row belongs to this set. The necessary FALSE completions above use actual rival rows or $(0,0)$; the sufficient corner constructions use the legal whole endpoints $(0,0)$ and $(1,1)$. Thus no continuum assumption is needed for the discrepancy. A single five-valued integer variable can represent each whole row exactly, yet it still omits the prefix prerequisites. This finite-alphabet corollary is analytic; the native checker below enumerates observation states in the continuous triangle rather than every archive over this alphabet.

The example was derived analytically before its exploratory exact Python check. That initial inline check was retained after execution. A separately retained canonical checker was subsequently frozen before its first execution and reproduced identically in an isolated copy. Its 64 prefix states and 512 arbitrary subsets confirm the complete classification above, with legal FALSE completions for all 62 and 506 rejected states respectively. This is a mathematical audit check, not a new radio experiment or preregistered discovery.

<a name="heading-research-access_models_and_implementation_boundaries-s4-2-legal-prefetch-and-comparator-transfer"></a>

### S4.2. Legal prefetch and comparator transfer
This section compares two observation rules on the same admissible archive class $\mathcal D$ and the same Boolean predicate. Each of $K$ labelled groups, including the candidate, has $N$ fixed ordered rows. A row has a fixed public price $w_{gj}>0$, determined by its group and position independently of hidden values. The unrestricted rule permits any unread whole row to be requested; the prefix rule permits only the next unread row of a group. No candidate observation or predecessor payment is free.

For a positive archive $I$, write $C_{\mathrm{free}}^*(I)$ and $C_{\mathrm{prefix}}^*(I)$ for the minimum prices of robust TRUE certificates under the respective rules. Both certificates quantify over the same completions in $\mathcal D$. Assume that the positive evaluation class is nonempty and $C_{\mathrm{free}}^*(I)>0$ on every scored archive, as holds when the predicate also has a legal negative input. Algorithms are correct and terminate almost surely on every legal positive and negative input. For $X\in\{\mathrm{free},\mathrm{prefix}\}$, define
$$
R_X^*=\inf_{A\in\mathcal A_X}
\sup_{I\in\mathcal D:\mathrm{GOOD}(I)}
\frac{\mathbb E\operatorname{Cost}_A(I)}{C_X^*(I)},
$$
where $\mathcal A_X$ contains the zero-error randomised policies with observation rule $X$. Thus the expected cost is evaluated on each fixed positive input before taking the input supremum. Both classes use the same public prices and all-input correctness requirements; only the legal observation rule differs. These assumptions are essential when comparing the two optima.

For a set $Q$ of rows, let $\operatorname{cl}(Q)$ contain every predecessor of every row in $Q$, including that row. Put
$$
P_g(j)=\sum_{k=1}^{j}w_{gk},
\qquad
\Gamma(w)=\max_{g,j}\frac{P_g(j)}{w_{gj}}.
$$

**Lemma S8 (Faithful legal prefetch).** Under these assumptions,
$$
C_{\mathrm{free}}^*(I)
\leq C_{\mathrm{prefix}}^*(I)
\leq \Gamma(w)C_{\mathrm{free}}^*(I).
$$
For every unrestricted evaluator $A$, a legal prefix evaluator $\widehat A$ can be constructed such that, on the same fixed input and coupled private coins,
$$
\operatorname{Cost}_{\widehat A}(I,\omega)
\leq \Gamma(w)\operatorname{Cost}_{A}(I,\omega).
$$
Consequently, for the same admissible input class, prices, predicate and zero-error randomised policy requirements,
$$
\frac{R_{\mathrm{free}}^*}{\Gamma(w)}
\leq R_{\mathrm{prefix}}^*
\leq \Gamma(w)R_{\mathrm{free}}^*.
$$

*Proof.* Write $W(Q)=\sum_{(g,j)\in Q}w_{gj}$. For each group touched by $Q$, let $m_g$ be its greatest requested position. Then
$$
W(\operatorname{cl}(Q))
=\sum_g P_g(m_g)
\leq\Gamma(w)\sum_g w_{g m_g}
\leq\Gamma(w)W(Q).
$$
A prefix certificate is also an unrestricted certificate. Conversely, the prefix closure of any unrestricted certificate contains its observations and therefore still forces TRUE. Applying the displayed inequality to a minimum unrestricted certificate proves the certificate bounds.

Run an internal copy of $A$. When it requests row $(g,j)$, reveal all still missing predecessors through $j$ in their legal order. Cache their values, but pass each value to the internal copy only when that copy explicitly requests it. A request already covered by the cache requires no further disclosure. The internal copy therefore sees exactly the transcript it would see under unrestricted access, with the same private coins. Ignoring optional earlier sound stopping, the paid rows are precisely the prefix closure of its requested set. The cost bound follows pointwise.

The simulation inherits all-input correctness and almost-sure termination. Its real observations contain every observation used by the internal copy, so a sound conclusion remains sound. Any additional early stop must itself be justified against all compatible completions. The construction does not use a positive-answer promise.

If $A$ has an expected upper bound $\rho C_{\mathrm{free}}^*(I)$ on every fixed positive archive, the simulation satisfies
$$
\frac{\mathbb E\operatorname{Cost}_{\widehat A}(I)}
     {C_{\mathrm{prefix}}^*(I)}
\leq
\Gamma(w)\rho
\frac{C_{\mathrm{free}}^*(I)}
     {C_{\mathrm{prefix}}^*(I)}
\leq\Gamma(w)\rho.
$$
Taking infima gives the upper comparison. For the reverse comparison, any prefix policy is also a valid unrestricted policy with the same realised cost. The certificate inequality gives
$$
\frac{\mathbb E\operatorname{Cost}_{B}(I)}
     {C_{\mathrm{free}}^*(I)}
\leq
\Gamma(w)
\frac{\mathbb E\operatorname{Cost}_{B}(I)}
     {C_{\mathrm{prefix}}^*(I)}.
$$
Taking the input supremum and policy infimum proves the lower comparison. Infima need not be attained. $\square$

At unit prices $\Gamma(w)=N$. If $\alpha\leq w_{gj}\leq\beta$, then $\Gamma(w)\leq1+(N-1)\beta/\alpha$. For $N\geq2$, arbitrary positive tariffs admit no bound on $\Gamma(w)$ depending only on $N$: taking $w_{g1}=M$ and $w_{g2}=1$ gives $\Gamma(w)\geq M+1$. For $N=1$, $\Gamma(w)=1$. A common compulsory uninformative setup charge can be included in both accounts: $\Gamma(w)\geq1$ preserves the same inequalities for the total costs.

The lemma is a sufficient generic comparison, not a claim that the target optima differ by $\Gamma(w)$. A source lower bound $L$ transfers through this argument only as $L/\Gamma(w)$, provided its input, price and randomisation quantifiers coincide. Deterministic extremal-price sharpness cannot be substituted for fixed-price randomised sharpness. The cost overhead may be smaller for a particular policy or archive. In particular, the inequality $C_{\mathrm{free}}^*\leq C_{\mathrm{prefix}}^*$ helps an upper transfer; a strict comparator gap does not by itself disprove one.

**Example S9 (A minimum free certificate need not give a minimum prefix path).** Consider the unit-price archive of Section S4.1, in the continuous triangle or its specified five-symbol joint alphabet. Its candidate rows are all $(99/100,299/1000)$, the northwest rows are $(0,0),(9/10,9/10),(9/10,9/10)$, and the southeast rows are all $(1,0)$. Section S4.1 proves
$$
C_{\mathrm{free}}^*=7,
\qquad
C_{\mathrm{prefix}}^*=8.
$$
Either nonzero northwest row, together with candidate and southeast census, is a minimum free certificate.

An unrestricted evaluator can request the third row of the fixed northwest-labelled group first, then all candidate and southeast rows, test robust TRUE and otherwise finish census. This defines a sound evaluator on the entire domain; the group name here identifies a fixed label in the displayed archive. Its cost on that archive is seven. Faithful prefetch first buys all three northwest rows, after which candidate and southeast census remain compulsory. Its cost is therefore nine against prefix optimum eight. Checking TRUE after each legal disclosure cannot remove that excess: the two compulsory censuses are still incomplete during the early northwest queries.

Requesting northwest row two first instead yields a seven-row free certificate whose closure has cost eight. Thus the same archive permits either exact cancellation of the comparator gap or a prefix ratio $9/8$, depending on the unrestricted request order. Neither evaluator is asserted to be globally one-competitive under unrestricted access. These are analytic consequences of the complete Section S4.1 certificate classification; no additional numerical execution is used.

**Example S10 (An ordered Pareto front does not determine unsupportedness).** Let both coordinates be minimised. Fix $L=(0,1)$ and $R=(1,0)$, and compare $p^-=(2/5,2/5)$ with $p^+=(3/5,3/5)$. Both triples have the same ordered nondominated labels $L,p,R$. Weights $(1,1)$ strictly support $p^-$, whose score is $4/5$ against the rivals' score one. In contrast, $(L+R)/2=(1/2,1/2)$ is strictly below $p^+$ in both coordinates. For every nonzero nonnegative weight, the average rival score is then strictly smaller than the candidate score, so some rival improves it. Thus GOOD is FALSE in the first triple and TRUE in the second.

This compares the information in the combinatorial output, rather than claiming that the initial metadata or paid actions of two models coincide. Returning all point coordinates would distinguish the cases. The example does not rule out a richer reduction; such a reduction must also account for the numerical information it acquires, its legal row prerequisites and the resulting certificate denominator. The observation is elementary and is not a historical novelty claim.

<a name="heading-research-access_models_and_implementation_boundaries-s4-3-two-obstructions-to-immediate-geometric-reductions"></a>

### S4.3. Two obstructions to immediate geometric reductions
The following constructions separate outputs and certificate denominators. They do not rule out reductions that retain additional information.

**Pareto membership does not determine GOOD.** Work in the square with three configurations and four rows. All four candidate rows are $(1/2,1/2)$. The observed first three northwest rows are $(0,5/6)$, and the first three southeast rows are $(5/6,0)$. At prefix $(4,3,3)$ the feasible mean regions are

$$
\{(1/2,1/2)\},\qquad
[0,1/4]\times[5/8,7/8],\qquad
[5/8,7/8]\times[0,1/4].
$$

Every completion has the same three Pareto labels: each rival crosses the candidate, and the two rival rectangles cross each other. Complete both unread rows with $(0,0)$. Their means become $(0,5/8)$ and $(5/8,0)$, whose equal mixture $(5/16,5/16)$ strictly dominates the candidate. The candidate is therefore unsupported and GOOD holds. Instead complete both unread rows with $(1,1)$. The rival coordinate sums are then $9/8$, whereas the candidate sum is $1$, so weights $(1,1)$ support the candidate and GOOD fails. A procedure returning only the known Pareto-membership set cannot distinguish these completions. At least one further disclosure is required for GOOD.

**Complete means do not determine the prefix comparator.** Consider the three-row archive in Section S4.1. Candidate rows are all $(99/100,299/1000)$, southeast rows are all $(1,0)$, and northwest rows are

$$
(0,0),\quad(9/10,9/10),\quad(9/10,9/10).
$$

All six candidate and southeast rows are compulsory, and the first informative northwest row is its second row. The cheapest TRUE prefix is $(3,2,3)$, of cost eight. Reorder only the northwest sequence as

$$
(9/10,9/10),\quad(0,0),\quad(9/10,9/10).
$$

The complete mean vectors and initial square mean regions are unchanged. Now $(3,1,3)$ is TRUE, of cost seven. The lower bound from Section S4.1 still requires the six compulsory rows and one nonzero northwest row, so seven is exact. Equivalently, direct use of the endpoint theorem in main Section 2 over all $4^3$ prefixes of each archive gives precisely these minima. Both archives lie in the triangle as well as the square, so endpoint transfer preserves the comparison between those domains.

Thus an atomic-point representation that retains only final means and initial regions cannot preserve the prefix denominator exactly. It must retain ordered records or prove an explicit distortion bound. The accompanying rational checker independently enumerates the 128 prefix states and verifies the two explicit four-row completions, including scalarisation ties and axis weights. The universal Pareto-label statement above follows from rectangle separation, rather than from sampling completions.

<a name="heading-research-access_models_and_implementation_boundaries-s4-4-boundaries-of-positive-input-policy-extension"></a>

### S4.4. Boundaries of positive-input policy extension
Positive-only evaluation matters. For Boolean OR on two unit-price bits, compare the full class $\{0,1\}^2$ with $\{00,10,11\}$. Robust TRUE observations coincide. On the smaller class, reading the first bit suffices on every input. On the larger class's negative input $00$, both bits are necessary. Therefore an extension cannot preserve all input costs, despite preserving positive costs.

Certificate invariance also matters. For predicate $x_1\land\neg x_2$, restricting the full bit-pair class to $\{00,10\}$ makes the first bit a cost-one positive certificate on $10$. The full class requires both bits there. These Boolean examples delimit the general argument; they are not additional Pareto results.

Finally, decidable membership is an explicit implementation assumption. The finite alphabets and inequality-defined bands used here satisfy it under exact arithmetic. An arbitrary unspecified domain may require a membership oracle. Correlated rows, different tariffs, informative metadata, changed access rules or noisy observations require separate arguments; endpoint inclusion alone does not establish this extension in those models.

As in main Section 7, a paid-query transcript records the ordered queried locations and their revealed values, excluding the private random tape and internal computation. On a fixed archive there are finitely many such transcripts. Extension between nonnested endpoint-containing domains requires decidable consistency tests for both domains and a shared nonempty positive evaluation set. Certificate equivalence itself permits empty certificates; certificate-normalised ratios require positive denominators. The product-domain Pareto problem has an all-equal negative archive, so an empty transcript cannot certify TRUE.


<a name="auxiliary-transfer-boundaries"></a>

<a name="heading-research-access_models_and_implementation_boundaries-s4-auxiliary-extensions"></a>

## S4 Auxiliary Extensions
Exact source lines 1392–1397; SHA-256 `72d3fffee2534c2db05d6824d9efb5b59503a58c26f4640a4109a8736c089d31`.

Public dependence can also be quantified when its structure is explicit. If each archive is partitioned into public consecutive blocks of identical rows and distinct blocks admit Cartesian-product completions, rounding an observed prefix to the end of its last touched block identifies its block-model certificate with an independent-row certificate. The resulting comparator distortion is at most the largest block length at unit prices, and has an explicit price-dependent factor otherwise. Both bounds can be attained on the three-configuration triangle (Supplementary Proposition S11).

For independently completable endpoint-containing row domains in $[0,1]^d$, the endpoint test also accommodates unequal archive lengths and public positive aggregation weights. Helly's theorem ([DGK63](../REFERENCES.md#ref-dgk63)) on the supporting-weight simplex yields a sharp bound of $d$ rival witnesses (Section S5.6). These aggregation weights affect the means and differ from disclosure prices. This certificate extension does not transfer the two-dimensional numerical acquisition ratios: in $[0,\infty)\times[0,1]^{d-1}$ with $d\ge3$, a robust TRUE certificate can leave the candidate incomplete (Section S5.8). Dependence that removes endpoint completions likewise requires a new certificate analysis, except where a separate sufficient test or an explicit distortion argument applies.

An exact dimensional transfer is available under a stronger structural condition. Suppose every legal row has a public representation $z=b+My$, where $y$ is planar, $M\geq0$ has no zero row and contains positive multiples of both coordinate axes as rows. If latent and full archives correspond bijectively with the same completion information, aggregation weights, query order and prices, then every prefix verdict and $C^*$ are preserved (Theorem S18). Main Theorem 20 consequently transfers when the latent model also meets all its hypotheses, including the three-configuration, equal-length, uniform-aggregation, unit-price and triangle or endpoint-subdomain assumptions. This covers arbitrarily many recorded criteria determined by two anchors; it does not cover arbitrary independent criteria or a representation fitted after observing hidden rows.


<a name="extended-acquisition-model-comparison"></a>

<a name="heading-research-access_models_and_implementation_boundaries-s4-extended-comparison"></a>

## S4 Extended Comparison
Exact source lines 1411–1432; SHA-256 `037231ee570b1fee626ca12d0da72ef55cbef5d1caff9ac01ad40ac9dd615473`.

<a name="heading-research-access_models_and_implementation_boundaries-s4-6-extended-comparison-with-other-acquisition-models"></a>

### S4.6. Extended comparison with other acquisition models
**Priced information and instance complexity.** The certificate benchmark follows Charikar et al. (2002), randomised AND/OR evaluation (Laber, 2003, 2008) and the certificate-sensitive analyses of Cicalese and Laber (2011) and Cicalese and Milanič (2008). The remark in main Section 2 identifies it with the input-specific optimum of a globally correct policy, as in deterministic instance complexity ([GKN20](../REFERENCES.md#ref-gkn20); [LM26](../REFERENCES.md#ref-lm26)). Blanc, Lange and Tan ([BLT21](../REFERENCES.md#ref-blt21)) analyse priced Boolean queries under the uniform input distribution, allowing error and comparing expected cost with that of an optimal strategy. Their influence-based guarantee concerns this distributional benchmark; here correctness is exact and cost is normalised by the cheapest realised prefix certificate. Our performance supremum covers positive archives, while correctness covers both answers. Randomised policies retain the robust certificate denominator, unlike bounded-error instance optimality normalised by randomised certificate complexity. On a finite alphabet, each whole row can be treated as one variable (Cicalese & Milanič, 2008), but bit encoding alone does not preserve whole-record costs, legal bit patterns or predecessor payments. Section S4.2 proves an unrestricted-query prefetch comparison with factor
$$
\Gamma(w)=\max_{g,j}\frac{\sum_{k\le j}w_{gk}}{w_{gj}},
$$
which equals $N$ at unit prices. This comparison accounts for the access difference but does not yield the sharp ratios above. Feder et al. (2003) study interval-constrained inputs whose exact values can be purchased to determine a selection value to prescribed precision. Known prices and adversarial fixed archives also distinguish this model from unknown acquisition costs (Nadimpalli et al., 2025) and stochastic certification under a distribution supported on positive inputs (Ghuge et al., 2026).

**Sorted access and certificate discovery.** Fagin, Lotem and Naor's NRA algorithm ([FLN03](../REFERENCES.md#ref-fln03)), Section 8.1, uses no random access and may identify the top objects without their exact scores. Its lists are sorted by revealed grades, so the last observed grade constrains every unseen entry. Our archives have arbitrary fixed row orders, and the joint predicate concerns vector means rather than one monotone aggregate. Mandatory predecessors and decisions from incomplete scores therefore have direct precedents, while the geometric verifier and the exact bounds require separate analysis. Blanc et al. ([BKLT22](../REFERENCES.md#ref-bklt22)) study a complementary certification problem: the input is supplied and queries evaluate an unknown Boolean function; here the predicate is specified and queries disclose the unknown archive.

**Ordered certification and partial evaluation.** Next-best elicitation already compares prefix-query cost with hindsight evidence for necessarily Pareto-optimal and rank-maximal matchings ([HMSS21](../REFERENCES.md#ref-hmss21); [Pet22](../REFERENCES.md#ref-pet22)). These problems concern ordinal preference rankings and their legal completions, rather than unsupportedness of a designated vector-mean point. Shah and Yu (2026) compare next-best preference queries with the shortest realised prefix sequence determining all tied voting winners. Their access order and retrospective benchmark are close to ours, while the output is a voting outcome and legal completions are preference rankings. Yu et al. (2026, Theorem 3) recover a conformal calibration quantile from prefix-ordered acceptance verdicts and prove the optimal deterministic ratio $2-1/(n-k+1)$ for finite thresholds when $k\ge n-k+1$, where $n$ is the calibration sample size and $k$ the quantile rank. Their certificate and cost statements hold for fixed verdict tables; exchangeability enters the separate coverage guarantee. Sui and Tang (2026) give an exact top-$k$ certificate for information-disjoint Cartesian loss intervals and a polynomial-time hindsight optimiser for unit-cost empirical Expected Shortfall evaluations. Their exact point queries are freely selectable. They also prove search lower bounds separating online acquisition from hindsight optimisation; the ratios reported for benchmark replays are empirical. The present theorems analyse a designated vector-mean candidate's joint nondomination and unsupportedness, including exact deterministic and randomised ratios on the unbounded domain, diagonal-band transitions and the candidate-observation obstruction on a fixed alphabet.

**Incremental refinement.** Tseng and Kirkpatrick (2011) give a direct precedent for prefix revelation through leading bits of numerical inputs and geometric certificate discovery. Their presentation-based denominator differs from the cheapest realised positive prefix here. Gupta et al. (2016) study repeated queries that narrow uncertainty intervals. Our convex row domains fit that state-level pattern: after $s$ rows in $\mathcal T_d$, the exact feasible mean region is $L_j(s)+(N-s)\mathcal T_d/N$, so successive regions are nested and different-configuration updates commute. The missing ingredients for the present predicate are its verifier, attainable prefix geometry and acquisition bounds. Long uninformative prefixes followed by an informative update are also established lower-bound devices; Meißner (2018, Theorem 4.37) uses them in repeated-update spanning trees. The fixed-alphabet construction here realises a particular ambiguity through legal bounded vector rows and proves its entire TRUE-prefix set.

**Geometric retrieval.** Bruce et al. (2005) compare maximal-point and convex-hull retrieval with minimum sufficient realised update sets. Charalambous and Hoffmann (2013) prove NP-hardness of minimum verification for unrestricted planar uncertainty regions; coordinate-product regions admit a sharp three-update online bound and polynomial-time minimum verification (Charalambous, 2016, Theorems 6.12 and 6.38, respectively). After reversing the objective order, the closed-rectangle nondomination part of our endpoint criterion is the corresponding maximality test. More recent bounds include $\Theta(r)$ hull retrievals with $O(r\log^3n)$ time for constant-complexity polygonal regions (de Berg et al., 2025), and at most $5r$ Pareto-front retrievals for rectangles (de Berg et al., 2026). Here $r$ is the respective minimum sufficient retrieval count. Those retrievals collapse a whole point region; a query here reveals only its next vector row. Sections S4.1 and S4.3 also give two concrete obstructions to immediate reductions: the same Pareto labels can coexist with both answers to GOOD, and reordering rows while preserving every complete mean can change the prefix comparator from eight to seven.

**Search and ordinal reductions.** The terminal-choice balancing in main Section 4 is the priced two-box search mechanism (Angelopoulos et al., 2016); its geometric realisation and exclusion of cheaper certificates supply the application here. Bichromatic sorting instead purchases comparisons and certifies an entire order (Goswami & Jacob, 2024), whereas one value disclosure here settles comparisons with every previously disclosed value and a single strict crossing pair suffices. Order-invariant reductions have a long history (Fischer, 2004; Moran et al., 1985). In particular, the causal Ramsey proof adapts the discretised next-action architecture of Baleshzar et al. (2020, Section 3.1). Main Section 3 supplies the additional expected-stopping-cost, legal-continuation and paid-prefix arguments. The cardinal-versus-ordinal online model of Gravin et al. (2023) has an externally supplied arrival order, unlike adaptive choice of the next hidden label here.

**Scalarisation and certificate geometry.** The limitations of weighted sums for recovering nondominated points are established background (Das & Dennis, 1997). Our convention permits zero coordinates in a nonzero weight vector and counts scalarisation ties as support (Könen & Stiglmayr, 2025). The supporting-weight interval argument behind the two-witness criterion is given in full in Main Lemma 2, including the axis and equality cases. The acquisition results require further analysis of attainable prefix certificates, robust nondomination and the observations needed to discover a certificate under the prescribed access rule. The $d$-witness extension uses classical Helly theory; its role here is to bound the number of rival prefixes required in the exact retrospective certificate, with a matching finite example (Section S5.6).

**Objective reduction.** Preserving dominance under objective omission or approximation is an established subject ([BZ09](../REFERENCES.md#ref-bz09)). Low-rank multi-objective linear programming can also reduce the objective dimension by changing the ordering cone ([LZ26](../REFERENCES.md#ref-lz26)). These geometric reductions do not by themselves preserve unsupportedness under our axis-weight convention or a paid-prefix observation model. Theorem S16 specialises classical convex geometry to sparse supporting weights and exact scalar feasibility for three alternatives. Theorem S18 supplies the additional public row and completion correspondence needed to preserve the information and comparator costs. Proposition S19 gives sufficient error-margin conditions; Proposition S17 rules out universal compression by nonnegative affine aggregation. No general dimensional-reduction method or new higher-dimensional minimax constant is asserted.


<a name="original-operational-specification"></a>

<a name="heading-research-access_models_and_implementation_boundaries-s7-operational"></a>

## S7 Operational
Exact source lines 2283–2303; SHA-256 `64ffc3dd47e76d1e3230c25609508fdba7806b4fff1bfdad77481cdf094870ad`.

<a name="supp-s7"></a>

## S7. Operational specification of the constructive policies
The public input, next-whole-row access contract, exact prefix state and strict TRUE criterion are those of main Sections 2 and 3. A policy observes neither the hidden archive nor the cheapest realised certificate. Unit row prices underlie the numerical triangle bounds; a common compulsory information-free setup charge is permitted, whereas arbitrary tariffs require separately proved results. Equation (C11b), also used in Section S8, refers to main Theorem 19.

Main Section 3.3 specifies unbounded-domain acquisition, and main Sections 6.1–6.4 specify the candidate-census and mixed triangle policies. The complete operational walkthrough is retained in `docs/implementation/CONSTRUCTIVE_POLICIES.md`. All variants preserve strict scalarisation comparisons and exact full-census fallback; scalarisation ties and coordinate-axis weights count as support. The mixed policy chooses its rival-first branch $Q$ with probability $1/12$ before any observation. Only its candidate-first branch observes $G$ and then uses the conditional probability

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


<a name="separate-retrospective-comparator"></a>

<a name="heading-research-access_models_and_implementation_boundaries-s8-retrospective-comparator"></a>

## S8 Retrospective Comparator
Exact source lines 2334–2335; SHA-256 `2ec3abb783f15ded7318d5fc5470ba5641835bd68fee272c26261a8fe075a09e`.

The retrospective comparator is a separate algorithm. Section S1.1 merges monotone witness-threshold streams and computes an exact optimum in $O(KN^2\log K)$ rational operations and $O(KN)$ space for equal lengths, with positive public disclosure tariffs. With arbitrary configuration lengths $n_g$ and positive normalised aggregation weights, its bound is $O((n_A+1)M\log K)$, where $M=\sum_g(n_g+1)$, and its storage is $O(M)$. These are full-archive computations; their access to hidden rows cannot be supplied free to an acquiring policy. Section S5.6 states the distinct fixed-dimensional witness and comparator extensions.


