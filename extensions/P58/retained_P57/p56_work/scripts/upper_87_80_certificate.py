"""Exact rational Bernstein producer for NEW mixed triangle policy, P56.
Numerical searches are not imported. Producer uses sparse Fraction polynomial
expansion, exact Bernstein conversion and rational midpoint subdivision.
"""
import sys,json,math,time
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from upper_polynomial import Poly
start=time.monotonic();g,z,w=[Poly.variable(n)for n in ['g','z','w']];tvar=Poly.variable('t');Gvar=Poly.variable('G')
e=F(7,80);lam=F(1,12);h=F(3,4)
t=g*(1-g)*z;H=2-(1-g)*z;J=w*(1-z);E=H-J
Vn=g*z*H+J;Un=(1-g*z)*H-2*J

def coeffs(G,t,kind):
 if kind=='low':den=4+G;num=F(19,3)*G-2*G*G
 else:den=G;num=(1+e)*G-3*e
 return (3*e+(2*lam+e)*t)*den,(1+e)*den-num,(lam+e)*den+num

def full(G,kind):
 D,A,B=coeffs(G,t,kind)
 return (D*H*E-A*g*H*Un-B*(1-g)*Vn*E)

def cut(G,tnew,kind):
 D0=2*g-tvar;delta=g*(1-g)-tvar
 E0=(1-g)*D0-w*delta;U0=(1-g-tvar)*D0-2*w*delta;V0=tvar*D0+w*delta
 D,A,B=coeffs(G,tvar,kind)
 out=D*D0*E0-A*g*D0*U0-B*V0*E0
 return (out.subs(tvar,tnew))
T2=(h-g)*z;T3=h-g+(g*(1-g)-(h-g))*z
families={
 'L0':(full(g,'low'),(F(0),F(3,4))),
 'L1':(full(g+t,'low'),(F(0),F(1,2))),
 'L2':(cut(g+tvar,T2,'low'),(F(1,2),F(3,4))),
 'L3':(cut(h,T3,'low'),(F(1,2),F(3,4))),
 'H0':(full(g,'high'),(F(3,4),F(1))),
 'H1':(full(g+t,'high'),(F(3,4),F(1))),
 'H2':(cut(g+tvar,T3,'high'),(F(1,2),F(3,4))),
 'H3':(cut(h,T3,'high'),(F(1,2),F(3,4))),
}

def bernstein(poly,box):
 variables=(g,z,w);deg=tuple(poly.degree(v) for v in variables)
 powers={idx:co for idx,co in poly.terms(variables)};mapped={}
 for alpha,co in powers.items():
  choices=[]
  for exponent,(lo,hi)in zip(alpha,box):
   choices.append([(j,F(math.comb(exponent,j))*lo**(exponent-j)*(hi-lo)**j)for j in range(exponent+1)])
  for term in product(*choices):
   beta=tuple(a[0]for a in term);c=co
   for _,fac in term:c*=fac
   mapped[beta]=mapped.get(beta,F(0))+c
 vals={}
 for idx in product(*[range(d+1)for d in deg]):
  out=F(0)
  for ex,c in mapped.items():
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

def cert(poly,box,maxdepth=48,maxnodes=500000):
 deg,vals=bernstein(poly,box);todo=[('',vals)];accepted=[];failed=[];nodes=0
 while todo:
  path,v=todo.pop();nodes+=1;mn=min(v.values())
  if mn>=0:accepted.append({'path':path,'minimum':str(mn)});continue
  if len(path)>=maxdepth or nodes>maxnodes:failed.append({'path':path,'minimum':str(mn)});break
  axis=len(path)%3;l,r=split(deg,v,axis);todo.extend([(path+'1',r),(path+'0',l)])
 return {'degrees':deg,'box':[[str(v) for v in p] for p in box],'nodes':nodes,'leaves':accepted,'failed':failed,'remaining':len(todo),'status':'PASS' if not failed and not todo else 'UNRESOLVED'}
if __name__=='__main__':
 out={'lambda':str(lam),'excess_bound':str(e),'ratio':'87/80','cut':str(h),'families':{},'status':'RUNNING'}
 names=sys.argv[1:] or list(families)
 for name in names:
  poly,gg=families[name];print(name,'degrees',tuple(poly.degree(v)for v in(g,z,w)),flush=True)
  res=cert(poly,[gg,(F(0),F(1)),(F(0),F(1))]);res['power_terms']=[{'exponents':idx,'coefficient':str(co)}for idx,co in poly.terms((g,z,w))]
  out['families'][name]=res;print(name,res['status'],res['nodes'],len(res['leaves']),res['failed'],flush=True)
  out['status']='PASS' if all(v['status']=='PASS'for v in out['families'].values())and len(out['families'])==8 else 'INCOMPLETE'
  out['elapsed_seconds']=time.monotonic()-start
  Path('p56_work/evidence/upper_87_80_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
