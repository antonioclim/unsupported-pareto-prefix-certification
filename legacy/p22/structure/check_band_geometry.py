#!/usr/bin/env python3
"""Own stdlib exact-arithmetic arithmetic tests, not continuous-domain proof."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def legal(p, d):
    c, f = p
    return 0 <= f <= c <= 1 and c - f <= d


def unsupported(p, rivals):
    # Directly intersect the closed scalarisation-support intervals w in [0,1].
    lo, hi = F(0), F(1)
    for rc, rf in rivals:
        intercept = p[1] - rf
        slope = p[0] - rc - intercept
        if slope > 0:
            hi = min(hi, -intercept / slope)
        elif slope < 0:
            lo = max(lo, -intercept / slope)
        elif intercept > 0:
            return True
    return lo > hi


def true_prefix(rows, counts):
    n = len(rows[0])
    low, up = [], []
    for group, k in zip(rows, counts):
        z = tuple(sum((v[c] for v in group[:k]), F(0)) / n for c in (0, 1))
        low.append(z)
        up.append(tuple(v + F(n-k, n) for v in z))
    p = up[0]
    for v in low[1:]:
        if all(x <= y for x, y in zip(v, p)) and any(x < y for x, y in zip(v, p)):
            return False
    return unsupported(low[0], up[1:])


def construct(n, a, i, j, d):
    t, s, r = (F(n-k, n) for k in (a, i, j))
    u, v, b = s+t, r+t, d*(1-r)
    m = b-u-v
    if not (m > 0 and m*m > 4*u*v):
        return None
    z = m/2
    delta = z*z-u*v
    eps = delta/(2*b)
    x, y = b-t-eps, r+z-eps
    obs = [(x/(1-t), y/(1-t)), ((b-s+r)/(2*(1-s)),)*2, (d, F(0))]
    assert all(legal(p, d) for p in obs)
    rows = [[obs[g]]*k+[(F(0), F(0))]*(n-k) for g, k in enumerate((a, i, j))]
    assert true_prefix(rows, (a, i, j))
    # Independent numerical identity of the claimed strict crossing margin.
    assert (z-eps)**2-(u+eps)*(v+eps) == delta/2 > 0
    return rows


def lower_worlds(n, d):
    q = F(1, n)
    c = d*(1-q)
    assert c > 2*q
    eps = min((c-2*q)/16, q*q/16)
    p = (3*c/4+q/2+eps, c/4+q/2+eps)
    zero, one = (F(0), F(0)), (F(1), F(1))
    common = [[p]*n, [(d/2, d/2)]*(n-1), [(d, F(0))]*(n-1)]
    return [[common[0], common[1]+[zero], common[2]+[one]],
            [common[0], common[1]+[one], common[2]+[zero]]]


def main():
    widths = [F(1,8), F(1,4), F(1,3), F(1,2), F(2,3), F(3,4), F(1)]
    count, feasible, minima, candidate_minima = 0, 0, 0, 0
    for n in range(1, 13):
        for d in widths:
            least_sum, least_a = 3*n+1, n+1
            for a, i, j in product(range(1,n+1), repeat=3):
                count += 1
                rows = construct(n,a,i,j,d)
                if rows is not None:
                    feasible += 1
                    least_sum = min(least_sum, a+i+j)
                    least_a = min(least_a, a)
            assert least_sum == ((3-d)*n).__floor__()+1
            assert least_a == (n*(1-d/4)).__floor__()+1
            minima += 1
            candidate_minima += 1
            # Extend the sharp three-group construction to five configurations.
            i = (n*(1-d)).__floor__()+1
            rows = construct(n,n,i,n,d)
            rows += [[(F(1),F(1))]*n for _ in range(2)]
            assert true_prefix(rows,(n,i,n,1,1))
    world_cases, prefix_cases, price_cases = [], 0, 0
    for n in range(4,13):
        ds = sorted(set([F(1), F(5,2*(n-1)), F(3,n-1)] +
                        [d for d in widths if d*(n-1)>2]))
        for d in ds:
            if not 0 < d <= 1 or not d*(n-1)>2:
                continue
            worlds = lower_worlds(n,d)
            actual = []
            for idx, rows in enumerate(worlds):
                assert all(legal(p,d) for g in rows for p in g)
                passing = []
                for state in product(range(n+1), repeat=3):
                    prefix_cases += 1
                    if true_prefix(rows,state):
                        passing.append(list(state))
                expected = [[n,n,n-1],[n,n,n]] if idx == 0 else [[n,n-1,n],[n,n,n]]
                assert passing == expected, (n,d,idx,passing)
                actual.append(passing)
            world_cases.append({'N': n, 'd': str(d), 'TRUE_states': actual})
            for w,x,y in [(F(3*n-2),F(1),F(1)),(F(1,2),F(2),F(7)),(F(23),F(13,5),F(1,9))]:
                theta=y*(w+y)/(x*(w+x)+y*(w+y))
                r1=(w+x+(1-theta)*y)/(w+x)
                r2=(w+y+theta*x)/(w+y)
                claimed=1+x*y/(x*(w+x)+y*(w+y))
                assert r1 == r2 == claimed
                det=min(max((w+x+(1-q)*y)/(w+x),(w+y+q*x)/(w+y)) for q in (F(0),F(1)))
                assert det == 1+min(x,y)/(w+max(x,y))
                price_cases += 1
    out = {
        'status': 'PASS',
        'method': 'exact Fraction arithmetic; scalarisation interval oracle; own synthetic archives',
        'feasibility_integer_triples': count,
        'feasible_constructions_verified': feasible,
        'minimum_total_length_checks': minima,
        'minimum_candidate_length_checks': candidate_minima,
        'five_configuration_attainment_checks': minima,
        'hard_world_parameter_cases': len(world_cases),
        'hard_world_full_prefix_states': prefix_cases,
        'weighted_two_world_games': price_cases,
        'world_cases': world_cases,
        'scientific_scope': 'Arithmetic and implementation checks, not exhaustive tests of the continuous domain and not historical priority.',
        'producer_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'theory_sha256': hashlib.sha256((ROOT/'Band_Domain_Theorems_P22.md').read_bytes()).hexdigest(),
    }
    target = ROOT/'Band_Geometry_Exact_Check.json'
    target.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k != 'world_cases'},indent=2))


if __name__ == '__main__':
    main()
