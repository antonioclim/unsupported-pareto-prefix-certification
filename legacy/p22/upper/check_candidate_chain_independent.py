"""Independent exact audit of the candidate/NW hidden-chain lower family.

Integer corners, P2 and strict crossing determinants; no producer imports.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json


def construct(q, pad, world):
    n0, n = 4 * q, 4 * q + pad
    zeros = [(0, 0)] * pad
    rows = [zeros + [(3, 1)] * (3 * q) + [(0, 0)] * q,
            zeros + [(1, 1)] * (3 * q) + [(3, 3)] * q,
            zeros + [(3, 0)] * n0]
    if world == "A":
        rows[1][-1] = (0, 0)
    else:
        rows[0][-1] = (3, 0)
    sums = []
    for group in rows:
        s = [(0, 0)]
        for c, f in group:
            s.append((s[-1][0] + c, s[-1][1] + f))
        sums.append(s)
    return n, sums


def robust_true(n, sums, state):
    lower = [sums[k][state[k]] for k in range(3)]
    upper = [tuple(v + 3 * (n - state[k]) for v in lower[k]) for k in range(3)]
    p, up = lower[0], upper[0]
    if any(r[0] <= up[0] and r[1] <= up[1] and r != up for r in lower[1:]):
        return False
    nw = next((r for r in upper[1:] if r[0] < p[0] and r[1] > p[1]), None)
    se = next((r for r in upper[1:] if r[0] > p[0] and r[1] < p[1]), None)
    return nw is not None and se is not None and (
        (p[0] - nw[0]) * (p[1] - se[1]) > (nw[1] - p[1]) * (se[0] - p[0]))


def main():
    records, checked = [], 0
    for q, pad in [(3, 0), (3, 1), (3, 3), (4, 0), (5, 2), (8, 1)]:
        for world in ("A", "B"):
            n, sums = construct(q, pad, world)
            actual = [s for s in product(range(n + 1), repeat=3) if robust_true(n, sums, s)]
            if world == "A":
                expected = [(a, n, j) for a in range(pad + 3 * q + 2, n + 1)
                            for j in range(n - 1, n + 1)]
                cost = 3 * n - q + 1
            else:
                expected = [(n, i, j) for i in range(pad + 3 * q + 1, n + 1)
                            for j in range(n - 1, n + 1)]
                cost = 3 * n - q
            assert actual == expected, (q, pad, world, actual, expected)
            assert min(map(sum, actual)) == cost
            checked += (n + 1) ** 3
            records.append({"q": q, "padding": pad, "N": n, "world": world,
                            "TRUE_states": actual, "minimum_cost": cost})
    n, sums = construct(2, 0, "B")
    assert not robust_true(n, sums, (8, 7, 7))
    assert robust_true(n, sums, (8, 7, 8))

    balance = []
    for q, pad in product(range(3, 40), range(4)):
        n = 4 * q + pad
        w, x, y = 3 * n - 2 * q + 2, q - 2, q - 1
        denominator = x * (w + x) + y * (w + y)
        theta = Q(y * (w + y), denominator)
        ratio = 1 + Q(x * y, denominator)
        assert (w + y + theta * x) / Q(w + y) == ratio
        assert (w + x + (1 - theta) * y) / Q(w + x) == ratio
        assert ratio == 1 + Q((q - 2) * (q - 1),
                             (q - 2) * (3 * n - q) + (q - 1) * (3 * n - q + 1))
        if pad == 0:
            assert ratio == 1 + Q((q - 2) * (q - 1), 22 * q * q - 32 * q - 1)
        balance.append({"q": q, "padding": pad, "ratio": str(ratio),
                        "candidate_first_probability": str(theta)})
    report = {"status": "PASS", "checker": "independent integer P2 and crossing determinant",
              "prefix_states_checked": checked, "world_cases": records,
              "q2_boundary_control": {"B_8_7_7": False, "B_8_7_8": True,
                                       "interpretation": "q>=3 is necessary for the claimed SE threshold"},
              "balance_cases_checked": len(balance), "balance": balance,
              "scope": "Full prefix enumeration of six pairs, including leading-zero padding; does not prove universal parameters or historical novelty."}
    Path(__file__).with_name("Candidate_Chain_Independent_Check.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "prefix_states_checked": checked,
                      "balance_cases_checked": len(balance)}))


if __name__ == "__main__":
    main()
