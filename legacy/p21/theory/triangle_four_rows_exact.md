# Exact triangular acquisition: the four-row threshold and arbitrary prices

Working analytic result, 23 October 2026. Authoritative baseline: P20 manuscript v9. This note does not assert historical priority or external peer review. It changes no P20 file.

## Contract and notation

There are three configurations, candidate A and two labelled rivals L,R, each containing N ordered whole rows in T={(c,f):0<=f<=c<=1}. Missing rows are independently completable. Queries reveal the next whole row. GOOD means Pareto nondomination AND unsupportedness by every nonzero nonnegative linear scalarisation, including axes and ties as support. Algorithms must be zero-error and terminate on every legal input; only positive inputs are scored. The denominator is the cheapest realised TRUE prefix certificate. Row prices are fixed, positive, public and independent of hidden values. A nonnegative common compulsory information-free setup F may be added to both costs.

The endpoint argument in P20 Theorem 5 makes the square corner criterion exact on T: robust P2 means no rival lower corner dominates the candidate upper corner; robust unsupportedness means candidate lower corner is unsupported against the rival upper corners. The proof uses actual whole endpoints (0,0),(1,1), not a rectangle approximation to T.

## 1. Exact feasibility of a triangular three-group TRUE prefix

Let the candidate prefix have a rows, a northwest witness i rows, and a southeast witness j rows; 1<=a,i,j<=N. Put

    t=(N-a)/N, s=(N-i)/N, r=(N-j)/N,
    M=1-s-2r-2t.

There exists a legal robust TRUE prefix with these oriented lengths if and only if

    M>0 and M^2>4(s+t)(r+t).                         (T1)

Equivalently, with Z=i+2j+2a-4N,

    Z>0 and Z^2>4(2N-a-i)(2N-a-j).                 (T2)

The northwest/southeast orientation matters: the triangle is not invariant under swapping the two coordinates.

Necessity. Write candidate lower corner p=(x,y) and crossing rival upper corners

    u=(x-A,y+C), v=(x+D,y-E),

where A,C,D,E>0 and AE>CD. This strict crossing characterisation follows from nondomination and unsupportedness in two objectives. The northwest lower corner is u-s(1,1). Its first coordinate is below candidate upper x+t, so P2 safety forces C>s+t. The southeast lower corner similarly forces D>r+t. Membership in triangular mean envelopes gives A+C<=x-y, E<=y-r, and D<=1-x. Therefore x<1-r-t and

    (x-y-s-t)(y-r) > (s+t)(r+t).

Set z=y-r>0. Since x<1-r-t, the left side is strictly below z(M-z), whose maximum over real z is M^2/4. Its positivity implies M>0. This proves (T1).

Sufficiency and an explicit rational construction. Suppose (T1), and put z=M/2 and Delta=z^2-(s+t)(r+t)>0. Set

    epsilon=Delta/[2(1-r)]
           =[Z^2-4(2N-a-i)(2N-a-j)]/(8Nj).

Since 2z+s+r+2t=1-r,

    (z-epsilon)^2-(s+t+epsilon)(r+t+epsilon)=Delta/2>0.

Also z<=(1-r)/2 and Delta<=z^2 imply 0<epsilon<=z/4. Define

    x=1-r-t-epsilon,
    y=(1-s-2t)/2-epsilon,
    u=((1+s)/2,(1+s)/2),
    v=(1,r).

Here y-r=z-epsilon>0 and x-y=(1+s-2r)/2>0, while x<=1-t=a/N. Thus candidate lower p=(x,y) is attained by a identical rows (Nx/a,Ny/a) in T. The northwest lower corner is ((1-s)/2,(1-s)/2), attained by i copies of (1/2,1/2). The southeast lower corner is (1-r,0), attained by j copies of (1,0). Their upper corners are exactly u,v.

Their crossing differences are A=E=z-epsilon, C=s+t+epsilon and D=r+t+epsilon, so the displayed strict inequality proves unsupportedness. P2 safety holds because the northwest lower failure is y+t+epsilon and the southeast lower cost is x+t+epsilon. This proves sufficiency with rational observations.

