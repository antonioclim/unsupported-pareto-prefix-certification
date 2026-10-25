"""Independent exact verifier of the P56 87/80 certificate.
No producer imports. Rational function-free evaluations of the proof's
inequality are interpolated directly in the Bernstein basis on every leaf.
An independent degree-bound grid proves equality with the exported polynomial.
"""
from fractions import Fraction as F
from itertools import product
from math import comb,prod
from functools import lru_cache
from pathlib import Path
import json,time,hashlib,copy,sys
if not __debug__:raise RuntimeError('Do not run proof verification with -O')
BASE=Path(__file__).resolve().parents[1]
FILE=BASE/'evidence/upper_87_80_certificate.json'
ROOTS={'L0':(F(0),F(3,4)),'L1':(F(0),F(1,2)),'L2':(F(1,2),F(3,4)),'L3':(F(1,2),F(3,4)),'H0':(F(3,4),F(1)),'H1':(F(3,4),F(1)),'H2':(F(1,2),F(3,4)),'H3':(F(1,2),F(3,4))}
# Conservative degrees obtained from sums/products of the defining formulas,
# before cancellation: one entry for each of (g,z,w).
BOUNDS={'L0':(6,3,2),'L1':(8,5,2),'L2':(6,5,2),'L3':(7,3,2),'H0':(5,3,2),'H1':(6,4,2),'H2':(9,4,2),'H3':(7,3,2)}

def direct(name,g,z,w):
    e,lam,h=F(7,80),F(1,12),F(3,4)
    cut=name in ('L2','L3','H2','H3')
    if name=='L2':t=(h-g)*z
    elif name in ('L3','H2','H3'):t=h-g+(g*(1-g)-h+g)*z
    else:t=g*(1-g)*z
    if name in ('L0','H0'):G=g
    elif name in ('L1','L2','H1','H2'):G=g+t
    else:G=h
    if name.startswith('L'):den,num=4+G,F(19,3)*G-2*G*G
    else:den,num=G,F(87,80)*G-F(21,80)
    D=(3*e+(2*lam+e)*t)*den
    A=(1+e)*den-num;B=(lam+e)*den+num
    if cut:
        d=2*g-t;delta=g*(1-g)-t
        kden=(1-g)*d-w*delta
        un=(1-g-t)*d-2*w*delta;vn=t*d+w*delta
        return D*d*kden-A*g*d*un-B*vn*kden
    H=2-(1-g)*z;J=w*(1-z);E=H-J
    un=(1-g*z)*H-2*J;vn=g*z*H+J
    return D*H*E-A*g*H*un-B*(1-g)*vn*E

@lru_cache(None)
def inv_collocation(n):
    # Matrix maps Bernstein coefficients to polynomial values at i/n.
    if n==0:return ((F(1),),)
    a=[]
    for i in range(n+1):
        x=F(i,n)
        a.append([F(comb(n,j))*x**j*(1-x)**(n-j) for j in range(n+1)]+[F(i==j) for j in range(n+1)])
    for k in range(n+1):
        pivot=next(i for i in range(k,n+1) if a[i][k]);a[k],a[pivot]=a[pivot],a[k]
        c=a[k][k];a[k]=[v/c for v in a[k]]
        for i in range(n+1):
            if i!=k:
                c=a[i][k]
                a[i]=[u-c*v for u,v in zip(a[i],a[k])]
    return tuple(tuple(row[n+1:]) for row in a)

def bernstein_from_values(name,degree,box):
    ranges=[range(n+1) for n in degree]
    v={idx:direct(name,*[lo+(hi-lo)*F(i,n) if n else lo for i,n,(lo,hi) in zip(idx,degree,box)]) for idx in product(*ranges)}
    for axis,n in enumerate(degree):
        inv=inv_collocation(n);other=[j for j in range(3) if j!=axis];new={}
        for oi in product(*[ranges[j] for j in other]):
            key=[0,0,0]
            for j,i in zip(other,oi):key[j]=i
            line=[]
            for i in ranges[axis]:key[axis]=i;line.append(v[tuple(key)])
            for i in ranges[axis]:
                key[axis]=i;new[tuple(key)]=sum((inv[i][j]*line[j] for j in ranges[axis]),F(0))
        v=new
    return v

