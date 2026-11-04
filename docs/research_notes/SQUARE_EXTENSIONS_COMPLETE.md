<a name="heading-research_notes-square_extensions_complete-complete-square-extensions-and-comparator-development"></a>

# Complete square extensions and comparator development
> Rights: manuscript-derived text retains its existing rights. No new licence is granted by routing it to Markdown.

[Documentation index](../README.md)

This is a complete retained mathematical research note from the audited P61 source. The essential review supplement identifies the results used by the article; the additional results below are preserved as secondary research material. Historical identifiers are retained and are qualified by this note.

**Current reader role:** Complete square/comparator research note; the essential Figure 1 argument remains in the core supplement, while wider developments are secondary.

**Reading context.** Section and statement identifiers refer to their original research stages. This note preserves the stated arguments, evidence and limitations. The article and Essential Supplement form a separate review package.

<a name="supp-s1"></a>

## S1. Square certificate geometry and acquisition
This section supplies the square-domain geometry and acquisition arguments. There are $K\geq3$ groups, each containing $N\geq1$ ordered rows; the initially unknown candidate is group $0$. Queries reveal whole rows in prefix order, including paid candidate rows. Algorithms must be correct on both answers. The completion domain is the independent continuous product $[0,B]\times[0,1]$, with $B>0$ public. Dividing the first coordinate by $B$ preserves nondomination, all nonnegative scalarisations and query costs. We therefore work in the unit square. No relation between $K$ and $N$ is required.

Each disclosure costs one. GOOD means that the complete candidate mean is Pareto-nondominated and unsupported by every nonzero nonnegative scalarisation, with both coordinates minimised. Pareto domination requires at least one strict coordinate improvement; scalarisation ties and the coordinate axes count as support. Admissible policies are causal, zero-error and almost surely terminating on every legal positive and negative input. Let $C_B^*(I)$ be the least total prefix length forcing TRUE over every compatible square completion of the fixed positive archive $I$. Let $C_U^*(I)$ be its corresponding comparator when the first row coordinate instead has the unbounded domain $[0,\infty)$. Neither retrospective comparator is supplied to a policy. Define

$$
R_B^*(K,N)=\inf_{\mathcal A}\sup_{I:\mathrm{GOOD}(I)}
\frac{\mathbb E C_{\mathcal A}(I)}{C_B^*(I)},
$$

where each expectation is taken on a fixed archive before the input supremum. Write $R_{{\rm det},B}^*$ for the same optimum over deterministic policies. Throughout, $D=K+3N-3$ and

$$
\delta_K=
\begin{cases}
(4K-13)/6,&K\text{ even},\\
(4K-13)/6+1/[3(K-1)],&K\text{ odd}.
\end{cases}
$$

These are the constants from the general catalogue theorem in main Section 3.

<a name="heading-research_notes-square_extensions_complete-s1-1-exact-corners-and-a-faster-retrospective-comparator"></a>

### S1.1. Exact corners and a faster retrospective comparator
At a prefix of length $s_r$, let $S_r$ be the observed coordinate sum and set

$$
L_r=S_r/N,\qquad U_r=L_r+(1-s_r/N)(1,1).
$$

<a name="eq-research_notes-square_extensions_complete-q1"></a>

Equation (Q1).

Every compatible mean belongs to the rectangle $[L_r,U_r]$, and each point of that rectangle is attainable. For a missing-row count $q>0$, assign all missing rows the same pair $N(p-L_r)/q$. Its coordinates lie in $[0,1]$. Completions of different groups are independent, so all required corners can be attained simultaneously.

A state forces GOOD precisely when

$$
\text{no }L_r\text{ Pareto-dominates }U_0,
\qquad
L_0\text{ is unsupported by the points }U_r\ (r\ne0).
$$

<a name="eq-research_notes-square_extensions_complete-q2"></a>

Equation (Q2).

