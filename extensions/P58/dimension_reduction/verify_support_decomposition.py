"""Finite corroboration; the convex-geometric argument supplies the proof.

Compare exact rational feasibility on every objective pair, a separately coded
exact interval test across all objectives, and an independent full-dimensional
floating-point LP for two rivals. No performance benchmark.
"""
from fractions import Fraction
from itertools import combinations
import json
import platform
import random

import numpy as np
import scipy
from scipy.optimize import linprog


def pair_feasible(differences, first, second):
    lower, upper = Fraction(0), Fraction(1)
    for row in differences:
        intercept = Fraction(row[second])
        slope = Fraction(row[first] - row[second])
        if slope == 0:
            if intercept < 0:
                return False
        elif slope > 0:
            lower = max(lower, -intercept / slope)
        else:
            upper = min(upper, -intercept / slope)
    return lower <= upper


def unsupported_interval(differences):
    """Solve lambda*v1_i+(1-lambda)*v2_i<0 for every i, exactly.

    The original simplex interval [0,1] is closed; each objective contributes
    a strict half-line. Endpoint inclusion is retained explicitly.
    """
    lower, upper = Fraction(0), Fraction(1)
    lower_closed, upper_closed = True, True
    for first, second in zip(*differences):
        slope = Fraction(first - second)
        right = Fraction(-second)
        if slope == 0:
            if right <= 0:
                return False, {"reason": "constant strict inequality is impossible"}
            continue
        threshold = right / slope
        if slope > 0:
            if threshold < upper:
                upper, upper_closed = threshold, False
            elif threshold == upper:
                upper_closed = False
        else:
            if threshold > lower:
                lower, lower_closed = threshold, False
            elif threshold == lower:
                lower_closed = False
    feasible = lower < upper or (lower == upper and lower_closed and upper_closed)
    return feasible, {
        "lower": str(lower), "lower_closed": lower_closed,
        "upper": str(upper), "upper_closed": upper_closed,
    }


def boundary_controls():
    # Expected answers and endpoint behaviour are specified independently.
    controls = [
        ("lambda_one_is_included", [[-1, -2], [2, 3]], True,
         {"lower": "2/3", "lower_closed": False, "upper": "1", "upper_closed": True}),
        ("lambda_zero_is_included", [[2, 3], [-1, -2]], True,
         {"lower": "0", "lower_closed": True, "upper": "1/3", "upper_closed": False}),
        ("opposing_strict_intervals_meet", [[1, -1], [-1, 1]], False,
         {"lower": "1/2", "lower_closed": False, "upper": "1/2", "upper_closed": False}),
        ("constant_coordinate_tie", [[-1, 0], [-1, 0]], False,
         {"reason": "constant strict inequality is impossible"}),
        ("constant_negative_coordinates", [[-1, -2], [-1, -3]], True,
         {"lower": "0", "lower_closed": True, "upper": "1", "upper_closed": True}),
        ("closed_relaxation_only_lambda_zero", [[1, -1], [0, -1]], False,
         {"lower": "0", "lower_closed": True, "upper": "0", "upper_closed": False}),
        ("closed_relaxation_only_lambda_one", [[0, -1], [1, -1]], False,
         {"lower": "1", "lower_closed": False, "upper": "1", "upper_closed": True}),
        ("nonempty_open_interval", [[1, -3], [-3, 1]], True,
         {"lower": "1/4", "lower_closed": False, "upper": "3/4", "upper_closed": False}),
        ("nonempty_narrow_rational_interval", [[3, -7], [-2, 4]], True,
         {"lower": "4/11", "lower_closed": False, "upper": "2/5", "upper_closed": False}),
    ]
    results = []
    for name, differences, expected, expected_bounds in controls:
        actual, bounds = unsupported_interval(differences)
        pair_support = pair_feasible(differences, 0, 1)
        if actual != expected or bounds != expected_bounds or pair_support == actual:
            raise AssertionError((name, actual, bounds, pair_support))
        results.append({"name": name, "unsupported": actual, "bounds": bounds, "passed": True})
    return results


def main():
    seed = 20261025
    dimensions = [2, 3, 5, 20, 50]
    rng = random.Random(seed)
    totals = {"total": 0, "supported": 0, "unsupported": 0,
              "mismatches": 0, "exact_interval_mismatches": 0}
    by_dimension = []
    for dimension in dimensions:
        counts = {key: 0 for key in totals}
        cases = []
        for _ in range(200):
            cases.append(("random", [
                [rng.randint(-9, 9) for _ in range(dimension)]
                for _ in range(2)
            ]))
        for _ in range(100):
            first = [rng.randint(-9, 9) for _ in range(dimension)]
            cases.append(("strictly_unsupported", [first, [-x - 1 for x in first]]))
        for _ in range(100):
            columns = [(2, -1), (-1, 2)]
            for _ in range(dimension - 2):
                scale = rng.randint(1, 4)
                sign = rng.choice([0, 1])
                base = (2, -1) if sign == 0 else (-1, 2)
                columns.append(tuple(scale * x for x in base))
            cases.append(("supported_without_axis_support", [list(row) for row in zip(*columns)]))
        family_counts = {}
        for family, differences in cases:
            exact = any(
                pair_feasible(differences, first, second)
                for first, second in combinations(range(dimension), 2)
            )
            interval_unsupported, _ = unsupported_interval(differences)
            full = linprog(
                np.zeros(dimension),
                A_ub=-np.array(differences, dtype=float), b_ub=np.zeros(2),
                A_eq=np.ones((1, dimension)), b_eq=np.ones(1),
                bounds=(0, None), method="highs",
            )
            if full.status not in (0, 2):
                raise RuntimeError(full.message)
            if family == "strictly_unsupported" and exact:
                raise AssertionError("A fixed strictly negative rival mixture must preclude support")
            if family == "supported_without_axis_support" and not exact:
                raise AssertionError("The first two columns admit a supporting mixture")
            counts["total"] += 1
            counts["supported" if exact else "unsupported"] += 1
            counts["mismatches"] += exact != bool(full.success)
            counts["exact_interval_mismatches"] += exact == interval_unsupported
            family_counts[family] = family_counts.get(family, 0) + 1
        for key in totals:
            totals[key] += counts[key]
        by_dimension.append({"dimension": dimension, **counts, "families": family_counts})
    result = {
        "test": "Exact objective-pair support, exact all-objective interval, and full-dimensional numerical LP",
        "rivals": 2, "seed": seed,
        "cases_per_dimension": 400,
        "python": platform.python_version(), "scipy": scipy.__version__,
        "by_dimension": by_dimension, **totals,
        "scope": "Synthetic corroboration; not a proof, deployed test or runtime benchmark.",
        "reference_method": "Full-dimensional SciPy/HiGHS LP uses floating-point arithmetic.",
        "interval_method": "Independent rational strict-interval intersection; O(d) rational operations.",
        "boundary_controls": boundary_controls(),
    }
    print(json.dumps(result, indent=2))
    if totals["mismatches"] or totals["exact_interval_mismatches"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
