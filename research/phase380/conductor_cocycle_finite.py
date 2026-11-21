#!/usr/bin/env python3
"""Exact rational order-conductor/Euler-correction cocycle controls at s=1.

True local algebra, not a Lean proof of analytically continued L-functions.
"""
from fractions import Fraction
from math import gcd


def prime_divisors(n):
    assert n>0
    result=[]
    for p in range(2,n+1):
        if n%p:continue
        if any(p%q==0 for q in result):continue
        result.append(p)
        while n%p==0:n//=p
        if n==1:break
    return result


def primitive_chi(D,p):
    assert D in (-4,-8)
    if p%2==0:return 0
    if D==-4:return 1 if p%4==1 else -1
    return 1 if p%8 in (1,3) else -1


def chi_at_level(D,f,p):
    M=abs(D)*f*f
    return 0 if gcd(p,M)>1 else primitive_chi(D,p)


def correction_full(D,f,g):
    assert f>0 and g%f==0
    M=abs(D)*f*f;N=abs(D)*g*g
    result=Fraction(1)
    for p in prime_divisors(N):
        result*=1-Fraction(chi_at_level(D,f,p),p)
    return result


def correction_atlas(D,f,g):
    assert f>0 and g%f==0
    result=Fraction(1)
    for p in prime_divisors(g):
        if f%p:
            result*=1-Fraction(primitive_chi(D,p),p)
    return result


def run():
    count_pair=count_triple=0
    for D in (-4,-8):
        for f in range(1,21):
            for g in range(f,21,f):
                assert correction_full(D,f,g)==correction_atlas(D,f,g),(D,f,g)
                count_pair+=1
                for h in range(g,21,g):
                    a=correction_full(D,f,h)
                    b=correction_full(D,f,g)*correction_full(D,g,h)
                    assert a==b,(D,f,g,h,a,b)
                    count_triple+=1
    assert correction_full(-4,1,3)==Fraction(4,3)
    assert correction_full(-8,1,3)==Fraction(2,3)
    assert correction_full(-4,3,9)==1
    assert correction_full(-4,1,9)==Fraction(4,3)
    naive_primitive_factor = 1 - Fraction(primitive_chi(-4,3),3)
    assert naive_primitive_factor==Fraction(4,3) != correction_full(-4,3,9)
    print('PASS: %d f|g exact source-vs-atlas corrections; %d f|g|h cocycles' %(count_pair,count_triple))
    print('Wrong re-use of primitive chi at already masked p=3:',naive_primitive_factor,'vs correct',correction_full(-4,3,9))

if __name__=='__main__':run()
