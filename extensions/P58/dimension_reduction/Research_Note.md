---
title: "When can many objectives be reduced to two?"
subtitle: "Exact obstructions, planar subproblems and certified transfer of paid-prefix certificates"
author: "Research working note prepared for Antonio Clim"
date: "25 October 2026"
lang: en-GB
geometry: margin=25mm
fontsize: 11pt
colorlinks: true
---

\newpage

**Status.** This is an AI-assisted research derivation and verification record. It is not a submitted article, a claim of historical novelty or an edit to the canonical SICOMP manuscript. The statements have self-contained proofs, independent adversarial review and the finite checks identified below. Finite checks do not replace proofs. No field deployment, economic benefit or new unrestricted competitive ratio is claimed.

# Research question and answer

Can a catalogue evaluated by $d$ minimised criteria be reduced to two criteria while retaining the property that a nominated alternative is nondominated and unsupported by every nonzero nonnegative weighted sum?

There are four distinct answers.

1. **No universal single reduction:** nonnegative affine aggregation can require all $d$ criteria, even when chosen after inspecting the complete catalogue. The obstruction has a fixed positive margin.
2. **An exact family of planar tests for three alternatives:** unsupportedness can be checked through all pairs of original criteria, with nondomination checked separately in the original space. This requires no rank-two assumption.
3. **Exact structural reduction to one plane:** a nondegenerate affine family of intrinsic dimension two admits two anchor criteria preserving both dominance and support. Under a public raw-row correspondence, all prefix certificates and paid costs are preserved too.
4. **Certified approximation:** valid reconstruction-error bounds and sufficient margins allow an exact original verdict from a two-coordinate calculation. Failure of the sufficient test requires further analysis, not rejection of the candidate.

These statements distinguish a smaller representation, a family of small computations and an information-cost reduction. They are not interchangeable.

# Definitions

Let $P=\{p_A,p_1,\ldots,p_{K-1}\}\subset\mathbb R^d$ be a finite labelled catalogue. All criteria are minimised. A rival dominates $p_A$ if it is no larger in every coordinate and strictly smaller in at least one. Candidate $A$ is supported if

$$
\exists w\in\mathbb R_+^d\setminus\{0\}\quad
w^Tp_A\le w^Tp_g\quad\text{for every rival }g.
$$

Ties and axis weights count as support. Write GOOD for nondominated and unsupported. Weight normalisation $\sum_iw_i=1$ does not change rankings.

For finite catalogues, unsupportedness is equivalent to a convex combination of rivals strictly below the candidate in every coordinate:

$$
\exists\lambda_g\ge0,\quad\sum_g\lambda_g=1,
\qquad\sum_g\lambda_gp_g<p_A.
$$

This is a classical separation/minimax consequence, also used in Supplementary S5.7. The mixture is a geometric witness; it need not be an operationally admissible decision.

# Theorem 1: robust impossibility of adaptive monotone affine compression

**Statement.** For every $d\ge3$ and $1\le m<d$, some GOOD candidate in $[0,1]^d$ loses this property under every nonnegative affine map to $m$ objectives, even when the map is selected after inspecting the catalogue. For nonconstant output objectives, positive row normalisation yields false projected domination with margin at least $1/4$.

**Construction and proof.** Set

$$
p_A=\tfrac34\mathbf1,\qquad p_i=e_i\quad(1\le i\le d).
$$

Each rival is worse than $A$ in its own coordinate, hence cannot dominate it. The mean of any two distinct rivals is at most $\tfrac12\mathbf1$, strictly below $p_A$, so $A$ is unsupported with a two-rival witness and margin at least $1/4$.

Write a proposed map as $T(x)=c+Wx$, $W\ge0$. Offsets cancel in comparisons. A zero row gives a constant criterion whose axis weight supports every projected alternative, already destroying GOOD. Otherwise divide each row by its positive sum; such changes of units preserve the verdict. Each row now sums to one, so $Wp_A=\tfrac34\mathbf1$.

