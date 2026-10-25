"""Independent exact small-game check using full posterior world partitions.
No recurrence A3 is used in the solver. The solver can inspect all previously
revealed relative orders, query any remaining label and adapt every decision.
Its stopping constraint is an actually observed L<R edge, not inferred positivity.
"""
from itertools import permutations, product
from functools import lru_cache
from fractions import Fraction
from math import factorial
from pathlib import Path
import json


def solve(m, n, numeric=False):
    # Sorted colour pattern: R_bad^(n-1), L_good, R_good, L_bad^(m-1).
    Lranks=(n-1, *range(n+1,n+m))
    Rranks=(*range(n-1),n)
    worlds=tuple(tuple(lp)+tuple(rp) for lp,rp in product(permutations(Lranks),permutations(Rranks)))
    k=m+n; count_values={}
    @lru_cache(None)
    def value(mask, ids):
        seen=tuple(i for i in range(k) if mask>>i&1)
        representative=worlds[ids[0]]
        if any(representative[l]<representative[r] for l in seen if l<m for r in seen if r>=m):
            return Fraction()
        # Verify that observational equivalence really makes the edge event common.
        assert all(not any(worlds[w][l]<worlds[w][r] for l in seen if l<m for r in seen if r>=m) for w in ids)
        options=[]
        for nxt in range(k):
            if mask>>nxt&1: continue
            parts={}
            expanded=seen+(nxt,)
            for wid in ids:
                outcome=(worlds[wid][nxt] if numeric else tuple(sorted(expanded,key=lambda label:worlds[wid][label])))
                parts.setdefault(outcome,[]).append(wid)
            options.append(Fraction(1)+sum((Fraction(len(g),len(ids))*value(mask|(1<<nxt),tuple(g)) for g in parts.values()),Fraction()))
        assert options
        best=min(options)
        key=(sum(i<m for i in seen),sum(i>=m for i in seen))
        count_values.setdefault(key,set()).add(best)
        return best
    ans=value(0,tuple(range(len(worlds))))
    lo,hi=sorted((m,n))
    formula=Fraction(lo)+Fraction(hi+1,2)-Fraction(lo*lo-1,6*hi)
    if not numeric:
        assert ans==formula,(m,n,ans,formula)
        assert all(len(v)==1 for v in count_values.values()),count_values
    return {'m':m,'n':n,'worlds':len(worlds),'query_observation':'exact known ranks' if numeric else 'full relative order',
            'optimal_expected_queries':str(ans),'q_formula':str(formula),
            'matches_formula':ans==formula,'posterior_states':value.cache_info().currsize,
            'remaining_value_constant_at_fixed_counts':all(len(v)==1 for v in count_values.values())}

results=[solve(m,n) for m in range(1,5) for n in range(m,5) if m+n<=7]
numeric=[solve(2,2,True),solve(3,3,True)]
report={'method':'Exact posterior dynamic programme over all label/rank assignments and all next-label actions; no recurrence A3 used.',
        'ordinal_cases':results,'numeric_comparisons':numeric,
        'scope_limit':'Finite ordinal checks do not prove the general theorem, Ramsey lemma, arbitrary-real kernel measurability or archive compression. Numeric comparisons are promised fixed-rank games and are not a counterexample to the manuscript lower bound.'}
out=Path(__file__).with_name('full_ordinal_game_results.json');out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
