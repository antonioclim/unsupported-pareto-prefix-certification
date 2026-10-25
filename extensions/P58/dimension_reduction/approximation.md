# Certified approximate objective reduction: research note

Status: mathematical derivations prepared for the current research phase, not integrated into the canonical manuscript. The elementary perturbation arguments below are not claimed as novel. Their possible contribution is a careful application to the conjunction of nondomination and unsupportedness, with explicit paid-prefix accounting.

## 1. Exact question and notation

There are finitely many alternatives, with candidate A and rivals g. Every objective is minimised. The true objective vector is x_g in R^d. Supported means that some nonzero nonnegative weight vector makes A a minimiser, including ties and axis weights. GOOD means nondominated by every individual rival and unsupported by every such weight vector.

A two-coordinate surrogate z_g can be reconstructed as xhat_g = b + B z_g. For the first theorem, neither this affine form nor positivity of B is needed: any approximation accompanied by valid deterministic coordinatewise error bounds is admissible. Assume |x_gi - xhat_gi| <= e_gi for every alternative and coordinate. An empirically small average reconstruction error does not establish these bounds for an unseen alternative or unread archive row.

## 2. General robust transfer theorem

**Proposition A (safe positive transfer).** Suppose:

1. For every rival g there exists a coordinate i such that

   xhat_gi - xhat_Ai > e_gi + e_Ai.

2. There are coefficients lambda_g >= 0 with sum_g lambda_g = 1 such that, for every coordinate i,

   xhat_Ai - sum_g lambda_g xhat_gi > e_Ai + sum_g lambda_g e_gi.

Then the original candidate x_A is nondominated and unsupported.

**Proof.** For the coordinate selected in condition 1,

   x_gi - x_Ai >= xhat_gi - xhat_Ai - e_gi - e_Ai > 0.

Thus each rival is strictly worse in at least one coordinate and cannot dominate A. Condition 2 gives

   x_Ai - sum_g lambda_g x_gi
   >= xhat_Ai - sum_g lambda_g xhat_gi - e_Ai - sum_g lambda_g e_gi > 0

in every coordinate. For every nonzero nonnegative weight vector w, the rival mixture consequently has strictly smaller weighted score than A. At least one rival therefore has strictly smaller score than A. Hence A is unsupported. QED.

This is a sound sufficient condition. Failure to satisfy it does not establish that GOOD is false. It can fail because the margins are too small, because the available error bounds are loose, or because a rival ties the candidate on all coordinates relevant to the strict witness.

**Margins alone do not guarantee that a useful low-dimensional reconstruction exists.** A separate adversarial audit supplies the following obstruction. Let d>=3, A=(3/4)1 and rivals e_1,...,e_d. The candidate has strict individual nondomination margin 1/4, and the equal mixture of any two distinct rivals is strictly below A in every coordinate with margin at least 1/4. Nevertheless, every monotone affine projection to m<d nonconstant aggregate coordinates makes some projected rival strictly dominate the projected candidate. To see this, normalise each nonnegative projection row to sum to one. Each row has at most one coefficient above 1/2, so fewer than d rows leave some index i with every row coefficient at most 1/2. The projected e_i is then at most 1/2 in every coordinate, whereas the projected A is 3/4. Thus good original margins are not a substitute for the certified reconstruction/error assumptions in Propositions A and B. This observation is credited here to the parallel impossibility audit, not to a source search.

### Uniform-error corollary and sharp constant

If e_gi <= epsilon uniformly, it suffices that

   delta_hat_g := max_i (xhat_gi - xhat_Ai) > 2 epsilon  for every rival g,

and that some rival mixture has

   gamma_hat := min_i (xhat_Ai - sum_g lambda_g xhat_gi) > 2 epsilon.

The constant 2 and the strict inequality cannot be improved using only these uniform coordinatewise bounds. For unsupportedness, take xhat_A=(1/2,1/2), xhat_L=(1/10,7/10), xhat_R=(7/10,1/10) and epsilon=1/20. The equal rival mixture is (2/5,2/5), so gamma_hat=1/10=2epsilon, while both nondomination margins are 1/5>2epsilon. Set x_A=(9/20,9/20), x_L=(3/20,3/4), x_R=(3/4,3/20). Each error is epsilon. All three actual alternatives have coordinate sum 9/10, so A is supported by weights (1,1), while remaining nondominated. The strict unsupported verdict is lost exactly at the error threshold, despite sufficient nondomination margins.

