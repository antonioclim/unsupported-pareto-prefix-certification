"""Independent exact-rational P22 N=5 hard-world and policy-envelope audit.
Imports only the independent review module, not either producer's code.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
from check_band_independent import corners, is_true

n=5
common_a=[(Q(79,80),Q(1,8))]*4
common_l=[(Q(51,100),Q(51,100))]+[(Q(13,50),Q(13,50))]*3
r=[(Q(1),Q(0))]*5
worlds=[ [common_a+[(Q(0),Q(0))], common_l+[(Q(13,50),Q(13,50))],r],
         [common_a+[(Q(1),Q(0))], common_l+[(Q(1),Q(1))],r] ]
states=0
for wi,w in enumerate(worlds):
    assert all(0<=f<=c<=1 for g in w for c,f in g)
    boxes=[corners(g) for g in w]
    yes=[]
    for state in product(range(6),repeat=3):
        states+=1
        if is_true(boxes,state):
            yes.append(state)
    expected=[(4,5,5),(5,5,5)] if wi==0 else [(5,i,5) for i in range(1,6)]
    assert yes==expected,(wi,yes)

feasible=[]
for a,i,j in product(range(1,6),repeat=3):
    z=i+2*j+2*a-20
    if z>0 and z*z>4*(10-a-i)*(10-a-j):
        feasible.append((a,i,j))
minimal=[p for p in feasible if not any(q!=p and all(x<=y for x,y in zip(q,p)) for q in feasible)]
assert minimal==[(4,5,5),(5,1,5),(5,5,3)]

setup_values=[Q(0),Q(1,13),Q(1,2),Q(1),Q(5),Q(100),Q(10**6)]
cost_cases=0
for F in setup_values:
    den=5*F+67
    prob=4*(F+14)/den
    target=1+4/den
    # Full exhaustive C* classes of the analytical policy proof.
    for c,acost,bcost in [(11,Q(11),15),(12,Q(12),15),
                           (13,Q(27,2),15),(14,Q(59,4),15),
                           (14,Q(15),14),(15,Q(15),15)]:
        ratio=(F+prob*acost+(1-prob)*bcost)/(F+c)
        assert ratio<=target,(F,c,ratio,target)
        cost_cases+=1
    q=4*(F+14)/den
    assert (F+14+q)/(F+14)==target
    assert (F+15-4*q)/(F+11)==target
    for c,detcost in [(11,11),(12,12),(13,13),(14,15),(15,15)]:
        assert Q(F+detcost,F+c)<=1+1/(F+14)
        cost_cases+=1

out={"status":"PASS","independent_code":True,"exact_rational_arithmetic":True,
     "hard_worlds":2,"prefix_states":states,"length_shapes":125,
     "minimal_feasible_shapes":minimal,"setup_values":[str(x) for x in setup_values],
     "policy_cost_envelope_checks":cost_cases,"randomised_optimum_at_zero_setup":"71/67",
     "deterministic_optimum_at_zero_setup":"15/14",
     "limits":"Hard archives and policy envelope arithmetic only; continuous-policy soundness checked analytically in separate review."}
Path(__file__).with_name('N5_Independent_Checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
