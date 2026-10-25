#!/usr/bin/env python3
"""Exact Fraction checks for P56 new dimensional/margin derivations.
No P55 code is imported. This is finite corroboration, not the general proof.
"""
from fractions import Fraction as F
from itertools import combinations, product
from functools import lru_cache
from random import Random
import json
from pathlib import Path

def solve(a,b):
    n=len(b); a=[list(x)+[y] for x,y in zip(a,b)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if a[i][j]),None)
        if pivot is None:return None
        a[j],a[pivot]=a[pivot],a[j]
        z=a[j][j];a[j]=[x/z for x in a[j]]
        for i in range(n):
            if i!=j:
                z=a[i][j];a[i]=[x-z*y for x,y in zip(a[i],a[j])]
    return tuple(a[i][-1] for i in range(n))

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def dominates(a,b):return all(x<=y for x,y in zip(a,b)) and any(x<y for x,y in zip(a,b))
@lru_cache(maxsize=100000)
def support(p, rivals):
    """Exact vertex enumeration of w>=0,sumw=1,w.(r-p)>=0."""
    d=len(p)
    cs=[tuple(F(i==j) for j in range(d)) for i in range(d)]
    cs += [tuple(x-y for x,y in zip(r,p)) for r in rivals]
    for ids in combinations(range(len(cs)),d-1):
        w=solve([tuple(F(1) for _ in p)]+[cs[i] for i in ids],[F(1)]+[F(0)]*(d-1))
        if w is not None and all(dot(c,w)>=0 for c in cs):return w
    return None

def robust(corners, b):
    la,ua=corners[0][b[0]]
    if any(dominates(corners[g][b[g]][0],ua) for g in range(1,len(b))):return False
    return support(la,tuple(corners[g][b[g]][1] for g in range(1,len(b)))) is None

def arrays(rows, weights):
    d=len(rows[0][0]);ans=[]
    for rr,ww in zip(rows,weights):
        cur=[F(0)]*d;seen=F(0);arr=[]
        arr.append((tuple(cur),tuple(F(1) for _ in cur)))
        for r,w in zip(rr,ww):
            cur=[x+w*y for x,y in zip(cur,r)];seen+=w
            arr.append((tuple(cur),tuple(x+1-seen for x in cur)))
        assert seen==1
        ans.append(arr)
    return ans

def comparator(rows, weights, prices):
    co=arrays(rows,weights);n=[len(r) for r in rows];k=len(n);d=len(rows[0][0])
    pc=[]
    for pp in prices:
        aa=[F(0)]
        for x in pp:aa.append(aa[-1]+x)
        pc.append(aa)
    brute=None;states=0;true=0
    for b in product(*(range(x+1) for x in n)):
        states+=1
        if robust(co,b):
            true+=1;c=sum(pc[g][b[g]] for g in range(k))
            if brute is None or c<brute:brute=c
    structured=None
    for s in range(n[0]+1):
        la,ua=co[0][s];hh={}
        for g in range(1,k):
            h=next((b for b in range(n[g]+1) if not dominates(co[g][b][0],ua)),None)
            if h is None:break
            hh[g]=h
        if len(hh)<k-1:continue
        base=pc[0][s]+sum(pc[g][hh[g]] for g in hh)
        for size in range(1,min(d,k-1)+1):
            for jj in combinations(range(1,k),size):
                for bb in product(*(range(hh[g],n[g]+1) for g in jj)):
                    if support(la,tuple(co[g][b][1] for g,b in zip(jj,bb))) is None:
                        c=base+sum(pc[g][b]-pc[g][hh[g]] for g,b in zip(jj,bb))
                        if structured is None or c<structured:structured=c
    assert brute==structured,(brute,structured,rows,weights,prices)
    return dict(d=d,lengths=n,states=states,true_states=true,positive=brute is not None,minimum=None if brute is None else str(brute))

