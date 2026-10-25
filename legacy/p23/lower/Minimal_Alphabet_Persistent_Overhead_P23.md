# Persistent certification overhead on a smallest possible alphabet

Antonio Clim — P23 research note, 23 October 2026.

This note strengthens the P22 construction by reducing its common public
alphabet from five symbols to the three vertices of the triangular domain.
The numerical lower bounds are unchanged. A separate minimality theorem
shows that no common alphabet with fewer symbols admits any positive input.
The results concern the declared mathematical acquisition model. They do not
claim historical priority, external review, physical validation or exact
global asymptotic acquisition ratios.

## 1. Contract and endpoint test

There are three labelled configurations, designated candidate A and rivals
L and R, each with N ordered rows. A query reveals the next whole row of
one configuration and costs one. The complete mean minimises both
coordinates. GOOD means that A is Pareto nondominated and is not supported
by any nonzero nonnegative linear scalarisation. Ties and axis weights
count as support. A valid algorithm terminates correctly on every legal
input. Its competitive ratio is evaluated on positive inputs against the
cheapest realised TRUE-prefix certificate.

Let the common public independent row-completion domain be

    S = {(0,0),(1,0),(1,1)}.

For a prefix of k rows with vector sum z, write lower corner z/N and
upper corner [z+(N-k)(1,1)]/N. Both corners are legal because S contains
(0,0) and (1,1). The exact robust TRUE test is the same as on the full
triangle T={(c,f):0<=f<=c<=1}:

1. No rival lower corner Pareto-dominates the candidate upper corner:
   coordinatewise no larger, with at least one strict inequality.
2. No nonzero nonnegative weight supports the candidate lower corner
   against all rival upper corners.

For completeness, failure of either condition gives a legal counterexample
completion by taking the named corners. Conversely, coordinatewise bounds
show that the first condition excludes domination in every completion and
that the second excludes a supporting weight in every completion. Corners
for different configurations can be attained simultaneously. The proof
therefore applies to S itself and to the full triangle, without assuming
that unseen rows follow the construction's particular block pattern.

## 2. Two fixed archives using only the three symbols

Fix q>=3 and N=4q. The common blocks are:

| Configuration | First block | Second block | Remaining common rows |
|---|---|---|---|
| A | 2q copies of (1,0) | q copies of (1,1) | q-1 copies of (0,0) |
| L | q copies of (1,1) | 2q copies of (0,0) | q-1 copies of (1,1) |
| R | N copies of (1,0) | — | — |

Only the last row of A and L distinguishes the worlds:

| World | Final row of A | Final row of L |
|---|---|---|
| U | (0,0) | (0,0) |
| V | (1,0) | (1,1) |

Put h=1/N, p=(3/4,1/4), u=(1/2,1/2) and v=(1,0).
After A's first 3q rows its lower corner stays p until the final row.
After L's first 3q rows its upper corner stays u until the final row.
The complete means are (p,u-h(1,1),v) in U and (p+(h,0),u,v) in V.

**Theorem 1 (exact TRUE prefixes).** The complete sets of TRUE prefixes are

    U: {(a,N,j): 3q+2<=a<=N, N-1<=j<=N};
    V: {(N,i,j): 3q+1<=i<=N, N-1<=j<=N}.

Consequently their minimum unit-price certificate costs are respectively
11q+1 and 11q.

### Necessity

In U, every L prefix before its final row has upper corner (l,l) with
l>=1/2. The upper R corner has coordinate sum at least one, whereas every
candidate lower corner has coordinate sum at most one. Equal positive
weights support that lower corner, so L census is mandatory.

At candidate length a=3q+1, the upper corner is (1-h,1/2-h). Even the
fully observed L has lower corner (1/2-h,1/2-h), which dominates it.
Information monotonicity therefore excludes every candidate length
a<=3q+1, independently of the order of the first 3q candidate symbols.

In V, every candidate prefix a<N has lower-corner coordinate sum at most
one. Both complete rivals have coordinate sum one, and their partial upper
corners can only be larger. Equal weights again support the candidate, so
candidate census is mandatory. For i<=3q the L lower corner has both
coordinates at most 1/4. It dominates the complete candidate
(3/4+h,1/4), so i>=3q+1 is mandatory.

In either world j>=N-1 is necessary. By information monotonicity, it is
enough to examine j=N-2 with A and L complete. The upper R corner is
(1,2h). For U the strict crossing determinant is

    (1/4+h)(1/4-2h) - (1/4-h)(1/4) = -2h^2 < 0.

For V the same expression results from the shifted candidate. The two
rival upper corners strictly cross the candidate (N>=12), and this
nonpositive determinant means that a nonnegative supporting weight exists.
Thus j=N-2 is not TRUE, and neither is any shorter R prefix.

### Sufficiency

At j=N-1 the R lower and upper corners are (1-h,0) and (1,h).

In U, at a=3q+2 and i=N, the candidate upper corner is
(1-2h,1/2-2h). L's lower failure 1/2-h exceeds the candidate upper
failure; R's lower cost 1-h exceeds its upper cost. Hence no rival lower
corner dominates it. The crossing determinant is

    (1/4+h)(1/4-h) - (1/4-h)(1/4) = h(1/4-h) > 0.

