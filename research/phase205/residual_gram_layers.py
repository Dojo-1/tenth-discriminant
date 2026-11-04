#!/usr/bin/env python3
"""Phase205-A: p-adic source-normalized Gram Smith layers; issue #139.
Independent modular diagonalization of the residual metric, on original E.
"""
from collections import Counter
from source_spectral_pilot import E, B, detG, vp, rank
N=len(E);M=len(E[0])

def vcap(z,p,K):
    if z==0:return K
    t=0
    while z%p==0:z//=p;t+=1
    return t

def normalized_C(p,K=22,L=8):
    mod=p**K
    A=[[x%mod for x in row] for row in E]
    U=[[int(i==j) for j in range(N)] for i in range(N)]
    exps=[]
    for k in range(N):
        v,i,j=min((vcap(A[i][j],p,K),i,j)
                  for i in range(k,N) for j in range(k,M))
        assert v<K
        A[k],A[i]=A[i],A[k];U[k],U[i]=U[i],U[k]
        for rr in A:rr[k],rr[j]=rr[j],rr[k]
        pv=p**v;z=A[k][k];inner=mod//pv
        inv=pow(z//pv,-1,inner)
        for i in range(k+1,N):
            if A[i][k]:
                t=(A[i][k]//pv)*inv%inner
                A[i]=[(x-t*y)%mod for x,y in zip(A[i],A[k])]
                U[i]=[(x-t*y)%mod for x,y in zip(U[i],U[k])]
        for j in range(k+1,M):
            if A[k][j]:
                t=(A[k][j]//pv)*inv%inner
                for i in range(N):A[i][j]=(A[i][j]-t*A[i][k])%mod
        exps.append(v)
    assert K-max(exps)>L
    C=[];modH=p**L
    for i,k in enumerate(exps):
        row=[]
        for j in range(M):
            z=sum(U[i][r]*E[r][j] for r in range(N))%mod
            assert z%(p**k)==0
            row.append(z//(p**k)%modH)
        C.append(row)
    assert rank(C,p)[0]==N
    H=[[sum(x*y*w for x,y,w in zip(a,b,B))%modH for b in C] for a in C]
    return exps,H

def residue_smith(H,p,L=8):
    n=len(H);mod=p**L;A=[[x%mod for x in row] for row in H]
    levels=[]
    for k in range(n):
        v,i,j=min((vcap(A[i][j],p,L),i,j) for i in range(k,n) for j in range(k,n))
        assert v<L
        A[k],A[i]=A[i],A[k]
        for rr in A:rr[k],rr[j]=rr[j],rr[k]
        pv=p**v;inner=mod//pv;inv=pow(A[k][k]//pv,-1,inner)
        for i in range(k+1,n):
            if A[i][k]:
                t=(A[i][k]//pv)*inv%inner
                A[i]=[(x-t*y)%mod for x,y in zip(A[i],A[k])]
        for j in range(k+1,n):
            if A[k][j]:
                t=(A[k][j]//pv)*inv%inner
                for i in range(n):A[i][j]=(A[i][j]-t*A[i][k])%mod
        levels.append(v)
    return Counter(levels)

expected={3:{0:31,1:1},5:{0:29,1:2,2:1},7:{0:32}}
for p in (3,5,7):
    k,H=normalized_C(p);hist=residue_smith(H,p)
    assert dict(sorted(hist.items()))==expected[p]
    assert 2*sum(k)+sum(t*n for t,n in hist.items())==vp(detG,p)
    assert N-rank(H,p)[0]==sum(n for t,n in hist.items() if t>0)
    print('RESIDUAL_LAYERS',p,dict(sorted(hist.items())),
          'source_smith_index',sum(k),'residual_valuation',sum(t*n for t,n in hist.items()))
print('PASS Phase205 three-prime normalized residual Smith spectrum')
