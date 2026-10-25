#!/usr/bin/env python3
"""Frozen exact replay on fixed SHA-ranked APEX three-configuration slices.

Standard-library only. No producer imports, random simulation, live data,
external software, future-value input to client policies or physical claims.
"""
from collections import defaultdict,Counter
from fractions import Fraction as Q
from itertools import combinations,product
from pathlib import Path
import csv,hashlib,json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
N=3
GROUPS=(0,1,2)

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def parse(point):return tuple(map(Q,point))
def dominates(p,q):return p!=q and all(x<=y for x,y in zip(p,q))

def has_support(p,others):
    """Comparator oracle: closed interval for weights(t,1-t), axes/ties included."""
    lo,hi=Q(0),Q(1)
    for r in others:
        b=r[1]-p[1];slope=r[0]-p[0]-b
        if slope>0:lo=max(lo,-b/slope)
        elif slope<0:hi=min(hi,-b/slope)
        elif b<0:return False
    return lo<=hi

def full_good(rows):
    means=[tuple(sum((r[d] for r in group),Q(0))/N for d in (0,1)) for group in rows]
    return not any(dominates(p,means[0]) for p in means[1:]) and not has_support(means[0],means[1:])

def observer_corners(observed):
    out=[]
    for group in observed:
        lo=tuple(sum((r[d] for r in group),Q(0))/N for d in (0,1))
        out.append((lo,tuple(v+Q(N-len(group),N) for v in lo)))
    return out

def comparator_true(rows,counts):
    corners=observer_corners([g[:n] for g,n in zip(rows,counts)])
    la,ua=corners[0]
    return not any(dominates(b[0],ua) for b in corners[1:]) and not has_support(la,[b[1] for b in corners[1:]])

def strict_pair_below(p,left,right):
    """Client oracle: strict open interval for a convex mixture, not support code."""
    lo,hi=Q(0),Q(1)
    for d in (0,1):
        base=right[d]-p[d];slope=left[d]-right[d]
        if slope>0:hi=min(hi,-base/slope)
        elif slope<0:lo=max(lo,-base/slope)
        elif base>=0:return False
    # Strict inequalities permit some interior alpha iff the open intersection
    # with (0,1) has positive length. Under robust P2 one-point witnesses cannot
    # be strict improvements, so no endpoint-only feasible case is lost.
    return lo<hi

class Server:
    def __init__(self,rows):
        self.__rows=tuple(tuple(g) for g in rows)
        self.__n=[0,0,0]
        self.log=[]
    def next_row(self,g):
        if g not in GROUPS or self.__n[g]>=N:raise ValueError('illegal next-row request')
        index=self.__n[g];self.__n[g]+=1
        self.log.append((g,index+1))
        return index+1,self.__rows[g][index]

class Client:
    """Policy information consists of public N and received rows only."""
    def __init__(self,next_row):self.__next=next_row;self.rows=[[],[],[]];self.trace=[]
    def query(self,g):
        index,row=self.__next(g)
        assert index==len(self.rows[g])+1 and 1<=index<=N
        self.rows[g].append(row);self.trace.append((g,index))
    def p2_safe(self,g):
        b=observer_corners(self.rows)
        return not dominates(b[g][0],b[0][1])
    def true(self):
        b=observer_corners(self.rows)
        return not any(dominates(z[0],b[0][1]) for z in b[1:]) and strict_pair_below(b[0][0],b[1][1],b[2][1])
    def finish(self):
        answer=self.true()
        assert answer or all(len(g)==N for g in self.rows)
        return {'answer':answer,'queries':len(self.trace),'counts':tuple(map(len,self.rows)),'trace':self.trace}
    def fallback(self):
        for g in GROUPS:
            while len(self.rows[g])<N:
                self.query(g)
                if self.true():return self.finish()
        return self.finish()

def screen(client):
    for _ in range(N):client.query(0)
    for g in (1,2):
        while not client.p2_safe(g):
            if len(client.rows[g])==N:return False
            client.query(g)
    return True

