#!/usr/bin/env python3
"""Phase162: source-matched finite controls for the binary null-polynomial lower.

The production object remains the original ordinary-Z derivative matrix:
E_Q, trace weights (2,2D), G_Q = E_Q B_Q E_Q.T.
The mathematical uniform divisibility theorem is still a paper proof
until its full row-jet factorization is checked in Lean.
"""
from math import comb, factorial, gcd
from sympy import Matrix, Poly, Symbol, diff
from phase159_observation_continuum import (
    ordinary_effective, source_correspondence, rankmod, beta, pairmul, powers
)


def binary_floor(R, S):
    """All RS Gram rows have a factor 2^floor(r/4) on EACH side.

    The trace metric supplies another global factor 2^RS.
    """
    assert R >= 0 and S >= 0
    ksum = sum(r // 4 for r in range(R))
    return R * S + 2 * S * ksum


def normalized_exact_identity_control():
    for R in range(1, 101):
        for S in (1, 2, 3, 5, 13):
            t = R % 4
            lam = binary_floor(R, S)
            assert 4 * lam == S * (R*R + t*(4-t))
            assert 4 * lam >= R*R*S
    print("PHASE162_QUARTER_NORMALIZED_LOWER_PASS", flush=True)


def original_null_value(q, D):
    """z^4 - z^2 in Z[sqrt(-D)] without changing the original order."""
    zz = powers(q, 4, D)
    return zz[4][0] - zz[2][0], zz[4][1] - zz[2][1]


def source_row_certificate(Q, D, R, S):
    E, weights, orders = ordinary_effective(Q, D, R, S)
    assert len(E) == R*S
    assert len(E[0]) == len(weights) == len(orders)
    assert all(w in (2, 2*D) for w in weights)
    assert len(weights) >= R*S

    # P_rs(Z,W) = Z^(r-4k)*(Z^4-Z^2)^k*W^s.
    # The t-th term is (-1)^t * C(k,t) * Z^(r-2t)*W^s.
    # t=0 gives diagonal 1; all t>0 decrease the row-major index.
    row_factors = []
    for r in range(R):
        k = r//4
        assert all(r-2*t < r and r-2*t >= 0 for t in range(1,k+1))
        for s in range(S):
            m = 2**k
            for col in range(len(weights)):
                val = sum((-1)**t*comb(k,t)*E[(r-2*t)*S+s][col]
                          for t in range(k+1))
                assert val % m == 0, (Q,D,R,S,r,s,col,k,val)
            row_factors.append(k)
    assert binary_floor(R,S)==R*S+2*sum(row_factors)
    return binary_floor(R,S), beta(Q,D,R,S), len(weights)


def null_point_controls():
    for D in (1,2,3,4,19,163):
        for x in range(-3,4):
            for y in range(-3,4):
                a,b=original_null_value((x,y),D)
                assert a%2==b%2==0
    # ALL positive ordinary derivatives of F are even as POLYNOMIALS,
    # a stronger statement than merely evaluating F mod 2 at one point.
    Z=Symbol("Z")
    F=Z**4-Z**2
    for j in range(1,9):
        f=Poly(diff(F,Z,j),Z)
        assert all(int(c)%2==0 for c in f.all_coeffs())
    # Simpler-looking degree-two null is FALSE on the same selected order.
    q=(0,1);z=powers(q,2,3)
    wrong=(z[2][0]-q[0],z[2][1]-q[1])
    assert wrong==(-3,-1) and wrong[1]%2
    print("PHASE162_SOURCE_NULL_POLYNOMIAL_AND_NEGATIVE_CONTROL_PASS",flush=True)


def finite_support_controls():
    samples=[
      (3,8,4,[(0,2),(-2,1),(-1,0),(0,1),(1,1)],64),
      (19,8,4,[(x,0) for x in range(-5,6)]+[(0,1)],64),
      (163,30,5,[(x,0) for x in range(-10,11)]
        +[(x,1) for x in range(-2,3)],1130),
      (163,30,5,[(x,0) for x in range(-10,11) if x!=0]
        +[(x,1) for x in range(-2,3)],1130),
      (4,12,3,[(x,0) for x in range(-12,13)],108),
    ]
    for D,R,S,Q,want in samples:
        lower,base,ncols=source_row_certificate(Q,D,R,S)
        assert lower==want
        if (D,R,S)==(163,30,5):
            assert base==(430 if len(Q)==26 else 450)
            assert lower-base==(700 if len(Q)==26 else 680)
        print("PHASE162_BINARY_LOWER_CONTROL",{
           "D":D,"R":R,"S":S,"support":len(Q),"channels":ncols,
           "fact_floor":base,"null_floor":lower},flush=True)

    # A row-factor theorem is NOT a positivity theorem. One node gives
    # too few channels for this nontrivial four-row polynomial rectangle.
    E,_,_=ordinary_effective([(0,0)],3,4,2)
    assert len(E[0]) < 8 and rankmod(E,3)<8


def mixed_floor(R, S):
    """Unimodular two-variable null factors: F=Z^4-Z^2, H=Z^2-W^2."""
    m = 0
    for r in range(R):
        for ss in range(S):
            b = min(r//2, (S-1-ss)//2)
            a = (r-2*b)//4
            m += a+b
    return R*S+2*m


def mixed_row_certificate(Q, D, R, S):
    """Exact original (r,s,j,point,re/im) row transform; no new sampler."""
    E, weights, _ = ordinary_effective(Q, D, R, S)
    assert len(E) == R*S and len(E[0]) == len(weights)
    for r in range(R):
        for ss in range(S):
            b = min(r//2, (S-1-ss)//2)
            a = (r-2*b)//4
            assert 4*a+2*b <= r and ss+2*b < S
            for col in range(len(weights)):
                val = sum(
                    (-1)**(t+u) * comb(a,t) * comb(b,u)
                    * E[(r-2*t-2*u)*S+ss+2*u][col]
                    for t in range(a+1) for u in range(b+1))
                assert val % (2**(a+b)) == 0, (D,r,ss,col,a,b,val)
    return mixed_floor(R,S)


def mixed_controls():
    samples = [
        (3,8,4,[(0,2),(-2,1),(0,0),(2,-1)],80),
        (19,8,4,[(0,2),(-2,1),(0,0),(2,-1)],80),
        (163,30,5,[(x,0) for x in range(-10,11)]
            + [(x,1) for x in range(-2,3)],1242),
        (2,10,5,[(x,y) for x in range(-2,3)
                    for y in range(-2,3)],162),
    ]
    for D,R,S,Q,want in samples:
        assert mixed_row_certificate(Q,D,R,S) == want
        assert want >= binary_floor(R,S)
    for R in range(1,101):
        for S in range(1,14):
            assert mixed_floor(R,S) >= binary_floor(R,S)
    # H=Z^2-W^2 vanishes at order zero with a factor four, and
    # all positive ordinary Z derivatives are even as well.
    for D in (1,2,3,19,163):
        for x in range(-3,4):
            for y in range(-3,4):
                z2=powers((x,y),2,D)[2]
                w2=powers((x,-y),2,D)[2]
                h=(z2[0]-w2[0],z2[1]-w2[1])
                assert h==(0,4*x*y) and all(v%2==0 for v in h)
    print("PHASE162_TWO_VARIABLE_BINARY_WEAVE_PASS",flush=True)


def coprime_control():
    # The odd prime mass is a separate existing theorem; the only legal
    # conjunction is coprimality, not a second count of odd factors.
    binary=2**11
    odd=3**5*5**4
    assert gcd(binary,odd)==1
    n=binary*odd*7
    assert n%binary==0 and n%odd==0 and n%(binary*odd)==0
    print("PHASE162_BINARY_ODD_COPRIME_CONTROL_PASS",flush=True)


if __name__ == "__main__":
    source_correspondence()
    null_point_controls()
    normalized_exact_identity_control()
    finite_support_controls()
    mixed_controls()
    coprime_control()
    print("PHASE162_BINARY_NULL_LOWER_PASS: finite source checks only",flush=True)
