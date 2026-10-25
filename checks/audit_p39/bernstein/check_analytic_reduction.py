#!/usr/bin/env python3
"""Independent finite checks of P37 C8-C11 reduction, not the Bernstein verifier.

Uses integer prefix corners and exact supporting-weight interval intersection.
Synthetic archives and rational grids are declared finite controls; universal
coverage and inequality arguments are supplied separately in the audit note.
"""
from fractions import Fraction as F
from pathlib import Path
from itertools import product
import hashlib,json,random,sys,time

ROOT=Path(__file__).resolve().parent
START=time.monotonic()
RNG=random.Random(2026102402)
SCALE=8
GRID=[(c,f) for c in range(SCALE+1) for f in range(c+1)]

def prefix_sums(rows):
    out=[(0,0)]
    for x,y in rows:out.append((out[-1][0]+x,out[-1][1]+y))
    return out

def dominates(p,q):
    return p[0]<=q[0] and p[1]<=q[1] and p!=q

def supported(p,others):
    lo,hi=F(0),F(1)
    for q in others:
        dx,dy=q[0]-p[0],q[1]-p[1]
        a=dx-dy
        if a>0:lo=max(lo,F(-dy,a))
        elif a<0:hi=min(hi,F(-dy,a))
        elif dy<0:return False
    return lo<=hi

def is_true(sums,N,state):
    lower=[sums[g][state[g]] for g in range(3)]
    upper=[tuple(x+SCALE*(N-state[g]) for x in lower[g]) for g in range(3)]
    return not any(dominates(q,upper[0]) for q in lower[1:]) and not supported(lower[0],upper[1:])

def hard_world(N,world):
    q=N//4;pad=N-4*q
    A=[(0,0)]*pad+[(SCALE,0)]*(2*q)+[(SCALE,SCALE)]*q+[(0,0)]*(q-1)+([(0,0)] if world=='U' else [(SCALE,0)])
    L=[(0,0)]*pad+[(SCALE,SCALE)]*q+[(0,0)]*(2*q)+[(SCALE,SCALE)]*(q-1)+([(0,0)] if world=='U' else [(SCALE,SCALE)])
    R=[(0,0)]*pad+[(SCALE,0)]*(4*q)
    return [A,L,R]

archives=[]
for N in (3,4,5,6,8,12):
    for i in range(50):archives.append((f'grid_N{N}_{i}',N,[[RNG.choice(GRID) for _ in range(N)] for _ in range(3)]))
for N in (1,2,3,4,5,6,8,12):
    archives.append((f'constant_positive_N{N}',N,[[(6,3)]*N,[(4,4)]*N,[(8,0)]*N]))
for N in range(12,20):
    for world in ('U','V'):archives.append((f'hard_{world}_N{N}',N,hard_world(N,world)))

