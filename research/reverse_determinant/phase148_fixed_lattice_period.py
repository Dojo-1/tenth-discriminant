#!/usr/bin/env python3
"""Phase148: exact universal parameter period in a FIXED observation universe.

D is an indeterminate in the original integer-pair ordinary-Z jet evaluator.
The real-axis jet lattice is independent of D. Six consecutive polynomial
checks prove an all-integer-D congruence of original columns modulo that
lattice. The test deliberately does not assert the varying ellipse is fixed.
"""
from __future__ import annotations
from math import prod
from sympy import ZZ
from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form
from phase147_prime_adequacy import N,R,S,J,original_eval,qellipse,dabs

def first_failure(C):
    for i in range(C.rows):
        for j in range(C.cols):
            if C[i,j].q!=1:return (i,j,int(C[i,j].q))
    return None

def main():
    assert (N,R,S,J)==(32,8,4,4)
    omega=qellipse(17)
    assert len(omega)==21 and omega==qellipse(21)
    # Fixed real channels; zero imaginary coordinates on the x-axis.
    axis=original_eval([(x,0) for x in range(-4,4)],19)
    fixed=axis[:,[8*t+2*j for t in range(8) for j in range(J)]]
    # This matrix is independent of the parameter D.
    assert fixed==original_eval([(x,0) for x in range(-4,4)],21)[:,[8*t+2*j for t in range(8) for j in range(J)]]
    determinant=dabs(fixed)
    assert determinant>0
    smith=smith_normal_form(fixed,domain=ZZ)
    factors=[abs(int(smith[i,i])) for i in range(N)]
    assert prod(factors)==determinant
    exponent=factors[-1]
    assert exponent==1058400
    assert exponent%529200==0
    print("fixed-real-lattice Smith exponent",exponent,
          "index",determinant,flush=True)

    Binv=fixed.inv()
    samples=[original_eval(omega,d) for d in range(6)]

    def column_period(t):
        """Six integer-valued polynomial samples certify ALL integer D."""
        for d in range(6):
            delta=Binv*(original_eval(omega,d+t)-samples[d])
            fail=first_failure(delta)
            if fail is not None:return False,(d,*fail)
        return True,None

    # Exponent is a universal period because E(D) has integer polynomial
    # entries and exp(Z^32/im fixed)=exponent.
    yes,fail=column_period(exponent)
    assert yes
    period=529200
    yes,fail=column_period(period)
    assert yes
    # Positive periods form a subgroup in Z under addition. Since period is
    # a period, absence of period/p for every prime p dividing period
    # proves it is the MINIMUM positive period of this COLUMN congruence,
    # not necessarily the shortest period of the full IMAGE itself.
    for p in (2,3,5,7):
        assert period%p==0
        yes,fail=column_period(period//p)
        assert not yes and fail is not None,(p,yes,fail)
        print("excluded divisor",period//p,"prime",p,
              "first failure (d,row,col,denominator)",fail,flush=True)

    # The period is universal in the formal fixed Omega, including outside
    # its original elliptical admissibility when D is shifted.
    for d in (17,18,19,20,21):
        delta=Binv*(original_eval(omega,d+period)-original_eval(omega,d))
        assert first_failure(delta) is None
        # Verify that the literal INTEGER COLUMN IMAGE, not merely its
        # abstract Smith group, is unchanged in this fixed universe.
        H0=hermite_normal_form(original_eval(omega,d),D=determinant)
        H1=hermite_normal_form(original_eval(omega,d+period),D=determinant)
        assert H0==H1
    print("PASS: literal full-image return for each D17..21 after formal parameter period",flush=True)
    print("PHASE148_PERIOD_PASS: all-integer-D column-congruence period",
          period,"minimum for fixed real-axis quotient",flush=True)

if __name__=="__main__":
    main()
