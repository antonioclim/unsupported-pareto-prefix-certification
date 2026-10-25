# Universal three-configuration acquisition bounds on the triangle

Antonio Clim — P23 research note, 23 October 2026.

This note proves upper bounds, not exact global minimax values. It uses the
P21 endpoint certificate lemma and the P22 oriented feasibility argument.
The randomised bound has a small exact polynomial certificate, verified by
own standard-library rational code. It is not a sample extrapolation,
external review or theorem-prover verification.

## 1. Result and scope

There are three ordered configurations: designated candidate A and two
rivals, each containing N whole records in
T={(c,f):0<=f<=c<=1}. Every unread row is independently completable in T.
Queries reveal the next row of one configuration, at unit cost. GOOD means
Pareto nondomination and unsupportedness by every nonzero nonnegative
linear scalarisation; ties and coordinate axes count as support.
Algorithms must terminate correctly on every legal archive, including
negative ones. The competitive comparator is the cheapest realised TRUE
prefix, including candidate-partial prefixes.

**Theorem.** For every integer N>=1, at unit prices and zero setup,

    R_rand,T*(3,N) <= 35/32,
    R_det,T*(3,N) <= 3/(4 sqrt(2)-3) = (9+12 sqrt(2))/23.

The same numerical upper bounds hold with any finite common compulsory
information-free setup F>=0. They also hold on any declared independent
row domain S contained in T that includes both (0,0) and (1,1), because
the endpoint certificate predicate is unchanged. In particular they apply
to the three-vertex alphabet {(0,0),(1,0),(1,1)} and every positive-width
diagonal band from P22. This does not claim the bounds are sharp on any of
these domains. The transfer is a per-positive-input guarantee; a minimax
ratio for a restricted domain is asserted only when its positive class is
nonempty. No numerical ratio is assigned to an empty positive class. The
known exact small-N and narrow-band bounds should be used whenever stronger.

## 2. Observable policies and a per-certificate envelope

Both policies first acquire all candidate rows, giving its exact mean p
and gap G=p_c-p_f. If G is 0 or 1, or another exceptional/negative branch
is encountered, finish all observations and decide exactly. No positive
archive has G=0 or G=1: its two strict crossing rivals would require a
positive gap and a strictly larger southeast gap, respectively.

Screen each labelled rival, in a fixed label order, to the first prefix
whose lower corner does not dominate p. On a positive archive this always
identifies one northwest rival and one southeast rival. The northwest
lower corner has cost strictly below p_c and failure strictly above p_f;
the southeast corner has the opposite strict inequalities. A positive
archive cannot have an entirely northeast rival or two rivals on the same
side. If the observed screen does not identify the required crossing
sides, the policy may simply finish all rows and decide exactly.

After screening, select one side, finish that rival, then extend the other
until the exact TRUE test succeeds or full census is reached. At every
eligible step, testing TRUE and stopping earlier is allowed. Negative
archives always reach an exact full-census decision.

These screens do not waste observations relative to any TRUE certificate.
To see this even for a candidate-partial certificate, let its prefix
lengths be (a,i,j), with i northwest and j southeast. The northwest upper
corner has cost below the candidate lower cost. Robust nondomination
therefore requires its lower failure to exceed the candidate upper
failure. Its actual mean is strictly northwest of the full candidate.
The analogous argument makes the southeast actual mean strictly
southeast. Thus the orientations agree for every TRUE certificate on the
same archive, and the first safe screens occur no later than i,j.

Consequently, for every realised TRUE certificate (a,i,j), regardless of
its optimality, the two deterministic completion orders satisfy

    C_NW-first <= 2N+j,
    C_SE-first <= 2N+i.

Completing the candidate and one rival only extends the original TRUE
state; by the time the other reaches its certified prefix, TRUE is
unavoidable. Earlier stopping or an already-complete screen only improves
these upper envelopes.

Normalise the unread fractions by

    t=1-a/N, s=1-i/N, r=1-j/N,

and let g be the gap of the candidate *lower* corner at length a. Write

    U=s+t, V=r+t, C=(a+i+j)/N=3-U-V+t.

Because each unread actual row has gap in [0,1],

    g <= G <= g+t.

