#!/usr/bin/env python3
"""Exact Fraction certificate: 199 < (8*pi*exp(-EulerGamma))^2 < 200.

External mathematical identities used: Machin formula for pi, atanh log2,
harmonic-number bounds for Euler's constant, and exp Taylor remainder.
No special-function evaluation or floating-point value is an acceptance gate.
"""
from fractions import Fraction as F
from math import factorial

def atan_interval(x, terms):
    s=sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(terms)), F())
    err=x**(2*terms+1)/F(2*terms+1)
    return (s,s+err) if terms%2==0 else (s-err,s)

def log2_interval(terms):
    x=F(1,3)
    s=2*sum((x**(2*k+1)/F(2*k+1) for k in range(terms)),F())
    rem=2*x**(2*terms+1)/(F(2*terms+1)*(1-x*x))
    return s,s+rem

def gamma_interval(n=256, terms=18):
    assert n>0 and n&(n-1)==0
    h=sum((F(1,k) for k in range(1,n+1)),F())
    lo2,hi2=log2_interval(terms)
    power=n.bit_length()-1
    # 1/(2(n+1)) < H_n-log(n)-EulerGamma < 1/(2n).
    return h-power*hi2-F(1,2*n), h-power*lo2-F(1,2*(n+1))

def exp_interval(x,terms=20):
    assert F(0)<=x<F(1)
    partial=sum((x**k/F(factorial(k)) for k in range(terms)),F())
    rem=(x**terms/F(factorial(terms)))/(1-x/F(terms+1))
    return partial,partial+rem

def certificate():
    a5l,a5u=atan_interval(F(1,5),9)
    a239l,a239u=atan_interval(F(1,239),5)
    pil,piu=16*a5l-4*a239u,16*a5u-4*a239l
    assert 3<pil<piu<F(22,7)
    gl,gu=gamma_interval()
    assert F(1,2)<gl<gu<F(3,5)
    el,_=exp_interval(gl)
    _,eu=exp_interval(gu)
    lower=64*pil*pil/(eu*eu)
    upper=64*piu*piu/(el*el)
    assert F(199)<lower<upper<F(1593,8)<F(200)
    print("PASS exact rational: 199 < C=(8*pi*exp(-EulerGamma))^2 < 199.125")
    print("display-only rational interval for C:",float(lower),float(upper))
    return lower,upper

if __name__=="__main__":
    certificate()
