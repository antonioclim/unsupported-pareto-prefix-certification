#!/usr/bin/env python3
"""Deterministic finite controls for the dimension-reduction research note.

All logical controls use fractions.Fraction. Optional SciPy checks are explicitly
floating-point cross-checks, not exact certificates or proofs of universal claims.
No manuscript, remote repository, or external service is modified.
"""
from __future__ import annotations

from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from pathlib import Path
import json
import random
import time

SEED = 20261025
ROOT = Path(__file__).resolve().parent


def dominates(x, y):
    return all(a <= b for a, b in zip(x, y)) and any(a < b for a, b in zip(x, y))


@lru_cache(maxsize=None)
def unsupported_two(a, r1, r2):
    """Exact feasibility of lambda*r1+(1-lambda)*r2 < a coordinatewise.

The strict interval constraints are intersected without floating point. Their
feasibility is equivalent to absence of a nonzero nonnegative supporting weight.
"""
    lo, hi = F(0), F(1)
    for ai, p, q in zip(a, r1, r2):
        b, s = ai-q, p-q
        if s == 0:
            if b <= 0:
                return False
        elif s > 0:
            hi = min(hi, b/s)
        else:
            lo = max(lo, b/s)
    if lo >= hi:
        return False
    lam = (lo+hi)/2
    assert 0 <= lam <= 1
    assert all(lam*p+(1-lam)*q < ai for ai,p,q in zip(a,r1,r2))
    return True


def good(a, r1, r2):
    return not dominates(r1,a) and not dominates(r2,a) and unsupported_two(a,r1,r2)


def mix_margin(a, r1, r2):
    """Exact piecewise-linear maximisation, used only for small boundary controls."""
    lines = [(ai-q, q-p) for ai,p,q in zip(a,r1,r2)]
    candidates = {F(0),F(1)}
    for (b,s),(c,t) in product(lines, repeat=2):
        if s != t:
            z = (c-b)/(s-t)
            if 0 <= z <= 1:
                candidates.add(z)
    return max(min(b+s*z for b,s in lines) for z in candidates)


def multiply(rows, x):
    return tuple(sum((w*z for w,z in zip(row,x)), F(0)) for row in rows)


def axis(d,i):
    return tuple(F(int(k==i)) for k in range(d))


def no_go_controls():
    rng = random.Random(SEED)
    counts = {}
    q=F(3,4)
    for d in (3,5,20,50):
        candidate=(q,)*d
        rivals=tuple(axis(d,i) for i in range(d))
        assert all(not dominates(r,candidate) for r in rivals)
        assert all((rivals[0][i]+rivals[1][i])/2 < q for i in range(d))
        matrices=[]
        if d == 3:
            grid=tuple((F(i,4),F(j,4),F(4-i-j,4))
                       for i in range(5) for j in range(5-i))
            assert len(grid)==15
            matrices.extend(product(grid, repeat=2))
        # Test both two rows and the demanding m=d-1 regime, with boundary rows.
        for m in sorted({1,2,d-1}):
            matrices.append(tuple(axis(d,i) for i in range(m)))
            matrices.append(tuple((F(1,d),)*d for _ in range(m)))
            for _ in range(40):
                rows=[]
                for __ in range(m):
                    raw=[rng.randrange(0,11) for ___ in range(d)]
                    if not any(raw):
                        raw[0]=1
                    total=sum(raw)
                    rows.append(tuple(F(v,total) for v in raw))
                matrices.append(tuple(rows))
        for rows in matrices:
            assert 1 <= len(rows) < d
            assert all(sum(row)==1 and min(row)>=0 for row in rows)
            covered={i for row in rows for i,v in enumerate(row) if v>F(1,2)}
            assert len(covered)<=len(rows)<d
            i=next(i for i in range(d) if i not in covered)
            projected_a=multiply(rows,candidate)
            projected_r=multiply(rows,rivals[i])
            assert dominates(projected_r,projected_a)
            assert all(a-r>=F(1,4) for a,r in zip(projected_a,projected_r))
        counts[str(d)]={"matrices_checked":len(matrices),
                         "all_destroy_nondomination":True,
                         "minimum_proved_projected_gap":"1/4"}
    return counts


def anchors(d):
    # Distinct, nonnegative row-stochastic reconstruction; includes both anchors.
    return ((F(1),F(0)),(F(0),F(1)))+tuple(
        (F(i,d-1), F(d-1-i,d-1)) for i in range(1,d-1))


