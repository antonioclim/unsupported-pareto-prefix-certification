# P56: a strict improvement for unrestricted triangle acquisition

## Status and scope

A new policy and a complete rational polynomial proof certificate are given below. The primary exact producer passes all eight continuous-domain certificate families. An independent rational collocation implementation has reproduced all 6,639 coefficients on 59 leaves, checked 891 unisolvent identity points, and rejected four mutations. A separate agent has independently checked the causal policy, its cost reduction and its geometric case partition, with 11,754 rational arithmetic controls; see `triangle_lower.md`, Section 2. This note does not claim to settle the unrestricted optimum, and it does not modify the canonical manuscript, the published companion, or any public release.

**Theorem.** For three configurations, every integer archive length N>=1, independent row completions in the triangle T={(c,f):0<=f<=c<=1}, and unit prices, there is an all-input valid zero-error randomized policy with positive-instance competitive ratio at most

\[
87/80=1.0875 < 12/11.
\]

A common compulsory information-free setup charge preserves this bound. The endpoint transfer theorem extends the guarantee pointwise to independent endpoint-containing subdomains. The theorem does not cover arbitrary unequal tariffs. The candidate-census restricted asymptotic optimum remains 12/11; the new policy is outside that restricted class. This also gives the same upper and policy-class separation on the fixed three-symbol alphabet S={(0,0),(1,0),(1,1)}, by the existing endpoint certificate transfer.

## Policy

Before making observations, draw a branch coin with probability lambda=1/12.

* In branch Q, completely observe both rivals, then observe the candidate until the exact robust TRUE test succeeds or the candidate is complete. At full census return the exact GOOD verdict.
* With probability 11/12, run the candidate-first policy from main Section 6.1: census the candidate, observe its mean gap G, and screen the rivals to the first domination-safe lower corners. On a positive archive the two crossing orientations are then known. Choose the southeast-first continuation with probability p(G)=12 alpha(G)/11, where

\[
\alpha(G)=\begin{cases}
\dfrac{(19/3)G-2G^2}{4+G},&0\le G\le3/4,\\[4pt]
\dfrac{87}{80}-\dfrac{21}{80G},&3/4<G\le1.
\end{cases}
\]

Negative, degenerate, or noncrossing observations retain exact census fallback. In particular, the rival-first branch does not assume a positive-answer promise.

The branch coin is independent of all observations. The value G is used only within the candidate-first branch after candidate census; the rival-first branch never needs an unobserved G.

The low alpha branch is increasing because its derivative has numerator 76/3-16G-2G^2, which is at least 293/24>0 on [0,3/4]. Its range is [0,29/38]. The high branch is increasing with range (59/80,33/40]. Thus 0<=p(G)<=9/10<1. There is a downward jump at 3/4; both one-sided branch endpoints are verified separately in the proof.

## Exact cost reduction

Fix any realised robust TRUE certificate with oriented counts (a,i,j), where i is northwest and j southeast. Define unread fractions t=1-a/N, s=1-i/N, r=1-j/N and C=3-t-s-r. Retain g as the observed candidate lower-corner gap at prefix a, and U=s+t, V=r+t.

The existing screening argument gives candidate-first continuation costs at most 2N+j and 2N+i. Rival-first cost is at most 2N+a: by upward closure of TRUE, the state (a,N,N) is TRUE whenever (a,i,j) is TRUE.

Therefore the mixture's expected excess over NC is at most

\[
N[(1-\lambda)t+(1-\alpha(G))s+(\lambda+\alpha(G))r]
=N[(1-\alpha(G))U+(\lambda+\alpha(G))V-2\lambda t].
\]

Set e=7/80. It suffices to prove

\[
(1+e-\alpha(G))U+(\lambda+e+\alpha(G))V
\le3e+(2\lambda+e)t. \tag{P56-1}
\]

The coefficient of U is positive throughout both branches. The geometry from main (C9)-(C11e) gives

\[
0<g<1,\quad0\le t<g(1-g),\quad g\le G\le g+t,
\]
\[
U\le \frac{g(k-2V)}{k-V},\quad k=1+t-g,
\quad t\le V\le t+\frac{g(1-g)-t}{2g-t}.
\]

Closed inequalities safely enlarge the strictly feasible states. Thus U may be replaced by its displayed upper bound. For fixed g,t,V,U, the left side of (P56-1) is affine in alpha(G). Since each alpha branch is monotone, its extremum over any interval within that branch occurs at a G endpoint. A linear numerator in G is not needed for this reduction.

## Eight polynomial families and their domains

Use the full parameterisation

\[
t=g(1-g)z,\quad H=2-(1-g)z,\quad J=w(1-z),\quad E=H-J,
\]
\[
V_n=gzH+J,\qquad U_n=(1-gz)H-2J,
\qquad V=(1-g)V_n/H,\quad U_{max}=gU_n/E,
\]

with z,w in [0,1]. The legal denominators H and E are positive.

Write alpha(G)=n(G)/d(G), with d=4+G and n=(19/3)G-2G^2 in the low branch, and d=G, n=(1+e)G-3e in the high branch. Define

\[
D=[3e+(2\lambda+e)t]d,\quad A=(1+e)d-n,\quad B=(\lambda+e)d+n.
\]

The full polynomial is

\[
F(G,g,z,w)=DHE-AgHU_n-B(1-g)V_nE.
\]

For a cut parameterisation of t, define

\[
D_0=2g-t,\quad\delta=g(1-g)-t,\quad
E_0=(1-g)D_0-w\delta,
\]
\[
U_0=(1-g-t)D_0-2w\delta,\qquad V_0=tD_0+w\delta.
\]

