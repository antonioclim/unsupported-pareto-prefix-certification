# Exact structural reduction to two objectives: proof note

Status: a self-contained derivation for the present research task, not a novelty claim. The geometric core belongs to classical cone/objective-redundancy theory. No canonical manuscript has been edited. All objectives are minimised. A point is supported if it minimises a nonzero nonnegative weighted sum; ties and axis weights count as support. GOOD means nondominated and unsupported.

## 1. Exact affine anchor theorem

Let Y be any subset of R^2. Suppose the n-dimensional objective vector associated with y in Y is

    x(y) = b + M y,

where b is common to every alternative and M is an n-by-2 matrix such that:

1. every entry of M is nonnegative;
2. every row of M is nonzero;
3. among its rows are a e_1^T and c e_2^T for some a,c>0.

Then, for every finite labelled catalogue contained in Y:

- x(y) Pareto-dominates x(z) if and only if y Pareto-dominates z;
- y is supported in the two-objective catalogue if and only if x(y) is supported in the n-objective catalogue;
- consequently every candidate has exactly the same GOOD label in both catalogues.

### Proof of order equivalence

If y<=z coordinatewise, nonnegativity gives My<=Mz. If y!=z, one anchor row detects a strict inequality, so strict Pareto domination is preserved. Conversely, My<=Mz implies y_1<=z_1 and y_2<=z_2 by the two anchor rows. The map has rank two, so a strict inequality in objective space cannot correspond to y=z. This proves both directions, including ties between labelled alternatives.

### Proof of support equivalence

For every w>=0, w!=0,

    w^T x(y) = w^T b + (M^T w)^T y.

The vector M^T w is nonnegative and nonzero: some positive w_i multiplies a nonzero nonnegative row, and cancellation is impossible. Thus every admissible n-dimensional score has the same ranking as an admissible two-dimensional score. Conversely, every q=(q_1,q_2)>=0, q!=0 is M^T w for a vector supported on the two anchors, with anchor weights q_1/a and q_2/c. Hence the two families of weighted rankings agree exactly, and minimisers including ties coincide. Normalising weights to sum one does not alter rankings.

The condition can equivalently be written as cone(rows M)=R^2_+, with no zero rows. The no-zero condition matters for the supportedness definition: a zero row is a constant objective and admits a nonzero weight which produces a constant scalarisation.

This is much stronger than preservation of one selected candidate: the same fixed map preserves all pairwise dominance relations and all support labels in every finite catalogue in the specified structural family.

The anchor/cone condition is also necessary for a universal affine coordinatewise order isomorphism on a latent domain containing an open ball. Indeed, translating and scaling differences gives Mu>=0 if and only if u>=0 for every u in R^2. Thus {u:Mu>=0}=R^2_+, and taking dual cones yields cone(rows M)=R^2_+. For a finite row set this entails nonnegative rows and generators on both axes. Preservation of support labels additionally excludes zero rows, because an open latent ball contains a translated and scaled planar unsupported Pareto example, whereas a zero output row supports every image point. This necessity statement is about an order isomorphism on a full-dimensional latent domain, not merely preservation of a few labels in one fixed catalogue.

## 2. Rank-two affine dichotomy and automatic anchor selection

Suppose x(z)=b+Bz, where B is an arbitrary real n-by-2 matrix of rank two. Its entries need not be nonnegative. Exactly one of the following cases occurs.

**Degenerate scalarisation case.** There exists w>=0, w!=0 with B^T w=0. Then w^T x(z)=w^T b for all z. Every alternative in every catalogue is supported, so no candidate is GOOD. This includes an objective which is constant on the entire affine family, but also positive combinations of nonconstant objectives which cancel.

**Pointed-cone case.** There is no such w. Then two original objective coordinates can be selected, with their common offsets removed, so that the affine anchor theorem applies exactly.

### Proof

Let H=cone{b_1,...,b_n} in R^2, where b_i is the ith row of B. Rank two implies that H spans R^2. Absence of a nonnegative nonzero kernel vector implies that no b_i is zero. It also implies pointedness: if v and -v belong to H for some v!=0, express each as a nonnegative combination of rows and add the representations to obtain a forbidden nonnegative nonzero kernel vector.

Conversely, a positive dependence among nonzero rows makes H nonpointed. Indeed, isolate any positively weighted row; its negative is a nonnegative combination of the remaining rows. Thus, apart from the separately excluded zero-row case, the kernel condition and pointedness are equivalent.

