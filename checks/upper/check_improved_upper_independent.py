#!/usr/bin/env python3
"""Independent direct Bernstein interpolation on each certified box.

No imports from the producer. Evaluates the unexpanded polynomial formula
exactly on tensor grids, then inverts Bernstein collocation matrices. This
checks the algebraic certificate, not the policy's mathematical reduction.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb
from pathlib import Path
import hashlib
import json

def inverse(matrix):
    n=len(matrix)
    m=[row[:]+[Q(i==j) for j in range(n)] for i,row in enumerate(matrix)]
    for k in range(n):
        pivot=next(i for i in range(k,n) if m[i][k])
        m[k],m[pivot]=m[pivot],m[k]
        divisor=m[k][k]
        m[k]=[v/divisor for v in m[k]]
        for i in range(n):
            if i!=k:
                a=m[i][k]
                m[i]=[x-a*y for x,y in zip(m[i],m[k])]
    return [row[n:] for row in m]

def bernstein_inverse(n):
    return inverse([[Q(comb(n,j))*Q(i,n)**j*(1-Q(i,n))**(n-j)
                     for j in range(n+1)] for i in range(n+1)])

def bounds(path):
    intervals=[[Q(0),Q(1)] for _ in range(3)]
    for axis,side in path:
        lo,hi=intervals[axis];mid=(lo+hi)/2
        intervals[axis]=[lo,mid] if side==0 else [mid,hi]
    return intervals

def value(g,z,w,e,j):
    t=g*(1-g)*z
    H=2-(1-g)*z
    J=w*(1-z)
    E=H-J
    Vn=g*z*H+J
    Un=(1-g*z)*H-2*J
    G=g+j*t
    A=4*(1+e)+(e-4)*G
    B=4*e+(5+e)*G
    D=e*(3+t)*(4+G)
    return D*H*E-A*g*H*Un-B*(1-g)*Vn*E

def leaf_coefficients(box,n,e,j):
    keys=list(product(*(range(d+1) for d in n)))
    arr={k:value(*(box[a][0]+(box[a][1]-box[a][0])*Q(k[a],n[a])
                   for a in range(3)),e,j) for k in keys}
    for axis in range(3):
        inv=bernstein_inverse(n[axis]);new={}
        for k in keys:
            total=Q(0)
            for i in range(n[axis]+1):
                idx=list(k);idx[axis]=i
                total+=inv[k[axis]][i]*arr[tuple(idx)]
            new[k]=total
        arr=new
    return arr

def verify_cover(leaves):
    paths=[tuple(tuple(x) for x in leaf['path']) for leaf in leaves]
    assert len(set(paths))==len(paths)
    assert sum((Q(1,2**len(p)) for p in paths),Q(0))==1
    for i,p in enumerate(paths):
        for j,q in enumerate(paths):
            if i!=j: assert p!=q[:len(p)],'Overlapping dyadic leaves'
        for depth,(axis,side) in enumerate(p):
            assert axis==depth%3 and side in (0,1)

def main():
    source=Path(__file__).with_name('Improved_Upper_Exact_Certificate.json')
    data=json.loads(source.read_text())
    # These degree bounds follow from the displayed unexpanded formula;
    # they are not trusted metadata supplied by the certificate producer.
    target=[r for r in data['polynomial_certificates'] if r['excess']=='73/800']
    assert len(target)==2, 'Exactly two endpoint certificates are required'
    assert sorted(r['endpoint'] for r in target)==[0,1], 'Missing or duplicate endpoint'
    expected_degrees={0:[5,3,2],1:[6,4,2]}
    for record in target:
        assert record['degrees']==expected_degrees[record['endpoint']], 'Invalid polynomial degree bounds'
        assert record['status']=='PASS', 'Uncertified endpoint'
    results=[]
    for record in target:
        verify_cover(record['leaves'])
        n=record['degrees'];count=0;mins=[]
        for leaf in record['leaves']:
            coeff=leaf_coefficients(bounds(leaf['path']),n,Q(record['excess']),record['endpoint'])
            low=min(coeff.values());assert low>=0
            assert low==Q(leaf['minimum_coefficient'])
            count+=len(coeff);mins.append(low)
        results.append(dict(endpoint=record['endpoint'],status='PASS',
                            boxes=len(mins),coefficients=count,
                            minimum_coefficient=str(min(mins))))
    assert len(results)==2
    out=dict(status='PASS',method='Exact tensor Bernstein collocation inversion from unexpanded formula',
             results=results,total_coefficients=sum(x['coefficients'] for x in results),
             input_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
             script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    Path(__file__).with_name('Improved_Upper_Independent_Check.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()
