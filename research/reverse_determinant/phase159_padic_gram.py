#!/usr/bin/env python3
"""Phase159: q-adic Smith filtration of the SAME ordinary-jet trace Gram.

Exact arithmetic modulo 2^64 and 2^128, not floating point or a field bound.
The pivot algorithm uses invertible row/column operations over Z/(2^K).
All observed invariant exponents are < K, so their sums are exact v2(det).
"""
from __future__ import annotations

from phase159_observation_continuum import ordinary_effective, beta, vq


def valuation_2_bounded(a,K):
    if a==0:return K
    return (a&-a).bit_length()-1


def smith_exponents_2(matrix,K):
    """Find 2-adic pivot exponents using unit operations modulo 2^K.

    Returns (exponents, censored_nullity). A complete result is exact only if
    censored_nullity=0, i.e. all pivots are visible below precision K.
    """
    n=len(matrix)
    assert all(len(row)==n for row in matrix)
    mod=1<<K
    a=[[int(v)%mod for v in row] for row in matrix]
    out=[]
    for k in range(n):
        best=K
        pivot=None
        for i in range(k,n):
            for j in range(k,n):
                v=valuation_2_bounded(a[i][j],K)
                if v<best:
                    best=v
                    pivot=(i,j)
                    if best==0:break
            if best==0:break
        if pivot is None:break
        i,j=pivot
        a[k],a[i]=a[i],a[k]
        if j!=k:
            for row in a:row[k],row[j]=row[j],row[k]
        two=1<<best
        inv=pow(a[k][k]//two,-1,mod//two)
        r=a[k]
        for i in range(k+1,n):
            if not a[i][k]:continue
            assert a[i][k]%two==0
            multiplier=((a[i][k]//two)*inv)%(mod//two)
            if multiplier:
                for j in range(k+1,n):
                    a[i][j]=(a[i][j]-multiplier*r[j])%mod
                a[i][k]=0
        out.append(best)
    return out,n-len(out)


def gram_mod_2_power(E,weights,K):
    mod=1<<K
    rows=len(E)
    width=len(weights)
    Ew=[[int(v)*weights[k]%mod for k,v in enumerate(row)] for row in E]
    return [[sum(Ew[i][k]*int(E[j][k]) for k in range(width))%mod
             for j in range(rows)] for i in range(rows)]


def exact_2_valuation(matrix):
    estimates=[]
    for K in (64,128):
        invariants,unknown=smith_exponents_2(matrix,K)
        assert not unknown and max(invariants)<64
        estimates.append((sum(invariants),len(invariants),max(invariants)))
    assert estimates[0]==estimates[1]
    return estimates[0]


def original_gram_cases():
    D,p,R,S=163,31,30,5
    full=[(x,0) for x in range(-13,14)]+[(x,1) for x in range(-2,3)]
    re=sorted((q for q in full if q[1]==0),
              key=lambda q:(abs(q[0]),q[0]))[:21]
    nonreal=sorted((q for q in full if q[1]!=0),
                   key=lambda q:(q[0]*q[0]+D,abs(q[0]),q[0]))
    chosen=re+nonreal
    assert len(chosen)==26
    cases=((None,430,3187,None),((0,0),450,3200,1525),
           ((10,0),450,3176,1513))
    for removed,floor,want,e_want in cases:
        Q=[q for q in chosen if q!=removed]
        E,weights,_=ordinary_effective(Q,D,R,S)
        assert beta(Q,D,R,S)==floor
        if e_want is not None:
            assert len(E)==len(E[0])==R*S
            ve,_,me=exact_2_valuation(E)
            assert ve==e_want and me<64
            assert 2*ve+sum(vq(w,2) for w in weights)==want
        else:
            assert len(E[0])==155 and len(E)==R*S
        matrix=gram_mod_2_power(E,weights,128)
        v,rank,max_invariant=exact_2_valuation(matrix)
        assert rank==R*S and v==want
        assert v>=floor
        print('PHASE159_EXACT_2ADIC',dict(removed=removed,
             nodes=len(Q),effective_channels=len(weights),
             beta2=floor,v2_det_gram=v,max_smith_exponent=max_invariant),
             flush=True)
    print('PHASE159_VALUATION_NONMONOTONE_PASS: finite exact',flush=True)


def tiny_independent_bareiss():
    from sympy import Matrix,diag
    D,R,S=3,2,2
    for Q in ([(0,2)],[(0,2),(0,1)]):
        E,w,_=ordinary_effective(Q,D,R,S)
        G=Matrix(E)*diag(*w)*Matrix(E).T
        expected=vq(abs(int(G.det(method='domain-ge'))),2)
        M=gram_mod_2_power(E,w,128)
        assert exact_2_valuation(M)[0]==expected


def main():
    tiny_independent_bareiss()
    original_gram_cases()
    print('PHASE159_PADIC_GRAM_PASS: finite only',flush=True)


if __name__=='__main__':main()