A finitely generated pointed full-dimensional cone in R^2 has exactly two extreme rays. Each extreme ray contains at least one generating row. Choose such rows b_i,b_j and let T be the invertible 2-by-2 matrix with these rows. Every b_k has a nonnegative representation b_k=m_{k1} b_i+m_{k2} b_j. Therefore B=MT for a nonnegative matrix M, with ith row e_1^T and jth row e_2^T. No row of M is zero because no row of B is zero. Set y=Tz=(x_i-b_i^{offset},x_j-b_j^{offset}); apply Section 1.

The proof concerns the two-dimensional affine family. It does not require a particular catalogue distribution, a Euclidean approximation or a small numerical error. The error is exactly zero. However, affine rank two is a substantive structural restriction: this is not a reduction of n independent criteria to two.

### How to check the assumptions

- Obtain the affine representation from public model equations or a verified complete finite data set.
- Check rank exactly when an exact claim is intended.
- Test whether B^T w=0, w>=0, sum w_i=1 is feasible.
- If infeasible, find the two extreme generating rays and solve the 2-by-2 systems for all nonnegative coefficients.
- Verify the identities and signs exactly, or with validated arithmetic and a separately stated error guarantee.

An approximately rank-two numerical matrix is not covered by this exact theorem. It needs a perturbation/margin theorem.

## 3. A useful three-alternative corollary

Every completely known catalogue with three alternatives has affine dimension at most two. If it contains a nondominated unsupported candidate, its affine dimension is exactly two and it lies in the pointed-cone case above. Consequently, there are two original objective coordinates whose projection preserves all pairwise dominance relations and supportedness labels on that particular three-alternative catalogue.

To justify the rank-one exclusion, write x(t)=b+v t. If a coordinate of v is zero, a constant objective supports every point. If v has both positive and negative components, choose nonnegative weights to cancel them, again supporting every point. If all components have the same strict sign, the extremal t-value dominates every distinct nonextremal point and is supported; therefore no point is both nondominated and unsupported. Rank zero is immediate.

For affine rank two, an unsupported point rules out the degenerate scalarisation branch, so the anchor theorem applies.

**This corollary is a full-information, data-dependent representation, not an online acquisition theorem.** The two retained criteria may depend on objective means that the online algorithm has not yet purchased. Compatible unread completions can occupy other affine planes or have different anchor criteria. Knowing that every realised positive three-alternative catalogue has some two-dimensional representation does not supply a common free representation across all compatible archives.

The earlier counterexample A=(.6,.6,0), L=(0,1,1), R=(1,0,1) is consistent with this corollary: A is supported in three dimensions, and the catalogue has a nonnegative constant scalarisation. It is not a positive catalogue of the corollary.

An exact-arithmetic finite control was executed with `check_three_alternative_projection.py`. It exhausts all 41,664 unordered three-alternative catalogues on the grid {0,1,2,3}^3. Of these, 423 contain a GOOD candidate; all 423 have a pair of original objective coordinates preserving every pairwise dominance relation and all three support labels. Results are in `three_alternative_projection_control.json`. This finite control corroborates the implementation of the criterion; the argument above proves the universal corollary. It does not establish online acquisition savings.

## 4. Exact paid-prefix isomorphism

Suppose the affine anchor structure holds publicly at the raw-row level, with a common b,M. Every legal n-dimensional row is x=b+My for one and only one legal latent row y in a specified two-dimensional domain D_gj. Conversely, every legal latent row produces a legal n-dimensional row. The same row indices, archive lengths and order are used. Queries reveal the entire corresponding row, and have the same public price, independent of hidden values. Initial information and any common setup are the same under this translation.

For positive public aggregation weights omega_gj shared across the coordinates of a row and summing to one within each group,

    p_g = sum_j omega_gj x_gj = b + M sum_j omega_gj y_gj.

The following conclusions are exact.

1. A full raw row determines its latent row from the two anchors; a latent row reconstructs the full row. Thus each query response is informationally equivalent.
2. Full legal archives and every prefix's compatible completions are in bijection.
3. Every completed catalogue has the same GOOD label by Section 1.
4. A prefix forces TRUE, forces FALSE, or leaves the answer open in one model if and only if its translated prefix does so in the other.
5. Every realised positive certificate cost is the same; hence the hindsight comparator C* is identical.
6. Every causal acquisition policy in one model can be simulated in the other. Coupling random coins gives exactly the same paid query sequence and charge on each translated archive.
7. Therefore optimal paid-acquisition ratios, and any proved ratio of a transferred policy, are identical.

This argument does not rely on independent completion if a more general public completion family is itself mapped bijectively. To inherit a theorem which assumes independence, the induced two-dimensional model must satisfy that theorem's independence and other assumptions.

### Conditional inheritance of 87/80

