<a name="heading-research-mathematical_extensions_p61-complete-p61-mathematical-extensions-and-controls"></a>

# Complete P61 mathematical extensions and controls
[Documentation index](../README.md)

<a name="p61-s5-full"></a>

This preserves the complete S5 of the audited P61 source, including the additional results now outside the essential review route. The compact review supplement separately contains complete statements and proofs of S16--S19 with their necessary endpoint and strict-mixture bridges. Repetition here records provenance; the optional earlier developments are not premises omitted from those core proofs. No new execution or external peer review is asserted by this migration.

Rights: manuscript-derived prose, mathematics and bibliography retain their existing rights. Repository placement grants no additional CC BY licence.

**Current reader role:** Complete earlier S5, including secondary developments; S16–S19 and their prerequisites have complete proofs in the Essential Supplement.

**Reading context.** Section and statement identifiers refer to their original research stages. This note preserves the stated arguments, evidence and limitations. The article and Essential Supplement form a separate review package.

<a name="supp-s5"></a>

## S5. Mathematical extensions and information-utility controls
<a name="heading-research-mathematical_extensions_p61-s5-1-bounded-numerical-examples-and-finite-representations"></a>

### S5.1. Bounded numerical examples and finite representations
Table S8 gives exact values for $N=6$ in the bounded interval of the square acquisition bracket. Its first numerical column also equals the exact unbounded randomised ratio.

Table S8. Illustrative lower and upper bounds for bounded domains at $N=6$.

| $K$ | Bounded lower bound | Bounded upper bound |
|---:|---:|---:|
| 6 | $181/126$ | $181/96$ |
| 16 | $147/62$ | $147/52$ |
| 36 | $961/306$ | $961/276$ |

The fifteen-pair row alphabet is $\mathcal C\times\mathcal F$, where $\mathcal C=\{0,3/8,5/8,7/8,1\}$ and $\mathcal F=\{0,7/8,1\}$.

**Finite-domain square result.** If every row independently ranges over this known full product alphabet, the global $K=N=3$ competitive optima are $25/23$ randomised and $9/8$ deterministic. The same equalities hold on the uniform eighth grid and on any larger coordinate alphabets within the unit square that contain these levels.

Both whole endpoints $(0,0)$ and $(1,1)$ belong to each stated domain. At every legal prefix, filling missing rows with these endpoints attains all corner configurations needed by (Q2); monotonicity supplies the converse implication. Thus the exact TRUE-prefix sets agree with those in the square, even though intermediate points of each mean rectangle need not be attainable. Both fixed A/D archives from Section S1.6 are legal in the fifteen-pair product. Their TRUE-prefix lists and certificate costs eight and seven are preserved, as is their shared history before the distinguishing tail. The same fixed-world lower inequalities therefore hold for every policy correct on the entire finite domain. Conversely, the complete square policies remain valid and keep their upper bounds there. This proves the stated global finite-domain equalities, without a positive-family promise or Ramsey homogenisation.

All fifteen pairs are admissible, including pairs absent from the witnesses. A fixed public joint dictionary represents a complete numeric row by a four-bit index; the unused sixteenth code is invalid. Separate coordinate indices require three plus two bits. On the uniform eighth grid each coordinate has nine levels, requiring four index bits including endpoint one. These are exact numeric payload counts. Configuration identity, row numbering, headers, integrity, retries, processing and radio energy remain outside this count. The alphabet and decoder are identical in both worlds and reveal no outcome flag. These payload counts do not establish a minimum bit budget. The separate minimal common-alphabet theorem in Section S2.3 concerns existence of GOOD and persistent acquisition overhead, not this particular product-alphabet coding.

This finite closure does not transfer every ordinal theorem to a prescribed alphabet. A separate explicit $K=6,N=2$ family permutes two left and three right types among fixed labels. Its raw coordinates fit a five-bit dyadic representation with cost cap three, strict mixture gaps $1/144$ and certificate nine. A numeric threshold recognises the good left type. Independent searches reveal the good endpoints in expected $3/2+2=7/2$ tails, giving total cost $21/2$ and ratio $7/6$, matched on that twelve-archive family. The ordinal calculation is $65/54$. Perturbing only final competitor rows coordinatewise by at most $1/288$ retains the family ratio and witness margin at least $1/192$. These are family-evaluation results with full-domain correctness. They do not contradict the distinct global $K=N=3$ theorem or supply a general precision-dependent minimax formula.

<a name="heading-research-mathematical_extensions_p61-s5-2-exact-common-setup-accounting-for-the-square"></a>

### S5.2. Exact common setup accounting for the square
Throughout this section $K=N=3$ and missing rows range independently over the closed unit square. Policies A and B and their four positive certificate classes are defined in Section S1.6. The calculation here uses those complete blind policies and includes the same fixed raw-prefix payments.

A common compulsory setup charge changes the exact ratio rather than merely preserving an upper guarantee. Suppose a public $F\geq0$ conveys no information and is charged once to both policy and certificate, in addition to unit disclosures. The comparator is $F+C_B^*$. Choose A with probability $q_F=2(F+8)/(3F+23)$ and B otherwise. The same certificate classes above give the exact optima

$$
R_{\mathrm{rand},B}^*(F)=1+\frac{2}{3F+23},\qquad
R_{\mathrm{det},B}^*(F)=1+\frac{1}{F+8}.
$$

Indeed the cost-seven and partial-candidate cost-eight excess ratios balance at $2(1-q_F)/(F+7)=q_F/(F+8)$. The full-candidate cost-eight class has excess at most $(1-q_F/2)/(F+8)$, which is smaller because $q_F>2/3$. Census certificates have ratio at most one. The fixed A/D archives give the matching lower $\max\{1+q/(F+8),1+(2-2q)/(F+7)\}$. Their ratio-averaging prior becomes $(q_F,1-q_F)$, while the normalised raw-cost prior remains $(2/3,1/3)$ with Bayes total $F+25/3$. The deterministic first-choice lower and the cost-seven screening policy followed by census give the second equality. These exact formulas also hold on the fifteen-pair alphabet, which contains both hard archives. They do not automatically hold on restricted domains excluding those archives. A ratio approaching one as $F$ grows reflects a larger common denominator, not reduced information or energy expenditure.

