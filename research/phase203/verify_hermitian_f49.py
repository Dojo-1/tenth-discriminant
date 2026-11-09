#!/usr/bin/env python3
"""Phase203-B: exact F49-Hermitian refinement of the source row space.

Preregistered in Issue #134. The same operator C works on all 49 INDIVIDUAL
F7^2 residue points (not just 25 symmetric orbits). Its F49-module action is
on the row space, not the split INTEGRAL ORDER Z[sqrt(-D)] mod 7 = F7 x F7.
No integer square determinant or improved field-discriminant bound is claimed.
"""
from collections import Counter
from random import Random
from check_intertwiner_f7 import (
    D, P, EVEN, ODD, U_at, gram_split, matmul, trans, det_mod
)

assert P == 7 and D % P == 5
N=28
IDX=EVEN+ODD


def eye(n): return [[int(i==j) for j in range(n)] for i in range(n)]
def neg(A): return [[-v%P for v in row] for row in A]
def reorder(G): return [[G[i][j] for j in IDX] for i in IDX]


def inverse(A):
    n=len(A)
    A=[list(row)+[int(i==j) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if A[i][j]%P),None)
        assert pivot is not None
        A[j],A[pivot]=A[pivot],A[j]
        v=pow(A[j][j],-1,P)
        A[j]=[x*v%P for x in A[j]]
        for i in range(n):
            if i!=j and A[i][j]:
                c=A[i][j]
                A[i]=[(x-c*y)%P for x,y in zip(A[i],A[j])]
    assert all(A[i][j]==int(i==j) for i in range(n) for j in range(n))
    return [row[n:] for row in A]


def build():
    U=U_at(P)
    assert det_mod(U,P)==1
    Ui=inverse(U)
    Parity=[[0]*N for _ in range(N)]
    Switch=[[0]*N for _ in range(N)]
    for i in range(N):
        Parity[i][i]=1 if i<14 else P-1
    for i in range(14):
        for j in range(14):
            Switch[i][14+j]=U[i][j]
            Switch[14+i][j]=Ui[i][j]
    C=matmul(Parity,Switch,P)
    I=eye(N)
    assert matmul(Parity,Parity,P)==I
    assert matmul(Switch,Switch,P)==I
    assert matmul(Parity,Switch,P)==neg(matmul(Switch,Parity,P))
    assert matmul(C,C,P)==neg(I)
    return Parity,Switch,C


# F49 as pairs (a,b) encoded by a+7*b, with i^2=-1.
def add(a,b): return ((a%7+b%7)%7)+7*((a//7+b//7)%7)
def sub(a,b): return ((a%7-b%7)%7)+7*((a//7-b//7)%7)
def mul(a,b):
    a0,a1=a%7,a//7
    b0,b1=b%7,b//7
    return ((a0*b0-a1*b1)%7)+7*((a0*b1+a1*b0)%7)
def inv(a):
    assert a!=0
    x,y=a%7,a//7
    q=pow((x*x+y*y)%7,-1,7)
    return (x*q%7)+7*((-y*q)%7)


def rank(A,field):
    A=[list(row) for row in A]
    n=len(A);m=len(A[0]);r=0
    for j in range(m):
        pivot=next((i for i in range(r,n) if A[i][j]),None)
        if pivot is None: continue
        A[r],A[pivot]=A[pivot],A[r]
        v=(pow(A[r][j],-1,P) if field==7 else inv(A[r][j]))
        for t in range(j,m):
            A[r][t]=(A[r][t]*v%P if field==7 else mul(A[r][t],v))
        for i in range(r+1,n):
            c=A[i][j]
            if c:
                for t in range(j,m):
                    A[i][t]=((A[i][t]-c*A[r][t])%P if field==7
                             else sub(A[i][t],mul(c,A[r][t])))
        r+=1
    return r


def hermitian_rank(B,C):
    # Skew-adjoint complex structure C: C^T B = -B C.
    BC=matmul(B,C,P)
    assert matmul(trans(C),B,P)==neg(BC)
    assert matmul(trans(C),BC,P)==B
    assert matmul(BC,C,P)==neg(B)
    assert all(B[i][j]==B[j][i] and BC[i][j]==-BC[j][i]%P
               for i in range(N) for j in range(N))
    # h(x,y)=B(x,y)+i*B(x,Cy). Hermitian over F49.
    H=[[B[i][j]+7*BC[i][j] for j in range(N)] for i in range(N)]
    r7=rank(B,7);r49=rank(H,49)
    assert r7==2*r49
    return r7,r49


def main():
    Parity,Switch,C=build()
    per_point={}
    for y in range(P):
        for x in range(P):
            B=reorder(gram_split([(x,y)],P,3))
            hermitian_rank(B,C)
            per_point[(x,y)]=B
    pairs=Counter(hermitian_rank(B,C) for B in per_point.values())
    assert pairs==Counter({(2,1):7,(4,2):42})
    print("POINTWISE_HERMITIAN",{"characteristic":7,"points":49,
          "rank_pairs":dict(pairs),"C_squared":"-I",
          "Hermitian_linear_first_antilinear_second":True})
    # P and J separately are NOT universally isometric for a single
    # asymmetric point; C unexpectedly remains an isometry.
    one=per_point[(1,0)]
    assert matmul(trans(Parity),matmul(one,Parity,P),P)!=one
    assert matmul(trans(Switch),matmul(one,Switch,P),P)!=one
    assert matmul(trans(C),matmul(one,C,P),P)==one

    rng=Random(1)
    det_hist=Counter();rank_hist=Counter()
    for _ in range(30):
        weights={z:rng.randrange(P) for z in sorted(per_point)}
        G=[[sum(w*per_point[z][i][j] for z,w in weights.items())%P
            for j in range(N)] for i in range(N)]
        r7,r49=hermitian_rank(G,C)
        d=det_mod(G,P)
        assert d in (0,1,2,4),("nonsquare determinant",d)
        det_hist[d]+=1
        rank_hist[r7]+=1
    assert det_hist==Counter({2:9,4:13,1:4,0:4})
    assert rank_hist==Counter({28:26,26:4})
    print("ASYMMETRIC_CONTROLS",{"seed":1,"trials":30,
        "nonzero_determinants":26,"determinant_classes":dict(det_hist),
        "rank_F7":dict(rank_hist),"all_nonzero_dets_square_in_F7":True,
        "every_rank_even":True,"asymmetric_parity_symmetry_broken":True})
    print("PASS: fixed-place F49 Hermitian row-module refinement")


if __name__=="__main__":
    main()
