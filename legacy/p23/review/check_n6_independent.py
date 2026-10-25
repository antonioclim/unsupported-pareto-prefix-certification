#!/usr/bin/env python3
"""Independent exact review checks for the P23 N=6 theorem.

No import from the producer or prior checkers. All row coordinates use
integer denominator 3000. Supporting weights use a lambda>=0 interval,
with the cost-axis case handled separately.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
PROOF = ROOT.parent/'finite/N6_Deterministic_Exact_and_Randomised_Lower_P23.md'
SCALE, N = 3000, 6


def support(p, rivals):
    diffs = [(z[0]-p[0], z[1]-p[1]) for z in rivals]
    if all(dx >= 0 for dx, dy in diffs):
        return True  # w_f=0 is legal.
    lower, upper = F(0), None
    for dx, dy in diffs:
        if dx == 0:
            if dy < 0:
                return False
        elif dx > 0:
            lower = max(lower, F(-dy, dx))
        else:
            bound = F(-dy, dx)
            upper = bound if upper is None else min(upper, bound)
    return upper is None or lower <= upper


def corners(rows):
    result = []
    for group in rows:
        values, total_c, total_f = [], 0, 0
        for k in range(N+1):
            if k:
                c, f = group[k-1]
                assert 0 <= f <= c <= SCALE
                total_c += c
                total_f += f
            w = SCALE*(N-k)
            values.append(((total_c, total_f), (total_c+w, total_f+w)))
        result.append(values)
    return result


def true(cs, state):
    (pl, pu), (ll, lu), (rl, ru) = [cs[g][k] for g, k in enumerate(state)]
    if any(z[0] <= pu[0] and z[1] <= pu[1] and z != pu for z in (ll, rl)):
        return False
    return not support(pl, (lu, ru))


def worlds():
    r = [(3000, 0)]*6
    d_a = [(2988, 900)]*5
    d_l = [(2280, 2280)]*2 + [(420, 420)]*2
    q_a = [(2988, 360)]*5
    q_l = [(1830, 1830)] + [(840, 840)]*4
    return {
        'U': [d_a+[(0, 0)], d_l+[(2220, 2220), (3000, 3000)], r],
        'V': [d_a+[(3000, 0)], d_l+[(3000, 3000)]*2, r],
        'A': [q_a+[(0, 0)], q_l+[(840, 840)], r],
        'B': [q_a+[(3000, 0)], q_l+[(3000, 3000)], r],
    }


def main():
    records = []
    archives = worlds()
    expected_cost = {'U':16, 'V':14, 'A':17, 'B':13}
    for name, rows in archives.items():
        cs = corners(rows)
        found = []
        for a, i, j in product(range(7), repeat=3):
            if name == 'U':
                expected = a >= 5 and i >= 5 and j == 6
            elif name == 'V':
                expected = a == 6 and i >= 2 and j == 6
            elif name == 'A':
                expected = a >= 5 and i == 6 and j == 6
            else:
                expected = a == 6 and i >= 1 and j == 6
            actual = true(cs, (a, i, j))
            assert actual == expected, (name, (a, i, j), actual, expected)
            if actual:
                found.append((a, i, j))
        assert min(map(sum, found)) == expected_cost[name]
        records.append(dict(world=name, states_checked=343, true_states=found,
                            minimum_row_cost=expected_cost[name]))
    assert archives['U'][0][:-1] == archives['V'][0][:-1]
    assert archives['U'][1][:4] == archives['V'][1][:4]
    assert archives['U'][1][-1] == archives['V'][1][-1]
    assert archives['A'][0][:-1] == archives['B'][0][:-1]
    assert archives['A'][1][:-1] == archives['B'][1][:-1]

    feasible = []
    for a, i, j in product(range(1, 7), repeat=3):
        z = i+2*j+2*a-24
        if z > 0 and z*z > 4*(12-a-i)*(12-a-j):
            feasible.append((a, i, j))
    minima = [x for x in feasible if not any(y != x and all(a <= b for a, b in zip(y, x)) for y in feasible)]
    assert minima == [(5, 5, 6), (6, 1, 6), (6, 5, 5), (6, 6, 4)]
    assert all(x == (6, sum(x)-12, 6) for x in feasible if sum(x) <= 15)
    assert [x for x in feasible if x[0] == 6 and sum(x) == 16] == [(6, 4, 6), (6, 5, 5), (6, 6, 4)]
    assert [x for x in feasible if x[0] < 6 and sum(x) == 16] == [(5, 5, 6)]

    # Exact all-F upper envelope: coefficients of an affine polynomial after
    # cancellation of F^2 must both be nonpositive.
    upper_cases = []
    for c, cost in [(13, 13), (14, 14), (15, 15), (16, 17), (17, 18), (18, 18)]:
        coefficient, constant = cost-c-1, 16*cost-17*c
        assert coefficient <= 0 and constant <= 0
        upper_cases.append(dict(comparator=c, policy_cost_bound=cost,
                                affine_F_coefficient=coefficient, affine_constant=constant))

    gap_checks = 0
    for k in range(121):
        g = F(k, 120)
        assert ((g-F(1, 3))*(F(5, 6)-g) > F(1, 18)) == (F(1, 2) < g < F(2, 3))
        gap_checks += 1
    assert F(1, 2)+F(2, 3) == F(7, 6) and F(1, 2)*F(2, 3) == F(1, 3)

    setup_checks = 0
    for setup in [F(k) for k in range(101)] + [F(1, 100), F(2, 3), F(101, 7)]:
        assert min((setup+17)/(setup+16), (setup+17)/(setup+14)) == 1+1/(setup+16)
        q = 5*(setup+17)/(6*setup+98)
        ratio = 1+5/(6*setup+98)
        assert 0 < q < 1
        assert (setup+17+q)/(setup+17) == ratio
        assert (setup+18-5*q)/(setup+13) == ratio
        assert ratio <= 1+1/(setup+16)
        setup_checks += 1

    result = dict(status='PASS', proof_sha256=hashlib.sha256(PROOF.read_bytes()).hexdigest(),
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  worlds=records, all_prefix_states=1372, prefix_shape_triples=216,
                  minimal_shapes=minima, all_F_upper_envelope=upper_cases,
                  exact_gap_cases=gap_checks, exact_setup_cases=setup_checks,
                  global_randomised_exactness_claimed=False,
                  scope='Independent finite exact checks and all-F affine envelope; universal policy validity is analytically reviewed separately.')
    (ROOT/'N6_Independent_Check.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','proof_sha256','all_prefix_states','prefix_shape_triples','exact_gap_cases','exact_setup_cases']}, indent=2))


if __name__ == '__main__':
    main()
