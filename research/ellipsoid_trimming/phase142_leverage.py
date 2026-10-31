#!/usr/bin/env python3
"""Phase142: exact leverage determinants and the original 8-node jet witness.

Only standard-library exact Python integers/Fraction. Original D=19,
R=8,S=J=4, same pointwise ordinary Z jets, same factor-two trace form.
The 21-node ellipse remains the baseline. We compare two antipodal-pair
deletions by Sylvester's determinant identity and independently verify a
full-rank 8-REAL-node support, outside the usual sufficient count guard.
None of this constitutes a production interpolating theorem or a new
number-field discriminant bound.

Run: python3 research/ellipsoid_trimming/phase142_leverage.py
"""
from __future__ import annotations
from fractions import Fraction as F
from math import log
from phase140_exact_trim import (D,R,S,J,DIM,ORIGINAL,jets,one_node_gram,
    determinant,ln,add_matrix,falling)

def det_general(matrix):
    """Fraction-free Bareiss of an arbitrary square integer matrix."""
    a=[row[:] for row in matrix]
    n=len(a)
    if n==0:return 1
    sign,prev=1,1
    for k in range(n-1):
        if a[k][k]==0:
            h=next((i for i in range(k+1,n) if a[i][k]!=0),None)
            if h is None:return 0
            a[k],a[h]=a[h],a[k]
            sign=-sign
        p=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                v=a[i][j]*p-a[i][k]*a[k][j]
                assert v%prev==0
                a[i][j]=v//prev
            a[i][k]=0
        prev=p
    return sign*a[-1][-1]

def det_fraction(matrix):
    a=[row[:] for row in matrix]
    n=len(a)
    out=F(1)
    for k in range(n):
        p=next((i for i in range(k,n) if a[i][k]),None)
        if p is None:return F(0)
        if p!=k:
            a[k],a[p]=a[p],a[k]
            out=-out
        t=a[k][k]
        out*=t
        for i in range(k+1,n):
            if a[i][k]==0:continue
            z=a[i][k]/t
            for j in range(k+1,n):
                a[i][j]-=z*a[k][j]
            a[i][k]=F(0)
    return out

def invert_fraction(matrix):
    n=len(matrix)
    a=[[F(z) for z in row]+[F(i==j) for j in range(n)]
       for i,row in enumerate(matrix)]
    for k in range(n):
        p=next((i for i in range(k,n) if a[i][k]),None)
        assert p is not None,"baseline original Gram must be invertible"
        a[k],a[p]=a[p],a[k]
        v=a[k][k]
        a[k]=[z/v for z in a[k]]
        for i in range(n):
            if i==k:continue
            t=a[i][k]
            if t:
                a[i]=[x-t*y for x,y in zip(a[i],a[k])]
    inv=[row[n:] for row in a]
    for i in range(n):
        for j in range(n):
            assert sum(matrix[i][h]*inv[h][j] for h in range(n))==int(i==j)
    return inv

def sum_gram(nodes):
    out=[[0]*DIM for _ in range(DIM)]
    for q in nodes:
        b=one_node_gram(q)
        for i in range(DIM):
            for j in range(DIM):
                out[i][j]+=b[i][j]
    return out

def square_real_jet_matrix(xs):
    # Rows (r,s), columns (node, derivative j), NOT the imaginary columns
    # because all y=0. This matrix is exactly R*S by R*J when |xs|=R.
    assert len(xs)==R and len(set(xs))==R and J==S
    return [[jets((x,0))[i][j][0] for x in xs for j in range(J)]
            for i in range(DIM)]

def vandermonde(xs):
    out=1
    for i in range(len(xs)):
        for j in range(i+1,len(xs)):
            out*=xs[j]-xs[i]
    return out

def block_columns(qs):
    cols=[]
    weights=[]
    for q in qs:
        j=jets(q)
        for h in range(J):
            cols.append([j[i][h][0] for i in range(DIM)])
            weights.append(2)
            cols.append([j[i][h][1] for i in range(DIM)])
            weights.append(2*D)
    C=[[cols[k][i] for k in range(len(cols))] for i in range(DIM)]
    return C,weights

def leverage_ratio(Ginv, qs):
    C,weights=block_columns(qs)
    d=len(weights)
    # B*C^T*G^{-1}*C may be nonsymmetric because B is diagonal.
    # Its determinant update is nevertheless exact over Q.
    A=[[sum(Ginv[i][j]*C[j][k] for j in range(DIM))
        for k in range(d)] for i in range(DIM)]
    K=[[weights[a]*sum(C[i][a]*A[i][b] for i in range(DIM))
        for b in range(d)] for a in range(d)]
    L=[[(F(int(a==b))-K[a][b]) for b in range(d)] for a in range(d)]
    return det_fraction(L)

