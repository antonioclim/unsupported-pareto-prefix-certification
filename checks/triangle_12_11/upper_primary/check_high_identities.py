"""Exact symbolic identity checks for the analytic high-branch argument.

SymPy is used here as an auxiliary identity checker. The independent final
Bernstein verifier uses only the Python standard library.
"""
import sys,json,hashlib,datetime
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent/'deps'))
import sympy as s
g,t,V,x,G,d,w=s.symbols('g t V x G d w')
k=1+t-g;D=2*g-t;delta=g*(1-g)-t;q=2*g-1
Q=(13*G-3)*V**2+(6*g-(13*G-3)*k-G*(3+t))*V+k*(G*(3+t)-3*g)
Umax=g*(k-2*V)/(k-V)
checks={}
def check(name,lhs,rhs):
    residual=s.factor(lhs-rhs)
    assert residual==0,(name,residual)
    checks[name]='PASS'
check('cleared_excess',Q,(k-V)*(G*(3+t)-3*Umax-(13*G-3)*V))
check('G_g_expansion',Q.subs({G:g,V:t+x}),
      (13*g-3)*x*x+(13*g*g-13*g+3+(12*g-3)*t)*x+3*t*q*q)
a=13*(g+t)-3
b=13*g*g-13*g+3+(25*g-19)*t+12*t*t
c=3*t*(q*q*(2-g)+4*(1-g)*delta)
check('G_gt_expansion',Q.subs({G:g+t,V:t+x}),a*x*x+b*x+c)
P=13*g**3-11*g*g*t-10*g*g-12*g*t*t+3*g*t+3*g+12*t**3+10*t*t-3*t
check('G_gt_far_endpoint',s.cancel(Q.subs({G:g+t,V:t+delta/D})*D*D),g*k*P)
M=2*c*D+b*delta
check('quadratic_Bernstein_w',s.cancel(Q.subs({G:g+t,V:t+w*delta/D})*D*D),
      c*D*D*(1-w)**2+D*M*w*(1-w)+g*k*P*w*w)
A=3*g*g*(2-g)*(g+1)
B=-18*g**3+15*g*g+17*g-3
C=10+24*g-36*g*g-12*d
check('P_delta_decomposition',P.subs(t,g*(1-g)-d),A*q*q+B*q*d+C*d*d)
C0=s.Rational(89,5)-24*g*g
check('C_lowerbound_low_g',C.subs(d,2*g-g*g-s.Rational(13,20)),C0)
disc=-36*g**6+252*g**5-s.Rational(2013,5)*g**4-s.Rational(2022,5)*g**3+s.Rational(1141,5)*g*g+102*g-9
check('discriminant_polynomial',4*A*C0-B*B,disc)
bs=[s.Rational(v) for v in ['539951/15625','653387/18750','6526313/187500','1720069/50000','1007879/30000','9707/300','613/20']]
y=s.symbols('y')
check('discriminant_Bernstein_coefficients',disc.subs(g,s.Rational(2,5)+y/s.Integer(10)),
      sum(bs[i]*s.binomial(6,i)*y**i*(1-y)**(6-i) for i in range(7)))
assert min(bs)==s.Rational(613,20)
assert s.Rational(3)*s.Rational(4,5)**2-s.Rational(2)*s.Rational(1,4)**2==s.Rational(359,200)
out={'status':'PASS','identity_checks':checks,'identities':len(checks),
     'discriminant_minimum_coefficient':'613/20',
     'analytic_large_g_lower_bound':'359/200',
     'sympy':s.__version__,'scope':'Exact polynomial identities and displayed rational constants; inequalities and domain coverage also require the written proof.',
     'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'finished_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
Path(__file__).with_name('High_Analytic_Identity_Check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
