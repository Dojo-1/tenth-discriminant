#!/usr/bin/env python3
"""Phase383 exact-rational Epstein sign gate at s=33/64.

Conditional on standard Epstein/Poisson, class-number and Dedekind identities,
and the zero-free interval (33/64,1), proves |D| <= 199 when h(K)=1.
Acceptance uses Fraction/int arithmetic, not floating point.
"""
from fractions import Fraction as Q
from math import comb, factorial

DEN = 10**12
TERMS = 64

def lower_root(n, d, p):
    assert n > 0 and d > 0 and p > 0
    t = n * DEN**p
    lo, hi = 0, DEN*max(2,n+1)
    while d*hi**p <= t:
        hi *= 2
    while hi-lo > 1:
        m = (lo+hi)//2
        if d*m**p <= t:
            lo = m
        else:
            hi = m
    assert d*lo**p <= t < d*(lo+1)**p
    return lo

def eta_interval(above_one):
    vals=[]
    for k in range(1,TERMS+1):
        z=lower_root(1,k,32)
        lo,hi=Q(z,DEN),Q(z+1,DEN)
        if above_one:
            lo,hi=lo/k,hi/k
        vals.append((lo,hi))
    lower=upper=Q(0)
    for n in range(TERMS):
        dl=du=Q(0)
        for k in range(n+1):
            a,b=vals[k]
            c=comb(n,k)
            if k%2 == 0:
                dl+=c*a
                du+=c*b
            else:
                dl-=c*b
                du-=c*a
        lower+=dl/Q(2**(n+1))
        upper+=du/Q(2**(n+1))
    upper+=Q(1,2**TERMS)
    assert 0<lower<upper
    return lower,upper

def beta_interval():
    a,b=Q(1,64),Q(1,2)
    c1=c2=Q(1)
    s1=s2=Q(0)
    for k in range(TERMS):
        s1+=c1/(2**k*(a+k))
        s2+=c2/(2**k*(b+k))
        c1*=(k+1-b)/(k+1)
        c2*=(k+1-a)/(k+1)
    t1=Q(2,2**TERMS)/(a+TERMS)
    t2=Q(2,2**TERMS)/(b+TERMS)
    r1=lower_root(1,2,64)
    r2=lower_root(1,2,2)
    return (Q(r1,DEN)*s1+Q(r2,DEN)*s2,
            Q(r1+1,DEN)*(s1+t1)+Q(r2+1,DEN)*(s2+t2))

def certificate():
    e1l,e1u=eta_interval(False)
    e33l,e33u=eta_interval(True)
    x=lower_root(2**31,1,32)
    y=lower_root(1,2,32)
    assert Q(x,DEN)>1 and Q(y+1,DEN)<1
    z1lo=e1l/(Q(x+1,DEN)-1)
    z1hi=e1u/(Q(x,DEN)-1)
    z33lo=e33l/(1-Q(y,DEN))
    z33hi=e33u/(1-Q(y+1,DEN))
    blo,bhi=beta_interval()
    a200hi=Q(lower_root(1,50,64)+1,DEN)
    assert Q(30**10,factorial(10))>10**8
    r=Q(1,10**8)
    tail=24*r/(1-r)**2
    assert tail<Q(1,10**6)
    bound=z33lo-bhi*z1hi*a200hi-tail
    assert bound>Q(1,1000), "positive sign gate failed"
    a199lo=Q(lower_root(4,199,64),DEN)
    negative_control=z33hi-blo*z1lo*a199lo
    assert negative_control<0, "negative main-term control failed"
    print("EXACT_FRACTION_PASS ZF(33/64), h=1 => absolute D <= 199")
    print("lower_zeta_K_at_d_ge_200",float(bound))
    print("upper_main_term_at_d_199",float(negative_control))
    print("bessel_tail_upper",float(tail))
    return bound

if __name__ == "__main__":
    certificate()
