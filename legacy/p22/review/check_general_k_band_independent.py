"""Independent exact checks of P22 general-K diagonal-band embedding.

Own audit implementation, Python standard library only. Finite enumerations
test explicit archives; they do not prove the continuous-domain minimax lower
or replace the inherited adaptive Ramsey theorem.
"""
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import hashlib
import json


def supporting_weight_exists(p, rivals):
    low, high = F(0), F(1)
    for c, f in rivals:
        v0 = f - p[1]
        slope = c - p[0] - v0
        if slope == 0:
            if v0 < 0:
                return False
        elif slope > 0:
            low = max(low, -v0 / slope)
        else:
            high = min(high, -v0 / slope)
        if low > high:
            return False
    return True


def all_corners(archive):
    n = len(archive[0])
    result = []
    for rows in archive:
        sums = [F(0), F(0)]
        boxes = []
        for s in range(n + 1):
            if s:
                for k in (0, 1):
                    sums[k] += rows[s - 1][k]
            lower = (sums[0] / n, sums[1] / n)
            upper = tuple(v + F(n - s, n) for v in lower)
            boxes.append((lower, upper))
        result.append(boxes)
    return result


def true_state(boxes, state):
    p, u = boxes[0][state[0]]
    uppers = []
    for b, s in zip(boxes[1:], state[1:]):
        lower, upper = b[s]
        if lower[0] <= u[0] and lower[1] <= u[1] and lower != u:
            return False
        uppers.append(upper)
    return not supporting_weight_exists(p, uppers)


def legal(archive, d):
    return all(F(0) <= f <= c <= F(1) and c - f <= d
               for group in archive for c, f in group)


def psi(z):
    return F(6, 5) + z / (5 * (z + 1))


def embedded_archive(n, left, right, d):
    c, f = F(2, 3), F(1, 6)
    out = [[(d * c / n, d * f / n)] * n]
    for z in left:
        u = psi(z)
        ell = (c * u + f) / (1 + u)
        assert F(29, 66) < ell < F(11, 24)
        out.append([(d / 3, d / 3)] + [(F(0), F(0))] * (n - 2)
                   + [(d * (ell - F(1, 3)),) * 2])
        assert (ell - f) / (c - ell) == u
    for z in right:
        v = psi(z)
        rr = c + f / v
        assert F(11, 14) < rr < F(29, 36)
        out.append([(3 * d / 4, F(0))] + [(F(0), F(0))] * (n - 2)
                   + [(d * (rr - F(3, 4)), F(0))])
        assert f / (rr - c) == v
    return out


def check_inversion_case(n, m, r, d, every_permutation=True):
    # Rbad^(r-1), Lgood, Rgood, Lbad^(m-1), with strictly increasing ranks.
    left = [F(r)] + [F(z) for z in range(r + 2, r + m + 1)]
    right = [F(z) for z in range(1, r)] + [F(r + 1)]
    lp = list(permutations(left)) if every_permutation else [tuple(left)]
    rp = list(permutations(right)) if every_permutation else [tuple(right)]
    count = states = positive_states = 0
    comparator = n + m + r + 2 * (n - 1)
    for lv, rv in product(lp, rp):
        archive = embedded_archive(n, lv, rv, d)
        assert legal(archive, d)
        boxes = all_corners(archive)
        li = 1 + lv.index(F(r))
        ri = 1 + m + rv.index(F(r + 1))
        positives = []
        for s in product(range(n + 1), repeat=1 + m + r):
            actual = true_state(boxes, s)
            expected = s[0] == n and min(s[1:]) >= 1 and s[li] == n and s[ri] == n
            assert actual == expected, (n, m, r, d, lv, rv, s, actual)
            states += 1
            if actual:
                positives.append(sum(s))
                positive_states += 1
        assert min(positives) == comparator
        # A concrete legal false completion for every uncensused candidate.
        actual_means = [group[-1][0] for group in boxes]
        anchor = actual_means[1 + m]
        for a in range(n):
            candidate_rows = list(archive[0])
            candidate_rows[a] = (F(1), F(1))
            cp = tuple(sum(row[k] for row in candidate_rows) / n for k in (0, 1))
            assert anchor[0] < cp[0] and anchor[1] < cp[1]
        count += 1
    return {'N': n, 'L': m, 'R': r, 'd': str(d), 'worlds': count,
            'prefix_states': states, 'TRUE_states': positive_states,
            'comparator': comparator}


def deterministic_archive(n, m, good, d):
    archive = [[(2 * d / (3 * n), d / (6 * n))] * n]
    archive.append([(3 * d / 4, F(0))] + [(F(0), F(0))] * (n - 1))
    for j in range(m):
        tail = F(0) if j == good else d / 4
        archive.append([(d / 3, d / 3)] + [(F(0), F(0))] * (n - 2)
                       + [(tail, tail)])
    return archive