For the first condition, a dominating corner pair itself gives a legal counterexample. Conversely, any domination in a completion implies domination of the corresponding corner pair: $L_r\leq p_r\leq p_0\leq U_0$, with a strict inequality surviving in some coordinate. For the second condition, candidate $L_0$ and competitor points $U_r$ are simultaneously attainable. If they admit a supporting nonnegative weight, that completion is FALSE. If they admit none, then for every nonzero nonnegative weight some $U_r$ has strictly smaller score than $L_0$; replacing $U_r$ by a smaller competitor mean and $L_0$ by a larger candidate mean preserves the strict inequality. These statements also explain why full-vector equality is safe for nondomination, whereas a scalarisation tie remains support.

For a fixed candidate prefix $s$, consider each rival's closed interval of supporting weights against $L_0(s)$ at its upper corner. Robust nondomination excludes an individually empty interval: both upper coordinates strictly below $L_0(s)$ would give domination at the lower corners. An empty intersection of finitely many nonempty closed intervals is witnessed by two disjoint intervals. Thus unsupportedness in (Q2) is equivalent to two distinct upper corners having a convex combination strictly below $L_0(s)$ in both coordinates. Touching intervals do not suffice.

Let $h_r(s)$ be the first rival prefix whose lower corner does not dominate $U_0(s)$. Once safe, it remains safe because lower corners increase coordinatewise. If a required $h_r(s)$ does not exist, discard $s$. For each pair $r,t$, minimise the additional observations beyond $h_r(s),h_t(s)$ needed for their upper corners to form the strict pair; call this minimum $e_{rt}(s)$, or infinity if no pair is feasible. Every TRUE state must pay all the $h_r(s)$ and attain such a strict pair of upper corners. Conversely, paying precisely the safe prefixes and a minimising pair establishes both conditions of (Q2). This proves the exact bounded certificate decomposition

$$
C_B^*(I)=\min_{s\text{ feasible}}
\left[s+\sum_{r\ne0}h_r(s)+\min_{r<t}e_{rt}(s)\right],
$$

without imposing a restricted certificate syntax. All prefixes and minima here refer to the realised archive $I$.

For completeness, the pair predicate is upward closed in its two prefix counts: additional observations lower upper corners and preserve an existing strict mixture. In a fixed pair grid, increase the first count while retaining the smallest feasible second count, moving the latter only downwards. Each index traverses at most $N$ positions. Initial infeasible rows are skipped with the second count at $N$. The sweep therefore finds the minimum pair total in $O(N)$ exact arithmetic operations. Across $N+1$ candidate prefixes and $O(K^2)$ pairs this gives $O(K^2N^2)$ operations, after the $O(KN)$ corner arrays are formed, with $O(KN)$ working storage. These arrays use the realised archive; this is a retrospective computation, not free information for an acquisition policy.

**Merged-threshold refinement.** The quadratic enumeration of rival pairs can be removed. With rational coordinates and arbitrary public strictly positive rational row prices, the cheapest realised robust TRUE-prefix certificate can be computed in $O(KN^2\log K)$ rational arithmetic and comparison operations, using $O(KN)$ working storage. The algorithm returns a minimising prefix or reports that no TRUE prefix exists. A common compulsory information-free setup charge $F\geq0$ is allowed. The result also holds for independent row domains contained in the square and containing both whole endpoints: the proof uses the endpoint criterion, not attainability of intermediate rectangle points. This is an arithmetic-operation bound; rational encoding lengths still affect bit complexity.

To prove the claim, precompute the corners and cumulative row prices $P_r(b)$. Fix a candidate prefix $s$, write $p=L_0(s)$ and $q=U_0(s)$, and compute the same earliest safe prefixes $h_r(s)$. If one does not exist, discard $s$. Otherwise every feasible certificate pays at least the base

$$
B_s=F+P_0(s)+\sum_{r\ne0}P_r(h_r(s)).
$$

<a name="eq-research_notes-square_extensions_complete-q2a"></a>

Equation (Q2a).

For $b\geq h_r(s)$, let $d_r(b)=P_r(b)-P_r(h_r(s))$. All these increments are nonnegative. The preceding decomposition remains valid with prices: a TRUE prefix can be reduced to the safe base and the extensions of two witness rivals without increasing cost.

