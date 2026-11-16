#!/usr/bin/env python3
"""Phase330 — parity-constrained integral weave/deweave of conjugate charts.

Instead of dividing by 2, use the non-unimodular *integral* map
    W(x,y)=(x+y,x-y).
Its image is the parity sublattice Lambda={(u,v):u=v mod 2}.
W:Z^(2N)->Lambda is an integral lattice isomorphism.
The ambient index is 2^N, so it must NOT be treated as a
unimodular map Z^(2N)->Z^(2N).

The swap acts in woven coordinates as (u,v)->(u,-v),
and the original bilinear B+B descends to
    (u^T B u' + v^T B v')/2,
which is integral **on Lambda**, not necessarily on the ambient
Z^(2N). All determinant index factors are retained.

For the Phase328 four-copy Q8 carrier we apply W on the (0,1)
and (2,3) chart pairs. Every Q8 signed-permutation frame has an
exact *integral* conjugate in woven coordinates; it preserves
the parity sublattice. This is a positive external intertwiner
but NOT an integral descent to a single original Z-jet chart,
not an H_D action and not a new 2-adic determinant factor.
"""
from __future__ import annotations
from fractions import Fraction
from pathlib import Path
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"phase328"))
from stabilized_return import (  # noqa: E402
    Q8, quaternion_left_frame, determinant, matrix_mul, transpose, block_diag,
    identity,
)


def weave_pair(x:tuple[int,...],y:tuple[int,...])->tuple[tuple[int,...],tuple[int,...]]:
    if len(x)!=len(y):
        raise ValueError("paired charts need equal abstract rank")
    return (tuple(a+b for a,b in zip(x,y)),
            tuple(a-b for a,b in zip(x,y)))


def parity_compatible(u:tuple[int,...],v:tuple[int,...])->bool:
    if len(u)!=len(v):
        return False
    return all((a-b)%2==0 for a,b in zip(u,v))


def deweave_pair(u:tuple[int,...],v:tuple[int,...]
                 )->tuple[tuple[int,...],tuple[int,...]]:
    if not parity_compatible(u,v):
        raise ValueError("ambient woven pair violates integral parity gluing")
    return (tuple((a+b)//2 for a,b in zip(u,v)),
            tuple((a-b)//2 for a,b in zip(u,v)))


def swap_woven_pair(u:tuple[int,...],v:tuple[int,...]
                    )->tuple[tuple[int,...],tuple[int,...]]:
    return (u,tuple(-b for b in v))


def exact_woven_matrix(n:int):
    """Explicit W=[[I,I],[I,-I]] without branch ambiguity."""
    if n<1:raise ValueError("n>=1")
    return tuple(tuple(
        (int(i%n==j%n) if i<n or j<n else
         -int(i%n==j%n))
        for j in range(2*n))
        for i in range(2*n))


def four_copy_weave(n:int):
    return block_diag(exact_woven_matrix(n),exact_woven_matrix(n))


def rational_mm(A, B):
    if not A or not B or len(A[0])!=len(B):
        raise ValueError("Matrix mismatch")
    return tuple(tuple(
        sum(Fraction(A[i][k])*Fraction(B[k][j]) for k in range(len(B)))
        for j in range(len(B[0])))
        for i in range(len(A)))


def woven_quaternion_action(u:tuple[int,int,int,int],n:int):
    """Integer conjugate of Q8 action despite nonunimodular W."""
    W=four_copy_weave(n)
    Winv=tuple(tuple(Fraction(x,2) for x in row) for row in W)
    U=quaternion_left_frame(u,n)
    tmp=rational_mm(rational_mm(W,U),Winv)
    assert all(x.denominator==1 for row in tmp for x in row)
    Uprime=tuple(tuple(int(x) for x in row) for row in tmp)
    assert matrix_mul(Uprime,W)==matrix_mul(W,U)
    assert determinant(Uprime)==determinant(U)==1
    assert matrix_mul(Uprime,transpose(Uprime))==identity(4*n)
    return Uprime


def bilinear(B, x:tuple[int,...], y:tuple[int,...])->int:
    n=len(B)
    if n!=len(x) or n!=len(y) or any(len(row)!=n for row in B):
        raise ValueError("Source Gram shapes differ")
    return sum(x[i]*B[i][j]*y[j]
               for i in range(n) for j in range(n))


def woven_bilinear(B, u:tuple[int,...],v:tuple[int,...],
                   up:tuple[int,...],vp:tuple[int,...])->int:
    """(u^T B u' + v^T B v')/2 on parity-compatible lattice."""
    if not parity_compatible(u,v) or not parity_compatible(up,vp):
        raise ValueError("Must restrict to the actual integral woven lattice")
    num=bilinear(B,u,up)+bilinear(B,v,vp)
    assert num%2==0
    return num//2


def verify_weave(n:int):
    W=exact_woven_matrix(n)
    assert matrix_mul(W,W)==tuple(
        tuple(2 if i==j else 0 for j in range(2*n))
        for i in range(2*n))
    assert determinant(W)==(-2)**n
    W4=four_copy_weave(n)
    assert determinant(W4)==4**n
    from chart_descent import swap
    S=swap(n)
    signed=block_diag(identity(n),
        tuple(tuple(-int(i==j) for j in range(n)) for i in range(n)))
    assert matrix_mul(W,S)==matrix_mul(signed,W)
    for u in Q8:
        woven_quaternion_action(u,n)
    return {"rank":n, "paired_index":2**n,
            "four_copy_index":4**n,
            "q8_compatible":True,
            "inverse_requires_parity":True}


if __name__=="__main__":
    import json
    print("PHASE330_PARITY_WEAVE",
          json.dumps([verify_weave(n) for n in (1,2,3)],sort_keys=True))
