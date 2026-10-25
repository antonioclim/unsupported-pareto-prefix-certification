# Exact certificates and acquisition phase boundaries in diagonal bands

P22 working mathematical note, 23 October 2026. This note establishes results under the declared exact-information model; it makes no historical-priority, measurement or external-peer-review claim. P21 files remain unchanged.

## Model

For a public parameter 0<d<=1, every whole row belongs to

    T_d = {(c,f): 0<=f<=c<=1, c-f<=d}.

Rows are independently completable and revealed in their fixed group-prefix order. There are K>=3 configurations, N rows each, including a designated candidate. TRUE means that every legal completion makes the candidate Pareto nondominated and unsupported by every nonzero nonnegative linear scalarisation. Axes and ties count as support. Algorithms must terminate and be correct on every input; competitive costs are scored only on positive inputs against their minimum realised TRUE-prefix certificate. Prices, when used, are fixed public strictly positive row prices independent of hidden values. A finite common compulsory uninformative setup F>=0 may be included in both costs.

Both whole endpoints (0,0),(1,1) belong to T_d. Therefore the P21 endpoint theorem applies: TRUE iff no rival lower corner dominates the candidate upper corner, and the candidate lower corner is unsupported against all rival upper corners. This does not assume that all points in a rectangular envelope belong to T_d.

At d=0 all means lie on the diagonal. Every nondominated candidate is supported, so there are no positive inputs. All nonvacuous claims below explicitly assume d>0.

## Theorem S1: exact oriented prefix feasibility

For K=3 let a,i,j be candidate, northwest-witness and southeast-witness observed lengths, respectively, in {1,...,N}. Put

    t=1-a/N, s=1-i/N, r=1-j/N,
    U=s+t, V=r+t, b=d(1-r), M=b-U-V.

A legal robust TRUE prefix with these oriented lengths exists iff

    M>0 and M^2>4UV.                                      (S1)

Equivalently, b>(sqrt(U)+sqrt(V))^2. At d=1, this is exactly P21's triangular criterion.

Proof of necessity. Write candidate lower p=(x,y), g=x-y, and crossing upper witnesses

    u=(x-A,y+C), v=(x+D,y-E),

where A,C,D,E>0 and AE>CD. Such a pair is necessary for nondomination together with unsupportedness in two objectives. P2 safety forces C>U and D>V. The northwest upper gap is nonnegative, giving A+C<=g. The southeast upper gap is at most d(1-r)=b, giving D+E<=b-g. Thus

    (g-U)(b-g-V) > UV,

with both factors positive. Their fixed sum is M, and their product is at most M^2/4. This proves (S1).

Proof of sufficiency, with explicit rational observations. Set

    z=M/2, Delta=z^2-UV>0, epsilon=Delta/(2b),
    x=b-t-epsilon, y=r+z-epsilon,
    h=(b+s+r)/2.

Use candidate lower p=(x,y), northwest upper u=(h,h), southeast upper v=(b+r,r). They are attained by constant observed rows

    candidate: (x/(1-t), y/(1-t)),
    northwest: ((b-s+r)/(2(1-s)), (b-s+r)/(2(1-s))),
    southeast: (d,0).

Since b>U+V, 0<z<=b/2 and 0<epsilon<=z/4. Hence y>0. The candidate gap is

    g=(b+s-r)/2=b-r-t-z>0,

and g<b-r-t<=d(1-t), while x<=b-t<=1-t. Thus its observed row is in T_d. The northwest observed diagonal lies in [0,1], since b>s+r+2t implies its numerator is positive and b<=1-r implies b+s+r<=2. The southeast row is legal by definition.

The crossing differences are A=E=z-epsilon, C=U+epsilon and D=V+epsilon. Consequently

    AE-CD=Delta-b*epsilon=Delta/2>0.

The northwest lower failure exceeds candidate upper failure by epsilon, and the southeast lower cost exceeds candidate upper cost by epsilon. Both P2 comparisons are therefore safe. This proves TRUE and completes the construction. Unread actual rows may all be zero.

For rational d=P/Q>0 in lowest terms, write

    H=Pj-Q(4N-2a-i-j),
    D=H^2-4Q^2(2N-a-i)(2N-a-j).

Then epsilon=D/(8PQNj), and the two candidate observed coordinates share denominator 8PQaj<=8PQN^2. Northwest observed coordinates have denominator 2Qi; southeast coordinates have denominator Q. The construction has O(log N+log P+log Q)-bit coordinates. This finite-precision statement concerns this band feasibility construction only, not the general Ramsey lower bound.

