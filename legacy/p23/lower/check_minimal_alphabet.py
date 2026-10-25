#!/usr/bin/env python3
"""Own exact finite checks for the three-symbol P23 lower construction.

Standard library only. Critical-weight vertices are tested independently
of the P22 interval-intersection implementation. The analytic note supplies
the universal all-N and all-algorithm proof.
"""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
ALPHABET = {(0, 0), (1, 0), (1, 1)}


def has_support(candidate, rivals):
    """Each affine half-interval's endpoints suffice in one weight dimension."""
    differences = [(c-candidate[0], f-candidate[1]) for c, f in rivals]
    weights = [(0, 1), (1, 1)]
    for dx, dy in differences:
        num, den = -dy, dx-dy
        if den < 0:
            num, den = -num, -den
        if den > 0 and 0 <= num <= den:
            weights.append((num, den))
    return any(all(dx*num + dy*(den-num) >= 0 for dx, dy in differences)
               for num, den in weights)


def true(corners, state):
    (pl, pu), (ll, lu), (rl, ru) = [corners[g][k] for g, k in enumerate(state)]
    if any(z[0] <= pu[0] and z[1] <= pu[1] and z != pu for z in (ll, rl)):
        return False
    return not has_support(pl, (lu, ru))


def make(q, padding, world):
    assert q >= 2 and padding >= 0 and world in ('U', 'V')
    n = 4*q + padding
    a = [(0, 0)]*padding + [(1, 0)]*(2*q) + [(1, 1)]*q + [(0, 0)]*q
    l = [(0, 0)]*padding + [(1, 1)]*q + [(0, 0)]*(2*q) + [(1, 1)]*q
    r = [(0, 0)]*padding + [(1, 0)]*(4*q)
    a[-1] = (0, 0) if world == 'U' else (1, 0)
    l[-1] = (0, 0) if world == 'U' else (1, 1)
    rows = [a, l, r]
    assert all(len(group) == n for group in rows)
    assert {row for group in rows for row in group} == ALPHABET
    corners = []
    for group in rows:
        c, f = 0, 0
        values = []
        for k in range(n+1):
            if k:
                c += group[k-1][0]
                f += group[k-1][1]
            values.append(((c, f), (c+n-k, f+n-k)))
        corners.append(values)
    return rows, corners, n