For D=Z^2-4(2N-a-i)(2N-a-j), the two candidate row coordinates are [8j(a+j-N)-D]/(8aj) and [4j(2a+i-2N)-D]/(8aj). Their common denominator is at most 8N^2, while the rival rows are (1/2,1/2) and (1,0). Thus the construction uses O(log N)-bit rational coordinates. This constructive precision guarantee concerns this new triangular feasibility theorem only; it does not change the Ramsey lower construction's precision limitations.

Consequences. Taking i=j=N makes (T1) equivalent to a>3N/4. Every positive certificate therefore contains at least floor(3N/4)+1 candidate rows, and that bound is attainable for every N. For K>3 the lower bound remains valid because a strict crossing pair exists; attainability can be retained by adding fully observed harmless rivals.

For N=4, every positive certificate censuses the candidate. Prefix (a,i,j)=(4,3,3) is infeasible: M=1/4 whereas 2 sqrt((s+t)(r+t))=1/2. By monotonicity, both rivals cannot remain partial in any TRUE certificate.

## 2. Exact four-row theorem with arbitrary fixed positive row prices

For N=4 define W as F plus the prices of all four candidate rows and the first three rows of each rival. Let x>0 and y>0 be the prices of the fourth rows of the two labelled rivals. Then

    R_rand^* = 1 + xy / [x(W+x)+y(W+y)],             (T3)
    R_det^*  = 1 + min(x,y)/(W+max(x,y)).            (T4)

At unit row prices and F=0 these are 23/22 and 12/11. This is a global minimax statement on the complete triangular domain, not a promise that an archive belongs to a two-world family.

Upper bound. Census the candidate, obtaining p=(p_c,p_f), and let g=p_c-p_f. Branch on g before querying rival rows. In the two exterior branches specified below, screen both rivals to their first P2-safe prefixes. On every positive archive these prefixes are compulsory. Its two rivals must have opposite crossing orientations, which the safe lower corners identify. All negative and degenerate cases can be handled by exact full census, ensuring a complete algorithm.

If a northwest witness has i<4 observed rows, its upper failure exceeds p_f+(4-i)/4 by P2 safety, and its upper cost is at least its upper failure. Since that upper cost must be below p_c,

    g > 1-i/4.                                    (T5)

If a southeast witness has j<4 observed rows, its upper failure is at least (4-j)/4 and below p_f. Its P2-safe lower cost exceeds p_c but is at most j/4. Consequently

    g < 2j/4-1.                                   (T6)

For g<=1/4, (T5) forces northwest census in every positive certificate. For g>=1/2, (T6) forces southeast census. Complete that compulsory rival, then extend the sole remaining rival only until TRUE. The result is the componentwise least positive certificate, so its cost is optimal for every positive price schedule.

For 1/4<g<1/2, (T5) excludes northwest prefixes of length <=2, and (T6) excludes southeast prefixes of length <=2. Thus (4,3,3) is compulsory in every positive certificate. By Section 1 it cannot itself be TRUE. Acquire precisely this base; query the last row of the first labelled rival with probability

    q = y(W+y)/[x(W+x)+y(W+y)],

otherwise query the other last row. Test TRUE after the first final row and complete the other if needed. A certificate needs either only the x-tail, only the y-tail, or both. If only x suffices, expected cost is W+x+(1-q)y; if only y suffices it is W+y+qx. The two excess ratios coincide and equal xy/[x(W+x)+y(W+y)]. If both single tails suffice, the comparator takes the cheaper one; the corresponding bound still applies. If neither suffices the algorithm and comparator both pay W+x+y. This proves (T3). For deterministic acquisition, reveal the cheaper final row first, proving (T4).

The side-identification screen is used only in the exterior branches. In the middle branch it must not consume a fourth rival row before the randomised choice: the compulsory base is acquired directly. If no TRUE certificate follows the first chosen tail, take full census and decide. This keeps the policy complete on negative archives without biasing the final-row choice.

Lower bound. Candidate rows are all (13/20,31/100). Each rival's first three rows is fixed:

    NW: (7/15,7/15) each; SE: (14/15,0) each.

