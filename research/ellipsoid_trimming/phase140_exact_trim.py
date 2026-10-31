#!/usr/bin/env python3
"""Phase140: exact integer Gram when a nested ellipse trims original nodes.

All calculations are exact arbitrary-precision Python integers, except
DISPLAY ONLY base-e logarithms. The only arithmetic field chart here
is x+y*sqrt(-19); all J=4 ordinary Z derivatives with W held fixed,
R=8 S=4 monomial rows and original trace weights (2,2D).
No new field discriminant result is asserted.

Run: python3 research/ellipsoid_trimming/phase140_exact_trim.py
"""

from __future__ import annotations
from math import log

D, R, S, J, RHO = 19, 8, 4, 4, 5
DIM = R*S
GUARD = 2*(R-1)+(S-1)


def qellipse(d: int, rho: int) -> list[tuple[int, int]]:
    return [(x, y) for x in range(-rho, rho+1)
            for y in range(-rho, rho+1)
            if x*x+d*y*y <= rho*rho]


ORIGINAL = qellipse(D, RHO)
# (6/5)x^2+19y^2<=25, exactly the rational nested ellipse
# 6x^2+95y^2<=125. Difference from original form is (1/5)x^2.
NESTED = [q for q in ORIGINAL if 6*q[0]*q[0]+95*q[1]*q[1]<=125]


