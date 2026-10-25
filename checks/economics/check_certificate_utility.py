"""Exact finite counterexample for the naive TRUE-certificate reward.
New P40 audit code; independent of retained manuscript checkers.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,hashlib,datetime,platform
S=((F(0),F(0)),(F(0),F(1)),(F(1),F(0)),(F(1),F(1)),(F(3,5),F(3,5)))
worlds=list(product(S,repeat=3))
def good(w):
 p=w[0]
 for r in w[1:]:
  if all(r[i]<=p[i] for i in (0,1)) and any(r[i]<p[i] for i in (0,1)):return False
 lo,hi=F(0),F(1)
 for r in w[1:]:
  df=p[1]-r[1];slope=p[0]-r[0]-df
  if slope>0:hi=min(hi,-df/slope)
  elif slope<0:lo=max(lo,-df/slope)
  elif df>0:return True
 return lo>hi
labels={w:good(w) for w in worlds}
def compatible(obs):return [w for w in worlds if all(w[i]==v for i,v in obs.items())]
def reward(obs):return int(all(labels[w] for w in compatible(obs)))
def gain(obs,i):
 assert i not in obs
 ws=compatible(obs)
 return sum((F(reward({**obs,i:w[i]})-reward(obs)) for w in ws),F(0))/len(ws)
initial={}
psi={1:(F(0),F(1)),2:(F(1),F(0))}
before=gain(initial,0);after=gain(psi,0)
assert before==0 and after==F(1,5)
assert all(gain(initial,i)==0 for i in range(3))
assert reward(psi)==0
p=(F(3,5),F(3,5));l=(F(0),F(1));r=(F(1),F(0));mix=tuple((l[i]+r[i])/2 for i in range(2))
assert good((p,l,r)) and all(mix[i]<p[i] for i in range(2))
assert all(p[i]<=F(7,10) for i in range(2))
assert not all(l[i]<=F(7,10) for i in range(2)) and not all(r[i]<=F(7,10) for i in range(2))
result={'status':'PASS','model':'K=3,N=1, uniform product prior on five-symbol endpoint-containing square domain; each query reads one whole vector','alphabet':[[str(x) for x in s] for s in S],'complete_archives':len(worlds),'positive_archives':sum(labels.values()),'reward':'one iff observed transcript forces GOOD on every alphabet completion; zero otherwise','candidate_expected_marginal_before':str(before),'candidate_expected_marginal_after_known_crossing_rivals':str(after),'conditional_worlds':len(compatible(psi)),'adaptive_submodularity_violated':before<after,'indivisible_example':{'candidate':[str(x) for x in p],'left':[str(x) for x in l],'right':[str(x) for x in r],'equal_mixture':[str(x) for x in mix],'threshold':'7/10','candidate_is_unique_threshold_feasible':True},'scope':'Elementary exact counterexample for this naive reward only. Does not exclude other submodular utilities or reductions, prove a new acquisition ratio, or validate an economic deployment.','python':platform.python_version(),'finished_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_name('Certificate_Utility_Check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