A strict northwest upper corner $U_r(b)=(p_c-A,p_f+C)$, with $A,C>0$, permits a supporting weight $(\theta,1-\theta)$ precisely when

$$
\theta\leq\ell_r(b):=\frac{C}{A+C}.
$$

A strict southeast upper corner $U_t(c)=(p_c+D,p_f-E)$, with $D,E>0$, requires

$$
\theta\geq m_t(c):=\frac{E}{D+E}.
$$

Their pair witnesses unsupportedness exactly when $m_t(c)>\ell_r(b)$. Equality leaves a scalarisation tie and therefore support. Other upper corners may be omitted. A corner weakly southwest of $p$, with at least one strict coordinate, would imply $L_r\leq U_r\leq p\leq q$ with a strict coordinate and would violate safety. A weak northeast corner, including equality, imposes no supporting-weight restriction.

Every upper-corner sequence is coordinatewise nonincreasing. Consequently, on northwest states $A$ increases and $C$ decreases, so $\ell_r$ is nonincreasing with the prefix; on southeast states $D$ decreases and $E$ increases, so $m_r$ is nondecreasing. A rival cannot supply states of both kinds: after a northwest state its cost remains strictly below $p_c$, whereas a southeast state requires cost strictly above $p_c$; the reverse temporal order is excluded by the failure coordinate. Thus the two selected streams automatically have distinct rival labels.

List northwest states in increasing prefix order and southeast states in decreasing prefix order. Each rival then contributes at most one stream sorted by decreasing threshold. Merge the at most $K-1$ streams with a binary heap. Maintain the least southeast increment among states at strictly larger thresholds. For a group of equal thresholds, first evaluate every northwest state against this stored least increment, then insert the southeast states at that threshold. Processing ties in this order enforces the strict inequality. The sweep therefore computes exactly

$$
\min_{m_t(c)>\ell_r(b)}\{d_r(b)+d_t(c)\}.
$$

<a name="eq-research_notes-square_extensions_complete-q2b"></a>

Equation (Q2b).

Store the two realising prefix indices whenever the minimum improves. Adding $B_s$ and taking the minimum over $s$ gives the exact comparator and its certificate. If no pair is found at any $s$, no TRUE prefix exists; by full census, the complete archive is negative. Each candidate prefix uses $O(KN)$ corner and safety operations and a merge of $O(KN)$ states costing $O(KN\log K)$ comparisons. There are $N+1$ candidate prefixes, proving the stated complexity. The old pair staircase remains a valid alternative; the improvement concerns dependence on catalogue size, since both bounds are $O(N^2)$ for fixed $K$.

**Unequal lengths and positive aggregation weights.** Let group $r$ have $n_r$ rows and public weights $\omega_{rj}>0$ summing to one within that group. Its objective is the weighted mean, with corners

$$
L_r(b)=\sum_{j\leq b}\omega_{rj}z_{rj},\qquad
U_r(b)=L_r(b)+\left(\sum_{j>b}\omega_{rj}\right)(1,1).
$$

<a name="eq-research_notes-square_extensions_complete-q2c"></a>

Equation (Q2c).

The same endpoint proof, safety monotonicity and threshold order apply. For $M=\sum_r(n_r+1)$ the complexity is $O((n_0+1)M\log K)$ arithmetic and comparison operations and $O(M)$ storage. Aggregation weights determine contributions to the objective and unread uncertainty; disclosure prices determine certificate cost. They are distinct inputs. This offline extension does not transfer the paper's numerical acquisition ratios to unequal lengths, arbitrary aggregation weights or arbitrary prices.

The research extensions supply the exact implementation `geo_comparator.py`. Against an independently coded closed-interval oracle it agrees on 2,966 archives and 695,812 enumerated prefixes, including nonuniform prices, unequal lengths and nonuniform aggregation weights; 566 archives are positive. A separate rational LP-vertex oracle agrees on 100 archives and 15,516 prefixes, including 40 unequal-length or nonuniform-weight cases. These finite checks corroborate the implementation; the analytic proof establishes the general algorithmic claim.

<a name="heading-research_notes-square_extensions_complete-s1-2-exact-feasibility-of-three-designated-prefix-lengths"></a>

