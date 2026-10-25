#!/usr/bin/env python3
"""P56 private exploratory replay of official SAT2024 penalized-score archive.
No redistribution of source CSVs; requires official zip at research path.
All generated policy executions access only observed values through next_row().
"""
from pathlib import Path
from zipfile import ZipFile
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
import csv,io,json,hashlib,time
BASE=Path(__file__).resolve().parents[2];OUT=BASE/'p56_work/evidence';SRC=BASE/'p56_work/research/SAT2024_detailed_results.zip';PROTOCOL=BASE/'p56_work/research/practical_SAT2024_protocol.txt'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dominates(x,y):return x!=y and x[0]<=y[0] and x[1]<=y[1]
def ratio_leq(x,y):return x[0]*y[1]<=y[0]*x[1]
def support_witness(p,rs):
    lo=(0,1);hi=(1,1)
    for r in rs:
        df=r[1]-p[1];s=r[0]-p[0]-df
        if s>0:
            z=(-df,s)
            if not ratio_leq(z,lo):lo=z
        elif s<0:
            z=(df,-s)
            if ratio_leq(z,hi):hi=z
        elif df<0:return None
    return lo if ratio_leq(lo,hi) else None

def independent_complete_good(p,rs):
    if any(dominates(r,p) for r in rs):return False
    weights={F(0),F(1)}
    for r in rs:
        dc,df=r[0]-p[0],r[1]-p[1]
        if dc!=df:
            a=F(-df,dc-df)
            if 0<=a<=1:weights.add(a)
    return not any(all(a*(r[0]-p[0])+(1-a)*(r[1]-p[1])>=0 for r in rs) for a in weights)

class Stop(Exception):pass
class Server:
    def __init__(self,rows):self.__a=rows;self.__count=[0,0,0];self.log=[]
    def next_row(self,g):
        j=self.__count[g]
        if not 0<=g<3 or j>=N:raise ValueError('illegal query')
        self.__count[g]+=1;self.log.append((g,j+1));return j+1,self.__a[g][j]

class Client:
    def __init__(self,next_row,early):self.__next=next_row;self.early=early;self.b=[0,0,0];self.s=[[0,0] for _ in range(3)];self.trace=[];self.verdict=None;self.reason=None
    def corners(self):return self.s,[[self.s[g][d]+(N-self.b[g])*D for d in (0,1)] for g in range(3)]
    def false(self):
        low,up=self.corners()
        for g in (1,2):
            if dominates(up[g],low[0]):return 'certain_domination'
        w=support_witness(up[0],low[1:])
        if w is not None:return 'certain_support'
        return None
    def true(self):
        low,up=self.corners()
        return not any(dominates(r,up[0]) for r in low[1:]) and support_witness(low[0],up[1:]) is None
    def buy(self,g):
        j,row=self.__next(g);assert j==self.b[g]+1;self.b[g]=j;self.trace.append((g,j))
        for d in (0,1):self.s[g][d]+=row[d]
        if self.early:
            why=self.false()
            if why:self.verdict=False;self.reason=why;raise Stop()
    def census(self):
        for g in (0,1,2):
            while self.b[g]<N:self.buy(g)
        self.verdict=self.true()
    def triangle(self,first):
        while self.b[0]<N:self.buy(0)
        for g in (1,2):
            while self.b[g]<N and dominates(self.s[g],self.s[0]):self.buy(g)
            if dominates(self.s[g],self.s[0]):self.verdict=False;self.reason='observed_dominator';return
        roles={}
        for g in (1,2):
            l=self.s[g];p=self.s[0]
            if l[0]<p[0] and l[1]>p[1]:roles['NW']=g
            if l[0]>p[0] and l[1]<p[1]:roles['SE']=g
        if len(roles)==2:
            g=roles[first]
            while self.b[g]<N:self.buy(g)
            g=roles['SE' if first=='NW' else 'NW']
            while not self.true() and self.b[g]<N:self.buy(g)
            if self.true():self.verdict=True;return
        self.census()

def run(rows,name,early):
    server=Server(rows);c=Client(server.next_row,early)
    try:c.census() if name=='census' else c.triangle(name)
    except Stop:pass
    assert c.trace==server.log and sum(c.b)==len(c.trace)
    assert c.verdict is not None
    return {'answer':c.verdict,'queries':len(c.trace),'counts':c.b,'reason':c.reason},c.trace

