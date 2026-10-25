"""Independent finite checks of the constructive continuations and row embedding.

No Ramsey theorem, measurable-kernel claim, minimax theorem or infinite-domain
lower bound is proved by this script. All arithmetic is exact Fraction arithmetic.
The enumerator treats histories as observed value sets, not adaptive policy paths.
"""
from fractions import Fraction as F
from itertools import product, combinations
from pathlib import Path
import json, hashlib, platform, datetime

def fill_below(limit, count, used):
    answer=[];j=2
    while len(answer)<count:
        value=limit/j;j+=1
        if value not in used:
            answer.append(value);used.add(value)
    return answer

def fill_above(limit, count, used):
    answer=[];j=1
    while len(answer)<count:
        value=limit+j;j+=1
        if value not in used:
            answer.append(value);used.add(value)
    return answer

def positive_completion(L,R,m,n):
    LL=list(L);RR=list(R);used=set(L+R)
    if len(L)<m and len(R)<n:
        r=max(R,default=F(0));l=min(L,default=r+3)
        u=r+(l-r)/3;v=r+2*(l-r)/3
        LL.append(u);RR.append(v);used.update((u,v))
        LL+=fill_above(v,m-len(LL),used)
        RR+=fill_below(u,n-len(RR),used)
    elif len(L)==m:
        ls=sorted(L);v=(ls[0]+ls[1])/2 if len(ls)>1 else ls[0]+1
        RR.append(v);used.add(v)
        RR+=fill_below(ls[0],n-len(RR),used)
    else:
        rs=sorted(R);u=(rs[-1]+rs[-2])/2 if len(rs)>1 else rs[-1]/2
        LL.append(u);used.add(u)
        LL+=fill_above(rs[-1],m-len(LL),used)
    return LL,RR

def phi(z,N):return (F(3,5)+z/(5*(z+1)))/N
def inverse_phi(t,N):return (5*N*t-3)/(4-5*N*t)
def negative_completion(L,R,m,n,N):
    ell=F(3,5*N);high=F(4,5*N)
    lo=max([ell]+[phi(x,N) for x in R]);hi=min([high]+[phi(x,N) for x in L]);c=(lo+hi)/2
    LL=[phi(x,N) for x in L]+[(c+high)/2]*(m-len(L))
    RR=[phi(x,N) for x in R]+[(ell+c)/2]*(n-len(R))
    assert lo<hi
    assert max(RR)<min(LL)
    assert all(ell<x<high and inverse_phi(x,N)>0 and phi(inverse_phi(x,N),N)==x for x in LL+RR)
    return LL,RR

def row_checks(L,R,N):
    f=F(1,2*N)
    for z in L:
        u=phi(z,N);last=N*u-F(1,2)
        assert F(1,10)<last<F(3,10)
        assert (1+last)/N==f+u
        assert last==F(3*z+1,10*(z+1))
    for z in R:
        v=phi(z,N);last=N*(f/v-F(1,2))
        assert last>0
        assert (F(3*N,2)+last)/N==1+f/v
        assert last==N*(z+2)/(2*(4*z+3))
    # Candidate is nondominated for every completed family member.
    assert F(1,N)>f and F(3,2)>1
    return sum(u<v for u in L for v in R)

def main():
    counts={'no_edge_partial_histories':0,'both_sides_missing':0,'all_L_observed':0,'all_R_observed':0,'negative_threshold_completions':0,'embedded_unique_edge_archives':0,'hard_integer_embeddings':0}
    alphabet=[F(i) for i in range(1,6)]
    for m,n in product(range(1,4),repeat=2):
        for tags in product((0,1,2),repeat=len(alphabet)):
            L=[z for z,t in zip(alphabet,tags) if t==1];R=[z for z,t in zip(alphabet,tags) if t==2]
            if len(L)>m or len(R)>n or len(L)+len(R)==m+n:continue
            if any(l<r for l in L for r in R):continue
            counts['no_edge_partial_histories']+=1
            category='both_sides_missing' if len(L)<m and len(R)<n else ('all_L_observed' if len(L)==m else 'all_R_observed')
            counts[category]+=1
            LL,RR=positive_completion(L,R,m,n)
            assert len(LL)==m and len(RR)==n and LL[:len(L)]==L and RR[:len(R)]==R
            assert len(set(LL+RR))==m+n and min(LL+RR)>0
            assert sum(l<r for l in LL for r in RR)==1
            for N in (2,3,5,7):
                negative_completion(L,R,m,n,N);counts['negative_threshold_completions']+=1
                assert row_checks(LL,RR,N)==1;counts['embedded_unique_edge_archives']+=1
    for m,n in product(range(1,4),repeat=2):
        k=m+n
        for S in combinations(range(1,8),k):
            L=[F(S[n-1])]+[F(x) for x in S[n+1:]]
            R=[F(x) for x in S[:n-1]]+[F(S[n])]
            assert len(L)==m and len(R)==n
            for N in (2,3,5,7):
                assert row_checks(L,R,N)==1
                M=max(S);bound=10*N*(M+1)
                coordinates=[F(0),F(1),F(1,2*N),F(3*N,2)]
                coordinates += [F(3*z+1,10*(z+1)) for z in L]
                coordinates += [N*(z+2)/(2*(4*z+3)) for z in R]
                assert all(0<=x.numerator<=bound and 1<=x.denominator<=bound for x in coordinates)
                assert N+k+2*(N-1)==(k+1)+3*N-3
                counts['hard_integer_embeddings']+=1
    result={'status':'PASS','counts':counts,'python':platform.python_version(),'finished_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Finite exact-rational continuation/embedding checks only. No verification of universal Ramsey, minimax, private-state kernels or arbitrary-policy lower bound.'}
    target=Path(__file__).with_name('Ramsey_Continuation_Check.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
