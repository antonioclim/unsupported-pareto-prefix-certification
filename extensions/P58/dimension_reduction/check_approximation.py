"""Exact finite controls for approximation.md; not a proof or performance benchmark."""
from fractions import Fraction as F
import json
import random


def nondominated(a, rivals):
    return not any(all(x <= y for x, y in zip(r, a)) and any(x < y for x, y in zip(r, a)) for r in rivals)


def mixture_gap(a, rivals, weights):
    return min(x - sum(w * r[i] for w, r in zip(weights, rivals)) for i, x in enumerate(a))


def supported_by(a, rivals, weight):
    return all(sum(w * (r[i] - a[i]) for i, w in enumerate(weight)) >= 0 for r in rivals)


def main():
    rng = random.Random(20261025)
    z_a = (F(3, 5), F(3, 5))
    z_rivals = [(F(1, 5), F(4, 5)), (F(4, 5), F(1, 5))]
    weights = [F(1, 2), F(1, 2)]
    epsilon = F(1, 25)
    tested = {}
    minimum_gap = None
    for d in (2, 5, 20, 50):
        for _ in range(100):
            alphas = [F(1), F(0)] + [F(rng.randrange(101), 100) for _ in range(d - 2)]
            true_vectors = []
            for z in [z_a] + z_rivals:
                vector = []
                for i, alpha in enumerate(alphas):
                    residual = F(0) if i < 2 else epsilon * F(rng.randrange(-100, 101), 100)
                    vector.append(alpha * z[0] + (1 - alpha) * z[1] + residual)
                true_vectors.append(vector)
            a, rivals = true_vectors[0], true_vectors[1:]
            assert nondominated(a, rivals)
            gap = mixture_gap(a, rivals, weights)
            assert gap >= F(1, 10) - 2 * epsilon > 0
            minimum_gap = gap if minimum_gap is None else min(minimum_gap, gap)
        tested[str(d)] = 100

    # The two-anchor bound fails precisely at its non-strict boundary.
    a = list(z_a) + [F(11, 20)]
    rivals = [list(z) + [F(11, 20)] for z in z_rivals]
    assert nondominated(a, rivals)
    assert supported_by(a, rivals, [F(0), F(0), F(1)])
    assert mixture_gap(a, rivals, weights) == 0

    # The general coordinatewise 2*epsilon unsupportedness threshold is sharp.
    boundary_epsilon = F(1, 20)
    a_hat = [F(1, 2), F(1, 2)]
    rivals_hat = [[F(1, 10), F(7, 10)], [F(7, 10), F(1, 10)]]
    a = [F(9, 20), F(9, 20)]
    rivals = [[F(3, 20), F(3, 4)], [F(3, 4), F(3, 20)]]
    assert mixture_gap(a_hat, rivals_hat, weights) == 2 * boundary_epsilon
    assert all(max(r[i] - a_hat[i] for i in range(2)) > 2 * boundary_epsilon for r in rivals_hat)
    assert all(abs(x-y) <= boundary_epsilon for old, new in zip([a_hat] + rivals_hat, [a] + rivals) for x, y in zip(old, new))
    assert nondominated(a, rivals)
    assert supported_by(a, rivals, [F(1, 2), F(1, 2)])
    assert mixture_gap(a, rivals, weights) == 0

    # The same 2*epsilon threshold for strict nondomination witnesses is sharp.
    rivals_hat = [[F(1, 10), F(3, 5)], [F(3, 5), F(1, 10)]]
    a = [F(11, 20), F(11, 20)]
    r = [F(11, 20), F(1, 20)]
    assert mixture_gap(a_hat, rivals_hat, weights) > 2 * boundary_epsilon
    assert max(rivals_hat[1][i] - a_hat[i] for i in range(2)) == 2 * boundary_epsilon
    assert all(abs(x-y) <= boundary_epsilon for old, new in [(a_hat, a), (rivals_hat[1], r)] for x, y in zip(old, new))
    assert not nondominated(a, [r])

    # A projected tie is not an adequate nondomination witness under residuals.
    a = [F(1, 2), F(1, 2), F(3, 5)]
    r = [F(1, 2), F(1, 2), F(2, 5)]
    assert nondominated(a[:2], [r[:2]])
    assert not nondominated(a, [r])

    print(json.dumps({
        "status": "passed",
        "arithmetic": "fractions.Fraction, exact rational",
        "seed": 20261025,
        "two_anchor_positive_controls_by_dimension": tested,
        "smallest_observed_positive_mixture_gap": str(minimum_gap),
        "analytic_uniform_gap_lower_bound": str(F(1, 10) - 2 * epsilon),
        "boundary_and_tie_controls": 4,
        "limitations": "Finite synthetic controls only; proofs are in approximation.md. No timing, real data or paid-access efficiency measured."
    }, indent=2))


if __name__ == "__main__":
    main()