At most one coefficient in each row can exceed $1/2$. Fewer than $d$ rows leave some coordinate index $i$ with coefficient at most $1/2$ in every row. Thus

$$
Wp_i\le\tfrac12\mathbf1<\tfrac34\mathbf1=Wp_A.
$$

The projected rival strictly dominates $A$. This proves the claim and its margin. $\square$

Two rivals can therefore witness unsupportedness while all $d$ aggregate coordinates remain necessary to protect nondomination. The theorem covers ordinary nonnegative weighted aggregation and coordinate selection. It does not exclude arbitrary encodings of real numbers, unrestricted signed transformations or maps which first solve and then encode the answer.

## Quantitative refinement

For $p_A=q\mathbf1$, $q>1/2$, define the best strict separation margin over $m$ row-stochastic nonnegative aggregation rows:

$$
\tau_m=\max_W\min_i\max_s(W_{si}-q).
$$

Then

$$
\tau_m=\frac1{\lceil d/m\rceil}-q.
$$

Assign each coordinate to a row attaining its maximum coefficient. Some row receives at least $\lceil d/m\rceil$ coordinates; one assigned coefficient is at most the reciprocal of this number. This proves the upper bound. A balanced partition of the coordinates, with each row uniform on its assigned group, attains it. For $m>d$, repeat singleton rows. At $m=2,q=3/4$, the forced domination margins for $d=5,20,50$ are at least $5/12$, $13/20$ and $71/100$ in normalised output coordinates. These are constructed mathematical bounds, not measured application errors.

# Theorem 2: sparse supporting weights and exact planar subproblems

**Statement.** With $m=K-1\ge1$ rivals, a supported candidate admits a supporting weight with at most $\min(d,m)$ nonzero entries.

**Proof.** For criterion $i$, form the column

$$
v_i=((p_g-p_A)_i)_{g=1}^{m}\in\mathbb R^m.
$$

Support is equivalent to $Q=\operatorname{conv}\{v_1,\ldots,v_d\}$ intersecting $\mathbb R_+^m$. If the affine dimension of $Q$ is at most $m-1$, Caratheodory's theorem represents any feasible point using at most $m$ columns. Otherwise $Q$ is full-dimensional. From a feasible $z\ge0$, move in direction $\mathbf1$ until reaching the boundary of the compact polytope $Q$. The endpoint remains nonnegative and lies in a proper face of dimension at most $m-1$. Caratheodory on that face again gives at most $m$ columns. The convex coefficients are the required supporting weights. The additional bound $d$ is immediate. $\square$

**Three-alternative corollary.** For $K=3$ and $d\ge2$,

$$
\text{$A$ is unsupported in $d$ dimensions}
\quad\Longleftrightarrow\quad
\text{$A$ is unsupported in every two-coordinate projection}.
$$

Indeed, a supporting weight on any projection extends by zeros to the original problem, while the theorem supplies a projection whenever full support exists. Axis support is included in pairs. The direct procedure uses $\binom d2$ planar support tests: 10, 190 and 1,225 for 5, 20 and 50 criteria.

**Nondomination is checked separately in all original coordinates.** Do not require every planar projection to be nondominated: that would be a different and overly strong condition. Thus the full GOOD verdict can be computed exactly by an original-space nondomination scan plus these planar support tests.

This decomposition also applies to the supporting-weight feasibility test at a prefix in Supplementary S12: use columns of the corner differences $U_g-L_A$. Its exact applicability requires the original endpoint hypotheses of S12. It changes the internal way a predicate is evaluated; it does not eliminate the cost of revealing original rows or transfer a planar acquisition ratio.

For general $K$, the same argument uses coordinate subsets of size at most $K-1$. It does not provide a universal family of pair tests when there are more rivals.

## A faster three-alternative calculation

For two rivals, unsupportedness is also the existence of $\lambda\in[0,1]$ such that

$$
\lambda p_L+(1-\lambda)p_R<p_A
$$

