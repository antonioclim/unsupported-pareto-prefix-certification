# Constant acquisition overhead on one fixed coarse triangular alphabet

23 October 2026. New analytic result relative to P21 and the earlier P22
two-rival construction. The earlier files remain unchanged. This note proves
lower bounds for the full input problem, not exact global acquisition ratios.
It does not assert historical priority, external review or formal verification.

## 1. Model and the fixed alphabet

Use the P21 model: three ordered configurations, candidate A and rivals L,R,
each with N whole rows in T={(c,f):0<=f<=c<=1}; independent completion of each
unread row; next-row prefix queries; zero-error termination on all inputs;
GOOD means nondomination and unsupportedness by every nonzero nonnegative
linear scalarisation, with axes and ties counting as support. The cost ratio
is scored on positive archives against the cheapest realised TRUE prefix.

The construction uses the SAME alphabet for every N:

    S={(0,0),(1,0),(1,1),(1,1/3),(1/3,1/3)}.

Thus all actual coordinates belong to {0,1/3,1}; S is contained in the fixed
uniform 1/3 triangular grid. Coordinate denominators do not grow with N.
Because S contains both complete-vector endpoints, the exact corner test
continues to hold when S itself is the public independent completion domain.
Consequently every bound below holds for the continuous triangle, the fixed
1/3 triangular grid and this single fixed five-symbol domain. No claim of
minimum alphabet cardinality is made.

## 2. Two explicit archives at N=4q, q>=3

The common observations are:

* Candidate A: the first 3q rows are (1,1/3), the next q-1 are (0,0).
* Northwest rival L: the first 3q rows are (1/3,1/3), the next q-1 are (1,1).
* Southeast rival R: all 4q rows are (1,0).

The final candidate and L observations distinguish the two fixed worlds:

    World U: final candidate (0,0), final L (0,0).
    World V: final candidate (1,0), final L (1,1).

Let h=1/N and p=(3/4,1/4). After its first block, the candidate lower corner
stays p until its final row. Its actual mean is p in U and p+(h,0) in V.
After L's first block, its upper corner stays u=(1/2,1/2) until its final
row. Its actual mean is u-h(1,1) in U and u in V. The complete R mean is
v=(1,0). Candidate p lies exactly on segment uv.

**Theorem 1 (complete TRUE-prefix sets).**

    U: {(a,N,j): 3q+2<=a<=N, N-1<=j<=N};
    V: {(N,i,j): 3q+1<=i<=N, N-1<=j<=N}.

The unit-price minimum certificate costs are 11q+1 in U and 11q in V.

### Proof: necessary prefixes

The P21 triangular feasibility theorem requires a>3N/4=3q in every TRUE
prefix. This theorem still supplies a necessary condition on the fixed S
domain because its corners are exact there.

In U, before L's last row, the sum of coordinates of its upper corner is at
least one. R's upper-corner sum is also at least one, whereas the candidate
lower-corner sum is at most one. Equal scalarisation weights therefore
support the candidate lower corner: L census is compulsory. At candidate
prefix a=3q+1 its upper corner is (1-h,1/2-h). Even the fully observed L has
lower corner (1/2-h,1/2-h), which dominates it (strictly in cost, equally in
failure). Thus a>=3q+2 is compulsory in U. Monotonicity excludes shorter
candidate prefixes as well.

In V, every candidate prefix a<N has lower-corner sum at most one. Even
after full rival observation, L and R both have coordinate sum one, so equal
weights support that lower corner. Candidate census is compulsory. With the
candidate full, any L prefix i<=3q has lower failure at most 1/4 and lower
cost at most 1/4, hence dominates (3/4+h,1/4). Thus i>=3q+1 is necessary.

In either world, R requires at least N-1 observations. By monotonicity it
suffices to inspect j=N-2 with the candidate and L fully known. Write the
upper R corner as (1,r), with r=2h. In U the northwest point is
(1/2-h,1/2-h) and the candidate lower is p. In V the northwest point is u
and the candidate lower is p+(h,0). In both cases the crossing determinant
that would have to be positive for unsupportedness is

    (1/4+h)(1/4-r) - (1/4-h)(1/4)
       = h/2-r/4-hr = -2h^2 < 0   at r=2h.

The northwest/southeast crossing inequalities hold since N>=12. Thus a
positive normal to their negatively sloped segment supports the candidate.
No shorter R prefix can certify TRUE.

### Proof: sufficient prefixes

It remains to check the componentwise least states in the displayed sets.
At j=N-1, the R lower and upper corners are (1-h,0) and (1,h).

In U at a=3q+2, candidate upper is (1-2h,1/2-2h). L's lower failure
1/2-h exceeds candidate upper failure, and R's lower cost 1-h exceeds
candidate upper cost. Hence P2 is safe. At i=N, the unsupportedness
determinant becomes

    (1/4+h)(1/4-h)-(1/4-h)(1/4)
       = h(1/4-h)>0.

The strict crossing conditions hold, so the candidate is unsupported.

In V at i=3q+1, L's lower corner is (1/4+h,1/4+h), whose failure exceeds
the full candidate failure 1/4. R's lower cost 1-h exceeds the candidate
cost 3/4+h because N>8. The same determinant h(1/4-h)>0 establishes
unsupportedness. Therefore the least state is TRUE. All its componentwise
extensions remain TRUE. Necessity and sufficiency prove the complete lists.
QED.