def check_deterministic(n, m, d):
    states = 0
    for good in range(m):
        archive = deterministic_archive(n, m, good, d)
        assert legal(archive, d)
        boxes = all_corners(archive)
        minimum = 10**9
        for s in product(range(n + 1), repeat=m + 2):
            expected = s[0] == s[1] == s[2 + good] == n and min(s[2:]) >= 1
            actual = true_state(boxes, s)
            assert expected == actual, (n, m, d, good, s)
            if actual:
                minimum = min(minimum, sum(s))
            states += 1
        assert minimum == (m + 2) + 3 * n - 3
    bad = deterministic_archive(n, m, None, d)
    assert not true_state(all_corners(bad), (n,) * (m + 2))
    return {'N': n, 'K': m + 2, 'd': str(d), 'positive_worlds': m,
            'prefix_states': states, 'all_bad_supported': True}


def band_feasible(n, a, i, j, d):
    t, s, r = F(n - a, n), F(n - i, n), F(n - j, n)
    u, v, b = s + t, r + t, d * (1 - r)
    mm = b - u - v
    return mm > 0 and mm * mm > 4 * u * v


def construct(n, a, i, j, d):
    t, s, r = F(n - a, n), F(n - i, n), F(n - j, n)
    u, v, b = s + t, r + t, d * (1 - r)
    z = (b - u - v) / 2
    delta = z * z - u * v
    epsilon = delta / (2 * b)
    x, y = b - t - epsilon, r + z - epsilon
    nw = (b - s + r) / (2 * (1 - s))
    values = [(x / (1 - t), y / (1 - t)), (nw, nw), (d, F(0))]
    archive = [[value] * k + [(F(0), F(0))] * (n - k)
               for value, k in zip(values, (a, i, j))]
    assert legal(archive, d)
    assert true_state(all_corners(archive), (a, i, j))
    aa = z - epsilon
    assert aa * aa - (u + epsilon) * (v + epsilon) == delta / 2
    return archive


def check_feasibility_and_minimum():
    triples = feasible = minima = 0
    records = []
    for n in range(1, 13):
        widths = sorted({F(1), F(1, 2), F(1, 3), F(1, n), F(1, n + 1),
                         min(F(1), F(2, n)), F(2 * n - 1, 2 * n)})
        for d in widths:
            best = 10**9
            for a, i, j in product(range(1, n + 1), repeat=3):
                triples += 1
                if not band_feasible(n, a, i, j, d):
                    continue
                archive = construct(n, a, i, j, d)
                feasible += 1
                missing = 3 * n - a - i - j
                assert missing < d * n
                if d * n <= 1:
                    assert (a, i, j) == (n, n, n)
                best = min(best, a + i + j)
            expected = ((3 - d) * n).__floor__() + 1
            assert best == expected, (n, d, best, expected)
            i = (n * (1 - d)).__floor__() + 1
            a3 = construct(n, n, i, n, d)
            # Additional rivals with only first row disclosed retain certificate.
            for k in (3, 4, 7):
                extended = a3 + [[(F(1), F(1))] * n for _ in range(k - 3)]
                state = (n, i, n) + (1,) * (k - 3)
                assert true_state(all_corners(extended), state)
                assert sum(state) == k + expected - 3
                minima += 1
            records.append({'N': n, 'd': str(d), 'minimum_three_group_cost': best,
                            'bridge_B': 3 * n - best,
                            'narrow_exact_regime': d * n <= 1})
    return {'oriented_triples': triples, 'feasible_constructions': feasible,
            'minimum_certificate_constructions': minima, 'records': records}


def main():
    inv = []
    for n, m, r, every in [(2, 1, 1, True), (3, 1, 1, True), (5, 1, 1, True),
                            (2, 1, 2, True), (3, 1, 2, True),
                            (2, 2, 2, True), (3, 2, 2, True),
                            (2, 2, 3, True), (3, 2, 3, False)]:
        for d in (F(1), F(1, n), F(1, n + 1)):
            inv.append(check_inversion_case(n, m, r, d, every))
    det = [check_deterministic(n, m, d)
           for n, m in [(2, 1), (3, 1), (2, 2), (3, 2), (2, 3), (3, 3)]
           for d in (F(1), F(1, n), F(1, n + 1))]
    geom = check_feasibility_and_minimum()
    result = {
        'status': 'PASS',
        'arithmetic': 'fractions.Fraction, exact rational',
        'inversion_cases': inv, 'deterministic_cases': det,
        'inversion_worlds': sum(x['worlds'] for x in inv),
        'inversion_prefix_states': sum(x['prefix_states'] for x in inv),
        'deterministic_positive_worlds': sum(x['positive_worlds'] for x in det),
        'deterministic_prefix_states': sum(x['prefix_states'] for x in det),
        'geometry': geom,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope': 'Finite checks of explicit band archives and constructive length theorem; '
                 'not exhaustive continuous-domain policy verification, formal proof, '
                 'or a replacement for the inherited adaptive Ramsey argument.'
    }
    destination = Path(__file__).with_name('General_K_Band_Independent_Check.json')
    destination.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items()
                      if k not in {'inversion_cases', 'deterministic_cases', 'geometry'}}, indent=2))
    print(json.dumps({k: v for k, v in geom.items() if k != 'records'}, indent=2))


if __name__ == '__main__':
    main()