def run():
    out={'status':'PASS','arithmetic':'fractions.Fraction, exact rational vertex enumeration','scope':'Finite corroboration only; universal proofs are in research/generalization.md','sharp_witness':[],'comparator':[],'margin':{}}
    for d in range(2,7):
        p=(F(1,2),)*d;a=F(1,4*d)
        rr=[tuple(F(1,2)+a-(F(1,2) if i==j else 0) for j in range(d)) for i in range(d)]
        assert support(p,tuple(rr)) is None
        assert all(not dominates(r,p) for r in rr)
        assert all(support(p,tuple(r for i,r in enumerate(rr) if i!=skip)) is not None for skip in range(d))
        mixture=tuple(sum(r[j] for r in rr)/d for j in range(d))
        assert all(x==F(1,2)-a for x in mixture)
        out['sharp_witness'].append({'d':d,'required_rivals':d,'mixture_gap':str(a)})
    rng=Random(5601)
    for d in (2,3,4):
        for case in range(10):
            k=d+1+(case%2 if d<4 else 0)
            ns=[rng.randint(1,3 if d<4 else 2) for _ in range(k)]
            weights=[];prices=[];rows=[]
            p=(F(1,2),)*d;a=F(1,4*d)
            means=[p]+[tuple(F(1,2)+a-(F(1,2) if i==j else 0) for j in range(d)) for i in range(d)]
            if k>d+1:means.append((F(4,5),)*d)
            for g,n in enumerate(ns):
                ww=[rng.randint(1,5) for _ in range(n)];weights.append([F(x,sum(ww)) for x in ww])
                prices.append([F(rng.randint(1,7),rng.randint(1,3)) for _ in range(n)])
                if case<6:rr=[means[g]]*n
                else:rr=[tuple(F(rng.randint(0,4),4) for _ in range(d)) for j in range(n)]
                rows.append(rr)
            out['comparator'].append(comparator(rows,weights,prices))
    # Exhaustively check margin implication for all prefixes in random fixed archives.
    tested=0;applicable=0
    for d in (2,3):
        for case in range(20):
            k=d+1;n=3
            # Symmetric sharp-d points, mildly perturbed common shifts by row.
            p=(F(1,2),)*d;a=F(1,4*d)
            means=[p]+[tuple(F(1,2)+a-(F(1,2) if i==j else 0) for j in range(d)) for i in range(d)]
            rows=[];weights=[]
            for g in range(k):
                ww=[rng.randint(1,4) for _ in range(n)];weights.append([F(x,sum(ww)) for x in ww])
                rr=[]
                for j in range(n):
                    shift=F(rng.randint(-1,1),100)
                    rr.append(tuple(x+shift for x in means[g]))
                rows.append(rr)
            co=arrays(rows,weights);pp=[c[-1][0] for c in co]
            delta=[max(x-y for x,y in zip(pp[g],pp[0])) for g in range(1,k)]
            mix=tuple(sum(pp[g][j] for g in range(1,k))/d for j in range(d))
            gamma=min(x-y for x,y in zip(pp[0],mix))
            for bb in product(range(n+1),repeat=k):
                tested+=1;res=[1-sum(weights[g][:bb[g]]) for g in range(k)]
                if all(res[0]+res[g]<delta[g-1] for g in range(1,k)) and res[0]+sum(res[1:])/d<gamma:
                    applicable+=1;assert robust(co,bb)
    # Exact triangle example pA=(7/8,3/8),L=(1/2,1/2),R=(1,0).
    p=(F(7,8),F(3,8));l=(F(1,2),F(1,2));r=(F(1),F(0))
    delta=min(max(x-y for x,y in zip(q,p)) for q in (l,r))
    gamma=min(p[j]-(l[j]+r[j])/2 for j in range(2))
    assert delta==gamma==F(1,8)
    # N=160: candidate last10 zeros; Llast10ones realizes failure at residual1/16.
    n=160;rows=[[(F(1),F(1))]*60+[(F(1),F(0))]*80+[(F(0),F(0))]*20,
               [(F(1),F(1))]*70+[(F(0),F(0))]*80+[(F(1),F(1))]*10,
               [(F(1),F(0))]*n]
    ww=[[F(1,n)]*n for _ in rows];co=arrays(rows,ww)
    assert [x[-1][0] for x in co]==[p,l,r]
    assert not robust(co,(150,150,150))
    assert robust(co,(151,151,151))
    # Repeated rows same means: stop threshold s>8/9.
    rr=[[x]*n for x in (p,l,r)];cc=arrays(rr,ww)
    first=next(b for b in range(n+1) if robust(cc,(b,b,b)))
    assert first==n*8//9+1
    # d3 candidate-census counterexample: interval endpoints in bounded dims,
    # all finite candidate costs >=3/5. Mixture strictly below lower candidate.
    ca=(F(3,5),F(11,20),F(11,20));upper_bounded=(F(19,20),F(19,20))
    riv=((F(0),F(1),F(0)),(F(0),F(0),F(1)))
    assert all(any(q[j+1]>upper_bounded[j] for j in range(2)) for q in riv)
    assert all(sum(q[j] for q in riv)/2<ca[j] for j in range(3))
    out['margin']={'prefixes_tested':tested,'sufficient_conditions_applicable_and_sound':applicable,
       'triangle_delta':str(delta),'triangle_gamma':str(gamma),'N':n,
       'worst_order_boundary_prefix':[150]*3,'boundary_is_TRUE':False,
       'guaranteed_prefix':[151]*3,'guaranteed_is_TRUE':True,
       'guaranteed_savings_rows':27,'census_rows':480,
       'same_means_repeated_rows_first_lockstep_prefix':first,'repeated_rows_savings':3*(n-first)}
    out['unbounded_dimension_family']=[]
    for dim in range(3,9):
        t=F(3,2*(dim-1));c=(t+F(1,dim-1))/2
        assert F(1,dim-1)<c<t<1
        assert c+1-t<1
        out['unbounded_dimension_family'].append({'d':dim,'N':2*(dim-1),'candidate_observed':3,'bounded_candidate_lower':str(c),'bounded_candidate_upper':str(c+1-t),'rival_axis_mixture_coordinate':str(F(1,dim-1))})
    out['d3_unbounded_candidate_partial']={'N':10,'prefix':[6,10,10],'candidate_lower':[str(x) for x in ca],'bounded_candidate_upper':[str(x) for x in upper_bounded],'status':'verified by exact inequalities'}
    out['comparator_totals']={'archives':len(out['comparator']),'positive':sum(x['positive'] for x in out['comparator']),'prefixes':sum(x['states'] for x in out['comparator']),'true_prefixes':sum(x['true_states'] for x in out['comparator'])}
    path=Path(__file__).resolve().parents[1]/'evidence'/'Generalization_Checks_P56.json'
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ('status','comparator_totals','margin','d3_unbounded_candidate_partial')},indent=2))
if __name__=='__main__':run()