### S1.2. Exact feasibility of three designated prefix lengths
Let $a,i,j\in\{1,\ldots,N\}$ be the candidate prefix and the prefixes of two designated strict witnesses. Write

$$
t=1-a/N,\qquad u=1-i/N,\qquad v=1-j/N,
$$

and let the candidate lower corner be $(x,y)$. Its upper corner is $(x+t,y+t)$. Robust nondomination excludes a witness upper corner weakly below $(x,y)$ with at least one strict coordinate. A strict pair must therefore cross $(x,y)$ in opposite directions. Relabel the witnesses so that the first upper corner is northwest and the second southeast.

The northwest witness's lower cost is already strictly below the candidate upper cost. Its lower failure must consequently exceed $y+t$; full-vector safe equality is impossible in this situation. The southeast witness similarly needs lower cost exceeding $x+t$. Observed-sum bounds give

$$
x<1-v-t,\qquad y<1-u-t.
$$

<a name="eq-research_notes-square_extensions_complete-q3"></a>

Equation (Q3).

Let $\lambda\in(0,1)$ be the northwest weight in a strict mixture. The northwest upper cost is at least $u$, and its upper failure exceeds $y+t+u$. The southeast upper failure is at least $v$, and its upper cost exceeds $x+t+v$. The cost mixture inequality and (Q3) imply

$$
\lambda(1-u)>t+v.
$$

The failure inequality similarly implies

$$
(1-\lambda)(1-v)>t+u.
$$

<a name="eq-research_notes-square_extensions_complete-q4"></a>

Equation (Q4).

Thus the admissible interval is nonempty only if

$$
\frac{t+v}{1-u}+\frac{t+u}{1-v}<1.
$$

Substitution and multiplication by the positive integers $i,j$ give exactly

$$
(2N-a)(i+j)<i^2+ij+j^2,
$$

<a name="eq-research_notes-square_extensions_complete-q5"></a>

Equation (Q5).

which is the square feasibility criterion.

Conversely, suppose (Q5) holds and choose a rational $\lambda$ satisfying (Q4). Put $x_0=1-v-t$ and $y_0=1-u-t$. The inequalities imply $t+u+v<1$, so both limits are positive. At the limiting candidate lower corner $(x_0,y_0)$, use formal lower witness corners $(0,y_0+t)$ and $(x_0+t,0)$. Their upper-corner mixture has cost gap

$$
x_0-\bigl[\lambda u+(1-\lambda)(x_0+t+v)\bigr]
=\lambda(1-u)-(t+v)>0,
$$

and failure gap $(1-\lambda)(1-v)-(t+u)>0$.

Choose $x,y$ slightly below $x_0,y_0$, then choose a sufficiently small rational $\epsilon>0$. Take the actual lower witness corners to be

$$
(0,y+t+\epsilon),\qquad(x+t+\epsilon,0).
$$

<a name="eq-research_notes-square_extensions_complete-q6"></a>

Equation (Q6).

The decreases in $x,y$ allow the extra $\epsilon$ while keeping these corners within their observed-sum caps $[0,i/N]^2$ and $[0,j/N]^2$. The candidate remains in $[0,a/N]^2$. Strict mixture gaps survive sufficiently small perturbations. The lower witnesses are P2-safe because their respective escape coordinates exceed the candidate upper coordinates. Realise each lower corner by identical observed rows equal to $N$ times that corner divided by its prefix length; these rows belong to the unit square. Fill unread actual rows with zero. The prefix then forces GOOD, giving a legal positive archive. This proves sufficiency, including $N=1$.

Adding (Q4), whose left side is at most one, gives the useful strict budget condition

$$
2a+i+j>3N.
$$

<a name="eq-research_notes-square_extensions_complete-q7"></a>

Equation (Q7).

In particular $a>N/2$, $i+j>N$, and $a+i+j\geq2N+1$. Condition (Q7) alone is insufficient: for $N=5$ and $a=i=j=4$, (Q5) is equality, so no strict certificate exists.

