# Six-row triangular acquisition: exact deterministic ratio and a randomised lower bound

23 October 2026. New internal research result relative to P22. Historical
priority, external peer review and formal verification are not claimed.
All earlier project sources remain unchanged.

## 1. Contract and statements

There are three labelled configurations, a designated candidate A and two
rivals, each with N=6 ordered whole rows in
T={(c,f):0<=f<=c<=1}. Every unread row is independently completable in T.
A next-row query costs one. A common compulsory, information-free finite
setup cost F>=0 is added once to every algorithm and comparator cost.
GOOD means Pareto nondomination and unsupportedness by every nonzero
nonnegative linear scalarisation; axes and ties count as support.
Algorithms must be correct and terminate on all inputs, with no positive
promise. Ratios are scored on positive inputs against their minimum realised
robust TRUE-prefix cost. Let C* denote this minimum ROW cost, excluding F.

**Theorem 1.** On the full continuous triangular domain,

    R_det,T*(3,6;F) = 1 + 1/(F+16).

In particular the zero-setup optimum is 17/16.

**Theorem 2.** On the same domain,

    R_rand,T*(3,6;F) >= 1 + 5/(6F+98).

At zero setup this is 103/98. It is a lower bound only: this note does
NOT establish the global randomised optimum. The deterministic policy of
Theorem 1 also supplies the valid, generally weaker, randomised upper
1+1/(F+16).

## 2. All feasible oriented prefix shapes

Use the exact corner criterion and triangular shape theorem proved in the
preceding manuscript/addendum. If a,i,j are the candidate, northwest and
southeast prefix lengths, respectively, let

    Z=i+2j+2a-24.

A TRUE prefix of these lengths exists iff

    Z>0 and Z^2 > 4(12-a-i)(12-a-j).

The componentwise minimal feasible shapes are precisely

    (5,5,6), (6,1,6), (6,5,5), (6,6,4).                 (1)

Here is an analytic reduction, independently checkable by the accompanying
216-shape enumeration. The sharp candidate law a>3N/4 forces a>=5. At a=5,
j<=5 is impossible even when i=6: its largest feasibility value occurs at
i=6,j=5, where Z=2 and Z^2=4<8. At a=5,j=6, Z=i-2, hence feasibility
reduces to (i-2)^2>4(7-i), equivalently i^2>24, giving i>=5.

At a=6, j=6 admits every i>=1. At j=5, the criterion is
(i-2)^2>4(6-i), equivalently i^2>20, hence i>=5. At j=4,
it is (i-4)^2>8(6-i), with i>4; this gives i^2>32, hence i=6.
At j<=3, even i=6 fails (the j=3 case is equality). These facts prove (1).

Consequently C*>=13. A certificate with a<6 has a=5. Its least possible
cost is 16, attained only at (5,5,6); a candidate-partial cost-17 certificate
has shape (5,6,6). Candidate-census certificates with C*<=15 have shape
(6,i,6) with i<=3. Candidate-census cost-16 shapes are exactly

    (6,4,6), (6,5,5), (6,6,4).                         (2)

## 3. An observable deterministic policy

Census the candidate and let its realised mean be p=(p_c,p_f), with gap
g=p_c-p_f. Screen each rival only to its first P2-safe prefix: the first
prefix whose lower corner does not dominate p. On a positive archive,
every candidate-census TRUE certificate contains these screened prefixes.
The two rivals have identifiable opposite orientations. A northwest rival
has first-safe lower failure above p_f and cost below p_c; a southeast rival
has first-safe lower cost above p_c and failure below p_f. Equality and
noncrossing cases can be sent to full census. On a positive archive those
exceptional cases cannot occur: a strict crossing pair is necessary.

Choose the completion order by the observed gap alone:

    if g<=1/3, census the northwest rival first;
    if g>1/3, census the southeast rival first.

Test the exact robust TRUE predicate before each new row when stopping is
possible; after completing the selected side, extend the other side only
until TRUE. If TRUE is never reached, full census decides the input exactly.
This specifies a legal complete policy, including negative inputs.