<a name="heading-research-mathematical_extensions_p61-s5-3-endpoint-attainment-and-deadline-domains"></a>

### S5.3. Endpoint attainment and deadline domains
Endpoint attainment is substantive. For $M$ packets with strictly positive successful delivery times and the deadline objectives defined in Section S5.5, the exact row domain has $f=k/M$ and $f<c<1$ for $k<M$, together with $(1,1)$ for $k=M$. Its closure contains $(0,0)$ but the row is unattainable. Take $M=100,N=3$: candidate rows all $(3/5,49/100)$, group $C$ rows all $(51/100,1/2)$, and group $B$ rows $(9/10,0),(9/10,0),(1/10,0)$. These are feasible packet summaries. At prefix $(b_A,b_B,b_C)=(3,2,3)$ every admissible missing group-$B$ row has positive cost, so the group-$B$ mean cost is strictly above the candidate's and cannot dominate it. The group-$B$ upper corner is $(14/15,1/3)$; combining it with the known group-$C$ mean using weights $1/5,4/5$ gives $(223/375,7/15)<p$. TRUE is therefore forced at cost eight. Candidate census is necessary because a legal $(1,1)$ fill makes its upper corner dominated by the complete group-$C$ mean. Legal small-positive-cost, zero-failure completions force at least two group-$B$ and three group-$C$ rows. The exact positive-delay-domain comparator is eight, while the closed triangle and square comparators are nine because the unattainable zero-cost group-$B$ completion introduces a domination tie in cost. Thus positive scalarisation slack alone does not justify replacing an open physical domain by its closure.

<a name="heading-research-mathematical_extensions_p61-s5-4-priced-and-dependent-extensions-a-limit-of-greedy-information-utility"></a>

### S5.4. Priced and dependent extensions; a limit of greedy information utility
**Heterogeneous disclosure prices.** Different records may have different processing or contractual disclosure fees. Prices fixed publicly by group and position already fit the weighted comparator $C_w^*$. The priced band results cover their stated regimes, and legal prefetch has the explicit factor $\Gamma(w)$ in Section S4.2. Cost-aware policies for more general bounded domains remain to be analysed. In particular, neither the unit-price square ratio nor the triangle constants $12/11$ and $87/80$ are established for arbitrary tariffs. The adverse controls in Section S3.5 show why retaining the original policy while changing its account is insufficient.

