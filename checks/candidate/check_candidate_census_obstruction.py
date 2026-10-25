#!/usr/bin/env python3
"""Exact finite checks of a candidate-census obstruction.

Reconstructs whole rows and checks every prefix using nondomination plus
an independent scalarisation-weight interval test. Finite checks supplement
the symbolic proof; they do not establish the all-length theorem.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib
import json
import sys
import time

def prefix_sums(rows):
    out=[(0,0)]
    for x,y in rows:
        a,b=out[-1];out.append((a+x,b+y))
    return out

def rows(q,padding=0):
    zero=(0,0);east=(1,0);diag=(1,1)
    return ([zero]*padding+[east]*(2*q)+[diag]*q+[zero]*q,
            [zero]*padding+[diag]*q+[zero]*(2*q)+[diag]*(q-1)+[zero],
            [zero]*padding+[east]*(4*q))

def dominates(a,b):
    return a[0]<=b[0] and a[1]<=b[1] and a!=b

def supported(a,rivals):
    lo=Q(0);hi=Q(1)
    for r in rivals:
        dc,df=r[0]-a[0],r[1]-a[1]
        slope=dc-df
        if slope==0:
            if df<0:return False
        elif slope>0:lo=max(lo,Q(-df,slope))
        else:hi=min(hi,Q(-df,slope))
        if lo>hi:return False
    return lo<=hi

def true_prefix(sums,lengths,N):
    lower=[sums[g][lengths[g]] for g in range(3)]
    upper=[(v[0]+N-lengths[g],v[1]+N-lengths[g]) for g,v in enumerate(lower)]
    if any(dominates(lower[g],upper[0]) for g in (1,2)):return False
    return not supported(lower[0],upper[1:])

def check(q,padding):
    archive=rows(q,padding);N=len(archive[0]);sums=list(map(prefix_sums,archive))
    minimum=3*N+1;minimum_census=3*N+1;count=0;states=0
    for b in product(range(N+1),repeat=3):
        actual=true_prefix(sums,b,N)
        expected=b[0]>=3*q+2+padding and b[1]==N and b[2]>=N-1
        assert actual==expected,(q,padding,b,actual,expected)
        states+=1
        if actual:
            count+=1;minimum=min(minimum,sum(b))
            if b[0]==N:minimum_census=min(minimum_census,sum(b))
    assert minimum==3*N-q+1
    assert minimum_census==3*N-1
    # Padding scales the observed gap but preserves the certificate pattern.
    G=Q(2*q,N);p=5*G/(4+G)
    # The two stated complete continuations are evaluated from rows below.
    costs=[]
    for first in (1,2):
        b=[N,0,0]
        a=sums[0][N]
        for rival in (1,2):
            while dominates(sums[rival][b[rival]],a):
                b[rival]+=1
                if b[rival]==N:break
        while not true_prefix(sums,b,N):
            next_group=first if b[first]<N else 3-first
            b[next_group]+=1
        costs.append(sum(b))
    assert costs==[3*N-1,3*N],(q,padding,costs)
    expected_cost=(1-p)*costs[0]+p*costs[1]
    return dict(q=q,padding=padding,N=N,prefix_states=states,true_states=count,
                certificate_cost=minimum,candidate_census_certificate_cost=minimum_census,
                NW_first_cost=costs[0],SE_first_cost=costs[1],mixing_probability=str(p),
                mixed_expected_cost=str(expected_cost),mixed_ratio=str(expected_cost/minimum),
                candidate_census_ratio=str(Q(minimum_census,minimum)))

def main():
    start=time.perf_counter()
    cases=[(3,0),(3,1),(3,2),(3,3),(5,0),(8,0),(16,0)]
    results=[check(*case) for case in cases]
    # Adverse control: q=1 is not a valid positive hard world.
    a=rows(1);s=list(map(prefix_sums,a))
    assert not true_prefix(s,(4,4,4),4)
    s12=list(map(prefix_sums,rows(3)))
    positives=[b for b in product(range(13),repeat=3) if true_prefix(s12,b,12)]
    priced=[]
    for M in (Q(1,2),Q(34),Q(10000)):
        cost=lambda b:sum(b)+(M-1 if b[0]==12 else 0)
        best=min(map(cost,positives))
        best_full=min(cost(b) for b in positives if b[0]==12)
        assert best==34 and best_full==34+M
        priced.append(dict(final_candidate_price=str(M),certificate_cost=str(best),
                           candidate_census_cost=str(best_full),ratio=str(best_full/best)))
    out=dict(status='PASS',cases=results,
             total_prefix_states=sum(x['prefix_states'] for x in results),
             priced_cases=priced,priced_prefix_states=13**3,
             adverse_control='q=1 full archive is not GOOD; positivity assertion would fail',
             elapsed_seconds=time.perf_counter()-start,
             python_version=sys.version,
             command='python3 check_candidate_census_obstruction.py',
             scope='Finite exact checks. Universal proof is separate.',
             script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    Path(__file__).with_name('Candidate_Census_Exact_Check.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
