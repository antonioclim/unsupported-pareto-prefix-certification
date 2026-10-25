# P56: dimensional, weighted-archive and margin extensions

Date: 25 October 2026. Research note, not a change to the canonical P55 private manuscript or the published software. No journal submission has been made. The following are analytic derivations for this project, with explicitly scoped finite corroboration. They are not claims of first historical discovery. These extensions do not themselves improve the P55 triangle minimax interval; the separate P56 upper-bound track reports an additional 87/80 upper result, which is outside this note.

## Executive assessment

Three additions withstand a direct proof:

1. **Geometric margin implies guaranteed disclosure savings.** For strictly separated positive archives, a simple causal lockstep policy must stop before census. The guarantee is independent of record order, needs no stochastic model and does not need the margins as policy input. The universal factor two in the bound is sharp. This provides a mathematical mechanism linking geometry to possible operational savings, without claiming measured monetary savings.
2. **The certificate framework extends to arbitrary fixed objective dimension, unequal archive lengths, positive importance weights and arbitrary positive disclosure prices.** An exact certificate comprises the candidate prefix, a necessary safety prefix for every rival, and at most d rival witness prefixes. The dimension bound is sharp. It yields a polynomial retrospective comparator for fixed d. The geometric Helly ingredient is classical; the contribution is its correct integration into this paid-prefix certificate framework.
3. **The unbounded acquisition theorem is intrinsically two-dimensional.** In d>=3, candidate census can be unnecessary even with an unbounded first objective. A simple exact family allows a candidate observation fraction arbitrarily close to 1/(d-1). This is a useful boundary result: the higher-dimensional certificate framework generalizes, but the exact two-dimensional acquisition ratios cannot simply be transplanted.

There is also an independently checked planar comparator improvement by the geometry track, from the already present O(K²N²) retrospective algorithm to O(KN² log K); see the separate geometry report. This note does not claim the older O(K²N²) result as new.

## 1. Margin-to-disclosure theorem

Consider d>=2 objectives, independently completable rows in an endpoint-containing subdomain of [0,1]^d. Configuration g has n_g rows with public importance weights alpha_gj>0, sum_j alpha_gj=1. The complete objective is p_g=sum_j alpha_gj z_gj. These importance weights are distinct from disclosure prices. Let A be the designated candidate. Define

- delta_g = max_l (p_gl-p_Al), for every rival g;
- choose a probability vector lambda over rivals and gamma>0 with sum_g lambda_g p_g <= p_A-gamma*1 coordinatewise.

Assume delta_g>0 for every rival. This excludes a rival exactly coinciding with the candidate; it does not assert that such coincidences are impossible in the original model. Unsupportedness supplies a strict convex-mixture witness by the theorem of alternatives, but nondomination alone supplies only delta_g>=0.

At a prefix b, write r_g=sum_{j>b_g} alpha_gj for the unread importance mass. Then the following conditions suffice for a robust TRUE certificate:

\[
r_A+r_g<\delta_g\quad\hbox{for every rival }g,
\qquad
r_A+\sum_g\lambda_g r_g<\gamma.
\tag{M1}
\]

**Proof.** Since every unread coordinate is between zero and one,

\[
L_g\ge p_g-r_g\mathbf1,\qquad U_g\le p_g+r_g\mathbf1.
\]

Choose a coordinate attaining delta_g. In that coordinate,

\[
L_{g\ell}-U_{A\ell}\ge p_{g\ell}-p_{A\ell}-r_g-r_A>0.
\]

Thus no rival lower corner can dominate the candidate upper corner. Also,

\[
L_A-\sum_g\lambda_g U_g
\ge p_A-\sum_g\lambda_g p_g
       -(r_A+\sum_g\lambda_g r_g)\mathbf1>0.
\]

The same mixture of upper rival corners is strictly below L_A in every coordinate. Every nonzero nonnegative scalarisation therefore has a strictly better rival. The endpoint criterion proves TRUE. In fact the sufficient part uses boundedness only; endpoints/independence are needed for the exact endpoint equivalence, not for this sufficient implication. No hidden independence assumption about a sampling distribution appears. QED.

### Equal-length unit-weight corollary

For n_g=N and alpha_gj=1/N, put

\[
\mu=\min\{\gamma,\min_{g\ne A}\delta_g\}>0,
\quad
q=\left\lceil N\mu/2\right\rceil-1.
\tag{M2}
\]

