#!/usr/bin/env python3
"""Phase202 preregistered exact tests. Protocol: GitHub Issue #130.

Original integer-pair ordinary-Z derivatives, W held fixed. Pairs (a,b)
represent a+b*sqrt(-D). Finite tests are not a field-cutoff proof, not a
full-ring-of-integers identification, and not a v0.7.0 minor substitution.
Only Python standard library is required.
"""
from itertools import combinations
from math import gcd, prod


def points(D, rho):
    return [(x, y) for y in range(-rho, rho + 1)
            for x in range(-rho, rho + 1) if x*x + D*y*y <= rho*rho]


def mul(u, v, D, p):
    a,b=u; c,d=v
    return ((a*c-D*b*d) % p, (a*d+b*c) % p)


def power(u, n, D, p):
    z=(1,0)
    for _ in range(n):
        z=mul(z,u,D,p)
    return z


def jets(D, R, S, J, rho, p):
    Q=points(D,rho)
    rows=[(r,s) for r in range(R) for s in range(S)]
    cols=[(j,x,y) for j in range(J) for x,y in Q]
    A=[]
    for r,s in rows:
        line=[]
        for j,x,y in cols:
            if j>r:
                line.append((0,0))
            else:
                z=mul(power((x%p,y%p),r-j,D,p),
                      power((x%p,-y%p),s,D,p),D,p)
                f=prod(range(r-j+1,r+1))
                line.append((z[0]*f%p,z[1]*f%p))
        A.append(line)
    return Q,rows,cols,A


def channels(A):
    return [[c for a,b in row for c in (a,b)] for row in A]


def trace_gram(A,D,p):
    return [[2*sum(a*c+D*b*d for (a,b),(c,d) in zip(u,v))%p
             for v in A] for u in A]


def rank_p(M,p):
    if not M:return 0
    a=[list(row) for row in M]
    n=len(a); m=len(a[0]); k=0
    for j in range(m):
        h=next((i for i in range(k,n) if a[i][j]%p),None)
        if h is None:continue
        a[h],a[k]=a[k],a[h]
        inverse=pow(a[k][j],-1,p)
        for t in range(j,m):a[k][t]=a[k][t]*inverse%p
        for i in range(k+1,n):
            v=a[i][j]%p
            if v:
                for t in range(j,m):a[i][t]=(a[i][t]-v*a[k][t])%p
        k+=1
        if k==n:break
    return k


def inverse_pair(z,D,p):
    a,b=z
    den=(a*a+D*b*b)%p
    if not den:raise ZeroDivisionError("requires inert p")
    inv=pow(den,-1,p)
    return (a*inv%p,-b*inv%p)