For a censused candidate, elementary strict P2/crossing inequalities imply

    partial northwest length i: g > 1-i/6;
    partial southeast length j: g < j/3-1.              (3)

These restrictions concern any positive certificate; they are not inferred
from hypothetical unobserved values.

If C*<=15, (1) gives a certificate (6,i,6), i<=3, and (3) forces g>1/2.
The policy therefore completes the southeast side and reaches a certificate
at cost at most C*: screening cannot exceed its required prefixes, and the
other side is extended only to the first TRUE state. Hence the policy is
exactly optimal on every such archive.

If a cost-16 candidate-census certificate exists, the three cases in (2)
are exhaustive. For (6,4,6), (3) forces g>1/3, so the southeast-first policy
costs at most 16. For (6,6,4), (3) forces g<1/3, so northwest-first costs at
most 16. For (6,5,5), whichever side is completed first, the resulting TRUE
extension has cost 17, so the policy costs at most 17.

It remains to handle a cost-16 candidate-PARTIAL certificate (5,5,6).
Let its candidate lower corner have gap g0. In the band-feasibility proof,
t=s=1/6, r=0, U=1/3, V=1/6 and b=1. The necessary strict inequality is

    (g0-1/3)(5/6-g0)>1/18,

or, equivalently, (g0-1/2)(g0-2/3)<0. Thus

    1/2<g0<2/3.

The final candidate row has nonnegative c-f, so its full gap g>=g0>1/2.
The policy completes the southeast side first. Extending the known TRUE
prefix (5,5,6) to (6,5,6) preserves TRUE, hence costs at most 17. Its first
safe screening prefixes cannot exceed this TRUE extension.

Every remaining positive archive has C*>=17 and costs at most full census,
18. With the common setup included, the only potentially largest excess
ratios are 1/(F+16) at C*=16 and 1/(F+17) at C*=17. This proves the global
upper bound in Theorem 1 for every F>=0.

## 4. Fixed worlds matching the deterministic upper

The first five candidate rows are (249/250,3/10), giving candidate lower
p=(83/100,1/4). Every southeast row is (1,0). The northwest common rows are

    rows 1,2: (19/25,19/25);
    rows 3,4: (7/50,7/50);
    row 6:   (1,1).

The two differing rows are

    world U: candidate row 6=(0,0), northwest row 5=(37/50,37/50);
    world V: candidate row 6=(1,0), northwest row 5=(1,1).

Both archives are fixed before private randomness. Their exact TRUE sets are

    U: {(a,i,6): a>=5, i>=5};       C*_U=16;
    V: {(6,i,6): i>=2};            C*_V=14.             (4)

To verify (4), a>=5 follows from the universal candidate law. In U,
the northwest upper point before row 5 is at least (19/30,19/30), which
supports p together with (1,0): its diagonal coordinate exceeds
p_f/(1-p_c+p_f)=25/42. Thus i>=5 is necessary. In V even the full northwest
mean is (19/30,19/30), so every a<6 fails for the same reason. With a=6,
one northwest row has lower failure 19/150<1/4 and lower cost below the
candidate, so it dominates the candidate; i>=2 is necessary.

In U, even with the candidate and northwest fully known, a southeast prefix
of five has upper (1,1/6). The unsupportedness determinant is

    (83/100-59/100)(1/4-1/6)
       -(59/100-1/4)(1-83/100) = -189/5000 < 0.

In V the southeast lower corner at prefix five is (5/6,0), which dominates
the full candidate (299/300,1/4). Thus j=6 is necessary in both worlds.
Prefix monotonicity excludes all smaller omitted states.

At U's least listed state (5,5,6), candidate upper is (299/300,5/12),
northwest lower is (127/300,127/300), northwest upper is (59/100,59/100)
and the southeast point is (1,0). The P2 safety margins are 1/150 in
northwest failure and 1/300 in southeast cost. The strict unsupportedness
determinant is 11/5000>0.