The cut polynomial is

\[
F_{cut}(G,g,t,w)=DD_0E_0-AgD_0U_0-BV_0E_0.
\]

All denominators cleared here are positive at legal states. Put h=3/4,
T2=(h-g)z and T3=h-g+[g(1-g)-(h-g)]z. The exact rational producer certifies:

| Family | Branch and endpoint | g interval | t representation | Degree (g,z,w) | Leaves |
|---|---|---|---|---|---|
| L0 | low, G=g | [0,3/4] | full | (5,3,2) | 19 |
| L1 | low, G=g+t | [0,1/2] | full | (7,5,2) | 19 |
| L2 | low, G=g+t | [1/2,3/4] | T2 | (6,5,2) | 16 |
| L3 | low, G=h | [1/2,3/4] | T3 | (7,3,2) | 1 |
| H0 | high, G=g | [3/4,1] | full | (5,3,2) | 1 |
| H1 | high, G=g+t | [3/4,1] | full | (6,4,2) | 1 |
| H2 | high, G=g+t | [1/2,3/4] | T3 | (9,4,2) | 1 |
| H3 | high, G=h | [1/2,3/4] | T3 | (7,3,2) | 1 |

Coverage: if g<=1/2 then g+t<=2g-g^2<=3/4. If g>=1/2, the endpoint g+t is below h precisely when t<=h-g, and above h precisely when t>=h-g. T2 and T3 respectively cover those portions. Low endpoints are g and min(g+t,h); high endpoints are max(g,h) and g+t. This yields exactly the eight listed families. Both branch definitions at the cut are certified, despite the downward jump in alpha.

Every family has nonnegative tensor Bernstein coefficients after the listed exact dyadic subdivisions. The coefficient file specifies each root box, degree, leaf path, exact leaf minimum and polynomial power coefficients. Each path bisects axes cyclically g,z,w. Leaf prefix-freeness and unit total dyadic volume give a complete cover; these partition properties were also checked independently. Nonnegative Bernstein coefficients prove nonnegativity on each entire box, not merely at finite sampled states.

Together with the completed independent certificate verification, this proves (P56-1). Choose a cheapest realised certificate only in the analysis, never as information supplied to the policy. Expected cost is then at most (1+e)C*=87C*/80. Common setup F preserves the guarantee by F+RC*<=R(F+C*) for R>=1.

## Quantitative consequence and remaining limit

The existing lower limit 23/22 remains unchanged. The new proven upper gives

\[
23/22\le\liminf_{N\to\infty}R^*_{\mathrm{rand},\mathcal T}(3,N)\le\limsup_{N\to\infty}R^*_{\mathrm{rand},\mathcal T}(3,N)\le87/80.
\]

Thus every accumulation point lies in [23/22,87/80]. Existence of the unrestricted asymptotic limit is not asserted.

Its width is 37/880, compared with the previous 1/22=40/880: a 7.5% reduction in interval width. This is a strict mathematical advance, not a solution of the remaining minimax problem and not a demonstrated economic saving.

On the former candidate-census hard family, the new mixture's asymptotic cost ratio is at most 13/12 (strictly below 87/80), because branch Q leaves approximately N/4 candidate rows unread. The global upper is not obtained by changing the public completion model or assuming the hard family.

## Strict policy-class separation

The result establishes a qualitative distinction that the previous bounds did not establish: unrestricted policies strictly outperform policies requiring full candidate observation in the asymptotic regime. Indeed, the latter optimum tends to 12/11, whereas the new unrestricted limsup is at most 87/80, leaving a gap of at least 3/880.

There is also a finite separation. For N=4q, the existing restricted lower bound is (12q-1)/(11q+1). This is strictly greater than 87/80 exactly when 3q>167. Therefore every q>=56, starting at N=224, exhibits a strict separation between the two policy classes. For general N=4q+r with r in {0,1,2,3}, the sufficient inequality is 3q>167+21r; it holds for every N>=308. These are sufficient separation thresholds from the existing lower bound and the new upper, not claimed minimal thresholds for the true optima.

## Reproducible files

* `p56_work/scripts/upper_87_80_certificate.py`: exact primary producer; standard-library-only.
* `p56_work/scripts/upper_polynomial.py`: sparse rational symbolic arithmetic, adapted from the prior P55 independent arithmetic implementation.
* `p56_work/evidence/upper_87_80_certificate.json`: all eight families, coefficients and dyadic leaf certificates.
* `p56_work/evidence/upper_87_80_producer.log`: producer transcript.
* `p56_work/scripts/root_verify_87_80.py` and `p56_work/evidence/Root_87_80_Independent_P56.json`: independent rational collocation verification (parent agent).
* `p56_work/scripts/upper_87_80_operational.py`: exact operational branch checks, including actual partial-candidate stopping on the fixed hard worlds; output in `p56_work/evidence/upper_87_80_operational.json`.

The operational check passed 1,816 ordinary synthetic cases (141 positive, 1,675 negative) and 224 hard-world cases, executing 6,120 branches in exact arithmetic. It enumerated 68,309 ordinary comparator states and 8,788 hard-world prefix states; the remaining hard-world comparators use the existing complete TRUE-prefix characterisation of Theorem 16. All 112 world-U rival-first branches actually stopped with the candidate partly unread. These are finite implementation checks, separate from the continuous polynomial proof.

The earlier nonlinear searches and sampled LP in adjacent files are discovery evidence only. They are not used by the exact producer or by the stated proof.
