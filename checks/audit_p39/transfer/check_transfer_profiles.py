#!/usr/bin/env python3
"""Independent finite audit of certificate/price/positive-transcript equivalence.
No imported manuscript checker. Exhaustive n=2 domain pairs, selected n=3 full-Y models.
Finite deterministic policies only; continuous random seeds are treated analytically.
"""
from functools import lru_cache
from itertools import product
from pathlib import Path
import hashlib,json,time
started=time.perf_counter()
counts={'models':0,'certificate_equal_models':0,'certificate_unequal_models':0,'price_vectors_checked':0,'comparator_checks':0,'source_profile_count':0,'target_profile_count':0,'empty_certificate_models':0}

def bits(x,j):return (x>>j)&1

def legal_sets(n,pred):
 return [m for m in range(1<<n) if all(not(m>>j&1) or pred[j]&m==pred[j] for j in range(n))]

def certs(n,domain,positive,f,legal):
 return {x:frozenset(m for m in legal if all(f[y] for y in domain if (y&m)==(x&m))) for x in positive}

def profiles(n,domain,positive,f,pred):
 # Each profile contains the ordered paid-query transcript for every scored input.
 @lru_cache(None)
 def solve(mask,value):
  compatible=tuple(y for y in domain if y&mask==value)
  active=tuple(i for i,x in enumerate(positive) if x&mask==value)
  if not active:return frozenset({tuple(None for _ in positive)})
  assert compatible
  answer=set()
  if all(f[y] for y in compatible):
   answer.add(tuple(() if i in active else None for i in range(len(positive))))
  for j in range(n):
   bit=1<<j
   if mask&bit or pred[j]&mask!=pred[j]:continue
   left=solve(mask|bit,value)
   right=solve(mask|bit,value|bit)
   for a in left:
    for b in right:
     row=[]
     for i,x in enumerate(positive):
      if i not in active:row.append(None)
      else:
       t=b[i] if x&bit else a[i]
       assert t is not None
       row.append((j,)+t)
     answer.add(tuple(row))
  assert answer
  return frozenset(answer)
 return solve(0,0)

examples=[]
def one(n,X,Y,f,pred,case):
 positive=tuple(x for x in X if f[x])
 if not positive:return
 legal=legal_sets(n,pred)
 cx=certs(n,X,positive,f,legal);cy=certs(n,Y,positive,f,legal)
 equal=cx==cy
 # The finite separating family specified in R5, including the empty set.
 tariff_equal=True
 for T in legal:
  w=tuple(1 if T>>j&1 else n+1 for j in range(n))
  cost=lambda S:sum(w[j] for j in range(n) if S>>j&1)
  if any(min(map(cost,cx[x]))!=min(map(cost,cy[x])) for x in positive):tariff_equal=False
  counts['price_vectors_checked']+=1
 assert tariff_equal==equal,(case,'tariffs',X,Y,f,pred)
 px=profiles(n,X,positive,f,pred);py=profiles(n,Y,positive,f,pred)
 assert (px<=py)==equal,(case,'profiles',X,Y,f,pred)
 # Independent direct check of comparator identity for a fixed nonunit tariff.
 w=tuple(j+2 for j in range(n))
 for i,x in enumerate(positive):
  certificate=min(sum(w[j] for j in range(n) if S>>j&1) for S in cx[x])
  policy_min=min(sum(w[j] for j in p[i]) for p in px)
  assert certificate==policy_min,(case,'comparator',x,X,f,pred)
  counts['comparator_checks']+=1
 counts['models']+=1
 counts['certificate_equal_models' if equal else 'certificate_unequal_models']+=1
 counts['source_profile_count']+=len(px);counts['target_profile_count']+=len(py)
 if any(0 in cx[x] for x in positive):counts['empty_certificate_models']+=1
 if len(examples)<5 and not equal:
  missing=next(p for p in px if p not in py)
  examples.append({'n':n,'X':X,'Y':Y,'f':f,'predecessor_masks':pred,'positive_inputs':positive,'unextendible_positive_profile':missing})

# All total predicates, all nonempty X subset Y subset {0,1}^2, all 2-element posets.
n=2
for truth in range(1<<(1<<n)):
 f=tuple((truth>>x)&1 for x in range(1<<n))
 for ym in range(1,1<<(1<<n)):
  Y=tuple(x for x in range(1<<n) if ym>>x&1)
  xm=ym
  while xm:
   X=tuple(x for x in range(1<<n) if xm>>x&1)
   for pred in [(0,0),(0,1),(2,0)]:one(n,X,Y,f,pred,'exhaustive_n2')
   xm=(xm-1)&ym
exhaustive_counts=counts.copy()
# All 16 symmetric predicates on three bits, every nonempty X, four posets.
n=3;Y=tuple(range(1<<n))
for coefficients in range(16):
 f=tuple((coefficients>>x.bit_count())&1 for x in Y)
 for xm in range(1,1<<(1<<n)):
  X=tuple(x for x in Y if xm>>x&1)
  for pred in [(0,0,0),(0,1,3),(0,0,3),(0,1,0)]:one(n,X,Y,f,pred,'symmetric_n3')
# Explicit unit-price coincidence counterexample from §7.3, checked independently.
n=3;Y=tuple(range(8));X=(0,1,2,7) # x3 = x1 OR x2 uses encoding correction below
X=tuple(x for x in Y if bits(x,2)==(bits(x,0)|bits(x,1)))
f=tuple(int(bits(x,0)|bits(x,1)) for x in Y)
positive=tuple(x for x in X if f[x]);legal=legal_sets(n,(0,0,0))
cx=certs(n,X,positive,f,legal);cy=certs(n,Y,positive,f,legal)
assert all(min(m.bit_count() for m in cx[x])==min(m.bit_count() for m in cy[x])==1 for x in positive)
assert cx!=cy
px=profiles(n,X,positive,f,(0,0,0));py=profiles(n,Y,positive,f,(0,0,0))
assert min(max(len(s) for s in p) for p in px)==1
assert min(max(len(s) for s in p) for p in py)==2
# Uniform hard pair makes every deterministic globally correct tree cost >=3/2.
pair=tuple(x for x in positive if bits(x,0)+bits(x,1)==1)
ix=[positive.index(x) for x in pair]
assert min(sum(len(p[i]) for i in ix) for p in py)==3
report={'status':'PASS','counts':counts,'exhaustive_n2_counts':exhaustive_counts,'scope':'Exact finite deterministic transcript-profile enumeration, certificate families and finite separating tariffs. Does not enumerate continuous random seeds, arbitrary real inputs or certify general analytic R5 by computation.','models_n2':'All 16 total Boolean predicates, every nonempty nested pair X subset Y subset {0,1}^2 with a positive X input, three possible posets on two labelled locations. Predicates differing outside Y may count as repeated restricted models.','models_n3':'All 16 symmetric total predicates, full Y={0,1}^3, all nonempty X with a positive input, four declared posets.','unit_price_counterexample':'All positive certificate minima one, but X deterministic optimum one and Y-valid positive optimum two; equal hard pair average lower bound 3/2.','examples':examples,'elapsed_seconds':time.perf_counter()-started,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
p=Path(__file__).with_name('Transfer_Profiles_Independent_Check.json');p.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['status','counts','exhaustive_n2_counts','elapsed_seconds']},indent=2))