counts={'archives':len(archives),'positive_archives':0,'negative_archives':0,'prefixes_examined':0,'true_prefixes':0,'candidate_partial_true_prefixes':0,'parameter_projections':0}
records=[]
for ident,N,rows in archives:
    sums=[prefix_sums(r) for r in rows]
    if not is_true(sums,N,(N,N,N)):
        counts['negative_archives']+=1
        continue
    counts['positive_archives']+=1
    p=sums[0][N]
    nw=[j for j in (1,2) if sums[j][N][0]<p[0] and sums[j][N][1]>p[1]]
    se=[j for j in (1,2) if sums[j][N][0]>p[0] and sums[j][N][1]<p[1]]
    assert len(nw)==len(se)==1
    # Normalise rival indices only; their records remain in original order.
    sums=[sums[0],sums[nw[0]],sums[se[0]]]
    G=F(p[0]-p[1],SCALE*N)
    assert 0<G<1
    screen=[]
    for j in (1,2):
        h=next(i for i in range(N+1) if not dominates(sums[j][i],p))
        screen.append(h)
    jstar=next(j for j in range(screen[1],N+1) if is_true(sums,N,(N,N,j)))
    istar=next(i for i in range(screen[0],N+1) if is_true(sums,N,(N,i,N)))
    costNW,costSE=2*N+jstar,2*N+istar
    true=[]
    for state in product(range(N+1),repeat=3):
        counts['prefixes_examined']+=1
        if not is_true(sums,N,state):continue
        counts['true_prefixes']+=1
        a,i,j=state
        counts['candidate_partial_true_prefixes']+=int(a<N)
        assert screen[0]<=i and screen[1]<=j
        assert costNW<=2*N+j and costSE<=2*N+i
        t,s,r=F(N-a,N),F(N-i,N),F(N-j,N)
        U,V=s+t,r+t
        g=F(sums[0][a][0]-sums[0][a][1],SCALE*N)
        k=1+t-g
        C=F(a+i+j,N)
        assert C==3-U-V+t
        assert (g-U)*(k-2*V)>U*V
        assert g>U>=t and V>=t and g<=G<=g+t
        assert k>2*V and k-V>0 and 2*g-t>0
        assert 0<=t<g*(1-g)
        top=t+(g*(1-g)-t)/(2*g-t)
        assert t<=V<top
        z=t/(g*(1-g))
        H=2-(1-g)*z
        w=(V-t)*H/((1-g)*(1-z))
        assert 0<=z<1 and 0<=w<1
        J=w*(1-z);E=H-J
        Vn=g*z*H+J;Un=(1-g*z)*H-2*J
        assert H>=1 and E>=1
        assert V==(1-g)*Vn/H
        assert g*(k-2*V)/(k-V)==g*Un/E
        assert U<g*Un/E
        prob=5*G/(4+G)
        envelope=((1-prob)*U+prob*V)/C
        assert envelope<=F(73,800)
        # Equivalence of C11c with the target envelope, before substitution.
        e=F(73,800)
        A=4*(1+e)+(e-4)*G;B=4*e+(5+e)*G;D=e*(3+t)*(4+G)
        assert D-A*U-B*V==(4+G)*(e*C-((1-prob)*U+prob*V))
        counts['parameter_projections']+=1
        true.append(sum(state))
    cstar=min(true)
    prob=5*G/(4+G)
    ecost=(1-prob)*costNW+prob*costSE
    ratio=ecost/cstar
    assert ratio<=F(873,800)
    if ident.startswith('hard_'):
        q=N//4
        expected=3*N-q+1 if ident.startswith('hard_U') else 3*N-q
        assert cstar==expected
        if ident.startswith('hard_U'):
            assert costNW==3*N-1 and costSE==3*N
            assert ecost==3*N-1+F(5*q,2*N+q)
    records.append({'id':ident,'N':N,'Cstar':cstar,'NW_cost':costNW,'SE_cost':costSE,'prob_SE':str(prob),'expected_cost':str(ecost),'ratio':str(ratio)})

# Closed cube checks include the limiting faces g=0,1 and z=1 which do not
# represent strict legal certificate states. Analytic bounds cover the cube.
cube_points=0
for g,z,w in product([F(i,10) for i in range(11)],repeat=3):
    t=g*(1-g)*z;H=2-(1-g)*z;J=w*(1-z);E=H-J
    assert H>=1 and E>=1+g*z>=1
    assert 0<=g<=g+t<=1
    for G in (g,g+t):
        e=F(73,800);A=4*(1+e)+(e-4)*G
        assert A>=5*e
    cube_points+=1

out={'status':'PASS','scope':'Independent finite state-level checks of C8, C9 and analytic parameter projection; not a universal proof by enumeration and not a new Bernstein coefficient replay','counts':counts,'cube_points':cube_points,'synthetic_seed':2026102402,'grid_rows_numerators':GRID,'row_denominator':SCALE,'archive_records':records,'python':sys.version.split()[0],'elapsed_seconds':time.monotonic()-START,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'Analytic_Reduction_Finite_Check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('archive_records','grid_rows_numerators')},indent=2))
