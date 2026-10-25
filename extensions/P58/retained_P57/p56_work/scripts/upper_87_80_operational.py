#!/usr/bin/env python3
"""P56 operational verification of new87/80 mixed triangle policy.
This is audit-only code, not part of published 1.0.0, not a general proof.
"""
from fractions import Fraction as Q
from itertools import product
from random import Random
from pathlib import Path
import json,sys,time,hashlib,platform
from datetime import datetime,timezone
START=time.monotonic(); rng=Random(550319); D=20

def dominates(x,y): return x[0]<=y[0] and x[1]<=y[1] and x!=y

def supported(cand,rivals):
    # Online endpoint test: exact intersection of closed supporting intervals.
    lo,hi=Q(0),Q(1)
    for p in rivals:
        dc,df=p[0]-cand[0],p[1]-cand[1]; slope=dc-df
        if slope==0:
            if df<0: return False
        elif slope>0:lo=max(lo,Q(-df,slope))
        else:hi=min(hi,Q(-df,slope))
    return lo<=hi

def complete_good(means):
    # Separate complete-data test: endpoints and all line breakpoints.
    p=means[0];rs=means[1:]
    if any(dominates(r,p) for r in rs):return False
    weights={Q(0),Q(1)}
    for r in rs:
        dc,df=r[0]-p[0],r[1]-p[1]
        if dc!=df:
            w=Q(-df,dc-df)
            if 0<=w<=1:weights.add(w)
    return not any(all(w*(r[0]-p[0])+(1-w)*(r[1]-p[1])>=0 for r in rs) for w in weights)

class Case:
    def __init__(self,archive):
        self.a=archive;self.n=len(archive[0]);self.s=[]
        for rows in archive:
            sums=[(0,0)]
            for x,y in rows:sums.append((sums[-1][0]+x,sums[-1][1]+y))
            self.s.append(sums)
        self.good=complete_good([v[-1] for v in self.s])
    def corners(self,b):
        lows=[self.s[g][b[g]] for g in range(3)]
        ups=[tuple(v+(self.n-b[g])*D for v in lows[g]) for g in range(3)]
        return lows,ups
    def true(self,b):
        low,up=self.corners(b)
        return not any(dominates(r,up[0]) for r in low[1:]) and not supported(low[0],up[1:])
    def oracle(self):
        # Theorem1 reduces all legal triangle completions to endpoint cases.
        # The retrospective comparator uses an independent complete predicate
        # on the two extremal completion patterns, not supported().
        best=3*self.n+1;states=0
        for b in product(range(self.n+1),repeat=3):
            states+=1;low,up=self.corners(b)
            good_nd=not any(dominates(r,up[0]) for r in low[1:])
            # robust nondomination plus unsupportedness at L_A vs all U_r
            extreme_good=complete_good([low[0],up[1],up[2]])
            result=good_nd and extreme_good
            assert result==self.true(b)
            if result:best=min(best,sum(b))
        return (best if best<=3*self.n else None),states
    def policy(self,first):
        b=[0,0,0];trace=[]
        def buy(g):
            assert b[g]<self.n
            b[g]+=1;trace.append((g,b[g]))
        for _ in range(self.n):buy(0)
        p=self.s[0][-1]
        for g in (1,2):
            while b[g]<self.n and dominates(self.s[g][b[g]],p):buy(g)
            if dominates(self.s[g][b[g]],p):
                return False,len(trace),b,trace
        roles={}
        for g in (1,2):
            l=self.s[g][b[g]]
            if l[0]<p[0] and l[1]>p[1]:roles['NW']=g
            elif l[0]>p[0] and l[1]<p[1]:roles['SE']=g
        if len(roles)==2:
            g=roles[first]
            while b[g]<self.n:buy(g)
            g=roles['SE' if first=='NW' else 'NW']
            while not self.true(b) and b[g]<self.n:buy(g)
            if self.true(b):return True,len(trace),b,trace
        for g in (1,2):
            while b[g]<self.n:buy(g)
        return self.true(b),len(trace),b,trace

archives=[]
# Exhaustive N=1 archives over the 6 quarter-free grid triangle symbols.
small=[(0,0),(10,0),(10,10),(20,0),(20,10),(20,20)]
for pts in product(small,repeat=3):archives.append(('exhaustive_N1',tuple((p,) for p in pts)))
# Fixed-seed independent synthetic archives, varied N, no favourable filtering.
alphabet=[(c,f) for c in range(0,D+1,2) for f in range(0,c+1,2)]
for n in range(2,9):
    for _ in range(200):archives.append(('fixed_seed_grid',tuple(tuple(rng.choice(alphabet) for _ in range(n)) for _ in range(3))))
# Designed constant-row positive and boundary cases in both rival label orders.
triples=[((18,5),(7,7),(20,0)), # G=13/20 exact transition
         ((18,4),(7,7),(20,0)), # high branch
         ((18,6),(7,7),(20,0)), # low branch
         ((12,10),(11,11),(20,0)),
         ((0,0),(10,0),(20,20)), # supported/axis case
         ((20,0),(10,0),(20,20)), # G=1, dominated
         ((10,10),(0,0),(20,20)), # G=0, dominated
         ((10,10),(10,10),(10,10))] # coincident
for n in range(1,9):
    for pts in triples:
        for swap in (False,True):
            if swap:pts=(pts[0],pts[2],pts[1])
            archives.append(('designed_boundary',tuple(tuple(p for _ in range(n)) for p in pts)))

# New rational transition G=3/4, both nearby branches, and swapped rival labels.
for n in range(1,13):
    for af in [Q(159,40),Q(4),Q(161,40)]:
        pts=((19,af),(7,7),(20,0))
        for sw in (False,True):
            pp=pts if not sw else (pts[0],pts[2],pts[1])
            archives.append(('new_cut_neighbours',tuple(tuple(p for _ in range(n))for p in pp)))

