#!/usr/bin/env python3
"""Own stdlib exact checks of P22's explicit terminal-chain lower family.

No external code, network, packages or empirical data. Finite checks are not
a replacement for the analytic proof or a test of historical priority.
"""
from decimal import Decimal, localcontext
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def supported(p, rivals):
    """Solve both scalarisation inequalities exactly, with integer fractions."""
    ln, ld, hn, hd = 0, 1, 1, 1
    for rc, rf in rivals:
        dx, dy = rc - p[0], rf - p[1]
        slope = dx - dy
        if slope > 0:
            bn, bd = -dy, slope
            if bn * ld > ln * bd:
                ln, ld = bn, bd
        elif slope < 0:
            bn, bd = dy, -slope
            if bn * hd < hn * bd:
                hn, hd = bn, bd
        elif dy < 0:
            return False
    return ln * hd <= hn * ld


def make(x, y, q, pad, winner):
    assert x >= y >= 1 and q >= 1 and y*y*q > 1 and pad >= 0
    D = x*x + 2*x*y + 2*y*y
    n0, scale = D*q, 2*D
    n = n0 + pad
    ellL, ellR = 2*y*(x+y)*q, (x+y)**2*q
    zero, one = (0, 0), (scale, scale)
    rows = [
        [zero]*pad + [(2*(x+y)**2, 2*y*(x+y))]*n0,
        [zero]*pad + [(D, D)]*ellL + [one]*(n0-ellL),
        [zero]*pad + [(scale, 0)]*ellR + [one]*(n0-ellR),
    ]
    rows[1 if winner == 'L' else 2][-1] = zero
    assert all(0 <= f <= c <= scale for group in rows for c,f in group)
    corners = []
    for group in rows:
        c, f = 0, 0
        groupcorners = []
        for k in range(n+1):
            if k:
                c += group[k-1][0]
                f += group[k-1][1]
            width = (n-k)*scale
            groupcorners.append(((c,f),(c+width,f+width)))
        corners.append(groupcorners)
    return corners, n, pad+ellL+1, pad+ellR+1, rows, scale


def true(corners, state):
    (pl, pu), (ll, lu), (rl, ru) = [g[s] for g,s in zip(corners,state)]
    for rival in (ll,rl):
        if rival[0] <= pu[0] and rival[1] <= pu[1] and rival != pu:
            return False
    return not supported(pl,(lu,ru))


def expected(n,bL,bR,winner,state):
    a,i,j = state
    return a == n and ((i == n and j >= bR) if winner == 'L'
                      else (j == n and i >= bL))


