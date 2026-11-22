#!/usr/bin/env python3
"""Exact source-jet p^(m+1) transport and full-Q residue histogram controls."""
from math import comb,isqrt
from source_jet_histogram import (
    exact_ellipse_histogram,ellipse_points,count_y_slices,positive_ellipse_radius,
    production_row_jet,mod_gram_from_hist,mod_gram_direct,rank_mod)
from direct_integer_oracle import ordinary_jet,normal_jet

D_PROD=322**4+15

def prime_trial(n):
    if n<2:return False
    if n%2==0:return n==2
    return all(n%d for d in range(3,isqrt(n)+1,2))

def test_small():
    D=43;p=3;S=3;R=7;J=3
    for a in ((0,0),(1,0),(-2,0),(2,1),(-3,-1),(0,3)):
        for r in range(R):
            for s in range(S):
                for m in (1,2):
                    got=production_row_jet(D,p,r,s,S,J,a,m)
                    assert all(got[j]==tuple(n%p**m for n in normal_jet(D,p,S,r,s,j,a))
                               for j in range(J))
                for dx,dy in ((9,0),(0,9),(-9,9)):
                    b=(a[0]+dx,a[1]+dy)
                    assert production_row_jet(D,p,r,s,S,J,a)==production_row_jet(D,p,r,s,S,J,b)
                for dx,dy in ((27,0),(0,27)):
                    b=(a[0]+dx,a[1]+dy)
                    assert production_row_jet(D,p,r,s,S,J,a,2)==production_row_jet(D,p,r,s,S,J,b,2)

    # Different source arithmetic implementations, j>=p included.
    for a in ((0,0),(1,1),(-2,1),(3,0)):
        for r in range(16):
            for s in range(6):
                k=min(r//p,5-s)
                got=production_row_jet(D,p,r,s,6,6,a,2)
                for j in range(6):
                    raw=[0,0]
                    for t in range(k+1):
                        v=ordinary_jet(D,r-p*t,s+t,j,a)
                        for c in (0,1):raw[c]+=(-1)**t*comb(k,t)*v[c]
                    assert all(x%p**k==0 for x in raw)
                    assert got[j]==tuple(x//p**k%9 for x in raw)

    # A non-inert source cannot silently inherit this factorization.
    rejected=False
    try:production_row_jet(19,5,5,0,2,2,(0,1),1)
    except AssertionError:rejected=True
    assert rejected
    assert [normal_jet(43,3,3,3,0,0,(x,0))[0]%3
            for x in (0,3,6)]==[0,2,1]

    rows=[(r,s) for r in range(R) for s in range(S)]
    for rho,expected in ((8,8),(9,21),(10,20),(12,21)):
        Q=list(ellipse_points(D,rho))
        for m in (1,2):
            hist=exact_ellipse_histogram(D,rho,p**(m+1))
            h1=mod_gram_from_hist(D,p,S,rows,J,hist,m)
            h2=mod_gram_direct(D,p,S,rows,J,Q,m)
            assert h1==h2
            if m==1:assert rank_mod(h1,p)==expected
    print('PASS: independent original source jets, higher derivatives, split kill, four exact small histogram Grams')

def test_production():
    D=D_PROD;p=3
    assert D==10750371871 and D%4==3 and D%3==1 and prime_trial(D)
    R=D//4;S=R//25;rho=positive_ellipse_radius(D)
    K=min((R-1)//p,S-1)
    assert rho==14689950 and S==107503718 and K==107503717
    assert 3**16>2*rho
    N=count_y_slices(D,rho)
    assert N==6538432431
    hist9=exact_ellipse_histogram(D,rho,9)
    hist27=exact_ellipse_histogram(D,rho,27)
    assert len(hist9)==81 and sum(hist9.values())==N
    assert len(hist27)==729 and sum(hist27.values())==N
    assert all(n==hist9[(-x%9,-y%9)] for (x,y),n in hist9.items())
    assert all(n==hist27[(-x%27,-y%27)] for (x,y),n in hist27.items())
    assert hist9[(0,0)]==sum(n for (x,y),n in hist27.items()
                             if x%9==0 and y%9==0)
    active=sum(n%3!=0 for n in hist9.values())
    assert active==59

    # Only five source-compatible rows and Jprobe=4, NOT the full Gram.
    rows=[(3,0),(6,0),(12,0),(3*S,0),(3*S,2)]
    assert all(r<R and s<S for r,s in rows)
    assert min((3*S)//p,S-1)==S-1
    for a in ((2,1),(5,4),(0,0),(8,8)):
        for r,s in rows:
            value=production_row_jet(D,p,r,s,S,4,a)
            for dx,dy in ((9,0),(0,9),(9,-9)):
                b=(a[0]+dx,a[1]+dy)
                assert production_row_jet(D,p,r,s,S,4,b)==value
    matrix=mod_gram_from_hist(D,p,S,rows,4,hist9,1)
    assert rank_mod(matrix,p)==4
    assert matrix==[[2,0,0,0,0],[0,2,0,2,2],[0,0,0,0,1],
                    [0,2,0,2,0],[0,2,1,0,0]]
    n=R*S;J=S
    bound=2*J*p**4
    active_bound=2*J*active
    assert (n,bound,n-bound)==(288926236423151306,17415602316,288926219007548990)
    assert (active_bound,n-active_bound)==(12685438724,288926223737712582)
    print('PASS: actual production Q',N,'points ->',len(hist9),
          'classes (active',active,'); no full determinant allocated')
    print('PAPER COROLLARY: full normalized Gram rank <=',active_bound,
          'and, if det nonzero, residual v3 >=',n-active_bound)

if __name__=='__main__':
    test_small()
    test_production()
