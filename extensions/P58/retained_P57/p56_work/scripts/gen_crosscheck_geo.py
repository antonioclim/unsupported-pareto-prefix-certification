#!/usr/bin/env python3
"""Independent general-LP oracle audit of the planar sorted-stream solver."""
import importlib.util
from pathlib import Path
from fractions import Fraction as F
from random import Random
from itertools import product
import json
import hashlib
ROOT=Path(__file__).resolve().parents[1]
def load(name,fn):
    sp=importlib.util.spec_from_file_location(name,ROOT/'scripts'/fn);mod=importlib.util.module_from_spec(sp);sp.loader.exec_module(mod);return mod
own=load('own','gen_endpoint_margin_checks.py')
geo=load('geo','geo_comparator.py')
rng=Random(5602);cases=0;states=0;positive=0
for k,n in ((3,2),(3,3),(4,2),(4,3),(5,2)):
    for t in range(12):
        if t<6:
            means=[(F(3,5),F(3,5)),(F(1,5),F(4,5)),(F(4,5),F(1,5))]+[(F(3,5),F(3,5))]*(k-3)
            rows=[]
            for p in means:
                eps=tuple(F(rng.randint(-2,2),40) for _ in range(2))
                rows.append([tuple(x+y for x,y in zip(p,eps))]+[p]*(n-2)+[tuple(x-y for x,y in zip(p,eps))])
        else:rows=[[tuple(F(rng.randint(0,5),5) for _ in range(2)) for _ in range(n)] for _ in range(k)]
        ww=[[F(1,n)]*n for _ in range(k)]
        prices=[[F(rng.randint(1,30),rng.randint(1,7)) for _ in range(n)] for _ in range(k)]
        setup=F(rng.randint(0,6),7)
        co=own.arrays(rows,ww);pc=[]
        for pp in prices:
            arr=[F(0)]
            for p in pp:arr.append(arr[-1]+p)
            pc.append(arr)
        opt=None
        for bb in product(range(n+1),repeat=k):
            states+=1
            if own.robust(co,bb):
                val=setup+sum(pc[g][bb[g]] for g in range(k))
                if opt is None or val<opt:opt=val
        got,_=geo.comparator(rows,prices,setup)
        assert (got is None)==(opt is None)
        if got:
            assert got['cost']==opt
            assert own.robust(co,got['prefix'])
            positive+=1
        cases+=1
# Final generalized API: unequal lengths and nonuniform importance weights.
weighted_cases=0
for t in range(40):
    k=3+t%3; ns=[rng.randint(1,4) for _ in range(k)]
    means=[(F(3,5),F(3,5)),(F(1,5),F(4,5)),(F(4,5),F(1,5))]+[(F(9,10),F(9,10))]*(k-3)
    rows=[];ww=[];prices=[]
    for g,n in enumerate(ns):
        aa=[rng.randint(1,9) for _ in range(n)];ww.append([F(x,sum(aa)) for x in aa])
        prices.append([F(rng.randint(1,30),rng.randint(1,7)) for _ in range(n)])
        rows.append([means[g]]*n if t<25 else [tuple(F(rng.randint(0,5),5) for _ in range(2)) for j in range(n)])
    setup=F(rng.randint(0,6),7);co=own.arrays(rows,ww);pc=[]
    for pp in prices:
        arr=[F(0)]
        for p in pp:arr.append(arr[-1]+p)
        pc.append(arr)
    opt=None
    for bb in product(*(range(n+1) for n in ns)):
        states+=1
        if own.robust(co,bb):
            val=setup+sum(pc[g][bb[g]] for g in range(k))
            if opt is None or val<opt:opt=val
    got,_=geo.comparator(rows,prices,setup,ww)
    assert (got is None)==(opt is None)
    if got:
        assert got['cost']==opt
        assert own.robust(co,got['prefix'])
        positive+=1
    cases+=1;weighted_cases+=1
report={'status':'PASS','archives':cases,'weighted_unequal_archives':weighted_cases,'positive':positive,'geo_source_sha256':hashlib.sha256((ROOT/'scripts'/'geo_comparator.py').read_bytes()).hexdigest(),'prefixes_exhausted':states,'oracle':'Separate exact d-dimensional rational simplex-vertex feasibility; no use of geo interval_oracle or brute','scope':'Finite corroboration plus manual proof review; not formalverification'}
(ROOT/'evidence'/'Generalization_Crosscheck_Geometry_P56.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