def main():
    records = []
    full_count = slice_count = 0
    cases = [(q, 0) for q in range(3, 13)] + [(3, 1), (4, 2), (5, 3), (25, 0), (100, 3)]
    for q, padding in cases:
        for world in ('U', 'V'):
            rows, corners, n = make(q, padding, world)
            other_rows = make(q, padding, 'V' if world == 'U' else 'U')[0]
            assert rows[0][:-1] == other_rows[0][:-1]
            assert rows[1][:-1] == other_rows[1][:-1]
            assert rows[2] == other_rows[2]
            b_a, b_l, b_r = n-q+2, n-q+1, n-1
            obstruction = (n, n-1, n) if world == 'U' else (n-1, n, n)
            assert not true(corners, obstruction)
            full = n <= 48
            if full:
                states = product(range(n+1), repeat=3)
            elif world == 'U':
                states = ((a, n, j) for a, j in product(range(n+1), repeat=2))
            else:
                states = ((n, i, j) for i, j in product(range(n+1), repeat=2))
            total = positives = 0
            minimum = None
            for a, i, j in states:
                expected = (a >= b_a and i == n and j >= b_r) if world == 'U' else (a == n and i >= b_l and j >= b_r)
                got = true(corners, (a, i, j))
                assert got == expected, (q, padding, world, (a, i, j), got, expected)
                total += 1
                if got:
                    positives += 1
                    cost = a+i+j
                    minimum = cost if minimum is None else min(minimum, cost)
            assert positives == (2*(q-1) if world == 'U' else 2*q)
            assert minimum == (3*n-q+1 if world == 'U' else 3*n-q)
            if full:
                full_count += total
            else:
                slice_count += total
            records.append(dict(q=q, padding=padding, N=n, world=world,
                                mode='all_prefixes' if full else 'complete_2d_slice_with_monotone_exclusion',
                                states_checked=total, true_states=positives,
                                minimum_certificate=minimum, omitted_region_obstruction=obstruction))

    # Preserve the actual adverse q=2 boundary; the claimed family starts at q=3.
    _, bad_corners, _ = make(2, 0, 'V')
    assert not true(bad_corners, (8, 7, 7))
    assert true(bad_corners, (8, 7, 8))

    weighted = 0
    for W, X, Y in product(map(F, (1, 10, 100)),
                          (F(1, 100), F(1), F(7, 3), F(100)),
                          (F(1, 100), F(1), F(7, 3), F(100))):
        den = X*(W+X)+Y*(W+Y)
        theta = Y*(W+Y)/den
        ratio = 1+X*Y/den
        assert (W+Y+theta*X)/(W+Y) == ratio
        assert (W+X+(1-theta)*Y)/(W+X) == ratio
        assert 1+min(X, Y)/(W+max(X, Y)) == min(1+X/(W+Y), 1+Y/(W+X))
        weighted += 1

    identities = 0
    for q in range(3, 1003):
        h = F(1, 4*q)
        assert (F(1, 4)+h)*(F(1, 4)-2*h)-(F(1, 4)-h)*F(1, 4) == -2*h*h
        assert (F(1, 4)+h)*(F(1, 4)-h)-(F(1, 4)-h)*F(1, 4) == h*(F(1, 4)-h) > 0
        for padding in range(4):
            n = 4*q+padding
            W, X, Y = 3*n-2*q+2, q-2, q-1
            randomised = 1+F(X*Y, X*(W+X)+Y*(W+Y))
            expected = 1+F((q-2)*(q-1), (q-2)*(3*n-q)+(q-1)*(3*n-q+1))
            assert randomised == expected
            assert 1+F(min(X, Y), W+max(X, Y)) == 1+F(q-2, 3*n-q+1)
            identities += 1

    # A finite corroboration only; Theorem 3 proves all possible two-vector alphabets.
    lattice = list(product(range(-1, 2), repeat=2))
    two_symbol_cases = 0
    for x, y in combinations(lattice, 2):
        for n in range(1, 7):
            means = [(n*x[0]+m*(y[0]-x[0]), n*x[1]+m*(y[1]-x[1])) for m in range(n+1)]
            for a, l, r in product(means, repeat=3):
                dominated = any(z[0] <= a[0] and z[1] <= a[1] and z != a for z in (l, r))
                assert dominated or has_support(a, (l, r)), (x, y, n, a, l, r)
                two_symbol_cases += 1

    nonvacuity = []
    n5_positive = set()
    for n in range(1, 6):
        means = [(m, k) for m in range(n+1) for k in range(m+1)]
        total = positives = 0
        for a, l, r in product(means, repeat=3):
            dominated = any(z[0] <= a[0] and z[1] <= a[1] and z != a for z in (l, r))
            good = not dominated and not has_support(a, (l, r))
            total += 1
            positives += good
            if n == 5 and good:
                n5_positive.add((a, l, r))
        assert (positives > 0) == (n >= 5)
        nonvacuity.append(dict(N=n, complete_mean_triples=total, positive_triples=positives))
    assert not has_support((4, 1), ((2, 2), (5, 0)))
    expected_n5 = {((4, 1), (2, 2), (5, 0)), ((4, 1), (5, 0), (2, 2)),
                   ((4, 2), (3, 3), (5, 0)), ((4, 2), (5, 0), (3, 3))}
    assert n5_positive == expected_n5
    n5_partial_checks = 0
    for means in sorted(n5_positive):
        for group in range(3):
            m, k = means[group]
            counts = {(0, 0):5-m, (1, 0):m-k, (1, 1):k}
            for last, count in counts.items():
                if not count:
                    continue
                corners = [[(v, v)] for v in means]
                lower = (m-last[0], k-last[1])
                upper = (lower[0]+1, lower[1]+1)
                corners[group] = [(lower, upper)]
                assert not true(corners, (0, 0, 0)), (means, group, last)
                n5_partial_checks += 1

    result = dict(status='PASS',
                  scope='Exact finite explicit archives, critical-weight vertex checks and arithmetic; universal proofs are in the note.',
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  proof_sha256=hashlib.sha256((ROOT/'Minimal_Alphabet_Persistent_Overhead_P23.md').read_bytes()).hexdigest(),
                  alphabet=[list(x) for x in sorted(ALPHABET)], alphabet_size=3,
                  worlds=records, worlds_checked=len(records),
                  fully_enumerated_prefix_states=full_count,
                  complete_slice_states=slice_count,
                  total_prefix_states=full_count+slice_count,
                  weighted_balancing_cases=weighted,
                  formula_padding_cases=identities,
                  two_symbol_negative_cases=two_symbol_cases,
                  exact_nonvacuity_grid=nonvacuity,
                  n5_positive_complete_triples=sorted(n5_positive),
                  n5_critical_one_unread_row_checks=n5_partial_checks,
                  n5_arbitrary_positive_price_ratios={'randomised':'1','deterministic':'1'},
                  adverse_q2={'state_8_7_7':False, 'state_8_7_8':True},
                  asymptotic_randomised_lower='23/22',
                  asymptotic_deterministic_lower='12/11',
                  global_asymptotic_exactness=False,
                  new_measurements=0, external_code=False, network=False, installs=False)
    (ROOT/'Minimal_Alphabet_Exact_Check.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','worlds_checked','fully_enumerated_prefix_states','complete_slice_states','total_prefix_states','weighted_balancing_cases','formula_padding_cases','two_symbol_negative_cases']}, indent=2))


if __name__ == '__main__':
    main()
