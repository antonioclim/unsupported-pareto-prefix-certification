"""Exact hindsight comparator via merged supporting-threshold streams.

Research prototype. Inputs are complete realised archives; this is NOT an
online acquisition policy. Independent endpoint-containing row domains in
[0,1]^2, arbitrary positive public row prices, and optional unequal archive
lengths / positive known mean weights. Default means are uniform in each group.
All arithmetic is Fraction. The construction removes the pair enumeration
from P55 Supplement S1.1; the proof is in research/geometry.md.
"""
from fractions import Fraction as F
from itertools import groupby, product
from heapq import merge
import random
import json
from pathlib import Path
import time
import hashlib
import platform


def arrays(rows, prices=None, weights=None):
    k = len(rows)
    if k < 3 or any(len(r) < 1 for r in rows):
        raise ValueError('Need K>=3 nonempty archives')
    if prices is None:
        prices = [[F(1)] * len(r) for r in rows]
    if len(prices) != k or any(len(p) != len(r) for p,r in zip(prices,rows)):
        raise ValueError('Price dimensions')
    if weights is None:
        weights = [[F(1,len(r))] * len(r) for r in rows]
    if len(weights)!=k or any(len(ws)!=len(r) for ws,r in zip(weights,rows)):
        raise ValueError('Weight dimensions')
    low, high, costs = [], [], []
    for seq, tariffs, ws in zip(rows, prices, weights):
        ws=list(map(F,ws))
        if any(w<=0 for w in ws) or sum(ws)!=1:
            raise ValueError('Mean weights must be strictly positive and sum to one')
        sums, cc = [(F(0), F(0))], [F(0)]
        remaining=[F(1)]
        for (x, y), w, mass in zip(seq, tariffs, ws):
            x, y, w = F(x), F(y), F(w)
            if not (0 <= x <= 1 and 0 <= y <= 1 and w > 0):
                raise ValueError('Domain/price violation')
            sums.append((sums[-1][0] + mass*x, sums[-1][1] + mass*y))
            cc.append(cc[-1] + w)
            remaining.append(remaining[-1]-mass)
        low.append(sums)
        high.append([(x + remaining[b], y + remaining[b])
                     for b,(x,y) in enumerate(sums)])
        costs.append(cc)
    return low, high, costs


def dominates(x, y):
    return x[0] <= y[0] and x[1] <= y[1] and x != y


def interval_oracle(low, high, counts):
    """Independent robust oracle: intersect supporting alpha intervals.

    Does not use witness-pair selection, sorted streams, or comparator costs.
    """
    p, pa = low[0][counts[0]], high[0][counts[0]]
    if any(dominates(low[g][counts[g]], pa) for g in range(1,len(counts))):
        return False
    left, right = F(0), F(1)
    for g in range(1,len(counts)):
        x, y = high[g][counts[g]]
        intercept = y-p[1]
        slope = (x-p[0])-intercept
        if slope == 0:
            if intercept < 0:
                return True
        elif slope > 0:
            left = max(left, -intercept/slope)
        else:
            right = min(right, -intercept/slope)
    return left > right


def brute(rows, prices=None, setup=0, weights=None):
    low, high, costs = arrays(rows, prices, weights)
    k = len(rows)
    best = None
    examined = 0
    for b in product(*(range(len(r)+1) for r in rows)):
        examined += 1
        if interval_oracle(low,high,b):
            value = F(setup) + sum(costs[g][b[g]] for g in range(k))
            if best is None or value < best['cost']:
                best = {'cost': value, 'prefix':b}
    return best, examined


