"""Independent finite ordinal-state audit. Own code; stdlib only.
Enumerates full labelled worlds and conditional observation states. Does not use
manuscript transition probabilities or count-state recurrence to obtain values.
"""
from fractions import Fraction as F
from itertools import permutations, product
from functools import lru_cache
import json
from pathlib import Path


def solve(m,n):
    L=tuple(range(m)); R=tuple(range(m,m+n)); k=m+n
    # Fixed global sorted pattern Rbad^(n-1), Lgood, Rgood, Lbad^(m-1)
    lvals=(n-1,)+tuple(range(n+1,k))
    rvals=tuple(range(n-1))+(n,)
    worlds=[lp+rp for lp in permutations(lvals) for rp in permutations(rvals)]
    stats={'states':0,'nonterminal_states':0,'worlds':len(worlds)}
    count_values={}
    @lru_cache(None)
    def V(lorder,rorder):
        # State records actual ordinal observations, not just counts.
        observed=lorder+rorder
        obsset=set(observed)
        compatible=[w for w in worlds if
          tuple(sorted(lorder,key=lambda j:w[j]))==lorder and
          tuple(sorted(rorder,key=lambda j:w[j]))==rorder and
          (not lorder or not rorder or w[rorder[-1]]<w[lorder[0]])]
        assert compatible
        stats['states']+=1
        if len(observed)==k:
            raise AssertionError('A full no-edge state cannot occur in this prior')
        stats['nonterminal_states']+=1
        options=[]
        for j in range(k):
            if j in obsset: continue
            outcomes={}
            for w in compatible:
                newl=tuple(sorted(lorder+(j,),key=lambda t:w[t])) if j<m else lorder
                newr=tuple(sorted(rorder+(j,),key=lambda t:w[t])) if j>=m else rorder
                if newl and newr and w[newl[0]]<w[newr[-1]]:
                    key=None # strict edge observed
                else:
                    key=(newl,newr)
                outcomes[key]=outcomes.get(key,0)+1
            cost=F(1)
            for key,num in outcomes.items():
                if key is not None: cost+=F(num,len(compatible))*V(*key)
            options.append(cost)
        best=min(options)
        count_values.setdefault((len(lorder),len(rorder)),set()).add(best)
        return best
    value=V((),())
    mm,nn=sorted((m,n))
    formula=F(mm)+F(nn+1,2)-F(mm*mm-1,6*nn)
    assert value==formula,(m,n,value,formula)
    assert all(len(v)==1 for v in count_values.values())
    return {'m':m,'n':n,'enumerated_optimum':str(value),
            'formula':str(formula),'history_orders_do_not_change_value':True,**stats}

if __name__=='__main__':
    rows=[solve(m,n) for m in range(1,5) for n in range(m,5)]
    out={'status':'PASS','scope':'Finite ordinal game only; not numeric/Ramsey proof',
         'method':'Exact posterior enumeration of all labelled worlds and ordinal states',
         'results':rows}
    path=Path(__file__).with_name('Ordinal_World_Enumeration.json')
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