in every coordinate. Each coordinate supplies an open linear inequality on one scalar. Their feasible intervals can be intersected in one scan, with careful treatment of zero slopes and open boundaries. Thus the family of pair tests is an exact decomposition, not a claim that $\binom d2$ computations are necessary. The direct interval method uses $O(d)$ rational comparisons after the vectors are available. This is a classical one-dimensional feasibility calculation and does not constitute a new paid-query bound.

At an incomplete prefix, failure of the robust TRUE condition means that TRUE is not yet forced. It is not automatically a forced FALSE verdict: other legal completions may remain positive. A correct acquisition policy must preserve this distinction and may continue to census.

# Theorem 3: exact reduction through two anchor criteria

Suppose every vector in a specified family has the form

$$
x(y)=b+My,\qquad y\in Y\subset\mathbb R^2,
$$

where $b$ is common to all alternatives, $M\ge0$, no row of $M$ is zero and two rows are positive multiples of $(1,0)$ and $(0,1)$. Then the same map preserves, in both directions, every Pareto relation and every supported/unsupported label on every finite catalogue in the family.

**Proof.** If $y\le z$, nonnegativity gives $My\le Mz$ and an anchor detects each strict inequality. Conversely, the anchor rows imply $y\le z$ from $My\le Mz$. Thus ties and strict domination agree. For support,

$$
w^Tx(y)=w^Tb+(M^Tw)^Ty.
$$

Every nonzero nonnegative $w$ gives a nonzero nonnegative $M^Tw$, because no row of $M$ is zero. Conversely, every nonzero nonnegative two-dimensional weight is obtainable by placing suitable weights on the two anchor rows. The families of weighted rankings therefore coincide exactly. $\square$

The nonzero-row condition matters: a constant criterion supports every alternative through its axis weight. Nonnegative aggregation without the two anchor directions also need not reflect domination.

## Rank-two affine dichotomy

Suppose $x(z)=b+Bz$, $\operatorname{rank}B=2$, with signed entries allowed in $B$. If there is $w\ge0$, $w\ne0$ satisfying $B^Tw=0$, the scalarisation is constant, so every alternative is supported. Otherwise two original coordinates provide the anchors in Theorem 3.

To prove the latter claim, the cone generated by the rows of $B$ is full-dimensional, pointed and has no zero generating row. A line in that cone would supply positive representations of $v$ and $-v$ and hence an excluded nonnegative kernel vector. A finitely generated pointed planar cone has two extreme rays, each containing a generating row. Select those two rows as an invertible matrix $Q$. Every other row is a nonnegative nonzero combination, so $B=MQ$. Put $y=Qz$ and apply Theorem 3.

This is an exact structural restriction, not an assertion that $d$ independent criteria have rank two. Its geometric mechanism belongs to established objective-redundancy and cone-reduction theory.

# Proposition 4: a positive three-alternative catalogue has one planar representation

If a fully known catalogue of exactly three alternatives in $\mathbb R^d$ contains a GOOD candidate, two original coordinates can be selected preserving all pairwise domination relations and all three support labels on that catalogue.

**Direct proof.** Put $v=p_L-p_A$, $u=p_R-p_A$. Unsupportedness gives

$$
\lambda v+(1-\lambda)u<0,\qquad 0<\lambda<1.
$$

An endpoint would make one rival dominate $A$, so neither endpoint can supply this witness. Neither rival can duplicate $A$ for the same reason. Nondomination supplies $i$ with $v_i>0$ and $j$ with $u_j>0$. The strict mixture forces $u_i<0$ and $v_j<0$, hence $i\ne j$.

Projection onto $(i,j)$ keeps each rival worse than $A$ in one coordinate, and keeps the strict mixture below $A$. Candidate $A$ remains GOOD. Rival $L$ uniquely wins criterion $j$ and rival $R$ uniquely wins criterion $i$; all three are pairwise incomparable. The same statements hold in the full space. Thus every support label and domination relation is preserved. $\square$

This is a full-information, catalogue-dependent representation. A positive verdict is a premise. A projected positive verdict cannot establish that premise: $A=(.6,.6,0)$, $L=(0,1,1)$, $R=(1,0,1)$ give a positive first-two-coordinate projection while the third axis supports $A$ originally.