For fixed $a$, put $d=N-a$ and $s=i+j>N$. The right side of (Q5) is $s^2-ij$. At fixed $s$, this is largest at $\{i,j\}=\{N,s-N\}$, since that choice minimises $ij$ within the allowed interval. Writing $s=N+r$ reduces feasibility to

$$
r^2>d(N+r).
$$

<a name="eq-research_notes-square_extensions_complete-q8"></a>

Equation (Q8).

There is a solution $1\leq r\leq N$ exactly when $N^2>2Nd$, or $a>N/2$. The least such $r$ gives the least designated witness total $N+r$. This three-group feasibility statement does not assign the P2 costs of additional rivals at a partial candidate prefix.

<a name="heading-research_notes-square_extensions_complete-s1-3-sharp-minimum-certificate-and-the-unbounded-comparator-bridge"></a>

### S1.3. Sharp minimum certificate and the unbounded comparator bridge
A TRUE state must observe every group. An unobserved candidate has lower corner zero and is axis-supported. An unobserved rival can be completed at zero and dominate any nonzero candidate upper corner; if that upper corner is zero, unsupportedness is impossible. A strict witness pair and (Q7) therefore require at least $2N+1$ observations in their three groups, plus one in each other group. Hence

$$
C_B^*\geq D_B:=K+2N-2.
$$

<a name="eq-research_notes-square_extensions_complete-q9"></a>

Equation (Q9).

The following single family makes this bound and the bridge sharp for every $K\geq3,N\geq1$. Repeat the candidate row

$$
p=\left(\frac1{2N},1-\frac1{4N^2}\right)
$$

$N$ times, repeat $(0,1)$ in one rival L, and repeat $(1,0)$ in each of the other $K-2$ rivals. Census the candidate and L and read one row from each remaining rival. P2 is safe because $1>p_f$ for L and $1/N>p_c$ for every other rival. A one-row rival upper corner is $(1,1-1/N)$. Giving it weight $3/(8N)$ and L the remaining weight yields

$$
\left(\frac3{8N},1-\frac3{8N^2}\right)<p.
$$

<a name="eq-research_notes-square_extensions_complete-q10"></a>

Equation (Q10).

The certificate costs $D_B$, so (Q9) is sharp, including $N=1$.

Now take any minimum bounded certificate and one of its strict pairs, with counts $a,i,j$. Census just these three groups. The realised candidate is above its old lower corner; the realised witnesses are below their old uppers. The old strict mixture remains below the realised candidate. P2 also remains safe: a rival lower corner with some coordinate above the old candidate upper remains above the smaller realised candidate in that coordinate. If it equalled the old upper in both coordinates, it either remains equal to the candidate or exceeds it in a coordinate. Raising rival lower corners cannot destroy safety.

The resulting state has a known candidate, a known strict pair and safe lower corners for every other rival, so it also forces TRUE under the unbounded-cost contract. By (Q7), its additional cost is

$$
3N-a-i-j\leq N-1.
$$

The bounded completion class is smaller, giving the other inequality. Thus

$$
C_B^*\leq C_U^*\leq C_B^*+N-1,
\qquad \frac{C_U^*}{C_B^*}\leq\frac{K+3N-3}{K+2N-2}.
$$

<a name="eq-research_notes-square_extensions_complete-q11"></a>

Equation (Q11).

In the repeated-row family above, L needs all its rows for P2 safety against $p$, while each other rival needs one. The unbounded certificate must additionally census one of those other rivals as its second witness. The unbounded comparator formula in main Section 3 therefore gives $C_U^*=K+3N-3$. The additive gap is $N-1$, and the ratio in (Q11) is attained. When $N=1$, both comparators equal $K$ and the sharp gap is zero.

<a name="heading-research_notes-square_extensions_complete-s1-4-bounded-lower-bounds-and-the-finite-parameter-bracket"></a>

### S1.4. Bounded lower bounds and the finite-parameter bracket
It is insufficient simply to change the denominator of the unbounded lower bound. For $N\geq2$, scale its fixed raw-cost embedding by $1/(2N)$. Put $f=1/(2N)$ and retain