For nondomination, use xhat_A=(1/2,1/2), xhat_L=(1/10,3/5) and xhat_R=(3/5,1/10). Then delta_hat_R=1/10=2epsilon while the equal-mixture margin is 3/20>2epsilon. Choose x_A=(11/20,11/20) and x_R=(11/20,1/20). The rival dominates A at the permitted error epsilon=1/20, despite a sufficient unsupportedness margin. These are separate sharpness perturbations; a claim that both obstructions occur under the same perturbation is unnecessary.

## 3. A genuinely two-coordinate positive certificate with bounded residuals

The preceding general test still scans d coordinates. A stronger structural formulation permits a two-coordinate calculation after the error model has been established.

Assume two retained coordinates z_g=(z_g1,z_g2) are exact original objectives. Every original objective has the form

   x_gi = b_i + B_i1 z_g1 + B_i2 z_g2 + r_gi,

where B_i1,B_i2 >= 0, s_i=B_i1+B_i2>0 and |r_gi| <= s_i eta_g. The retained coordinate rows are (1,0) and (0,1), with zero residual and the appropriate zero offsets. Offsets and coefficients are common to all alternatives. These are substantive assumptions, not consequences of a good PCA fit.

**Proposition B (two-anchor residual certificate).** Suppose:

1. Every rival is strictly worse than A in at least one retained coordinate:

   max_{k=1,2}(z_gk-z_Ak)>0.

2. A rival mixture satisfies

   z_A - sum_g lambda_g z_g >= rho (1,1)

for some rho > eta_A + sum_g lambda_g eta_g.

Then A is GOOD in all d original objectives.

**Proof.** The exact retained coordinates provide the strict nondomination witnesses. For any original coordinate i, the reconstructed mixture gap is at least s_i rho. The residual difference is bounded below by -s_i(eta_A+sum_g lambda_g eta_g). The actual gap is therefore strictly positive in every original coordinate. Apply the mixture argument of Proposition A. QED.

Important tie condition: plain projected nondomination is insufficient when two alternatives have identical retained coordinates. Omitted residuals can make one dominate the other. Condition 1 deliberately requires a strict retained-coordinate witness. Under exact reconstruction with zero residuals, identical retained vectors imply identical originals, which removes this particular obstruction.

For a uniform eta, the condition becomes rho>2eta. No property of dimension d appears in this inequality. Consequently, a deterministic two-coordinate certificate can certify the exact d-dimensional verdict for 5, 20 or 50 objectives **when the structural and residual assumptions hold**. This is not a universal two-dimensional representation of the complete Pareto order.

### Sharp boundary for the two-anchor certificate

Let z_A=(3/5,3/5), z_L=(1/5,4/5), z_R=(4/5,1/5). Their equal mixture is (1/2,1/2), so rho=1/10. Add an objective reconstructed by (z_1+z_2)/2. Give A residual -1/20 and both rivals residual +1/20. All three true values of that added objective become 11/20. Thus the added axis weight supports A, even though A is nondominated and unsupported on the two retained coordinates. This saturates rho=2eta and shows why strict residual slack is necessary. An epsilon slightly above 1/20 can make A strictly best on that additional objective.

## 4. Safe negative results and an explicit inconclusive output

The positive test should be part of a three-way procedure: TRUE, FALSE or INCONCLUSIVE.

**Dominance certificate for FALSE.** If a rival g satisfies

   xhat_gi + e_gi <= xhat_Ai - e_Ai  for every i,

with at least one strict inequality, g dominates A for every admissible error realisation.

**Support certificate for FALSE.** If some w>=0, sum_i w_i=1 satisfies

   sum_i w_i (xhat_gi-xhat_Ai-e_gi-e_Ai) >= 0  for every rival g,

then the same weight vector supports A for every admissible error realisation. Equality is correctly accepted because scalarisation ties count as support.

If neither TRUE nor FALSE is certified, retain INCONCLUSIVE and acquire more information or run the original full-dimensional test. Failure of a sufficient TRUE test is not evidence of FALSE. Different legal error realisations can have different verdicts.

This wrapper is logically safe, not automatically faster. It needs accounting for reconstruction, error certification, LP solves and data access.

## 5. Relation to paid prefixes