def comparator(rows, prices=None, setup=0, weights=None):
    """O(K N^2 log K) exact arithmetic, O(KN) working storage.

    Returns None for negative archives, otherwise an optimal cost and prefix.
    Candidate is row group 0. setup is common, compulsory and nonnegative.
    Unequal lengths: O((n_A+1)L log K) arithmetic, O(L) storage, where
    L=sum_g(n_g+1). weights are positive rational masses summing to one per group.
    """
    if F(setup) < 0:
        raise ValueError('Negative setup')
    low, high, costs = arrays(rows,prices,weights)
    k, n_A = len(rows),len(rows[0])
    best = None
    stream_states = 0
    feasible_candidate_prefixes = 0
    for a in range(n_A+1):
        p, pa = low[0][a], high[0][a]
        sigma = [a]
        for g in range(1,k):
            safe = next((b for b in range(len(rows[g])+1)
                         if not dominates(low[g][b], pa)),None)
            if safe is None:
                break
            sigma.append(safe)
        if len(sigma) != k:
            continue
        feasible_candidate_prefixes += 1
        base = F(setup) + sum(costs[g][sigma[g]] for g in range(k))
        streams=[]
        for g in range(1,k):
            nw, se = [], []
            for b in range(sigma[g],len(rows[g])+1):
                x,y = high[g][b]
                extra=costs[g][b]-costs[g][sigma[g]]
                if x < p[0] and y > p[1]:
                    A,C = p[0]-x,y-p[1]
                    nw.append((C/(A+C),'NW',extra,g,b))
                elif x > p[0] and y < p[1]:
                    D,E = x-p[0],p[1]-y
                    se.append((E/(D+E),'SE',extra,g,b))
            # Opposite sides cannot occur for one coordinatewise decreasing
            # upper-corner sequence. Every stream is descending in threshold.
            assert not (nw and se)
            seq = nw or list(reversed(se))
            assert all(seq[j][0] >= seq[j+1][0] for j in range(len(seq)-1))
            if seq:
                streams.append(seq)
                stream_states += len(seq)
        best_se = None
        merged = merge(*streams,key=lambda state:state[0],reverse=True)
        for threshold, same_threshold in groupby(merged,key=lambda state:state[0]):
            tied=list(same_threshold)
            # Strict inequality is essential: process NW before inserting
            # equal-threshold SE states. Equal scalarisation scores support A.
            if best_se is not None:
                for _,side,extra,g,b in tied:
                    if side == 'NW':
                        assert g != best_se[3]
                        value=base+extra+best_se[2]
                        if best is None or value < best['cost']:
                            witness=list(sigma)
                            witness[g]=b
                            witness[best_se[3]]=best_se[4]
                            best={'cost':value,'prefix':tuple(witness)}
            for state in tied:
                if state[1]=='SE' and (best_se is None or state[2]<best_se[2]):
                    best_se=state
    if best is not None:
        assert interval_oracle(low,high,best['prefix'])
    return best, {'stream_states':stream_states,
                  'feasible_candidate_prefixes':feasible_candidate_prefixes}


