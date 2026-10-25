"""Independent finite audit of P37 endpoint/B2/B3/B4/B5 obligations.

No manuscript checker is imported. Exact Fraction arithmetic; supporting
weights are tested by direct intersection of one-dimensional inequalities,
not by the manuscript's determinant test. This is finite corroboration,
not verification of the continuous all-size proofs or Ramsey reduction.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json, time, hashlib, sys

START=time.perf_counter()
HERE=Path(__file__).resolve().parent
counts={}
Z=(F(0),F(0));O=(F(1),F(1))
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def scale(a,x):return (a*x[0],a*x[1])
def dominates(q,p):return q[0]<=p[0] and q[1]<=p[1] and q!=p
def supported(p,rivals):
    low=F(0);high=F(1)
    for q in rivals:
        intercept=q[1]-p[1]
        slope=q[0]-p[0]-intercept
        if slope>0:low=max(low,-intercept/slope)
        elif slope<0:high=min(high,-intercept/slope)
        elif intercept<0:return False
    return low<=high
def good(points):
    return not any(dominates(q,points[0]) for q in points[1:]) and not supported(points[0],points[1:])
def true_corners(lowers,lengths,N):
    uppers=[add(p,scale(F(N-b,N),O)) for p,b in zip(lowers,lengths)]
    return not any(dominates(q,uppers[0]) for q in lowers[1:]) and not supported(lowers[0],uppers[1:])
def legal(p,d):return 0<=p[1]<=p[0]<=1 and p[0]-p[1]<=d
def sums(rows):
    ans=[Z]
    for row in rows:ans.append(add(ans[-1],row))
    return ans
def all_true_prefixes(rows):
    N=len(rows[0]);ps=[sums(rs) for rs in rows];trues=[]
    for lengths in product(range(N+1),repeat=len(rows)):
        lows=[scale(F(1,N),pp[b]) for pp,b in zip(ps,lengths)]
        if true_corners(lows,lengths,N):trues.append(lengths)
    return trues

# Exhaustive finite completions verify endpoint equivalence in domains that
# include both whole-vector endpoints; these are independent small models.
domains=[(Z,O),(Z,(F(1),F(0)),O),(Z,(F(0),F(1)),O),(Z,(F(1),F(0)),(F(0),F(1)),O), (Z,O,(F(3,4),F(3,8)),(F(1,2),F(1,2)),(F(1),F(0))), (Z,O,(F(1,4),F(15,16)),(F(0),F(1)),(F(1),F(0)))]
states_count=completion_count=true_states=partial_true_states=0
for alphabet in domains:
    N=2
    prefixes=[p for b in range(N+1) for p in product(alphabet,repeat=b)]
    possible={}
    for pre in prefixes:
        possible[pre]=[scale(F(1,N),sums(pre+tail)[-1]) for tail in product(alphabet,repeat=N-len(pre))]
    for prefixes3 in product(prefixes,repeat=3):
        lengths=tuple(map(len,prefixes3))
        lowers=[scale(F(1,N),sums(pre)[-1]) for pre in prefixes3]
        predicted=true_corners(lowers,lengths,N)
        actual=True
        for means in product(*(possible[p] for p in prefixes3)):
            completion_count+=1
            if not good(means):actual=False;break
        assert actual==predicted,(alphabet,prefixes3,predicted,actual)
        states_count+=1
        if actual:
            true_states+=1
            partial_true_states+=int(sum(lengths)<3*N)
assert true_states>0 and partial_true_states>0
counts['finite_endpoint_TRUE_states']=true_states
counts['finite_endpoint_partial_TRUE_states']=partial_true_states
counts['finite_endpoint_prefix_states']=states_count
counts['finite_endpoint_completion_evaluations']=completion_count

# B2 feasibility witnesses: sweep all oriented integer lengths over many widths.
widths=sorted({F(p,q) for q in range(1,11) for p in range(1,q+1)})
triples=feasible=boundary=0
for N in range(1,11):
    for d in widths:
        P,Q=d.numerator,d.denominator
        for a,i,j in product(range(1,N+1),repeat=3):
            triples+=1
            H=P*j-Q*(4*N-2*a-i-j)
            J=H*H-4*Q*Q*(2*N-a-i)*(2*N-a-j)
            if H<0 or J<0:continue
            t,s,r=(F(N-a,N),F(N-i,N),F(N-j,N))
            b=d*(1-r);M=b-(s+t)-(r+t);z=M/2
            delta=z*z-(s+t)*(r+t)
            eps=delta/(2*b)
            x=b-t-eps;y=r+z-eps
            records=[(x/(1-t),y/(1-t)),((b-s+r)/(2*(1-s)),)*2,(d,F(0))]
            if H>0 and J>0:
                assert all(legal(rec,d) for rec in records)
                lows=[scale(F(length,N),rec) for length,rec in zip((a,i,j),records)]
                assert true_corners(lows,(a,i,j),N),(N,d,a,i,j)
                assert eps==F(J,8*P*Q*N*j)
                assert records[0][0].denominator<=8*P*Q*N*N and records[0][1].denominator<=8*P*Q*N*N
                assert a>F(N)*(1-d/4)
                assert a+i+j>F(N)*(3-d)
                feasible+=1
            elif J==0 and H>=0 and all(legal(rec,d) for rec in records):
                lows=[scale(F(length,N),rec) for length,rec in zip((a,i,j),records)]
                assert not true_corners(lows,(a,i,j),N)
                boundary+=1
counts.update(B2_parameter_triples=triples,B2_legal_true_constructions=feasible,B2_equality_constructions_rejected=boundary)

# B4 exact whole-prefix TRUE sets on both fixed worlds. Include 0-prefix states.
b4_instances=b4_states=0
widths_b4=sorted({F(p,q) for q in range(1,7) for p in range(1,q+1)})
for N in range(4,11):
    for d in widths_b4:
        if d*(N-1)<=2:continue
        q=F(1,N);C=d*(1-q);eps=min((C-2*q)/16,q*q/16)
        p=(3*C/4+q/2+eps,C/4+q/2+eps)
        for world in ('A','B'):
            rows=[[p]*N,[(d/2,d/2)]*(N-1)+[Z if world=='A' else O],[(d,F(0))]*(N-1)+[O if world=='A' else Z]]
            assert all(legal(rec,d) for rs in rows for rec in rs)
            trues=set(all_true_prefixes(rows))
            expected={(N,N,N),(N,N,N-1) if world=='A' else (N,N-1,N)}
            assert trues==expected,(N,d,world,trues,expected)
            b4_instances+=1;b4_states+=(N+1)**3
counts.update(B4_fixed_worlds=b4_instances,B4_prefix_states=b4_states)

# B5 priced two-choice upper bound including the both-tails-suffice case.
values=[F(1,10),F(1,3),F(1),F(2),F(7),F(100)]
price_cases=0
for W,x,y in product(values,repeat=3):
    den=x*(W+x)+y*(W+y);theta=y*(W+y)/den;R=1+x*y/den
    one_x=(W+x+(1-theta)*y)/(W+x)
    one_y=(W+y+theta*x)/(W+y)
    both=(W+theta*x+(1-theta)*y)/(W+min(x,y))
    assert one_x==one_y==R
    assert both<=R
    assert 1+min(x,y)/(W+max(x,y))==min(1+y/(W+x),1+x/(W+y))
    price_cases+=1
counts['B5_exact_price_cases']=price_cases

# B3 bounded embedding: a K=5 unique inversion requires completed candidate
# and one unique opposite-side pair; enumerate every prefix for N=2..5.
def psi(z):return F(6,5)+z/(5*(z+1))
embed_cases=embed_states=0
for N in range(2,6):
    for d in (F(1,10),F(1,2),F(1)):
        c,f=F(2,3),F(1,6)
        rows=[[scale(d,(c/N,f/N))]*N]
        for raw in (F(2),F(4)):
            u=psi(raw);ell=(c*u+f)/(1+u)
            rows.append([scale(d,(F(1,3),F(1,3)))]+[Z]*(N-2)+[scale(d,(ell-F(1,3),ell-F(1,3)))])
        for raw in (F(1),F(3)):
            v=psi(raw);rho=c+f/v
            rows.append([scale(d,(F(3,4),F(0)))]+[Z]*(N-2)+[scale(d,(rho-F(3,4),F(0)))])
        assert all(legal(rec,d) for rs in rows for rec in rs)
        trues=all_true_prefixes(rows)
        assert trues and min(map(sum,trues))==5+3*N-3
        assert all(t[0]==N and t[1]==N and t[4]==N and min(t[2:4])>=1 for t in trues)
        embed_cases+=1;embed_states+=(N+1)**5
counts.update(B3_unique_inversion_archives=embed_cases,B3_prefix_states=embed_states)

# Supplementary cases: exact feasible-shape minima and entire hard-world
# prefix sets. These checks are independent of the retained legacy programs.
minima_expected={5:{(4,5,5),(5,1,5),(5,5,3)},6:{(5,5,6),(6,1,6),(6,5,5),(6,6,4)}}
shape_count=0
for N,expected in minima_expected.items():
    feasible_shapes=[]
    for a,i,j in product(range(1,N+1),repeat=3):
        H=2*a+i+2*j-4*N
        J=H*H-4*(2*N-a-i)*(2*N-a-j)
        if H>0 and J>0:feasible_shapes.append((a,i,j))
        shape_count+=1
    mins={p for p in feasible_shapes if not any(q!=p and all(x<=y for x,y in zip(q,p)) for q in feasible_shapes)}
    assert mins==expected,(N,mins)
counts['supplementary_feasible_shapes_checked']=shape_count

worlds=[]
for name,ca,rr,expected in [('Q1_A',Z,(F(3,8),F(0)),{(2,3,3),(3,3,3)}),('Q1_D',(F(0),F(1)),O,{(3,3,1),(3,3,2),(3,3,3)})]:
    worlds.append((name,[[(F(3,8),F(7,8))]*2+[ca],[(F(0),F(1))]*2+[(F(0),F(7,8))],[(F(7,8),F(0)),(F(5,8),F(0)),rr]],expected))
for name,ca,ll,expected in [('B6_A',Z,(F(13,50),F(13,50)),{(4,5,5),(5,5,5)}),('B6_B',(F(1),F(0)),O,{(5,i,5) for i in range(1,6)})]:
    worlds.append((name,[[(F(79,80),F(1,8))]*4+[ca],[(F(51,100),F(51,100))]+[(F(13,50),F(13,50))]*3+[ll],[(F(1),F(0))]*5],expected))
for name,ca,ll,expected in [('C4_DU',Z,(F(37,50),F(37,50)),{(a,i,6) for a in (5,6) for i in (5,6)}),('C4_DV',(F(1),F(0)),O,{(6,i,6) for i in range(2,7)})]:
    worlds.append((name,[[(F(249,250),F(3,10))]*5+[ca],[(F(19,25),F(19,25))]*2+[(F(7,50),F(7,50))]*2+[ll,O],[(F(1),F(0))]*6],expected))
for name,ca,ll,expected in [('C4_QA',Z,(F(7,25),F(7,25)),{(5,6,6),(6,6,6)}),('C4_QB',(F(1),F(0)),O,{(6,i,6) for i in range(1,7)})]:
    worlds.append((name,[[(F(249,250),F(3,25))]*5+[ca],[(F(61,100),F(61,100))]+[(F(7,25),F(7,25))]*4+[ll],[(F(1),F(0))]*6],expected))
supp_states=0
for name,rows,expected in worlds:
    trues=set(all_true_prefixes(rows))
    assert trues==expected,(name,trues,expected)
    supp_states+=(len(rows[0])+1)**3
counts['supplementary_hard_worlds']=len(worlds)
counts['supplementary_hard_world_prefix_states']=supp_states

# The five-row mixture residual is affine in setup. Check both coefficients,
# rather than merely several arbitrary setup values.
table=[(11,F(11),F(15)),(12,F(12),F(15)),(13,F(27,2),F(15)),(14,F(59,4),F(15)),(14,F(15),F(14)),(15,F(15),F(15))]
coefficients=[]
for C,A,B in table:
    def residual(setup):return 4*(setup+C)-(5*setup+67)*(B-C)-4*(setup+14)*(A-B)
    intercept=residual(0);slope=residual(1)-intercept
    assert intercept>=0 and slope>=0
    coefficients.append([str(intercept),str(slope)])
assert coefficients==[['0','0'],['15','1'],['2','0'],['3','0'],['0','0'],['60','4']]
counts['B6_setup_affine_residuals']=6

result={'status':'PASS','scope':'Independent finite rational corroboration only; no Ramsey/minimax or universal proof execution','counts':counts,'elapsed_seconds':time.perf_counter()-START,'python':sys.version.split()[0],'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'manuscript_changed':False}
(HERE/'Independent_Band_Audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
