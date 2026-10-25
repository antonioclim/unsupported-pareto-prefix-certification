"""Exact checks of the P21 dependence-aware certificate extension.

Own code; Python standard library only; no network, installation or radio data.
Exploratory checks, not preregistered discovery or a replacement for proof.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json


def dominates(q, p):
    return q[0] <= p[0] and q[1] <= p[1] and q != p


def unsupported(p, rivals):
    """Exact emptiness of intersection of supporting-weight intervals."""
    lo, hi = F(0), F(1)
    for q in rivals:
        d0, d1 = q[0] - p[0], q[1] - p[1]
        slope = d0 - d1
        if slope > 0:
            lo = max(lo, -d1 / slope)
        elif slope < 0:
            hi = min(hi, -d1 / slope)
        elif d1 < 0:
            return True
    return lo > hi


def good(p, rivals):
    return not any(dominates(q, p) for q in rivals) and unsupported(p, rivals)


def positive_ramp_sum(a, ell, count):
    if not ell:
        return count * a
    m = min(count, a // ell)
    return m * a - ell * m * (m + 1) / 2


def bounds(prefix, N, ell):
    if not prefix:
        return (F(0), F(0)), (F(1), F(1))
    remaining = N - len(prefix)
    sums = tuple(sum(row[c] for row in prefix) for c in range(2))
    lower = tuple((sums[c] + positive_ramp_sum(prefix[-1][c], ell, remaining)) / N for c in range(2))
    upper = tuple((sums[c] + remaining - positive_ramp_sum(1 - prefix[-1][c], ell, remaining)) / N for c in range(2))
    return lower, upper


def corner_true(boxes):
    la, ua = boxes[0]
    return not any(dominates(li, ua) for li, ui in boxes[1:]) and unsupported(la, [ui for li, ui in boxes[1:]])


def finite_domain_audit(triangle, denominator=2):
    N, ell = 2, F(1, denominator)
    levels = tuple(F(k, denominator) for k in range(denominator + 1))
    alphabet = [(x, y) for x, y in product(levels, repeat=2) if not triangle or y <= x]
    sequences = [x for x in product(alphabet, repeat=N) if all(abs(x[1][c] - x[0][c]) <= ell for c in range(2))]
    prefixes = sorted({seq[:s] for seq in sequences for s in range(N + 1)}, key=lambda x: (len(x), x))
    ids = {prefix: i for i, prefix in enumerate(prefixes)}
    pcount = len(prefixes)
    seq_ids = [[ids[seq[:s]] for s in range(N + 1)] for seq in sequences]
    means = [tuple(sum(row[c] for row in seq) / N for c in range(2)) for seq in sequences]
    boxes = [bounds(prefix, N, ell) for prefix in prefixes]
    # Independent finite completion extrema, not the ramp formula.
    for index, prefix in enumerate(prefixes):
        completion_means = [means[j] for j, seq in enumerate(sequences) if seq[:len(prefix)] == prefix]
        lo = tuple(min(p[c] for p in completion_means) for c in range(2))
        hi = tuple(max(p[c] for p in completion_means) for c in range(2))
        assert boxes[index] == (lo, hi)
        assert lo in completion_means and hi in completion_means
    flags = bytearray(pcount ** 3)
    positives = 0
    for ia, il, ir in product(range(len(sequences)), repeat=3):
        label = good(means[ia], [means[il], means[ir]])
        positives += label
        bit = 1 if label else 2
        for a, b, c in product(seq_ids[ia], seq_ids[il], seq_ids[ir]):
            flags[(a * pcount + b) * pcount + c] |= bit
    robust_true_count = 0
    for a, b, c in product(range(pcount), repeat=3):
        flag = flags[(a * pcount + b) * pcount + c]
        assert flag
        expected = flag == 1
        actual = corner_true([boxes[a], boxes[b], boxes[c]])
        assert actual == expected, (triangle, a, b, c, flag, actual)
        robust_true_count += actual
    return dict(domain="triangle" if triangle else "square", rows=N, coordinate_denominator=denominator, alphabet=len(alphabet), legal_group_sequences=len(sequences), complete_archives=len(sequences)**3, positive_archives=positives, prefix_states=pcount**3, robust_true_states=robust_true_count, exact_completion_and_corner_agreement=True)


def square_constant_true(N, a, i, j):
    # Independently derived integer inequalities for the constant archive.
    return 5*i > 5*N - 2*a and 5*j > 5*N - 2*a and 5*i*j > (5*N - 3*a)*(i+j)


def square_min_exhaustive(N):
    return min(a+i+j for a,i,j in product(range(1,N+1), repeat=3) if square_constant_true(N,a,i,j))


def square_min_linear_boundary(N):
    answer = 3*N
    argmin = (N,N,N)
    for a in range(1,N+1):
        safe = (5*N-2*a)//5 + 1
        q = 5*N-3*a
        for i in range(safe,N+1):
            denominator = 5*i-q
            if denominator <= 0:
                continue
            j = max(safe, q*i//denominator + 1)
            if j <= N and a+i+j < answer:
                answer, argmin = a+i+j, (a,i,j)
    return answer, argmin


def separation_audit():
    result = []
    for N in list(range(1,41)) + [64,100,121,200]:
        independent, argmin = square_min_linear_boundary(N)
        claimed = 9 if N == 3 else 13*N//5 + 1
        assert independent == claimed
        if N <= 12:
            assert square_min_exhaustive(N) == independent
        if N >= 2:
            ell = F(1,10*(N-1))
            first = [((F(3,5),F(3,5)),), ((F(0),F(1)),), ((F(1),F(0)),)]
            assert corner_true([bounds(p,N,ell) for p in first])
            # Any missing group has attainable all-zero/all-one counterexamples.
            for g in range(3):
                altered = first.copy()
                altered[g] = ()
                assert not corner_true([bounds(p,N,ell) for p in altered])
        result.append(dict(N=N,square_certificate=independent,square_argmin=argmin,smooth_certificate=3,ratio=str(F(independent,3))))
    return result


def measurement_margin_audit():
    results = []
    for kappa in [F(0),F(1,50),F(1,10),F(2,15),F(1,5)]:
        for eps in [F(0),F(1,100),F(1,60),F(1,50),F(1,10)]:
            d = kappa/2
            boxes = [((F(3,5)-eps-d,)*2, (F(3,5)+eps+d,)*2), ((F(0),1-eps-d),(eps+d,F(1))), ((1-eps-d,F(0)),(F(1),eps+d))]
            actual = corner_true(boxes)
            expected = 2*eps+kappa < F(2,15)
            assert actual == expected
            results.append(dict(kappa=str(kappa),epsilon=str(eps),robust_true=actual))
    # Same first rows; sharp failure at the threshold.
    N, kappa = 11, F(2,15)
    ell = kappa/(N-1)
    candidate = tuple((F(3,5)-ell*t,)*2 for t in range(N))
    left = tuple((ell*t,F(1)) for t in range(N))
    right = tuple((F(1),ell*t) for t in range(N))
    means = [tuple(sum(row[c] for row in seq)/N for c in range(2)) for seq in [candidate,left,right]]
    assert means[0] == (F(8,15),F(8,15))
    assert means[1] == (F(1,15),F(1))
    assert means[2] == (F(1),F(1,15))
    assert not good(means[0],means[1:])
    assert not any(dominates(p,means[0]) for p in means[1:])
    return dict(parameter_checks=results,sharp_false_completion={"N":N,"kappa":str(kappa),"means":[[str(v) for v in p] for p in means],"supported_at_equal_weights":True})


def main():
    output = dict(status="PASS",scope="Exact synthetic mathematical checks only",source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),finite_domains=[finite_domain_audit(False),finite_domain_audit(True),finite_domain_audit(True,4)],separation=separation_audit(),measurement_margin=measurement_margin_audit())
    target = Path(__file__).with_name("Lipschitz_Certificate_Checks.json")
    target.write_text(json.dumps(output,indent=2)+"\n")
    print(json.dumps({"status":output["status"],"finite_domains":output["finite_domains"],"separation_cases":len(output["separation"]),"measurement_cases":len(output["measurement_margin"]["parameter_checks"]),"output":str(target)},indent=2))


if __name__ == "__main__":
    main()
