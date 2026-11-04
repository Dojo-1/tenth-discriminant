#!/usr/bin/env python3
"""Phase205: one frozen 32x168 ordinary-jet source; Issues #139 and #140.
Two independent Gram constructions, p-local Smith normalization, six-block upper.
Finite witness only; no new uniform field-discriminant theorem.
"""
from collections import Counter
from functools import lru_cache
from math import factorial, log

D, RHO, R, S, J = 19, 5, 8, 4, 4
Q = [(x,y) for y in range(-5,6) for x in range(-5,6) if x*x+D*y*y<=25]
rows = [(r,s) for r in range(R) for s in range(S)]
B = [w for j in range(J) for z in Q for w in (2,2*D)]
assert len(Q)==21 and len(rows)==32 and len(B)==168

def mult(v,w):
    a,b=v;c,d=w
    return a*c-D*b*d,a*d+b*c
@lru_cache(None)
def power(z,n):
    out=(1,0)
    for _ in range(n):out=mult(out,z)
    return out
def jet(r,s,j,z):
    if j>r:return (0,0)
    a,b=mult(power(z,r-j),power((z[0],-z[1]),s))
    k=factorial(r)//factorial(r-j)
    return a*k,b*k
E=[[v for j in range(J) for z in Q for v in jet(r,s,j,z)] for r,s in rows]
G=[[sum(x*y*w for x,y,w in zip(a,b,B)) for b in E] for a in E]
@lru_cache(None)
def M(a,b):
    return sum(mult(power(z,a),power((z[0],-z[1]),b))[0] for z in Q)