If the induced two-dimensional row domains are the exact triangle T={(c,f):0<=f<=c<=1}, or the eligible independent endpoint-containing subdomains covered by the existing transfer theorem, and the remaining K=3, equal-length, unit-price and observation assumptions hold, the existing 87/80 paid-acquisition bound transfers to the n-coordinate representation without loss.

This is an inheritance theorem for a structurally two-dimensional family presented with n coordinates. It is not a new competitive bound for n independent objectives. No CPU-speedup or constant-time reconstruction of n values follows: the isomorphism preserves paid-information costs, not every computational resource.

For a direct example with n=50, retain c and f and define the remaining 48 criteria as public mixtures alpha_i c+(1-alpha_i)f with 0<=alpha_i<=1. All 50 values lie in [0,1], the full zero and full one rows are attainable, and the raw-row structure exactly reconstructs the entire vector from c,f. With the appropriate latent triangle archive and the unchanged tariff, the original three-alternative bound transfers. The 48 criteria are redundant by construction; empirical merely strong correlations do not establish this relation.

### Mean-only structure is insufficient for this cost result

A relation observed after all objective means have been computed can establish a full-catalogue reduction. It cannot justify giving an online algorithm that relation for free, constraining unseen completions to it, or revealing extra components without charge. Likewise, coordinate-by-coordinate prices, value-dependent prices, different row order, or a latent representation found using hidden rows can break transcript equivalence.

## 5. Boundary examples

### Omitted constant objective

Add a third objective equal to zero to the planar catalogue A=(.6,.6), L=(0,1), R=(1,0). The planar A is nondominated and unsupported. In three dimensions the third axis supports every point at equality. Dropping the constant objective changes support labels. This explains why nonzero rows are necessary for the universal support-equivalence statement.

### Nonnegative map without both anchor directions

Let every row of M have two strictly positive entries; for instance M has rows (1,1) and (1,2). Compare y=(0,1) with z=(3,0). These latent points are incomparable, but My=(1,2)<Mz=(3,3). The incomparable latent pair becomes comparable. Nonnegative forward aggregation alone preserves existing domination but need not reflect it. Anchor generation of the whole orthant supplies the missing reverse direction.

### Monotone nonlinear redundancy preserves order but can alter support

Take A=(.6,.6), L=(0,1), R=(1,0), and append h(y)=max(y_1,y_2). The added criterion is monotone in both retained criteria, so it does not alter pairwise dominance when the originals remain present. But h(A)=.6<h(L)=h(R)=1, so the new axis supports A. In two dimensions A was unsupported. Thus a Pareto-preserving reduction need not preserve the specific unsupported-Pareto predicate.

### Positive affine changes of units

Common positive scaling and common translation of an objective preserve all weighted rankings after the reciprocal change in weight. Alternative-specific shifts do not generally preserve comparisons. The offset b in Section 1 must be common to all alternatives; raw-row offsets can vary only if their known aggregate offset is the same across alternatives or is explicitly incorporated without breaking the equivalence.

## 6. Prior-art audit and novelty limits

The following primary sources were actually retrieved. Their relevance is reported narrowly; this note does not claim to have proved novelty relative to their full literature.

- Löhne, A., & Zillmann, P. (2026). Low-rank multi-objective linear programming (arXiv:2508.20880v3, 25 September 2026). https://doi.org/10.48550/arXiv.2508.20880 . Full author preprint: https://arxiv.org/pdf/2508.20880 . It factorises the objective matrix, reduces objective-space dimension to rank and retains a transformed ordering cone. It explicitly connects to classical conic redundancy. This is very close prior art for the geometric rank/cone reduction and must be cited; the present geometric argument should not be sold as a new universal dimension-reduction discovery.
- Brockhoff, D., & Zitzler, E. (2009). Objective reduction in evolutionary multiobjective optimization: Theory and applications. Evolutionary Computation, 17(2), 135–166. https://doi.org/10.1162/evco.2009.17.2.135 . Author publication page: https://www.sop.tik.ee.ethz.ch/people/brockho/publications.html . It studies exact/approximate preservation of dominance structure, which is not automatically preservation of unsupportedness plus paid-prefix information.
- Eichfelder, G., Gerlach, T., & Kugelmann, C. (2026). Redundant objectives in multiobjective optimization. Author preprint dated 22 September, posted 23 September 2026. No DOI was verified. https://optimization-online.org/2026/09/redundant-objectives-in-multiobjective-optimization/ . Full PDF https://optimization-online.org/wp-content/uploads/2026/09/Redundant_objectives_in_multiobjective_optimization_Eichfelder_Gerlach_Kugelmann.pdf . It distinguishes efficiency-related redundancy and stronger order redundancy; the notions should not be conflated.