The candidate lower corner is strictly unsupported, so this prefix is TRUE.

In V, at a=N and i=3q+1, the L lower corner is
(1/4+h,1/4+h), whose failure exceeds the candidate's failure. R's lower
cost 1-h exceeds candidate cost 3/4+h because N>8. The same strictly
positive determinant excludes support. This prefix too is TRUE.

All componentwise extensions of these prefixes remain TRUE. The necessary
conditions and these least-state checks prove the exact sets. No prior
prefix-feasibility theorem is required for this construction. QED.

## 3. Lower bounds allowing arbitrary adaptive interleaving

Every TRUE prefix in either world contains the common base

    (b_A,b_L,b_R) = (3q+2,3q+1,N-1).

The candidate chain beyond this base has X=q-2 rows; the L chain has
Y=q-1 rows. All nonterminal candidate-chain rows are zero and all
nonterminal L-chain rows are (1,1). Their terminal rows distinguish U and V.
The unused final R row is the same in both worlds and does not replace
either decisive chain.

More generally, permit any fixed public positive row prices and a common
finite compulsory information-free setup cost F>=0. Let W be F plus the
base-row prices, and X,Y the two terminal-chain price sums. Theorem 1
gives exact comparator costs W+Y in U and W+X in V.

Let theta be the probability that A's terminal row is reached before L's
terminal row. Couple the two executions with the same private random seed.
Their histories are identical up to the first decisive terminal revelation,
so theta is identical in both fixed worlds. Every successful certificate
contains the whole winning chain. Therefore every valid algorithm obeys

    E[C(U)] >= W+Y+theta X,
    E[C(V)] >= W+X+(1-theta)Y.

Queries interleaved arbitrarily between chains, or taken before the entire
base is acquired, do not invalidate these inequalities: their prices are
nonnegative, and the displayed mandatory observations must still be paid.
Balancing gives the exact restricted-pair optimum

    1+XY/[X(W+X)+Y(W+Y)]

for randomisation, and

    1+min(X,Y)/(W+max(X,Y))

for deterministic policies. These values are attained on the pair by
acquiring the base and then whole chains in the appropriate random or
deterministic order. Applying the exact TRUE test after each relevant query
and otherwise using full census extends this to a valid all-input policy.
These are restricted-pair optima and global lower bounds, not global
optimality claims. The elementary two-chain search calculation itself is
inherited; the new statement is its three-symbol geometric realisation.

## 4. Every sufficiently large archive length

For any N>=12, put q=floor(N/4) and p=N-4q. Prepend p zero rows to
each configuration of both N0=4q archives. At corresponding post-padding
prefixes, all lower and upper corners are multiplied by N0/N. Positive
common scaling preserves both parts of the exact TRUE test. A prefix
inside a padding block cannot be TRUE: extending it to the block's end
would yield a TRUE state with a zero prefix in the unpadded construction,
contrary to Theorem 1.

The exact TRUE-prefix lists are thus translated by (p,p,p), with base

    (N-q+2,N-q+1,N-1).

At unit prices and zero setup, W=3N-2q+2, X=q-2 and Y=q-1. Hence:

**Theorem 2 (three-symbol persistent overhead).** For every N>=12, with
the same known common alphabet S throughout,

    R_rand(3,N;S) >= 1 + (q-2)(q-1) /
       [(q-2)(3N-q)+(q-1)(3N-q+1)],

    R_det(3,N;S) >= 1 + (q-2)/(3N-q+1),
    q=floor(N/4).

In particular,

    liminf_(N->infinity) R_rand(3,N;S) >= 23/22,
    liminf_(N->infinity) R_det(3,N;S) >= 12/11.

The same lower bounds hold on the full triangle. No growing coordinate
denominator, Ramsey extraction, unknown observation alphabet or continuous
row precision is involved. The constants remain lower bounds only.

## 5. Three symbols are necessary for any positive instance

**Theorem 3 (alphabet-cardinality minimality).** With a common alphabet of
at most two vectors in two objective dimensions, no archive has a GOOD
candidate, regardless of its row counts or ordering. Thus three is the
smallest cardinality of a common alphabet that can exhibit the persistent
overhead of Theorem 2, and already the smallest that admits any positive
instance.

Proof. With one vector all means coincide and every weight supports them.
With two vectors x,y, every configuration mean lies on their segment:
z=x+t(y-x). If the direction y-x has components of opposite signs, a
strictly positive normal makes every point on the segment tie, so every
candidate is supported. If a component of the direction is zero, the
corresponding coordinate-axis weight makes every point tie. In the remaining
case both direction components have the same strict sign. After orienting
the segment so both are positive, any point above the smallest realised t
is dominated by the configuration at that smallest t. A nondominated
candidate must therefore have the smallest realised t, and is supported by
either coordinate weight. All cases exclude GOOD. QED.

The positive-input scoring class for these smaller alphabets is empty.
The theorem does not assign a ratio of one, or any numerical competitive
ratio, to that empty class.

## 6. The sharp nonvacuity threshold on this alphabet

