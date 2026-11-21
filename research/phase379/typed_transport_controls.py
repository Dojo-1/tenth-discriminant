#!/usr/bin/env python3
"""Exact finite counterworlds and bounded analytic sanity checks.

These tests are not a Lean proof of a general analytic L-function statement,
Selberg or Ihara RH, or Masullo's claimed trace formula.
"""
import cmath
import math
from fractions import Fraction


def matmul_2(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def trace_2(a):
    return a[0][0]+a[1][1]


def masullo_two_counterexamples():
    # Appendix C Lemma C.3.4.1(2): absolute diagonal sum is NOT ONB invariant.
    T=((1,0),(0,-1))
    # U = H / sqrt(2), H=[[1,1],[1,-1]], so U^T T U = H^T T H/2.
    H=((1,1),(1,-1))
    HT=tuple(zip(*H))
    HTTH=matmul_2(HT,matmul_2(T,H))
    rotated=tuple(tuple(Fraction(x,2) for x in row) for row in HTTH)
    assert rotated==((0,Fraction(1)),(Fraction(1),0))
    assert abs(T[0][0])+abs(T[1][1]) == 2
    assert abs(rotated[0][0])+abs(rotated[1][1]) == 0
    assert trace_2(T)==trace_2(rotated)==0

    # Appendix C Lemma C.3.4.4(2): ||AT||_1 = ||TA||_1 is false.
    P=((1,0),(0,0))
    A=((0,1),(0,0))
    AP=matmul_2(A,P)
    PA=matmul_2(P,A)
    assert AP==((0,0),(0,0))
    assert PA==A
    # Singular values square to eigenvalues of B^T B, here diagonal (0,1).
    PAT=tuple(zip(*PA))
    normal=matmul_2(PAT,PA)
    assert normal==((0,0),(0,1))
    assert matmul_2(AP,AP)==((0,0),(0,0))
    return {"abs_diagonal_standard":2,"abs_diagonal_rotated":0,
            "trace_norm_AP":0,"trace_norm_PA":1,
            "correct_general_replacement":"each trace norm <= ||A||*||T||_1"}


def polynomial_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c


def order_at_zero(poly):
    return next((i for i,c in enumerate(poly) if c!=0), None)


def multiplicity_jet_controls():
    L=[0,0,0,3,2]   # z^3(3+2z)
    F=[5,-1,2]      # local analytic unit: F(0) !=0
    G=[0,4,1]       # not a unit, G(0)=0
    assert order_at_zero(L)==3
    assert order_at_zero(polynomial_mul(L,F))==3
    assert order_at_zero(polynomial_mul(L,G))==4
    # Metamorphic test: any constant nonzero local factor preserves the order.
    for m in range(6):
        poly=[0]*m+[1,7]
        for c in [-7,-2,-1,1,2,9]:
            assert order_at_zero(polynomial_mul(poly,[c,1,-3]))==m
    return {"analytic_unit_preserves_order":True,
            "zero_constant_factor_can_increase_order":True}


def boundary_euler_control():
    # Primitive chi_{-4}(3)=-1; induced character at modulus 12
    # introduces the factor F(s)=1+3^{-s}.
    p=3
    boundary=1j*math.pi/math.log(p)
    assert abs(1+cmath.exp(-boundary*math.log(p)))<1e-12
    for sigma in [0.125,0.5,0.875,1,2]:
        # For Re(s)>0, |3^{-s}|=3^{-Re(s)}<1, so F cannot vanish.
        assert p**(-sigma)<1
    return {"boundary_pole_or_zero_location":str(boundary),
            "new_euler_zero_real_part":0,
            "right_half_plane_euler_nonvanishing":True}


def ihara_counterworld():
    # Existing repository fixture: connected 4-regular switched K4,4.
    # Its characteristic polynomial contains x^2 - 2*x - 6.
    q=3
    lam=1+math.sqrt(7)
    assert math.sqrt(7)>2
    assert lam>2*math.sqrt(q)
    discr=lam*lam-4*q
    u1=(lam-math.sqrt(discr))/(2*q)
    u2=(lam+math.sqrt(discr))/(2*q)
    assert u1>0 and u1<1/math.sqrt(q)<u2
    assert abs(u1*u2-1/q)<1e-13
    t=math.acosh(lam/(2*math.sqrt(q)))
    delta=t/math.log(q)
    s1=-math.log(u1)/math.log(q)
    s2=-math.log(u2)/math.log(q)
    assert abs(s1-(0.5+delta))<1e-12
    assert abs(s2-(0.5-delta))<1e-12
    return {"lambda":lam,"critical_threshold":2*math.sqrt(q),
            "poles":(u1,u2),"real_s":(s1,s2),"delta":delta}


if __name__ == '__main__':
    for name,fn in [('Masullo finite counterexamples',masullo_two_counterexamples),
                    ('Taylor multiplicity',multiplicity_jet_controls),
                    ('Dirichlet Euler boundary',boundary_euler_control),
                    ('Ihara non-Ramanujan',ihara_counterworld)]:
        print(name,fn())
