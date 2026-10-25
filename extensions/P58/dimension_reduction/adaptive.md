# Candidate-adaptive aggregation: impossibility and an exact diagnostic

Research note, 25 October 2026. Derived for the present task; not a claim of literature novelty. All objectives are minimised. Supported means optimal, including ties, for some nonzero nonnegative scalarisation. The claims below concern affine aggregations with nonnegative coefficients. They do not exclude arbitrary nonlinear, catalogue-dependent encodings of already-computed labels.

## 1. Unsupportedness survives a nonnegative aggregation

Let a be a candidate, r_j its rivals, and F(x)=Tx+b, where T has m nonzero nonnegative rows. If a is unsupported in the original objective space, F(a) is unsupported against F(r_j).

Proof. If a reduced weight u>=0, u!=0 supported F(a), then w=T^T u>=0 and w!=0, because every row of T is nonzero. The inequalities u·(F(r_j)-F(a))>=0 would be w·(r_j-a)>=0 for all j, contradicting original unsupportedness. Affine offsets cancel. This is a classical scalarisation observation, not a new universal reduction result. Nondomination can fail after the aggregation.

Each nonzero row may be normalised to sum one: independently rescaling reduced objectives by positive constants preserves dominance and the existence of supporting weights. Write these rows as w^s in the probability simplex Δ_{d-1}.

## 2. Even a single nominated candidate can require all d aggregation coordinates

For any integer d>=2 and q in (1/2,1), consider the bounded catalogue

    a=q·1 in [0,1]^d,
    r_i=e_i, i=1,...,d.

The candidate is nondominated: rival i is better in d−1 coordinates but worse in coordinate i. The nondomination margin max_l(r_il-a_l) is 1−q for each rival.

The candidate is unsupported: the average of any two distinct rivals is at most 1/2 in every coordinate, strictly below q. Thus two rivals already witness unsupportedness, with a uniform mixture margin at least q−1/2.

For every nonnegative affine aggregation with m<d nonzero rows, the projected candidate is strictly dominated by a projected rival. This holds even if the aggregation is selected after inspecting the entire catalogue.

Proof. Normalise each row to sum one. Because q>1/2, each row has at most one coefficient >=q. At most m coordinate indices have a coefficient >=q in some row. Choose an uncovered index i. Every row then gives w^s_i<q, so F(r_i)_s<F(a)_s for every s. Hence the rival strictly dominates the candidate in all reduced coordinates. The identity map shows d coordinates suffice; thus d is the exact minimum for this family.

This separates two notions sharply: only TWO alternatives are needed to witness unsupportedness, but ALL d aggregation coordinates are needed to preserve nondomination.

## 3. Exact quantitative obstruction for the same family

Define

    τ_m = max_{w^1,...,w^m in Δ} min_i max_s (w^s_i−q).

Then, for 1<=m<=d,

    τ_m = 1/ceil(d/m) − q.

Upper bound. Assign each i to a row attaining max_s w^s_i. One row receives at least ceil(d/m) indices. If t=min_i max_s w^s_i, those coefficients sum to at least ceil(d/m)t, hence t<=1/ceil(d/m).

Attainment. Partition the d indices into m nonempty groups as evenly as possible. On row s place uniform weights on its group and zero elsewhere. Each index has maximum coefficient the inverse of its group size, whose minimum is 1/ceil(d/m).

Therefore every two-coordinate aggregation has some rival whose projected coordinates are both smaller than the candidate's by at least

    q − 1/ceil(d/2).

For q=3/5 this is 4/15 for d=5, 1/2 for d=20 and 14/25 for d=50. These are margins in row-normalised projected objectives, not reconstruction-error bounds in the original space. The result rules out a universal “small qualitative loss” reading for this class of reductions; it does not impose a lower bound on all imaginable nonlinear encodings.

## 4. A candidate-specific constructive diagnostic

For a general catalogue define v_j=r_j−a, and

    τ_m(a) = max_{w^1,...,w^m in Δ} min_j max_s w^s·v_j.