def main():
    global N,D
    start=time.monotonic()
    with ZipFile(SRC) as z:data=z.read('detailed_main.csv')
    csvrows=list(csv.DictReader(io.StringIO(data.decode())));N=len(csvrows)
    labels=sorted(set(csvrows[0])-{'hash','vresult'})
    assert len(labels)==14 and N==400 and len({r['hash'] for r in csvrows})==N
    maxdec=max(len(r[l].partition('.')[2]) for r in csvrows for l in labels);scale=10**maxdec;D=10000*scale
    archives={};means={};sentinels=0
    for l in labels:
        values=[]
        for r in csvrows:
            assert r[l] and r[l] not in ('NA','NaN')
            score=F(r[l]);assert score==10000 or 0<=score<=5000
            if score==10000:sentinels+=1
            c=score*scale;assert c.denominator==1
            values.append((int(c),D if score==10000 else 0))
        archives[l]=values;means[l]=tuple(sum(v[d] for v in values) for d in (0,1))
    full_catalogue={l:independent_complete_good(means[l],[means[r] for r in labels if r!=l]) for l in labels}
    records=[];names=('census','NW','SE')
    for triple in combinations(labels,3):
        for candidate in triple:
            order=(candidate,)+tuple(l for l in triple if l!=candidate);rows=[archives[l] for l in order]
            good=independent_complete_good(means[candidate],[means[l] for l in order[1:]])
            record={'triple':list(triple),'candidate':candidate,'GOOD':good,'policies':{}}
            runs={}
            for name in names:
                for early in (False,True):
                    key=name+('_early' if early else '')
                    result,trace=run(rows,name,early);assert result['answer']==good
                    if early:
                        assert trace==runs[name][1][:len(trace)]
                        if good:assert trace==runs[name][1]
                    runs[key]=(result,trace);record['policies'][key]=result
            G=F(means[candidate][0]-means[candidate][1],N*D)
            assert 0<=G<=1
            prob=5*G/(4+G) if G<=F(13,20) else (12*G-3)/(11*G)
            assert 0<=prob<=1
            for early in (False,True):
                suf='_early' if early else ''
                record['policies']['mixture'+suf]={'queries':str((1-prob)*runs['NW'+suf][0]['queries']+prob*runs['SE'+suf][0]['queries'])}
            if runs['NW_early'][1]!=runs['SE_early'][1]:
                assert runs['NW_early'][0]['counts'][0]==N and runs['SE_early'][0]['counts'][0]==N
            record['probability_SE']=str(prob);records.append(record)
    keys=tuple(records[0]['policies'])
    def summary(rs):
        return {'tasks':len(rs),'positive_tasks':sum(x['GOOD'] for x in rs),'negative_tasks':sum(not x['GOOD'] for x in rs),'queries':{k:str(sum((F(r['policies'][k]['queries']) for r in rs),F())) for k in keys},'positive_queries':{k:str(sum((F(r['policies'][k]['queries']) for r in rs if r['GOOD']),F())) for k in keys},'negative_queries':{k:str(sum((F(r['policies'][k]['queries']) for r in rs if not r['GOOD']),F())) for k in keys}}
    result={'status':'PASS','schema':'P56-SAT2024-replay-v1','source_url':'https://satcompetition.github.io/2024/downloads/detailed_results.zip','source_zip_sha256':sha(SRC),'source_csv_sha256':hashlib.sha256(data).hexdigest(),'protocol_sha256':sha(PROTOCOL),'script_sha256':sha(Path(__file__)),'rows_per_configuration':N,'configurations':len(labels),'input_cells':N*len(labels),'unsolved_penalty_cells':sentinels,'score_decimal_scale':scale,'exact_coordinate_denominator':D,'ordering':'CSV source order (instance hash)','full_catalogue_GOOD':full_catalogue,'complete_mean_objectives':{l:[str(F(v,N*D)) for v in means[l]] for l in labels},'summary':summary(records),'records':records,'elapsed_seconds':time.monotonic()-start,'limitations':['Exploratory all-triple reanalysis of public scores; all tasks overlap.','Scores are reported decimal PAR-2 penalties, not raw actual CPU use; failure is recovered from exact published penalty sentinel.','Closed independent triangle is a declared conservative completion contract, not asserted physical input image.','Candidate-census triangle mixture is unchanged theorem19, not new improved unrestricted algorithm.','No empirical optimal-certificate ratio is computed and no comparison to the tighter-domain comparator is asserted.','Positive policy traces unchanged by sound negative stopping; no taskwise ex-post best schedule selection.','Public aggregate and raw data access withheld in simulated client; no real metered service.','No monetary, energy, network-byte or future-population claim.','No reuse licence confirmed for downloaded CSVs/ZIP; do not redistribute those bytes.']}
    OUT.mkdir(exist_ok=True,parents=True);(OUT/'practical_sat2024_replay_P56.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('records','complete_mean_objectives')},indent=2))
if __name__=='__main__':main()