def _vand(xs):
    v=1
    for i in range(len(xs)):
        for j in range(i+1,len(xs)):
            v*=xs[j]-xs[i]
    return v

def verify_diagonal_vandermonde_family():
    """Finite falsification sweep of a general polynomial factorization target.

    The factor Vandermonde(xs)^S is forced by column collisions and
    total homogeneity; its constant being NONZERO when S<=R remains
    a separate general proof obligation, not inferred from the sweep.
    """
    def eval_matrix(rr,ss,xs):
        return [[0 if j>r else falling(r,j)*x**(r+s-j)
                 for x in xs for j in range(ss)]
                for r in range(rr) for s in range(ss)]
    def vand(xs):
        return _vand(xs)
    tested=0
    for rr in range(2,7):
        for ss in range(1,min(5,rr+1)+1):
            a=list(range(rr))
            b=[i*i+2*i-3 for i in range(rr)]
            da=det_general(eval_matrix(rr,ss,a))
            db=det_general(eval_matrix(rr,ss,b))
            va,vb=vand(a),vand(b)
            assert va and vb
            assert da%(va**ss)==0 and db%(vb**ss)==0
            ca,cb=da//(va**ss),db//(vb**ss)
            assert ca==cb
            assert (ca!=0)==(ss<=rr)
            tested+=1
    # The stronger guess Vandermonde^(S^2), as in 1-variable
    # confluent derivatives ALONG node position, is FALSE here:
    # ordinary derivatives are in Z with W held fixed.
    x=[0,1,2]
    d=det_general(eval_matrix(3,2,x))
    v=vand(x)
    assert d==8 and v==2 and d%(v**4)!=0
    assert tested>=20
    print(f"Finite diagonal-Vandermonde sweep: {tested} (R,S) regimes, "
          "two independent node placements each; no failures.")

def main():
    G=sum_gram(ORIGINAL)
    full=determinant(G)
    assert full>0 and full%3**38==0
    assert len(ORIGINAL)==21
    # A single full-Gram inverse can support MANY 2J/4J-sized
    # block leverage evaluations. This remains computationally
    # expensive in n for production without structural shortcuts.
    inv=invert_fraction(G)
    for q in [(5,0),(1,0)]:
        pair=[q,(-q[0],-q[1])]
        new=add_matrix(add_matrix(G,one_node_gram(pair[0]),-1),
                       one_node_gram(pair[1]),-1)
        newdet=determinant(new)
        assert newdet>0 and newdet%3**38==0
        exact=F(newdet,full)
        small=leverage_ratio(inv,pair)
        assert small==exact
        assert F(0)<small<F(1)
        print(f"removed antipodal {q}: 16x16 leverage ratio equals "
              f"32x32 determinant ratio exactly; log saving={-log(float(small)):.9f}")

    xs1=[-4,-3,-2,-1,1,2,3,4] # centrally symmetric, norm radius 4
    xs2=[-4,-3,-2,-1,0,1,2,3] # nonsymmetric, same number of real nodes
    constants=[]
    for xs in [xs1,xs2]:
        E=square_real_jet_matrix(xs)
        dE=det_general(E)
        V=vandermonde(xs)
        assert V!=0 and dE!=0 and dE%(V**S)==0
        constants.append(dE//(V**S))
        G8=sum_gram([(x,0) for x in xs])
        det8=determinant(G8)
        # On the real axis, the 2*D imaginary metric columns are zero,
        # and the exact 32x32 Gram is 2*E*E^T.
        assert det8==2**DIM*dE*dE and det8>0
        assert det8%3**38==0
        print(f"8 real nodes {xs}: rank32, det positive, "
              f"log determinant={ln(det8):.9f}; "
              f"interpolation guard 17<8 is FALSE.")
    assert constants[0]==constants[1],"finite test of a conjectural universal confluent-Vandermonde factor"
    assert constants[0]!=0
    xs7=[-3,-2,-1,0,1,2,3]
    assert len(xs7)*J<DIM
    assert determinant(sum_gram([(x,0) for x in xs7]))==0
    print(f"7 real nodes: only 28 nonzero real jet columns < 32 rows; det=0.")
    print("The original 2R+S point-count guard is sufficient, not necessary.")
    verify_diagonal_vandermonde_family()
    print("No uniform smaller-radius or complexity-theoretic claim established.")

if __name__=="__main__":
    main()