## 3. Hidden terminal chains and exact restricted-pair cost

Every TRUE prefix in either world contains the common base

    candidate length b_A=3q+2,
    northwest length b_L=3q+1,
    southeast length b_R=N-1.

The candidate tail from b_A+1 to N has length X0=q-2 and consists of zeros
until the distinguishing final row. The L tail from b_L+1 to N has length
Y0=q-1 and consists of ones until its distinguishing final row. Thus an
algorithm cannot distinguish the worlds by inspecting an early tail row.
It must reach a terminal row, possibly after arbitrary interleaving.

Permit arbitrary fixed positive row prices and a common finite compulsory
information-free setup F>=0. Let W be F plus the prices of all rows in the
common base, X the total candidate-tail price and Y the total L-tail price.
Theorem 1 makes the exact comparator costs W+Y in U and W+X in V. The final
R row is unnecessary in both minima and does not distinguish the worlds;
querying it cannot invalidate the following lower bound.

**Theorem 2 (priced pair theorem).** The optimum worst-case ratio on this
pair, among algorithms valid on the complete input class, is

    1+XY/[X(W+X)+Y(W+Y)]                 for randomisation,
    1+min(X,Y)/(W+max(X,Y))              deterministically.

Consequently these expressions lower-bound the global acquisition optima.

Proof. Let theta be the probability that the candidate's final row is reached
before L's final row. Both fixed archives induce the same law for this event.
In U every certificate contains the complete L tail; if the candidate is
finished first, its whole tail is wasted. In V every certificate contains
the complete candidate tail; if L is finished first, its whole tail is
wasted. Therefore

    E[C(U)] >= W+Y+theta X,
    E[C(V)] >= W+X+(1-theta)Y.

This argument permits interleaving, queries before completing the common
base and all private randomisation. Equalising excess ratios gives

    theta=Y(W+Y)/[X(W+X)+Y(W+Y)].

For a deterministic algorithm theta is zero or one. Both lower bounds are
attained on the pair by acquiring the base, choosing an entire tail with
the stated probability (or the cheaper tail first deterministically),
testing TRUE and acquiring the other tail if needed. On other inputs full
census is an exact terminating fallback, including R's final row if needed.
Hence this is compatible with correctness over the complete input class.
QED.

This is the standard two-terminal-chain indistinguishability mechanism.
Its new role here is the explicit triangular realisation with exact
certificate sets and a fixed coarse alphabet, not a new abstract search game.

## 4. Every sufficiently large N and constant limits

For arbitrary N>=12 take q=floor(N/4)>=3 and d=N-4q in {0,1,2,3}. Prepend
d zero rows to every group of both archives. After the padding, every corner
is multiplied by 4q/N relative to the unpadded state. Positive common scaling
preserves the corner tests. A prefix inside the padding cannot certify TRUE:
extending it to the padding's end cannot destroy TRUE, and the corresponding
unpadded zero-prefix state is absent from Theorem 1. Thus the exact TRUE
sets are translated, with common base

    b_A=N-q+2, b_L=N-q+1, b_R=N-1.

The hidden-tail lengths remain q-2 and q-1. At unit prices and F=0,

    W=3N-2q+2,
    C*_U=3N-q+1,  C*_V=3N-q.

**Corollary 3 (nonvanishing fixed-alphabet lower bound).** For every N>=12,
on each of the continuous triangle, the fixed 1/3 triangular grid and the
single fixed five-symbol alphabet S,

    R_rand(3,N) >= 1 + (q-2)(q-1) /
       [(q-2)(3N-q)+(q-1)(3N-q+1)],

    R_det(3,N) >= 1 + (q-2)/(3N-q+1),
    where q=floor(N/4).

In particular,

    liminf_(N->infinity) R_rand(3,N) >= 23/22,
    liminf_(N->infinity) R_det(3,N) >= 12/11.

For N=4q the randomised excess is (q^2-3q+2)/(22q^2-32q-1), and the
deterministic excess is (q-2)/(11q+1). The finite-N formula should be combined
with stronger established lower bounds where appropriate; it is not claimed
to dominate every small-N result. The limits are lower bounds for global
minimax, not proved exact global asymptotic values.

The alphabet restriction is especially relevant to the scope: persistent
overhead occurs with denominator-three observations and does not depend on
Ramsey extraction or increasing observation precision. It is a statement
about the declared mathematical observation contract, not a measured radio
or IoT effect.

## 5. Executed validation and limits

The companion own-code standard-library checker uses an exact integer
implementation of the scalarisation feasibility inequalities. It enumerates
all prefix states of small constructed archives, and for larger archives
checks complete two-dimensional slices together with the monotone exclusion
of all remaining states. It also checks arbitrary-price balancing identities,
the support/unsupported determinant values and fixed-alphabet membership.

The finite computation verifies explicit archives and arithmetic. All-N,
all-price and algorithm-quantifier claims rely on the analytic arguments
above. No external scientific code, installation, network request, physical
measurement, external peer review or theorem-prover execution is involved.