The necessary part of the P22 geometric proof gives

    (g-U)(1+t-g-2V)>UV,                           (1)
    g>U>=t, 1+t-g-2V>0, V>=t.

Indeed, the two strict crossing witnesses give positive horizontal and
vertical differences whose product must beat the product of their robust
nondomination margins. The northwest observed gap is nonnegative and the
southeast observed gap is at most 1-r. These yield precisely (1), not just
the gap-free feasibility condition.

For a policy choosing southeast first with probability p(G), its excess
normalised cost above this certificate is at most

    t+(1-p(G))s+p(G)r = (1-p(G))U+p(G)V.            (2)

The proof below bounds (2)/C for every TRUE certificate. Selecting a
minimum certificate afterwards therefore preserves the retrospective
comparator and does not assume that the policy knows its prefix lengths.

## 3. Elementary deterministic upper

Put h=6-4 sqrt(2), the smaller root of h^2-12h+4=0. Thus 1/3<h<1.
Choose northwest first when G<=h, southeast first otherwise. For rational
observations, comparison with h requires no numerical approximation:
G<=h is equivalent to (6-G)^2>=32, since 0<=G<=1.

### Northwest-first branch

Here g<=G<=h and the excess ratio is U/(3-U-r). Solving (1) for U gives

    U < g(1-g-2r-t)/(1-g-r)
      <= g[1-r/(1-g-r)] <= g(1-r/3).

All displayed denominators are positive by (1), and 1-g-r<=1<3.
The last bound is exactly sufficient for

    U/(3-U-r) <= g/(3-g) <= h/(3-h).

### Southeast-first branch

Set x=g-t, so x>s>=0. Solving (1) for V gives

    V < (x-s)(1-x)/(2x+t-s).

Let V0=x(1-x)/(2x+t). Direct multiplication gives

    [(x-s)(1-x)/(2x+t-s)] / V0 <= (3-s)/3,

because the difference after clearing positive denominators is

    s[x+t-x(2x+t)/3+xs/3] >= 0.

The bracket is nonnegative for 0<x<1 and t,s>=0. Therefore

    V/(3-s-V) <= V0/(3-V0).

Since G<=g+t=x+2t and G>h, we have t>=(h-x)/2. Hence

    V0 <= 2x(1-x)/(3x+h) <= h.

The second inequality follows from

    2x^2+(3h-2)x+h^2
      =2[x-(2-3h)/4]^2 >=0,

using h^2-12h+4=0. Thus this branch also has excess ratio at most
h/(3-h), proving the deterministic bound 3/(3-h).

The apparently simpler threshold 1/3 proves a 9/8 bound only when the
comparator is required to census the candidate. That restriction is not
our model. The necessary-inequality relaxation can violate the attempted 9/8
*envelope*: t=1/20,g=29/100,s=0,r=29/100,G=g+t satisfies (1), yet
(t+r)/(3-t-s-r)=17/133>1/8. This is a failure of that upper-bound
argument, not a counterexample to every possible 9/8 policy or even a
claim that every envelope is attained by its policy. The optimised threshold above
handles the whole comparator without that gap.

## 4. Randomised policy and reduction to two polynomials

Use the same candidate census and screens, then select southeast first
with probability

    p(G)=2G/(1+G),

and northwest first with the remaining probability. The probability is
legal for 0<=G<=1. It depends only on observations already acquired.

Set e=3/32. By (2), it suffices to prove

    (1-p(G))U+p(G)V <= e(3-U-V+t).

Multiplication by 1+G>0 gives the equivalent inequality

    A(G)U+B(G)V <= C(G,t),                        (3)

where

    A(G)=(1+e)+(e-1)G,
    B(G)=e+(2+e)G,
    C(G,t)=e(3+t)(1+G).

A(G)>0 on the unit interval. Both sides of (3) are affine in G, so it
suffices to check G=g and G=g+t. No inference from finitely sampled gap
values is being made.

Let k=1+t-g. Solving (1) for U yields

    U < g(k-2V)/(k-V).

Because U,V>=t, evaluating the left side of (1) minus its right side at
U=V=t gives

    0<=t<g(1-g),  0<g<1.

For fixed g,t the permitted southeast quantity lies in

    t <= V < t+[g(1-g)-t]/(2g-t).

