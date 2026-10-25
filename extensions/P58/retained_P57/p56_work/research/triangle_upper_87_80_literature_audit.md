# Independent conceptual audit of the proposed87/80 upper bound

Status: **PASS within the scope below.** Date:25October2026. Reviewer: independent P56 literature/research track. This is an AI-assisted author audit, not external peer review or proof-assistant verification.

Inspected: `p56_work/research/triangle_upper_87_80.md`, the exact primary producer `scripts/upper_87_80_certificate.py`, and canonical P55 main§6.1–6.3 for the reused screening and geometry inequalities. I did not rerun or independently reconstruct the Bernstein coefficients; that check is assigned to root's separate exact implementation. This audit is conditional on those eight polynomial-family certificates being valid.

## Findings

No conceptual defect found in the new mixture, probability choice, polynomial reduction or coverage. The new policy deliberately has a rival-first branch, so it is not constrained by the12/11 candidate-census barrier. All claims concern K=3, triangle completions, unit row prices and a common setup; arbitrary tariffs are not covered.

1. **Causality and correctness:** the1/12 branch coin is drawn before data. Rival-first requires no hidden G. The other branch reads the entire candidate before computing G and its second coin. Robust TRUE tests and exact census fallback establish both signs correctly and terminate after at most3N acquired rows. The positive-instance analysis does not assume a positive promise.
2. **Probabilities:** the low α branch increases from0 to29/38; the high branch increases from the right limit59/80 to33/40. The low derivative numerator is76/3−16G−2G²≥293/24 on[0,3/4]. Thus p=12α/11 lies in[0,9/10]. The downward jump is real and is handled by separate endpoint checks, not ignored.
3. **Continuation costs:** canonical screening bounds give C_NW≤2N+j and C_SE≤2N+i for every realised TRUE certificate(a,i,j), including a<N. Upward closure gives C_Q≤2N+a. These are inequalities on each fixed archive, so their mixture is valid without coupling the random choices to the unknown optimum certificate.
4. **Mixture algebra:** unconditional weights are λ,1−λ−α,α on Q,NW,SE. Expected cost/N≤3−λt−(1−λ−α)r−αs. Subtracting C=3−t−s−r gives (1−λ)t+(1−α)s+(λ+α)r. With U=s+t,V=r+t, the desired bound is exactly(P56-1), with e=7/80.
5. **Eliminating U:**1+e−α≥87/80−33/40=21/80>0. Replacing U by the geometric upper bound therefore yields a sufficient inequality with the correct direction.
6. **G endpoint reduction:** for fixed g,t,U,V the unmultiplied slack is affine in α. Monotonicity of α within each branch is sufficient; affine dependence on G is not needed. Every branch endpoint is certified. The discontinuity at3/4 cannot introduce an unchecked interior maximum.
7. **Geometry and denominators:** the reused(C9)–(C11e) relations apply to every positive TRUE certificate. At legal states0<g<1,0≤t<g(1−g),k−V>0,D0=2g−t>0 and E0≥gk>0. In the full parameterisation H≥1 and E≥1+gz≥1. Low d=4+G and high d=G are positive on their legal branches. Clearing denominators cannot reverse the inequality.
8. **Full/cut formulas:** the supplied D,A,B coefficients are exactly the slack of(P56-1) multiplied by the appropriate positive d. The full polynomial multiplies by HE; the cut polynomial multiplies by D0E0. Their terms match the U and V substitutions, including the negative2λt benefit of the rival-first branch.
9. **Coverage:** g≤1/2 implies g+t<2g−g²≤3/4, so L0,L1 suffice. For g∈[1/2,3/4], h−g≤g(1−g); T2 spans[0,h−g] and T3 spans[h−g,g(1−g)]. L2,L3 cover the clipped low endpoint; H2,H3 cover both high endpoints when the interval crosses the cut. For g≥3/4, H0,H1 cover both endpoints. Degenerate boundary intervals and both one-sided values at h are included by closed polynomial boxes.
10. **AllN and setup:** the continuous feasibility relaxation contains the fractions arising from every integer N≥1. No asymptotic limit or rounding approximation is used in the upper bound. A common F≥0 preserves it because F+RC*≤R(F+C*) for R≥1. Endpoint-domain transfer is pointwise on shared archives and retains the same robust certificates.

## An additional finite-size consequence

P55 Theorem17 already proves the restricted lower bound

    (3N−1)/(3N−floor(N/4)+1).

It exceeds87/80 exactly when

    87floor(N/4)>21N+167.

Writing N=4q+r, r∈{0,1,2,3}, this is q≥56+7r. Consequently, **for every N≥308, unrestricted policies are strictly better than policies that always census the candidate before TRUE**, in the worst-case optimal competitive-ratio sense. N307 is the last failure of this sufficient comparison; some smaller lengths also satisfy it. This statement follows algebraically from the existing restricted lower bound and the new universal upper, not from simulations.

The asymptotic separation is at least12/11−87/80=3/880. The unresolved interval width is87/80−23/22=37/880, compared with40/880 previously, a7.5% narrowing. Neither statement settles the unrestricted limiting optimum or proves convergence of its sequence.

On the existing U family, Q stops at a=N−q+2 after both rivals are complete, paying C*+1; its limiting ratio is1. The candidate-first part has limiting ratio12/11. Their mixture therefore has limiting ratio1/12+(11/12)(12/11)=13/12. This is consistent with the candidate-observation lower bound and does not claim that this family attains the new global upper.

## Residual verification boundary

This audit checks assumptions, derivation, domain coverage and logical consequences. It relies on the previous P55 geometric lemmas and on root's separate exact check of every Bernstein coefficient, polynomial and dyadic partition. Finite operational testing is useful as an implementation control; it is not a substitute for the continuous-domain certificates.
