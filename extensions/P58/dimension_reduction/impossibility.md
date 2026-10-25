# Dimension-reduction obstructions for unsupported Pareto certification

Research note, 25 October 2026. These are self-contained derivations checked in this session. They are not claims of historical novelty, and they have not been inserted into the canonical manuscript.

## Setting and scope

All objectives are minimised. A candidate is GOOD when it is Pareto-nondominated among the individual rivals and unsupported by every nonzero nonnegative linear scalarisation; ties and axis weights count as support. A reduction is *monotone affine* when `F(x)=Tx+b`, with `T` entrywise nonnegative. Nonzero output rows can be rescaled to sum to one without changing Pareto dominance or supportedness. A zero output row creates a constant objective; assigning all scalarisation weight to it supports every point, so no projected point can be GOOD.

The strongest result below concerns a single designated candidate, and allows the map to depend on the entire realised catalogue. It is therefore stronger than a counterexample to a fixed coordinate projection.

## Proposition 1: a robust obstruction even to catalogue-adaptive aggregation

Let `d>=3`, let `1<=m<d`, and consider the `d+1` points in `[0,1]^d`

`A=(3/4,...,3/4)` and `R_i=e_i`, for `i=1,...,d`.

Then A is GOOD in the original objectives, but A is not GOOD after **any** monotone affine reduction to m objectives. The conclusion holds even if the reduction is chosen after inspecting this catalogue.

### Proof

Each rival R_i is worse than A in coordinate i, since `1>3/4`, and better in every other coordinate. Thus no individual rival dominates A. Take any two distinct rivals. Their mean has coordinates at most `1/2`, hence is strictly below A in every coordinate. Consequently every nonzero nonnegative scalarisation has a rival with strictly lower score than A: A is unsupported. Both the coordinate separating each rival from dominance and the displayed mixture certificate have margins at least `1/4`.

Now let `T` have m nonzero nonnegative rows and normalise each row to sum to one. In each row, at most one coefficient is strictly larger than `1/2`. Therefore at most m input-coordinate indices have a coefficient larger than `1/2` somewhere. As `m<d`, choose an index i outside that union. Every coordinate of `T e_i` is at most `1/2`, whereas every coordinate of `T A` equals `3/4`. Thus projected R_i strictly dominates projected A, in every output coordinate by at least `1/4`. Adding b does not change this comparison. Zero rows were handled above. QED.

### Consequences and limits

- The desired universal exact reduction from d objectives to two nonnegative aggregate objectives is false for every d>=3.
- The same example defeats reduction to *any* smaller m<d in this map class.
- This is not a near-tie artefact: the original and false projected certificates have substantial normalised margins.
- Only **two** rivals are needed to witness original unsupportedness, yet no reduction to two nonnegative aggregates preserves the full GOOD property. The obstruction comes from protecting nondomination against the *whole* catalogue.
- A family of multiple two-dimensional views can collectively cover information that no single view preserves. Such a family does not constitute one two-dimensional reduction.
- This proposition does not rule out signed linear maps for one particular finite catalogue, arbitrary nonlinear encodings, restricted domains, or restricted preferences. Such changes require their own statements.

## Proposition 2: fixed rank-deficient monotone maps also fail with only two rivals

Let T be a nonnegative m-by-d matrix with m<d, all output rows nonzero, and let b be arbitrary. There exists a catalogue with one candidate and only two rivals on which `Tx+b` changes GOOD from true to false.

Choose nonzero h in ker(T), orienting it so `max h>0`. Because T is nonnegative and has nonzero rows, h cannot be strictly positive in every coordinate; hence `min h<=0`. Choose `0<epsilon<max h`, and put `delta=epsilon/2`,

`v=h-epsilon*1`, `u=delta*1-h`.

Both v and u have at least one positive and at least one negative coordinate. Relative to candidate 0, neither rival dominates. Their mean is `(delta-epsilon)/2 * 1<0`, so the candidate is unsupported. Yet `Tv=-epsilon*T1<0` coordinatewise, so the projected first rival dominates the projected candidate. Translating the catalogue to the centre of the cube and shrinking by a sufficiently small positive factor makes all original vectors lie in `[0,1]^d` without changing any verdict. QED.

