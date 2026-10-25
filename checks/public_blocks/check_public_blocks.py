"""Independent exact finite checks of the public constant-block certificate lemma.

No project or Phase 1 checker is imported. Dependent certificates are obtained
by exhaustive truth-table intersection. Independent certificates enumerate all
attainable finite-alphabet row-sum completions, not geometric endpoint tests.
The finite checks support but do not replace the analytic proof.
"""
from fractions import Fraction as F
from itertools import product, combinations_with_replacement
from functools import lru_cache
from pathlib import Path
import argparse, datetime, hashlib, json, time

# Coordinates share denominator 20; common normalisation by N is unnecessary
# for dominance and nonnegative scalarisation comparisons.
ALPHABET=((0,0),(20,20),(16,6),(10,10),(20,0))

def good(means):
    p=means[0]
    for r in means[1:]:
        if r[0]<=p[0] and r[1]<=p[1] and r!=p:return False
    low,high=F(0),F(1)
    for r in means[1:]:
        # alpha*(p0-r0)+(1-alpha)*(p1-r1) <= 0
        a=(p[0]-r[0])-(p[1]-r[1]); b=r[1]-p[1]
        if a>0:high=min(high,F(b,a))
        elif a<0:low=max(low,F(b,a))
        elif b<0:return True
    return low>high

def rows_for(parts,assignment):
    rows=[];k=0
    for lengths in parts:
        rr=[]
        for length in lengths:
            rr.extend([assignment[k]]*length);k+=1
        rows.append(tuple(rr))
    return tuple(rows)

def row_sums(rows):
    return tuple((sum(ALPHABET[j][0] for j in rr),sum(ALPHABET[j][1] for j in rr)) for rr in rows)

def observation(rows,b):return tuple(rr[:n] for rr,n in zip(rows,b))

def rounding(lengths,b):
    if b==0:return 0
    end=0
    for n in lengths:
        end+=n
        if b<=end:return end
    raise ValueError('prefix out of range')

def exhaustive_dependent_table(parts):
    n=sum(parts[0]);assert all(sum(x)==n for x in parts)
    prefixes=list(product(range(n+1),repeat=3))
    table={};archives=[]
    for assignment in product(range(len(ALPHABET)),repeat=sum(map(len,parts))):
        rows=rows_for(parts,assignment);verdict=good(row_sums(rows))
        archives.append((rows,verdict))
        for b in prefixes:
            key=observation(rows,b)
            table[key]=table.get(key,True) and verdict
    return archives,prefixes,table

@lru_cache(None)
def all_missing_sums(n):
    # Each ordered finite-alphabet row completion has one of these exact sums;
    # every enumerated multiset is realised by an ordered row completion.
    values=set()
    for c in combinations_with_replacement(range(len(ALPHABET)),n):
        values.add((sum(ALPHABET[j][0] for j in c),sum(ALPHABET[j][1] for j in c)))
    return tuple(sorted(values))

q_oracle_calls=0
q_completed_mean_triples=0
@lru_cache(None)
def q_certificate(n,summary):
    global q_oracle_calls,q_completed_mean_triples
    q_oracle_calls+=1
    choices=[]
    for b,x,y in summary:
        choices.append(tuple((x+u,y+v) for u,v in all_missing_sums(n-b)))
    for means in product(*choices):
        q_completed_mean_triples+=1
        if not good(means):return False
    return True

def q_true(n,obs):
    summary=tuple((len(rr),sum(ALPHABET[j][0] for j in rr),sum(ALPHABET[j][1] for j in rr)) for rr in obs)
    return q_certificate(n,summary)

def profiles(n):
    return {
      'unit':tuple(tuple(F(1) for _ in range(n)) for _ in range(3)),
      'fractional':tuple(tuple(F(g+j+2,7+g+2*j) for j in range(n)) for g in range(3)),
      'expensive_last':tuple(tuple(F(1000 if j==n-1 else 1,7) for j in range(n)) for _ in range(3)),
      'expensive_first':tuple(tuple(F(1000 if j==0 else 1,11) for j in range(n)) for _ in range(3)),
      'heterogeneous':tuple(tuple(F((g+1)*7**j,g+j+2) for j in range(n)) for g in range(3)),
    }

def price_data(parts,bs):
    result={};n=sum(parts[0])
    for name,w in profiles(n).items():
        W=tuple(tuple(sum(rr[:b],F(0)) for b in range(n+1)) for rr in w)
        rho=max(W[g][rounding(parts[g],b)]/W[g][b] for g in range(3) for b in range(1,n+1))
        costs=tuple(sum((W[g][b[g]] for g in range(3)),F(0)) for b in bs)
        result[name]=(costs,rho)
    return result