def leaf_box(root,path):
    box=list(root)
    for j,bit in enumerate(path):
        assert bit in '01';axis=j%3;lo,hi=box[axis];mid=(lo+hi)/2
        box[axis]=(lo,mid) if bit=='0' else (mid,hi)
    return box

def verify(data,only=None):
    assert (data['lambda'],data['excess_bound'],data['ratio'],data['cut'])==('1/12','7/80','87/80','3/4')
    assert set(data['families'])==set(ROOTS)
    result={};identity_points=0;coefficient_count=0
    for name,f in data['families'].items():
        if only and name!=only:continue
        degree=tuple(f['degrees']);bound=BOUNDS[name]
        assert all(0<=d<=b for d,b in zip(degree,bound))
        root=[ROOTS[name],(F(0),F(1)),(F(0),F(1))]
        assert [[str(x) for x in p] for p in root]==f['box']
        terms={tuple(x['exponents']):F(x['coefficient']) for x in f['power_terms']}
        assert len(terms)==len(f['power_terms'])
        assert all(all(0<=a<=d for a,d in zip(ex,degree)) for ex in terms)
        # Tensor-grid identity is exact, not random sampling: the known
        # conservative multidegree bounds make this grid unisolvent.
        for idx in product(*[range(n+1) for n in bound]):
            xyz=[lo+(hi-lo)*F(i,n) for i,n,(lo,hi) in zip(idx,bound,root)]
            exported=sum((c*prod(x**a for x,a in zip(xyz,ex)) for ex,c in terms.items()),F(0))
            assert exported==direct(name,*xyz),(name,'polynomial identity',idx)
            identity_points+=1
        paths=[x['path'] for x in f['leaves']]
        assert len(set(paths))==len(paths)
        assert all(not y.startswith(x) for i,x in enumerate(paths) for j,y in enumerate(paths) if i!=j)
        assert sum((F(1,2**len(p)) for p in paths),F(0))==1
        assert f['status']=='PASS' and not f['failed'] and f['remaining']==0
        count=0;mins=[]
        for leaf in f['leaves']:
            vals=bernstein_from_values(name,degree,leaf_box(root,leaf['path']))
            mn=min(vals.values());assert mn>=0,(name,leaf['path'],mn)
            assert mn==F(leaf['minimum']),(name,leaf['path'],'wrong minimum')
            count+=len(vals);mins.append(mn)
        coefficient_count+=count
        result[name]={'leaves':len(paths),'coefficients':count,'minimum':str(min(mins)),'degree':degree,'identity_degree_bound':bound}
    return {'families':result,'polynomial_identity_grid_points':identity_points,'exact_bernstein_coefficients':coefficient_count,'leaf_count':sum(v['leaves'] for v in result.values())}

def main():
    start=time.monotonic();data=json.loads(FILE.read_text());results=verify(data)
    mutations=[]
    for kind in ('wrong_ratio','wrong_polynomial','missing_leaf','wrong_minimum'):
        bad=copy.deepcopy(data)
        if kind=='wrong_ratio':bad['ratio']='1'
        elif kind=='wrong_polynomial':bad['families']['L0']['power_terms'][0]['coefficient']=str(F(bad['families']['L0']['power_terms'][0]['coefficient'])+1)
        elif kind=='missing_leaf':bad['families']['L0']['leaves'].pop()
        else:bad['families']['L0']['leaves'][0]['minimum']='12345'
        try:verify(bad,only='L0')
        except AssertionError:mutations.append({'kind':kind,'rejected':True})
        else:raise RuntimeError('Mutation accepted: '+kind)
    out={'status':'PASS','method':'Independent direct rational evaluations and Bernstein-basis collocation inversion; no producer imports; exact degree-bound identity grids, prefix-free full partition check.','ratio':'87/80',**results,'mutation_controls':mutations,'source_certificate_sha256':hashlib.sha256(FILE.read_bytes()).hexdigest(),'verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'seconds_observed':time.monotonic()-start,'limitation':'Proves the polynomial inequalities and checks exported partition. Policy semantics and analytic reduction require separate proof review.'}
    (BASE/'evidence/Root_87_80_Independent_P56.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
