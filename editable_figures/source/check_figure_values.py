#!/usr/bin/env python3
"""Check the exported values independently of the plotting module (stdlib only)."""

# Assertion-based verification must not run with its checks disabled.
if not __debug__:
    raise SystemExit("Run without Python optimisation (-O or -OO).")

import argparse
from fractions import Fraction as Q
import json
from pathlib import Path


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('values',type=Path,nargs='?',default=Path(__file__).parent/'generated'/'Figure_Exact_Values.json')
    args=p.parse_args();v=json.loads(args.values.read_text())
    f1=v['Fig2'];f2=v['Fig3'];n=f2['N'];q=f2['q']
    assert n==12 and q==3 and n==4*q
    zero=(0,0);x=(1,0);xy=(1,1)
    a=[x]*(2*q)+[xy]*q+[zero]*(q-1)
    l=[xy]*q+[zero]*(2*q)+[xy]*(q-1)
    worlds={'U':{'A':a+[zero],'L':l+[zero],'R':[x]*n},
            'V':{'A':a+[x],'L':l+[xy],'R':[x]*n}}
    means={}
    for name,world in worlds.items():
        means[name]={}
        for configuration,rows in world.items():
            assert len(rows)==n
            assert all(list(map(str,row)) in f2['alphabet'] for row in rows)
            result=[sum(Q(r[k]) for r in rows)/n for k in (0,1)]
            assert result==list(map(Q,f2['worlds'][name][configuration]))
            means[name][configuration]=list(map(str,result))
        a,l,r=(tuple(map(Q,f2['worlds'][name][k])) for k in ('A','L','R'))
        # Direct 2D determinant: positive means A lies above the rival chord.
        determinant=(r[0]-l[0])*(a[1]-l[1])-(r[1]-l[1])*(a[0]-l[0])
        assert determinant/(r[0]-l[0])==Q(f2['candidate_vertical_gap_above_rival_chord'][name])>0
        assert a[0]>l[0] and a[1]<l[1] and a[0]<r[0] and a[1]>r[1]
    threshold_points=0
    for row in f1['boundaries']:
        n=row['N']
        # Reconstruct the exact upper edges by testing the inequalities at rational candidates.
        expected={'zero_overhead_upper':min(Q(1),Q(2,max(1,n-1))),
                  'first_supercritical_upper':min(Q(1),Q(3,max(1,n-1))),
                  'general_exact_upper':Q(1,n)}
        for key,val in expected.items():assert Q(row[key])==val
        candidates={Q(1),Q(1,n),Q(row['zero_overhead_upper']),Q(row['first_supercritical_upper'])}
        for d in candidates:
            regime='zero' if d*(n-1)<=2 else ('first' if d*(n-1)<=3 else 'remaining')
            assert (regime=='zero')==(d<=Q(row['zero_overhead_upper']))
            assert (regime=='first')==(Q(row['zero_overhead_upper'])<d<=Q(row['first_supercritical_upper']))
            threshold_points+=1
    b=f2['bounds']
    assert [(Q(x['lower']),Q(x['upper'])) for x in b[:2]]==[(Q(23,22),Q(12,11)),(Q(12,11),Q(12,11))]
    assert Q(b[2]['lower'])==Q(12,11) and b[2]['upper_expression']=='3/(4*sqrt(2)-3)'
    assert Q(12,11)-Q(12,11)==Q(f2['candidate_complete_bound_gap'])==0
    assert Q(12,11)-Q(23,22)==Q(f2['unrestricted_randomised_bound_gap'])==Q(1,22)
    assert f1['finite_marker']['randomised']=='71/67' and f1['finite_marker']['deterministic']=='15/14'
    assert f1['finite_marker']['N']==5 and Q(f1['finite_marker']['d'])==1
    assert f1['domain']['d']=='0<d<=1'
    assert f1['d_zero'].startswith('excluded')
    assert 'every positive archive' in b[1]['policy_class']
    assert 'whose convergence is not proved' in f2['bounds_scope']['meaning']
    assert Q(f2['candidate_census_asymptotic_limit'])==Q(12,11)
    assert f2['exact_global_limits']=={'randomised_candidate_census':'12/11','randomised_unrestricted':'open','deterministic_unrestricted':'open'}
    prefix=v.get('Fig1')
    if prefix is not None:
        mix=Q(prefix['prob_candidate_first'])
        assert prefix['common_prefix']==[2,3,1] and prefix['minimum_costs']=={'I':8,'II':7}
        assert (mix*9+(1-mix)*8)/8==(mix*7+(1-mix)*9)/7==Q(prefix['displayed_ratio'])==Q(25,23)
    print(json.dumps({'schema':'sicomp-figure-values-check-p44-v1','revision':'P44','status':'PASS','row_means_reconstructed':means,
        'prefix_route_mixture_checked':prefix is not None,'threshold_points_checked':threshold_points,'scope':'Independent arithmetic and semantic checks of exported constants, not theorem proofs'},indent=2))


if __name__=='__main__':main()
