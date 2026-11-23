#!/usr/bin/env python3
"""Phase384: rational central-point sign certificate.

The only acceptance gate is an exact Fraction inequality.  External analytic
inputs (Epstein/Poisson, central Bessel identity, elementary log/gamma
bounds, class-number formula and optional zero-free hypothesis) are NOT
proved by this program.
"""
from fractions import Fraction as Q
from math import factorial

def log_bracket(x: Q, terms: int=4) -> tuple[Q,Q]:
    """Atanh-series interval for log(x), x>1."""
    assert x>1 and terms>=1
    z=(x-1)/(x+1)
    assert 0<z<1
    lo=2*sum((z**(2*k+1)/Q(2*k+1) for k in range(terms)), Q(0))
    hi=lo+2*z**(2*terms+1)/(Q(2*terms+1)*(1-z*z))
    return lo,hi

def certificate() -> Q:
    # H_n-log(n)-1/(2n) strictly increases to Euler's constant.
    n=128
    harmonic=sum((Q(1,k) for k in range(1,n+1)), Q(0))
    gamma_lo=harmonic-7*log_bracket(Q(2),4)[1]-Q(1,2*n)

    # pi<22/7 and sqrt(200)>707/50; monotonically extend to d>=200.
    assert Q(707,50)**2<200
    ratio=Q(8800,4949)
    assert ratio==(8*Q(22,7))/Q(707,50)
    logratio_hi=log_bracket(ratio,4)[1]

    # For d>=200, K_0(pi*sqrt(d)*n*k) <= exp(-pi*sqrt(d)*n*k).
    # exp(30)>30^10/10!>10^8, r<10^-8,
    # sum r^(n*k) <= r/(1-r)^2.
    assert Q(30**10,factorial(10))>10**8
    r=Q(1,10**8)
    tail_hi=4*r/(1-r)**2
    assert tail_hi<Q(1,10**6)
    lower=gamma_lo-logratio_hi-tail_hi
    assert lower>Q(1,1000)
    assert gamma_lo>Q(577,1000)
    assert logratio_hi<Q(576,1000)
    assert lower>Q(16,10000)
    for name,val in [
        ('Euler gamma lower',gamma_lo),
        ('log(8pi/sqrt(200)) upper',logratio_hi),
        ('Bessel tail upper',tail_hi),
        ('zeta_K(1/2) lower under h=1,d>=200',lower)]:
        print(f'{name}: {float(val):.15g}')
    print('PHASE384_EXACT_RATIONAL_PASS')
    return lower

if __name__=='__main__':
    certificate()