This proposition has different quantifiers from Proposition 1: the map is fixed first and the three-point catalogue can depend on it. It therefore does not rule out all catalogue-adaptive maps for catalogues with only three alternatives.

## Proposition 3: arbitrary nonlinear maps cannot always preserve the complete dominance order

For d>=3 take the 2d points `a_i=e_i` and `b_i=1-e_i` in `[0,1]^d`. Then

`a_i <= b_j` if and only if `i != j`.

No map of this catalogue into `R^m`, m<d, can preserve and reflect its complete coordinatewise partial order.

### Elementary proof

Assume such an order embedding F exists. For each i, the fact that `a_i` is not below `b_i` requires some output coordinate `c_i` with `F(a_i)[c_i]>F(b_i)[c_i]`. Since m<d, two distinct indices i,j use the same coordinate c. Cross-comparability gives

`F(a_i)[c] <= F(b_j)[c] < F(a_j)[c] <= F(b_i)[c] < F(a_i)[c]`,

a contradiction. QED.

This is the classical standard-example obstruction in order-dimension theory, written directly for objective vectors. It applies even to nonlinear, catalogue-adaptive maps when they must preserve the *whole dominance relation*. It does **not** imply impossibility for maps required to preserve only one already-known Boolean label.

## Proposition 4: no margin-free uniform stability of the exact label

For any `epsilon>0`, sufficiently small to remain in the cube, consider

`A=(3/5,3/5,epsilon)`, `L=(0,1,0)`, `R=(1,0,0)`.

A is nondominated and unsupported: the equal rival mixture is `(1/2,1/2,0)`, strictly smaller in every coordinate. Perturb only A's third coordinate to zero. All alternatives then have zero in that coordinate, so the axis weight `(0,0,1)` supports every alternative. The candidate remains nondominated, but GOOD becomes false. The perturbation has sup norm epsilon, arbitrarily small.

Therefore a theorem saying merely that reconstructed criteria are numerically close cannot guarantee preservation of the exact label. It needs explicit separation margins or an abstention/uncertainty region.

## Why mean-compatible reduction naturally leads to the affine class

If a rowwise transformation F is required to commute with all admissible weighted means on a convex domain,

`F(t*x+(1-t)*y) = t*F(x)+(1-t)*F(y)` for every x,y and t in [0,1],

then F is affine by definition. Requiring monotonicity in the original minimisation order makes its linear coefficients nonnegative on a full-dimensional domain. Thus Proposition 1 is directly relevant to universal reductions that seek to preserve both the additive archive semantics and the objective directions. A nonlinear map applied only *after* complete means are known has a different access model and does not automatically preserve paid-prefix certificates.

## Claims that must not be made

1. Do not claim that no imaginable two-number encoding can preserve a finite catalogue's answers. Without regularity, semantics or computation restrictions, data can be encoded in real numbers or answers can first be computed and then represented.
2. Do not claim that an order-embedding obstruction proves impossibility for one Boolean predicate; these are different requirements.
3. Do not claim that a dimension-d witness bound means d criteria can always be replaced by d or fewer rival *counts*. Objectives and alternatives play different roles.
4. Do not claim historical novelty for the elementary constructions without a dedicated prior-art assessment. Proposition 3 is explicitly classical.
5. Do not transfer a verdict-preserving offline map into equality of prefix certificates or hindsight costs without checking all legal completions, observable information and prices.

## Primary-source context

Dushnik, B., & Miller, E. W. (1941). Partially ordered sets. *American Journal of Mathematics, 63*(3), 600–610. https://doi.org/10.2307/2371374

The DOI and bibliographic entry were verified in the American Mathematical Society's reference record at https://doi.org/10.1090/s0002-9939-1986-0840635-8 (web ref `turn115search4`). The original Delft-hosted scan timed out on opening and was not inspected. A primary author-hosted paper explicitly states the standard-example dimension result: https://trotter.math.gatech.edu/papers/127.pdf (web ref `turn116search0`, DOI shown there `10.1007/s11083-011-9222-4`). The parent must open any source it cites directly.