Theorem 2 supplies a valid way to check full unsupportedness before using this compact explanation. Proposition 4 does not grant an online policy access to unknown full means. It also does not contradict Theorem 1, whose difficult catalogue has $d+1$ alternatives.

# Theorem 5: exact preservation of paid-prefix certificates and costs

Assume Theorem 3's structure is public, exact and computationally usable at the raw-row level. Every legal full row is $x=b+My$ for exactly one legal latent row, and conversely. Require identical archive lengths, order, initial information, whole-row query rule and public disclosure prices. All admissible complete archives, including public dependencies, must correspond bijectively.

For public positive weights normalised within each alternative,

$$
p_g=\sum_j\omega_{gj}x_{gj}
=b+M\sum_j\omega_{gj}y_{gj}.
$$

A prefix forces TRUE, forces FALSE or remains undecided in one representation if and only if its counterpart does so in the other. Certificate costs and the hindsight comparator $C^*$ are identical. Every causal acquisition policy can be simulated with identical paid query paths.

**Proof.** The anchors recover the latent row and the public map reconstructs the full row. Query responses are informationally equivalent. The archive bijection restricts to a bijection of every prefix's compatible completions. Theorem 3 preserves GOOD on every completion, hence preserves forced verdicts and certificate sets. Prices coincide, giving identical certificate costs and minima. Translate each observed response before simulating a policy's next action; coupling random coins yields identical paid paths. $\square$

This preserves paid information costs, not necessarily CPU time. Discovering the map from hidden data is not free preprocessing. A relationship fitted only to complete means does not constrain unread rows unless genuinely included in the public model.

## Conditional inheritance of $87/80$

If the induced latent domains satisfy the existing triangle theorem or its eligible independent endpoint-containing subdomains, and the remaining three-alternative, equal-length, unit-price and observation assumptions hold, its bound transfers without loss to the $d$-coordinate representation.

For example, retain $c,f$ with $0\le f\le c\le1$ and define 48 further criteria as public mixtures $\alpha_i c+(1-\alpha_i)f$, $0\le\alpha_i\le1$. This gives 50 coordinates with two independent ones. Under identical disclosure rules, $C^*$ and the existing ratio are preserved exactly.

This is a result for a structurally restricted family, not a new competitive ratio for 50 independent objectives. A general induced two-dimensional domain need not be triangular. Arbitrary coordinate-specific prices, additional free information or hidden-data preprocessing can invalidate the cost equivalence.

# Theorem 6: exact positive certification with bounded reconstruction error

Let reconstructed vectors $\widehat p_g$ have valid deterministic bounds

$$
|p_{gi}-\widehat p_{gi}|\le e_{gi}.
$$

It is sufficient for the original candidate to be GOOD that each rival has some coordinate with

$$
\widehat p_{gi}-\widehat p_{Ai}>e_{gi}+e_{Ai},
$$

and that some rival mixture satisfies, for every coordinate,

$$
\widehat p_{Ai}-\sum_g\lambda_g\widehat p_{gi}
>e_{Ai}+\sum_g\lambda_ge_{gi}.
$$

**Proof.** The first inequality leaves each actual rival strictly worse in at least one coordinate after subtracting the full possible errors. The second leaves the actual mixture strictly below the actual candidate in every coordinate after subtracting its full error budget. These prove nondomination and unsupportedness respectively. $\square$

With uniform error $\varepsilon$, strict margins greater than $2\varepsilon$ suffice. The factor and strictness cannot be relaxed using only these bounds. Take

$$
\widehat p_A=(.5,.5),\quad\widehat p_L=(.1,.7),\quad
\widehat p_R=(.7,.1),\qquad\varepsilon=.05.
$$

The mixture gap is $.1=2\varepsilon$, while the nondomination margins are $.2>2\varepsilon$. Permitted true values

$$
p_A=(.45,.45),\quad p_L=(.15,.75),\quad p_R=(.75,.15)
$$

