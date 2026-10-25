#!/usr/bin/env python3
"""Own exact finite checks for the P23 N=6 theorem; standard library only."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
from math import lcm
import hashlib
import json
import random

ROOT=Path(__file__).resolve().parent
N=6

def support(p, rivals):
    lo,hi=Q(0),Q(1)
    for r in rivals:
        dx,dy=r[0]-p[0],r[1]-p[1]
        slope=dx-dy
        if slope>0:lo=max(lo,-Q(dy,slope))
        elif slope<0:hi=min(hi,-Q(dy,slope))
        elif dy<0:return False
    return lo<=hi

def dominates(x,y):
    return x[0]<=y[0] and x[1]<=y[1] and x!=y

def corners(rows):
    den=lcm(*(Q(x).denominator for g in rows for r in g for x in r))
    scaled=[[(int(Q(c)*den),int(Q(f)*den)) for c,f in g] for g in rows]
    out=[]
    for g in scaled:
        c=f=0;b=[]
        for k in range(N+1):
            if k:c+=g[k-1][0];f+=g[k-1][1]
            w=den*(N-k)
            b.append(((c,f),(c+w,f+w)))
        out.append(b)
    return out

def is_true(boxes,state):
    (pl,pu),(ll,lu),(rl,ru)=[g[k] for g,k in zip(boxes,state)]
    return not any(dominates(x,pu) for x in (ll,rl)) and not support(pl,(lu,ru))

def policy(boxes):
    state=[0,0,0]
    def advance(group):
        if is_true(boxes,state):return False
        assert state[group]<N
        state[group]+=1
        return True
    def census_remaining():
        for group in range(3):
            while state[group]<N:
                if not advance(group):return sum(state),True
        return sum(state),is_true(boxes,state)
    while state[0]<N:advance(0)
    p=boxes[0][N][0]
    for group in (1,2):
        while dominates(boxes[group][state[group]][0],p) and state[group]<N:
            if not advance(group):return sum(state),True
    orientation={}
    for group in (1,2):
        lower=boxes[group][state[group]][0]
        if lower[0]<p[0] and lower[1]>p[1]:orientation['NW']=group
        elif lower[0]>p[0] and lower[1]<p[1]:orientation['SE']=group
    if set(orientation)!={'NW','SE'}:return census_remaining()
    # All coordinates are sums scaled by den. The upper corner at zero is
    # N*den, giving an exact comparison to g=1/3 without floating point.
    scale=boxes[0][0][1][0]
    chosen=orientation['NW' if 3*(p[0]-p[1])<=scale else 'SE']
    other=3-chosen
    for group in (chosen,other):
        while state[group]<N:
            if not advance(group):return sum(state),True
    return sum(state),is_true(boxes,state)

def hard_worlds():
    r=[(Q(1),Q(0))]*N
    a=[(Q(249,250),Q(3,10))]*5
    l=[(Q(19,25),)*2]*2+[(Q(7,50),)*2]*2
    u=[a+[(Q(0),Q(0))],l+[(Q(37,50),)*2,(Q(1),)*2],r]
    v=[a+[(Q(1),Q(0))],l+[(Q(1),)*2,(Q(1),)*2],r]
    a2=[(Q(249,250),Q(3,25))]*5
    l2=[(Q(61,100),)*2]+[(Q(7,25),)*2]*4
    w=[a2+[(Q(0),Q(0))],l2+[(Q(7,25),)*2],r]
    z=[a2+[(Q(1),Q(0))],l2+[(Q(1),)*2],r]
    return [('U16',u),('V14',v),('A17',w),('B13',z)]

def feasibility(a,i,j):
    z=i+2*j+2*a-24
    return z>0 and z*z>4*(12-a-i)*(12-a-j)

def construction(a,i,j):
    t,s,r=(1-Q(v,N) for v in (a,i,j))
    U,V=s+t,r+t;b=1-r;z=(b-U-V)/2
    delta=z*z-U*V;epsilon=delta/(2*b)
    x,y=b-t-epsilon,r+z-epsilon
    row_a=(x/(1-t),y/(1-t))
    row_l=((b-s+r)/(2*(1-s)),)*2
    return [[row_a]*a+[(Q(0),Q(0))]*(N-a),
            [row_l]*i+[(Q(0),Q(0))]*(N-i),
            [(Q(1),Q(0))]*j+[(Q(0),Q(0))]*(N-j)]

def main():
    feasible=[s for s in product(range(1,N+1),repeat=3) if feasibility(*s)]
    minimal=[s for s in feasible if not any(v!=s and all(x<=y for x,y in zip(v,s)) for v in feasible)]
    assert minimal==[(5,5,6),(6,1,6),(6,5,5),(6,6,4)]
    hard=[];states=0;policy_cases=0
    for name,rows in hard_worlds():
        assert all(0<=f<=c<=1 for g in rows for c,f in g)
        boxes=corners(rows);true=[]
        for state in product(range(N+1),repeat=3):
            states+=1
            if is_true(boxes,state):true.append(state)
        if name=='U16':expected=[(a,i,6) for a in (5,6) for i in (5,6)]
        elif name=='V14':expected=[(6,i,6) for i in range(2,7)]
        elif name=='A17':expected=[(5,6,6),(6,6,6)]
        else:expected=[(6,i,6) for i in range(1,7)]
        assert true==expected,(name,true)
        cost,answer=policy(boxes);opt=min(map(sum,true))
        assert answer
        limit=opt if opt<=15 else 17 if opt==16 else 18
        assert cost<=limit
        policy_cases+=1
        hard.append({'name':name,'true_states':true,'C_star':opt,'deterministic_policy_cost':cost,'whole_row_symbols':len(set(r for g in rows for r in g))})
    generated=0
    for a,i,j in feasible:
        rows=construction(a,i,j)
        assert all(0<=f<=c<=1 for g in rows for c,f in g)
        for swap in (False,True):
            rr=rows if not swap else [rows[0],rows[2],rows[1]]
            boxes=corners(rr);true=[]
            for state in product(range(N+1),repeat=3):
                states+=1
                if is_true(boxes,state):true.append(state)
            opt=min(map(sum,true));cost,answer=policy(boxes)
            assert answer
            limit=opt if opt<=15 else 17 if opt==16 else 18
            assert cost<=limit
            generated+=1;policy_cases+=1
    # Finite synthetic policy checks, including negative archives; not a
    # substitute for the all-input analytic proof.
    rng=random.Random(230623)
    alphabet=[(Q(c,10),Q(f,10)) for c in range(11) for f in range(c+1)]
    positive=negative=0
    for case in range(120):
        rows=[[rng.choice(alphabet) for _ in range(N)] for _ in range(3)]
        boxes=corners(rows);true=[]
        for state in product(range(N+1),repeat=3):
            states+=1
            if is_true(boxes,state):true.append(state)
        cost,answer=policy(boxes)
        assert answer==bool(true) and cost<=18
        if true:
            positive+=1;opt=min(map(sum,true))
            limit=opt if opt<=15 else 17 if opt==16 else 18
            assert cost<=limit
        else:negative+=1
        policy_cases+=1
    # The exact positive determinants and safety gaps stated in the proof.
    def det(x,y,l,r=Q(0)):
        return (x-l)*(y-r)-(l-y)*(1-x)
    assert det(Q(83,100),Q(1,4),Q(59,100))==Q(11,5000)>0
    assert det(Q(83,100),Q(1,4),Q(59,100),Q(1,6))==-Q(189,5000)<0
    assert det(Q(299,300),Q(1,4),Q(23,25))==Q(127,7500)>0
    assert det(Q(83,100),Q(1,10),Q(67,200))==Q(191,20000)>0
    assert det(Q(299,300),Q(1,10),Q(187,200))==Q(203,60000)>0
    setup_checks=0
    for F in [Q(0),Q(1,101),Q(1,7),Q(1),Q(7),Q(100),Q(10**6)]:
        target=1+1/(F+16)
        for c in range(13,19):
            upper=c if c<=15 else 17 if c==16 else 18
            assert (F+upper)/(F+c)<=target
            setup_checks+=1
        assert min((F+17)/(F+16),(F+17)/(F+14))==target
        q=5*(F+17)/(6*F+98);lower=1+5/(6*F+98)
        assert 0<q<1
        assert (F+17+q)/(F+17)==lower==(F+18-5*q)/(F+13)
        assert lower>1+3/(4*F+62)
        setup_checks+=3
    report={'status':'PASS','exact_arithmetic':True,'prefix_states_enumerated':states,
            'hard_archives':hard,'positive_length_triples_checked':216,
            'minimal_feasible_shapes':minimal,'constructed_policy_archives':generated,
            'random_synthetic_archives':120,'random_synthetic_positive':positive,
            'random_synthetic_negative':negative,'policy_cases':policy_cases,
            'setup_arithmetic_checks':setup_checks,
            'deterministic_exact_zero_setup':'17/16','randomised_lower_zero_setup':'103/98',
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'proof_sha256':hashlib.sha256((ROOT/'N6_Deterministic_Exact_and_Randomised_Lower_P23.md').read_bytes()).hexdigest(),
            'scope':'Finite explicit-world, constructed-world and synthetic policy checks plus exact setup arithmetic; continuous universal policy correctness is analytic, not exhaustively computed. Randomised optimum remains open.'}
    (ROOT/'N6_Exact_Check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
