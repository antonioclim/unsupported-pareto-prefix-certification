#!/usr/bin/env python3
"""Exact best response to a finite weighted positive corpus, triangle model.
Research artifact P56. Does not establish a full-domain upper bound.
Stdlib only. Prefixes allow arbitrary interleaving; robust stopping is tested
against the entire triangle, never just against the finite corpus.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json
from pathlib import Path


def dominates(x,y):
    return all(a<=b for a,b in zip(x,y)) and x!=y


def true_prefix(prefix_sums, b, n):
    # Scaling all means by n leaves both geometric predicates unchanged.
    low=[tuple(prefix_sums[g][b[g]]) for g in range(3)]
    up=[tuple(v+n-b[g] for v in low[g]) for g in range(3)]
    if any(dominates(low[g],up[0]) for g in (1,2)):
        return False
    lo,hi=F(0),F(1)
    a=low[0]
    for g in (1,2):
        # support requires alpha*(u_c-a_c)+(1-alpha)*(u_f-a_f)>=0
        dc,df=up[g][0]-a[0],up[g][1]-a[1]
        slope=dc-df
        if slope==0:
            if df<0:return True
        elif slope>0:lo=max(lo,-F(df,slope))
        else:hi=min(hi,-F(df,slope))
    return lo>hi


def sums(archive):
    out=[]
    for rows in archive:
        p=[(F(0),F(0))]
        for x,y in rows:p.append((p[-1][0]+x,p[-1][1]+y))
        out.append(p)
    return out


def comparator(archive):
    n=len(archive[0]);ps=sums(archive)
    choices=(b for b in product(range(n+1),repeat=3) if true_prefix(ps,b,n))
    b=min(choices,key=lambda b:(sum(b),b))
    return sum(b),b


def best_response(archives, prior, comparators=None):
    n=len(archives[0][0]);m=len(archives)
    if any(len(a)!=3 or any(len(g)!=n for g in a) for a in archives):
        raise ValueError('Need K=3 and commonN')
    if any(not(0<=y<=x<=1) for a in archives for rows in a for x,y in rows):
        raise ValueError('Archive outside triangle')
    if len(prior)!=m or sum(prior)!=1 or min(prior)<0:
        raise ValueError('prior is nonnegative rational probabilityvector')
    ps=[sums(a) for a in archives]
    for p in ps:
        if not true_prefix(p,(n,n,n),n):raise ValueError('Nonpositive archive')
    costs=[comparator(a)[0] for a in archives] if comparators is None else comparators
    masses=[prior[i]/costs[i] for i in range(m)]
    actions={}
    @lru_cache(None)
    def solve(b,inds):
        if true_prefix(ps[inds[0]],b,n):
            return F(0)
        w=sum(masses[i] for i in inds)
        cand=[]
        for g in range(3):
            if b[g]==n:continue
            by={}
            for i in inds:by.setdefault(archives[i][g][b[g]],[]).append(i)
            nb=list(b);nb[g]+=1;nb=tuple(nb)
            value=w+sum(solve(nb,tuple(js)) for js in by.values())
            cand.append((value,g))
        if not cand:raise AssertionError('Full archive must be TRUE')
        value,g=min(cand)
        actions[(b,inds)]=g
        return value
    value=solve((0,0,0),tuple(range(m)))
    return {'weighted_normalized_cost':str(value),'states':solve.cache_info().currsize,
            'state_bound':m*(n+1)**3,'comparators':costs,
            'initial_action':actions.get(((0,0,0),tuple(range(m))))}


def hard_pair(q):
    n=4*q
    A=[(1,0)]*(2*q)+[(1,1)]*q+[(0,0)]*(q-1)
    L=[(1,1)]*q+[(0,0)]*(2*q)+[(1,1)]*(q-1)
    R=[(1,0)]*n
    return [[A+[(0,0)],L+[(0,0)],R], [A+[(1,0)],L+[(1,1)],R]]


def main():
    results=[]
    for q in (3,4,5,6):
        n=4*q;W=3*n-2*q+2;X=q-2;Y=q-1
        D=X*(W+X)+Y*(W+Y)
        prior=[F(Y*(W+Y),D),F(X*(W+X),D)]
        result=best_response(hard_pair(q),prior)
        expected=F(1)+F(X*Y,D)
        assert F(result['weighted_normalized_cost'])==expected
        assert result['states']<=result['state_bound']
        result.update(q=q,n=n,prior=list(map(str,prior)),expected_ratio=str(expected),pass_check=True)
        results.append(result)
    out={'status':'PASS','purpose':'Independent exact finite-corpus best-response verification',
         'not_claimed':'No full-triangle upper bound, no asymptotic optimum',
         'cases':results}
    dest=Path(__file__).resolve().parents[1]/'evidence'/'Literature_Finite_Oracle_P56.json'
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
