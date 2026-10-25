"""Independent exact collocation verification of both-branch certificates.

Standard-library only. Does not import SymPy, the producer or project checkers.
The proof obligations and rational domain cover are in Main Section 6, Theorem 19.
A standalone run requires a fresh --output path; retained evidence is not replaced.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from math import comb
from hashlib import sha256
import json,time,copy,argparse

if not __debug__:
 raise RuntimeError('Optimised Python is not permitted for this exact certificate checker.')


def prepare_output(path):
    """Require a fresh regular JSON path; never replace retained evidence."""
    raw = path.expanduser().absolute()
    if raw.is_symlink() or any(p.is_symlink() for p in raw.parents):
        raise ValueError('Output cannot name or traverse a symbolic link.')
    if raw.suffix.lower() != '.json':
        raise ValueError('Output must have a .json suffix.')
    if raw.exists():
        raise ValueError('Output already exists; choose a new --output filename.')
    raw.parent.mkdir(parents=True, exist_ok=True)
    return raw

def write_output(path, result):
    # Exclusive creation also prevents replacing a file created since preflight.
    with path.open('x', encoding='utf-8') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')

ROOT=Path(__file__).resolve().parent
H=F(13,20)
EXPECTED={
 'g':((5,3,2),[(F(0),F(1,2)),(F(1,2),H)]),
 'gtlow':((6,4,2),[(F(0),F(2,5))]),
 'gtcut':((5,4,2),[(F(2,5),F(1,2)),(F(1,2),H)]),
 'h':((7,3,2),[(F(2,5),F(1,2)),(F(1,2),H)]),
 'high_h':((7,3,2),[(F(2,5),F(1,2)),(F(1,2),H)]),
 'middlecut':((7,3,0),[(F(2,5),F(1,2)),(F(1,2),H)]),
 'middlefull':((7,3,0),[(H,F(1))])}

class Poly:
 def __init__(self,terms):self.terms={k:F(v) for k,v in terms.items() if v}
 @staticmethod
 def coerce(x):return x if isinstance(x,Poly) else Poly({(0,0,0):F(x)})
 def __add__(self,other):
  out=dict(self.terms)
  for k,v in self.coerce(other).terms.items():out[k]=out.get(k,F(0))+v
  return Poly(out)
 __radd__=__add__
 def __neg__(self):return Poly({k:-v for k,v in self.terms.items()})
 def __sub__(self,other):return self+-self.coerce(other)
 def __rsub__(self,other):return self.coerce(other)+-self
 def __mul__(self,other):
  out={}
  for a,v in self.terms.items():
   for b,u in self.coerce(other).terms.items():
    k=tuple(x+y for x,y in zip(a,b));out[k]=out.get(k,F(0))+v*u
  return Poly(out)
 __rmul__=__mul__
 def degree(self):return tuple(max(k[i] for k in self.terms) for i in range(3))

def exact_polynomial(mode):
 # Degree bounds obtained by exact sparse arithmetic, not inferred from samples.
 g=Poly({(1,0,0):1});v=Poly({(0,1,0):1});w=Poly({(0,0,1):1})
 return value(mode,g,v,w)

def value(mode,g,v,w):
 if mode in ('middlecut','middlefull'):
  t=H-g+(g*(1-g)-(H-g))*v if mode=='middlecut' else g*(1-g)*v
  d=g*(1-g)-t;dd=2*g-t;q=2*g-1
  b=13*g*g-13*g+3+(25*g-19)*t+12*t*t
  c=3*t*(q*q*(2-g)+4*(1-g)*d)
  return 2*c*dd+b*d
 if mode in ('g','gtlow'):
  z=v;t=g*(1-g)*z;G=g if mode=='g' else g+t
  hh=2-(1-g)*z;j=w*(1-z);e=hh-j
  vn=g*z*hh+j;un=(1-g*z)*hh-2*j
  return (4+G)*(3+t)*hh*e-(48-43*G)*g*hh*un-(4+56*G)*(1-g)*vn*e
 t=(H-g)*v if mode=='gtcut' else H-g+(g*(1-g)-(H-g))*v
 G=g+t if mode=='gtcut' else H
 aa=2*g-t;d=g*(1-g)-t;ee=(1-g)*aa-w*d
 un=(1-g-t)*aa-2*w*d;vn=t*aa+w*d
 if mode=='high_h':
  return 40000*(H*(3+t)*aa*ee-3*g*aa*un-(13*H-3)*vn*ee)
 # This equals 160000*g^2*(1-g)*P after the rational substitution.
 return 160000*((4+G)*(3+t)*aa*ee-(48-43*G)*g*aa*un-(4+56*G)*vn*ee)

def inverse_collocation(n):
 # Distinct rational nodes i/n, with n=0 interpreted as the constant case.
 if n==0:return [[F(1)]]
 rows=[]
 for i in range(n+1):
  x=F(i,n)
  rows.append([F(comb(n,j))*x**j*(1-x)**(n-j) for j in range(n+1)]+[F(i==j) for j in range(n+1)])
 for k in range(n+1):
  pivot=next(i for i in range(k,n+1) if rows[i][k])
  rows[k],rows[pivot]=rows[pivot],rows[k]
  a=rows[k][k];rows[k]=[v/a for v in rows[k]]
  for i in range(n+1):
   if i!=k:
    a=rows[i][k];rows[i]=[v-a*u for v,u in zip(rows[i],rows[k])]
 return [row[n+1:] for row in rows]

def coefficients(mode,degree,box):
 vals={}
 keys=list(product(*[range(n+1) for n in degree]))
 for idx in keys:
  x=[a+(b-a)*F(i,n) if n else a for i,n,(a,b) in zip(idx,degree,box)]
  vals[idx]=value(mode,*x)
 for axis,n in enumerate(degree):
  inv=inverse_collocation(n);new={}
  for key in keys:
   a=list(key);v=F(0)
   for j in range(n+1):
    a[axis]=j;v+=inv[key[axis]][j]*vals[tuple(a)]
   new[key]=v
  vals=new
 return vals

def leaf_box(root,path):
 box=[list(ab) for ab in root]
 for i,c in enumerate(path):
  assert c in '01','invalid path digit'
  axis=i%3;a,b=box[axis];mid=(a+b)/2
  box[axis]=[a,mid] if c=='0' else [mid,b]
 return box

def verify(mode,data):
 degree,intervals=EXPECTED[mode]
 assert exact_polynomial(mode).degree()==degree,'independent polynomial degree mismatch'
 assert data['mode']==('h' if mode=='high_h' else mode)
 assert len(data['results'])==len(intervals),'missing root'
 records=[]
 for record,interval in zip(data['results'],intervals):
  assert tuple(record['degrees'])==degree,'degree mismatch'
  box=tuple(tuple(F(s) for s in ab) for ab in record['box'])
  assert box==(interval,(F(0),F(1)),(F(0),F(1))),'root mismatch'
  assert record['status']=='PASS' and not record['failed'] and record['remaining']==0
  entries=record['certificate'];paths=[p for p,_ in entries]
  assert len(paths)==len(set(paths)),'duplicate box'
  for i,p in enumerate(paths):
   assert all(not q.startswith(p) for j,q in enumerate(paths) if i!=j),'overlap'
  assert sum((F(1,2**len(p)) for p in paths),F(0))==1,'incomplete cover'
  for path,claimed in entries:
   vals=coefficients(mode,degree,leaf_box(box,path));mn=min(vals.values())
   assert mn==F(claimed),'wrong minimum'
   assert mn>=0,'negative coefficient'
   records.append({'root_g':[str(v) for v in interval],'path':path,'coefficients':len(vals),'minimum':str(mn)})
 return records

def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--output',type=Path,default=ROOT/'Upper_Independent_Check.json')
 args=parser.parse_args()
 destination=prepare_output(args.output)
 start=time.monotonic();results={}
 for mode in EXPECTED:
  p=ROOT/f'low_{mode}_bernstein.json' if mode not in ('high_h','middlecut','middlefull') else ROOT.parent/'upper_primary'/f'high_{"h" if mode=="high_h" else mode}_bernstein.json'
  data=json.loads(p.read_text())
  records=verify(mode,data)
  poly=exact_polynomial(mode)
  results[mode]={'status':'PASS','input_sha256':sha256(p.read_bytes()).hexdigest(),'independent_exact_degree':poly.degree(),'power_terms':len(poly.terms),'boxes':len(records),'coefficients':sum(x['coefficients'] for x in records),'records':records}
 # Negative controls are derived from a successfully verified certificate.
 baseline=json.loads((ROOT/'low_g_bernstein.json').read_text());negative=[]
 for mutation in ['wrong_minimum','missing_box','overlapping_box','underestimated_degree']:
  d=copy.deepcopy(baseline);r=d['results'][0]
  if mutation=='wrong_minimum':r['certificate'][0][1]=str(F(r['certificate'][0][1])+1)
  elif mutation=='missing_box':r['certificate'].pop()
  elif mutation=='overlapping_box':r['certificate'].append(['','0'])
  else:r['degrees'][0]-=1
  try:verify('g',d)
  except AssertionError as e:negative.append({'mutation':mutation,'status':'REJECTED','reason':str(e)})
  else:raise AssertionError('Malformed certificate accepted: '+mutation)
 out={'status':'PASS','checker':'independent Fraction collocation and exact sparse degree derivation; no producer/project imports','modes':results,'negative_controls':negative,'total_boxes':sum(r['boxes'] for r in results.values()),'total_coefficients':sum(r['coefficients'] for r in results.values()),'elapsed_seconds':time.monotonic()-start,'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'limitations':['Analytic domain cover and remaining high-branch inequalities require the accompanying proof.','Exact certificate does not establish historical novelty.']}
 write_output(destination,out)
 print(json.dumps({k:v for k,v in out.items() if k not in ['modes']},indent=2))

if __name__=='__main__':main()
