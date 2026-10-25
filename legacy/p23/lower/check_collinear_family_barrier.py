#!/usr/bin/env python3
"""Finite rational checks for a sharply delimited asymptotic family barrier."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def main():
    count = 0
    max_random = F(1)
    max_det = F(1)
    equality = []
    for li in range(1, 40):
        l = F(li, 40)
        for ci in range(li+1, 40):
            c = F(ci, 40)
            f = l*(1-c)/(1-l)
            x = l-f
            if not 0 < f < l < c < 1:
                continue
            for ta in range(1, 9):
                t = F(ta, 8)*min(1-c, x)
                for sa in range(1, 9):
                    s = F(sa, 8)*x
                    resource = s/l+t/(1-l)
                    assert resource <= 1
                    # Equivalent squared form, avoiding irrational arithmetic.
                    assert 1-s-t >= 0 and (1-s-t)**2 >= 4*s*t
                    assert 1/t+1/s >= 8
                    excess = t*s/(t*(3-s)+s*(3-t))
                    deterministic = min(t, s)/(3-min(t, s))
                    assert excess <= F(1, 22)
                    assert deterministic <= F(1, 11)
                    max_random = max(max_random, 1+excess)
                    max_det = max(max_det, 1+deterministic)
                    if excess == F(1, 22) or deterministic == F(1, 11):
                        assert (t, s, l, c, f) == (F(1,4), F(1,4), F(1,2), F(3,4), F(1,4))
                        equality.append([str(z) for z in (t, s, l, c, f)])
                    count += 1
    assert max_random == F(23, 22) and max_det == F(12, 11)
    assert equality
    result = dict(status='PASS', parameter_cases=count,
                  maximum_randomised_restricted_pair_ratio=str(max_random),
                  maximum_deterministic_restricted_pair_ratio=str(max_det),
                  equality_skeletons=equality,
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  proof_sha256=hashlib.sha256((ROOT/'Collinear_Two_Chain_Family_Barrier_P23.md').read_bytes()).hexdigest(),
                  global_acquisition_optimality_claimed=False,
                  scope='Finite exact rational grid corroboration; the universal restricted-family proof is analytic.')
    (ROOT/'Collinear_Family_Barrier_Exact_Check.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