def run_policy(rows,name):
    server=Server(rows);c=Client(server.next_row)
    if name=='B':
        for g,m in ((0,2),(1,3),(2,3)):
            while len(c.rows[g])<m:c.query(g)
        out=c.finish() if c.true() else c.fallback()
    elif name=='census':
        for g in GROUPS:
            for _ in range(N):c.query(g)
        out=c.finish()
    else:
        if not screen(c):out=c.fallback()
        elif c.true():out=c.finish()
        elif name in ('A_LR','A_RL'):
            for g in (1,2):
                while len(c.rows[g])<2:
                    c.query(g)
                    if c.true():break
                if c.true():break
            if not c.true():
                for g in ((1,2) if name=='A_LR' else (2,1)):
                    while len(c.rows[g])<N:
                        c.query(g)
                        if c.true():break
                    if c.true():break
            out=c.finish() if c.true() else c.fallback()
        elif name=='det':out=c.fallback()
        elif name=='greedy':
            while not c.true() and any(len(c.rows[g])<N for g in (1,2)):
                corners=observer_corners(c.rows)
                g=min((g for g in (1,2) if len(c.rows[g])<N),key=lambda j:(sum(corners[j][1]),j))
                c.query(g)
            out=c.finish() if c.true() else c.fallback()
        else:raise ValueError(name)
    assert out['trace']==server.log
    assert out['queries']==sum(out['counts'])<=9
    previous=[0,0,0]
    for g,index in out['trace']:
        assert index==previous[g]+1;previous[g]=index
    return out

def load(protocol,count):
    raw=json.loads((ROOT/f'p9/licence/apex_dataset/{protocol}_results.json').read_text(),parse_float=Q)
    groups=defaultdict(list)
    for r in raw:groups[tuple(sorted(r['params'].items()))].append(r)
    assert len(groups)==count
    output=[]
    for key in sorted(groups):
        rows=sorted(groups[key],key=lambda r:r['id']);assert len(rows)==6
        converted=[]
        for row in rows:
            latency=Q(row['metrics']['latency']);failure=1-Q(row['metrics']['reliability'])
            assert latency>=0 and 0<=failure<=1
            converted.append((latency/(latency+100),failure))
        output.append({'params':dict(key),'trial_ids':[r['id'] for r in rows],'rows':converted})
    return output

def selection(protocol,groups,limit,seed):
    # Labels are the fixed indices obtained by lexicographic parameter sorting.
    ranked=[]
    for triple in combinations(range(len(groups)),3):
        key=seed+'|'+protocol+'|'+','.join(map(str,triple))
        ranked.append((hashlib.sha256(key.encode()).hexdigest(),triple))
    return sorted(ranked)[:limit]

def freeze_check():
    f=json.loads((HERE/'FREEZE_v1.json').read_text())
    for p,h in f['sha256'].items():assert digest(ROOT/p)==h,p
    return f

def summarise(records):
    positive=[r for r in records if r['GOOD']]
    out={'tasks':len(records),'positive_tasks':len(positive),'negative_tasks':len(records)-len(positive),
         'certificate_histogram':dict(sorted(Counter(str(r['C_star']) for r in positive).items())),
         'positive_cost_sums':{k:str(sum((Q(r[k]) for r in positive),Q(0))) for k in ('mixture','det','greedy','census')},
         'positive_mixture_vs_det':{'fewer':sum(Q(r['mixture'])<r['det'] for r in positive),'equal':sum(Q(r['mixture'])==r['det'] for r in positive),'more':sum(Q(r['mixture'])>r['det'] for r in positive)},
         'positive_mixture_vs_greedy':{'fewer':sum(Q(r['mixture'])<r['greedy'] for r in positive),'equal':sum(Q(r['mixture'])==r['greedy'] for r in positive),'more':sum(Q(r['mixture'])>r['greedy'] for r in positive)},
         'max_positive_ratios':{k:str(max((Q(r[k])/r['C_star'] for r in positive),default=Q(0))) if positive else None for k in ('mixture','det','greedy','census')}}
    return out

