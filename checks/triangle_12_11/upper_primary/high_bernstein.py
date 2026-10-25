"""Exact high-branch certificates. Construction only; independent checker separate."""
import sys,json
from pathlib import Path
from fractions import Fraction as F
sys.path.insert(0,str(Path(__file__).parents[1]/'upper_check'))
from low_bernstein import s,g,z,w,H,E,Vn,Un,t,cert

h=s.Rational(13,20)
mode=sys.argv[1]
if mode=='h':
    raw=h*(3+t)*H*E-3*g*H*Un-(13*h-3)*(1-g)*Vn*E
    nt=h-g+(g*(1-g)-(h-g))*z
    numerator,denominator=s.fraction(s.cancel(raw.subs(z,nt/(g*(1-g)))))
    if denominator.subs(g,s.Rational(1,2))<0:numerator=-numerator;denominator=-denominator
    poly=s.Poly(numerator,g,z,w)
    roots=[(F(2,5),F(1,2)),(F(1,2),F(13,20))]
else:
    tt=s.symbols('t');d=g*(1-g)-tt;D=2*g-tt
    B=13*g*g-13*g+3+(25*g-19)*tt+12*tt*tt
    C=3*tt*((2*g-1)**2*(2-g)+4*(1-g)*d)
    raw=2*C*D+B*d
    nt=h-g+(g*(1-g)-(h-g))*z if mode=='middlecut' else g*(1-g)*z
    poly=s.Poly(s.expand(raw.subs(tt,nt)),g,z,w)
    denominator=s.Integer(1)
    roots=[(F(2,5),F(1,2)),(F(1,2),F(13,20))] if mode=='middlecut' else [(F(13,20),F(1))]

results=[]
for low,high in roots:
    box=((low,high),(F(0),F(1)),(F(0),F(1)))
    r=cert(poly,box,maxdepth=42,maxnodes=100000)
    results.append(r)
    print(mode,r['status'],r['nodes'],len(r['certificate']),r['failed'],flush=True)
Path(__file__).with_name('high_'+mode+'_bernstein.json').write_text(json.dumps({'mode':mode,'denominator':str(denominator),'polynomial_terms':[[list(ex),str(c)] for ex,c in poly.terms()],'results':results},indent=2)+'\n')