def archive_controls():
    symbols=((F(0),F(0)),(F(1),F(0)),(F(1),F(1)))
    sequences=tuple(product(symbols,repeat=2))
    archives=tuple(product(sequences,repeat=3))
    assert len(archives)==729
    prefixes=tuple(product(range(3),repeat=3))
    prices=((2,5),(3,7),(11,13))
    cost=lambda p:17+sum(sum(prices[g][:p[g]]) for g in range(3))
    full_cost=cost((2,2,2))

    @lru_cache(maxsize=None)
    def bounds(seq,b):
        low=tuple(sum((row[i] for row in seq[:b]),F(0))/2 for i in range(2))
        return low,tuple(v+F(2-b,2) for v in low)

    def verdict_bounds(states):
        la,ua=states[0]
        return (all(not dominates(lg,ua) for lg,ug in states[1:])
                and unsupported_two(la,states[1][1],states[2][1]))

    result={}
    for d in (5,20,50):
        matrix=anchors(d)
        assert len(matrix)==d
        @lru_cache(maxsize=None)
        def project(point):
            return multiply(matrix,point)
        # Every N=2 archive is tested at full disclosure in each dimension.
        positives=0
        for archive in archives:
            p=tuple(bounds(seq,2)[0] for seq in archive)
            original=good(*p)
            lifted=good(*(project(x) for x in p))
            assert original==lifted
            positives+=original
            # All three pairwise relations, both orientations.
            for i in range(3):
                for j in range(3):
                    assert dominates(p[i],p[j])==dominates(project(p[i]),project(p[j]))
        # Complete prefix enumeration for d=5; prespecified systematic subset for 20,50.
        indices=range(729) if d==5 else sorted(set(range(0,729,9))|{728})
        states_checked=0
        cost_comparisons=0
        positive_costs=0
        finite_costs=[]
        for ai in indices:
            archive=archives[ai]
            c2=cn=None
            for prefix in prefixes:
                bs=tuple(bounds(archive[g],prefix[g]) for g in range(3))
                nbs=tuple((project(l),project(u)) for l,u in bs)
                v2=verdict_bounds(bs)
                vn=verdict_bounds(nbs)
                assert v2==vn
                states_checked+=1
                if v2:
                    c2=min(c2,cost(prefix)) if c2 is not None else cost(prefix)
                if vn:
                    cn=min(cn,cost(prefix)) if cn is not None else cost(prefix)
            assert c2==cn
            cost_comparisons+=1
            if c2 is not None:
                positive_costs+=1
                finite_costs.append(c2)
                assert c2<=full_cost
        result[str(d)]={"full_archive_verdict_comparisons":729,
                        "full_archive_positive_count":positives,
                        "prefix_archives":len(indices),
                        "prefix_states_compared":states_checked,
                        "retrospective_cost_comparisons":cost_comparisons,
                        "finite_positive_costs":positive_costs,
                        "positive_cost_values":sorted(set(finite_costs)),
                        "all_equal":True,
                        "setup":17,"row_prices":prices}
    return result


def boundary_controls():
    a=(F(1,2),F(1,2))
    r1=(F(1,10),F(7,10));r2=(F(7,10),F(1,10))
    eps=F(1,20)
    assert good(a,r1,r2)
    gamma=mix_margin(a,r1,r2)
    assert gamma==2*eps
    assert all(max(ri-ai for ri,ai in zip(r,a))>2*eps for r in (r1,r2))
    aa=tuple(x-eps for x in a)
    rr1=tuple(x+eps for x in r1);rr2=tuple(x+eps for x in r2)
    assert not good(aa,rr1,rr2)
    assert mix_margin(aa,rr1,rr2)==0

    a=(F(3,5),F(3,5)); b=(F(0),F(1)); c=(F(1),F(0))
    assert good(a,b,c)
    assert not unsupported_two(a+(F(0),),b+(F(0),),c+(F(0),))
    cubed=tuple(tuple(v**3 for v in p) for p in (a,b,c))
    assert not good(*cubed)
    assert sum(cubed[0])<sum(cubed[1])==sum(cubed[2])
    for i,j in product(range(3),repeat=2):
        assert dominates((a,b,c)[i],(a,b,c)[j])==dominates(cubed[i],cubed[j])
    return {"strict_2epsilon_boundary":{"epsilon":str(eps),
                "surrogate_mixture_margin":str(gamma),"actual_mixture_margin":"0",
                "surrogate_good":True,"actual_good":False},
            "constant_added_objective_changes_support":True,
            "coordinatewise_cube_preserves_dominance_but_changes_support":True}