Consequently all required states are covered by the cube parameters
g,z,w in [0,1], using

    t=g(1-g)z,
    H=2-(1-g)z,
    J=w(1-z),
    E=H-J,
    Vn=gzH+J,
    Un=(1-gz)H-2J,
    V=(1-g)Vn/H,
    U <= g Un/E.

The boundary cube points include limits of legal states; it is enough to
prove nonnegativity on the entire larger closed cube. H>=1 and E>=1
there, so clearing these denominators is safe. For G0=g and G1=g+t,
define the explicit polynomials

    P_j(g,z,w) = C(G_j,t) H E
                 - A(G_j) g H Un
                 - B(G_j)(1-g) Vn E,  j=0,1.      (4)

Their multidegrees are (5,3,2) and (6,4,2), respectively. Positivity of
both P_j proves (3), then the expected-cost upper for every certificate.

## 5. Exact positivity certificate over the continuous cube

The following is a finite exact polynomial proof certificate. For each
listed sub-box, expand P_j in the tensor Bernstein basis at its stated
multidegree after affine rescaling to [0,1]^3. Every basis function is
nonnegative and their sum is one. Thus a positive minimum coefficient
proves positivity throughout that box, including every real interior
point. The table covers the whole unit cube; it is not a grid of sampled
values.

Intervals are closed and shared boundaries cause no problem.

| Polynomial | g interval | z interval | w interval | Minimum Bernstein coefficient |
|---|---|---|---|---|
| P0 | [0,1/2] | [0,1/2] | [0,1/2] | 1409/20480 |
| P0 | [0,1/2] | [0,1/2] | [1/2,1] | 969/20480 |
| P0 | [0,1/2] | [1/2,1] | [0,1] | 143/15360 |
| P0 | [1/2,1] | [0,1] | [0,1] | 27/1024 |
| P1 | [0,1/2] | [0,1/2] | [0,1] | 1/128 |
| P1 | [0,1/2] | [1/2,1] | [0,1/2] | 53/2048 |
| P1 | [0,1/4] | [1/2,1] | [1/2,1] | 86967/1048576 |
| P1 | [1/4,1/2] | [1/2,3/4] | [1/2,1] | 2261/3145728 |
| P1 | [1/4,1/2] | [3/4,1] | [1/2,1] | 725/1572864 |
| P1 | [1/2,1] | [0,1/2] | [0,1] | 7/128 |
| P1 | [1/2,1] | [1/2,1] | [0,1] | 9/1024 |

For reproduction, if P=sum c_alpha x^alpha has multidegree n, its unit
cube Bernstein coefficient at index i is

    b_i=sum_(alpha<=i) c_alpha product_j
          [binom(i_j,alpha_j)/binom(n_j,alpha_j)].

The supplied checker constructs (4) with rational polynomial arithmetic,
uses this conversion and exact de Casteljau bisection to verify every
coefficient. The two final certificates have 4 and 7 leaves. At the
specified degrees this checks 288 and 735 leaf coefficients respectively,
1023 coefficient inequalities in total. The retained JSON records the
whole subdivision paths and exact minima. The looser e=1/10 certificate
is also retained as an additional positive control, not as a stronger
result.

Thus (3) holds throughout every admissible continuous state, proving

    E[C_policy(I)] <= (35/32) C_T*(I)

on every positive archive I. This is a computer-assisted polynomial
positivity step inside an otherwise analytic policy proof. Its current
verification status must not be described as formal verification in a
proof assistant or independent external peer review.

## 6. Setup, alphabet restrictions and limits

If the row-cost guarantee is E[C]<=R C*, then adding a common compulsory
F>=0 gives F+E[C]<=R(F+C*) because R>=1. No new setup-dependent exact
constant is asserted.

On an independent domain containing both complete-vector endpoints, the
TRUE corner predicate is the same for every shared archive. The triangle
necessity inequalities and policies above therefore apply unchanged to
endpoint-containing subsets of the triangle. Omitting endpoints is a
different information model and is not covered by this transfer.

These are universal upper bounds, not solved global optima. Combined with
P22's persistent lower construction (or its P23 three-symbol refinement),
they leave genuine asymptotic gaps. They add no physical measurement or
radio-network claim. Screening, reading complete candidate rows and exact
predicate evaluation are operations in the stated observation contract.
