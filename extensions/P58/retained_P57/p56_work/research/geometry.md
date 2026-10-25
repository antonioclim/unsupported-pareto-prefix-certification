# P56 research note: a faster exact retrospective certificate optimizer

Status: new proved algorithmic refinement of P55 Supplement S1.1, with a
private exact-arithmetic prototype and independent finite checks. This does
**not** improve the online triangle ratio, solve its open optimum, or measure
economic benefit. It makes a concrete part of the computational contribution
stronger, particularly when the catalogue has many configurations.

## Baseline and actual change

P55 Supplement S1.1 already proves an exact comparator decomposition and an
`O(K²N²)` arithmetic-operation algorithm: for each candidate prefix, inspect
every rival pair using a monotone two-dimensional staircase. The `K=3`,
`O(N²)` observation is consequently **not new**.

The refinement here removes the quadratic enumeration of rival pairs. Merge
the already monotone supporting-weight threshold streams of all rivals. The
new exact bound is

\[
O\bigl(KN^2\log K\bigr)
\]

rational arithmetic/comparison operations and `O(KN)` working storage. The
comparator can return an optimal prefix, not just its cost. Public arbitrary
strictly positive row tariffs and a common nonnegative setup cost are allowed.
For fixed `K`, both old and new bounds remain `O(N²)`; the asymptotic improvement
is in catalogue size. There is no claim that this is a lower-bound-optimal
running time or a new general-purpose merge method.

## Theorem (merged-threshold comparator)

Let `K≥3`, `N≥1`, and let every observed whole-vector row lie in an independent
public completion domain `D⊆[0,1]²` containing `(0,0)` and `(1,1)`. Let the
complete realised archive be supplied to an **offline** algorithm. Give every
row a strictly positive rational public acquisition price, fixed independently
of hidden values, and let a compulsory setup cost `F≥0` be common to all
certificates. If the realised coordinates and tariffs are rational, an exact
algorithm computes the cheapest realised robust TRUE-prefix certificate, or
reports that there is none, using `O(KN² log K)` rational arithmetic/comparison
operations and `O(KN)` working storage.

The setup constant may be any represented nonnegative number for which the
stated exact arithmetic is permitted; the rational assumption makes the
prototype executable. This is an arithmetic-operation bound, not a claim of
constant-cost operations on arbitrarily long encodings. No prefix or future
row is disclosed free to an online acquisition policy.

### Proof

Precompute all lower and upper corners and cumulative tariffs `P_g(b)` in
`O(KN)` arithmetic operations. For a fixed candidate prefix `a`, put

\[
p=L_A(a),\quad q=U_A(a),\quad
\sigma_g=\min\{b:L_g(b)\text{ does not Pareto-dominate }q\}.
\]

Here domination requires at least one strict improvement; equality is safe.
Since the lower corners are coordinatewise nondecreasing, safety is upward
closed in `b`. If some `σ_g` does not exist, no TRUE certificate has candidate
prefix `a`. Otherwise every such certificate pays the mandatory base

\[
B_a=F+P_A(a)+\sum_{g\ne A}P_g(\sigma_g).
\]

For `b≥σ_g`, let `δ_g(b)=P_g(b)−P_g(σ_g)≥0`. A TRUE certificate additionally
needs a strict northwest–southeast upper-corner witness pair against `p`
(P55 Lemma 2 and the endpoint criterion). Conversely, such a pair together
with all the safe prefixes suffices. Every feasible certificate can therefore
be reduced, without increasing cost, to the safe base plus extensions of just
two rivals.

For a northwest state `U_g(b)=(p_c−A,p_f+C)` with `A,C>0`, define

\[
\lambda_g(b)=\frac{C}{A+C}.
\]

It permits supporting weights `(α,1−α)` only if `α≤λ_g(b)`. For a southeast
state `U_h(c)=(p_c+D,p_f−E)`, `D,E>0`, define

\[
\mu_h(c)=\frac{E}{D+E}.
\]

