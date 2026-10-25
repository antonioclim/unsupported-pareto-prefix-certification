# P56 — lower-bound search and independent audit of the mixed upper bound

Date: 25 October 2026. This is an author-side research note, not external peer review.
The canonical P55 manuscript and the public software were not changed.

## 1. Outcome of the lower-bound search

No improved unrestricted asymptotic lower bound has been established here.
The proved lower bound remains **23/22**. A useful obstruction was derived for a
natural way of varying its construction: changing the relative lengths of the
two hidden terminal chains and leaving a common southeast suffix unread cannot
improve the limiting two-choice bound within the explicitly specified template
below. This is a restriction on that search template, not a theorem about every
possible hard pair or every finite hard family.

### The terminal-plateau template

Consider a limiting two-world construction with candidate tail length `tN`,
northwest tail length `sN`, and a common unread southeast fraction `r`. Candidate
tail records before the distinguishing terminal record are zeros. Northwest tail
records before its distinguishing terminal record are `(1,1)`. The terminal
perturbations have size `O(1/N)` in the complete means. The limiting candidate
lower corner is `p`, and the limiting northwest and southeast upper corners are

\[
u=(p_c-A,p_f+C),\qquad v=(p_c+D,p_f-E),
\]

where all four offsets are positive and the common supporting boundary is
`AE=CD`. World U has the certificate that completes the northwest chain and
leaves the candidate tail unread; world V completes the candidate chain and
leaves the northwest tail unread. Assume that their complete certificate sets
indeed reduce the pair to the two-choice game with common base
`W=(3-t-s-r)N` and residual chain prices `tN,sN`.

Robust nondomination on the two certificate types implies, in the limit,

\[
C\ge\max(t,s),\qquad D\ge t+r.
\]

The triangle and southeast unread fraction imply

\[
A+C+D+E\le1-r.
\]

Since `AE=CD`, the arithmetic–geometric mean inequality gives

\[
(\sqrt C+\sqrt D)^2\le A+C+D+E\le1-r,
\]

and hence the weaker but convenient necessary condition

\[
(\sqrt t+\sqrt s)^2\le1-r.
\]

The two-choice excess ratio is

\[
e(t,s,r)=\frac{ts}{(3-r)(t+s)-2ts}.
\]

For `x=sqrt(t), y=sqrt(s)`, the exact polynomial identity

\[
(x+y)^2(x^2+y^2)-8x^2y^2
=(x-y)^2(x^2+4xy+y^2)\ge0
\]

proves `ts/(t+s) <= (1-r)/8`. Therefore

\[
e(t,s,r)\le\frac{1-r}{22-6r}\le\frac1{22}.
\]

Equality in this closed limiting relaxation requires `r=0,t=s=1/4`, precisely
the scale approached by the existing construction. Thus simply rebalancing
these plateau blocks cannot strengthen 23/22. A genuinely stronger lower bound
would need a different ambiguity structure, more than two relevant information
branches, or a construction outside this shared-boundary template.

An attempted three-way terminal trigger (candidate, northwest, or southeast)
also revealed a concrete obstacle. If all three alternatives must be certified
from one common symmetric base with unread fractions `t=s=r=a`, robust
nondomination at that base and triangle feasibility force `a<=1/9` in the
limiting relaxation. Uniform three-choice search then gives only `26/25`, less
than 23/22. This rejects that symmetric attempt; it does not rule out asymmetric
or multistage three-world constructions.

## 2. Independent conceptual audit: new mixed upper bound 87/80

I independently checked the policy, cost identity, geometric reduction and
case coverage of the upper-bound agent's construction. I did not use the
producer's polynomial class or its source for the finite arithmetic check.
The separate root audit is responsible for independently rechecking all exact
Bernstein coefficients. Subject to that successful certificate check, the
following continuum argument is complete.

### Policy and validity

With probability `lambda=1/12`, run Q: fully observe both rivals, then acquire
candidate records until the robust TRUE test succeeds or census is reached.
On a negative archive use exact full-census evaluation. Otherwise run P: the
existing candidate-census, first-safe-screening policy, but choose southeast
first with conditional probability `p(G)=12 alpha(G)/11`, where

\[
\alpha(G)=
\begin{cases}
\bigl((19/3)G-2G^2\bigr)/(4+G),&G\le3/4,\\
87/80-21/(80G),&G>3/4.
\end{cases}
\]

All choices use public randomness and observed values only. Both constituent
policies terminate correctly on either verdict. Q needs no knowledge of the
retrospective certificate: full rivals plus any actual TRUE certificate's
candidate prefix are a valid extension of that certificate.

The function alpha increases on each branch:

\[
\alpha'_{\rm low}(G)
=\frac{76/3-16G-2G^2}{(4+G)^2}>0\quad(0\le G\le3/4),
\qquad
\alpha'_{\rm high}(G)=\frac{21}{80G^2}>0.
\]