At V's least listed state (6,2,6), the full candidate is (299/300,1/4),
northwest lower is (19/75,19/75) and upper is (23/25,23/25). Both P2 safety
margins are 1/300. The strict determinant is 127/7500>0. Monotonicity now
proves every listed extension TRUE, completing the exact sets.

The worlds agree until either candidate row 6 or northwest row 5 is read.
Let theta be the probability of reading candidate row 6 first. It has the
same distribution on both fixed archives under arbitrary adaptive prefix
interleaving and private randomisation. No TRUE state precedes both
distinguishing observations. From (4), every algorithm correct on the full
class obeys

    E[C(U)]>=16+theta;
    E[C(V)]>=14+3(1-theta).

For a deterministic algorithm theta is zero or one. Its worst ratio is
therefore at least min{(F+17)/(F+16),(F+17)/(F+14)}=1+1/(F+16).
Together with the global upper, this proves Theorem 1. Randomisation of
this pair alone gives the weaker lower 1+3/(4F+62).

The same deterministic equality holds when the public independent
completion domain is the seven-symbol alphabet used in these worlds,
because it contains both (0,0) and (1,1): the endpoint corner test remains
exact, the hard TRUE sets remain unchanged and the continuous-domain upper
policy applies. No minimum-alphabet claim is made.

## 5. A stronger randomised lower pair

Use first five candidate rows (249/250,3/25), so their lower mean is
p=(83/100,1/10). Every southeast row remains (1,0). Northwest row 1 is
(61/100,61/100), and rows 2 through 5 are (7/25,7/25). Set the final rows:

    world A: candidate row 6=(0,0), northwest row 6=(7/25,7/25);
    world B: candidate row 6=(1,0), northwest row 6=(1,1).

The exact TRUE sets are

    A: {(5,6,6),(6,6,6)};          C*_A=17;
    B: {(6,i,6):1<=i<=6};          C*_B=13.              (5)

Again a>=5 is compulsory. The northwest upper point before its final row
is at least (91/200,91/200), which supports p together with (1,0), since
91/200>p_f/(1-p_c+p_f)=10/27. Hence A requires northwest census, while B
requires candidate census even with both rivals full. A wholly unread
northwest rival dominates the candidate, so B requires at least one row.
Every southeast prefix j<=5 has upper failure at least 1/6>1/10; northwest
upper failure also exceeds 1/10. The failure axis therefore supports the
candidate lower corner until the southeast is full, in both worlds.

At A's least state (5,6,6), its candidate upper is (299/300,4/15), northwest
mean is (67/200,67/200), and southeast mean is (1,0). Both P2 comparisons
are strictly safe; the unsupportedness determinant is 191/20000>0.
At B's least state (6,1,6), candidate mean is (299/300,1/10), northwest
lower is (61/600,61/600), upper is (187/200,187/200), and southeast is
(1,0). P2 margins are 1/600 and 1/300; the determinant is 203/60000>0.
These minimal TRUE states and the necessary conditions establish (5).

The worlds remain identical until candidate row 6 or northwest row 6 is
read. If the candidate terminal row is read first with probability q,
the two expected row costs are at least 17+q and 18-5q respectively.
Balancing their ratios gives

    q=5(F+17)/(6F+98),
    R_rand,T*(3,6;F)>=1+5/(6F+98).

The argument permits arbitrary prefix interleaving; reaching the northwest
terminal row first necessarily pays all five rows beyond its compulsory
first row. Actual worlds, not an adversary reacting to private coins,
supply the bound. This proves Theorem 2. The pair uses six fixed symbols,
including both endpoints, and therefore also proves the same lower on
that known alphabet or the uniform 1/500 triangular grid.

## 6. Verification and limitations

The accompanying own standard-library checker enumerates every prefix
state of all four fixed archives using exact integer corner arithmetic,
enumerates all 216 positive length triples, checks the strict determinants
and P2 margins, and checks the setup-dependent lower and upper arithmetic.
The all-domain policy proof is analytic; finite enumeration does not cover
all numerical continuous archives. The randomised global optimum remains
open. No measurements, external scientific code, installation, public
deposit, external peer review or theorem-prover execution is involved.
