"""Independent exact rational spot checks for the P56 mixed-policy proof.

This file imports neither the producer nor its polynomial implementation.
The continuum argument is documented separately; these checks are finite
arithmetic corroboration, NOT a substitute for Bernstein certificates.
"""
from fractions import Fraction as F
from pathlib import Path
import json

lam, eps, cut = F(1, 12), F(7, 80), F(3, 4)

def alpha(G, branch):
    if branch == 'low':
        return (F(19, 3)*G - 2*G*G)/(4+G)
    return F(87, 80) - F(21, 80)/G

checks = 0
min_residual = None
seen = set()
for gi in range(1, 24):
    g = F(gi, 24)
    for zi in range(9):
        z = F(zi, 8)
        t = g*(1-g)*z
        D0 = 2*g-t
        delta = g*(1-g)-t
        for wi in range(9):
            w = F(wi, 8)
            V = t+w*delta/D0
            k = 1+t-g
            U = g*(k-2*V)/(k-V)
            assert U >= t and V >= t
            s, r = U-t, V-t
            C = 3-t-s-r
            assert C > 0
            endpoints = []
            if g <= cut:
                endpoints.extend([(g, 'low'), (min(g+t, cut), 'low')])
            if g+t >= cut:
                endpoints.extend([(max(g, cut), 'high'), (g+t, 'high')])
            # Include interior points, not just the endpoints used in the proof.
            for qi in range(1, 5):
                G = g+t*F(qi, 5)
                endpoints.append((G, 'low' if G <= cut else 'high'))
            for G, branch in endpoints:
                a = alpha(G, branch)
                p = a/(1-lam)
                assert 0 <= p <= 1
                # Independently derive mixture and excess directly from costs.
                p_cost = 3-(1-p)*r-p*s
                q_cost = 3-t
                mixed = (1-lam)*p_cost+lam*q_cost
                linear_excess = (1-a)*U+(lam+a)*V-2*lam*t
                assert mixed-C == linear_excess
                residual = 3*eps+(2*lam+eps)*t-(1+eps-a)*U-(lam+eps+a)*V
                assert residual >= 0, (g, z, w, G, branch, residual)
                assert mixed <= F(87, 80)*C
                min_residual = residual if min_residual is None else min(min_residual, residual)
                checks += 1
                seen.add(branch)

# Boundary values, derivative bounds and downward jump checked exactly.
alpha_left = alpha(cut, 'low')
alpha_right = alpha(cut, 'high')
assert alpha_left == F(29, 38)
assert alpha_right == F(59, 80)
assert alpha_left > alpha_right
assert alpha(F(1), 'high') == F(33, 40)
low_derivative_numerator_min = F(76, 3)-16*cut-2*cut*cut
assert low_derivative_numerator_min > 0
assert F(87, 80)-F(33, 40) == F(21, 80) > 0

out = {
    'status': 'PASS',
    'finite_exact_point_checks': checks,
    'branches': sorted(seen),
    'minimum_grid_residual': str(min_residual),
    'alpha_left_at_cut': str(alpha_left),
    'alpha_right_at_cut': str(alpha_right),
    'alpha_maximum': '33/40',
    'conditional_southeast_probability_maximum': '9/10',
    'low_derivative_numerator_lower_bound': str(low_derivative_numerator_min),
    'new_ratio': '87/80',
    'old_upper_minus_new_upper': str(F(12, 11)-F(87, 80)),
    'new_upper_minus_old_lower': str(F(87, 80)-F(23, 22)),
    'gap_relative_reduction': str((F(12, 11)-F(87, 80))/(F(12, 11)-F(23, 22))),
    'scope': 'Finite exact arithmetic corroboration of independently derived cost identity; not a continuum nonnegativity proof.'
}
path = Path('p56_work/evidence/Lower_Independent_Mixed_Policy_Audit_P56.json')
path.write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