Its left limit at the cut is `29/38`, its right limit is `59/80`, and its
overall supremum is `33/40`. Thus `0<=p(G)<=9/10`. There is a downward jump at
the cut; both one-sided values must be checked in the proof.

### Cost identity

Fix *any* realised TRUE certificate `(a,i,j)`, including partial-candidate
ones, and write `t=1-a/N,s=1-i/N,r=1-j/N`. Its cost divided by N is
`C=3-t-s-r`. Existing screening compatibility proves

\[
C_P/N\le3-(1-p)r-ps,
\qquad C_Q/N\le3-t.
\]

Set `U=s+t,V=r+t`. The mixture's expected excess over C is at most

\[
(1-\alpha)U+(\lambda+\alpha)V-2\lambda t.
\]

For `epsilon=7/80`, the desired upper bound is therefore exactly

\[
(1+\epsilon-\alpha)U+(\lambda+\epsilon+\alpha)V
\le3\epsilon+(2\lambda+\epsilon)t.
\]

There is no omission of the candidate-census penalty. In particular, the
coefficient `-2 lambda t` is the correct result of the mixture calculation.
The coefficient of U is at least `21/80>0`, so replacing U by its geometric
upper bound is valid.

### Geometric coverage and endpoint reduction

For the candidate lower-corner gap g, all legal certificates satisfy the
previously proved inequalities

\[
0<g<1,\quad 0\le t<g(1-g),\quad g\le G\le g+t,
\]
\[
t\le V<t+\frac{g(1-g)-t}{2g-t},\qquad
U<\frac{g(1+t-g-2V)}{1+t-g-V}.
\]

Every denominator is positive on legal states. The existing `(g,z,w)` cube
parameterisation covers this entire region, including every actual TRUE
certificate. Closed faces used by polynomial certificates merely add limiting
states and do not omit any actual states.

For fixed `g,t,U,V`, the residual is affine in alpha, which is monotone on
each branch. Endpoints in G therefore suffice. **The argument is not that the
new low-branch polynomial is affine in G:** it is quadratic after clearing
its denominator. This distinction was communicated to the producer and must
be retained in the proof.

The eight endpoint families cover the whole range:

| Family | G | g range | t range |
|---|---|---|---|
| L0 | g | [0,3/4] | [0,g(1-g)] |
| L1 | g+t | [0,1/2] | [0,g(1-g)] |
| L2 | g+t | [1/2,3/4] | [0,3/4-g] |
| L3 | 3/4, low formula | [1/2,3/4] | [3/4-g,g(1-g)] |
| H0 | g | [3/4,1] | [0,g(1-g)] |
| H1 | g+t | [3/4,1] | [0,g(1-g)] |
| H2 | g+t | [1/2,3/4] | [3/4-g,g(1-g)] |
| H3 | 3/4, high formula | [1/2,3/4] | [3/4-g,g(1-g)] |

For `g<=1/2`, `g+t<=2g-g^2<=3/4`, so no high branch is missing. On
`[1/2,3/4]`, `g(1-g)>=3/4-g`, so both affine t-parameterisations are ordered
correctly. L3 and H3 are both necessary because the cut has a jump. At the
actual equality G=3/4 the policy uses the low formula; the high formula there
is included only as a limiting endpoint of G>3/4.

After proving the residual nonnegative on these eight families, choosing a
cheapest certificate in the *analysis* yields the all-archive bound 87/80.
The acquisition policy never computes that certificate. A common nonnegative
information-free setup cost preserves the bound. The same endpoint criterion
and the same observation policy give pointwise transfer to independent
endpoint-containing triangle subdomains. The statement does not cover
arbitrary unequal row tariffs.

### Finite independent arithmetic corroboration

`scripts/lower_audit_mixed_policy.py` imports neither the producer nor its
polynomial implementation. It checked 11,754 rational parameter points,
including boundary cases, both cut values and interior G values. It checks
probability validity, the cost identity derived directly from P/Q costs,
nonnegative residuals and the final ratio. All passed. The evidence is
`evidence/Lower_Independent_Mixed_Policy_Audit_P56.json`.

These finite checks do not prove a continuum inequality; that proof is the
geometric reduction plus the independently verified exact polynomial
certificates.

## 3. Size and limits of the improvement

The new upper bound reduces `12/11` by exactly `3/880`. The remaining interval
above the lower bound 23/22 has width `37/880`, so the previous gap is narrowed
by exactly **7.5%**. The unrestricted optimum remains open. This is a concrete
mathematical improvement, not a proof of a sharp unrestricted constant.

The candidate-census class still has its established limiting optimum 12/11;
the new mixture belongs to the unrestricted class. The algorithm can leave
the candidate partly unread in branch Q. It therefore does not contradict
the existing lower theorem for candidate-census policies.
