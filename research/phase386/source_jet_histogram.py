#!/usr/bin/env python3
"""Source-faithful normalized ordinary Z-jets and exact ellipse histograms.
No full production determinant is computed. Standard-library only.
"""
from math import comb, isqrt
from collections import defaultdict

def pair_mul(x,y,D,m):
    return ((x[0]*y[0]-D*x[1]*y[1])%m,
            (x[0]*y[1]+x[1]*y[0])%m)

def pair_add(x,y,m):
    return ((x[0]+y[0])%m,(x[1]+y[1])%m)

def pair_mul_scalar(x,a,m):
    return (x[0]*a%m,x[1]*a%m)

def pair_pow(x,n,D,m):
    assert n>=0
    a=(1,0);x=(x[0]%m,x[1]%m)
    while n:
        if n&1:a=pair_mul(a,x,D,m)
        x=pair_mul(x,x,D,m);n//=2
    return a

def pair_pow_unbounded(x,n,D):
    assert n>=0
    a=(1,0)
    while n:
        if n&1:
            a=(a[0]*x[0]-D*a[1]*x[1],a[0]*x[1]+a[1]*x[0])
        x=(x[0]*x[0]-D*x[1]*x[1],2*x[0]*x[1])
        n//=2
    return a

def positive_ellipse_radius(D):
    """ceil((11/25)*D^(3/4)) using integer inequalities only."""
    assert D>0
    target=11**4*D**3
    hi=1
    while 25**4*hi**4<target:hi*=2
    lo=0
    while lo+1<hi:
        mid=(lo+hi)//2
        if 25**4*mid**4>=target:hi=mid
        else:lo=mid
    return hi

def count_y_slices(D,rho):
    lim=isqrt(rho*rho//D)
    return sum(2*isqrt(rho*rho-D*y*y)+1
               for y in range(-lim,lim+1))

def ellipse_points(D,rho):
    lim=isqrt(rho*rho//D)
    for y in range(-lim,lim+1):
        xlim=isqrt(rho*rho-D*y*y)
        for x in range(-xlim,xlim+1):
            yield x,y

def interval_count_in_residue(lo,hi,m,r):
    start=lo+(r-lo)%m
    return 0 if start>hi else 1+(hi-start)//m

def exact_ellipse_histogram(D,rho,m):
    """Counts source Q in residue classes without enumerating Q."""
    assert D>0 and rho>=0 and m>0
    H=defaultdict(int)
    lim=isqrt(rho*rho//D)
    for y in range(-lim,lim+1):
        xlim=isqrt(rho*rho-D*y*y)
        for xr in range(m):
            n=interval_count_in_residue(-xlim,xlim,m,xr)
            if n:H[(xr,y%m)]+=n
    return dict(H)

def jet_mul(A,B,D,m):
    """Binomial convolution for ORDINARY derivative jets."""
    J=len(A);assert J==len(B)
    out=[]
    for j in range(J):
        v=(0,0)
        for t in range(j+1):
            w=pair_mul(A[t],B[j-t],D,m)
            v=pair_add(v,pair_mul_scalar(w,comb(j,t),m),m)
        out.append(v)
    return out

def jet_pow(A,k,D,m):
    J=len(A)
    acc=[(1,0)]+[(0,0)]*(J-1)
    while k:
        if k&1:acc=jet_mul(acc,A,D,m)
        A=jet_mul(A,A,D,m);k//=2
    return acc

def normalized_source_jet(D,p,r,s,J,a,k,m=1):
    """Source U row derivative / p^k at sample a, reduced modulo p^m."""
    assert J>=1 and m>=1 and p>=2 and 0<=k<=r//p and s>=0
    M=p**m;d=r-p*k
    x,y=a
    z=x%M,y%M
    zbar=x%M,(-y)%M
    delta=pair_pow_unbounded((x,y),p,D)
    delta=delta[0]-x,delta[1]+y
    assert delta[0]%p==0 and delta[1]%p==0,(D,p,a)
    q=delta[0]//p%M,delta[1]//p%M
    h=[q]
    c=1
    for t in range(1,J):
        if t>p:h.append((0,0));continue
        if t>=2:c*=p-(t-1)
        h.append(pair_mul_scalar(pair_pow(z,p-t,D,M),c,M))
    power_jet=jet_pow(h,k,D,M)
    w_pow=pair_pow(zbar,s,D,M)
    g=[]
    fall=1
    for t in range(J):
        if t>d:g.append((0,0));continue
        if t>0:fall*=d-(t-1)
        g.append(pair_mul_scalar(
            pair_mul(pair_pow(z,d-t,D,M),w_pow,D,M),fall,M))
    return jet_mul(g,power_jet,D,M)

def production_row_jet(D,p,r,s,S,J,a,m=1):
    return normalized_source_jet(D,p,r,s,J,a,min(r//p,S-1-s),m)

def trace_pair(D,a,b,m):
    return (2*(a[0]*b[0]+D*a[1]*b[1]))%m

def mod_gram_from_hist(D,p,S,rows,J,hist,m=1):
    M=p**m;n=len(rows)
    H=[[0]*n for _ in range(n)]
    for a,count in hist.items():
        jets=[production_row_jet(D,p,r,s,S,J,a,m) for r,s in rows]
        for i in range(n):
            for j in range(i,n):
                v=sum(trace_pair(D,jets[i][t],jets[j][t],M) for t in range(J))%M
                H[i][j]=(H[i][j]+count*v)%M
    for i in range(n):
        for j in range(i):H[i][j]=H[j][i]
    return H

def mod_gram_direct(D,p,S,rows,J,Q,m=1):
    M=p**m;n=len(rows)
    H=[[0]*n for _ in range(n)]
    for a in Q:
        jets=[production_row_jet(D,p,r,s,S,J,a,m) for r,s in rows]
        for i in range(n):
            for j in range(i,n):
                v=sum(trace_pair(D,jets[i][t],jets[j][t],M) for t in range(J))%M
                H[i][j]=(H[i][j]+v)%M
    for i in range(n):
        for j in range(i):H[i][j]=H[j][i]
    return H

def rank_mod(M,p):
    if not M:return 0
    a=[[int(z)%p for z in row] for row in M]
    n=len(a);cols=len(a[0]);rank=0
    for j in range(cols):
        pivot=next((k for k in range(rank,n) if a[k][j]),None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank]
        inv=pow(a[rank][j],-1,p)
        a[rank]=[(z*inv)%p for z in a[rank]]
        for k in range(n):
            if k!=rank and a[k][j]:
                f=a[k][j]
                a[k]=[(x-f*y)%p for x,y in zip(a[k],a[rank])]
        rank+=1
        if rank==n:break
    return rank
