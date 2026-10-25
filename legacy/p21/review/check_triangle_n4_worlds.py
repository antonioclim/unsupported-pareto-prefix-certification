"""Independent exact corner-state enumeration for the proposed triangle N=4 lower.
Own audit code. Stdlib only. Triangle contains both whole-vector endpoints;
independent rows therefore have the same robust-TRUE test as the square.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

N=4
A=[(F(13,20),F(31,100))]*N
L=[(F(7,15),F(7,15))]*3
R=[(F(14,15),F(0))]*3
W={'A':[A,L+[(F(0),F(0))],R+[(F(1),F(1))]],
   'B':[A,L+[(F(1),F(1))],R+[(F(0),F(0))]]}

def corners(rows,s):
    lo=tuple(sum((r[k] for r in rows[:s]),F(0))/N for k in (0,1))
    hi=tuple(x+F(N-s,N) for x in lo)
    return lo,hi

def support(candidate,points):
    lower,upper=F(0),F(1)
    for p in points:
        dc,df=p[0]-candidate[0],p[1]-candidate[1]
        slope=dc-df
        if slope==0:
            if df<0:return False
        elif slope>0:lower=max(lower,-df/slope)
        else:upper=min(upper,-df/slope)
        if lower>upper:return False
    return True

def robust_true(world,state):
    box=[corners(rows,s) for rows,s in zip(world,state)]
    lo,hi=box[0]
    for lr,ur in box[1:]:
        if all(x<=y for x,y in zip(lr,hi)) and any(x<y for x,y in zip(lr,hi)):
            return False
    return not support(lo,[b[1] for b in box[1:]])

results={}
for name,w in W.items():
    assert all(0<=f<=c<=1 for rows in w for c,f in rows)
    positives=[p for p in product(range(N+1),repeat=3) if robust_true(w,p)]
    expected=[(4,4,3),(4,4,4)] if name=='A' else [(4,3,4),(4,4,4)]
    assert positives==expected,(name,positives)
    results[name]={'TRUE_prefixes':positives,'minimum_cost':min(map(sum,positives))}
assert W['A'][0]==W['B'][0] and W['A'][1][:3]==W['B'][1][:3] and W['A'][2][:3]==W['B'][2][:3]
out={'status':'PASS','states_evaluated':250,'worlds':results,
     'randomised_lower_ratio':'23/22','deterministic_lower_ratio':'12/11',
     'scope':'Verifies explicit two fixed archives; global upper is analytic, not finite enumeration.'}
Path(__file__).with_name('Triangle_N4_Independent_World_Check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
