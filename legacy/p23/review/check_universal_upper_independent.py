#!/usr/bin/env python3
"""Independent exact continuous check of the P23 universal randomised upper.

This checker does not import or run the producer. It computes Bernstein
coefficients by exact interpolation of the cleared gap, rather than the
producer's symbolic power coefficients and recursive de Casteljau splits.
All 32 boxes of a fixed 4 x 4 x 2 partition are checked at the common
degree (6,4,2). A separate rational interpolation identity check guards
the assumed polynomial degree at extra nodes. Analytic degree bounds,
policy legality, and geometric reduction are in the independent review.
"""
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
DEGREES = (6, 4, 2)
INDICES = tuple(product(*(range(n + 1) for n in DEGREES)))


def bernstein(n, j, x):
    return F(comb(n, j)) * x**j * (1-x)**(n-j)


def inverse(matrix):
    n = len(matrix)
    a = [list(row) + [F(int(i == j)) for j in range(n)]
         for i, row in enumerate(matrix)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if a[i][j])
        a[j], a[pivot] = a[pivot], a[j]
        scale = a[j][j]
        a[j] = [v/scale for v in a[j]]
        for i in range(n):
            if i != j:
                scale = a[i][j]
                a[i] = [v-scale*w for v, w in zip(a[i], a[j])]
    assert all(a[i][j] == int(i == j) for i in range(n) for j in range(n))
    return [row[n:] for row in a]


INVERSES = [inverse([[bernstein(n, j, F(k, n)) for j in range(n+1)]
                     for k in range(n+1)]) for n in DEGREES]


def cleared_gap(endpoint, g, z, w):
    # Derived directly from e*(certificate cost) - policy excess, times
    # the three positive denominators (1+G), H, E.
    e = F(3, 32)
    t = g*(1-g)*z
    big_gap = g if endpoint == 0 else g+t
    h = 2-(1-g)*z
    j = w*(1-z)
    e_denom = h-j
    v = (1-g)*(g*z*h+j)/h
    u = g*((1-g*z)*h-2*j)/e_denom
    prob_se = 2*big_gap/(1+big_gap)
    certificate = 3+t-u-v
    excess = (1-prob_se)*u+prob_se*v
    return (e*certificate-excess)*(1+big_gap)*h*e_denom


def coefficients(endpoint, box):
    sampled = {}
    for k in INDICES:
        point = [lo+(hi-lo)*F(i, n) for i, n, (lo, hi)
                 in zip(k, DEGREES, box)]
        sampled[k] = cleared_gap(endpoint, *point)
    for axis, transform in enumerate(INVERSES):
        new = {}
        for k in INDICES:
            total = F(0)
            key = list(k)
            for j in range(DEGREES[axis]+1):
                key[axis] = j
                total += transform[k[axis]][j]*sampled[tuple(key)]
            new[k] = total
        sampled = new
    return sampled


def evaluate_bernstein(coeffs, point):
    bases = [[bernstein(n, j, x) for j in range(n+1)]
             for n, x in zip(DEGREES, point)]
    return sum((value*bases[0][k[0]]*bases[1][k[1]]*bases[2][k[2]]
                for k, value in coeffs.items()), F(0))


def verify():
    partitions = [[(F(i, n), F(i+1, n)) for i in range(n)] for n in (4, 4, 2)]
    boxes = tuple(product(*partitions))
    report = {
        'status': 'PASS',
        'method': 'Exact rational tensor interpolation into Bernstein basis; fixed partition',
        'common_multidegree': list(DEGREES),
        'partition_counts': [4, 4, 2],
        'coefficients_per_box': len(INDICES),
        'degree_argument': 'Cleared expression has coordinate degrees at most (6,4,2); see review.',
        'polynomials': [],
    }
    for endpoint in (0, 1):
        rows = []
        for box in boxes:
            coeffs = coefficients(endpoint, box)
            minimum = min(coeffs.values())
            assert minimum >= 0, (endpoint, box, minimum)
            # Extra-node identity checks do not establish positivity; exact
            # Bernstein coefficients plus the analytic degree bound do.
            for point in ((F(1,7),F(2,7),F(3,7)),
                          (F(4,7),F(5,7),F(6,7))):
                actual = [lo+(hi-lo)*x for x,(lo,hi) in zip(point,box)]
                assert evaluate_bernstein(coeffs, point) == cleared_gap(endpoint, *actual)
            rows.append({'box': [[str(lo),str(hi)] for lo,hi in box],
                         'minimum_coefficient': str(minimum)})
        report['polynomials'].append({'endpoint':endpoint,
            'boxes':rows, 'minimum_coefficient':str(min(F(row['minimum_coefficient']) for row in rows)),
            'coefficients_checked':len(rows)*len(INDICES),
            'additional_identity_checks':2*len(rows)})
    report['total_coefficients_checked'] = 2*len(boxes)*len(INDICES)
    report['input_sha256'] = {str(path.relative_to(ROOT)):
        hashlib.sha256(path.read_bytes()).hexdigest() for path in (
            ROOT/'upper/Universal_Triangle_Upper_Bounds_P23.md',
            ROOT/'upper/check_universal_upper.py',
            ROOT/'upper/Universal_Upper_Exact_Check.json',
            Path(__file__).resolve())}
    return report


if __name__ == '__main__':
    result = verify()
    destination = Path(__file__).with_name('Universal_Upper_Independent_Check.json')
    destination.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','total_coefficients_checked','common_multidegree')}))
    for item in result['polynomials']:
        print('Endpoint',item['endpoint'],'minimum exact Bernstein coefficient',item['minimum_coefficient'])
