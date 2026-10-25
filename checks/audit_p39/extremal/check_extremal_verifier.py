"""Finite cross-check of incremental threshold verifier against weight intervals.

Complete catalogues on an exact grid include ties, axis support and domination.
This corroborates the elementary implementation lemma, not the acquisition bounds.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

POINTS=list(product([F(0),F(1,2),F(3,5),F(1),F(2)],[F(0),F(1,2),F(3,5),F(1)]))

def direct_intervals(a,rivals):
    nondominated=all(not(p[0]<=a[0] and p[1]<=a[1] and p!=a) for p in rivals)
    lo,hi=F(0),F(1)
    supported=True
    for p in rivals:
        # Supporting weight (alpha,1-alpha), including both axes.
        b=p[1]-a[1];m=(p[0]-a[0])-b
        if m>0:lo=max(lo,-b/m)
        elif m<0:hi=min(hi,-b/m)
        elif b<0:supported=False
    supported=supported and lo<=hi
    return nondominated and not supported

def incremental_extrema(a,rivals):
    nw=None;se=None
    for p in rivals:
        if p[0]<=a[0] and p[1]<=a[1] and p!=a:return False
        if p[0]<a[0] and p[1]>a[1]:
            u=(p[1]-a[1])/(a[0]-p[0]);nw=u if nw is None else min(nw,u)
        elif p[0]>a[0] and p[1]<a[1]:
            v=(a[1]-p[1])/(p[0]-a[0]);se=v if se is None else max(se,v)
    return nw is not None and se is not None and nw<se

results=[]
for number_rivals in [2,3]:
    total=positive=0
    for a in POINTS:
        for rivals in product(POINTS,repeat=number_rivals):
            expected=direct_intervals(a,rivals);got=incremental_extrema(a,rivals)
            assert expected==got,(a,rivals,expected,got)
            total+=1;positive+=int(got)
    results.append({'K':number_rivals+1,'catalogues':total,'GOOD':positive})
report={'status':'PASS','scope':'Finite complete-catalogue verifier equivalence with exact ties and axes; not a proof of acquisition ratios or arbitrary rational universality','grid':[[str(x),str(y)] for x,y in POINTS],'results':results,'total_catalogues':sum(r['catalogues'] for r in results)}
Path(__file__).with_name('Extremal_Verifier_Check_P39.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report['results']))