## Corollary S1.1: sharp candidate observation law

Every TRUE certificate, for any K>=3, has

    a>N(1-d/4).                                         (S2)

Indeed (S1) implies d>=b>(sqrt(s+t)+sqrt(r+t))^2>=4t. For K>3 a strict crossing pair still exists. Conversely set i=j=N, so (S1) reduces to d>4t. The explicit construction attains every such candidate length, with any additional rivals fully observed at (1,1). Thus the least possible candidate length is floor(N(1-d/4))+1.

## Corollary S1.2: exact minimum unit-price certificate size

For all K>=3,N>=1 and 0<d<=1, the minimum certificate cost over all legal positive archives is

    D_band(K,N,d)=K+floor((3-d)N)-2.                    (S3)

Proof. Every group has at least one observation. A strict witness pair has t+s+r<d, because (S1) gives

    d(1-r)>s+r+2t+2sqrt((s+t)(r+t)).

Therefore a+i+j>(3-d)N and every certificate pays at least floor((3-d)N)+1 for those three groups, plus K-3 observations for the others.

For attainment, set a=j=N and i=floor(N(1-d))+1. Then s<d, so S1 constructs a TRUE prefix at precisely the claimed three-group cost. In this construction candidate lower failure is y=(d-s)/2-epsilon<1/(2N), because i<=N(1-d)+1. For every other rival, use first row (1,1) and any legal remaining rows, and observe only that first row. Its lower failure 1/N is above candidate failure, so P2 is safe; its upper (1,1) cannot invalidate the already strict witness pair. This attains (S3).

## Theorem S2: exact zero-overhead boundary

For K=3, under every fixed positive row-price schedule and finite common setup, a complete algorithm of positive-certificate ratio one exists iff

    d(N-1)<=2.                                        (S4)

Upper proof. Under (S4), Nd<=2+d<=3, so (S2) forces candidate census. Reveal it and write g=p_c-p_f. A partial northwest witness with unread fraction s>=1/N requires g>s, hence g>1/N. A partial southeast witness with unread fraction r>=1/N requires

    g<d(1-r)-r<=d-(d+1)/N.                            (S5)

The last bound is <=1/N by (S4). If g<=1/N, every positive certificate must census the northwest witness. If g>1/N, every positive certificate must census the southeast witness.

Screen each rival only to its first P2-safe prefix against the censused candidate. On a positive archive these are compulsory prefixes and their crossing orientations are identifiable. Complete the compulsory side just identified, then extend the remaining side until TRUE. Every positive certificate contains the same candidate census, compulsory-side census and safe prefixes; with these fixed, TRUE is monotone in the remaining prefix. The policy reaches the componentwise minimum TRUE certificate and is optimal for all fixed positive prices. Handle every negative or degenerate branch by exact census, which makes the policy complete. The N=1 case simply reads all three rows.

The strict lower when d(N-1)>2 is proved below by two fixed archives, rather than by an adaptive adversary.

## Lemma S3: opposite-final-row worlds throughout the supercritical regime

Assume d(N-1)>2. Necessarily N>=4. Put

    q=1/N, C=d(1-q)>2q,
    epsilon=min((C-2q)/16, q^2/16),
    p0=(3C/4+q/2, C/4+q/2), p=p0+epsilon(1,1).

Every candidate row is p. Each rival's first N-1 rows are

    northwest: (d/2,d/2), southeast: (d,0).

In world A the last northwest row is (0,0) and the last southeast row is (1,1); in world B these last rows are swapped. All rows are in T_d: p_c<C<1, p_f>0 and p_c-p_f=C/2<=d.

Write L=(C/2,C/2), R=(C,0). The full means in A are L,R+q(1,1), while those in B are L+q(1,1),R. The point p0 is the midpoint of either pair. Hence p exceeds that midpoint strictly in both coordinates. P2 safety holds because

    C-p_c=C/2-p_f=(C-2q)/4-epsilon>0.

Thus A is TRUE at (N,N,N-1), and B at (N,N-1,N).

We now prove that these and full census are the ONLY TRUE prefix states.

1. Candidate census is necessary. With one candidate row unread, its lower corner is (1-q)p<p0 coordinatewise, since p0_f>q and epsilon(1-q)<q^2. At full rival census p0 lies on the segment between the two crossing rivals. A positive normal to this segment supports the lower candidate or ranks it ahead of both rivals. Therefore it is not unsupported. Monotonicity excludes every shorter candidate prefix.

