#!/usr/bin/env python3
"""Own exact-rational checks for P21 triangular acquisition extensions.

Finite checks exercise explicit constructions and lower witnesses only. They do
not exhaust the continuous domain, prove historical novelty, or replace proofs.
Standard library only; no network access or external code execution.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def dominated(p, q):
    """p is strictly Pareto dominated by q."""
    return all(v <= u for u, v in zip(p, q)) and p != q


def supported(p, rivals):
    lo, hi = Q(0), Q(1)
    for r in rivals:
        dx, dy = r[0] - p[0], r[1] - p[1]
        slope = dx - dy
        if slope > 0:
            lo = max(lo, -dy / slope)
        elif slope < 0:
            hi = min(hi, -dy / slope)
        elif dy < 0:
            return False
    return lo <= hi


def corners(rows, length):
    n = len(rows)
    low = tuple(sum((r[k] for r in rows[:length]), Q(0)) / n for k in (0, 1))
    return low, tuple(v + Q(n - length, n) for v in low)


def robust_true(archive, lengths):
    intervals = [corners(rows, s) for rows, s in zip(archive, lengths)]
    candidate_lo, candidate_hi = intervals[0]
    if any(dominated(candidate_hi, low) for low, high in intervals[1:]):
        return False
    return not supported(candidate_lo, [high for low, high in intervals[1:]])


def triangle_row(row):
    return 0 <= row[1] <= row[0] <= 1


def hard_archive(n, world):
    zero = (Q(0), Q(0))
    one = (Q(1), Q(1))
    pad = [zero] * (n - 4)
    a = pad + [(Q(13, 20), Q(31, 100))] * 4
    left = pad + [(Q(7, 15), Q(7, 15))] * 3 + [zero if world == 'A' else one]
    right = pad + [(Q(14, 15), Q(0))] * 3 + [one if world == 'A' else zero]
    return [a, left, right]


def feasibility(n, a, i, j):
    z = i + 2*j + 2*a - 4*n
    return z > 0 and z*z > 4*(2*n-a-i)*(2*n-a-j)


def construct_feasible(n, a, i, j):
    t, s, r = (Q(n-u, n) for u in (a, i, j))
    z = (1-s-2*r-2*t)/2
    delta = z*z - (s+t)*(r+t)
    epsilon = delta/(2*(1-r))
    assert (z-epsilon)**2-(s+t+epsilon)*(r+t+epsilon) == delta/2
    assert 0 < epsilon <= z/4
    x, y = 1-r-t-epsilon, (1-s-2*t)/2-epsilon
    zero = (Q(0), Q(0))
    return [
        [(n*x/a, n*y/a)]*a + [zero]*(n-a),
        [(Q(1, 2), Q(1, 2))]*i + [zero]*(n-i),
        [(Q(1), Q(0))]*j + [zero]*(n-j),
    ]


def main():
    states_checked = 0
    hard_records = []
    for n in (4, 5, 8, 12):
        for world in ('A', 'B'):
            archive = hard_archive(n, world)
            assert all(triangle_row(row) for group in archive for row in group)
            true_states = []
            for state in product(range(n+1), repeat=3):
                states_checked += 1
                if robust_true(archive, state):
                    true_states.append(state)
            expected = [(n,n,n-1), (n,n,n)] if world == 'A' else [(n,n-1,n), (n,n,n)]
            assert true_states == expected, (n, world, true_states)
            minimum = min(sum(p) for p in true_states)
            assert minimum == 3*n-1
            hard_records.append({'N': n, 'world': world, 'true_states': true_states,
                                 'minimum_certificate': minimum})
    feasible_count = 0
    tuples_checked = 0
    minimum_candidates = []
    for n in range(1, 13):
        passing = []
        for a, i, j in product(range(1, n+1), repeat=3):
            tuples_checked += 1
            if not feasibility(n, a, i, j):
                continue
            feasible_count += 1
            archive = construct_feasible(n, a, i, j)
            assert all(triangle_row(row) for group in archive for row in group)
            assert robust_true(archive, (a, i, j)), (n, a, i, j)
            passing.append(a)
        smallest = min(passing)
        assert smallest == 3*n//4 + 1
        minimum_candidates.append({'N': n, 'minimum_candidate_prefix': smallest})
    weighted_records = []
    for W, x, y in product(map(Q, (1, 10, 100)),
                            (Q(1, 100), Q(1), Q(7, 3), Q(100)),
                            (Q(1, 100), Q(1), Q(7, 3), Q(100))):
        denom = x*(W+x) + y*(W+y)
        q = y*(W+y)/denom
        ratio = 1+x*y/denom
        ratio_A = (W+x+(1-q)*y)/(W+x)
        ratio_B = (W+y+q*x)/(W+y)
        both_suffice_ratio = (W+q*x+(1-q)*y)/(W+min(x,y))
        assert ratio == ratio_A == ratio_B
        assert both_suffice_ratio <= ratio
        det = 1+min(x,y)/(W+max(x,y))
        assert det == min(1+x/(W+y), 1+y/(W+x))
        weighted_records.append({'W':str(W),'x':str(x),'y':str(y),'q':str(q),
                                 'randomised_ratio':str(ratio),'deterministic_ratio':str(det)})
    assert 1+Q(1,22) == Q(23,22)
    assert 1+Q(1,11) == Q(12,11)
    result = {
        'status':'PASS',
        'scope':'Exact finite arithmetic checks of explicit witnesses and constructions; analytic continuum results require the accompanying proofs.',
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'proof_sha256':hashlib.sha256((ROOT/'triangle_four_rows_exact.md').read_bytes()).hexdigest(),
        'hard_worlds':hard_records,
        'hard_world_prefix_states_checked':states_checked,
        'feasibility_integer_tuples_checked':tuples_checked,
        'feasible_tuples_constructed_and_verified':feasible_count,
        'candidate_minimum_checks':minimum_candidates,
        'weighted_formula_cases':weighted_records,
        'weighted_formula_cases_checked':len(weighted_records),
        'installs':False,'network_access':False,'external_scientific_code':False,
        'new_measurements':0,
    }
    target = ROOT/'Triangle_Extension_Exact_Check.json'
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:result[key] for key in (
        'status','hard_world_prefix_states_checked','feasibility_integer_tuples_checked',
        'feasible_tuples_constructed_and_verified','weighted_formula_cases_checked')},indent=2))


if __name__ == '__main__':
    main()