$$
\phi(z)=\frac{3/5+z/[5(z+1)]}{N},\qquad z>0.
$$

The candidate has constant row $(f,f)$. An L threshold $u=\phi(z_L)$ uses first row $(0,1)$, zero middle rows and last row $(0,Nu-1/2)$. An R threshold $v=\phi(z_R)$ uses first row $(3/4,0)$, zero middle rows and last row $((f/v-1/2)/2,0)$. All rows lie in the square. Their means are $(0,f+u)$ and $((1+f/v)/(2N),0)$, and a strict pair is equivalent to $u<v$.

Candidate census remains compulsory: replace one unread candidate row by $(1,1)$, retaining its other actual rows. The resulting candidate cost is at least $1/N$, whereas every actual R cost is below $11/(12N)$ and its failure is zero. This is a legal dominating completion. Every rival needs a first row, which makes it P2-safe. Once the candidate is complete, any incomplete rival upper corner has both coordinates at least $1/N>f$ and imposes no restriction on supporting weights. Thus two complete witnesses are necessary. Every embedded unique-edge archive has

$$
C_B^*=N+K-1+2(N-1)=D.
$$

<a name="eq-research_notes-square_extensions_complete-q12"></a>

Equation (Q12).

The causal compression and Ramsey argument of main Section 3 now apply to these rows. Earlier rows remain fixed, and the scaling is fixed independently of the policy and its hard subset. At a no-edge history, dense rational threshold extensions provide compatible positive completions. Keeping unread candidate rows at $(f,f)$ and filling unread rival rows with $(1,1)$ gives a compatible supported completion: incomplete rival means are northeast of the candidate and completed no-edge points share a supporting weight. Hence no early answer is licensed merely by restricting the proof to positive hard inputs. The same finite-action kernels and coupling yield the randomised lower $[D+\delta_K(N-1)]/D$, with exactly the quantifiers and precision limitations of main Section 3.

For deterministic lower bounds one may instead scale every cost in the all-bad/last-good construction of main Section 3 by $1/(3N)$. Its candidate row is $(1/(3N),1/(2N))$, its anchor first row is $(1/2,0)$ and its potential L groups have first row $(0,1)$ and last row either zero or $(1,0)$. These are bounded legal rows. An unread candidate row filled by $(1,1)$ is dominated by the actual anchor; incomplete rival uppers are northeast of the candidate. The same compulsory-census and fixed-transcript argument therefore gives $KN/D$. This argument is for a fixed deterministic policy, not an adversary applied separately to private random tapes.

The unbounded blind policy has the instance bound $\mathbb E C_A\leq C_U^*+\delta_K(N-1)$. Applying (Q11) and (Q9), and writing $A_{K,N}=D+\delta_K(N-1)$, gives the square acquisition bracket

$$
\frac{A_{K,N}}{D}\leq R_B^*(K,N)\leq\frac{A_{K,N}}{D_B},
\qquad
\frac{KN}{D}\leq R_{{\rm det},B}^*(K,N)\leq\frac{KN}{D_B}.
$$

The randomised lower and upper bounds have quotient $D/D_B$ and relative gap $(N-1)/D_B$. Since $\delta_K/K\to2/3$, they squeeze the fixed-$N$ randomised limit to $(2N+1)/3$. The deterministic bounds similarly squeeze the fixed-$N$ limit to $N$. For $N=1$, every TRUE certificate observes all groups, and both acquisition ratios are one. None of these arguments asserts a joint asymptotic in varying $K,N$.

<a name="heading-research_notes-square_extensions_complete-s1-5-exact-acquisition-when-every-group-has-two-rows"></a>

### S1.5. Exact acquisition when every group has two rows
Set $N=2$. Candidate-majority necessity in (Q7) forces candidate census in every TRUE certificate. After reading it, screen each rival to its first P2-safe prefix $h_r\in\{1,2\}$. On a positive archive these are compulsory observations; write their total cost, including the candidate, as $H$. If the bounded corner test is TRUE at this state, then $C_B^*=H$ and the policy is optimal there.

