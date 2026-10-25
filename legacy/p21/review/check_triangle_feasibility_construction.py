"""Independent arithmetic audit of an explicit rational feasibility construction.
Tests all oriented length triples through N=24. This does not prove necessity;
constructive sufficiency for all N is analytic. Own code, stdlib only.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json


def support(p,points):
    low,high=F(0),F(1)
    for v in points:
        a=v[0]-p[0]; b=v[1]-p[1]; slope=a-b
        if slope==0:
            if b<0:return False
        elif slope>0:low=max(low,-b/slope)
        else:high=min(high,-b/slope)
        if low>high:return False
    return True

counts=[]; total=0; feasible_total=0; minimum_det=None
for N in range(1,25):
    feasible=0
    for a,i,j in product(range(1,N+1),repeat=3):
        total+=1
        Z=i+2*j+2*a-4*N
        E=Z*Z-4*(2*N-a-i)*(2*N-a-j)
        if not (Z>0 and E>0):continue
        feasible+=1; feasible_total+=1
        t,s,r=F(N-a,N),F(N-i,N),F(N-j,N)
        epsilon=F(E,8*N*j)
        x=1-r-t-epsilon
        y=(1-s-2*t)/2-epsilon
        candidate_row=(N*x/a,N*y/a)
        rows=[candidate_row,(F(1,2),F(1,2)),(F(1),F(0))]
        assert all(0<=f<=c<=1 for c,f in rows)
        lengths=[a,i,j]
        lo=[tuple(v*F(length,N) for v in row) for row,length in zip(rows,lengths)]
        hi=[tuple(v+F(N-length,N) for v in l) for l,length in zip(lo,lengths)]
        for rival in lo[1:]:
            assert not (all(u<=v for u,v in zip(rival,hi[0])) and any(u<v for u,v in zip(rival,hi[0])))
        assert not support(lo[0],hi[1:]),(N,a,i,j)
        A=lo[0][0]-hi[1][0]; C=hi[1][1]-lo[0][1]
        D=hi[2][0]-lo[0][0]; EE=lo[0][1]-hi[2][1]
        determinant=A*EE-C*D
        assert determinant==F(E,8*N*N)>0
        minimum_det=determinant if minimum_det is None else min(minimum_det,determinant)
    counts.append({'N':N,'all_oriented_triples':N**3,'feasible_constructed':feasible})
out={'status':'PASS','all_oriented_triples':total,'feasible_constructed':feasible_total,
     'max_N':24,'minimum_constructed_strict_determinant':str(minimum_det),
     'epsilon':'[Z^2-4(2N-a-i)(2N-a-j)]/(8Nj)',
     'scope':'Finite constructive arithmetic checks; universal iff criterion requires analytic proof.',
     'counts':counts}
Path(__file__).with_name('Triangle_Feasibility_Construction_Check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='counts'},indent=2))