It requires `α≥μ_h(c)`. Thus the two states certify unsupportedness exactly
when `μ_h(c)>λ_g(b)`. Equality does not suffice because scalarisation ties
count as support.

Every upper-corner sequence is coordinatewise nonincreasing. On its northwest
states, `A` is nondecreasing and `C` nonincreasing, so `λ` is nonincreasing as
`b` grows. On its southeast states, `D` is nonincreasing and `E` nondecreasing,
so `μ` is nondecreasing. A single rival cannot supply states of both kinds:
if northwest occurs first, its cost stays strictly below `p_c` forever; if
southeast occurs first, its failure stays strictly below `p_f` forever. Thus
any northwest and southeast states automatically have distinct rival labels.

All other upper corners can be omitted from these lists. In particular, an
upper corner that weakly dominates `p` with at least one strict improvement
is incompatible with its lower corner being safe against `q`, since
`L_g≤U_g≤p≤q`. A northeast corner or equality imposes no effective restriction
on nonnegative supporting weights. Robust nondomination therefore rules out
an omitted one-rival unsupportedness witness.

Each rival contributes at most one sorted threshold stream. Use increasing
prefix order for northwest streams and decreasing prefix order for southeast
streams, so every stream is sorted in descending threshold. Merge the at most
`K−1` streams with a binary heap. Keep the cheapest southeast increment among
all southeast states whose threshold has already been passed. At threshold
`z`, first evaluate every northwest state at `z` against this stored cheapest
southeast increment, and only afterwards insert southeast states tied at
`z`. This order implements the required **strict** inequality.

For every northwest state, the maintained southeast state is exactly a
minimum-cost southeast extension with threshold strictly greater than its
own. Hence the sweep computes

\[
\min_{\mu_h(c)>\lambda_g(b)}\bigl(\delta_g(b)+\delta_h(c)\bigr)
\]

and identifies its prefix witnesses. The minimum over candidate prefixes of
this quantity plus `B_a` is precisely the cheapest certificate. If no pair is
found for any candidate prefix, no TRUE prefix exists. Full census shows this
is equivalent to the complete archive being negative.

For one candidate prefix there are `O(KN)` safety tests and threshold states,
and their heap merge uses `O(KN log K)` comparisons and `O(KN)` storage. There
are `N+1` candidate prefixes. The asserted bounds follow. ∎

### Unequal archive lengths and known positive mean weights

The same proof extends to archive lengths `n_g` and publicly fixed masses
`ω_gj>0` satisfying `Σ_j ω_gj=1` in each group. The complete objective is
`p_g=Σ_j ω_gj z_gj`, and the corners are

\[
L_g(b)=\sum_{j\le b}\omega_{gj}z_{gj},\qquad
U_g(b)=L_g(b)+\left(\sum_{j>b}\omega_{gj}\right)(1,1).
\]

The endpoint proof is unchanged, and each `L_g` increases and `U_g` decreases
coordinatewise. Writing `L=Σ_g(n_g+1)`, the comparator uses
`O((n_A+1)L log K)` arithmetic/comparison operations and `O(L)` working storage.
This complements the general endpoint/witness extension in the separate P56
generalization report. Known mean weights and acquisition tariffs are distinct
inputs: a row's contribution to a mean need not equal its disclosure price.

The prototype accepts these extensions through an optional `weights` argument;
its default is the uniform mean separately in each archive. Weights must be
positive and sum exactly to one per group. Unequal archive lengths are allowed.

## Pseudocode

```text
precompute lower/upper corners and cumulative tariffs
best = infinity
for candidate prefix a = 0,...,N:
    compute the earliest safe prefix σ[g] of every rival
    if any rival has no safe prefix: continue
    base = setup + candidate cost + sum of safe rival costs
    make one descending NW or SE threshold stream per rival
    merge all streams in descending threshold order
    best_SE = none
    for each group of equal thresholds:
        use every NW state with best_SE to update best certificate
        add this group's SE states to the running cheapest best_SE
return best and its realizing prefix, or none
```