Suppose the H-state is not TRUE. It is P2-safe, so it lacks robust unsupportedness. Two one-row witnesses cannot make a strict pair, since (Q5) fails at $(a,i,j)=(2,1,1)$. Suppose a later certificate instead uses a one-row witness and an opposite full witness. Exchange the coordinate names if necessary so that the partial upper has failure below $p_f$ and the full witness has cost below $p_c$. The partial upper failure is at least $1/2$, so $p_f>1/2$. The full witness's first lower cost is at most its complete cost, hence below $p_c$, and its first lower failure is at most $1/2<p_f$. Its first prefix therefore strictly dominates $p$ and is not P2-safe: this witness was already censused during screening. The partial witness's first prefix was also available at H. Their strict pair would already have made H TRUE, a contradiction. All comparisons excluding safe equality here are strict.

Consequently every positive certificate after a non-TRUE H-state requires two complete witnesses. Its minimum is exactly the unbounded decomposition with the same candidate and safe prefixes:

$$
C_B^*=C_U^*\geq K+3.
$$

<a name="eq-research_notes-square_extensions_complete-q13"></a>

Equation (Q13).

Stop at H if TRUE; otherwise use the balanced residual policy. On the latter positive class its additive overhead is at most $\delta_K$, giving ratio at most $1+\delta_K/(K+3)$. A deterministic policy can instead census the remaining rows, giving at most $2K/(K+3)$. The respective bounded lower constructions in Section S1.4 match these bounds, proving the two-row square theorem. At $K=3$ both equal one. On negative archives, sound early rejection or census and exact evaluation supplies a finite fallback. No positive-input promise is supplied to either policy.

All arguments count exact disclosures under the stated completion contract. They make no assertion about measurement noise, physical independence, radio energy or historical priority.


<a name="heading-research_notes-square_extensions_complete-s1-6-three-configurations-and-three-rows"></a>

### S1.6. Three configurations and three rows
For $K=N=3$, (Q5) leaves only candidate prefix two with witness prefixes three and three, or candidate prefix three with witness prefixes $(1,3)$, $(3,1)$, $(2,3)$, $(3,2)$ or $(3,3)$. Thus every positive archive has $C_B^*\in\{7,8,9\}$.

**Theorem S1.** Under the full bounded product-completion contract,

$$
R_B^*(3,3)=25/23,\qquad R_{{\rm det},B}^*(3,3)=9/8.
$$


First, every cost-seven certificate is discovered by candidate census followed by mandatory P2 screening and an immediate robust TRUE test. Such a certificate has prefixes $(3,1,3)$ or $(3,3,1)$. Orient the one-row witness upper corner so that its second coordinate is below the candidate's. That coordinate is at least $2/3$, so the candidate's second coordinate exceeds $2/3$. The opposite full witness improves the first coordinate. Its first two lower corners therefore lie strictly below the candidate in both coordinates: the first coordinate is no larger than its improving full mean, and the second is at most $2/3$. That witness needs all three rows for P2 safety. The partial witness is already safe at one row. Screening therefore reaches exactly the cost-seven certificate. Full census otherwise costs at most nine, giving the deterministic upper $9/8$.

For the randomised upper, define two complete blind policies. Policy A censuses the candidate, screens both competitors to their first P2-safe prefixes and tests robust TRUE before any prefetch. If necessary, it raises unfinished competitor prefixes to two, checking TRUE along the way, then reveals their last rows in a fresh uniform order. Policy B reads candidate prefix two and both competitors completely, tests TRUE at cost eight and otherwise reads the candidate's final row. Screening failure or a negative answer is handled by sound FALSE detection or full census. Both policies terminate within nine queries on every input.

Policy A costs seven when $C_B^*=7$. On a cost-eight archive admitting a candidate-census certificate, its expected cost is at most $17/2$. If screening has already completed one competitor, extending the other to prefix two reaches that certificate by cost eight. Otherwise, after state $(3,2,2)$ at least one of the two final competitor rows completes a certificate, and their order is fair. Policy B costs eight whenever $(2,3,3)$ is a certificate. Choose A with probability $16/23$ and B with probability $7/23$, independently of observations. The exhaustive retrospective classes give the following bounds; certificate types are used only in the analysis.

