#!/usr/bin/env python3
"""Finite mathematical witnesses for spectral sampling and positivity scope.

No claim about actual Hecke zeros, the Masullo trace formula, or universal
Selberg/Ihara spectra follows from these deliberately abstract controls.
"""
from fractions import Fraction as F
from math import exp


def bump(t, eps):
    """C-infinity compact bump centered at 0, max 1, support [-eps,eps]."""
    if abs(t)>=eps:return 0.0
    z=t/eps
    return exp(1-1/(1-z*z))


def sampling_counterworld():
    # For eps<1, all integer samples except n=0 vanish exactly, and
    # the 0-th sample is exactly 1. Yet L1 integral <= 2*eps.
    for denom in (10,100,1000,10000):
        eps=1/denom
        values=[bump(i,eps) for i in range(-5,6)]
        assert values[5]==1 and all(v==0 for i,v in enumerate(values) if i!=5)
        assert 2*eps < 1
        print('epsilon=1/%d sample sum=1, integral<=%g, lower ratio>=%.1f' %(denom,2*eps,denom/2))
    return True


def ihara_matrix_positivity_counterworld():
    # q=3, 2*sqrt(q)~3.46; diag(4,0) violates Ramanujan,
    # but trace(4*q*I-A^2)=(-4)+12=8 is strictly positive.
    q=3
    spectrum=[F(4),F(0)]
    diagonal=[F(4*q)-lam*lam for lam in spectrum]
    assert diagonal==[F(-4),F(12)]
    trace=sum(diagonal)
    assert trace==8 and min(diagonal)<0
    # Two violations can leave the determinant positive:
    bad2=[F(4),F(4)]
    matrixdiag=[F(4*q)-x*x for x in bad2]
    assert matrixdiag==[F(-4),F(-4)] and matrixdiag[0]*matrixdiag[1]==16
    print('Ihara quadratic-form test: positive trace=',trace,'but a negative eigenvalue exists')
    print('Two off-circle modes: determinant of 4qI-A^2=',16,'>0 despite non-PSD form')
    return True

if __name__=='__main__':
    sampling_counterworld()
    ihara_matrix_positivity_counterworld()
    print('PASS: finite logical counterworlds (NOT actual L-function or graph-theorem checks)')
