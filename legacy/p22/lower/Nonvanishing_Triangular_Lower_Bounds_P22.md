# Nonvanishing acquisition overhead on triangular archives

Working analytic result, 23 October 2026. This note extends the P21 triangular
construction, preserves the existing contract and does not assert historical
priority, external peer review or formal verification. The search lower bound
used below is the standard indistinguishability argument for two terminal
chains. The contribution claimed relative to P21 is its explicit realisation
by legal triangular rows with exact robust-certificate orthants and a fixed
five-symbol alphabet, giving a nonvanishing asymptotic lower bound.

## 1. Contract

There are three ordered groups: candidate A and labelled rivals L,R, each of
length N. A whole row lies in T={(c,f):0<=f<=c<=1}. Every unread row is freely
and independently completable in T. Queries reveal the next row of one group.
GOOD means Pareto nondomination and absence of support by every nonzero
nonnegative linear scalarisation; ties and axes count as support. An algorithm
is zero-error and terminates on every legal archive. Ratios are scored on
positive inputs against the cheapest realised TRUE prefix certificate.

For each group, its lower corner is the prefix sum divided by N and its upper
corner adds (N-length)/N to both coordinates. The exact P21 corner criterion
applies: no rival lower corner may dominate the candidate upper corner, and
the candidate lower corner must be unsupported against rival upper corners.

## 2. Explicit five-symbol family

Let x>=y>=1 be integers, q>=1 and

    D=x^2+2xy+2y^2,   N0=Dq,
    P=(x+y)^2/D,      Q=y(x+y)/D,
    h=1/N0,
    ell_L=2y(x+y)q=N0-x^2 q,
    ell_R=(x+y)^2 q=N0-y^2 q.

The candidate consists of N0 copies of p=(P,Q). Rival L starts with ell_L
copies of (1/2,1/2), and rival R starts with ell_R copies of (1,0). Fill each
remaining position with (1,1), except that one final row is (0,0):

* World L: L's final row is zero; R's final row is one.
* World R: R's final row is zero; L's final row is one.

All rows are legal in T. The public alphabet can be declared to be exactly
{(0,0),(1,1),(1/2,1/2),(1,0),p}; the endpoint corner test remains exact under
this independent alphabet restriction. Its entries are fixed as q changes.

Put b_L=ell_L+1, b_R=ell_R+1 and m_L=x^2q-1, m_R=y^2q-1. Thus b_L+m_L=N0
and b_R+m_R=N0. Assume m_R>0 for a nontrivial two-chain result; x>=y then
also gives m_L>0.

**Theorem 1 (exact certificate sets).** The complete sets of TRUE prefixes
are respectively

    World L: (N0,N0,j),  b_R<=j<=N0;
    World R: (N0,i,N0),  b_L<=i<=N0.

In particular, every positive certificate censuses the candidate and the
winning rival, while the other rival needs only its base prefix.

### Proof

After their initial blocks, but before a final zero, rival upper corners stay
constant because each observed one exactly replaces a missing-row upper
endpoint. These common corners are

    u=((x^2+xy+y^2)/D,(x^2+xy+y^2)/D),
    v=(1,y^2/D).

Relative to p they are

    u-p=(-a,c),  v-p=(d,-a),
    a=xy/D, c=x^2/D, d=y^2/D,  a^2=cd.

Hence p lies on the segment uv and is supported. Revealing a final zero
changes exactly one corner by -h(1,1).

First prove candidate census is compulsory. By monotonicity it suffices to
show that the candidate lower corner p'=p-hp at prefix N0-1 is supported
even after both rivals are fully known. For World L the oriented determinant
(candidate above the rival segment would require a positive value) is

    E_L=h(x+y)/D^2 [y^3-x^2y-x^3+x/q].

Since x>=y>=1 and q>=1, y^3-x^2y<=0 and -x^3+x/q<=0. Thus E_L<=0. For
World R the same determinant is

    E_R=-h y^3(x+y)/D^2-h^2 x(x+y)/D <0.

The rival segment has strictly negative slope in both worlds: its cost and
failure differences remain positive because y(x+y)>1 and x(x+y)>1, whereas
h<=1/D. Consequently its normal can be chosen strictly positive, and the
nonpositive determinants say that p' has scalarised value no greater than
either rival at that normal. It is supported. Monotonicity excludes every
prefix with fewer candidate rows.

With the candidate censused, any L prefix i<=ell_L has lower corner
(i/(2N0),i/(2N0)), whose failure is at most Q and whose cost is strictly below
P. It dominates p. Any R prefix j<=ell_R has lower corner (j/N0,0), whose
cost is at most P and failure is below Q. It too dominates p. Therefore b_L
and b_R are compulsory. After the first one, L's lower failure exceeds Q
and R's lower cost exceeds P, so P2 is safe; subsequent observations cannot
destroy safety. A final zero leaves the preceding lower sum unchanged and
is also safe because m_R>0 ensures there was at least one preceding one.

If neither final zero has been revealed, the upper corners are still u,v,
so p is supported. Thus the winning rival must be censused. After its zero,
the unsupportedness determinant at p is h(a+d)>0 in World L and h(a+c)>0
in World R. The relevant crossing differences remain strictly positive:
c-h>0 or d-h>0 follows from x^2q>1 or y^2q>1. Hence p is unsupported while
P2 is safe. This establishes every stated TRUE prefix and excludes all
others. QED.

## 3. Exact search cost on the two fixed archives