all have coordinate sum $.9$. Equal weights support $A$: the strict unsupported verdict is lost exactly at the boundary.

## A two-coordinate sufficient test

Retain two exact original anchor criteria $z_g$ and assume

$$
p_{gi}=b_i+B_{i1}z_{g1}+B_{i2}z_{g2}+r_{gi},
\quad B_{ik}\ge0,\quad s_i=B_{i1}+B_{i2}>0,
\quad |r_{gi}|\le s_i\eta_g.
$$

Suppose each rival is strictly worse in at least one retained anchor and a two-dimensional rival mixture satisfies

$$
z_A-\sum_g\lambda_gz_g\ge\rho\mathbf1,
\qquad\rho>\eta_A+\sum_g\lambda_g\eta_g.
$$

Then the original candidate is GOOD. The anchors prove nondomination; the true mixture gap in original coordinate $i$ is at least

$$
s_i\left(\rho-\eta_A-\sum_g\lambda_g\eta_g\right)>0,
$$

proving unsupportedness. Under uniform tolerance $\eta$, $\rho>2\eta$ suffices.

The final verdict can therefore be exact despite approximate reconstruction. This does not guarantee that a useful reconstruction exists: Theorem 1 rules out that inference even for well-separated original data. Duplicate anchor vectors need additional checking, because omitted residuals can introduce domination.

Residual bounds must cover every relevant alternative and, during acquisition, every compatible unseen completion. An empirical average error or correlation is insufficient. If this sufficient test fails, return UNKNOWN and continue original-space verification. Approximate transfer alone preserves neither $C^*$ nor the ratio $87/80$.

# Nonlinear maps and limits of the research claim

Preserving domination is weaker than preserving supportedness. For $A=(.6,.6)$, $L=(0,1)$, $R=(1,0)$, candidate $A$ is unsupported. Cubing both coordinates preserves every pairwise domination relation but turns $A$ into $(.216,.216)$, which uniquely wins equal weights.

Nor can every domination order be embedded in two coordinates by an arbitrary nonlinear map. The classical standard example uses $a_i=e_i$, $b_i=\mathbf1-e_i$ in dimension $d\ge3$. It has $a_i\le b_j$ exactly when $i\ne j$. In an order-reflecting representation with $m<d$ coordinates, each missing comparison $a_i\not\le b_i$ needs a coordinate with $F(a_i)>F(b_i)$. Two indices must use the same coordinate. Their two cross-comparabilities then give a strict circular inequality, which is impossible. This is an order-dimension obstruction (Dushnik & Miller, 1941), not an impossibility result for arbitrary encodings of one Boolean answer.

A rowwise transformation commuting with all weighted means on a convex domain is affine. Requiring preservation of the coordinatewise minimisation direction on a full-dimensional domain makes its coefficients nonnegative. These requirements explain why the class of Theorem 1 is relevant to additive archive objectives.

# Executed verification and its limits

The accompanying scripts and JSON receipts distinguish exact rational checks from numerical solver cross-checks. Their input families are synthetic. The written proofs establish the universal statements; no finite test count establishes a universal theorem.

| Control | Completed coverage | Outcome |
|:--|:--|:--|
| General-dimensional support decomposition | 2,000 cases at $d=2,3,5,20,50$; 1,340 supported and 660 unsupported | Exact pair tests and exact interval intersection agree; independent floating-point LP agrees |
| Strict interval boundaries | 9 controls, including ties, open boundaries and endpoint errors | All pass |
| Fully known three-alternative projections | All 41,664 unordered catalogues from $\{0,1,2,3\}^3$; 423 positive catalogues | Every positive case has the stated two-coordinate projection |
| Nonnegative-aggregation obstruction | 687 matrices at $d=3,5,20,50$ | All destroy nondomination as proved |
| Exact anchor transformation | 2,187 complete-archive verdict comparisons | All equal |
| Prefix certificate transformation | 57,963 prefix comparisons, including 33,852 designed positive-family prefix states | All equal |
| Hindsight positive certificate costs | 12 positive comparisons with heterogeneous prices | All equal in 2, 5, 20 and 50 coordinates |
| Approximate two-anchor transfer | 400 rational cases at $d=2,5,20,50$, plus 4 boundary/tie controls | All pass |