The maximum integer q satisfying q/N<mu/2 is exactly the quantity above. A lockstep policy reads one additional row from each configuration per round, checks robust TRUE after each legal acquisition, and otherwise finishes census and evaluates the complete predicate. It is causal and correct on both signs. On every archive satisfying the stated margins it returns TRUE by the end of round N-q. Hence

\[
C_{\rm lockstep}(I)\le K(N-q),\qquad
KN-C_{\rm lockstep}(I)\ge Kq.
\tag{M3}
\]

A common compulsory setup F adds F to both costs and does not change the saved disclosures. For a common disclosure tariff tau>0, avoided disclosure charges are at least tau*Kq; this is a conditional accounting identity, not an observed economic effect. General row prices retain the certificate guarantee but require summing the actually skipped tail tariffs.

The margins are **retrospective descriptors for the theorem**, not free oracle information given to the online policy. The policy runs the existing exact endpoint test. The result is an upper bound against full census; it is not a new competitive-ratio guarantee against C* and does not improve 12/11.

A useful intrinsic choice is

\[
\gamma_*=
\max_{\lambda\in\Delta_{K-2}}
\min_\ell\left(p_{A\ell}-\sum_g\lambda_g p_{g\ell}\right).
\]

It is positive exactly when no nonzero nonnegative supporting weight exists. Finite-dimensional minimax or separation gives this equivalence. One may use any explicit positive witness margin instead of solving this retrospective LP.

### A triangle example with explicit savings

Take complete means

\[
p_A=(7/8,3/8),\qquad p_L=(1/2,1/2),\qquad p_R=(1,0).
\]

They lie in the original triangle. The candidate is nondominated, delta_L=delta_R=1/8, and the equal mixture of the rivals is (3/4,1/4), giving gamma=1/8. Thus every archive order with these complete means has a lockstep certificate whenever the unread fraction is less than 1/16.

At N=160, q=9, so the theorem guarantees at least 27 avoided disclosures out of 480, i.e. 5.625%. This is a proved guarantee for the stated mean vectors and bounded rows, not an empirical data result. As N grows the guaranteed fraction approaches 6.25% from below. A repeated-row instance with the same means stops at b=143 in every group and saves 51/480=10.625%; that latter figure is an exact designed example, not a measured application.

### Sharpness of the universal factor two

The strict cutoff in (M2) cannot generally be weakened to r<=mu/2 or to a denominator below two based only on the displayed margins. Use N=160 and the same complete means, with ordered rows:

- A: 60 copies of (1,1), 80 of (1,0), 20 of (0,0);
- L: 70 copies of (1,1), 80 of (0,0), 10 of (1,1);
- R: 160 copies of (1,0).

At the common prefix b=150, r=1/16 and

\[
L_L=(7/16,7/16),\qquad U_A=(15/16,7/16).
\]

The rival lower corner dominates the candidate upper corner, so the prefix is not TRUE, although the complete means have delta=gamma=1/8. The missing endpoint choices witnessing domination are legal. Since r=mu/2<mu/c for every c<2, the same example rules out replacing the universal factor two by any smaller constant in this form of the theorem. At b=151, (M1) is strict and TRUE is guaranteed. This is a sharpness claim for the margin-only sufficient bound, not for all possible policies.

## 2. Endpoint certificates in arbitrary dimension and weighted archives

Let d>=2. Configuration g contains n_g fixed ordered rows in D_gj subset [0,1]^d, with 0 and 1 in every D_gj. Completions of distinct rows are independent. The public weights alpha_gj>0 sum to one separately for each configuration. Prices w_gj>0 are public and do not depend on hidden row values. For a prefix b_g define

\[
L_g(b_g)=\sum_{j\le b_g}\alpha_{gj}z_{gj},\qquad
r_g(b_g)=\sum_{j>b_g}\alpha_{gj},\qquad
U_g(b_g)=L_g(b_g)+r_g(b_g)\mathbf1.
\tag{D1}
\]

All objectives are minimized; scalarisation uses every w>=0,w!=0, including axis weights, and ties count as support. Pareto domination needs one strict coordinate.

**Proposition D1.** A prefix is TRUE if and only if

1. no rival L_g dominates U_A; and
2. there is no w in the probability simplex Delta_{d-1} such that w·(U_g-L_A)>=0 for every rival g.

The proof of P55 Theorem 1 works without a dimension restriction: all required corner completions are legal simultaneously, and coordinate monotonicity proves sufficiency. This does not assume that every point of the bounding box is attainable.

**Proposition D2 (sharp witness bound).** Under condition 1, condition 2 holds if and only if some set of at most d rivals already has no supporting weight for L_A. At least two are needed in this nondominated setting.

**Proof.** Each rival defines the convex closed set

