"""Exact finite control of the rank-two positive-catalogue corollary.

Uses rational interval feasibility for a strict mixture of two rivals; no LP
solver and no floating-point tolerance. This is a finite control, not a proof.
"""
from fractions import Fraction as Q
from itertools import product, combinations
from pathlib import Path
import json


def dominates(a, b):
    return all(x <= y for x, y in zip(a, b)) and any(x < y for x, y in zip(a, b))


def unsupported(a, rivals):
    b, c = rivals
    lo, hi = Q(0), Q(1)
    for ai, bi, ci in zip(a, b, c):
        coefficient, rhs = bi - ci, ai - ci
        if coefficient == 0:
            if rhs <= 0:
                return False
        elif coefficient > 0:
            hi = min(hi, Q(rhs, coefficient))
        else:
            lo = max(lo, Q(rhs, coefficient))
    if lo > hi:
        return False
    mixture_weight = (lo + hi) / 2
    return 0 <= mixture_weight <= 1 and all(
        mixture_weight * bi + (1 - mixture_weight) * ci < ai
        for ai, bi, ci in zip(a, b, c)
    )


def catalogue_facts(points):
    relation = tuple(dominates(a, b) for a in points for b in points)
    support = tuple(
        not unsupported(a, [b for j, b in enumerate(points) if j != i])
        for i, a in enumerate(points)
    )
    nondominated = tuple(
        not any(dominates(b, a) for j, b in enumerate(points) if j != i)
        for i, a in enumerate(points)
    )
    return relation, support, nondominated


def main():
    points = list(product(range(4), repeat=3))
    positive = tested = 0
    failures = []
    for catalogue in combinations(points, 3):
        tested += 1
        full = catalogue_facts(catalogue)
        if not any(n and not s for n, s in zip(full[2], full[1])):
            continue
        positive += 1
        valid_projection = False
        for coordinates in combinations(range(3), 2):
            reduced = tuple(tuple(p[j] for j in coordinates) for p in catalogue)
            if catalogue_facts(reduced) == full:
                valid_projection = True
                break
        if not valid_projection:
            failures.append(catalogue)
    result = {
        "arithmetic": "exact fractions",
        "grid": [0, 1, 2, 3],
        "objectives": 3,
        "unordered_three_alternative_catalogues": tested,
        "catalogues_with_GOOD": positive,
        "failures_of_two_original_coordinate_representation": len(failures),
        "first_failure": failures[:1],
        "scope": "finite control, not the universal proof or an online cost theorem",
    }
    assert tested == 41664 and positive == 423 and not failures
    destination = Path(__file__).with_name("three_alternative_projection_control.json")
    destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
