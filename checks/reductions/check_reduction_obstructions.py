"""Exact finite checks for two explicitly stated obstructions to simple reductions.

This does not exclude arbitrary reductions or verify all manuscript theorems.
Only Python's standard library is used; no existing project verifier is imported.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json

def dominates(x, y):
    return all(a <= b for a, b in zip(x, y)) and x != y

def supported(candidate, rivals):
    # A normalised nonnegative weight is (lambda, 1-lambda), lambda in [0,1].
    lo, hi = F(0), F(1)
    for rival in rivals:
        d0, d1 = (a-b for a, b in zip(candidate, rival))
        slope = d0-d1
        if slope == 0:
            if d1 > 0:
                return False
        elif slope > 0:
            hi = min(hi, -d1/slope)
        else:
            lo = max(lo, -d1/slope)
    return lo <= hi

def good(points):
    return (not any(dominates(p, points[0]) for p in points[1:])
            and not supported(points[0], points[1:]))

def means(archive):
    n = len(archive[0])
    return [tuple(sum(row[d] for row in rows)/n for d in (0,1))
            for rows in archive]

def true_prefix(archive, b):
    n = len(archive[0])
    lows = [tuple(sum((row[d] for row in rows[:length]), F(0))/n
                  for d in (0,1)) for rows, length in zip(archive, b)]
    highs = [tuple(v+F(n-length,n) for v in low)
             for low,length in zip(lows,b)]
    return (not any(dominates(low,highs[0]) for low in lows[1:])
            and not supported(lows[0],highs[1:]))

def certificate(archive):
    n = len(archive[0])
    states = [(b,sum(b)) for b in product(range(n+1), repeat=len(archive))
              if true_prefix(archive,b)]
    assert states
    cost = min(cost for _,cost in states)
    return cost, [list(b) for b,c in states if c==cost], len(states)

def main():
    # Known candidate; three observed rival rows sum to (0,5/2) and (5/2,0).
    a = [(F(1,2),F(1,2))]*4
    nw = [(F(0),F(5,6))]*3
    se = [(F(5,6),F(0))]*3
    zero,one = (F(0),F(0)),(F(1),F(1))
    worlds = [[a,nw+[last],se+[last]] for last in (zero,one)]
    points = [means(w) for w in worlds]
    assert good(points[0]) and not good(points[1])
    assert all(not any(dominates(q,p) for q in ps if q != p)
               for ps in points for p in ps)
    assert not true_prefix(worlds[0],(4,3,3))
    # Across all legal completions, opposite-separated rectangles ensure
    # the same three Pareto labels; the universal argument is analytic.
    a3 = [(F(99,100),F(299,1000))]*3
    c3 = [(F(1),F(0))]*3
    v = (F(9,10),F(9,10))
    original = [a3,[zero,v,v],c3]
    reordered = [a3,[v,zero,v],c3]
    assert means(original) == means(reordered)
    assert good(means(original))
    first,second = certificate(original),certificate(reordered)
    assert first[0]==8 and second[0]==7
    result = {
      "status":"PASS",
      "arithmetic":"fractions.Fraction; no floating point",
      "support_test":"exact closed interval intersection, including axes and ties",
      "same_pareto_labels_different_good":{
        "K":3,"N":4,"prefix":[4,3,3],
        "means":[[[str(c) for c in p] for p in ps] for ps in points],
        "GOOD":[True,False],
        "scope":"two exact completions; universal Pareto-label invariance follows analytically from rectangle separation"
      },
      "same_means_different_prefix_cost":{
        "K":3,"N":3,"prefix_states_examined":128,
        "original":{"cost":first[0],"minimisers":first[1],"true_states":first[2]},
        "reordered":{"cost":second[0],"minimisers":second[1],"true_states":second[2]}
      },
      "limit":"Checks only the two claimed simple-reduction obstructions; not a universal non-reducibility result.",
      "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    }
    Path(__file__).with_name("Reduction_Obstructions_Exact_Check.json").write_text(
        json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))

if __name__=="__main__":
    main()