\[
H_g=\{w\in\Delta_{d-1}:w\cdot(U_g-L_A)\ge0\}.
\]

All sets lie in the affine space sum_l w_l=1 of dimension d-1. If their intersection is empty, Helly's theorem gives an empty intersection of at most d of them. Conversely an empty subintersection is sufficient. A single H_g cannot be empty under condition 1: emptiness would require every coordinate of U_g-L_A to be negative, which would force domination by L_g at U_A. QED.

**Sharp example.** With N=1, take p_A=(1/2)*1 and, for i=1,...,d,

\[
p_i=(1/2+1/(4d))\mathbf1-\tfrac12 e_i.
\tag{D2}
\]

Each rival has one coordinate below p_A and all others above it, so none dominates. Its supporting constraint is w_i<=1/(2d). All d constraints cannot hold simultaneously because sum_i w_i=1, but after removing constraint i the axis weight e_i supports A against every remaining rival. The equal rival mixture is p_A-(1/(4d))*1. Exactly d rivals are therefore necessary to witness unsupportedness. All points lie in the unit cube; this is already an exact finite archive example. It shows that the two-witness property is a genuine two-dimensional specialization.

### Exact retrospective comparator

For a fixed candidate prefix a define h_g(a) to be the first rival prefix for which L_g(h_g(a)) does not dominate U_A(a). If one is absent, discard a. Such safety is preserved under further observations, since L_g grows coordinatewise. Let P_g(b)=sum_{j<=b}w_gj. Define

\[
E_J(a)=\min_{b_g\ge h_g(a),\ g\in J}
\left\{\sum_{g\in J}\bigl(P_g(b_g)-P_g(h_g(a))\bigr):
L_A(a)\text{ is unsupported against }(U_g(b_g))_{g\in J}\right\},
\]

with an infeasible minimum set to infinity. Then

\[
C^*(I)=F+\min_a\left[
P_A(a)+\sum_{g\ne A}P_g(h_g(a))+
\min_{2\le |J|\le \min(d,K-1)}E_J(a)
\right].
\tag{D3}
\]

Every TRUE prefix must include the safety prefixes, and D2 supplies a witness J of size at most d. Keeping those witnesses and resetting all other rival prefixes to their safety lengths preserves TRUE and cannot increase cost. Conversely every feasible choice in (D3) is TRUE by D1. This proves the exact formula; the acquisition policy is not given these complete-archive arrays.

For fixed d, this formula yields a polynomial retrospective algorithm. For a fixed J, the unsupportedness predicate is upward closed in the |J| prefix counts. Fix |J|-2 counts and sweep the last two as a monotone staircase; the index motion costs O(n_u+n_v) exact predicate tests. With equal N this gives O_d(K^d N^d) tests in a direct implementation, where the hidden constant accounts for a bounded-size d-dimensional feasibility problem. A simpler enumeration is O_d(K^d N^{d+1}). Unequal lengths replace the power by the corresponding sums of products. The finite checker implemented only the simpler enumeration, not the optimized multidimensional staircase. For d=2, P55 already has O(K²N²); the new geometry-track sorted-stream algorithm further improves the K dependence.

Weights alpha are not disclosure prices: they change objective aggregation and the geometric residual uncertainty; prices change the cost of purchasing a certificate. Treating them as interchangeable would be wrong. Neither this theorem nor endpoint transfer preserves the unbounded/band/triangle numerical acquisition constants under arbitrary importance weights or archive lengths.

## 3. Higher-dimensional obstruction to candidate census

Let

\[
\mathcal U_d=[0,\infty)\times[0,1]^{d-1},\qquad d\ge3.
\]

Use d-1 fully observed rivals with complete vectors (0,e_i), where e_i runs through the coordinate axes of the last d-1 coordinates. Take a candidate observed fraction t=a/N satisfying

\[
\frac1{d-1}<t<1.
\]

Choose a scalar c strictly between 1/(d-1) and t, and make every observed candidate row (1,(c/t)*1). These are legal. Its lower vector is (t,c*1). Its bounded upper coordinates are c+1-t<1, while its first upper coordinate is unbounded.

Every rival has a bounded coordinate equal to one, strictly above the candidate's corresponding upper coordinate, so it cannot dominate in any completion. The equal rival mixture is (0,(1/(d-1))*1), strictly below the candidate lower vector in every coordinate. Hence the partial-candidate prefix is robust TRUE, however large the unread first coordinate becomes.

