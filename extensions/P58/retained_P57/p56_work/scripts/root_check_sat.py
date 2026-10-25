"""Independent exact validation of SAT2024 derived results, no policy imports."""
from pathlib import Path
from fractions import Fraction as Q
from zipfile import ZipFile
from itertools import combinations
from collections import Counter
import json,csv,io,hashlib
B=Path(__file__).resolve().parents[1];P=B/'research/SAT2024_detailed_results.zip'
e=json.loads((B/'evidence/practical_sat2024_replay_P56.json').read_text())
assert hashlib.sha256(P.read_bytes()).hexdigest()==e['source_zip_sha256']
with ZipFile(P) as z:raw=z.read('detailed_main.csv')
assert hashlib.sha256(raw).hexdigest()==e['source_csv_sha256']
records=list(csv.DictReader(io.StringIO(raw.decode())));labels=sorted(set(records[0])-{'hash','vresult'})
N=len(records);D=10000*10**max(len(row[g].partition('.')[2]) for row in records for g in labels)
assert N==400 and len(labels)==14
prefix={}
for g in labels:
    s=[(0,0)]
    for row in records:
        score=Q(row[g]);v=score*D/10000;assert v.denominator==1
        s.append((s[-1][0]+int(v),s[-1][1]+(D if score==10000 else 0)))
    prefix[g]=s
def dom(x,y):return x!=y and x[0]<=y[0] and x[1]<=y[1]
def support(p,rs):
    ws={Q(0),Q(1)}
    for r in rs:
        x,y=r[0]-p[0],r[1]-p[1]
        if x!=y:
            a=Q(-y,x-y)
            if 0<=a<=1:ws.add(a)
    return any(all(a*(r[0]-p[0])+(1-a)*(r[1]-p[1])>=0 for r in rs) for a in ws)
def good(p,rs):return not any(dom(r,p) for r in rs) and not support(p,rs)
expected={(triple,g) for triple in combinations(labels,3) for g in triple}
tot=Counter();reasons=Counter();checked=0
for rec in e['records']:
    t=tuple(rec['triple']);g=rec['candidate'];expected.remove((t,g));order=(g,)+tuple(h for h in t if h!=g)
    means=[prefix[h][-1] for h in order];answer=good(means[0],means[1:])
    assert answer==rec['GOOD']==False
    for name,r in rec['policies'].items():
        if name.startswith('mixture'):tot[name]+=Q(r['queries']);continue
        counts=r['counts'];assert len(counts)==3 and all(0<=n<=N for n in counts)
        assert sum(counts)==r['queries']<=3*N and r['answer']==answer
        lo=[prefix[h][n] for h,n in zip(order,counts)]
        up=[tuple(x+(N-n)*D for x in l) for l,n in zip(lo,counts)]
        reason=r['reason']
        if reason=='certain_domination':assert any(dom(u,lo[0]) for u in up[1:])
        elif reason=='certain_support':assert support(up[0],lo[1:])
        elif reason=='observed_dominator':assert counts[0]==N and any(counts[i]==N and dom(lo[i],lo[0]) for i in (1,2))
        else:assert sum(counts)==3*N
        reasons[str(reason)]+=1;tot[name]+=r['queries'];checked+=1
    G=Q(means[0][0]-means[0][1],N*D)
    p=5*G/(4+G) if G<=Q(13,20) else (12*G-3)/(11*G)
    assert str(p)==rec['probability_SE']
    for suffix in ('','_early'):
        got=(1-p)*rec['policies']['NW'+suffix]['queries']+p*rec['policies']['SE'+suffix]['queries']
        assert got==Q(rec['policies']['mixture'+suffix]['queries'])
assert not expected and len(e['records'])==1092
for k,v in tot.items():assert v==Q(e['summary']['queries'][k])
out={'status':'PASS','method':'Independent raw CSV parsing, exact means/verdicts via weight breakpoints, every terminal negative certificate, costs and all mixture probabilities; imports no policy or producer.','tasks':1092,'positive_tasks':0,'policy_task_results_verified':checked,'negative_terminal_reasons':dict(reasons),'totals':{k:str(v) for k,v in tot.items()},'source_report_sha256':hashlib.sha256((B/'evidence/practical_sat2024_replay_P56.json').read_bytes()).hexdigest()}
(B/'evidence/Root_SAT_Verification_P56.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