def positive_archive_controls():
    """Positive rational archives, including certificates shorter than census.

The 729 endpoint-only N=2 archives above have no positive cases; these designed
controls prevent positive C* equality from being reported vacuously.
"""
    output={}
    for d in (5,20,50):
        matrix=anchors(d)
        @lru_cache(maxsize=None)
        def project(p):
            return multiply(matrix,p)
        cases=[]
        for n in (8,16):
            for alternating in (False,True):
                rows=[[],[],[]]
                for i in range(n):
                    sign=1 if i%2==0 else -1
                    da=F(sign,32) if alternating else F(0)
                    dl=F(sign,8) if alternating else F(0)
                    rows[0].append((F(7,8)+da,F(3,8)+da))
                    rows[1].append((F(1,2)+dl,F(1,2)+dl))
                    rows[2].append((F(1),F(0)))
                assert all(0<=f<=c<=1 for group in rows for c,f in group)
                prefix_bounds=[]
                for group in rows:
                    group_bounds=[]
                    for b in range(n+1):
                        lo=tuple(sum((p[i] for p in group[:b]),F(0))/n for i in range(2))
                        hi=tuple(v+F(n-b,n) for v in lo)
                        group_bounds.append((lo,hi))
                    prefix_bounds.append(group_bounds)
                means=tuple(group[-1][0] for group in prefix_bounds)
                assert good(*means) and good(*(project(x) for x in means))
                prices=tuple(tuple(i+1+2*g for i in range(n)) for g in range(3))
                cost=lambda p:17+sum(sum(prices[g][:p[g]]) for g in range(3))
                full_cost=cost((n,n,n))
                c2=cn=None
                witness=None
                checked=0
                true_states=0
                for p in product(range(n+1),repeat=3):
                    bs=tuple(prefix_bounds[g][p[g]] for g in range(3))
                    nbs=tuple((project(lo),project(hi)) for lo,hi in bs)
                    la,ua=bs[0]
                    v2=(all(not dominates(lo,ua) for lo,hi in bs[1:])
                        and unsupported_two(la,bs[1][1],bs[2][1]))
                    nla,nua=nbs[0]
                    vn=(all(not dominates(lo,nua) for lo,hi in nbs[1:])
                        and unsupported_two(nla,nbs[1][1],nbs[2][1]))
                    assert v2==vn
                    checked+=1
                    if v2:
                        true_states+=1
                        cp=cost(p)
                        if c2 is None or cp<c2:
                            c2=cp
                            witness=p
                    if vn:
                        cn=min(cn,cost(p)) if cn is not None else cost(p)
                assert c2==cn and c2 is not None
                assert c2<full_cost
                cases.append({"length":n,"alternating_rows":alternating,
                              "prefix_states_compared":checked,
                              "true_prefix_states":true_states,
                              "latent_Cstar":c2,"lifted_Cstar":cn,
                              "full_disclosure_cost":full_cost,
                              "minimum_cost_prefix":witness,
                              "positive_and_strictly_cheaper_than_census":True})
        output[str(d)]=cases
    return output


def numeric_crosscheck():
    try:
        from scipy.optimize import linprog
    except ImportError:
        return {"status":"not_run","reason":"SciPy unavailable; exact controls do not require it"}
    rng=random.Random(SEED+1)
    counts={}
    for d in (3,5,20,50):
        for _ in range(25):
            points=tuple(tuple(F(rng.randrange(11),10) for __ in range(d)) for ___ in range(3))
            a,b,c=points
            lp=linprog([0.0]*d,
                       A_ub=[[float(ai-ri) for ai,ri in zip(a,r)] for r in (b,c)],
                       b_ub=[0,0],A_eq=[[1.0]*d],b_eq=[1.0],bounds=[(0,None)]*d,
                       method="highs")
            assert lp.status in (0,2),lp.message
            exact=unsupported_two(a,b,c)
            assert exact==(lp.status==2)
        counts[str(d)]=25
    return {"status":"passed","cases_by_dimension":counts,
            "arithmetic":"floating-point SciPy/HiGHS; independent numerical cross-check only"}


def main():
    started=time.perf_counter()
    results={"status":"PASS","seed":SEED,
             "scope":"Finite exact controls and labelled numerical cross-checks; not universal proofs or deployment benchmarks.",
             "exact_arithmetic":"Python fractions.Fraction",
             "no_go":no_go_controls(),
             "exact_anchor_transfer":archive_controls(),
             "positive_archive_transfer":positive_archive_controls(),
             "boundary_controls":boundary_controls(),
             "numerical_crosscheck":numeric_crosscheck()}
    results["elapsed_seconds"]=round(time.perf_counter()-started,6)
    (ROOT/"RESULTS.json").write_text(json.dumps(results,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(results,indent=2))


if __name__=="__main__":
    main()