For this fixed rival family the threshold is exact: if t<=1/(d-1), the candidate lower bounded-coordinate sum is at most (d-1)t<=1. Set unread candidate rows to zero. Equal weights on the bounded coordinates, with zero weight on the unbounded first coordinate, support the candidate against every rival. Thus no such prefix can be TRUE.

**Concrete d=3 example.** Let N=10. Read the first six candidate rows, each (1,11/12,11/12). Read all ten copies of (0,1,0) in one rival and all ten copies of (0,0,1) in the other. Then

\[
L_A=(3/5,11/20,11/20),
\qquad (U_{A,2},U_{A,3})=(19/20,19/20).
\]

The rival mean (0,1,0) stays worse in coordinate 2 and (0,0,1) in coordinate 3, while their average (0,1/2,1/2) is strictly below L_A. Therefore prefix (6,10,10) is TRUE with four candidate rows unread. Candidate census is necessary in P55's two-dimensional unbounded theorem, but not here.

As d grows, the candidate fraction can approach 1/(d-1), so the fraction left unread can approach 1-1/(d-1). This is an exact dimensional boundary construction, not a lower or upper minimax acquisition ratio in the new dimension.

## 4. Evidence produced and proof audit

`p56_work/scripts/gen_endpoint_margin_checks.py` uses only Python standard-library Fraction arithmetic, exact Gaussian elimination and vertex enumeration of the normalized supporting-weight polytope. It imports no P55 code. `p56_work/evidence/Generalization_Checks_P56.json` records:

- 30 heterogeneous weighted/priced archives in d=2,3,4: 2,972 complete prefix states; exact comparator decomposition equals exhaustive optimum on all 30 (18 positive);
- sharp witness constructions for d=2,...,6: d rivals necessary, full mixture strict;
- 6,400 additional prefix states checking the weighted margin sufficient condition; it applies in 41 and is sound in all 41;
- exact triangle margin example, sharp boundary failure, guaranteed next round and repeated-row control;
- exact d=3 incomplete-candidate counterexample and dimension-family inequalities for d=3,...,8.

The small number of applicable random margin states reflects the stringent worst-order sufficient condition and short synthetic archives. The theorem's support is the proof; these finite checks are corroboration and are not field evidence.

`p56_work/scripts/gen_crosscheck_geo.py` separately checks the geometry-track sorted-stream comparator against the general rational LP oracle on 100 archives (57 positive), exhausting 15,516 prefixes, including 40 unequal-length/nonuniform-importance-weight cases. This does not reuse the geometry track's interval oracle or brute-force implementation. Result: PASS. The manual proof audit confirms stream monotonicity, distinct witness labels, strict-threshold grouping, safe-prefix reduction, arbitrary positive tariffs and the O(KN² log K) equal-length arithmetic count and its O((n_A+1)L log K) generalization, L=sum_g(n_g+1). No defect was found; this is not proof-assistant verification.

## 5. Literature grounding and novelty limits

The convex-geometric ingredients are established, and must not be presented as new Helly, separation or scalarisation theorems:

- **Stephen Boyd and Lieven Vandenberghe, Convex Optimization (2004), Sections 2.5 and 4.7.** Author-hosted PDF inspected: https://www.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf . Separation/theorems of alternatives justify the strict-mixture characterization. This does not analyze the present paid-prefix cost.
- **Ludwig Danzer, Branko Grünbaum and Victor Klee, Helly's Theorem and Its Relatives (1963), introductory theorem.** Authored mathematical source retrieved at https://academicweb.nd.edu/~andyp/teaching/2013SpringMath366/DanzerGruenbaumKlee.pdf . The dimension-d witness bound is an application of classical Helly in dimension d-1, not a novel convexity theorem.
- **David Könen and Michael Stiglmayr (2025), On Supportedness in Multi-Objective Integer Linear Programming**, DOI 10.1002/mcda.70024. Publisher full text inspected: https://onlinelibrary.wiley.com/doi/10.1002/mcda.70024 . Their distinction between positive and nonnegative scalarisation is directly relevant: this project's axis-inclusive definition must be retained in d dimensions. It is already cited in P55.

Targeted searches did not establish historical priority for the combined weighted-prefix decomposition or the sharp margin-to-disclosure formulation. They also did not locate a directly matching result. **Neither observation is a comprehensive novelty proof.** The cleanest integration is as transparent extensions and consequences of the existing framework, with the sharp examples emphasized and the underlying classical tools credited.

The promising contribution is that certificate geometry, practical stopping opportunities and dimensional scope become explicit. No theorem here closes the unrestricted triangle minimax gap, establishes measured economic benefit, or decides SICOMP editorial importance.