Tool reference IDs for the parent to reopen before using citations: turn114view0 (Löhne–Zillmann full PDF), turn114view1 (Brockhoff author page), turn114view2 (Eichfelder et al. full PDF). The 2009 DOI was independently displayed in PubMed, turn104search0; its author page confirms title, authors, journal, volume and pages.

Potential contribution to the current manuscript, if separately audited: a precise paid-prefix transcript-isomorphism corollary, explaining exactly when structural dimension reduction preserves the certificate comparator and transfers the existing theorem. Even this should be presented cautiously as a consequence/application unless its specific novelty is established.

## 7. Independent audit of the adaptive agent's complementary reduction

This section was added after independently checking the proposed dual sparsity result. It requires no rank-two structural assumption on the objective vectors. It is different from the single-map reduction above.

Let a be a candidate in R^d and let r_1,...,r_m be its m=K-1 rivals, with K>=2. All coordinates are minimised and nonnegative nonzero weights, including ties, define support. If the candidate is supported, there is a supporting weight using at most min(d,m) nonzero objective coordinates.

### Proof through finite Helly theory

By finite-dimensional separation/minimax, the candidate is unsupported precisely when a convex combination of the rivals is strictly smaller in every coordinate. For each objective i define

    C_i = {lambda in Delta_(m-1) : sum_j lambda_j r_(j,i) < a_i}.

These are convex subsets of the affine (m-1)-dimensional simplex. They need not be closed. The candidate is unsupported if and only if their full intersection is nonempty. If it is supported, the intersection is empty, so finite Helly's theorem supplies an empty subintersection of at most m sets. Those objective coordinates alone therefore already give a supported projected candidate. Extend its supporting weight by zeros to get the required full supporting weight. Finite Helly applies to convex open or closed sets, so strict mixture inequalities and scalarisation ties are handled correctly.

Consequently, for d>=2 and exactly three alternatives, the candidate is unsupported in d dimensions if and only if it is unsupported in EVERY projection onto a pair of original objective coordinates. Single-coordinate supporting weights are covered by pair projections which allow a zero weight on the other coordinate.

Nondomination is separate and must be tested on the original full vectors. Requiring that every pair projection is also nondominated would be an unjustified and generally false extra condition.

### Direct algorithm for three alternatives

There is no need to execute binomial(d,2) separate planar tests. With rivals b,c, unsupportedness is equivalent to feasibility of a single scalar lambda:

    0 <= lambda <= 1,
    lambda (b_i-c_i) < a_i-c_i,  i=1,...,d.

Intersect these intervals in O(d) rational operations, remembering open versus closed endpoints. A zero coefficient requires 0<a_i-c_i. Positive coefficients provide strict upper bounds; negative coefficients provide strict lower bounds. The bounds 0 and 1 are closed, so a singleton at 0 or 1 is feasible only when every original coordinate inequality is strict there. Nondomination against both rivals also takes O(d) comparisons.

Thus the full-vector predicate with three alternatives can be checked in linear arithmetic work in the number of objectives, without constructing a single equivalent two-dimensional point cloud. All d input criteria are still processed. Arithmetic bit complexity depends on input precision.

### Prefix application and caution

Under the exact endpoint hypotheses of S12, substitute a=L_A, b=U_B, c=U_C in the interval test, and separately verify that neither rival lower corner dominates U_A. This gives an O(d)-arithmetic exact TRUE-prefix test for K=3. A policy checking after every whole-row observation therefore has O(dN) arithmetic processing across O(N) observations, apart from its own additional computations.

If the interval intersection is empty, this means that the robust-TRUE unsupportedness condition fails. It does NOT automatically mean the prefix forces FALSE: one compatible completion may be supported while another is GOOD. A policy may use separately proved negative stopping or continue to census.

This computational decomposition neither gives the online policy free access to any criterion nor transfers the 87/80 acquisition ratio. Every pair projection can have a different useful certificate, and forcing full-dimensional nondomination still uses all relevant rivals/criteria.

### Sharpness of objective-weight sparsity

For d=m, choose objective columns v_i=m e_i-1 in R^m, meaning rival j has difference from the candidate (r_j-a)_i=m delta_(ij)-1. Supporting weights normalised to sum one must satisfy m w_j-1>=0 for every rival j, so w_j=1/m for every j. All m objective weights are necessary. Translate the candidate to (1/2)1 and scale the differences by 1/(2m) to obtain a bounded [0,1]^m example. This confirms the general m bound cannot be improved to two when the number of rivals grows.

The proof ingredients are classical. The complementary objective-sparsity statement and its paid-prefix implementation should be positioned carefully against existing Helly, Caratheodory, minimax and objective-reduction literature before a novelty claim.
