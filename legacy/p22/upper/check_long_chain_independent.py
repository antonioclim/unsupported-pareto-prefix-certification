"""Independent exact integer audit of the long-chain construction.

Uses strict crossing determinants after P2, rather than the producer's
support-interval checker. Does not import producer code or retained outputs.
"""
import hashlib
import json
from itertools import product
from pathlib import Path


def full_case(x, y, q, padding):
    d = x * x + 2 * x * y + 2 * y * y
    n0, scale = d * q, 2 * d
    n = n0 + padding
    ell_l, ell_r = 2 * y * (x + y) * q, (x + y) ** 2 * q
    assert y * y * q > 1
    candidate = (2 * (x + y) ** 2, 2 * y * (x + y))
    zero, one = (0, 0), (scale, scale)
    prefix = [zero] * padding
    out = []
    for winner in (1, 2):
        rows = [prefix + [candidate] * n0,
                prefix + [(d, d)] * ell_l + [one] * (n0 - ell_l),
                prefix + [(scale, 0)] * ell_r + [one] * (n0 - ell_r)]
        rows[winner][-1] = zero
        sums = []
        for group in rows:
            s = [(0, 0)]
            for c, f in group:
                s.append((s[-1][0] + c, s[-1][1] + f))
            sums.append(s)
        true_states = []
        for state in product(range(n + 1), repeat=3):
            lower = [sums[k][state[k]] for k in range(3)]
            upper = [tuple(v + scale * (n - state[k]) for v in lower[k])
                     for k in range(3)]
            p, up = lower[0], upper[0]
            if any(r[0] <= up[0] and r[1] <= up[1] and r != up
                   for r in lower[1:]):
                continue
            nw = next((r for r in upper[1:] if r[0] < p[0] and r[1] > p[1]), None)
            se = next((r for r in upper[1:] if r[0] > p[0] and r[1] < p[1]), None)
            if nw is None or se is None:
                continue
            if (p[0] - nw[0]) * (p[1] - se[1]) > (nw[1] - p[1]) * (se[0] - p[0]):
                true_states.append(state)
        if winner == 1:
            expected = [(n, n, j) for j in range(padding + ell_r + 1, n + 1)]
        else:
            expected = [(n, i, n) for i in range(padding + ell_l + 1, n + 1)]
        assert true_states == expected, (x, y, q, padding, winner, true_states, expected)
        out.append({"winner": winner, "TRUE_states": true_states,
                    "minimum_cost": min(map(sum, true_states))})
    return {"x": x, "y": y, "q": q, "padding": padding, "N": n,
            "prefix_states_checked": 2 * (n + 1) ** 3, "worlds": out}


def main():
    cases = [full_case(*parameters) for parameters in
             [(1, 1, 2, 0), (1, 1, 2, 1), (2, 1, 2, 0), (3, 2, 1, 1)]]
    proof = Path(__file__).resolve().parents[1] / "lower" / "Nonvanishing_Triangular_Lower_Bounds_P22.md"
    report = {"status": "PASS", "independent_checker": "integer strict crossing determinant after P2",
              "proof_sha256": hashlib.sha256(proof.read_bytes()).hexdigest(),
              "cases": cases, "prefix_states_checked": sum(c["prefix_states_checked"] for c in cases),
              "scope": "Entire prefix grids of four rational two-world families; not all-parameter proof or formal verification."}
    Path(__file__).with_name("Long_Chain_Independent_Check.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "prefix_states_checked": report["prefix_states_checked"]}))


if __name__ == "__main__":
    main()