def moment_gram(i,k):
    r,s=rows[i];t,u=rows[k]
    return 2*sum((factorial(r)//factorial(r-j))*(factorial(t)//factorial(t-j))*M(r-j+u,s+t-j)
                 for j in range(min(J,r+1,t+1)))
assert all(G[i][k]==moment_gram(i,k) for i in range(32) for k in range(32))
assert [sum((x*x+D*y*y)**k for x,y in Q) for k in range(4)]==[21,320,6396,135416]
a=rows.index((0,0));b=rows.index((2,0))
assert [G[a][a],G[a][b],G[b][b]]==[42,-120,15520]

def determinant(A):
    A=[list(row) for row in A];n=len(A)
    if not n:return 1
    sign=1;prev=1
    for k in range(n-1):
        if not A[k][k]:
            j=next((i for i in range(k+1,n) if A[i][k]),None)
            if j is None:return 0
            A[k],A[j]=A[j],A[k];sign=-sign
        q=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                t=A[i][j]*q-A[i][k]*A[k][j]
                assert t%prev==0
                A[i][j]=t//prev
            A[i][k]=0
        prev=q
    return sign*A[-1][-1]
def vp(x,p):
    if not x:return None
    x=abs(x);v=0
    while x%p==0:x//=p;v+=1
    return v
def rank(A,p):
    A=[[x%p for x in row] for row in A];n=len(A);m=len(A[0]);k=0;piv=[]
    for j in range(m):
        t=next((i for i in range(k,n) if A[i][j]),None)
        if t is None:continue
        A[k],A[t]=A[t],A[k]
        q=pow(A[k][j],-1,p)
        for h in range(j,m):A[k][h]=A[k][h]*q%p
        for i in range(k+1,n):
            t=A[i][j]
            if t:
                for h in range(j,m):A[i][h]=(A[i][h]-t*A[k][h])%p
        piv.append(j);k+=1
        if k==n:break
    return k,piv

def local_smith(E,weights,p):
    n=len(E);m=len(E[0]);K=22;q=p**K
    A=[[x%q for x in row] for row in E]
    U=[[int(i==j) for j in range(n)] for i in range(n)]
    exps=[]
    for k in range(n):
        best=(K,None,None)
        for i in range(k,n):
            for j in range(k,m):
                z=A[i][j];v=K
                if z:
                    v=0
                    while z%p==0:z//=p;v+=1
                if v<best[0]:best=(v,i,j)
                if v==0:break
            if best[0]==0:break
        v,i,j=best
        assert v<K
        A[k],A[i]=A[i],A[k];U[k],U[i]=U[i],U[k]
        for line in A:line[k],line[j]=line[j],line[k]
        z=A[k][k];pv=p**v;mod=q//pv
        inv=pow(z//pv,-1,mod)
        for h in range(k+1,n):
            if A[h][k]:
                assert A[h][k]%pv==0
                t=(A[h][k]//pv)*inv%mod
                A[h]=[(x-t*y)%q for x,y in zip(A[h],A[k])]
                U[h]=[(x-t*y)%q for x,y in zip(U[h],U[k])]
        for h in range(k+1,m):
            if A[k][h]:
                assert A[k][h]%pv==0
                t=(A[k][h]//pv)*inv%mod
                for i0 in range(n):A[i0][h]=(A[i0][h]-t*A[i0][k])%q
        exps.append(v)
    assert all(A[i][j]==0 for i in range(n) for j in range(m) if i!=j)
    C=[]
    for i,v in enumerate(exps):
        pv=p**v;line=[]
        for j in range(m):
            z=sum(U[i][r]*E[r][j] for r in range(n))%q
            assert z%pv==0
            line.append(z//pv%p)
        C.append(line)
    r,piv=rank(C,p)
    assert r==n
    minor=determinant([[E[i][j] for j in piv] for i in range(n)])
    assert minor and vp(minor,p)==sum(exps)
    H=[[sum(x*y*w for x,y,w in zip(a,b,weights))%p for b in C] for a in C]
    return Counter(exps),sum(exps),n-rank(H,p)[0]

detG=determinant(G)
assert detG>0
for p in (3,5,7,2,19):
    levels,index,rad=local_smith(E,B,p)
    val=vp(detG,p);extra=val-2*index
    assert extra>=rad>=0
    print('LOCAL',p,dict(sorted(levels.items())),index,rad,extra,val,flush=True)
assert vp(detG,2)==172 and vp(detG,3)==39 and vp(detG,5)==4

# Distinct Phase135 negative: n=8, J=2 and same Q, not a substitution.
E8=[[v for j in range(2) for z in Q for v in jet(r,s,j,z)] for r in range(4) for s in range(2)]
W8=[w for j in range(2) for z in Q for w in (2,38)]
l8,i8,r8=local_smith(E8,W8,3)
assert i8==1 and r8==0 and l8==Counter({0:7,1:1})
print('PHASE135_NEGATIVE',i8,r8,flush=True)

def principal(indices):
    v=determinant([[G[i][j] for j in indices] for i in indices])
    assert v>0
    return v
fib={d:[i for i,(r,s) in enumerate(rows) if r-s==d] for d in range(-3,8)}
part=[[-2,0],[2,4],[6],[-3,-1],[1,3],[5,7]]
assert sorted(d for p in part for d in p)==list(fib)
raw=1;radial=1;paired=1
for i in range(32):raw*=G[i][i]
for v in fib.values():radial*=principal(v)
for ds in part:paired*=principal([i for d in ds for i in fib[d]])
par=[[i for i,(r,s) in enumerate(rows) if (r+s)%2==t] for t in (0,1)]
assert all(G[i][j]==0 for i in par[0] for j in par[1])
assert detG==principal(par[0])*principal(par[1])
assert 0<detG<=paired<=radial<=raw
print('ANALYTIC',dict(raw=log(raw),radial=log(radial),paired=log(paired),
       exact=log(detG),gain=log(radial)-log(paired),
       normalized=(log(radial)-log(paired))/(R*R*S)),flush=True)
assert abs(log(radial)-543.904300463)<1e-8
assert abs(log(detG)-530.285191202)<1e-8
print('PASS Phase205 same-source arithmetic/analytic exact controls',flush=True)