Permit arbitrary fixed strictly positive row prices and a finite common
compulsory information-free setup F>=0. Define W to be F plus all candidate
prices and both base-prefix prices, X to be the total price of L positions
b_L+1,...,N0 and Y the corresponding R-tail price. Then X,Y>0.

**Theorem 2.** The optimum worst-case ratio restricted to these two positive
archives, among algorithms valid on the complete triangular input class, is

    1+XY/[X(W+X)+Y(W+Y)]                   (randomised),
    1+min(X,Y)/(W+max(X,Y))                (deterministic).

These values are lower bounds for the global complete-domain optima.

Proof. The two archives are identical until a rival's final row is queried.
Let theta be the probability that L's final row is reached first. The law of
this event is common to both fixed archives, even with interleaving, random
stopping rules or queries that precede the compulsory base acquisitions.
Theorem 1 gives comparator costs W+X in World L and W+Y in World R. Reaching
the wrong final row entails paying its entire tail as well as the whole
winning certificate. Therefore the expected costs are at least

    W+X+(1-theta)Y,    W+Y+theta X.

Equalising the two excess ratios gives

    theta=Y(W+Y)/[X(W+X)+Y(W+Y)]

and the stated randomised lower bound. For deterministic algorithms theta
is zero or one, giving the stated deterministic value. Both bounds are
attained on this pair by taking the compulsory base, choosing one complete
tail in the stated distribution (or the cheaper tail deterministically),
testing TRUE and then taking the other tail if necessary. This is part of
a valid complete-domain algorithm: on other observations, take full census
and decide exactly. Thus the restricted-pair optima are exact, without a
promise-only correctness assumption. QED.

The proof does not regard block repetition as a hidden value: all intermediate
tail observations are exactly the same one in both worlds. Only the final
row distinguishes the worlds, so the wasted price can be the whole tail.

At unit prices and F=0, W=3N0-m_L-m_R, so

    R_rand,T(3,N0) >= 1 + m_L m_R /
       [3N0(m_L+m_R)-2m_L m_R],
    R_det,T(3,N0) >= 1 + min(m_L,m_R) /
       [3N0-min(m_L,m_R)].

These are lower bounds, not claimed to be the global exact ratios.

## 4. All lengths and nonvanishing limits

For any N>=Dq, prepend N-Dq zero rows to each group. Clip a prefix shorter
than this padding to its end. Beyond the padding, every corner is Dq/N times
the corresponding unpadded corner; positive scaling preserves all criteria.
Monotonicity and Theorem 1 exclude earlier certificates. Thus the exact
TRUE sets are translated by the padding length. The candidate still requires
N rows, the hidden tails still have lengths m_L,m_R, and the unit-price
formulae above hold with N in place of N0. Arbitrary-price Theorem 2 also
continues to hold after including padding prices in W.

For x=y=1 choose q=floor(N/5), N>=10. Then m=q-1 and

    R_rand,T(3,N) >= 1 + (floor(N/5)-1) /
                         [2(3N-floor(N/5)+1)],
    R_det,T(3,N) >= 1 + (floor(N/5)-1) /
                         [3N-floor(N/5)+1].

Consequently

    liminf_(N->infinity) R_rand,T(3,N) >= 29/28,
    liminf_(N->infinity) R_det,T(3,N) >= 15/14.

These nonvanishing bounds strengthen the P21 padded lower bounds, whose
excess tends to zero. At finite N take the maximum of all established bounds;
the new family need not dominate previously established small-N results.

More generally, fixing x,y and taking q=floor(N/D) gives

    liminf R_rand,T(3,N) >=
       1+x^2y^2/[3D(x^2+y^2)-2x^2y^2].

For x=9,y=8 this is 1+1728/47729, approximately 1.03620545. This uses one
fixed five-symbol alphabet with rational coordinates independent of N.

The best asymptotic bound within THIS two-chain parameter family is obtained
by maximising, for k=x/y>=1,

    B(k)=k^2/[3(k^2+2k+2)(k^2+1)-2k^2].

Writing H(k)=k^2/[(k^2+1)(k^2+2k+2)] makes B=H/(3-2H). The derivative of H
has the sign of -(k^4+k^3-k-2). This polynomial is strictly increasing for
k>=1 (derivative 4k^3+3k^2-1>0), negative at 1 and positive at 2. Therefore
there is a unique maximiser k_star in (1,2). Density of rational x/y, followed
by the all-N padding limit for each fixed rational pair, proves

    liminf R_rand,T(3,N) >= 1+B(k_star).

This final constant is a supremum over finite rational alphabets; no one
rational alphabet is asserted to attain the irrational optimum. This is an
optimisation of the displayed lower-bound family only, not an upper bound,
global optimality theorem or universal classification of hard instances.

For deterministic acquisition within the x>=y family the asymptotic excess
is y^2/(3D-y^2)=1/[3k^2+6k+5], maximised at k=1. Hence the symmetric 15/14
bound is the strongest deterministic asymptotic bound in this family.

## 5. Scope and verification

The accompanying own-code, standard-library checker independently implements
exact rational corner testing using integer arithmetic. It enumerates every
prefix state for small explicit archives, checks the complete candidate-full
slices plus the monotone candidate-census obstruction for larger archives,
and checks representative arbitrary-price formulae. Finite checks support
the construction and arithmetic; the all-N and all-price assertions rest on
the proofs above. No real radio measurements, external code, installation,
external review or formal theorem-prover execution is claimed.
