"""Independent P56 APEX evidence verifier: imports no policy/producer code."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
from collections import defaultdict,Counter
import json,hashlib
B=Path(__file__).resolve().parents[2]
R=B/'p55_work/replay/reproduction/legacy'
O=B/'p56_work/evidence'
report=json.loads((O/'practical_negative_stopping_P56.json').read_text())
fixture=json.loads((R/'p17/apex_replay/fixtures_v1.json').read_text())

def dom(x,y):return x!=y and all(a<=b for a,b in zip(x,y))
def support(p,rs):
    candidates={Q(0),Q(1)}
    for x,y in rs:
        dx,dy=x-p[0],y-p[1]
        if dx!=dy:
            a=-dy/(dx-dy)
            if 0<=a<=1:candidates.add(a)
    return any(all(a*(x-p[0])+(1-a)*(y-p[1])>=0 for x,y in rs) for a in candidates)
def good(rows):
    p=[tuple(sum(g[i][d] for i in range(3))/3 for d in (0,1)) for g in rows]
    return not any(dom(x,p[0]) for x in p[1:]) and not support(p[0],p[1:])

tasks={}
for proto,count in fixture['protocols'].items():
    raw=json.loads((R/f'p9/licence/apex_dataset/{proto}_results.json').read_text(),parse_float=Q)
    gs=defaultdict(list)
    for row in raw:gs[tuple(sorted(row['params'].items()))].append(row)
    groups=[]
    for key in sorted(gs):
        entries=sorted(gs[key],key=lambda r:r['id'])
        groups.append([(Q(r['metrics']['latency'])/(Q(r['metrics']['latency'])+100),1-Q(r['metrics']['reliability'])) for r in entries])
    assert len(groups)==count
    ranked=sorted((hashlib.sha256((fixture['selection_seed']+'|'+proto+'|'+','.join(map(str,idx))).encode()).hexdigest(),idx) for idx in combinations(range(count),3))[:fixture['triples_per_protocol']]
    for rank,(sha,triple) in enumerate(ranked):
        for cand in triple:
            ids=(cand,)+tuple(i for i in triple if i!=cand)
            for start in fixture['block_starts']:
                tasks[(proto,rank,sha,cand,start)]=[groups[i][start:start+3] for i in ids]
assert len(tasks)==len(report['records'])==1536
totals=Counter();positive=0;witnesses=Counter();verified=0
for rec in report['records']:
    key=tuple(rec[k] for k in ('protocol','triple_rank','sha256','candidate','block_start'))
    rows=tasks.pop(key);verdict=good(rows)
    assert verdict==rec['GOOD'];positive+=verdict
    for name,res in rec['enhanced'].items():
        assert res['answer']==verdict
        b=res['counts'];assert len(b)==3 and all(isinstance(n,int) and 0<=n<=3 for n in b)
        assert sum(b)==res['queries']<=rec['baseline_queries'][name]==9
        lo=[tuple(sum((z[d] for z in rows[g][:b[g]]),Q(0))/3 for d in (0,1)) for g in range(3)]
        up=[tuple(x+Q(3-b[g],3) for x in lo[g]) for g in range(3)]
        w=res.get('negative_witness')
        if w:
            assert not verdict
            if w['kind']=='certain_domination':assert dom(up[w['rival']],lo[0])
            else:
                assert w['kind']=='certain_support'
                a,c=Q(w['weight_cost']),Q(w['weight_failure'])
                assert a+c==1 and min(a,c)>=0
                assert all(a*(lo[g][0]-up[0][0])+c*(lo[g][1]-up[0][1])>=0 for g in (1,2))
            witnesses[w['kind']]+=1
        else:assert sum(b)==9 or verdict
        if verdict:assert sum(b)==9
        totals[name]+=sum(b);verified+=1
    expected=Q(8,23)*(rec['enhanced']['A_LR']['queries']+rec['enhanced']['A_RL']['queries'])+Q(7,23)*rec['enhanced']['B']['queries']
    assert expected==Q(rec['mixture_enhanced']);totals['mixture']+=expected
assert not tasks and positive==41
for name,total in totals.items():assert total==Q(report['all_tasks'][name]['enhanced_rows'])
out={'status':'PASS','independence':'Raw JSON parsed and SHA selection reconstructed without importing producer or policy; full verdict checked by scalarisation breakpoint enumeration; every exported endpoint witness independently checked.','tasks':1536,'positive':positive,'negative':1536-positive,'policy_task_results_verified':verified,'negative_witnesses':dict(witnesses),'enhanced_disclosures':{k:str(v) for k,v in totals.items()},'fair_baseline_saving':str(Q(totals['census']-totals['det'],totals['census'])),'source_report_sha256':hashlib.sha256((O/'practical_negative_stopping_P56.json').read_bytes()).hexdigest(),'limitations':'Evidence validation supplements analytic soundness; no physical measurements or external peer review.'}
(O/'Root_APEX_Verification_P56.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