World A has last rows NW=(0,0), SE=(1,1). World B has NW=(1,1), SE=(0,0). These archives are legal in T. Candidate p=(13/20,31/100). After three rival rows the lower corners are (7/20,7/20) and (7/10,0), and their upper corners are (3/5,3/5) and (19/20,1/4).

World A has TRUE prefixes exactly (4,4,3),(4,4,4). At its minimum state, mixture weight 11/20 on the complete northwest witness yields (31/50,61/200), strictly below p by (3/100,1/200). World B has TRUE prefixes exactly (4,3,4),(4,4,4). Weight 61/120 on the northwest upper corner yields (779/1200,61/200), below p by (1/1200,1/200).

Candidate census is compulsory by Section 1. For both worlds, each rival's first two lower corners are strictly below p in both coordinates, so its first three rows are compulsory. Bothpartial (4,3,3) is impossible. In World A, completing SE retains its common upper corner, so (4,3,4) fails exactly as (4,3,3) does; analogously, in World B (4,4,3) fails. These arguments prove the complete TRUE-prefix lists without reliance on numerical enumeration.

The archives agree until the first rival tail. Let q be the probability the x-priced northwest tail is queried first. This choice has the same law in both fixed archives, even if the algorithm queries a tail before completing all compulsory base rows. Expected costs are at least W+x+(1-q)y in A and W+y+qx in B. The comparator costs are W+x and W+y. Minimising the larger ratio over q gives (T3); deterministic q in {0,1} gives (T4). Every input is fixed before private randomness. No assumption that actual observations arrive in the policy's canonical order is made.

## 3. Persistence for every larger archive length

For each N>=4 prepend N-4 zero rows to every group of each hard archive above. At prefixes past that padding, lower and upper corners are exactly 4/N times the corresponding four-row corners: observed sums are unchanged and the number of unread nonpadding rows is unchanged. GOOD and the robust corner tests are invariant under a common positive coordinate scale. Thus the two minimum TRUE states become (N,N,N-1) and (N,N-1,N).

A prefix not reaching the end of some zero padding cannot itself certify TRUE: extending it to the end of that padding reveals only zeros and cannot destroy a certificate, while the resulting four-row corner state at prefix zero is not TRUE. More generally, clipping each prefix length below N-4 to N-4 only extends information; after clipping, the exact scaling correspondence applies. Hence no additional TRUE states arise from the padding. The exact minimum certificate cost at unit prices is 3N-1 in both worlds, and the histories still agree until one rival's final row.

Consequently for K=3 and every N>=4,

    R_rand,T^*(3,N) >= 1+1/[2(3N-1)],
    R_det,T^*(3,N) >= 3N/(3N-1).                    (T7)

The same padded lower holds for arbitrary fixed positive row prices. Define W_N as F plus all N candidate-row prices and the first N-1 prices of each rival, and let x,y be their final-row prices. The two certificate costs are W_N+x and W_N+y, and the indistinguishable-tail argument gives

    R_rand,T^*(3,N) >= 1+xy/[x(W_N+x)+y(W_N+y)],
    R_det,T^*(3,N) >= 1+min(x,y)/(W_N+max(x,y)).    (T8)

Both inequalities are strict above one for every fixed positive price schedule and finite F. They need not be sharp when N>4.

For N=1 all three rows are compulsory. For N=2 the candidate is censused by a>3N/4. A partial southeast witness with j=1 would require g<2j/N-1=0, impossible in T. Its census is therefore compulsory in every positive certificate. Screening identifies the two sides using compulsory P2-safe prefixes; completing the southeast rival and then extending the northwest rival to its first TRUE prefix acquires the componentwise least certificate. The N=3 weighted optimum is the existing triangular theorem. Consequently, for EVERY fixed positive row-price schedule and common finite compulsory setup, zero-overhead acquisition on the complete independent triangular domain with three configurations occurs exactly when N<=3. General exact acquisition ratios for N>4 remain open.

## Verification status

Analytic arguments above prove universal statements under the declared contract. The independent exact-rational script accompanying this note enumerates all prefix states only for the explicit finite hard archives, checks complete TRUE-prefix lists, and verifies representative weighted minimax formulae. Such finite checks are arithmetic and implementation tests, not exhaustive checks of the continuous input class. An independent hostile rereading was requested. Historical novelty has not been established by this note.