def check_partition(parts, qtable=None):
    archives,bs,table=exhaustive_dependent_table(parts);n=sum(parts[0]);m=max(max(x) for x in parts)
    prices=price_data(parts,bs);rounded={b:tuple(rounding(parts[g],b[g]) for g in range(3)) for b in bs}
    positive=negative=certificates=inequalities=0
    max_ratio=F(0)
    for rows,is_good in archives:
        positive+=is_good;negative+=not is_good
        dt=[];qt=[]
        for b in bs:
            d=table[observation(rows,b)]
            qr=observation(rows,rounded[b])
            q=qtable[qr] if qtable is not None else q_true(n,qr)
            assert d==q,(parts,rows,b,d,q)
            dt.append(d);certificates+=d
            raw=observation(rows,b)
            qt.append(qtable[raw] if qtable is not None else q_true(n,raw))
            if not is_good:assert not d and not qt[-1]
        if not is_good:continue
        for name,(costs,rho) in prices.items():
            cd=min(c for c,t in zip(costs,dt) if t)
            cq=min(c for c,t in zip(costs,qt) if t)
            assert cd<=cq<=rho*cd,(parts,rows,name,cd,cq,rho)
            for setup in [F(0),F(1,3),F(100)]:
                assert setup+cd<=setup+cq<=rho*(setup+cd)
                inequalities+=1
            if name=='unit':
                assert cq<=m*cd
                max_ratio=max(max_ratio,cq/cd)
    return {'partitions':parts,'N':n,'m':m,'complete_archives':len(archives),
      'positive_archives':positive,'negative_archives':negative,
      'prefix_states_checked':len(archives)*len(bs),'distinct_observed_transcripts':len(table),
      'true_prefix_states':certificates,'price_profiles':list(prices),
      'rho_by_profile':{k:str(v[1]) for k,v in prices.items()},
      'cost_comparisons_including_setups':inequalities,'maximum_unit_distortion_in_finite_family':str(max_ratio)}

def exact_sharp_family(n):
    eps=F(1,100*n)
    p=(F(3,4)+eps,F(1,4)+eps);left=(F(1,2),F(1,2));right=(F(1),F(0))
    actual=(p,left,right)
    assert all(0<=y<=x<=1 for x,y in actual)
    assert good(actual)
    negatives=[]
    # Construct one legal negative completion after each immediate predecessor
    # of full census. This is stronger than a claim based only on sampled prices.
    for missing in range(3):
        completion=(F(0),F(0)) if missing==0 or (missing==2 and n==1) else (F(1),F(1))
        changed=list(actual)
        changed[missing]=tuple(((n-1)*actual[missing][j]+completion[j])/n for j in range(2))
        assert not good(tuple(changed)),(n,missing,changed)
        negatives.append([[str(v) for v in x] for x in changed])
    # In the block model a wholly unread group can be set to (0,0).
    for unread in range(3):
        changed=list(actual);changed[unread]=(F(0),F(0))
        assert not good(tuple(changed))
    weights=[F(1,7)]+[F(3*j+2,11) for j in range(1,n)]
    rho=sum(weights)/weights[0]
    assert (3*sum(weights))/(3*weights[0])==rho
    return {'N':n,'unit_CD':3,'unit_CQ':3*n,'unit_ratio':n,
      'common_prices':[str(x) for x in weights],'weighted_CD':str(3*weights[0]),
      'weighted_CQ':str(3*sum(weights)),'weighted_ratio_and_rho':str(rho),
      'explicit_negative_predecessor_completions':negatives}


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

def main():
    if not __debug__:
        raise SystemExit('Exact checks require assertions; run without -O or -OO.')
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=Path(__file__).with_name('Public_Block_Dependence_Check.json'));args=parser.parse_args()
    destination=prepare_output(args.output)
    started=time.time()
    _,_,qtable=exhaustive_dependent_table(((1,1),(1,1),(1,1)))
    results=[]
    for parts in product(((2,),(1,1)),repeat=3):results.append(check_partition(parts,qtable))
    for parts in [((1,2),(2,1),(3,)),((2,1),(3,),(1,2)),((1,1,1),(3,),(3,))]:
        results.append(check_partition(parts))
    sharp=[exact_sharp_family(n) for n in range(1,31)]
    result={'schema':'p44-public-block-dependence-v1','status':'PASS',
      'method':'Exact dependent truth-table intersection and independent finite-alphabet completion enumeration; no endpoint oracle or project checker imported.',
      'alphabet_common_denominator':20,'alphabet_integer_numerators':ALPHABET,
      'partition_families':results,'sharp_families':sharp,
      'totals':{'partition_families':len(results),'prefix_states_checked':sum(x['prefix_states_checked'] for x in results),
        'positive_archive_cases':sum(x['positive_archives'] for x in results),'negative_archive_cases':sum(x['negative_archives'] for x in results),
        'cost_comparisons_including_setups':sum(x['cost_comparisons_including_setups'] for x in results),
        'independent_Q_cached_calls':q_oracle_calls,'independent_Q_completed_mean_triples':q_completed_mean_triples,
        'sharp_family_N_values':len(sharp),'explicit_negative_predecessor_completions':3*len(sharp)},
      'limitations':['Finite alphabet and stated partition families only; cases overlap and are not independent physical samples.',
         'No universal proof or historical-priority claim follows from these counts.',
         'The analytic statement requires public partitions, exact equality within blocks and a Cartesian product of legal block completions.',
         'Weighted sharpness with common price profiles is derived from explicit certificate characterisation, not an operational measurement.'],
      'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'elapsed_seconds':time.time()-started,'finished_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    write_output(destination,result)
    print(json.dumps({'status':result['status'],'totals':result['totals'],'elapsed_seconds':result['elapsed_seconds']}))

if __name__=='__main__':main()