def rank_p2(A,D,p):
    # Irreducible X^2+D: the pair arithmetic is a FIELD only in this case.
    assert p>2 and pow((-D)%p,(p-1)//2,p)==p-1
    a=[list(row) for row in A]
    n=len(a);m=len(a[0]);k=0
    for j in range(m):
        h=next((i for i in range(k,n) if a[i][j]!=(0,0)),None)
        if h is None:continue
        a[h],a[k]=a[k],a[h]
        inv=inverse_pair(a[k][j],D,p)
        for t in range(j,m):a[k][t]=mul(a[k][t],inv,D,p)
        for i in range(k+1,n):
            z=a[i][j]
            if z!=(0,0):
                for t in range(j,m):
                    v=mul(z,a[k][t],D,p)
                    a[i][t]=((a[i][t][0]-v[0])%p,
                             (a[i][t][1]-v[1])%p)
        k+=1
        if k==n:break
    return k


def determinant(M):
    a=[list(row) for row in M]
    n=len(a)
    if not n:return 1
    prev=1;sgn=1
    for j in range(n-1):
        if a[j][j]==0:
            h=next((k for k in range(j+1,n) if a[k][j]),None)
            if h is None:return 0
            a[j],a[h]=a[h],a[j];sgn=-sgn
        pivot=a[j][j]
        for i in range(j+1,n):
            for k in range(j+1,n):
                z=a[i][k]*pivot-a[i][j]*a[j][k]
                assert z%prev==0
                a[i][k]=z//prev
            a[i][j]=0
        prev=pivot
    return sgn*a[-1][-1]


def determinantal_divisors(M):
    # Small matrices only: gcd of all k-minors; Smith factors follow.
    n=len(M);m=len(M[0]);ds=[1]
    for k in range(1,min(n,m)+1):
        d=0
        for rr in combinations(range(n),k):
            for cc in combinations(range(m),k):
                d=gcd(d,determinant([[M[i][j] for j in cc] for i in rr]))
        ds.append(d)
    return ds,[ds[i]//ds[i-1] for i in range(1,len(ds))]


def track_A():
    D,R,S,J,rho,p=3,2,2,2,2,5
    Q,rows,cols,A=jets(D,R,S,J,rho,p)
    assert len(Q)==11 and len(cols)==22 and len(rows)==4
    exact=[[22,0,0,64],[0,64,-8,0],[0,-8,86,0],[64,0,0,296]]
    G=trace_gram(A,D,p)
    assert G==[[x%p for x in row] for row in exact]
    det=determinant(exact)
    assert det==13143040 and det%5==0
    assert rank_p2(A,D,p)==4 and rank_p(channels(A),p)==4
    assert rank_p(G,p)==3
    witness=[0,1,3,0]
    assert all(sum(x*y for x,y in zip(row,witness))%5==0 for row in G)
    assert all(x==0 for row in trace_gram(
        jets(D,R,S,J,rho,2)[3],D,2) for x in row)
    assert rank_p(trace_gram(jets(D,R,S,J,rho,3)[3],D,3),3)==4
    ds,smith=determinantal_divisors(exact)
    assert ds==[1,2,4,32,13143040] and smith==[2,2,8,410720]
    # One determinant does not determine the local rank or Smith profile.
    a=[[1,0],[0,25]];b=[[5,0],[0,5]]
    assert determinant(a)==determinant(b)==25
    assert rank_p(a,5)==1 and rank_p(b,5)==0
    print("TRACK A",{"D":D,"p":p,"rank_A_over_Fp2":4,
          "rank_E_over_Fp":4,"rank_G_over_Fp":3,"radical_dim":1,
          "char2_G_rank":0,"char3_G_rank":4,
          "determinantal_divisors":ds,"smith_factors":smith,
          "same_det_different_local_rank_control":True})


def track_B():
    D,R,S,J,rho,p=215,53,2,2,16,53
    Q,rows,cols,A=jets(D,R,S,J,rho,p)
    assert len(Q)==59 and len(rows)==106 and len(cols)==118
    assert p==R and J<=p and 2*rho<p
    assert len(set((x%p,y%p) for x,y in Q))==len(Q)
    assert pow((-D)%p,(p-1)//2,p)==p-1
    max_degree=(R-1)+p*(S-1)
    assert len(Q)*J>max_degree
    assert not (len(Q)>2*(R-1)+(S-1))
    rank_A=rank_p2(A,D,p)
    rank_E=rank_p(channels(A),p)
    rank_G=rank_p(trace_gram(A,D,p),p)
    assert (rank_A,rank_E,rank_G)==(106,106,106)
    print("TRACK B",{"D":D,"p":p,"R":R,"S":S,"J":J,"rho":rho,
         "sample_count":len(Q),"nJ":len(Q)*J,
         "polynomial_degree_bound":max_degree,
         "old_count_threshold":2*(R-1)+(S-1),
         "rank_A_Fp2":rank_A,"rank_E_Fp":rank_E,
         "rank_G_Fp":rank_G,"radical_dim":R*S-rank_G})
    # Adversarial p<R: Z^p-W belongs to the row rectangle and vanishes.
    D,R,S,J,rho,p=3,6,2,2,2,5
    _,rows,cols,A=jets(D,R,S,J,rho,p)
    ix=rows.index((p,0));iw=rows.index((0,1))
    assert all(A[ix][i]==A[iw][i] for i in range(len(cols)))
    rank_A=rank_p2(A,D,p)
    assert rank_A==11 and rank_A<len(rows)
    print("FROBENIUS_COLLISION",{"p":p,"R":R,"rank":rank_A,
                                   "row_relation":"Z^p-W"})


if __name__=="__main__":
    track_A()
    track_B()
    print("PASS preregistered Phase202 exact two-track controls")
