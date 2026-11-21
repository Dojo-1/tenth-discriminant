#!/usr/bin/env python3
"""Rational gates for quadratic GRH + principal Epstein central sign => d<=199.

The executable proves *only* rational inequalities. Externally required:
Epstein/Poisson analytic continuation, zeta/Gamma Laurent constants,
Bessel K0 <= K1/2, quadratic Dedekind factorization, and zero-freeness
for the primitive imaginary quadratic L(s,chi_D) on real (1/2,1).
"""
from fractions import Fraction as F
from math import factorial
from central_threshold_exact import certificate as c_interval

def certificate():
    lower,upper=c_interval()
    cap=F(1593,8) # 199.125
    assert 199<lower<upper<cap<200
    # M_{1/2}(d) = (log(d/C))/2.  For d>=200 and C<cap,
    # log(200/C)>log(200/cap)>1-cap/200.
    main_lower=F(1,2)*(1-cap/F(200))
    assert main_lower==F(7,3200)
    # d>=200 => sqrt(d)>14, pi>3 => pi*sqrt(d)>42>16.
    # exp(16)>10000 from its positive Taylor partial sum.
    assert sum((F(16**k,factorial(k)) for k in range(6)), F())>10000
    # E_{1/2}(d)=4*sum_(n,k>=1) cos(pi*b*n*k)*K_0(pi*sqrt(d)*n*k).
    # For a=sqrt(d)/2>=7, K_0(x)<=K_(1/2)(x)
    # =sqrt(pi/(2x))*exp(-x) <= exp(-x)/2.
    # With r=exp(-pi*sqrt(d))<1/10000, |E| <=2*r/(1-r)^2.
    rcap=F(1,10000)
    tail_upper=2*rcap/(1-rcap)**2
    assert tail_upper < F(1,4000)
    margin=main_lower-F(1,4000)
    assert margin==F(31,16000)>0
    print("PASS rational gates: hypothetical h=1,d>=200 implies zeta_K(1/2) > 31/16000")
    print("NO unconditional theorem: the final sign-change contradiction assumes")
    print("the primitive quadratic L-function has no real zero in (1/2,1).")
    return margin

if __name__=="__main__":certificate()
