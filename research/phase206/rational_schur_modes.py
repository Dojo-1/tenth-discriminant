#!/usr/bin/env python3
"""Phase206-A exact generalized Schur eigenvalue inertia, prereg #142.

Thresholds were frozen at 1/2,1/4,1/8 before running. Counts, not
floating eigenvectors: signs of exact rational leading LDL minors.
"""
from fractions import Fraction as F
from source_probe import params,fibers,gram,det,inv,mm,tr

def det_fraction(A):
    A=[[F(x) for x in row] for row in A];n=len(A);v=F(1)
    for k in range(n):
        i=next((i for i in range(k,n) if A[i][k]),None)
        if i is None:return F(0)
        if i!=k:A[k],A[i]=A[i],A[k];v=-v
        q=A[k][k];v*=q
        for i in range(k+1,n):
            t=A[i][k]/q
            if t:
                for j in range(k+1,n):A[i][j]-=t*A[k][j]
                A[i][k]=0
    return v

def negative_inertia(A):
    prev=F(1);count=0
    for k in range(1,len(A)+1):
        d=det_fraction([row[:k] for row in A[:k]])
        assert d, "frozen-threshold leading minor degeneracy"
        if d/prev<0:count+=1
        prev=d
    return count

def run(D):
    rho,R,S,J,Q=params(D)
    ds=(R//4-1,R//2-1,R-S-7)
    t=(F(1,2),F(1,4),F(1,8));counts={str(x):0 for x in t}
    for d in ds:
        I=fibers(R,S,d);K=fibers(R,S,d+2)
        a=len(I);b=len(K);X=gram(D,Q,J,I+K)
        A=[row[:a] for row in X[:a]]
        B=[row[a:] for row in X[a:]]
        C=[row[a:] for row in X[:a]]
        Z=mm(mm(tr(C),inv(A)),C)
        residual=[[F(B[i][j])-Z[i][j] for j in range(b)] for i in range(b)]
        assert all(residual[i][j]==residual[j][i] for i in range(b) for j in range(b))
        assert all(det_fraction([row[:k] for row in residual[:k]])>0 for k in range(1,b+1))
        assert det_fraction(residual)/det(B)==F(det(X),det(A)*det(B))
        found={}
        for theta in t:
            P=[[residual[i][j]-theta*B[i][j] for j in range(b)] for i in range(b)]
            q=negative_inertia(P)
            counts[str(theta)]+=q;found[str(theta)]=q
        print('EXACT_INERTIA',{'D':D,'pair':(d,d+2),'dims':(a,b),
                              'Schur_residual_below':found},flush=True)
    print('THRESHOLD_COUNTS',D,counts,flush=True)
    assert counts==({ '1/2':0,'1/4':0,'1/8':0} if D==283
                   else {'1/2':5,'1/4':3,'1/8':2})

if __name__=='__main__':
    run(283);run(403)
    print('PASS exact Schur eigenvalue count for original source')