At a paid prefix, construct any deterministic boxes [L_g,U_g] containing every legal completion of each objective vector. They may combine latent-prefix bounds, reconstruction and residual bounds. The following sufficient positive conditions are independent of endpoint attainability:

* for every rival g, some coordinate satisfies L_gi>U_Ai;
* some rival mixture satisfies L_Ai>sum_g lambda_g U_gi for every coordinate i.

These directly certify every compatible completion. They are conservative: they may miss certificates exploiting correlations or equalities.

The two-anchor variant uses strict retained-coordinate bounds max_k(L^z_gk-U^z_Ak)>0 and a latent mixture gap L^z_A-sum_g lambda_g U^z_g >=rho(1,1), together with valid residual budgets eta_g for every compatible completion. Proposition B then applies uniformly.

If errors are rowwise and aggregate weights are public positive numbers omega_gj summing to one, an aggregate residual bound follows by weighted summation: e_gi <= sum_j omega_gj e_gji. Observed residuals can be incorporated exactly and only the unread residual budget need remain uncertain. Row weights are not objective preference weights and are not disclosure prices.

**Accounting limitations.**

* Learning B or validating residuals using hidden records must be charged. An empirical fit to previously seen rows does not validate all unread rows.
* In the existing whole-row query contract, a query reveals all d components; using a two-dimensional internal calculation does not by itself reduce the number of purchased rows or the bytes transported.
* Revealing only selected components is a new observation model, requiring new prices and comparator analysis.
* An approximate quotient need not preserve all TRUE prefixes or C*. Thus no automatic transfer of 87/80 or another competitive ratio follows.
* Public residual bounds may permit a sound accelerated test, but its overhead and actual savings require measurement.

## 6. Established literature and novelty limits

Objective reduction, dominance-preserving objective selection and approximation with controlled Pareto-set error are existing research topics. The claims above must not be advertised as inventing objective reduction or proving a universal 50-to-2 compression theorem.

Verified primary sources:

1. Brockhoff, D., & Zitzler, E. (2009). Objective reduction in evolutionary multiobjective optimization: Theory and applications. *Evolutionary Computation, 17*(2), 135–166. https://doi.org/10.1162/evco.2009.17.2.135

   Publisher indexed result: https://direct.mit.edu/evco/article/17/2/135/1309/Objective-Reduction-in-Evolutionary-Multiobjective (retrieval turn110search0; direct opening returned 403). The authors' ETH software page documents exact and greedy objective-reduction procedures, delta-MOSS and k-EMOSS: https://sop.tik.ee.ethz.ch/download/supplementary/objectiveReduction/ (turn112view1). This establishes direct prior art for dominance-focused objective reduction, not for the specific paid-prefix unsupportedness theorem proposed here.

2. Lindroth, P., Patriksson, M., & Strömberg, A.-B. (2010). Approximating the Pareto optimal set using a reduced set of objective functions. *European Journal of Operational Research, 207*(3), 1519–1534. https://doi.org/10.1016/j.ejor.2010.07.004

   Primary publisher indexed text: https://www.sciencedirect.com/science/article/abs/pii/S0377221710004868 (turn113search0). The available abstract and introduction describe aggregation with measured approximation loss on a finite decision subset, optimisation formulations and an industrial truck-configuration application. The source explicitly distinguishes preserving dominance from approximating the Pareto set. It does not establish unrestricted 2D reduction for the current predicate.

3. Deb, K., & Saxena, D. K. (2005). *On finding Pareto-optimal solutions through dimensionality reduction for certain large-dimensional multi-objective optimization problems* (KanGAL Report No. 2005011). Indian Institute of Technology Kanpur. https://www.egr.msu.edu/~kdeb/papers/k2005011.pdf

   Primary author-hosted indexed PDF: turn98search24. The report describes a PCA-based approach for problems with lower-dimensional structure, with examples up to 30 objectives. Later direct opening timed out. The 2006 conference version is confirmed on Saxena's institutional publication page https://iitr.ac.in/Departments/Mechanical%20and%20Industrial%20Engineering%20Department/People/Faculty/100603.html (turn113search6), but a DOI for that version was not verified; none is invented here.

The strongest honest research direction is a **certified conditional reduction**: two-dimensional computation plus a verifiable residual envelope produces an exact full-dimensional verdict when the margins exceed the envelope, with a sound inconclusive fallback. Establishing useful envelopes without buying the full archive and proving acquisition guarantees are the difficult additional problems.
