"""Independent standard-library check of the high-branch algebraic identities."""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json,argparse
from verify_upper_certificate import Poly,inverse_collocation,prepare_output,write_output

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument("--output",type=Path,default=Path(__file__).with_name("High_Analytic_Independent_Check.json"))
destination=prepare_output(parser.parse_args().output)

g=Poly({(1,0,0):1});t=Poly({(0,1,0):1});x=Poly({(0,0,1):1})
h=F(13,20)

def discr(g):
 a=3*g*g*(2-g)*(g+1)
 b=-18*g*g*g+15*g*g+17*g-3
 c=F(89,5)-24*g*g
 return 4*a*c-b*b

def q(g,t,x,G):
 k=1+t-g;v=t+x
 return G*(3+t)*(k-v)-3*g*(k-2*v)-(13*G-3)*v*(k-v)

checks={}
def ident(name,left,right):
 assert not (left-right).terms,name
 checks[name]='PASS'

ident('G_g_expansion',q(g,t,x,g),(13*g-3)*x*x+(13*g*g-13*g+3+(12*g-3)*t)*x+3*t*(2*g-1)*(2*g-1))
d=g*(1-g)-t;dd=2*g-t;k=1+t-g
a=13*(g+t)-3
b=13*g*g-13*g+3+(25*g-19)*t+12*t*t
c=3*t*((2*g-1)*(2*g-1)*(2-g)+4*(1-g)*d)
ident('G_gt_expansion',q(g,t,x,g+t),a*x*x+b*x+c)
p=13*g*g*g-11*g*g*t-10*g*g-12*g*t*t+3*g*t+3*g+12*t*t*t+10*t*t-3*t
ident('G_gt_far_endpoint',a*d*d+b*d*dd+c*dd*dd,g*k*p)
m=2*c*dd+b*d
ident('quadratic_Bernstein',a*d*d*x*x+b*d*dd*x+c*dd*dd,c*dd*dd*(1-x)*(1-x)+dd*m*x*(1-x)+g*k*p*x*x)

# t is now used as the independent delta variable.
delta=t;tt=g*(1-g)-delta;qq=2*g-1
pp=13*g*g*g-11*g*g*tt-10*g*g-12*g*tt*tt+3*g*tt+3*g+12*tt*tt*tt+10*tt*tt-3*tt
aa=3*g*g*(2-g)*(g+1);bb=-18*g*g*g+15*g*g+17*g-3;cc=10+24*g-36*g*g-12*delta
ident('P_delta_decomposition',pp,aa*qq*qq+bb*qq*delta+cc*delta*delta)
ident('C_low_g_remainder',cc-(F(89,5)-24*g*g),12*(2*g-g*g-h-delta))
ident('C_global_remainder',cc-(10+12*g-24*g*g),12*(g*(1-g)-delta))
expanded=-36*g*g*g*g*g*g+252*g*g*g*g*g-F(2013,5)*g*g*g*g-F(2022,5)*g*g*g+F(1141,5)*g*g+102*g-9
ident('discriminant_expansion',discr(g),expanded)
assert discr(g).degree()==(6,0,0)
nodes=[F(2,5)+(F(1,2)-F(2,5))*F(i,6) for i in range(7)]
inv=inverse_collocation(6)
coefs=[sum((u*discr(v) for u,v in zip(row,nodes)),F(0)) for row in inv]
expected=[F(539951,15625),F(653387,18750),F(6526313,187500),F(1720069,50000),F(1007879,30000),F(9707,300),F(613,20)]
assert coefs==expected and min(coefs)>0
checks['discriminant_Bernstein_coefficients']='PASS'
assert 3*F(81,100)*F(19,10)>=3
assert 3*F(4,5)**2-2*F(1,4)**2==F(359,200)
out={'status':'PASS','method':'independent exact sparse polynomial arithmetic and rational Bernstein collocation; no SymPy or producer imports','identities':checks,'discriminant_coefficients':list(map(str,coefs)),'discriminant_minimum':str(min(coefs)),'large_g_lower_bound':'359/200','script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Polynomial identities and displayed constants; range inequalities and domain coverage are supplied in Main Section 6, Theorem 19.'}
write_output(destination,out)
print(json.dumps(out,indent=2))