def main():
    freeze_check();fixture=json.loads((HERE/'fixtures_v1.json').read_text())
    records=[];selected={};data={};states=0;traces=0
    for protocol,count in fixture['protocols'].items():
        groups=load(protocol,count);assert sum(len(g['rows']) for g in groups)==6*count
        selections=selection(protocol,groups,fixture['triples_per_protocol'],fixture['selection_seed'])
        selected[protocol]=[{'rank':rank,'sha256':key,'configuration_indices':list(triple),'params':[groups[i]['params'] for i in triple]} for rank,(key,triple) in enumerate(selections)]
        data[protocol]={'source':f'p9/licence/apex_dataset/{protocol}_results.json','sha256':digest(ROOT/f'p9/licence/apex_dataset/{protocol}_results.json'),'configurations':count,'source_rows':count*6,'possible_triples':len(list(combinations(range(count),3))),'selected_triples':len(selections)}
        for rank,(key,triple) in enumerate(selections):
            for candidate in triple:
                order=(candidate,)+tuple(i for i in triple if i!=candidate)
                for start in fixture['block_starts']:
                    rows=[groups[i]['rows'][start:start+3] for i in order]
                    outcome=full_good(rows)
                    true=[n for n in product(range(4),repeat=3) if comparator_true(rows,n)]
                    states+=64;cb=min((sum(n) for n in true),default=None)
                    assert (cb is not None)==outcome
                    runs={name:run_policy(rows,name) for name in ('A_LR','A_RL','B','det','greedy','census')}
                    for name,run in runs.items():
                        assert run['answer']==outcome,(protocol,rank,candidate,start,name)
                        assert comparator_true(rows,run['counts'])==outcome
                        if not outcome:assert run['counts']==(3,3,3)
                    traces+=len(runs)
                    mixture=Q(8,23)*(runs['A_LR']['queries']+runs['A_RL']['queries'])+Q(7,23)*runs['B']['queries']
                    if outcome:
                        assert cb in (7,8,9)
                        assert mixture/cb<=Q(25,23)
                        assert Q(runs['det']['queries'],cb)<=Q(9,8)
                    records.append({'protocol':protocol,'triple_rank':rank,'triple_sha256':key,'configuration_indices':list(triple),'candidate_index':candidate,'policy_group_order':list(order),'block_start_one_based':start+1,'trial_ids':[groups[i]['trial_ids'][start:start+3] for i in order],'GOOD':outcome,'C_star':cb,'minimum_TRUE_prefixes':[list(n) for n in true if sum(n)==cb],
                                    'A_LR':runs['A_LR']['queries'],'A_RL':runs['A_RL']['queries'],'B':runs['B']['queries'],'mixture':str(mixture),'det':runs['det']['queries'],'greedy':runs['greedy']['queries'],'census':runs['census']['queries'],
                                    'terminal_prefixes':{name:list(run['counts']) for name,run in runs.items()},'traces':{name:[list(x) for x in run['trace']] for name,run in runs.items()}})
    assert len(records)==1536 and states==98304 and traces==9216
    freeze_check()
    result={'status':'PASS_EXACT_APEX_FIXED_SUBCATALOGUE_REPLAY','schema':'p17-apex-replay-v1','source_sha256':digest(Path(__file__)),'freeze_sha256':digest(HERE/'FREEZE_v1.json'),'dataset_manifest':data,'all_source_rows':312,'selected_triples':selected,'task_count':len(records),'prefix_states':states,'policy_paths':traces,'summary':summarise(records),'by_protocol':{p:summarise([r for r in records if r['protocol']==p]) for p in fixture['protocols']},'records':records,
            'scope':['All sampled triples selected by predeclared SHA ranking independent of outcomes','All three designated candidates and two nonoverlapping fixed blocks retained','Closed independent square is the declared audit relaxation; exact physical transformed completion domain not identified','Rows use latency/(latency+100ms), a different scientific objective','All arithmetic exact Fraction; expectation over policy branches, not Monte Carlo','Client policies see only received prefixes; source tables passed only to the server','Subcatalogues and row blocks reuse old data; no new physical trials, heldout test or independent replications','No claim of whole-catalogue empirical superiority, deployed service, radio energy savings or historical priority']}
    (HERE/'results_v1.json').write_text(json.dumps(result,indent=2)+'\n')
    fields=['protocol','triple_rank','candidate_index','block_start_one_based','GOOD','C_star','A_LR','A_RL','B','mixture','det','greedy','census']
    with (HERE/'comparison_v1.csv').open('w',newline='') as output:
        writer=csv.DictWriter(output,fieldnames=fields);writer.writeheader()
        for row in records:writer.writerow({k:row[k] for k in fields})
    print(json.dumps({k:v for k,v in result.items() if k not in ('records','selected_triples')},indent=2))

if __name__=='__main__':main()