**Theorem 4 (smallest nonempty positive-input class).** For the same alphabet
S={(0,0),(1,0),(1,1)}, common row count N and any K>=3 configurations,
a positive input exists if and only if N>=5.

Proof. Every mean has the form (m/N,n/N), where m,n are integers with
0<=n<=m<=N. A nondominated unsupported candidate must have both a strictly
northwest rival and a strictly southeast rival: otherwise one of the
coordinate-axis weights supports it. Writing its numerator as (m,n), the
southeast rival forces n>=1 and m<=N-1. A northwest rival with numerator
(x,y) satisfies n+1<=y<=x<=m-1, so m-n>=2. Hence N>=4.

At N=4 the only possible candidate numerator is (3,1). Any rival that does
not dominate it has cost-plus-failure numerator at least four: if its cost
is at most two, its failure must be at least two; if its cost is three,
its failure must be at least one; if its cost is four, the claim is automatic.
The equal-weight scalarisation therefore supports the candidate against
every possible collection of nondominating rivals. Thus N=4 also has no
positive input. Equivalently, its only possible strict crossing pair is
(2,2),(4,0), collinear with (3,1).

At N=5 take candidate numerator (4,1), northwest rival (2,2) and southeast
rival (5,0). None dominates the candidate. A supporting weight written as
(alpha,1-alpha) would require alpha<=1/3 from the northwest rival and
alpha>=1/2 from the southeast rival, an impossibility. These means are
realised by S rows: respectively one (1,1), three (1,0) and one zero;
two (1,1) and three zeros; and five (1,0). For any N>5 prepend N-5 zero
rows; positive common scaling preserves GOOD. For K>3 add configurations
whose every row is (1,1); these do not dominate the candidate or restore
support. QED.

For N<=4 the positive-input scoring class on this particular alphabet is
empty. No numerical acquisition ratio is assigned to it. Theorem 2 starts
at N>=12 because of its particular exact-prefix construction; it does not
assert that smaller positive instances are absent.

**Corollary 4.1 (exact acquisition at the first nonempty length).** With
S as above, K=3 and N=5, every positive archive has only the full-census
TRUE prefix. Consequently R_rand=R_det=1, for any fixed strictly positive
row prices and any common finite compulsory information-free setup cost.

Proof. The integer restrictions in Theorem 4 leave only the candidate
numerators (3,1), (4,1) and (4,2). For (3,1), the only northwest rival is
(2,2) and a southeast rival is (4,0) or (5,0); neither pair gives strict
unsupportedness. For (4,1), a southeast rival must be (5,0). A northwest
rival (x,y) must satisfy 2<=y<=x<=3, and the strict crossing determinant
is 5-x-y. Only (2,2) makes it positive. For (4,2), the northwest rival
must be (3,3) and a southeast rival is (5,r), r in {0,1}; the determinant
is 1-r, so only (5,0) works. Thus, up to exchanging the two rival labels,
the only positive complete numerator triples are

    I:  candidate (4,1), northwest (2,2), southeast (5,0);
    II: candidate (4,2), northwest (3,3), southeast (5,0).

It suffices to exclude the strongest partial states: exactly one final
row unread, with both other configurations complete. Every proper prefix
is componentwise below one such state. In both families the southeast
archive consists entirely of (1,0); with its final row unread its lower
corner numerator (4,0) dominates the candidate.

For the northwest archive, the only possible last symbols are (1,1)
and (0,0). With (1,1) last, its lower corner is respectively (1,1) or
(2,2), dominating the candidate. With zero last, its upper corner is
respectively (3,3) or (4,4); the candidate is supported against both rival
upper corners by weight (1,1) in I and weight (1,0) in II.

For the candidate, a last symbol (0,0) or (1,0) makes its upper corner
dominated by the complete northwest rival. A last symbol (1,1) makes its
lower corner respectively (3,0) or (3,1), supported by weight (0,1) in I
and weight (1,1) in II. These cases exhaust the possible last symbols.
All proper prefix states fail TRUE. Full census is therefore both the
only certificate and an exact all-input acquisition policy. The statement
holds for arbitrary positive prices because the mandatory observation set,
not merely its unit-price size, is identical to full census. QED.

At unit prices this gives a strict domain-class contrast with the full
triangle's P22 values 71/67 and 15/14 at N=5. The contrast does not come
from changing the TRUE-prefix set of a shared realised archive: the endpoint
test is identical. The smaller public alphabet changes the admissible class
of archives. The exact ratio one is not an asymptotic assertion, as Theorem 2
shows persistent overhead on the very same alphabet for long archives.

## 7. Executed checks and limitations

The accompanying checker is independent of the P22 support-interval
implementation: it tests the finitely many candidate weight vertices
0, 1 and the individual affine-inequality roots using integer arithmetic.
It checks exact TRUE sets of explicit three-symbol archives, including
padding, and verifies price balancing and small two-symbol alphabets.

The all-N and all-algorithm claims rest on the proofs above, not on the
finite computation. The q=2 adverse boundary from P22 is preserved as a
negative control. No external scientific code, installation, network
request, measurement or external review is part of this result.