The two-row endpoint-alphabet catalogues in the anchor verifier contain no positive examples. This nonpositive result is explicitly retained, not treated as positive validation. Separate rational positive archives of lengths 8 and 16 supply the positive comparator checks. With the declared heterogeneous prices and common setup 17, their costs are respectively $C^*=163$ versus full acquisition 173 and $C^*=450$ versus full acquisition 521, identically in each transformed dimension. These are designed cost-accounting examples, not monetary measurements and not tests of the unit-price $87/80$ bound.

The support-decomposition verifier compares two exact rational methods with a full-dimensional SciPy/HiGHS numerical LP. Its LP component is corroboration, not an exact solver certificate. The reduction verifier additionally makes 100 separately labelled numerical LP comparisons. The package records versions and seeds. Reported local execution durations are diagnostics only, not performance benchmarks.

No real-data residual bounds, production deployment, economic benefit or external peer review were established. The canonical manuscript, supplement and published releases have not been modified.

# Position relative to the manuscript and existing research

Supplementary S5.6 already proves fixed-dimensional endpoint certificates and a sharp rival-witness bound. It does not by itself reduce the number of criteria. S5.7 already gives margin-based sufficient certificates. The results here connect those facts to exact predicate decomposition, structural criterion reduction and error-controlled transfer.

Objective reduction is established prior work. Brockhoff and Zitzler (2009) study exact and approximate dominance preservation. Saxena et al. (2013) present linear and nonlinear reductions tested up to 50 objectives, conditional on the number of essential objectives. Lindroth et al. (2010) study approximation through reduced objective sets. Löhne and Zillmann's current preprint gives rank-based reduction with a transformed ordering cone. Generic objective reduction, geometric rank reduction, Helly and Caratheodory consequences must not be presented as newly invented here.

The exact planar-subproblem result is a classical convex-geometric consequence specialised to the manuscript's predicate. The explicit preservation of observable transcripts, admissible completions, certificate sets and paid costs is a well-defined candidate addition to the current work. No source inspected in this bounded search established that entire combination, but this absence is not evidence of priority. A full novelty assessment remains separate from the correctness of these derivations.

The research supports general predicate verification for three alternatives, conditional exact structural reduction and certified sufficient approximation. It does not support universal replacement of arbitrary independent objectives by two fixed criteria, or a new unrestricted many-objective acquisition ratio.

\newpage

# References

Brockhoff, D., & Zitzler, E. (2009). Objective reduction in evolutionary multiobjective optimization: Theory and applications. *Evolutionary Computation, 17*(2), 135-166.

<https://doi.org/10.1162/evco.2009.17.2.135>

Dushnik, B., & Miller, E. W. (1941). Partially ordered sets. *American Journal of Mathematics, 63*(3), 600-610.

<https://doi.org/10.2307/2371374>

Lindroth, P., Patriksson, M., & Strömberg, A.-B. (2010). Approximating the Pareto optimal set using a reduced set of objective functions. *European Journal of Operational Research, 207*(3), 1519-1534.

<https://doi.org/10.1016/j.ejor.2010.07.004>

Löhne, A., & Zillmann, P. (2026). *Low-rank multi-objective linear programming* (Version 3) [Preprint]. arXiv. First submitted in 2025; version 3 dated 25 September 2026.

<https://doi.org/10.48550/arXiv.2508.20880>

Saxena, D. K., Duro, J. A., Tiwari, A., Deb, K., & Zhang, Q. (2013). Objective reduction in many-objective optimization: Linear and nonlinear algorithms. *IEEE Transactions on Evolutionary Computation, 17*(1), 77-99.

<https://doi.org/10.1109/TEVC.2012.2185847>

The source manuscript and supplement are the user-provided P57 working versions, including Supplementary S5.6-S5.8, pages 34-38. This note assigns no new DOI or publication status to those working versions.