Then τ_m(a)>0 if and only if there is an m-coordinate nonnegative row-normalised aggregation for which every projected rival has at least one coordinate strictly worse than the projected candidate. Equivalently, it preserves strict nondomination with a positive margin. If a was originally unsupported, section 1 simultaneously preserves unsupportedness.

This is an exact characterisation of robust candidate-specific compression. It is deliberately stronger than ordinary nondomination, which also permits projected rival vectors identical to the candidate. Exact duplicates in the original catalogue can be removed for this diagnostic without changing original nondomination or unsupportedness; newly coalescing projected points should not be silently treated as robust preservation.

For a fixed assignment σ of each rival to a row, solve the linear programme

    maximise δ
    w^s>=0, sum_i w^s_i=1,
    w^{σ(j)}·v_j >= δ for every j.

The maximum over all assignments σ is τ_m(a). For m=2 this gives a finite collection of LPs or a mixed-integer formulation. It is a verifiable algorithmic route for a given catalogue, not a claim of polynomial scaling in catalogue size. It can return failure, which the axis family forces whenever m<d.

For vectors in [0,1]^d, one exact MILP representation for m=2 uses δ in [−1,1], binary z_j and big-M=2:

    w^1·v_j >= δ−2z_j,
    w^2·v_j >= δ−2(1−z_j).

Together with simplex constraints, maximising δ gives τ_2. At least one inequality is active for each rival; the other is redundant because w·v lies in [−1,1]. No solver execution or runtime claim is made in this note.

## 5. Two numerical summaries are not a two-objective reduction

