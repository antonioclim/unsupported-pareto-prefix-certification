"""Finite counterexample search for the P30 certificate-transfer criterion.

Enumerates every Boolean function and nonempty restricted input class on three
independently queryable bits. Tests certificates by compatible-input masks, and
compares minimum prices using only the separating integer tariffs in the proof.
This is a finite check, not a proof of the general theorem.
"""
from itertools import product
import json

n = 3
m = 1 << n
universe = (1 << m) - 1
subsets = range(1 << n)
compatible = [[sum(1 << y for y in range(m) if (x & q) == (y & q))
               for q in subsets] for x in range(m)]
tariffs = [tuple(1 if q & (1 << j) else n + 1 for j in range(n))
           for q in subsets]
costs = [[sum(w[j] for j in range(n) if q & (1 << j))
          for q in subsets] for w in tariffs]
cases = positive_instances = equal_classes = strict_classes = 0

for positive_mask in range(1, universe + 1):
    cert_y = [[q for q in subsets
               if compatible[x][q] & ~positive_mask == 0]
              for x in range(m)]
    for restricted in range(1, universe + 1):
        scored = restricted & positive_mask
        if not scored:
            continue
        cases += 1
        all_family_equal = True
        all_price_equal = True
        for x in range(m):
            if not scored & (1 << x):
                continue
            positive_instances += 1
            cert_x = [q for q in subsets
                      if compatible[x][q] & restricted & ~positive_mask == 0]
            family_equal = cert_x == cert_y[x]
            price_equal = all(min(c[q] for q in cert_x) ==
                              min(c[q] for q in cert_y[x]) for c in costs)
            if family_equal != price_equal:
                raise AssertionError((positive_mask, restricted, x,
                                      cert_x, cert_y[x]))
            all_family_equal &= family_equal
            all_price_equal &= price_equal
        assert all_family_equal == all_price_equal
        equal_classes += int(all_family_equal)
        strict_classes += int(not all_family_equal)

# Independent explicit unit-price counterexample, coordinates in listed order.
ys = list(product((0, 1), repeat=3))
xs = [a for a in ys if a[2] == (a[0] or a[1])]
positives = [a for a in xs if a[0] or a[1]]
def certificate_sets(cls, a):
    return [q for q in subsets if all(
        b[0] or b[1] for b in cls
        if all(a[j] == b[j] for j in range(n) if q & (1 << j)))]
example = []
for a in positives:
    cx, cy = certificate_sets(xs, a), certificate_sets(ys, a)
    unit_x = min(q.bit_count() for q in cx)
    unit_y = min(q.bit_count() for q in cy)
    wx = min(sum((4, 4, 1)[j] for j in range(n) if q & (1 << j)) for q in cx)
    wy = min(sum((4, 4, 1)[j] for j in range(n) if q & (1 << j)) for q in cy)
    assert unit_x == unit_y == 1
    assert wx == 1 and wy == 4
    assert 4 in cx and 4 not in cy  # the third bit alone
    example.append({"input": a, "unit_CX": unit_x, "unit_CY": unit_y,
                    "weighted_CX": wx, "weighted_CY": wy})

print(json.dumps({"status": "PASS", "bits": n,
    "function_restriction_cases": cases,
    "positive_instance_cases": positive_instances,
    "certificate_preserving_cases": equal_classes,
    "certificate_changing_cases": strict_classes,
    "separating_tariffs": tariffs,
    "unit_price_counterexample": example,
    "scope": "finite certificate/price equivalence and explicit counterexample; not policy or infinite-input proof"}, indent=2))
