#!/usr/bin/env python3
"""Phase329 — exact algebraic handle-slide / Gram knot resolution.

Use the actual Phase328 ordinary-Z integer trace Gram B as the
arithmetic source. Never replace its definition by the coupled form.

For n x n B and m x n integral coupling C let
  T_C = [[I_n, 0], [C, I_m]],
  Bhat = B direct_sum I_m,
  M_C  = T_C^T Bhat T_C
       = [[B+C^TC, C^T], [C, I_m]].
  iota_C = [[I_n],[-C]]
  pi_C   = [I_n,0].
Then det T_C=1, pi_C iota_C=I_n,
  iota_C^T M_C iota_C = B,
  det M_C = det B.

The analogy to a Kirby handle slide is algebraic only: without a
framed-link diagram this is NOT a topological Kirby equivalence.
All statements also hold with a unimodular auxiliary integral H,
but the implementation fixes H=I_m to avoid hidden assumptions.

A moving quaternionic U acts on the *same* rank 4n stabilized
lattice. The transport law for the coupled Gram is
  M_(u,C) = U M_C U^T
  iota_(u,C)=U iota_C
  pi_(u,C)=pi_C U^T,
with identical determinant and exact source return.
No extra prime factor can be promoted from these equivalences.
"""
from __future__ import annotations

from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"phase328"))

from stabilized_return import (  # noqa: E402
    Matrix, Q8, identity, transpose, matrix_mul, block_diag,
    determinant, quaternion_left_frame, original_integer_trace_gram,
    stabilized_gram,
)


def shear(C: Matrix) -> Matrix:
    """Unipotent integral matrix on N+M dimensions."""
    if not C:
        raise ValueError("Coupling must have at least one row")
    n=len(C[0])
    m=len(C)
    if n<1 or any(len(row)!=n for row in C):
        raise ValueError("C must be a nonempty rectangular matrix")
    dim=n+m
    return tuple(
        tuple((int(i==j) if i<n else
               C[i-n][j] if j<n else int(i-n==j-n))
              for j in range(dim))
        for i in range(dim)
    )


def shear_inverse(C: Matrix) -> Matrix:
    return shear(tuple(tuple(-v for v in row) for row in C))


def coupled_source_embedding(C: Matrix) -> Matrix:
    """Source split injection [I;-C], signed and integral."""
    n=len(C[0]);m=len(C)
    return tuple(
        tuple(int(i==j) if i<n else -C[i-n][j] for j in range(n))
        for i in range(n+m)
    )


def coupled_source_return(C: Matrix) -> Matrix:
    """Left inverse pi_C=[I,0]; does NOT project orthogonally for M_C."""
    n=len(C[0]);m=len(C)
    return tuple(
        tuple(int(i==j) for j in range(n+m))
        for i in range(n)
    )


def zero_block(m:int,n:int)->Matrix:
    return tuple((0,)*n for _ in range(m))


def coupled_gram(B: Matrix,C: Matrix)->Matrix:
    n=len(B)
    if n==0 or any(len(row)!=n for row in B):
        raise ValueError("B must be nonempty square")
    if len(C)==0 or any(len(row)!=n for row in C):
        raise ValueError("Coupling has wrong number of columns")
    T=shear(C)
    source=block_diag(B,identity(len(C)))
    return matrix_mul(matrix_mul(transpose(T),source),T)


def coupled_formula(B:Matrix,C:Matrix)->Matrix:
    """Independent explicit block-form evaluation (oracle)."""
    n=len(B);m=len(C)
    HC=C
    Ct=transpose(C)
    CtC=matrix_mul(Ct,C)
    return tuple(
        tuple(
            (B[i][j]+CtC[i][j] if i<n and j<n
             else Ct[i][j-n] if i<n
             else HC[i-n][j] if j<n
             else int(i-n==j-n))
            for j in range(n+m))
        for i in range(n+m)
    )


def frame_coupled_gram(B:Matrix,C:Matrix,u:tuple[int,int,int,int])->dict:
    n=len(B)
    if len(C)!=3*n:
        raise ValueError("Quaternion four-copy stabilization requires C of size 3N x N")
    base=coupled_gram(B,C)
    U=quaternion_left_frame(u,n)
    iota=coupled_source_embedding(C)
    pi=coupled_source_return(C)
    return {
        "moving":matrix_mul(matrix_mul(U,base),transpose(U)),
        "inclusion":matrix_mul(U,iota),
        "return":matrix_mul(pi,transpose(U)),
        "U":U,
        "base":base,
    }


def verify_coupled_return(B:Matrix,C:Matrix,u:tuple[int,int,int,int])->dict:
    n=len(B);m=len(C)
    T=shear(C)
    Tin=shear_inverse(C)
    A=coupled_gram(B,C)
    assert A==coupled_formula(B,C)
    assert matrix_mul(T,Tin)==identity(n+m)
    assert matrix_mul(Tin,T)==identity(n+m)
    assert determinant(T)==determinant(Tin)==1
    assert matrix_mul(coupled_source_return(C),coupled_source_embedding(C))==identity(n)
    assert matrix_mul(matrix_mul(transpose(coupled_source_embedding(C)),A),
                      coupled_source_embedding(C))==B
    assert determinant(A)==determinant(B)
    if m==3*n:
        f=frame_coupled_gram(B,C,u)
        assert matrix_mul(f["return"],f["inclusion"])==identity(n)
        assert matrix_mul(
            matrix_mul(transpose(f["inclusion"]),f["moving"]),
            f["inclusion"])==B
        assert determinant(f["moving"])==determinant(B)
    return {
        "n":n,"m":m,"source_det":determinant(B),
        "coupled_det":determinant(A),
        "shear_det":determinant(T),
        "exact_retraction":True,
    }


def source_dependent_coupling(B:Matrix)->Matrix:
    """Reproducible nonzero integral couplings derived from the source B.

    This changes no original jet nor source coefficient, but prevents
    testing a decorative zero-coupling case alone. It does not claim
    that the coupling has an arithmetic interpretation.
    """
    n=len(B)
    if n==0 or any(len(row)!=n for row in B):
        raise ValueError("B must be nonempty square")
    return tuple(
        tuple(((B[i%n][j]+(i//n+1)*(i%n+1)-2*j)%7)-3
              for j in range(n))
        for i in range(3*n)
    )


def vp(x:int,p:int)->int|None:
    """v_p for nonzero integer; None for the zero determinant."""
    if p<2:
        raise ValueError("prime must be >=2")
    if x==0:
        return None
    n=abs(x);v=0
    while n%p==0:
        n//=p;v+=1
    return v


if __name__=="__main__":
    import json
    Q=((0,0),(1,0),(0,1),(1,1),(-1,1),(2,1))
    B=original_integer_trace_gram(Q,7,2,2,2)
    C=source_dependent_coupling(B)
    print("PHASE329_INTEGRAL_UNKNOT_PASS",
          json.dumps(verify_coupled_return(B,C,(0,1,0,0)),sort_keys=True))
