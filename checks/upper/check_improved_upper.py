#!/usr/bin/env python3
"""Exact polynomial certificate for a universal triangular acquisition policy.

Own standard-library code. Bernstein coefficients on rational sub-boxes
certify polynomial nonnegativity over a continuous parameter cube. This is
not a sampling test. Policy validity and the polynomial reduction remain
mathematical arguments in the companion proof.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb
from pathlib import Path
import hashlib
import json

ZERO=(0,0,0)
def const(x): return {ZERO:Q(x)} if x else {}
def var(i):
    k=[0]*3;k[i]=1
    return {tuple(k):Q(1)}
def add(*polys):
    out={}
    for p in polys:
        for k,v in p.items():out[k]=out.get(k,Q(0))+v
    return {k:v for k,v in out.items() if v}
def scale(p,x): return {k:v*x for k,v in p.items() if v*x}
def mul(a,b):
    out={}
    for k,v in a.items():
        for l,w in b.items():
            m=tuple(x+y for x,y in zip(k,l));out[m]=out.get(m,Q(0))+v*w
    return {k:v for k,v in out.items() if v}
def sub(a,b):return add(a,scale(b,-1))
def bernstein(p):
    n=tuple(max(k[d] for k in p) for d in range(3))
    out={}
    for i in product(*(range(v+1) for v in n)):
        value=Q(0)
        for k,c in p.items():
            if all(k[d]<=i[d] for d in range(3)):
                w=c
                for d in range(3):w*=Q(comb(i[d],k[d]),comb(n[d],k[d]))
                value+=w
        out[i]=value
    return n,out
def split(n,b,axis):
    left={};right={}
    others=[d for d in range(3) if d!=axis]
    for fixed in product(*(range(n[d]+1) for d in others)):
        key=[0]*3
        for d,v in zip(others,fixed):key[d]=v
        row=[]
        for j in range(n[axis]+1):key[axis]=j;row.append(b[tuple(key)])
        l=[row[0]];r=[row[-1]]
        while len(row)>1:
            row=[(row[j]+row[j+1])/2 for j in range(len(row)-1)]
            l.append(row[0]);r.append(row[-1])
        r.reverse()
        for j in range(n[axis]+1):
            key[axis]=j;left[tuple(key)]=l[j];right[tuple(key)]=r[j]
    return left,right
def certify(p,max_depth=24):
    n,b=bernstein(p);leaves=[];todo=[(b,(),0)]
    while todo:
        coeff,path,depth=todo.pop()
        low=min(coeff.values())
        if low>=0:
            leaves.append({'path':list(path),'minimum_coefficient':str(low)})
            continue
        if depth>=max_depth:
            raise AssertionError(('Uncertified box',path,str(low)))
        axis=depth%3
        left,right=split(n,coeff,axis)
        todo.append((right,path+((axis,1),),depth+1))
        todo.append((left,path+((axis,0),),depth+1))
    return {'degrees':list(n),'polynomial_terms':len(p),'leaf_count':len(leaves),'max_depth':max(len(x['path']) for x in leaves),'leaves':leaves}
def polynomial(excess,endpoint):
    one=const(1);g,z,w=map(var,range(3));omg=sub(one,g);omz=sub(one,z)
    t=mul(mul(g,omg),z)
    H=sub(const(2),mul(omg,z))
    J=mul(w,omz); E=sub(H,J)
    Vn=add(mul(mul(g,z),H),J)
    Un=sub(mul(sub(one,mul(g,z)),H),scale(J,2))
    G=g if endpoint==0 else add(g,t)
    # p=5G/(4+G). Multiply desired excess gap by 4+G.
    A=add(const(4*(1+excess)),scale(G,excess-4))
    B=add(const(4*excess),scale(G,5+excess))
    D=scale(mul(add(const(3),t),add(const(4),G)),excess)
    return sub(sub(mul(mul(D,H),E),mul(mul(mul(A,g),H),Un)),mul(mul(mul(B,omg),Vn),E))
def main():
    results=[]
    for e in [Q(11,120),Q(73,800)]:
        for endpoint in (0,1):
            p=polynomial(e,endpoint)
            try:
                result=certify(p,max_depth=36)
                result.update(status='PASS',excess=str(e),endpoint=endpoint)
            except AssertionError as error:
                result={'status':'UNCERTIFIED','excess':str(e),'endpoint':endpoint,'detail':str(error)}
            result['polynomial']={','.join(map(str,k)):str(v) for k,v in sorted(p.items())}
            results.append(result)
            print(json.dumps({k:v for k,v in result.items() if k not in ('leaves','polynomial')}),flush=True)
    out={'status':'PASS' if all(x['status']=='PASS' for x in results) else 'PARTIAL',
         'policy':'p_SE(G)=5G/(4+G)',
         'polynomial_certificates':results,
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'scope':'Exact rational positivity certificate, contingent on the analytic C8-C11 reduction. Not an optimality proof.'}
    Path(__file__).with_name('Improved_Upper_Exact_Certificate.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