## Implementation and verification

Prototype: `p56_work/scripts/geo_comparator.py`.
Evidence: `p56_work/evidence/Geometry_Comparator_P56.json`.
Run from the project workspace:

```bash
python3 p56_work/scripts/geo_comparator.py
```

The prototype uses `fractions.Fraction`; floating point is used only to record
elapsed execution time, never in a verdict or cost comparison. It is a new
private research prototype, not part of the frozen public software release
`1.0.0`.

The independent oracle enumerates every realised prefix and intersects the
closed supporting-weight intervals directly. It does not use the merged
threshold algorithm, pair-cost selection, or a supplied comparator value.
The endpoint theorem is assumed by both implementations, so this is not an
independent proof of that theorem.

Executed exact checks:

| Corpus | Archives |
|---|---:|
| Exhaustive six-symbol square archives, `N=1`, `K=3,4` | 1,512 |
| Fixed-seed random archives and nonuniform rational prices, `K=3,...,6` | 800 |
| Designed positive archives, multiple witnesses, perturbed prefix order, rational prices | 400 |
| Triangle hard worlds U/V, `N=12,...,36`, with an expensive final candidate row | 14 |
| Unequal lengths, nonuniform positive mean weights, rational tariffs | 240 |
| **Total** | **2,966** |

The oracle inspected **695,812 prefixes**. There were **566 positive** and
**2,400 negative** archives. Every computed optimum agreed exactly, and every
returned prefix passed the separate interval oracle. The tie-sensitive
exhaustive alphabet includes `(0,1)`, `(1,0)` and `(1/2,1/2)` as a supported
equality control, and contains coincident configurations. Common setups were
also nonzero in many tests.

These finite checks are evidence for implementation correctness, not formal
verification or a substitute for the proof above. The measured run duration
in the JSON is environment-specific and is not a deployment benchmark.

A separate research track also reviewed the proof and final source and ran
an independent general-dimensional rational LP-vertex oracle: **100 archives**,
including **40 with unequal lengths and nonuniform importance weights**, **57
positive** cases and **15,516 exhausted prefix states**. All optima and returned
certificates agreed. This oracle does not reuse the interval oracle, corner
arrays or brute-force implementation above. See
`generalization_geometry_independent_review.md` and
`Generalization_Crosscheck_Geometry_P56.json`. This is an internal AI-assisted
review, not external peer review.

## What this improves, and what it leaves open

1. It reduces the asymptotic catalogue-size dependence of the article's
   retrospective optimiser from quadratic to essentially linear times a
   logarithm. This makes larger-catalogue exact replay more feasible.
2. It supports exact arbitrary tariffs directly, which is useful for a
   properly specified disclosure-cost model. It does not turn hypothetical
   tariffs into measured economic benefit.
3. It supplies independently checkable optimal prefixes for testing new
   acquisition policies. It gives no causal policy access to the retrospective
   optimum.
4. The offline optimiser alone makes no claim about an improved online
   triangle ratio. The separate P56 upper-bound track must be consulted for
   its new ratio result; it requires its own causal algorithm and all-input
   guarantee.

## Literature and claim calibration

The elementary merge and sweep are standard algorithmic techniques. The
model-specific decomposition into domination-safe prefixes and a strict
two-witness pair is already in P55 S1.1. The defensible claim is an improved
exact algorithm for **this manuscript's** hindsight benchmark. A targeted
literature sanity check found no identical merged-threshold comparator, but
does not establish priority or justify a claim of being the first polynomial
minimum-verification algorithm. Other settings already have polynomial exact
verification algorithms; for example Halldórsson and de Lima, *Query-
competitive sorting with uncertainty*, Theoretical Computer Science (2021),
DOI `10.1016/j.tcs.2021.03.021`, Theorem 7, concerns a different interval-sorting
verification task.

The new result is a computational strengthening suitable for a concise
replacement or addition to S1.1, subject to author review and the same final
integration checks as any manuscript amendment. P55 has not been edited.