Let J' be rivals whose full vector differs from a. Put

    δ(a)=min_{j in J'} max_i(r_ji−a_i),

with min(empty)=+infinity. Then a is nondominated exactly when δ(a)>0. The exclusion of exact duplicates is essential: otherwise δ=0 could incorrectly reject a legitimate nondominated candidate.

Put

    γ(a)=max_{λ>=0, sum_j λ_j=1} min_i(a_i−sum_j λ_j r_ji).

For a finite nonempty rival catalogue, convex separation/minimax gives unsupportedness exactly when γ(a)>0. Thus GOOD is equivalent to δ(a)>0 and γ(a)>0.

This compresses a completed analysis into two diagnostic values. Calculating them still uses the original d-dimensional data; γ is an optimisation over all coordinates. Two scalars alone do not furnish an independently checkable certificate without the underlying comparisons and mixture witness. Consequently this is neither a pre-acquisition data reduction nor a proof of lower paid-query cost. It also duplicates the margin perspective already present in supplementary S5.7 rather than establishing new novelty.

## 6. Implications for prefix certificates

At a fixed prefix, robust strict nondomination is obtained from v_j=L_j−U_A. Applying the τ_m diagnostic to these differences verifies that the same aggregation preserves that margin for every compatible completion. A full-space strict mixture between L_A and rival U_j also survives row-normalised nonnegative aggregation.

However, if those full-space prefix tests have already been performed, a subsequent two-dimensional display cannot be counted as having reduced their acquisition cost. A map chosen using hidden final data cannot be given to an online acquisition policy for free. A legitimate pre-acquisition reduction needs a public map, compatible completion domains and a faithful accounting of the original observations and prices.

## 7. Scope and novelty

All algebraic statements above have self-contained proofs. Literature priority has not been established. The central scalarisation and margin equivalences are classical; the axis-family obstruction and τ_m formulation should be described as derived observations pending prior-art verification. No canonical manuscript has been edited.

## 8. Positive single-candidate projection when there are only two rivals

Suppose a is nondominated and unsupported against exactly two rivals in any dimension. Neither rival can equal a: with only one other distinct rival, nondomination supplies an axis supporting a, contradicting unsupportedness. Choose i with r_1i>a_i and k with r_2k>a_k. They cannot coincide, since that common axis would support a against both rivals. Coordinate projection onto (i,k) preserves nondomination, and section 1 preserves unsupportedness.

More generally, choosing one strict-advantage coordinate for every distinct rival gives at most min(d,K−1) retained coordinates preserving a known positive verdict. This is a one-way existence statement about a positive candidate. A supported original candidate may also have an unsupported projection, so existence of a positive planar projection is NOT equivalent to full-dimensional GOOD. It cannot independently certify a positive original verdict or be given as a free online map chosen with hindsight.

## 9. Exact decomposition into low-dimensional support tests

Let m=K−1>=1. If a supporting weight exists in d objective dimensions, one exists with at most min(d,m) nonzero entries.

Proof. For each objective coordinate i form the column v_i=((r_j−a)_i)_{j=1}^m in R^m. A supporting normalised weight exists exactly when P=conv{v_i} intersects the nonnegative orthant. If dim(P)<m, Caratheodory's theorem gives a representation using at most m columns. If dim(P)=m, start at p in P intersect R_+^m and move along the ray p+t·1 until its last point in the compact polytope P. That boundary point is still nonnegative and lies in a face of dimension at most m−1, so it is a convex combination of at most m columns. The corresponding weights support a. The converse is immediate by padding zero weights.

Hence full-dimensional unsupportedness is equivalent to unsupportedness on EVERY coordinate subset of size at most m. If d>=m, subsets of size exactly m suffice because every smaller support can be included in one.

For EXACTLY THREE alternatives (two rivals), this is an exact reduction of the support decision to the family of binom(d,2) planar tests: 10 tests at d=5, 190 at d=20 and 1,225 at d=50. Each planar test is simply the feasibility of two linear inequalities over the interval of weights [0,1]. Original nondomination must still be checked separately in all d coordinates; do not require each planar projection to be nondominated.

The same decomposition applies to S12's prefix unsupportedness test after replacing the candidate by L_A and rivals by U_j. Together with the full-dimensional lower/upper-corner nondomination test, it reproduces the exact robust prefix criterion under S12's hypotheses.

This is an exact computational decomposition into a FAMILY of two-dimensional problems when K=3, not one faithful two-dimensional representation of the full catalogue. It does not reduce the price of obtaining an original whole-vector record or transfer the two-objective 87/80 acquisition policy. The dimension bound depends on number of alternatives; for large K the planar decomposition is no longer generally valid. The argument is a consequence of classical convex geometry, so literature novelty is unestablished.

## 10. A simpler O(d) pointwise test when K=3

The pair decomposition is a structural equivalence, not a requirement to run all binom(d,2) tests in an implementation. Convex separation gives an even simpler predicate: a is unsupported against r_1,r_2 exactly when there is a mixture parameter lambda in [0,1] such that

    lambda*r_1i + (1−lambda)*r_2i < a_i   for every i.

For each objective this is a strict linear inequality

    lambda*(r_1i−r_2i) < a_i−r_2i.

Its feasible set is a half-line, all reals or the empty set. Intersect these sets with [0,1], preserving the strict or closed status of endpoints. A nonempty intersection certifies unsupportedness. Nondomination is a separate scan of the original coordinates. The combined pointwise predicate uses O(d) rational operations. Bit complexity still depends on the numerical representation, and this statement is not a measured runtime guarantee.

For S12's prefix predicate, substitute candidate L_A and rivals U_1,U_2 in the interval test, and perform the separate corner-nondomination checks L_j versus U_A. This is an exact reformulation under S12's domain hypotheses. It does not reduce the dimension of the acquired observation, the set of possible prefix choices or the cost of the retrospective optimum.

Executed corroboration in verify_support_decomposition.py compares this independently coded exact rational interval algorithm with exact coordinate-pair support tests and a full-dimensional numerical SciPy/HiGHS LP on 2,000 synthetic cases in dimensions 2,3,5,20,50. All agree: 1,340 supported, 660 unsupported. Each dimension includes 200 random cases, 100 constructed unsupported cases and 100 supported cases without any supporting axis weight. Nine separately specified boundary controls check strict endpoint handling and constant-coordinate ties; all pass. The retained support_decomposition_checks.json contains full counts and scope. The exact algebraic arguments, not these finite tests, establish the universal claim.