2. The rival with final row (0,0) must be censused. Otherwise, even with the other rival complete, the upper witnesses are L+q(1,1),R+q(1,1), both lying on c+f=C+2q. The candidate has sum C+q+2epsilon<C+2q, so the equal-weight scalarisation supports it. Earlier prefixes cannot certify TRUE.

3. The other rival needs at least N-1 rows. In A, if the southeast prefix has only N-2 rows, its upper corner is (C+q+q(1-d),2q). Pair it with complete L. If there is no strict crossing, P2 and unsupportedness cannot both hold. If there is a crossing, write A0=C/4+q/2, B0=C/4-q/2>0. Its strict-pair determinant is

       -q[A0+B0(1-d)]+epsilon(C-qd)<0.

   Indeed the bracket is at least C/4, while 0<C-qd<C and epsilon<q/16. In B, the northwest N-2 upper corner is L+q(1,1)+k(1,1), where k=q(1-d/2)>=q/2. With complete R, the corresponding determinant is

       C(epsilon-k/2)<0.

   Again a missing crossing cannot restore TRUE. These maximal failed states and prefix monotonicity exclude all earlier prefixes.

Thus the exact TRUE lists are A:{(N,N,N-1),(N,N,N)} and B:{(N,N-1,N),(N,N,N)}.

Let W be F plus all candidate prices and the first N-1 prices of each labelled rival, and let x,y be the two final-row prices. The archives agree up to the first final-row disclosure. If the x-tail is queried first with probability theta, expected costs are at least W+x+(1-theta)y in A and W+y+theta*x in B. Their comparator costs are W+x and W+y. Balancing gives the universal lower bounds

    R_rand >= 1+xy/[x(W+x)+y(W+y)],
    R_det  >= 1+min(x,y)/(W+max(x,y)).                 (S6)

These are strictly greater than one, completing the converse of S2. Inputs are fixed before private randomisation. Even an algorithm that interleaves base rows and final-row revelation must eventually pay the compulsory base; the indistinguishability argument does not assume a canonical acquisition order.

## Theorem S4: exact priced acquisition on the first supercritical band

For K=3 and

    2<d(N-1)<=3,                                      (S7)

the two inequalities (S6) are equalities. At unit prices and F=0,

    R_rand=1+1/[2(3N-1)], R_det=3N/(3N-1).            (S8)

Upper proof. Since Nd<=3+d<=4, (S2) again forces candidate census. Let q=1/N and B=d-(d+1)q. Branch on the observed candidate gap g BEFORE rival screening.

For g<=q, northwest census is compulsory. For g>=B, southeast census is compulsory. The mandatory-side policy from S2 is optimal in these exterior branches.

For q<g<B, every positive certificate contains the first N-1 rows of both rivals. A northwest prefix of at most N-2 would require g>2q, but B=(d(N-1)-1)q<=2q. A southeast prefix of at most N-2 would require g<d-2(d+1)q=B-(d+1)q<q. Both are contradictions. Therefore acquire exactly the compulsory base of cost W. It is not TRUE: at t=0,s=r=q, S1 would require d(N-1)>4, contrary to (S7).

Choose the x-tail first with probability y(W+y)/[x(W+x)+y(W+y)], then test TRUE, taking the other tail if necessary. Every positive certificate needs at least one tail; the balancing calculation proves the randomised upper in (S6). Taking the cheaper tail first proves the deterministic upper. If both single tails suffice or both are necessary, the same bound follows directly. Negative cases terminate at census. The middle branch acquires the base directly and must not accidentally spend a final row during an orientation screen.

Together with Lemma S3 this proves exactness. At d=1, (S4) and (S7) recover P21's N<=3 zero-overhead regime and its N=4 priced optimum. For every N>=4, suitable narrower bands d in (2/(N-1), min(3/(N-1),1)] exhibit the same exact two-tail game, so the theorem is not limited to a fixed archive length.

## Scope and remaining questions

These results treat a whole family of exact public row domains and give an analytic domain-width phase diagram. They do not assert that a physical dataset satisfies any particular d or that inferring d from observed rows is a valid completion restriction. The first-supercritical-tranche equality does not solve general triangular N>=5 (d=1 gives d(N-1)>=4). It also does not establish historical novelty. The set consisting of the two endpoints, p, (d/2,d/2) and (d,0) has at most five distinct whole rows; with both endpoints retained, the same lower inputs and upper policies apply to that declared finite alphabet. No minimum-alphabet claim is made.
