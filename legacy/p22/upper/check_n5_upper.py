"""Own stdlib exact checks for the N=5 triangular upper proof.

No external data/code, approximate arithmetic or solver is used.
Finite checks accompany, rather than replace, the continuous-domain proof.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json


def feasible(a, i, j):
    z = i + 2 * j + 2 * a - 20
    return z > 0 and z * z > 4 * (10 - a - i) * (10 - a - j)


def main():
    shapes = [v for v in product(range(1, 6), repeat=3) if feasible(*v)]
    minimal = [v for v in shapes if not any(
        w != v and all(x <= y for x, y in zip(w, v)) for w in shapes)]
    assert minimal == [(4, 5, 5), (5, 1, 5), (5, 5, 3)]
    assert [v for v in shapes if v[0] < 5] == [(4, 5, 5)]
    assert not any(v[1] < 5 and v[2] < 5 for v in shapes)
    assert min(map(sum, shapes)) == 11
    classes = {k: [v for v in shapes if sum(v) == k] for k in range(11, 16)}
    assert classes[11] == [(5, 1, 5)]
    assert classes[12] == [(5, 2, 5)]
    assert set(classes[13]) == {(5, 3, 5), (5, 5, 3)}
    assert set(classes[14]) == {(4, 5, 5), (5, 4, 5), (5, 5, 4)}
    assert classes[15] == [(5, 5, 5)]

    # Inner rival acquisition envelopes. Each pair lists row costs under
    # NW-first and SE-first. Other positive certificates can only shorten.
    inner = {
        "NW3_SE5": (15, 13, 13),
        "NW4_SE5": (15, 14, 14),
        "NW5_SE4": (14, 15, 14),
    }
    inner_results = {}
    for name, (nw, se, optimum) in inner.items():
        expected = Q(nw, 4) + Q(3 * se, 4)
        assert expected <= (Q(27, 2) if optimum == 13 else Q(59, 4))
        inner_results[name] = {
            "NW_first": nw, "SE_first": se,
            "expected": str(expected), "minimum_certificate": optimum}

    # (certificate row cost, A bound, B bound)
    cost_classes = [
        (11, Q(11), Q(15)), (12, Q(12), Q(15)),
        (13, Q(27, 2), Q(15)), (14, Q(59, 4), Q(15)),
        (14, Q(15), Q(14)), (15, Q(15), Q(15))]
    setup_values = sorted(set([Q(0), Q(1, 1000), Q(1, 10), Q(1), Q(5),
                               Q(11), Q(14), Q(100), Q(1000000)] +
                              [Q(a, b) for a in range(16) for b in range(1, 9)]))
    mixtures = []
    for F in setup_values:
        d = 5 * F + 67
        p = 4 * (F + 14) / d
        target = 1 + 4 / d
        ratios = [(F + p * a + (1 - p) * b) / (F + c)
                  for c, a, b in cost_classes]
        assert max(ratios) == target
        assert ratios[0] == ratios[4] == target
        assert all(r < target for i, r in enumerate(ratios) if i not in (0, 4))
        assert all((F + c) / (F + c) <= 1 + 1 / (F + 14)
                   for c in (11, 12, 13, 15))
        assert (F + 15) / (F + 14) == 1 + 1 / (F + 14)
        mixtures.append({"F": str(F), "p_A": str(p), "ratio": str(target)})
    report = {
        "status": "PASS",
        "scope": "Exact finite shape and policy-envelope checks; analytic proof is separate.",
        "row_domain": "0<=f<=c<=1", "configurations": 3, "rows": 5,
        "length_triples_checked": 125, "feasible_length_triples": len(shapes),
        "minimal_oriented_shapes": minimal,
        "certificate_cost_classes": {str(k): v for k, v in classes.items()},
        "inner_policy_expected_costs": inner_results,
        "setup_values_checked": len(setup_values), "mixtures": mixtures,
        "unit_randomised_upper": "71/67", "unit_deterministic_upper": "15/14",
        "historical_priority": "NOT_ASSESSED", "physical_measurements": 0,
        "formal_verification": False}
    out = Path(__file__).with_name("N5_Upper_Exact_Check.json")
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in (
        "status", "length_triples_checked", "feasible_length_triples",
        "setup_values_checked", "unit_randomised_upper", "unit_deterministic_upper")}))


if __name__ == "__main__":
    main()