def main():
    records = []
    total_states = 0
    full_states = 0
    slice_states = 0
    # Every state for small worlds; whole candidate-full slices for larger
    # ones, together with the monotone exclusion at (N-1,N,N).
    cases = [(1,1,2,0), (1,1,2,3), (1,1,3,0), (1,1,4,0),
             (2,1,2,0), (3,2,1,0), (9,8,1,0), (9,8,1,4)]
    for x,y,q,pad in cases:
        for winner in ('L','R'):
            corners,n,bL,bR,rows,scale = make(x,y,q,pad,winner)
            pl = corners[0][n-1][0]
            assert supported(pl,(corners[1][n][1],corners[2][n][1]))
            assert not true(corners,(n-1,n,n))
            usefull = n <= 20
            states = product(range(n+1),repeat=3) if usefull else (
                (n,i,j) for i,j in product(range(n+1),repeat=2))
            checked, positive, mincost = 0,0,None
            for state in states:
                got = true(corners,state)
                want = expected(n,bL,bR,winner,state)
                assert got == want, (x,y,q,pad,winner,state,got,want)
                checked += 1
                if got:
                    positive += 1
                    cost = sum(state)
                    mincost = cost if mincost is None else min(mincost,cost)
            assert positive == (n-bR+1 if winner == 'L' else n-bL+1)
            assert mincost == 2*n + (bR if winner == 'L' else bL)
            other = make(x,y,q,pad,'R' if winner == 'L' else 'L')[4]
            assert rows[0] == other[0]
            assert rows[1][:-1] == other[1][:-1]
            assert rows[2][:-1] == other[2][:-1]
            total_states += checked
            if usefull:
                full_states += checked
            else:
                slice_states += checked
            records.append(dict(x=x,y=y,q=q,padding=pad,N=n,world=winner,
                                base_L=bL,base_R=bR,
                                checking='all_prefixes' if usefull else
                                'full_candidate_slice_and_monotone_exclusion',
                                states_checked=checked,true_states=positive,
                                minimum_certificate=mincost))

    # Independently evaluate the stated determinant identities in rational
    # coordinates, including cases not enumerated above.
    identities = 0
    for x in range(1,9):
        for y in range(1,x+1):
            for q in range(1,6):
                D = x*x+2*x*y+2*y*y
                h = Q(1,D*q)
                P,Qv = Q((x+y)**2,D), Q(y*(x+y),D)
                a,c,d = Q(x*y,D),Q(x*x,D),Q(y*y,D)
                detL = (a+h*(1-P))*(a-h*Qv)-(c-h*(1-Qv))*(d+h*P)
                detR = (a-h*P)*(a+h*(1-Qv))-(c+h*Qv)*(d-h*(1-P))
                formulaL = h*Q(x+y,D*D)*(y**3-x*x*y-x**3+Q(x,q))
                formulaR = -h*Q(y**3*(x+y),D*D)-h*h*Q(x*(x+y),D)
                assert detL == formulaL <= 0
                assert detR == formulaR < 0
                identities += 1

    weighted = []
    for W,X,Y in product(map(Q,(1,10,100)),
                         (Q(1,100),Q(1),Q(7,3),Q(100)),
                         (Q(1,100),Q(1),Q(7,3),Q(100))):
        denom = X*(W+X)+Y*(W+Y)
        theta = Y*(W+Y)/denom
        ratio = 1+X*Y/denom
        assert (W+X+(1-theta)*Y)/(W+X) == ratio
        assert (W+Y+theta*X)/(W+Y) == ratio
        det = 1+min(X,Y)/(W+max(X,Y))
        assert det == min(1+Y/(W+X),1+X/(W+Y))
        weighted.append(dict(W=str(W),X=str(X),Y=str(Y),theta=str(theta),
                             randomised_ratio=str(ratio),deterministic_ratio=str(det)))

    with localcontext() as ctx:
        ctx.prec = 70
        lo,hi = Decimal(1),Decimal(2)
        for _ in range(200):
            mid = (lo+hi)/2
            poly = mid**4+mid**3-mid-2
            if poly < 0:
                lo=mid
            else:
                hi=mid
        k=(lo+hi)/2
        excess=k*k/(3*(k*k+2*k+2)*(k*k+1)-2*k*k)
        approximate = {'k_star':str(k), 'ratio':str(1+excess),
                       'scope':'Decimal approximation; exact constant is defined by the polynomial in the proof.'}
    result = dict(status='PASS',
                  scope='Explicit finite archives and exact formula identities; no global optimum or historical priority check.',
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  proof_sha256=hashlib.sha256((ROOT/'Nonvanishing_Triangular_Lower_Bounds_P22.md').read_bytes()).hexdigest(),
                  worlds=records,states_checked=total_states,
                  fully_enumerated_prefix_states=full_states,
                  candidate_full_slice_states=slice_states,
                  candidate_census_determinant_identity_cases=identities,
                  weighted_cases=weighted,weighted_cases_checked=len(weighted),
                  rational_alphabet_9_8_limit=str(1+Q(1728,47729)),
                  symmetric_randomised_limit='29/28',symmetric_deterministic_limit='15/14',
                  within_family_optimum_approximation=approximate,
                  new_measurements=0,network=False,external_code=False,installs=False)
    target=ROOT/'Nonvanishing_Triangular_Lower_Check.json'
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','states_checked',
          'fully_enumerated_prefix_states','candidate_full_slice_states',
          'candidate_census_determinant_identity_cases','weighted_cases_checked',
          'within_family_optimum_approximation')},indent=2))


if __name__ == '__main__':
    main()
