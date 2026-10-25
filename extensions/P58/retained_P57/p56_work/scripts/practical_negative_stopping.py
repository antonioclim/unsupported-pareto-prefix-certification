#!/usr/bin/env python3
"""P56 exact APEX replay with a sound early-FALSE stopping wrapper.
Uses unchanged P17 public source rows, SHA task selection and policy schedules.
Does not modify or rerun the frozen producer's main(). No financial or energy data.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import Counter
import importlib.util,json,hashlib,time,platform,sys
BASE=Path(__file__).resolve().parents[2]
SRC=BASE/'p55_work/replay/reproduction/legacy/p17/apex_replay/apex_subcatalogue_replay_v1.py'
spec=importlib.util.spec_from_file_location('frozen_apex',SRC);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
OUT=BASE/'p56_work/evidence'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def false_certificate(observed):
    """Returns a self-contained rational witness; only public N and observations."""
    corners=m.observer_corners(observed); la,ua=corners[0]
    for g in (1,2):
        ur=corners[g][1]
        if all(ur[d]<=la[d] for d in (0,1)) and any(ur[d]<la[d] for d in (0,1)):
            return {'kind':'certain_domination','rival':g}
    # Fixed w=(a,1-a). Require w.U_A <= w.L_g for every rival.
    low,high=F(0),F(1)
    for g in (1,2):
        lr=corners[g][0];b=lr[1]-ua[1];slope=(lr[0]-ua[0])-b
        if slope>0:low=max(low,-b/slope)
        elif slope<0:high=min(high,-b/slope)
        elif b<0:return None
    if low<=high:return {'kind':'certain_support','weight_cost':str(low),'weight_failure':str(1-low)}
    return None

def independent_witness_check(observed,witness):
    # A separately expressed worst-endpoint inequality verifies exported witness.
    n=m.N
    lows=[tuple(sum((r[d] for r in g),F())/n for d in (0,1)) for g in observed]
    ups=[tuple(l[d]+F(n-len(g),n) for d in (0,1)) for g,l in zip(observed,lows)]
    if witness['kind']=='certain_domination':
        v=ups[witness['rival']];a=lows[0]
        return v[0]<=a[0] and v[1]<=a[1] and v!=a
    w=(F(witness['weight_cost']),F(witness['weight_failure']))
    return min(w)>=0 and sum(w)==1 and all(sum(w[d]*(lows[g][d]-ups[0][d]) for d in (0,1))>=0 for g in (1,2))

class EarlyFalse(Exception):pass
OriginalClient=m.Client
class EnhancedClient(OriginalClient):
    def query(self,g):
        super().query(g)
        witness=false_certificate(self.rows)
        if witness is not None:
            assert independent_witness_check(self.rows,witness)
            error=EarlyFalse();error.answer={'answer':False,'queries':len(self.trace),'counts':tuple(map(len,self.rows)),'trace':list(self.trace),'negative_witness':witness};raise error

def execute(rows,name,enhanced):
    m.Client=EnhancedClient if enhanced else OriginalClient
    try:return m.run_policy(rows,name)
    except EarlyFalse as e:return e.answer
    finally:m.Client=OriginalClient

def tasks():
    fix=json.loads((SRC.parent/'fixtures_v1.json').read_text())
    for protocol,count in fix['protocols'].items():
        groups=m.load(protocol,count)
        selections=m.selection(protocol,groups,fix['triples_per_protocol'],fix['selection_seed'])
        for rank,(key,triple) in enumerate(selections):
            for candidate in triple:
                order=(candidate,)+tuple(i for i in triple if i!=candidate)
                for start in fix['block_starts']:
                    yield {'protocol':protocol,'triple_rank':rank,'sha256':key,'candidate':candidate,'block_start':start,'rows':[groups[i]['rows'][start:start+3] for i in order]}

def finite_soundness():
    # Exhaustive finite-square endpoint-alphabet completion check, N=2.
    old_n=m.N;m.N=2
    alphabet=((F(0),F(0)),(F(0),F(1)),(F(1),F(0)),(F(1),F(1)),(F(3,5),F(3,5)))
    group_prefixes=[()] + [(x,) for x in alphabet] + list(product(alphabet,repeat=2))
    possible_outcomes={};full_count=0;positive_archives=0
    for flat in product(alphabet,repeat=6):
        rows=[flat[0:2],flat[2:4],flat[4:6]];good=m.full_good(rows);full_count+=1;positive_archives+=int(good)
        for counts in product(range(3),repeat=3):
            key=tuple(tuple(g[:n]) for g,n in zip(rows,counts))
            possible_outcomes[key]=possible_outcomes.get(key,0)|(2 if good else 1)
    count=0;kinds=Counter();missed=0
    for state in product(group_prefixes,repeat=3):
        witness=false_certificate(state)
        if witness:
            count+=1;kinds[witness['kind']]+=1
            assert possible_outcomes[state]==1,(state,witness)
            assert independent_witness_check(state,witness)
        elif possible_outcomes[state]==1:missed+=1
    m.N=old_n
    return {'archives':full_count,'positive_archives':positive_archives,'distinct_prefix_states':len(possible_outcomes),'certified_negative_states':count,'kinds':dict(kinds),'negative_states_not_detected':missed,'note':'Finite tests supplement analytic soundness; oracle not claimed complete.'}

def main():
    started=time.perf_counter();m.freeze_check();tests=finite_soundness();ts=list(tasks());records=[]
    names=('A_LR','A_RL','B','det','greedy','census')
    cpu={name:{'baseline':0,'enhanced':0} for name in names};saved_payload=0
    for task in ts:
        rows=task['rows'];good=m.full_good(rows);record={k:v for k,v in task.items() if k!='rows'};record['GOOD']=good
        results={};before={}
        for name in names:
            tick=time.process_time_ns();baseline=execute(rows,name,False);cpu[name]['baseline']+=time.process_time_ns()-tick
            tick=time.process_time_ns();aug=execute(rows,name,True);cpu[name]['enhanced']+=time.process_time_ns()-tick
            assert baseline['answer']==aug['answer']==good
            assert aug['trace']==baseline['trace'][:len(aug['trace'])]
            assert aug['queries']<=baseline['queries']
            if good:assert aug['trace']==baseline['trace']
            for g in range(3):assert [i for h,i in aug['trace'] if h==g]==list(range(1,aug['counts'][g]+1))
            results[name]=aug;before[name]=baseline['queries']
        record['baseline_queries']=before
        record['enhanced']={name:{k:v for k,v in result.items() if k!='trace'} for name,result in results.items()}
        record['mixture_baseline']=str(F(8,23)*(before['A_LR']+before['A_RL'])+F(7,23)*before['B'])
        record['mixture_enhanced']=str(F(8,23)*(results['A_LR']['queries']+results['A_RL']['queries'])+F(7,23)*results['B']['queries'])
        records.append(record)
    assert len(records)==1536 and sum(r['GOOD'] for r in records)==41
    def summary(rs):
        out={'tasks':len(rs),'positive_tasks':sum(r['GOOD'] for r in rs),'negative_tasks':sum(not r['GOOD'] for r in rs)}
        for name in names+('mixture',):
            old=sum((F(r['mixture_baseline']) if name=='mixture' else F(r['baseline_queries'][name]) for r in rs),F())
            new=sum((F(r['mixture_enhanced']) if name=='mixture' else F(r['enhanced'][name]['queries']) for r in rs),F())
            oldpos=sum((F(r['mixture_baseline']) if name=='mixture' else F(r['baseline_queries'][name]) for r in rs if r['GOOD']),F())
            newpos=sum((F(r['mixture_enhanced']) if name=='mixture' else F(r['enhanced'][name]['queries']) for r in rs if r['GOOD']),F())
            out[name]={'baseline_rows':str(old),'enhanced_rows':str(new),'saved_rows':str(old-new),'relative_saving':str((old-new)/old),'positive_baseline_rows':str(oldpos),'positive_enhanced_rows':str(newpos)}
            if name!='mixture':
                out[name]['early_negative_tasks']=sum(not r['GOOD'] and r['enhanced'][name]['queries']<9 for r in rs)
                out[name]['negative_witness_kinds']=dict(Counter(r['enhanced'][name].get('negative_witness',{}).get('kind','none') for r in rs if not r['GOOD']))
        return out
    result={'status':'PASS','schema':'P56-negative-wrapper-v1','source_program_sha256':sha(SRC),'audit_program_sha256':sha(Path(__file__)),'frozen_source_checks':'before_and_after_pass','finite_soundness':tests,'all_tasks':summary(records),'by_protocol':{p:summary([r for r in records if r['protocol']==p]) for p in ('Crystal','RPL')},'process_cpu_ns_single_sequential_pass':cpu,'wall_seconds':time.perf_counter()-started,'python':sys.version,'platform':platform.platform(),'records':records,'limitations':['Exploratory reanalysis of same overlapping APEX tasks; not held-out or independent physical measurements.','Square relaxation and transformed latency objective unchanged from P17.','Exact disclosed-row savings; no measured money, network bytes, radio energy or operational cost.','Single sequential CPU pass is diagnostic only; not a controlled performance comparison.','Negative oracle is sufficient, not complete or claimed optimal.','Positive paths and positive competitive guarantee are unchanged.','A proper baseline should itself include sound negative stopping.']}
    m.freeze_check();OUT.mkdir(exist_ok=True,parents=True)
    (OUT/'practical_negative_stopping_P56.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('records','by_protocol')},indent=2))
if __name__=='__main__':main()
