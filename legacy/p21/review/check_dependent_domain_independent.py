"""Independent arithmetic checks for P21, own code and Python standard library.

This checker does not import the producer's code. It checks the constructive
integer bound, endpoint ramp feasibility and the scalarisation threshold.
Universal claims remain analytic; these are finite checks.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json


def main():
    counts = 0
    for n in range(1, 5001):
        m = 8*n//5 + 1
        i, j = m//2, (m+1)//2
        difference = 5*i*j - 2*n*(i+j)
        q, r = divmod(n, 5)
        residue = (10*q, 4*q+1, 8*q+4, 2*q, 6*q+4)[r]
        assert difference == residue
        assert 1 <= i <= n and 1 <= j <= n
        assert 5*i > 3*n and 5*j > 3*n
        assert difference > 0 or n == 3
        assert n+i+j == 13*n//5+1
        counts += 1

    noise_cases = 0
    # Construct complete extremal archives, not just declared interval corners.
    for n in (2, 3, 4, 7, 11, 20):
        for ei in range(13):
            eps = Q(ei, 120)
            for ki in range(25):
                kappa = Q(ki, 120)
                step = kappa / (n-1)
                candidate_low = [(Q(3, 5)-eps-step*t,)*2 for t in range(n)]
                candidate_high = [(Q(3, 5)+eps+step*t,)*2 for t in range(n)]
                left_low = [(Q(0), 1-eps-step*t) for t in range(n)]
                left_high = [(eps+step*t, Q(1)) for t in range(n)]
                right_low = [(1-eps-step*t, Q(0)) for t in range(n)]
                right_high = [(Q(1), eps+step*t) for t in range(n)]
                sequences = [candidate_low, candidate_high, left_low,
                             left_high, right_low, right_high]
                for rows in sequences:
                    assert all(0 <= x <= 1 for row in rows for x in row)
                    assert all(abs(rows[t+1][c]-rows[t][c]) <= step
                               for t in range(n-1) for c in range(2))
                means = [tuple(sum(row[c] for row in rows)/n for c in range(2))
                         for rows in sequences]
                h = eps+kappa/2
                assert means == [(Q(3,5)-h,)*2, (Q(3,5)+h,)*2,
                                 (Q(0),1-h), (h,Q(1)),
                                 (1-h,Q(0)), (Q(1),h)]
                midpoint = tuple((means[3][c]+means[5][c])/2 for c in range(2))
                strict_separation = all(midpoint[c] < means[0][c] for c in range(2))
                expected = 2*eps+kappa < Q(2,15)
                assert strict_separation == expected
                if expected:
                    assert means[2][1] > means[1][1]
                    assert means[4][0] > means[1][0]
                else:
                    # Equal weights support candidate in a legal completion.
                    assert sum(means[3]) >= sum(means[0])
                    assert sum(means[5]) >= sum(means[0])
                noise_cases += 1

    result = {
        'status': 'PASS',
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'independent_of_producer_imports': True,
        'integer_constructive_cases': counts,
        'noise_extreme_archives_cases': noise_cases,
        'square_N3_exception': 9,
        'limitations': ['Finite arithmetic checks, not formal verification.',
                       'Does not claim positive-triangle exhaustive coverage.',
                       'Does not validate drift metadata on physical measurements.'],
    }
    out = Path(__file__).with_name('Dependent_Domain_Independent_Checks.json')
    out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
