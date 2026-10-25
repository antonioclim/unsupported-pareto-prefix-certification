"""Independent exact check of every monotone two-chain N5 certificate pattern.
The abstract patterns overapproximate actual continuous archives. Geometry and
screening soundness are established analytically in the accompanying review.
Own standard-library code, no import of a producer checker or scientific module.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib
import json


def true(i,j,im,jm):
    return (j==5 and i>=im) or (i==5 and j>=jm)


def path_cost(i,j,im,jm,first):
    # Candidate census already paid. Stop at every TRUE state.
    while not true(i,j,im,jm):
        if first=='L' and i<5:i+=1
        elif first=='R' and j<5:j+=1
        elif i<5:i+=1
        else:j+=1
    return 5+i+j


def policy(g,im,jm,hi,hj,deterministic=False):
    if true(hi,hj,im,jm):return Q(5+hi+hj)
    if g<=Q(1,5):return Q(path_cost(hi,hj,im,jm,'L'))
    if g>=Q(3,5):return Q(path_cost(hi,hj,im,jm,'R'))
    if g<=Q(2,5):
        left=path_cost(4,4,im,jm,'L')
        right=path_cost(4,4,im,jm,'R')
        return Q(left) if deterministic else Q(left+right,2)
    if hi==5 or hj==5:
        return Q(path_cost(hi,hj,im,jm,'R' if hi==5 else 'L'))
    i,j=max(3,hi),max(4,hj)
    left=path_cost(i,j,im,jm,'L')
    right=path_cost(i,j,im,jm,'R')
    return Q(right) if deterministic else Q(left+3*right,4)


def main():
    checked=0
    maxcost={c:Q(0) for c in range(11,16)}
    maxdet={c:Q(0) for c in range(11,16)}
    allcosts=[]
    for g in [Q(k,20) for k in range(21)]:
        for im,jm in product(range(1,6),range(3,6)):
            if im<5 and not g>1-Q(im,5):continue
            if jm<5 and not g<2*Q(jm,5)-1:continue
            c=10+min(im,jm)
            for hi,hj in product(range(1,im+1),range(1,jm+1)):
                cost=policy(g,im,jm,hi,hj)
                det=policy(g,im,jm,hi,hj,True)
                maxcost[c]=max(maxcost[c],cost)
                maxdet[c]=max(maxdet[c],det)
                bound={11:Q(11),12:Q(12),13:Q(27,2),14:Q(59,4),15:Q(15)}[c]
                assert cost<=bound,(g,im,jm,hi,hj,cost,bound)
                assert det<=(c if c<=13 or c==15 else 15)
                checked+=1
    # All mixture class inequalities are affine-polynomial identities in F.
    # d=5F+67,p=4(F+14)/d. The margin after multiplication by d is:
    # 4(F+C) - (5F+67)(B-C) - 4(F+14)(A-B).
    classes=[('C11',11,Q(11),15),('C12',12,Q(12),15),
             ('C13',13,Q(27,2),15),('C14_no_partial',14,Q(59,4),15),
             ('C14_partial',14,Q(15),14),('C15',15,Q(15),15)]
    polys={}
    for name,c,a,b in classes:
        linear=4-5*(b-c)-4*(a-b)
        constant=4*c-67*(b-c)-56*(a-b)
        assert linear>=0 and constant>=0
        polys[name]={'constant':str(constant),'coefficient_F':str(linear),
                     'nonnegative_for_every_F_ge_0':True}
    assert polys['C11']['constant']==polys['C11']['coefficient_F']=='0'
    assert polys['C14_partial']['constant']==polys['C14_partial']['coefficient_F']=='0'
    files=[Path('p22/upper/N5_Upper_Proof.txt'),Path('p22/three_tail/Triangle_N5_Two_World_Lower_Proof.txt')]
    result={'status':'PASS','abstract_gap_threshold_screen_states_checked':checked,
      'candidate_census_policy_max_costs':{str(k):str(v) for k,v in maxcost.items()},
      'deterministic_policy_max_costs':{str(k):str(v) for k,v in maxdet.items()},
      'all_F_ge_0_symbolic_margins':polys,
      'source_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
      'scope':'Exact arithmetic check of an abstract overapproximation, not numerical sampling of the continuum or a formal proof assistant.'}
    Path(__file__).with_name('N5_Upper_Independent_Check.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
