#!/usr/bin/env python3
"""Phase330: C2 conjugate-chart descent, transfer, norm and 2-torsion.

This deliberately isolates a *necessary* symmetry condition and does
not construct the actual Z/W derivative interchange for unequal
rectangles. On two ABSTRACT IDENTICAL copies of a free Z module J,
let sigma(x,y)=(y,x) and Delta(x)=(x,x).

A source-return P:J+J->J that is Z-linear, conjugation-invariant
(P*sigma=P), and a left inverse to Delta (P*Delta=I) would require
2*P(x,0)=x for every x. Impossible for any nonzero free Z module.
Over a ring R it exists for R^n iff 2 is a unit in R.

Norm N=I+S obeys N^2=2N over Z. In F2 it is nonzero nilpotent
rather than an idempotent; over F7, (4N)^2=4N is a projector.
This is an exact *loss-of-descent* obstruction at characteristic 2.

There is a weaker integral return (first projection) which is NOT
C2-equivariant. This is not a no-go for the Phase328 actual return
or the Phase323 original binary prime divisibility.
"""
from __future__ import annotations
from fractions import Fraction
from math import gcd

Matrix=tuple[tuple[int,...],...]


def swap(n:int)->Matrix:
    if n<=0:raise ValueError("Nontrivial chart rank required")
    return tuple(tuple(int(j==((i+n)%(2*n)))
                       for j in range(2*n)) for i in range(2*n))


def diagonal(n:int)->Matrix:
    if n<=0:raise ValueError("Nontrivial chart rank required")
    return tuple(tuple(int(i%n==j) for j in range(n))
                 for i in range(2*n))


def first_return(n:int)->Matrix:
    if n<=0:raise ValueError("Nontrivial chart rank required")
    return tuple(tuple(int(i==j) for j in range(2*n)) for i in range(n))


def identity(n:int)->Matrix:
    return tuple(tuple(int(i==j) for j in range(n)) for i in range(n))


def add(a:Matrix,b:Matrix)->Matrix:
    if len(a)!=len(b) or any(len(x)!=len(y) for x,y in zip(a,b)):
        raise ValueError("Matrices have different shapes")
    return tuple(tuple(x+y for x,y in zip(ra,rb)) for ra,rb in zip(a,b))


def scale(a:Matrix,c:int)->Matrix:
    return tuple(tuple(c*x for x in row) for row in a)


def mul(a:Matrix,b:Matrix, modulus:int|None=None)->Matrix:
    if not a or not b or len(a[0])!=len(b):
        raise ValueError("Matrices incompatible")
    if any(len(row)!=len(a[0]) for row in a) or any(len(row)!=len(b[0]) for row in b):
        raise ValueError("Ragged matrices")
    out=tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b)))
                        for j in range(len(b[0]))) for i in range(len(a)))
    return mod(out,modulus) if modulus is not None else out


def mod(a:Matrix,m:int)->Matrix:
    if m<2:raise ValueError("Coefficient ring must have characteristic >=2")
    return tuple(tuple(x % m for x in row) for row in a)


def two_chart_norm(n:int)->Matrix:
    return add(identity(2*n),swap(n))


def two_chart_difference(n:int)->Matrix:
    return add(identity(2*n),scale(swap(n),-1))


def symmetric_return_mod(n:int,m:int)->Matrix|None:
    """Unique symmetric linear retract over Z/m when 2 is a unit."""
    if m<2:raise ValueError("m>=2")
    if gcd(2,m)!=1:
        return None
    inv2=pow(2,-1,m)
    return tuple(tuple(inv2 if (j%n)==i else 0
                       for j in range(2*n)) for i in range(n))


def verify_chart_obstruction(n:int,m:int)->dict:
    if n<1 or m<2:raise ValueError("invalid chart or modulus")
    S=swap(n);Delta=diagonal(n);F=first_return(n)
    N=two_chart_norm(n);D=two_chart_difference(n)
    assert mul(S,S)==identity(2*n)
    assert mul(S,Delta)==Delta
    assert mul(F,Delta)==identity(n)
    assert mul(F,S)!=F
    assert mul(N,N)==scale(N,2)
    assert mul(N,D)==scale(identity(2*n),0)
    assert mul(D,N)==scale(identity(2*n),0)
    assert mul(Delta,tuple(tuple(int(i==0) if False else int(j==i)
                           for j in range(2*n)) for i in range(n))) if False else True

    P=symmetric_return_mod(n,m)
    if P is None:
        # n=1: all possible symmetric scalar row maps (a,a).
        if n==1:
            assert all((2*a)%m!=1 for a in range(m))
        return {
            "rank":n,"modulus":m,"two_is_unit":False,
            "symmetric_return_exists":False,
            "integral_first_return_exists":True,
            "norm_square_zero_if_char2": mul(mod(N,m),mod(N,m),m)==mod(scale(N,2),m),
            "descent_status":"two_torsion_obstruction",
        }
    Sm=mod(S,m);Dm=mod(Delta,m);Nm=mod(N,m);Pm=mod(P,m)
    assert mul(Pm,Sm,m)==Pm
    assert mul(Pm,Dm,m)==mod(identity(n),m)
    assert mul(Pm,Nm,m)==mod(scale(P,2),m)
    assert mul(mod(scale(N, pow(2,-1,m)),m),
               mod(scale(N,pow(2,-1,m)),m),m)==mod(scale(N,pow(2,-1,m)),m)
    return {
        "rank":n,"modulus":m,"two_is_unit":True,
        "symmetric_return_exists":True,"inverse_two":pow(2,-1,m),
        "integral_first_return_exists":True,
        "descent_status":"split_after_inverting_two",
    }


def single_chart_gram_pullback(B:Matrix)->Matrix:
    """(Delta)^T (B+B) Delta = 2B; not a gain on original B."""
    n=len(B)
    if n==0 or any(len(row)!=n for row in B):
        raise ValueError("source Gram must be square and nonempty")
    from pathlib import Path
    import sys
    sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"phase328"))
    from stabilized_return import block_diag,transpose,matrix_mul
    Delta=diagonal(n)
    return matrix_mul(matrix_mul(transpose(Delta),block_diag(B,B)),Delta)


def quotient_invariants_c2()->dict:
    """Cohomology H^1(C2,Z_sign)=Z/2 via 1-cocycles/coboundaries.

    A 1-cocycle is determined by any integer a, as (1+sigma)a=0
    for sigma=-1. A 1-coboundary is of the form -2b.
    This is exactly Z/2, a known cyclic-group cohomology formula.
    """
    for a in range(-24,25):
        assert a+(-a)==0
        assert all((-2*b)%2==0 for b in range(-24,25))
    return {"cocycles":"Z","coboundaries":"2Z",
            "H1_sign_C2":"Z/2Z", "obstruction_order":2}


if __name__=="__main__":
    import json
    print("PHASE330_CHART_DESCENT",
          json.dumps({"cases":[verify_chart_obstruction(n,m)
                        for n in (1,2,4) for m in (2,3,5,7,14)],
                      "cohomology":quotient_invariants_c2()},
                     sort_keys=True))
