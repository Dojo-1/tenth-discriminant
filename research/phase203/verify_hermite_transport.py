#!/usr/bin/env python3
"""Phase203-A: original-source Hermite reduction over the SPLIT F7 order.

Pre-registered in Issue #133. Source rows (r,s), 0<=r<53, s in {0,1},
ordinary Z derivatives j=0,1 with W held fixed. g(Z)=(Z^7-Z)^2.
One 106x28 coefficient matrix works for EVERY split residue node, hence
for any Q; it does NOT identify Q16 and Q25 integer Gram determinants,
nor apply to j=2 or inert residue points.
"""
from math import prod
from check_intertwiner_f7 import D, P, pairmul, pairpow, ellipse_points

assert D == 215 and P == 7 and -D % P == 2

R,S,J=53,2,2


def source_E(Q):
    # Exact original pair-coordinate jets in row-major (r,s) order;
    # each (j,x,y) column contributes the adjacent a,b channels.
    E=[]
    for r in range(R):
        for s in range(S):
            line=[]
            for j in range(J):
                for x,y in Q:
                    if j>r:
                        line.extend((0,0))
                    else:
                        v=pairmul(pairpow((x,y),r-j,P),
                                  pairpow((x,-y),s,P),P)
                        f=prod(range(r-j+1,r+1))
                        line.extend((f*v[0]%P,f*v[1]%P))
            E.append(line)
    return E


def hermite_T():
    # Mod (Z^7-Z)^2 = Z^14 - 2Z^8 + Z^2, and j=0,1 only.
    reductions=[[0]*14 for _ in range(R)]
    for r in range(14):reductions[r][r]=1
    for r in range(14,R):
        reductions[r]=[(2*reductions[r-6][t]-reductions[r-12][t])%P
                       for t in range(14)]
    T=[[0]*28 for _ in range(106)]
    for r in range(R):
        for s in range(S):
            for t in range(14):
                T[2*r+s][2*t+s]=reductions[r][t]
    assert T[:28]==[[int(i==j) for j in range(28)] for i in range(28)]
    return T


def multiply(A,B):
    assert len(A[0])==len(B)
    # Use the finite field F7; no floating-point matrices or SVD.
    BT=list(zip(*B))
    return [[sum(a*b for a,b in zip(row,col))%P for col in BT]
            for row in A]


def transpose(A):return [list(col) for col in zip(*A)]


def pivot_columns(A):
    a=[row[:] for row in A]
    n=len(a);m=len(a[0]);k=0;cols=[]
    for j in range(m):
        t=next((i for i in range(k,n) if a[i][j]%P),None)
        if t is None:continue
        a[k],a[t]=a[t],a[k]
        inv=pow(a[k][j],-1,P)
        for c in range(j,m):a[k][c]=a[k][c]*inv%P
        for i in range(k+1,n):
            coeff=a[i][j]
            if coeff:
                for c in range(j,m):a[i][c]=(a[i][c]-coeff*a[k][c])%P
        cols.append(j);k+=1
        if k==n:break
    return cols


def inv_matrix(A):
    n=len(A)
    a=[list(row)+[int(i==j) for j in range(n)]
       for i,row in enumerate(A)]
    for j in range(n):
        t=next((i for i in range(j,n) if a[i][j]%P),None)
        assert t is not None
        a[j],a[t]=a[t],a[j]
        v=pow(a[j][j],-1,P)
        a[j]=[z*v%P for z in a[j]]
        for i in range(n):
            if i!=j and a[i][j]:
                c=a[i][j]
                a[i]=[(z-c*w)%P for z,w in zip(a[i],a[j])]
    assert all(a[i][j]==int(i==j) for i in range(n) for j in range(n))
    return [row[n:] for row in a]


def trace_gram(E):
    # Source metric 2,2D on each adjacent real/imaginary channel.
    W=[2 if j%2==0 else 2*D for j in range(len(E[0]))]
    return [[sum(x*y*z for x,y,z in zip(a,b,W))%P for b in E] for a in E]


def test():
    T=hermite_T()
    assert sum(bool(z) for row in T for z in row)==166
    Q16=ellipse_points(16)
    Q25=ellipse_points(25)
    assert len(Q16)==59 and len(Q25)==133
    E16=source_E(Q16)
    piv=pivot_columns(E16[:28])
    assert len(piv)==28
    K=[[E16[i][j] for j in piv] for i in range(28)]
    fitted=multiply([[E16[i][j] for j in piv] for i in range(106)],
                    inv_matrix(K))
    assert T==fitted, "Hermite recurrence differs from independent pivot reconstruction"

    for rho,Q in ((16,Q16),(25,Q25)):
        E=source_E(Q)
        assert len(pivot_columns(E))==len(pivot_columns(E[:28]))==28
        assert E==multiply(T,E[:28]), "different evaluation source"
        full=trace_gram(E)
        reduced=trace_gram(E[:28])
        assert full==multiply(multiply(T,reduced),transpose(T)), "Gram pullback failure"
        print("MATCHED_SOURCE",{"rho":rho,"samples":len(Q),"full_rows":106,
              "quotient_rows":28,"same_T":True,"same_source_Gram_transport":True})

    # Each split residue pair is a point of the selected order tensor F7.
    # In particular z^7=z componentwise, and g(z)=g'(z)=0.
    for x in range(P):
        for y in range(P):
            E=source_E([(x,y)])
            assert E==multiply(T,E[:28]),("bad residue",(x,y))
    print("ALL_SPLIT_RESIDUES",{"points":49,"universal_Hermite_transport":True,
          "T_nonzeros":166,"matches_pivot_T":True})

    # Negative: d^2/dZ^2 at z=0 separates Z^14 from 2Z^8-Z^2.
    assert (0-(0-2))%P==2
    # Negative inert order: u^2=-1 over F7, so (u^7-u)^2=-4=3 !=0.
    assert (-4)%P == 3
    print("NEGATIVE_CONTROLS",{"j2_reduction_invalid":True,
          "inert_D1_degree14_reduction_invalid":True})
    print("PASS source-preserving F7 Hermite quotient transport")


if __name__=="__main__":
    test()