def cmul(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return (a[0]*b[0]-D*a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def cpow(a: tuple[int, int], n: int) -> tuple[int, int]:
    v=(1, 0)
    for _ in range(n):
        v=cmul(v, a)
    return v


def falling(n: int, j: int) -> int:
    ans=1
    for k in range(j):
        ans*=n-k
    return ans


def jets(q: tuple[int, int]) -> list[list[tuple[int, int]]]:
    z=q
    w=(q[0],-q[1])
    return [[(0,0) if j>r else
             tuple(falling(r,j)*t for t in cmul(cpow(z,r-j),cpow(w,s)))
             for j in range(J)]
            for r in range(R) for s in range(S)]


def one_node_gram(q: tuple[int, int]) -> list[list[int]]:
    a=jets(q)
    return [[sum(2*(a[i][j][0]*a[k][j][0]
                    +D*a[i][j][1]*a[k][j][1]) for j in range(J))
             for k in range(DIM)] for i in range(DIM)]


def add_matrix(a: list[list[int]], b: list[list[int]], sign: int=1) -> list[list[int]]:
    return [[a[i][j]+sign*b[i][j] for j in range(DIM)]
            for i in range(DIM)]


def determinant(a: list[list[int]]) -> int:
    """Fraction-free Bareiss; exact integer divisions checked."""
    mat=[row.copy() for row in a]
    den=1
    sign=1
    for k in range(DIM-1):
        if mat[k][k]==0:
            pivot=next((i for i in range(k+1,DIM) if mat[i][k]),None)
            if pivot is None:
                return 0
            mat[k],mat[pivot]=mat[pivot],mat[k]
            sign=-sign
        p=mat[k][k]
        for i in range(k+1,DIM):
            for j in range(k+1,DIM):
                num=mat[i][j]*p-mat[i][k]*mat[k][j]
                assert num%den==0, "invalid Bareiss division"
                mat[i][j]=num//den
            mat[i][k]=0
        den=p
    return sign*mat[-1][-1]


def ln(x: int) -> float:
    assert x>0
    s=str(x)
    k=min(15,len(s))
    return log(int(s[:k]))+(len(s)-k)*log(10)


def log_diagonal(a: list[list[int]]) -> float:
    return sum(ln(a[i][i]) for i in range(DIM))


def main() -> None:
    assert len(ORIGINAL)==21 and len(NESTED)==19 and GUARD==17
    assert GUARD<len(NESTED)
    assert set(ORIGINAL)-set(NESTED)=={(-5,0),(5,0)}
    # Every point in the FULL nested ellipse is inside the original:
    # 6x²+95y²<=125 implies 5x²+95y²<=125.
    for x in range(-6,7):
        for y in range(-3,4):
            if 6*x*x+95*y*y<=125:
                assert x*x+D*y*y<=25 and (x,y) in NESTED
    assert all(6*x*x+95*y*y<=125 for x,y in NESTED)

    # p=3 is inert for D=19 (T²+19 irreducible mod 3).
    # The same original rectangular exponent gives F_3=19 on every Q.
    f3=sum(min(r//3,S-1-s) for r in range(R) for s in range(S))
    assert f3==19
    p_divisor=3**(2*f3)

    contributions={q:one_node_gram(q) for q in ORIGINAL}
    old=[[sum(contributions[q][i][j] for q in ORIGINAL)
          for j in range(DIM)] for i in range(DIM)]
    assert old==[[sum(contributions[q][i][j] for q in NESTED)
                 +sum(contributions[q][i][j] for q in set(ORIGINAL)-set(NESTED))
                 for j in range(DIM)] for i in range(DIM)]

    full_det=determinant(old)
    assert full_det>0 and full_det%p_divisor==0
    d0=ln(full_det)
    diag0=log_diagonal(old)
    results=[]
    for q in ORIGINAL:
        if q[0]<0 or q[0]==0 and q[1]<=0:
            continue
        neg=(-q[0],-q[1])
        assert neg in contributions
        g=add_matrix(add_matrix(old,contributions[q],-1),
                     contributions[neg],-1)
        d=determinant(g)
        assert d>0 and d%p_divisor==0
        assert d<full_det
        log_d=ln(d)
        log_diag=log_diagonal(g)
        results.append((q,d0-log_d,diag0-log_diag,q== (5,0),g,d))
    assert len(results)==10
    results.sort(key=lambda z:z[1],reverse=True)
    assert results[0][0]==(5,0), "largest exact determinant drop"
    q,det_gain,diag_gain,_,slim_g,slim_det=results[0]
    assert q==(5,0) and slim_det%p_divisor==0
    assert 17.6185070<det_gain<17.6185071
    assert 10.2911332<diag_gain<10.2911334
    assert all(slim_g[i][i]<=old[i][i] for i in range(DIM))
    assert any(slim_g[i][i]<old[i][i] for i in range(DIM))

    # A shape matching the same cardinality but removing the pair (1,0)
    # also improves det; it improves it MUCH less than the nested ellipse.
    inner=next(z for z in results if z[0]==(1,0))
    assert det_gain>8*inner[1]
    # Non-nested rotated ellipse: (3,-1) satisfies x²+Dy²+5xy<=25,
    # but lies OUTSIDE x²+Dy²<=25. Can't reuse the old radial bound.
    assert 3*3+D*1*1>25
    assert 3*3+D*1*1+5*3*(-1)<=25

    # The sufficient interpolation guard changes discontinuously with D.
    # This is arithmetic lattice-point switching, NOT an NP-hardness result.
    assert len(qellipse(21,5))==21
    assert len(qellipse(22,5))==17
    assert GUARD<21 and not GUARD<17

    # Removing two antipodal pairs leaves 17 nodes. The *sufficient
    # interpolation criterion* no longer applies; this does NOT prove
    # the resulting Gram singular.
    assert len(ORIGINAL)-4==GUARD

    print("D=19 rho=5 R=8 S=J=4; original=21 nested=19; guard=17")
    print(f"same p-local divisor 3^(2F3) = 3^{2*f3}; exact division passed")
    print(f"log original determinant: {d0:.12f}")
    print(f"log nested determinant:   {ln(slim_det):.12f}")
    print(f"log determinant decrease: {det_gain:.12f}")
    print(f"raw monomial Hadamard log decrease: {diag_gain:.12f}")
    print("all 10 matched 19-node antipodal-pair controls:")
    for q,dgain,ugain,_,_,_ in results:
        print(f"  removed (+/-){q}: det log drop={dgain:.9f}; diagonal log drop={ugain:.9f}")
    print("PASS: exact original jets, positive Gram, same inert divisor,")
    print("nested ellipsoid, equal-card controls and discarded guard counterworld")


if __name__=="__main__":
    main()
