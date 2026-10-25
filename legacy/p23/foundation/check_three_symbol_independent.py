#!/usr/bin/env python3
"""Independent exact interval-based review of P23's three-symbol archives.

No producer imports. The proof supplies all-N and all-algorithm arguments.
"""
from fractions import Fraction as F
from itertools import product, combinations
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
PROOF = HERE.parent/'lower/Minimal_Alphabet_Persistent_Overhead_P23.md'

def support(p, others):
    lo, hi = F(0), F(1)
    for z in others:
        b = z[1]-p[1]
        a = z[0]-p[0]-b
        if a > 0:
            lo = max(lo, -b/a)
        elif a < 0:
            hi = min(hi, -b/a)
        elif b < 0:
            return False
    return lo <= hi

def dominates(x, y):
    return x[0] <= y[0] and x[1] <= y[1] and x != y

def corners(rows):
    n = len(rows)
    ans = []
    x = y = 0
    for k in range(n+1):
        if k:
            x += rows[k-1][0]
            y += rows[k-1][1]
        ans.append(((F(x,n),F(y,n)),(F(x+n-k,n),F(y+n-k,n))))
    return ans

def positive(grid, lengths):
    a, l, r = (grid[g][k] for g,k in enumerate(lengths))
    return not any(dominates(z[0],a[1]) for z in (l,r)) and not support(a[0],(l[1],r[1]))

def archive(q,pad,world):
    n0 = 4*q
    A = [(1,0) if k<2*q else (1,1) if k<3*q else (0,0) for k in range(n0)]
    L = [(1,1) if k<q or k>=3*q else (0,0) for k in range(n0)]
    R = [(1,0)]*n0
    A[-1] = (1,0) if world=='V' else (0,0)
    L[-1] = (1,1) if world=='V' else (0,0)
    return [[(0,0)]*pad+g for g in (A,L,R)]

def main():
    cases = [(3,0),(3,1),(3,2),(3,3),(4,0),(4,3),(6,0),(8,2)]
    world_records = []
    states = 0
    for q,pad in cases:
        for world in ('U','V'):
            rows=archive(q,pad,world); n=len(rows[0]); grid=list(map(corners,rows))
            assert set(sum(rows,[]))=={(0,0),(1,0),(1,1)}
            other=archive(q,pad,'V' if world=='U' else 'U')
            assert all(rows[g][:-1]==other[g][:-1] for g in (0,1))
            assert rows[2]==other[2]
            true_states=[]
            for a,l,r in product(range(n+1),repeat=3):
                got=positive(grid,(a,l,r))
                expected=(l==n and a>=n-q+2 and r>=n-1) if world=='U' else (a==n and l>=n-q+1 and r>=n-1)
                assert got==expected,(q,pad,world,(a,l,r),got,expected)
                if got:true_states.append((a,l,r))
                states+=1
            least=(n-q+2,n,n-1) if world=='U' else (n,n-q+1,n-1)
            assert least in true_states and all(all(x>=y for x,y in zip(s,least)) for s in true_states)
            world_records.append({'q':q,'padding':pad,'N':n,'world':world,'all_prefix_states':(n+1)**3,'positive_states':len(true_states),'least_TRUE_prefix':least,'minimum_cost':sum(least)})
    bad=list(map(corners,archive(2,0,'V')))
    assert not positive(bad,(8,7,7)) and positive(bad,(8,7,8))
    price_cases=0
    for W,X,Y in product((F(1,3),F(17,5),F(83)),(F(1,7),F(2),F(13)),(F(1,9),F(3),F(19))):
        theta=Y*(W+Y)/(X*(W+X)+Y*(W+Y))
        ratio=1+X*Y/(X*(W+X)+Y*(W+Y))
        assert 0<theta<1
        assert (W+Y+theta*X)/(W+Y)==ratio==(W+X+(1-theta)*Y)/(W+X)
        # On either side of the crossing the appropriate affine lower envelope
        # is at least the value at the crossing, including highly unequal prices.
        for prob in (F(0),theta/2,theta,(theta+1)/2,F(1)):
            assert max((W+Y+prob*X)/(W+Y),(W+X+(1-prob)*Y)/(W+X))>=ratio
        det=min(max(F(1),(W+X+Y)/(W+Y)),max((W+X+Y)/(W+X),F(1)))
        assert det==1+min(X,Y)/(W+max(X,Y))
        price_cases+=1
    two_symbol_cases=0
    points=list(product((-2,0,3),repeat=2))
    fractions=(F(0),F(1,5),F(1,2),F(4,5),F(1))
    for x,y in combinations(points,2):
        means=[tuple(F(x[j])+t*(y[j]-x[j]) for j in range(2)) for t in fractions]
        for cand,L,R in product(means,repeat=3):
            assert dominates(L,cand) or dominates(R,cand) or support(cand,(L,R))
            two_symbol_cases+=1
    lattice_records=[]
    five_row_positive_triples=[]
    for n in range(1,6):
        means=[(F(c,n),F(f,n)) for c in range(n+1) for f in range(c+1)]
        number=good=0
        for cand,L,R in product(means,repeat=3):
            is_good=not dominates(L,cand) and not dominates(R,cand) and not support(cand,(L,R))
            number+=1;good+=is_good
            if n==5 and is_good:five_row_positive_triples.append((cand,L,R))
        assert bool(good)==(n>=5)
        lattice_records.append({'N':n,'attainable_means':len(means),'all_ordered_mean_triples':number,'GOOD_triples':good})
    final_row_omissions=0
    for triple in five_row_positive_triples:
        for group in range(3):
            total_c,total_f=(int(5*x) for x in triple[group])
            feasible_last=[]
            if total_c<5:feasible_last.append((0,0))
            if total_f<total_c:feasible_last.append((1,0))
            if total_f>0:feasible_last.append((1,1))
            for last in feasible_last:
                intervals=[(z,z) for z in triple]
                low=(F(total_c-last[0],5),F(total_f-last[1],5))
                intervals[group]=(low,(low[0]+F(1,5),low[1]+F(1,5)))
                candidate,L,R=intervals
                is_true=not dominates(L[0],candidate[1]) and not dominates(R[0],candidate[1]) and not support(candidate[0],(L[1],R[1]))
                assert not is_true,(triple,group,last)
                final_row_omissions+=1
    for n in range(5,101):
        cand=(F(4,n),F(1,n)); L=(F(2,n),F(2,n)); R=(F(5,n),F(0))
        assert not dominates(L,cand) and not dominates(R,cand) and not support(cand,(L,R))
        assert not dominates((F(1),F(1)),cand)
    result={'status':'PASS','proof_sha256':hashlib.sha256(PROOF.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'method':'Independent Fraction-valued corner arrays and intersection of closed supporting-weight intervals; no producer imports.','worlds':world_records,'world_count':len(world_records),'fully_enumerated_prefix_states':states,'priced_pair_cases':price_cases,'two_symbol_no_GOOD_cases':two_symbol_cases,'complete_lattice_checks':lattice_records,'N5_maximal_proper_prefix_obstructions':final_row_omissions,'N5_all_positive_triples':len(five_row_positive_triples),'padded_positive_checks':96,'q2_negative_control':{'8_7_7':False,'8_7_8':True},'scope':'Finite corroboration of explicit archives and arithmetic. The all-N, minimality and algorithm quantifiers are reviewed analytically in a separate report; no continuum enumeration or formal proof.'}
    (HERE/'Three_Symbol_Independent_Check.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','world_count','fully_enumerated_prefix_states','priced_pair_cases','two_symbol_no_GOOD_cases')},indent=2))

if __name__=='__main__':main()
