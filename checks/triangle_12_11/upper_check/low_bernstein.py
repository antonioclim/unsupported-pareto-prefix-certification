"""Exploratory exact Bernstein positivity certificates for the 12/11 candidate."""
import sys,json,math,time
from pathlib import Path
from fractions import Fraction as F
from itertools import product
sys.path.insert(0,str(Path(__file__).parent/'deps'))
import sympy as s
g,z,w=s.symbols('g z w')
t=g*(1-g)*z;H=2-(1-g)*z;J=w*(1-z);E=H-J
Vn=g*z*H+J;Un=(1-g*z)*H-2*J

def polynomial(G):
 return s.Poly(s.expand((4+G)*(3+t)*H*E-(48-43*G)*g*H*Un-(4+56*G)*(1-g)*Vn*E),g,z,w)

def bernstein(poly,box):
 variables=(g,z,w)
 deg=tuple(poly.degree(v) for v in variables)
 transformed=s.Poly(poly.as_expr().subs({v:s.Rational(a)+(s.Rational(b)-s.Rational(a))*v for v,(a,b) in zip(variables,box)},simultaneous=True).expand(),*variables)
 powers={idx:F(int(c.p),int(c.q)) for idx,c in transformed.terms()}
 vals={}
 for idx in product(*[range(d+1) for d in deg]):
  out=F(0)
  for ex,c in powers.items():
   if all(a<=i for a,i in zip(ex,idx)):
    for a,i,n in zip(ex,idx,deg):c*=F(math.comb(i,a),math.comb(n,a))
    out+=c
  vals[idx]=out
 return deg,vals

def split(deg,vals,axis):
 left={};right={};others=[i for i in range(3) if i!=axis]
 for js in product(*[range(deg[i]+1) for i in others]):
  key=[0,0,0]
  for i,j in zip(others,js):key[i]=j
  line=[]
  for k in range(deg[axis]+1):key[axis]=k;line.append(vals[tuple(key)])
  lv=[line[0]];rv=[line[-1]]
  while len(line)>1:
   line=[(a+b)/2 for a,b in zip(line,line[1:])];lv.append(line[0]);rv.append(line[-1])
  rv.reverse()
  for k in range(deg[axis]+1):
   key[axis]=k;left[tuple(key)]=lv[k];right[tuple(key)]=rv[k]
 return left,right

def cert(poly,box,maxdepth=36,maxnodes=200000):
 deg,vals=bernstein(poly,box);todo=[('',vals)];accepted=[];failed=[];nodes=0
 while todo:
  path,v=todo.pop();nodes+=1;mn=min(v.values())
  if mn>=0:accepted.append((path,str(mn)));continue
  if len(path)>=maxdepth or nodes>maxnodes:failed.append((path,str(mn)));break
  axis=len(path)%3
  l,r=split(deg,v,axis);todo.extend([(path+'1',r),(path+'0',l)])
 return {'degrees':deg,'box':[[str(v) for v in p] for p in box],'nodes':nodes,'certificate':accepted,'failed':failed,'remaining':len(todo),'status':'PASS' if not failed and not todo else 'UNRESOLVED'}

if __name__=='__main__':
 mode=sys.argv[1] if len(sys.argv)>1 else 'g'
 P=polynomial(g if mode=='g' else g+t)
 roots=[((F(0),F(1,2)),(F(0),F(1)),(F(0),F(1))),((F(1,2),F(13,20)),(F(0),F(1)),(F(0),F(1)))]
 denominator=1
 if mode=='gtlow':
  roots=[((F(0),F(2,5)),(F(0),F(1)),(F(0),F(1)))]
 if mode in ['gtcut','h']:
  P=polynomial(g+t if mode=='gtcut' else s.Rational(13,20))
  nt=(s.Rational(13,20)-g)*z if mode=='gtcut' else s.Rational(13,20)-g+(g*(1-g)-(s.Rational(13,20)-g))*z
  numerator,denominator=s.fraction(s.cancel(P.as_expr().subs(z,nt/(g*(1-g)))))
  if denominator.subs(g,s.Rational(1,2))<0:numerator=-numerator;denominator=-denominator
  print('cleared denominator',s.factor(denominator),flush=True)
  P=s.Poly(numerator,g,z,w)
  roots=[((F(2,5),F(1,2)),(F(0),F(1)),(F(0),F(1))),((F(1,2),F(13,20)),(F(0),F(1)),(F(0),F(1)))]
 results=[]
 for box in roots:
  r=cert(P,box);results.append(r);print(mode,r['status'],r['nodes'],len(r['certificate']),r['failed'],flush=True)
 Path(__file__).with_name('low_'+mode+'_bernstein.json').write_text(json.dumps({'mode':mode,'denominator':str(denominator),'results':results},indent=2)+'\n')
