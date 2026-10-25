"""Exact rational audit of the N=5 triangular candidate/rival-tail hard pair.
Own code adapted from P21 independent corner enumerator, standard library only.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
N=5
A=[(F(79,80),F(1,8))]*4
L=[(F(51,100),F(51,100))]+[(F(13,50),F(13,50))]*3
R=[(F(1),F(0))]*N
W={'A':[A+[(F(0),F(0))],L+[(F(13,50),F(13,50))],R],
   'B':[A+[(F(1),F(0))],L+[(F(1),F(1))],R]}
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
    expected=[(4,5,5),(5,5,5)] if name=='A' else [(5,i,5) for i in range(1,6)]
    assert positives==expected,(name,positives)
    results[name]={'TRUE_prefixes':positives,'minimum_cost':min(map(sum,positives))}
assert W['A'][0][:4]==W['B'][0][:4] and W['A'][1][:4]==W['B'][1][:4] and W['A'][2]==W['B'][2]
q=F(56,67)
rA=(14+q)/14
rB=(15-4*q)/11
assert rA==rB==F(71,67)
prices=[]
for base in [F(0),F(1,3),F(10),F(100)]:
    for x in [F(1,3),F(1),F(7)]:
        for y in [F(1,4),F(2),F(5)]:
            den=x*(base+x)+y*(base+y)
            q=y*(base+y)/den
            a=(base+y+q*x)/(base+y)
            b=(base+x+(1-q)*y)/(base+x)
            assert a==b==1+x*y/den
            det=1+min(x/(base+y),y/(base+x))
            assert det==1+min(x,y)/(base+max(x,y))
            prices.append({'W':str(base),'x':str(x),'y':str(y),'q_candidate_first':str(q),'randomised_pair_value':str(a),'deterministic_pair_value':str(det)})
out={'status':'PASS','states_evaluated':432,'worlds':results,
 'randomised_lower_ratio':'71/67','deterministic_lower_ratio':'15/14',
 'balancing_candidate_first_probability':'56/67',
 'weighted_checks':prices,
 'alphabet_size':len(set(r for w in W.values() for rows in w for r in rows)),
 'scope':'Verifies explicit two fixed archives and weighted two-choice game. Does not prove the global N5 upper or historical novelty.'}
assert out['alphabet_size']==6
Path(__file__).with_name('Triangle_N5_Two_World_Exact_Check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'states_evaluated':out['states_evaluated'],'worlds':results,'weighted_cases':len(prices),'alphabet_size':out['alphabet_size']},indent=2))