**Public dependence with a sharp distortion bound.** Public relations between records change the legal completion class and hence its realised certificates. General priced-function formulations already permit a non-product input domain ([CM08](../REFERENCES.md#ref-cm08)); stochastic certification under correlated distributions addresses a different objective and comparator ([GMS26](../REFERENCES.md#ref-gms26)). The following result quantifies a specific dependence structure under the present paid-prefix contract. Independence below means that the legal block completions form a Cartesian product, not that a probabilistic model is assumed.

**Proposition S11 (public constant blocks).** Let $\mathcal E\subseteq[0,1]^2$ contain $(0,0)$ and $(1,1)$. In the independent-row model $\mathsf Q$, each of the $K$ groups has $N$ rows in $\mathcal E$. In the block model $\mathsf D$, each group $g$ has a public partition $\mathcal B_g$ into consecutive blocks. Rows within a block are equal; the value of each block ranges over $\mathcal E$ independently of the other blocks and groups. Both models use the same predicate, row order and public strictly positive prices $w_{gj}$. Let $m$ be the largest block length and define

$$
R_g(0)=0,\qquad R_g(b)=\text{the final position of the block containing }b\quad (b\ge1),
$$

with $R(b)$ defined coordinatewise. On every realised archive $x\in\mathsf D$ and every prefix vector $b$,

$$
b\text{ is TRUE in }\mathsf D
\quad\Longleftrightarrow\quad
R(b)\text{ is TRUE in }\mathsf Q.
$$

<a name="eq-research-mathematical_extensions_p61-s19"></a>

Equation (S19).

For $W_g(b)=\sum_{j=1}^{b}w_{gj}$, put

$$
\rho_{\mathcal B}(w)
=\max_{g,\,1\le b\le N}\frac{W_g(R_g(b))}{W_g(b)}.
$$

Then every positive $x\in\mathsf D$ satisfies

$$
C_{\mathsf D,w}^*(x)
\le C_{\mathsf Q,w}^*(x)
\le\rho_{\mathcal B}(w)C_{\mathsf D,w}^*(x).
$$

<a name="eq-research-mathematical_extensions_p61-s20"></a>

Equation (S20).

At unit prices, $\rho_{\mathcal B}(w)\le m$, so $C_{\mathsf Q}^*\le mC_{\mathsf D}^*$. The same multiplicative bounds hold after adding an identical compulsory information-free setup charge $F\ge0$ to both certificate costs. At zero setup cost, the factor $m$ is attained, even with $K=3$ on the triangle. The weighted factor is attained for any common positive price profile when each group consists of one block.

**Proof.** A prefix of length $b_g$ has touched precisely the blocks ending at or before $R_g(b_g)$. The equal-row information determines every row through that endpoint, including the unqueried part of the last touched block. Thus the effective known row sum in $\mathsf D$ at $b$ is the observed row sum in $\mathsf Q$ at $R(b)$. Every remaining block can be set entirely to $(0,0)$ or entirely to $(1,1)$. These choices attain the same lower and upper mean corners in both models, simultaneously across groups. The necessity and sufficiency argument of Theorem 1 therefore applies to these common corners and proves (S19). It uses endpoint attainment, not a claim that every intermediate mean is attainable. The identity holds on negative archives too: neither side can certify TRUE on a prefix compatible with its realised negative completion.

Since $\mathsf D\subseteq\mathsf Q$, a TRUE prefix in $\mathsf Q$ is also TRUE in $\mathsf D$, giving the first inequality of (S20). If $b$ minimises the block-model certificate cost, (S19) makes $R(b)$ a legal independent-row certificate and

$$
\sum_gW_g(R_g(b_g))
\le\rho_{\mathcal B}(w)\sum_gW_g(b_g).
$$

Coordinates with $b_g=0$ contribute zero to both sums; no ratio $0/0$ is used. Positive prices make every denominator in $\rho_{\mathcal B}(w)$ positive, and $b=N$ shows that $\rho_{\mathcal B}(w)\ge1$. For unit prices, $R_g(b)\le b+m-1\le mb$ when $b\ge1$, while $R_g(0)=0$. The setup claim follows from $F+\rho C\le\rho(F+C)$ for $\rho\ge1$.

For sharpness, take $K=3$, one block per group and $N=m$. Set $\varepsilon=1/(100N)$ and repeat the row vectors

$$
p=(3/4+\varepsilon,1/4+\varepsilon),\qquad
L=(1/2,1/2),\qquad R=(1,0).
$$

They lie in the triangle. The candidate is nondominated and equals the midpoint of $L,R$ plus $(\varepsilon,\varepsilon)$, so it is strictly worse than their average under every nonzero nonnegative weight. It is therefore unsupported. In $\mathsf D$, one row from each group reveals all three means. Leaving a rival wholly unread permits the dominating value $(0,0)$; leaving the candidate unread permits a supported candidate $(0,0)$. Hence $C_{\mathsf D,w}^*=\sum_gw_{g1}$.

In $\mathsf Q$, each of the three immediate predecessors of full census admits a negative completion. If the last candidate row is unread, set it to $(0,0)$: its mean coordinate sum is $(1-1/N)(1+2\varepsilon)<1$, so weights $(1,1)$ support it against both rivals. If the last $L$ row is unread, set it to $(1,1)$, giving $L'=(a,a)$ with $a=(N+1)/(2N)$. Weights $(a,1-a)$ give both rivals score $a$, whereas the candidate has score $1/4+a/2+\varepsilon<a$. If the last $R$ row is unread and $N\ge2$, set it to $(1,1)$, giving $R'=(1,1/N)$. Weights $(1/2-1/N,1/2)$ give both rivals score $1/2-1/(2N)$, whereas the candidate has score $1/2-3/(4N)+\varepsilon(1-1/N)$, strictly smaller. For $N=1$, replacing the unread rival by $(0,0)$ suffices. Each witness uses legal whole rows, and the weights include the permitted axis case at $N=2$.

Every proper prefix lies below one of these three predecessors. Consequently full census is the only TRUE prefix in $\mathsf Q$, and $C_{\mathsf Q,w}^*=\sum_gW_g(N)$. At unit prices the ratio is $3N/3=m$. If every group has the same price profile $(w_1,\ldots,w_N)$, the ratio is $W(N)/w_1$. For a single block, this equals $\max_{b\ge1}W(N)/W(b)=\rho_{\mathcal B}(w)$, proving the weighted sharpness claim. $\square$

A policy that is globally correct in $\mathsf Q$ and has a proved weighted acquisition ratio $r$ therefore has ratio at most $r\rho_{\mathcal B}(w)$ when used unchanged on $\mathsf D$. This is a transfer bound for a policy that ignores the public dependence; a dependence-aware policy can do better. A unit-price guarantee is not a weighted guarantee. In particular, the sharp example with $N=m=2$ and common row prices $(1,M)$ has distortion $1+M$, so bounding block length alone does not bound distortion under arbitrary tariffs.

The block partition and exact equalities must be public before acquisition. Statistical association, equality noticed after reading, relations shared between groups or additional constraints coupling the block values do not satisfy the stated product-of-blocks assumption. The result supplies an explicit conservative-relaxation factor for this contract; it does not infer energy savings or an expected economic utility from disclosure counts.

An independently written finite checker obtains block certificates by intersecting exhaustive truth tables and independent-row certificates by enumerating the attainable completion sums, without importing the manuscript's endpoint oracle. Across 11 partition families it checks 1,329,000 prefix states, including mixed block lengths, and 7,140 exact cost comparisons with five price profiles and three common setup charges. It also verifies the explicit sharp-family completions for $N=1,\ldots,30$. These finite checks supplement the proof; the counts include overlapping mathematical cases and are not physical replications.

**A binary certificate utility is not automatically adaptive-submodular.** Adaptive-submodular optimisation requires diminishing conditional expected gains for its specified utility ([GK11](../REFERENCES.md#ref-gk11)). Consider $K=3,N=1$ and the alphabet

$$
\mathcal S_{\mathrm{util}}=\{(0,0),(0,1),(1,0),(1,1),(3/5,3/5)\}.
$$

For this example only, put an independent uniform prior on the three records. Define $U(\psi)$ to be one if the observations $\psi$ force GOOD over every compatible $\mathcal S_{\mathrm{util}}$-valued completion, and zero otherwise. Before any observation, querying the candidate has expected marginal utility zero: one record cannot exclude negative completions of the two rivals. After the two rivals have been observed as $(0,1)$ and $(1,0)$, querying the still-unread candidate has expected marginal utility $1/5$. Exactly the candidate value $(3/5,3/5)$ then gives TRUE. The conditional marginal gain has increased, violating adaptive submodularity for this utility even though the prior is independent and every query is a legal prefix query. An exact finite check enumerates all 125 complete archives and the five conditional candidate completions.

This counterexample concerns the displayed binary positive-certificate utility. It does not exclude other utilities or reductions. Moreover, a complete negative archive has utility zero, so this choice does not provide an all-realisation positive cover target. Any application of an adaptive-cover theorem would have to establish its own utility, distributional and target assumptions. The prior used in this example is not an assumption of the competitive acquisition results.

<a name="heading-research-mathematical_extensions_p61-s5-5-transfer-to-tighter-completion-domains-and-physical-metrics"></a>

### S5.5. Transfer to tighter completion domains and physical metrics
Exact transcript, completion-domain and uniform-charge equivalence transfers both certificates and minimax ratios to such a service when its entire admissible input class is equivalent to the abstract class: every abstract archive must also be a legal service input. With a tighter true domain $\mathcal D\subseteq\mathcal Q$, conservative certificates remain sound, but competitiveness needs a comparator bound. If each disclosure charge lies between $\alpha>0$ and $\beta$, the implemented policy has query bound $\mathbb E T\leq rC_{\mathcal Q}^*$, and $C_{\mathcal Q}^*\leq\gamma C_{\mathcal D}^*$, then

$$
\frac{\mathbb E\operatorname{Cost}(A)}{C_{\mathcal D,w}^*}\leq (\beta/\alpha)r\gamma.
$$

The charge account must add no unmodelled information. The factor $\gamma$ cannot be discarded: if all rows within each group are publicly known to be constant, one row per group gives $C_{\mathcal D}^*=K$, whereas the bounded product-square comparator is at least $K+2N-2$. For repeated points $(3/5,3/5),(0,1),(1,0)$ at $N=12$, the exact bounded product-square comparator is 32 and the constant-row comparator is three. Thus a conservative relaxation can incur an unbounded-in-$N$ benchmark distortion. For packet delivery times $T_m$ and deadline $d>0$, averages $c=\overline{\min(T_m/d,1)}$ and $f=\overline{\mathbf1\{T_m\geq d\}}$ obey $0\leq f\leq c\leq1$. This explicitly defined deadline metric has a constrained row domain; generic latency and failure summaries need not satisfy that relation. If zero-time successful delivery is an admitted mathematical input, its fixed-M row domain contains both whole extreme pairs, and the endpoint transfer theorem applies under independent-row completion. Strictly positive delivery times exclude the lower endpoint, as the counterexample in Section S5.3 demonstrates. Neither endpoint assumption is inferred from APEX trial summaries.

<a name="heading-research-mathematical_extensions_p61-s5-6-fixed-dimensional-certificates-unequal-lengths-and-aggregation-weights"></a>

### S5.6. Fixed-dimensional certificates, unequal lengths and aggregation weights
The endpoint argument extends beyond two objectives, but its two-rival witness bound becomes dimension dependent. The geometric ingredient is classical Helly theory ([DGK63](../REFERENCES.md#ref-dgk63)); the result below applies it to the paid-prefix comparator.

**Theorem S12 (weighted endpoint certificates and a sharp witness bound).** Let $d\geq2$. Group $g$ has $n_g$ fixed ordered rows in public domains $\mathcal D_{gj}\subseteq[0,1]^d$, each containing the whole endpoints $\mathbf0$ and $\mathbf1$. Row completions are independent. Public aggregation weights $\omega_{gj}>0$ sum to one separately in each group. All coordinates are minimised; supporting weights are nonzero and nonnegative, including axis weights, and scalarisation ties count as support. For a prefix $b_g$, put

$$
L_g(b_g)=\sum_{j\leq b_g}\omega_{gj}z_{gj},\qquad
r_g(b_g)=\sum_{j>b_g}\omega_{gj},\qquad
U_g(b_g)=L_g(b_g)+r_g(b_g)\mathbf1.
$$

<a name="eq-research-mathematical_extensions_p61-s23"></a>

Equation (S23).

A prefix is TRUE if and only if no rival $L_g$ Pareto-dominates $U_A$ and

$$
\bigcap_{g\ne A}
\{w\in\Delta_{d-1}:w\cdot(U_g-L_A)\geq0\}
=\varnothing,
$$

<a name="eq-research-mathematical_extensions_p61-s24"></a>

Equation (S24).

where $\Delta_{d-1}=\{w\geq0:\sum_{\ell=1}^dw_\ell=1\}$. Under the nondomination condition, the empty intersection in (S24) is witnessed by between two and $d$ rivals. The upper bound $d$ is sharp, already with one row per group.

*Proof.* Every compatible vector lies between its lower and upper corners. Filling all missing rows with the appropriate whole endpoint attains the corner configurations used by the two tests. Thus a dominating lower corner at $U_A$ gives a legal negative completion, as does a supporting weight for candidate $L_A$ against the rival upper corners. Conversely, a domination in any completion implies domination by the corresponding lower corner at $U_A$. If (S24) holds, every nonnegative nonzero weight gives some rival upper corner strictly smaller score than $L_A$; replacing the rival by a smaller compatible vector and the candidate by a larger one preserves this inequality. This proves the exact criterion without requiring intermediate box points to be attainable.

The sets in (S24) are convex and lie in the affine space $\sum_\ell w_\ell=1$, of dimension $d-1$. Helly's theorem supplies an empty subintersection of at most $d$ sets. An empty subintersection is plainly sufficient. A single set could be empty only if every coordinate of $U_g-L_A$ were negative, which would make $L_g$ dominate $U_A$ and contradict safety. Hence at least two rivals are needed.

For sharpness, take candidate $p_A=\tfrac12\mathbf1$ and the $d$ rivals

$$
p_i=\left(\frac12+\frac1{4d}\right)\mathbf1-\frac12 e_i,
\qquad 1\leq i\leq d.
$$

<a name="eq-research-mathematical_extensions_p61-s25"></a>

Equation (S25).

All points lie in the unit cube. Each rival has one coordinate below the candidate and every other coordinate above it, so the candidate is nondominated. Its supporting constraint against rival $i$ is $w_i\leq1/(2d)$. The $d$ constraints cannot hold together because their sum would give $1\leq1/2$. After removing constraint $i$, the axis weight $e_i$ satisfies every remaining constraint. Precisely $d$ rivals are therefore necessary. Their equal mixture is $p_A-\mathbf1/(4d)$, explicitly witnessing unsupportedness. $\square$

This gives an exact priced decomposition. Let the public disclosure prices $v_{gj}>0$ be fixed independently of hidden values, write $P_g(b)=\sum_{j\leq b}v_{gj}$, and allow a common compulsory information-free setup $F\geq0$. At candidate prefix $a$, let $h_g(a)$ be the earliest rival prefix whose lower corner does not dominate $U_A(a)$. If one is absent, discard $a$. For a rival set $J$, let

$$
E_J(a)=\min_{\substack{b_g\geq h_g(a)\ (g\in J)\\
L_A(a)\text{ unsupported against }(U_g(b_g))_{g\in J}}}
\sum_{g\in J}\bigl(P_g(b_g)-P_g(h_g(a))\bigr),
$$

<a name="eq-research-mathematical_extensions_p61-s26"></a>

Equation (S26).

with an infeasible minimum equal to infinity. Then

$$
C^*(I)=F+\min_{a\text{ feasible}}\left[
P_A(a)+\sum_{g\ne A}P_g(h_g(a))+
\min_{2\leq|J|\leq\min(d,K-1)}E_J(a)
\right].
$$

<a name="eq-research-mathematical_extensions_p61-s27"></a>

Equation (S27).

Every TRUE prefix includes the safe prefixes and, by Theorem S12, has a witness set $J$ of size at most $d$. Resetting all other rivals to their safe prefixes preserves TRUE and cannot increase cost. Conversely, every feasible choice in (S27) satisfies both endpoint conditions. This proves the formula. The full archive used to form these arrays is supplied only to the retrospective calculation.

For fixed $d$ and equal archive length $N$, (S27) yields an algorithm using $O_d(K^dN^d)$ exact predicate tests. For a fixed $J$ of size $k\geq2$, fix $k-2$ prefix counts and sweep the other two with the monotone staircase of Section S1.1. Unsupportedness is preserved as upper corners decrease. The last two indices move through $O(N)$ positions, so each witness set uses $O(N^{k-1})$ tests per candidate prefix, and there are $N+1$ candidate prefixes and $O_d(K^d)$ witness sets. Each predicate has at most $d$ constraints on a fixed-dimensional simplex. Unequal lengths give the corresponding sums of products. Straight enumeration gives the simpler $O_d(K^dN^{d+1})$ bound; that simpler version is the one implemented in the finite checker. In the plane the merged-threshold method in Section S1.1 improves the catalogue-size dependence further to $O(KN^2\log K)$.

Aggregation weights $\omega_{gj}$ and disclosure prices $v_{gj}$ have different roles. Neither (S27) nor endpoint transfer establishes the paper's unbounded, band or triangle acquisition constants under arbitrary aggregation weights or unequal lengths. The accompanying exact checks enumerate 2,972 prefixes of 30 heterogeneous weighted and priced archives in dimensions two to four; 18 archives are positive, and the decomposition matches exhaustive optimisation in all cases. The sharp witness examples are also checked for dimensions two to six. These finite results supplement the proof, rather than proving its unrestricted dimensional statement.

<a name="heading-research-mathematical_extensions_p61-s5-7-geometric-margins-imply-order-independent-disclosure-savings"></a>

### S5.7. Geometric margins imply order-independent disclosure savings
The next consequence links geometric separation to possible early stopping without assuming a distribution of records. Its sufficient direction needs only valid bounds on row coordinates; endpoint attainment and independent completion are unnecessary for that direction.

**Theorem S13 (margin-to-disclosure guarantee).** Let every row lie in $[0,1]^d$, with positive public aggregation weights normalised separately in each group, as in (S23). Let $p_g$ denote the complete weighted objectives. Suppose

$$
\delta_g:=\max_{1\leq\ell\leq d}(p_{g\ell}-p_{A\ell})>0
\quad(g\ne A)
$$

<a name="eq-research-mathematical_extensions_p61-s28"></a>

Equation (S28).

and there are rival mixture weights $\lambda_g\geq0$, $\sum_{g\ne A}\lambda_g=1$, and $\gamma>0$ such that

$$
p_A-\sum_{g\ne A}\lambda_gp_g\geq\gamma\mathbf1.
$$

<a name="eq-research-mathematical_extensions_p61-s29"></a>

Equation (S29).

A prefix is robust TRUE whenever

$$
r_A+r_g<\delta_g\quad(g\ne A),\qquad
r_A+\sum_{g\ne A}\lambda_gr_g<\gamma.
$$

<a name="eq-research-mathematical_extensions_p61-s30"></a>

Equation (S30).

For equal lengths $N$ and uniform aggregation weights, define

$$
\mu=\min\{\gamma,\min_{g\ne A}\delta_g\}>0,
\qquad q=\left\lceil\frac{N\mu}{2}\right\rceil-1.
$$

<a name="eq-research-mathematical_extensions_p61-s31"></a>

Equation (S31).

A causal policy that reads one row from each group in every round, checks robust TRUE after each acquisition and otherwise completes census stops by round $N-q$. At unit prices it uses at most $K(N-q)$ disclosures and saves at least $Kq$ relative to census, irrespective of the row order. The strict threshold and the universal factor two in (S31) cannot be improved using only the displayed margins.

*Proof.* Boundedness of the unread rows gives $L_g\geq p_g-r_g\mathbf1$ and $U_g\leq p_g+r_g\mathbf1$. In a coordinate attaining $\delta_g$,

$$
L_{g\ell}-U_{A\ell}
\geq p_{g\ell}-p_{A\ell}-r_g-r_A>0.
$$

No rival can therefore dominate the candidate in any compatible completion. Moreover,

$$
L_A-\sum_{g\ne A}\lambda_gU_g
\geq p_A-\sum_{g\ne A}\lambda_gp_g
-\left(r_A+\sum_{g\ne A}\lambda_gr_g\right)\mathbf1>\mathbf0.
$$

This strict mixture defeats every nonzero nonnegative scalarisation, so all completions are unsupported as well. For uniform weights, after $N-q$ rounds every unread mass equals $q/N<\mu/2$ by the definition of $q$. Both inequalities in (S30) hold. The policy needs neither the complete means nor the margins as input: it runs the observed-prefix corner tests, which remain sufficient without endpoint attainment or independence, and uses census fallback on every input, including negative ones. The means and margins are retrospective descriptors in the bound. $\square$

The condition $\delta_g>0$ excludes a rival coinciding with the candidate; nondomination alone would give only $\delta_g\geq0$. A strict mixture margin exists for an unsupported finite objective set: normalising nonnegative scalarisations to the simplex and applying separation, or finite-dimensional minimax, gives

$$
\gamma_*=
\max_{\lambda_g\geq0,\ \sum_g\lambda_g=1}
\min_{1\leq\ell\leq d}
\left(p_{A\ell}-\sum_{g\ne A}\lambda_gp_{g\ell}\right)>0.
$$

<a name="eq-research-mathematical_extensions_p61-s32"></a>

Equation (S32).

Conversely, any positive value in (S32) rules out every supporting weight. These are classical convex-separation consequences ([BV04](../REFERENCES.md#ref-bv04)), not new scalarisation theorems. The stopping guarantee may use any explicit positive mixture margin without solving this retrospective optimisation.

For a triangle example, take

$$
p_A=(7/8,3/8),\qquad p_L=(1/2,1/2),\qquad p_R=(1,0).
$$

<a name="eq-research-mathematical_extensions_p61-s33"></a>

Equation (S33).

Here $\delta_L=\delta_R=1/8$, and the equal rival mixture $(3/4,1/4)$ gives $\gamma=1/8$. At $N=160$, (S31) gives $q=9$: the policy saves at least 27 of 480 disclosures, or $5.625\%$, for every legal row order with these means. The guaranteed fraction approaches $6.25\%$ as $N$ grows. A common setup leaves the number of saved disclosures unchanged. With a common tariff $\tau>0$, the avoided disclosure charges are at least $\tau Kq$; heterogeneous prices require summing the omitted tail prices. These are conditional cost statements, without accounting for a deployment's computation, communication or other overhead, and without a measured monetary benefit or a new ratio against $C^*$.

To prove sharpness, use $N=160$ and the ordered triangle rows

- candidate: 60 copies of $(1,1)$, then 80 of $(1,0)$, then 20 of $(0,0)$;
- rival $L$: 70 copies of $(1,1)$, then 80 of $(0,0)$, then 10 of $(1,1)$;
- rival $R$: 160 copies of $(1,0)$.

The complete means are (S33). At the common prefix 150, the unread mass is $1/16=\mu/2$ and

$$
L_L=(7/16,7/16),\qquad U_A=(15/16,7/16).
$$

<a name="eq-research-mathematical_extensions_p61-s34"></a>

Equation (S34).

The former dominates the latter. Both corner completions are attainable in the triangle, so this prefix is not TRUE. Thus replacing the strict condition by $r\leq\mu/2$ fails. For any constant $c<2$, the same unread mass satisfies $r<\mu/c$ and refutes the proposed replacement of the factor two by $c$. At common prefix 151 the inequalities become strict, and Theorem S13 guarantees TRUE. The sharpness concerns this margin-only bound, not optimality among all acquisition policies. In the different, designed archive with every row equal to its group's mean in (S33), common prefix 143 is already TRUE, saving 51 of 480 disclosures; this is a synthetic exact example, not an application measurement.

The supplied checker verifies the guarantee on 6,400 additional finite prefix states; its hypotheses hold in 41 and its conclusion holds in all 41. It also checks the exact triangle examples and the boundary failure above. The relatively few applicable short random archives reflect the strength of a worst-order sufficient condition, not evidence of deployment prevalence.

<a name="heading-research-mathematical_extensions_p61-s5-8-why-candidate-census-need-not-remain-necessary-in-higher-dimension"></a>

### S5.8. Why candidate census need not remain necessary in higher dimension
**Proposition S14 (an unbounded-dimensional boundary example).** Let $d\geq3$ and let rows range independently over

$$
\mathcal U_d=[0,\infty)\times[0,1]^{d-1}.
$$

<a name="eq-research-mathematical_extensions_p61-s35"></a>

Equation (S35).

There are robust TRUE prefixes leaving the candidate incomplete. In particular, with $d-1$ fully observed rivals of means $(0,e_i)$, where $e_i$ are the axes in the last $d-1$ coordinates, such prefixes exist at every attainable candidate observation fraction $t$ with $1/(d-1)<t<1$. For this fixed rival family, $t>1/(d-1)$ is necessary for any robust TRUE prefix with the candidate observed to fraction $t$.

*Proof.* Choose $1/(d-1)<c<t$ and make every observed candidate row $(1,(c/t)\mathbf1)$. Its lower vector is $(t,c\mathbf1)$. Every compatible candidate has bounded coordinates at most $c+1-t<1$, so each rival is strictly worse in its own unit coordinate and cannot dominate. The equal rival mixture is $(0,\mathbf1/(d-1))$, strictly below the candidate lower vector in every coordinate. Hence every nonzero nonnegative scalarisation has a strictly better rival, regardless of the unread first coordinates, and the prefix is TRUE.

Conversely, at $t\leq1/(d-1)$ the sum of the candidate's observed lower coordinates in positions two through $d$ is at most $(d-1)t\leq1$. Complete its unread rows with zero. Equal positive weights on these $d-1$ coordinates, and zero weight on the unbounded coordinate, support the candidate against every rival, each of which has bounded-coordinate sum one. The prefix therefore admits a negative completion. $\square$

For $d=3$ and $N=10$, let the first six candidate rows be $(1,11/12,11/12)$, and completely read the ten repeated rows $(0,1,0)$ in one rival and $(0,0,1)$ in the other. Then

$$
L_A=(3/5,11/20,11/20),\qquad
(U_{A,2},U_{A,3})=(19/20,19/20).
$$

<a name="eq-research-mathematical_extensions_p61-s36"></a>

Equation (S36).

Each rival remains worse in one bounded coordinate, while their mean $(0,1/2,1/2)$ is strictly below $L_A$. Prefix $(6,10,10)$ is consequently TRUE with four candidate rows unread. The necessity of candidate census in the paper's two-dimensional unbounded theorem does not generalise to $d\geq3$. This construction gives no new minimax ratio in higher dimensions. The exact checker verifies the concrete example and family inequalities for dimensions three to eight.

<a name="heading-research-mathematical_extensions_p61-s5-9-few-alternative-certificates-in-many-criteria"></a>

### S5.9. Few-alternative certificates in many criteria
Theorem S12 bounds the number of rivals needed to rule out support. A complementary bound controls the number of criteria needed to establish support. This distinction separates a family of low-dimensional tests from a single replacement of the objective space. The argument uses classical finite-dimensional convex geometry ([DGK63](../REFERENCES.md#ref-dgk63); [BV04](../REFERENCES.md#ref-bv04)).

**Theorem S16 (sparse supporting weights).** Let a finite catalogue contain a candidate $p_A\in\mathbb R^d$ and $m=K-1\geq1$ rivals. If the candidate is supported under nonzero nonnegative weights, it has a supporting weight with at most $\min(d,m)$ nonzero coordinates. Scalarisation ties and axis weights are included.

*Proof.* For each criterion $i$, form the column $v_i=((p_g-p_A)_i)_{g\ne A}\in\mathbb R^m$. Normalising weights to sum to one shows that support is equivalent to

$$
Q\cap\mathbb R_+^m\ne\varnothing,
\qquad Q=\operatorname{conv}\{v_1,\ldots,v_d\}.
$$

If $Q$ has affine dimension at most $m-1$, Caratheodory's theorem represents any point of this intersection using at most $m$ columns. Otherwise $Q$ is full-dimensional. Starting at a feasible point $z\geq0$, move in direction $\mathbf1$ to the last point of $Q$ on that ray. Compactness gives an endpoint, still nonnegative, on a proper face of dimension at most $m-1$. Caratheodory's theorem on that face again supplies at most $m$ columns. Their convex coefficients are supporting weights. There are only $d$ columns in total. $\square$

For three alternatives and $d\geq2$, it follows that

$$
\begin{gathered}
p_A\text{ is unsupported in }\mathbb R^d\\
\Longleftrightarrow\quad
p_A\text{ is unsupported in every two-coordinate projection}.
\end{gathered}
$$

A supporting weight in a projection extends by zeros, and Theorem S16 supplies such a projection whenever full-dimensional support exists. Nondomination must still be checked in all original coordinates; requiring nondomination in every projection would be unnecessarily strong. The support decomposition uses $\binom d2$ planar tests, without discarding any criterion. For general $K$, subsets of at most $K-1$ criteria suffice; pairs alone are not asserted to suffice.

For $K=3$ there is a faster direct calculation. By the strict-mixture characterisation in (S32), unsupportedness is equivalent to

$$
\exists\lambda\in[0,1]\quad
\lambda(p_{Li}-p_{Ri})<p_{Ai}-p_{Ri}
\quad(1\leq i\leq d).
$$

Start with the closed interval $[0,1]$. A positive coefficient supplies a strict upper bound, a negative coefficient a strict lower bound, and a zero coefficient requires a strictly positive right-hand side. Intersect these constraints, preserving whether each boundary is open. An equal lower and upper bound is feasible only when both are included. For rational input vectors, this takes $O(d)$ rational operations and constant additional interval storage once the vectors are available. Together with the original-space nondomination scan it computes GOOD exactly. This is a classical one-variable feasibility calculation, rather than a new bound on paid acquisition or bit complexity.

Under the endpoint assumptions of Theorem S12, the same calculation evaluates its unsupportedness condition using candidate $L_A$ and rivals $U_L,U_R$; its separate safety test compares each $L_g$ with $U_A$ in all $d$ coordinates. For rational corners, the resulting robust TRUE test therefore takes $O(d)$ rational operations per available corner catalogue when $K=3$. Without attainable endpoints it remains sufficient, but necessity is not claimed. Under Theorem S12's exact endpoint assumptions, failure means that TRUE is not forced; it does not establish that FALSE is forced. Outside those assumptions, failure of the sufficient test alone does not even settle whether TRUE is forced. A correct acquisition policy must retain these distinctions and a valid continuation rule.

<a name="heading-research-mathematical_extensions_p61-s5-10-a-robust-obstruction-to-universal-criterion-aggregation"></a>

### S5.10. A robust obstruction to universal criterion aggregation
**Proposition S17 (no universal monotone affine compression).** For every $d\geq3$ and $1\leq r<d$, there is a GOOD candidate in $[0,1]^d$ whose image is not GOOD under any map $T(x)=b+Wx$ with $W\in\mathbb R_+^{r\times d}$. The map may be chosen after the entire catalogue is known. When no output criterion is constant, normalising each row of $W$ to sum to one produces false projected domination with coordinatewise margin at least $1/4$.

*Proof.* Set $p_A=\tfrac34\mathbf1$ and $p_i=e_i$ for $1\leq i\leq d$. Each rival is worse in its own coordinate, so none dominates $A$. The mean of any two distinct rivals is at most $\tfrac12\mathbf1$, strictly below $p_A$, proving unsupportedness. Offsets cancel from comparisons. If $W$ has a zero row, the corresponding constant criterion supports every image through an axis weight. Otherwise positive rescaling of each output criterion preserves both domination and support, so normalise the rows of $W$ to sum to one. In each row at most one coefficient exceeds $1/2$. Since $r<d$, some index $i$ has $W_{si}\leq1/2$ for every output row $s$. Consequently

$$
Wp_i\leq\tfrac12\mathbf1
<\tfrac34\mathbf1=Wp_A,
$$

as required. $\square$

Thus even a two-rival strict-mixture witness does not imply that two aggregated criteria preserve nondomination. The proposition covers coordinate selection and nonnegative affine aggregation. It does not rule out arbitrary answer-encoding maps, unrestricted signed transformations or reductions justified by additional structure. Its catalogue contains $d+1$ alternatives and does not contradict the three-alternative test decomposition above.

<a name="heading-research-mathematical_extensions_p61-s5-11-exact-anchor-reduction-and-preservation-of-paid-prefixes"></a>

### S5.11. Exact anchor reduction and preservation of paid prefixes
Objective reduction has an established literature on dominance preservation ([BZ09](../REFERENCES.md#ref-bz09)); rank-based reductions can also change the ordering cone ([LZ26](../REFERENCES.md#ref-lz26)). The following sufficient condition records the additional support and observation requirements needed here.

**Theorem S18 (anchor and paid-prefix equivalence).** Suppose all vectors in a family have the common form

$$
x=b+My,\qquad y\in Y\subseteq\mathbb R^2,
$$

where $M\geq0$, no row of $M$ is zero, and two rows are positive multiples of $(1,0)$ and $(0,1)$. Every finite catalogue in the family has the same pairwise domination relations and supported/unsupported labels in its $x$ and $y$ representations.

Suppose additionally that this relation is public and computationally usable for every raw row, with a bijection between the legal complete archives in the two models. Require identical initial information, row order, archive lengths, whole-row query rule, disclosure prices and any compulsory setup charge. All public dependencies must correspond under the bijection. Aggregation weights are public, positive and normalised within each group, and are identical in the two representations. Then corresponding prefixes force the same verdicts, have the same certificate costs and comparator $C^*$, and admit policy simulations with identical paid query paths.

*Proof.* Nonnegativity maps coordinatewise inequalities from $y$ to $x$, and the two anchor rows reflect them back. An anchor also detects every strict inequality, so equality and strict domination are preserved. For any $w\geq0$, $w\ne0$,

$$
w^Tx=w^Tb+(M^Tw)^Ty.
$$

The induced weight $M^Tw$ is nonnegative and nonzero because no row of $M$ is zero. Conversely, every nonnegative nonzero planar weight is realised by weights on the two anchors. The possible scalarised rankings, including ties, therefore coincide.

The anchor values recover $y$ from an observed row, while the public map reconstructs $x$. Moreover, normalised aggregation gives

$$
\sum_j\omega_{gj}x_{gj}
=b+M\sum_j\omega_{gj}y_{gj}.
$$

The archive bijection restricts to a bijection between the completions consistent with each corresponding prefix. The first part preserves GOOD on every such completion, hence preserves forced TRUE, forced FALSE and undecided states. Certificate sets and their prices coincide, as do their minima. To simulate a causal policy, translate each observed response before its next decision. Coupling random choices gives the same queries and payments on every complete archive and random seed, and preserves termination and correctness. $\square$

The nonzero-row hypothesis is essential under our support convention: a constant criterion supports every alternative. A map fitted only to complete means supplies no constraint on unread rows unless it is genuinely part of the public completion model. The theorem equates information charges, not necessarily computation time.

As a conditional application, retain latent criteria $(c,f)$ with $0\leq f\leq c\leq1$, and append any number of public criteria $\alpha_i c+(1-\alpha_i)f$, $0\leq\alpha_i\leq1$, to every row. There are two anchors and no zero coefficient row. If the latent archives satisfy all assumptions of main Theorem 20, its $87/80$ bound transfers unchanged. This includes the stated three-configuration, equal-length, uniform-aggregation and unit-disclosure-price conditions and the required latent completion domain. Fifty recorded criteria formed in this way still have only two independent coordinates. This example gives no such ratio for fifty independent objectives, arbitrary tariffs or a latent domain outside the main theorem's hypotheses.

<a name="heading-research-mathematical_extensions_p61-s5-12-certified-approximation-with-reconstruction-margins"></a>

### S5.12. Certified approximation with reconstruction margins
Exact reduction may fail while a sufficiently accurate representation still certifies the original verdict. The error bounds in the following statement are deterministic bounds for every relevant coordinate and alternative, not fitted average errors.

**Proposition S19 (error-controlled positive certification).** Suppose nonnegative error bounds and reconstructed vectors satisfy $|p_{gi}-\widehat p_{gi}|\leq e_{gi}$. Candidate $A$ is GOOD if every rival $g$ has some coordinate $i$ such that

$$
\widehat p_{gi}-\widehat p_{Ai}>e_{gi}+e_{Ai},
$$

and there are rival weights $\lambda_g\geq0$, $\sum_g\lambda_g=1$, satisfying, for every coordinate $i$,

$$
\widehat p_{Ai}-\sum_g\lambda_g\widehat p_{gi}
>e_{Ai}+\sum_g\lambda_ge_{gi}.
$$

*Proof.* Subtracting the maximal possible errors leaves each actual rival strictly worse than $A$ in at least one coordinate, proving nondomination. The second condition leaves the actual rival mixture strictly below $p_A$ in every coordinate, proving unsupportedness by (S32). $\square$

Under uniform error $\varepsilon$, strict nondomination and mixture margins greater than $2\varepsilon$ suffice. The factor and strictness cannot be relaxed using only these error bounds. Take $\widehat p_A=(.5,.5)$, $\widehat p_L=(.1,.7)$, $\widehat p_R=(.7,.1)$ and $\varepsilon=.05$. The nondomination margins are $.2>2\varepsilon$, while the equal-mixture gap is $.1=2\varepsilon$. Permitted true values $p_A=(.45,.45)$, $p_L=(.15,.75)$ and $p_R=(.75,.15)$ all have coordinate sum $.9$, so equal weights support $A$ at the boundary.

A two-coordinate sufficient test follows when two exact original anchors $z_g\in\mathbb R^2$ are retained, nonnegative error tolerances $\eta_g$ are given, and the remaining criteria satisfy

$$
p_{gi}=b_i+B_i z_g+r_{gi},\qquad
B_i\geq0,\quad s_i=B_i\mathbf1>0,\quad
|r_{gi}|\leq s_i\eta_g.
$$

Suppose every rival is strictly worse than the candidate in at least one anchor, and a rival mixture satisfies

$$
z_A-\sum_g\lambda_gz_g\geq\rho\mathbf1,
\qquad \rho>\eta_A+\sum_g\lambda_g\eta_g.
$$

The anchors ensure nondomination. In each omitted coordinate the true mixture gap is at least $s_i(\rho-\eta_A-\sum_g\lambda_g\eta_g)>0$, while the retained gaps are positive as well. This proves GOOD. Uniform tolerance gives the sufficient condition $\rho>2\eta$. Coincident anchor vectors do not meet the strict rival condition; omitted residuals can then introduce domination and require additional checking.

For robust prefix certification, the bounds must cover every compatible completion, including unread rows. Failure of a sufficient margin test does not settle the verdict and calls for further original-space analysis; it does not justify FALSE. This approximation result alone preserves neither the exact comparator nor a numerical acquisition ratio.

