#!/usr/bin/env python3
"""Independent finite ordinal-posterior and Bellman audit; own stdlib code.
This checks finite instances, not the infinite Ramsey theorem.
P41 adaptation: omitted manuscript digest is labelled historical, never reverified.
"""
from fractions import Fraction as F
from itertools import permutations
from functools import lru_cache
from collections import defaultdict
from pathlib import Path
import hashlib,json

ROOT=Path(__file__).resolve().parent
counts={'rank_worlds':0,'world_history_pairs':0,'posterior_classes':0,'next_label_checks':0,'bellman_states':0,'split_checks':0}

def exact_q(m,n):
 if m>n:m,n=n,m
 return F(m)+F(n+1,2)-F(m*m-1,6*n)

def test_posterior(m,n):
 k=m+n; labels=tuple(range(k)); ls=labels[:m];rs=labels[m:]
 # R_bad ranks 0,...,n-2; L_good n-1; R_good n; L_bad n+1,...,k-1.
 Lr=(n-1,)+tuple(range(n+1,k)); Rr=tuple(range(n-1))+(n,)
 worlds=[]
 for lp in permutations(Lr):
  for rp in permutations(Rr):worlds.append(lp+rp)
 counts['rank_worlds']+=len(worlds)
 for d in range(k):
  for hist in permutations(labels,d):
   a=sum(x<m for x in hist);b=d-a
   if a*b==m*n:continue
   grouped=defaultdict(list)
   for w in worlds:
    if any(w[i]<w[j] for i in hist if i<m for j in hist if j>=m):continue
    order=tuple(sorted(range(d),key=lambda ix:w[hist[ix]]))
    grouped[order].append(w);counts['world_history_pairs']+=1
   for order,ws in grouped.items():
    counts['posterior_classes']+=1
    for nxt in labels:
     if nxt in hist:continue
     succeeds=sum(any(w[i]<w[j] for i in hist+(nxt,) if i<m for j in hist+(nxt,) if j>=m) for w in ws)
     expected=F(b if nxt<m else a,m*n-a*b)
     assert F(succeeds,len(ws))==expected,(m,n,hist,order,nxt,F(succeeds,len(ws)),expected)
     counts['next_label_checks']+=1

for m,n in [(1,1),(1,2),(1,3),(1,4),(2,2),(2,3),(2,4),(3,3)]:test_posterior(m,n)
for m in range(1,16):
 for n in range(1,16):
  @lru_cache(None)
  def w(a,b):
   counts['bellman_states']+=1
   if (a,b)==(m,n):return 0
   nxt=[]
   if a<m:nxt.append(w(a+1,b))
   if b<n:nxt.append(w(a,b+1))
   return m*n-a*b+min(nxt)
  assert F(w(0,0),m*n)==exact_q(m,n)
for k in range(2,81):
 q=exact_q(k//2,k-k//2)
 assert q==max(exact_q(m,k-m) for m in range(1,k))
 counts['split_checks']+=1
proofs=[Path('p22/general_k/Triangular_General_K_Embedding.txt'),Path('p22/structure/Band_Domain_Theorems_P22.md'),Path('p22/lower/Fixed_Alphabet_Constant_Overhead_P22.md')]
historical=json.loads(Path('provenance/Retired_Manuscript_P21.json').read_text())
assert historical['omitted_from_public_snapshot'] is True
assert historical['fresh_public_replay_verifies_source_bytes'] is False
assert not Path(historical['path_in_legacy']).exists()
result={'status':'PASS','counts':counts,'posterior_splits':[[1,1],[1,2],[1,3],[1,4],[2,2],[2,3],[2,4],[3,3]],'bellman_splits':225,'balanced_total_label_range':[2,80],'source_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in proofs},'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact enumeration of finite rank posterior histories and Bellman states. Does not execute infinite Ramsey, prove arbitrary real-domain policies by enumeration or constitute external peer review.'}
result['retained_historical_source']={'path':historical['path_in_legacy'],'sha256':historical['sha256'],'freshly_verified':False,'status':'digest retained as provenance; omitted source bytes not checked'}
(ROOT/'Ordinal_Foundation_Exact_Check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