Table S1. Policy bounds by positive certificate class in the three-row square.

| Positive certificate class | Policy A cost bound | Policy B cost bound | Mixture ratio bound |
|---|---:|---:|---:|
| $C_B^*=7$ | $7$ | $9$ | $25/23$ |
| $C_B^*=8$, admits $(2,3,3)$ | $9$ | $8$ | $25/23$ |
| $C_B^*=8$, no $(2,3,3)$ | $17/2$ expected | $9$ | $199/184$ |
| $C_B^*=9$ | $9$ | $9$ | $1$ |

For a matching lower, fix two archives before the algorithm's coins. Candidate rows one and two are $(3/8,7/8)$; left rows one and two are $(0,1)$; right rows one and two are $(7/8,0)$ and $(5/8,0)$. The left final row is $(0,7/8)$ in both archives. The distinguishing tails and unique cheapest certificates are:

Table S2. The two fixed square archives used for the matching lower bound.

| World | Candidate final row | Right final row | Minimum TRUE prefixes | $C_B^*$ |
|---|---|---|---|---:|
| A | $(0,0)$ | $(3/8,0)$ | $(2,3,3)$ | $8$ |
| D | $(0,1)$ | $(1,1)$ | $(3,3,1)$ | $7$ |

In A the complete means are $p=(1/4,7/12)$, $L=(0,23/24)$ and $R=(5/8,0)$. At candidate prefix two, $U_a=(7/12,11/12)$ is robustly P2-safe. The mixture $17L/28+11R/28=(55/224,391/672)$ is strictly below $L_a=p$, with coordinate gaps $1/224$ and $1/672$. With the candidate complete, a left prefix below two is P2-unsafe. At left prefix two and full right, both competitor upper costs exceed $1/4$, so the cost axis supports p. With left full and right prefix two, weights $(1,1)$ support p. Shorter states cannot force TRUE. The only TRUE states are $(2,3,3)$ and full census.

In D, $p=(1/4,11/12)$, $L=(0,23/24)$ and $R=(5/6,1/3)$. At candidate prefix two its lower corner is supported by weights $(1,1)$ even when competitors are full. Candidate census is mandatory. P2 then requires all three left rows, while the first right lower cost is $7/24>1/4$. Its upper corner is $(23/24,2/3)$. Weight $4/5$ on L and $1/5$ on that corner gives $(23/120,9/10)<p$. Exactly $(3,3,1)$, $(3,3,2)$ and full census force TRUE.

Histories in the two worlds agree until either the candidate's third row or the right competitor's third row is queried. Let $q$ be the probability that the candidate tail is queried first. The first choice has the same law on both fixed archives. In A, that choice destroys access to the unique cost-eight certificate, giving expected cost at least $8+q$. In D, querying the right tail first forces nine queries, giving at least $9-2q$. Consequently every randomised algorithm has worst ratio at least $\max\{1+q/8,(9-2q)/7\}$, whose minimum is $25/23$ at $q=16/23$. Equivalently, ratio-prior weights $16/23$ on A and $7/23$ on D give a constant lower $25/23$. They must not be confused with the raw-cost prior $(2/3,1/3)$. A deterministic first choice gives a worst ratio at least $9/8$. This proves both equalities.

The unbounded values at $K=N=3$ are both one, and the same two archives have $C_U^*=9$. Tightening the domain therefore increases the optimal relative ratio by reducing its certificate benchmark; this does not assert an increase in absolute information-acquisition cost. The cost-seven screening argument also gives the deterministic upper $3K/(K+5)$ for every $K\geq3,N=3$: all archives attaining $C_B^*=K+4$ stop at that screening state. No matching general-$K$ equality is claimed.

For $K=N=3$, a public compulsory setup charge $F\geq0$, paid equally by algorithm and certificate and revealing no information, changes these exact square ratios to $1+2/(3F+23)$ randomised and $1+1/(F+8)$ deterministic. Section S5.2 supplies the balancing probability, matching lower and accounting qualifications.