def run_tests():
    seed=20261025
    rng=random.Random(seed)
    cases=[]
    square=[(F(0),F(0)),(F(0),F(1)),(F(1),F(0)),(F(1),F(1)),
            (F(3,5),F(3,5)),(F(1,2),F(1,2))]
    triangle=[(F(0),F(0)),(F(1),F(0)),(F(1),F(1)),
              (F(3,4),F(1,4)),(F(1,2),F(1,2)),(F(1),F(1,2))]
    # Exhaustive N=1 square six-symbol archive corpus, K=3,4.
    for k in (3,4):
        for symbols in product(square,repeat=k):
            cases.append(('exhaustive_square_N1', [[s] for s in symbols],
                          [[F(rng.randint(1,19),rng.randint(1,7))] for _ in symbols],
                          F(rng.randrange(4),3)))
    for k,n,repeats in ((3,2,150),(3,3,150),(3,5,100),
                        (4,2,150),(4,3,100),(5,2,100),(6,2,50)):
        for j in range(repeats):
            alphabet=triangle if j%2 else square
            rows=[[rng.choice(alphabet) for _ in range(n)] for _ in range(k)]
            prices=[[F(rng.randint(1,31),rng.randint(1,9)) for _ in range(n)]
                    for _ in range(k)]
            cases.append(('random_rational_prices',rows,prices,F(rng.randrange(6),5)))
    # Deliberately positive archives stress choice among multiple witnesses,
    # candidate prefixes, nonuniform prices and setup. Paired perturbations
    # change prefix order while preserving each complete mean exactly.
    for k,n,repeats in ((3,3,100),(3,5,100),(4,3,100),(5,3,100)):
        for j in range(repeats):
            means=[(F(3,5),F(3,5)),(F(1,5),F(4,5)),(F(4,5),F(1,5))]
            means += [rng.choice([(F(1,5),F(4,5)),(F(4,5),F(1,5)),
                                  (F(9,10),F(9,10)),(F(3,5),F(3,5))])
                      for _ in range(k-3)]
            rows=[]
            for x,y in means:
                seq=[(x,y)]*n
                dx,dy=F(rng.randint(-2,2),25),F(rng.randint(-2,2),25)
                seq[0]=(x+dx,y+dy)
                seq[-1]=(x-dx,y-dy)
                if j%2:
                    seq.reverse()
                rows.append(seq)
            prices=[[F(rng.randint(1,100),rng.randint(1,9)) for _ in range(n)]
                    for _ in range(k)]
            cases.append(('designed_positive_square',rows,prices,F(rng.randrange(6),5)))
    # Fixed-symbol triangle U/V hard archives; exact prices include expensive
    # final candidate rows, exposing mistakes from compulsory candidate census.
    for q in range(3,10):
        n=4*q
        for world in ('U','V'):
            A=[(1,0)]*(2*q)+[(1,1)]*q+[(0,0)]*(q-1)+[ (0,0) if world=='U' else (1,0)]
            L=[(1,1)]*q+[(0,0)]*(2*q)+[(1,1)]*(q-1)+[ (0,0) if world=='U' else (1,1)]
            R=[(1,0)]*n
            prices=[[F(1)]*n for _ in range(3)]
            prices[0][-1]=F(97,3)
            cases.append(('triangle_hard_UV',[A,L,R],prices,F(2,7)))
    report={'schema':'p56-exact-comparator-merged-stream-v1','seed':seed,
            'cases':len(cases),'positive':0,'negative':0,
            'exhaustive_prefix_states':0,'categories':{},
            'cost_mismatches':0,'returned_certificate_failures':0,
            'python':platform.python_version(),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'arithmetic':'exact fractions.Fraction; no floating-point verdicts',
            'oracle_scope':'Exhaustive prefix enumeration with independent supporting-interval oracle; endpoint theorem assumed',
            'claim_limit':'Finite algorithm validation, not formal verification, novelty proof, online policy, economic measurement, or triangle-ratio improvement'}
    start=time.perf_counter()
    for tag,rows,prices,setup in cases:
        got,stats=comparator(rows,prices,setup)
        want,number=brute(rows,prices,setup)
        report['exhaustive_prefix_states']+=number
        report['categories'][tag]=report['categories'].get(tag,0)+1
        assert (got is None)==(want is None),(tag,rows,got,want)
        if got:
            assert got['cost']==want['cost'],(tag,rows,got,want)
            report['positive']+=1
        else:
            report['negative']+=1
    for j in range(240):
        k=rng.randint(3,5)
        lengths=[rng.randint(1,5) for _ in range(k)]
        if j%2:
            means=[(F(3,5),F(3,5)),(F(1,5),F(4,5)),(F(4,5),F(1,5))]
            means += [(F(9,10),F(9,10))]*(k-3)
            rows=[[means[g]]*lengths[g] for g in range(k)]
        else:
            rows=[[rng.choice(square) for _ in range(n)] for n in lengths]
        prices=[[F(rng.randint(1,50),rng.randint(1,9)) for _ in r] for r in rows]
        masses=[[rng.randint(1,13) for _ in r] for r in rows]
        weights=[[F(w,sum(ws)) for w in ws] for ws in masses]
        setup=F(rng.randint(0,9),7)
        got,stats=comparator(rows,prices,setup,weights)
        want,number=brute(rows,prices,setup,weights)
        report['exhaustive_prefix_states']+=number
        assert (got is None)==(want is None),('weighted',rows,got,want)
        if got:
            assert got['cost']==want['cost'],('weighted',rows,got,want)
            report['positive']+=1
        else:
            report['negative']+=1
    report['cases']+=240
    report['categories']['unequal_lengths_nonuniform_mean_weights']=240
    report['seconds_observed']=time.perf_counter()-start
    report['status']='PASS'
    out=Path(__file__).resolve().parents[1]/'evidence/Geometry_Comparator_P56.json'
    out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    run_tests()