def probability(G):
    alpha=((Q(19,3)*G-2*G*G)/(4+G))if G<=Q(3,4)else Q(87,80)-Q(21,80)/G
    p=Q(12,11)*alpha
    assert 0<=p<=1
    return p

def rivals_first(case):
    b=[0,0,0];trace=[]
    for g in (1,2):
        for _ in range(case.n):b[g]+=1;trace.append((g,b[g]))
    while b[0]<case.n and not case.true(b):
        b[0]+=1;trace.append((0,b[0]))
    return case.true(b),sum(b),b,trace

def execute(case):
    a=case.policy('NW');b=case.policy('SE');c=rivals_first(case)
    for answer,cost,prefix,trace in (a,b,c):
        assert answer==case.good
        assert cost==sum(prefix)==len(trace)<=3*case.n
        if answer:assert case.true(prefix)
    assert all(g in(1,2)for g,_ in c[3][:2*case.n])
    if not case.good:return None,(a,b,c)
    G=Q(case.s[0][-1][0]-case.s[0][-1][1],D*case.n);p=probability(G)
    expected=Q(1,12)*c[1]+Q(11,12)*((1-p)*a[1]+p*b[1])
    return expected,(a,b,c)

def serial(x):
    if isinstance(x,Q):return str(x)
    raise TypeError(type(x).__name__)

counts={};positives=0;branches=0;states=0;maximum=Q(0);maxcase=None;boundaries=set()
for index,(family,archive)in enumerate(archives):
    case=Case(archive);counts[family]=counts.get(family,0)+1
    expected,outs=execute(case);branches+=3
    if not case.good:continue
    positives+=1;opt,num=case.oracle();states+=num
    assert expected>=opt
    ratio=expected/opt;assert ratio<=Q(87,80),(index,ratio)
    G=Q(case.s[0][-1][0]-case.s[0][-1][1],D*case.n)
    if G==Q(3,4):boundaries.add(str(G))
    if ratio>maximum:maximum=ratio;maxcase={'index':index,'N':case.n,'gap':str(G),'opt':opt,'costs':[o[1]for o in outs],'expected':str(expected),'archive':archive}
    for setup in [Q(0),Q(1,2),Q(10)]:assert (setup+expected)/(setup+opt)<=Q(87,80)

hard=[];hard_max=Q(0);partial=0;hard_enum=0
for q in list(range(3,13))+[20,50,56,100]:
  for pad in range(4):
   n=4*q+pad
   for world in ('U','V'):
    A=[(0,0)]*pad+[(20,0)]*(2*q)+[(20,20)]*q+[(0,0)]*(q-1)+([(0,0)]if world=='U'else[(20,0)])
    L=[(0,0)]*pad+[(20,20)]*q+[(0,0)]*(2*q)+[(20,20)]*(q-1)+([(0,0)]if world=='U'else[(20,20)])
    R=[(0,0)]*pad+[(20,0)]*(4*q)
    for swap in (False,True):
     ar=(A,L,R)if not swap else(A,R,L);case=Case(ar);assert case.good
     expected,outs=execute(case);branches+=3
     oracle=3*n-q+1 if world=='U' else 3*n-q
     if q==3 and pad==0:
      oo,nn=case.oracle();hard_enum+=nn;assert oo==oracle
     ratio=expected/oracle;assert ratio<=Q(87,80),(n,world,ratio)
     hard_max=max(hard_max,ratio)
     qa=outs[2][2][0]
     if world=='U':assert qa==n-q+2 and qa<n;partial+=1
     else:assert qa==n
     hard.append({'N':n,'q':q,'pad':pad,'world':world,'swap':swap,'opt_by_theorem16':oracle,'costs':[o[1]for o in outs],'expected':str(expected),'ratio':str(ratio),'Q_candidate_prefix':qa})

# New strict policy-class separation: infinitely many finiteN and eventuallyallN.
assert all(Q(12*q-1,11*q+1)>Q(87,80)for q in range(56,1001))
assert Q(12*55-1,11*55+1)<=Q(87,80)
assert all(Q(3*n-1,3*n-n//4+1)>Q(87,80)for n in range(308,5001))
assert Q(3*307-1,3*307-307//4+1)<=Q(87,80)
result={'schema':'p56-mixed-triangle-87-80-operational-v1','status':'PASS','arithmetic':'exact Fraction; finite tests distinct from continuous proof','ordinary_case_counts':counts,'ordinary_cases':len(archives),'ordinary_positive':positives,'ordinary_negative':len(archives)-positives,'ordinary_comparator_prefixes':states,'ordinary_max_observed_ratio':str(maximum),'ordinary_maxcase':maxcase,'hard_world_cases':len(hard),'hard_U_actual_partial_stops':partial,'hard_max_observed_ratio':str(hard_max),'hard_enumerated_prefixes':hard_enum,'policy_branch_executions':branches,'cut_boundaries_checked':sorted(boundaries),'hard_records':hard,'separation_controls':{'multiples_of_four_q_56_through_1000':True,'all_N_308_through_5000':True,'N_220_and_307_below_separation_threshold':True},'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'elapsed_seconds':time.monotonic()-START,'limitations':'Synthetic and analytic-family stress controls; no economic/deployment measurement; finite controls do not prove the universal bound.'}
Path('p56_work/evidence/upper_87_80_operational.json').write_text(json.dumps(result,indent=2,default=serial)+'\n')
print(json.dumps({k:v for k,v in result.items()if k not in ['ordinary_maxcase','hard_records']},indent=2))
