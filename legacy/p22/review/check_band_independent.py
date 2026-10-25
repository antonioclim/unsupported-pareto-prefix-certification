"""Independent exact-rational checks of P22 diagonal-band claims.

Original audit code; stdlib only. The production implementation is not imported.
Finite checks supplement the analytic review and do not prove continuous claims.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json


def in_band(p, d):
    c, f = p
    return 0 <= f <= c <= 1 and c-f <= d


def support(p, rivals):
    lo, hi = Q(0), Q(1)
    for c, f in rivals:
        dc, df = c-p[0], f-p[1]
        slope = dc-df
        if slope == 0:
            if df < 0:
                return False
        elif slope > 0:
            lo = max(lo, -df/slope)
        else:
            hi = min(hi, -df/slope)
    return lo <= hi


def true_corners(boxes):
    lo, hi = boxes[0]
    for lr, ur in boxes[1:]:
        if all(x <= y for x,y in zip(lr,hi)) and any(x < y for x,y in zip(lr,hi)):
            return False
    return not support(lo, [box[1] for box in boxes[1:]])


def corners(rows):
    n=len(rows)
    total=[Q(0),Q(0)]
    out=[]
    for k in range(n+1):
        if k:
            total=[x+y for x,y in zip(total,rows[k-1])]
        lower=tuple(x/n for x in total)
        upper=tuple(x+Q(n-k,n) for x in lower)
        out.append((lower,upper))
    return out


def is_true(boxes, state):
    return true_corners([b[k] for b,k in zip(boxes,state)])


def construction(n,a,i,j,d):
    t,s,r=(Q(n-k,n) for k in (a,i,j))
    u,v=s+t,r+t
    b=d*(1-r)
    z=(b-u-v)/2
    delta=z*z-u*v
    if z <= 0 or delta <= 0:
        return None
    e=delta/(2*b)
    p=(b-t-e,r+z-e)
    left=((b-s+r)/2,)*2
    right=(b,Q(0))
    rows=[tuple(x/(1-t) for x in p),
          tuple(x/(1-s) for x in left),
          tuple(x/(1-r) for x in right)]
    assert all(in_band(row,d) for row in rows), (n,a,i,j,d,rows)
    boxes=[(p,tuple(x+t for x in p)),
           (left,tuple(x+s for x in left)),
           (right,tuple(x+r for x in right))]
    assert true_corners(boxes), (n,a,i,j,d)
    # Check the crossing determinant independently against the claimed margin.
    x,y=p
    lc,lf=boxes[1][1]
    rc,rf=boxes[2][1]
    determinant=(x-lc)*(y-rf)-(lf-y)*(rc-x)
    assert determinant==delta/2 and determinant>0
    return rows


def hard_worlds(n,d):
    q=Q(1,n)
    c=d*(1-q)
    assert c>2*q
    e=min((c-2*q)/16,q*q/16)
    p=(3*c/4+q/2+e,c/4+q/2+e)
    first_left=[(d/2,d/2)]*(n-1)
    first_right=[(d,Q(0))]*(n-1)
    worlds=[[[p]*n,first_left+[(Q(0),Q(0))],first_right+[(Q(1),Q(1))]],
            [[p]*n,first_left+[(Q(1),Q(1))],first_right+[(Q(0),Q(0))]]]
    assert all(in_band(row,d) for w in worlds for g in w for row in g)
    return worlds


def main():
    levels=sorted({Q(a,b) for b in range(1,9) for a in range(1,b+1)})
    tested=feasible=threshold=total_threshold=extra_groups=0
    for n in range(1,15):
        for d in levels:
            min_a=None
            min_total=None
            for a,i,j in product(range(1,n+1),repeat=3):
                tested+=1
                row=construction(n,a,i,j,d)
                if row is not None:
                    feasible+=1
                    min_a=a if min_a is None else min(min_a,a)
                    min_total=a+i+j if min_total is None else min(min_total,a+i+j)
            expected=int(n*(1-d/4))+1
            assert min_a==expected, (n,d,min_a,expected)
            threshold+=1
            assert min_total==int((3-d)*n)+1,(n,d,min_total)
            total_threshold+=1
            # Sharp total-cost construction with K=5 and one row in extras.
            i=int(n*(1-d))+1
            rows=construction(n,n,i,n,d)
            lengths=(n,i,n)
            box=[]
            for row,k in zip(rows,lengths):
                lo=tuple(x*Q(k,n) for x in row)
                hi=tuple(x+Q(n-k,n) for x in lo)
                box.append((lo,hi))
            box.extend([((Q(1,n),Q(1,n)),(Q(1),Q(1)))]*2)
            assert true_corners(box)
            assert n+i+n+2==5+int((3-d)*n)-2
            extra_groups+=1
    full_states=world_count=0
    for n in range(4,10):
        for d in levels:
            if d*(n-1)<=2:
                continue
            for windex,w in enumerate(hard_worlds(n,d)):
                boxes=[corners(g) for g in w]
                actual=[]
                for state in product(range(n+1),repeat=3):
                    full_states+=1
                    if is_true(boxes,state):
                        actual.append(state)
                expected=([(n,n,n-1),(n,n,n)] if windex==0
                          else [(n,n-1,n),(n,n,n)])
                assert actual==expected,(n,d,windex,actual)
                world_count+=1
    boundary_checks=boundary_worlds=0
    for n in range(4,101):
        for d in (Q(k,20) for k in range(1,21)):
            if d*(n-1)<=2:
                continue
            for windex,w in enumerate(hard_worlds(n,d)):
                boxes=[corners(g) for g in w]
                false_states=([(n-1,n,n),(n,n-1,n),(n,n,n-2)] if windex==0
                              else [(n-1,n,n),(n,n,n-1),(n,n-2,n)])
                for state in false_states:
                    assert not is_true(boxes,state),(n,d,windex,state)
                    boundary_checks+=1
                minimum=(n,n,n-1) if windex==0 else (n,n-1,n)
                assert is_true(boxes,minimum)
                assert is_true(boxes,(n,n,n))
                boundary_checks+=2
                boundary_worlds+=1
    prices=0
    for W,x,y in product((Q(0),Q(1),Q(11),Q(103,7)),
                         (Q(1,7),Q(1),Q(3),Q(13)),
                         (Q(1,11),Q(1),Q(5),Q(17))):
        q=y*(W+y)/(x*(W+x)+y*(W+y))
        ratio=1+x*y/(x*(W+x)+y*(W+y))
        assert (W+x+(1-q)*y)/(W+x)==ratio
        assert (W+y+q*x)/(W+y)==ratio
        # Both single tails sufficient: same chosen law still respects bound.
        assert (W+q*x+(1-q)*y)/(W+min(x,y))<=ratio
        assert min((W+x+y)/(W+y),(W+x+y)/(W+x))==1+min(x,y)/(W+max(x,y))
        prices+=1
    out={"status":"PASS", "independent_code":True,
         "exact_rational_arithmetic":True,"domain_levels":[str(d) for d in levels],
         "oriented_shapes_tested":tested,"feasible_constructions_checked":feasible,
         "sharp_candidate_threshold_checks":threshold,
         "sharp_total_certificate_threshold_checks":total_threshold,
         "K5_attainment_checks":extra_groups,
         "hard_worlds_full_enumeration":world_count,"full_prefix_states_checked":full_states,
         "hard_worlds_boundary_checks":boundary_worlds,
         "monotonicity_cover_boundary_states_checked":boundary_checks,
         "weighted_minimax_arithmetic_checks":prices,
         "limits":"Finite arithmetic checks of analytic constructions. Does not prove historical novelty, continuous minimax upper bound, or physical validity."}
    Path(__file__).with_name('Band_Independent_Checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()
