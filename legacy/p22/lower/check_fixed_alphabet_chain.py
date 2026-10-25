#!/usr/bin/env python3
"""Own stdlib exact checks for the fixed-alphabet candidate/rival chain family.

No external code execution, installation, network request or measured data.
Finite checks supplement the accompanying universal analytic proof.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def supported(p, rivals):
    # Exact interval intersection for alpha*(rc-pc)+(1-alpha)*(rf-pf)>=0.
    ln, ld, hn, hd = 0,1,1,1
    for rc,rf in rivals:
        dx,dy = rc-p[0],rf-p[1]
        slope=dx-dy
        if slope>0:
            if -dy*ld>ln*slope:
                ln,ld=-dy,slope
        elif slope<0:
            if dy*hd<hn*(-slope):
                hn,hd=dy,-slope
        elif dy<0:
            return False
    return ln*hd<=hn*ld


def make(q,pad,world):
    assert q>=3 and pad>=0 and world in ('U','V')
    n=4*q+pad
    rows=[[(0,0)]*pad+[(3,1)]*(3*q)+[(0,0)]*q,
          [(0,0)]*pad+[(1,1)]*(3*q)+[(3,3)]*q,
          [(0,0)]*pad+[(3,0)]*(4*q)]
    rows[0][-1]=(0,0) if world=='U' else (3,0)
    rows[1][-1]=(0,0) if world=='U' else (3,3)
    alphabet={(0,0),(3,0),(3,3),(3,1),(1,1)}
    assert {r for g in rows for r in g}<=alphabet
    corners=[]
    for group in rows:
        c,f=0,0
        groupcorners=[]
        for k in range(n+1):
            if k:
                c+=group[k-1][0]
                f+=group[k-1][1]
            width=3*(n-k)
            groupcorners.append(((c,f),(c+width,f+width)))
        corners.append(groupcorners)
    return corners,rows,n


def true(corners,state):
    (pl,pu),(ll,lu),(rl,ru)=[group[k] for group,k in zip(corners,state)]
    if any(r[0]<=pu[0] and r[1]<=pu[1] and r!=pu for r in (ll,rl)):
        return False
    return not supported(pl,(lu,ru))


def main():
    cases=[(q,0) for q in range(3,16)]
    cases.extend([(3,1),(4,2),(5,3),(25,0),(100,3)])
    records=[]
    fullcount,slicecount=0,0
    for q,pad in cases:
        for world in ('U','V'):
            corners,rows,n=make(q,pad,world)
            other=make(q,pad,'V' if world=='U' else 'U')[1]
            assert rows[0][:-1]==other[0][:-1]
            assert rows[1][:-1]==other[1][:-1]
            assert rows[2]==other[2]
            bA,bL,bR=n-q+2,n-q+1,n-1
            # These strongest omitted states fail. Information monotonicity
            # then excludes every state outside the checked large-N slices.
            obstruction=(n,n-1,n) if world=='U' else (n-1,n,n)
            assert not true(corners,obstruction)
            full=n<=60
            if full:
                states=product(range(n+1),repeat=3)
            elif world=='U':
                states=((a,n,j) for a,j in product(range(n+1),repeat=2))
            else:
                states=((n,i,j) for i,j in product(range(n+1),repeat=2))
            checked,positive,mincost=0,0,None
            for a,i,j in states:
                want=(a>=bA and i==n and j>=bR) if world=='U' else (
                    a==n and i>=bL and j>=bR)
                got=true(corners,(a,i,j))
                assert got==want,(q,pad,world,(a,i,j),got,want)
                checked+=1
                if got:
                    positive+=1
                    cost=a+i+j
                    mincost=cost if mincost is None else min(mincost,cost)
            assert positive==(2*(q-1) if world=='U' else 2*q)
            assert mincost==(3*n-q+1 if world=='U' else 3*n-q)
            if full:
                fullcount+=checked
            else:
                slicecount+=checked
            records.append(dict(q=q,padding=pad,N=n,world=world,
                                mode='all_prefixes' if full else
                                'complete_2d_slice_and_monotone_exclusion',
                                states_checked=checked,true_states=positive,
                                minimum_certificate=mincost,
                                omitted_region_obstruction=obstruction))

    # Direct rational determinant and finite-N formula identities.
    formulas=[]
    for q in range(3,1003):
        n=4*q
        h=F(1,n)
        det_missing_two=(F(1,4)+h)*(F(1,4)-2*h)-(F(1,4)-h)*F(1,4)
        det_missing_one=(F(1,4)+h)*(F(1,4)-h)-(F(1,4)-h)*F(1,4)
        assert det_missing_two==-2*h*h<0
        assert det_missing_one==h*(F(1,4)-h)>0
        W,X,Y=10*q+2,q-2,q-1
        ratio=1+F(X*Y,X*(W+X)+Y*(W+Y))
        assert ratio==1+F(q*q-3*q+2,22*q*q-32*q-1)
        assert 1+F(min(X,Y),W+max(X,Y))==1+F(q-2,11*q+1)
        if q in (3,4,5,10,100,1000):
            formulas.append(dict(q=q,N=n,randomised_ratio=str(ratio),
                                 deterministic_ratio=str(1+F(q-2,11*q+1))))

    weighted=[]
    for W,X,Y in product(map(F,(1,10,100)),
                         (F(1,100),F(1),F(7,3),F(100)),
                         (F(1,100),F(1),F(7,3),F(100))):
        denom=X*(W+X)+Y*(W+Y)
        theta=Y*(W+Y)/denom
        ratio=1+X*Y/denom
        assert (W+Y+theta*X)/(W+Y)==ratio
        assert (W+X+(1-theta)*Y)/(W+X)==ratio
        det=1+min(X,Y)/(W+max(X,Y))
        assert det==min(1+X/(W+Y),1+Y/(W+X))
        weighted.append(dict(W=str(W),X=str(X),Y=str(Y),theta=str(theta),
                             randomised_ratio=str(ratio),deterministic_ratio=str(det)))
    result=dict(status='PASS',
                scope='Finite explicit archives, exact support arithmetic and identities; universal claims use the proof.',
                script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                proof_sha256=hashlib.sha256((ROOT/'Fixed_Alphabet_Constant_Overhead_P22.md').read_bytes()).hexdigest(),
                worlds=records,worlds_checked=len(records),
                fully_enumerated_prefix_states=fullcount,
                complete_slice_states=slicecount,
                total_states_checked=fullcount+slicecount,
                formula_and_determinant_cases=1000,
                selected_finite_N_bounds=formulas,
                weighted_cases=weighted,weighted_cases_checked=len(weighted),
                fixed_alphabet=[['0','0'],['1','0'],['1','1'],['1','1/3'],['1/3','1/3']],
                asymptotic_randomised_lower='23/22',
                asymptotic_deterministic_lower='12/11',
                new_measurements=0,network=False,external_code=False,installs=False)
    (ROOT/'Fixed_Alphabet_Constant_Overhead_Check.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','worlds_checked',
         'fully_enumerated_prefix_states','complete_slice_states','total_states_checked',
         'formula_and_determinant_cases','weighted_cases_checked')},indent=2))


if __name__=='__main__':
    main()
