#!/usr/bin/env python3
"""Rational-only enclosure: ZF(3/4) => |disc(K)|<=295 for h(K)=1.

Assumes classical Epstein/Poisson, beta/eta/Bessel and class-number formulas.
Verifies finite rational inequalities only. No floating-point acceptance.
"""
from fractions import Fraction as Q
from math import comb, factorial, isqrt

DEN = 10**12
TERMS = 64


def scaled_root_lower(n, d, power):
    """Exact floor(DEN*(n/d)^(1/power))."""
    assert n > 0 and d > 0 and power > 0
    target=n*DEN**power
    lo,hi=0,DEN*max(2,n+1)
    while hi**power*d <= target:
        hi *= 2
    while hi-lo>1:
        m=(hi+lo)//2
        if m**power*d <= target:
            lo=m
        else:
            hi=m
    assert lo**power*d <= target < (lo+1)**power*d
    return lo


def inv_sqrt_bounds(k):
    z=isqrt(DEN**2//k)
    assert z*z*k <= DEN**2 < (z+1)**2*k
    return Q(z,DEN),Q(z+1,DEN)


def eta_bounds(s_num,nterms=TERMS):
    """Euler-transformed eta at s=1/2 or 3/2, tail <= 2^-N."""
    assert s_num in (1,3)
    vals=[]
    for k in range(1,nterms+1):
        l,u=inv_sqrt_bounds(k)
        if s_num==3:
            l/=k
            u/=k
        vals.append((l,u))
    low=high=Q(0)
    for n in range(nterms):
        ll=uu=Q(0)
        for k in range(n+1):
            a,b=vals[k]
            c=comb(n,k)
            if k%2==0:
                ll+=c*a
                uu+=c*b
            else:
                ll-=c*b
                uu-=c*a
        low+=ll/Q(2**(n+1))
        high+=uu/Q(2**(n+1))
    high+=Q(1,2**nterms)
    assert 0<low<high
    return low,high


def beta_bounds(nterms=TERMS):
    """Two positive split-integral series for B(1/4,1/2)."""
    a,b=Q(1,4),Q(1,2)
    c1=c2=Q(1)
    s1=s2=Q(0)
    for k in range(nterms):
        s1+=c1/(2**k*(a+k))
        s2+=c2/(2**k*(b+k))
        c1*=(k+1-b)/(k+1)
        c2*=(k+1-a)/(k+1)
    t1=Q(2,2**nterms)/(a+nterms)
    t2=Q(2,2**nterms)/(b+nterms)
    ra=scaled_root_lower(1,2,4)
    rb=scaled_root_lower(1,2,2)
    return (Q(ra,DEN)*s1+Q(rb,DEN)*s2,
            Q(ra+1,DEN)*(s1+t1)+Q(rb+1,DEN)*(s2+t2))


def certificate():
    eta05_lo,eta05_hi=eta_bounds(1)
    eta15_lo,eta15_hi=eta_bounds(3)
    root2=scaled_root_lower(2,1,2)
    invroot2=scaled_root_lower(1,2,2)
    abszeta05_lo=eta05_lo/(Q(root2+1,DEN)-1)
    abszeta05_hi=eta05_hi/(Q(root2,DEN)-1)
    zeta15_lo=eta15_lo/(1-Q(invroot2,DEN))
    zeta15_hi=eta15_hi/(1-Q(invroot2+1,DEN))
    beta_lo,beta_hi=beta_bounds()
    a296_hi=Q(scaled_root_lower(1,74,4)+1,DEN)
    # d>=296: a=sqrt(d)/2>8 and 2*pi*a>48>30.
    # K_(1/4)(x)<=K_(1/2)(x), so E<=24*r/(1-r)^2.
    assert Q(30**10,factorial(10))>10**8
    r=Q(1,10**8)
    tail_hi=24*r/(1-r)**2
    assert tail_hi<Q(1,10**6)
    lower=zeta15_lo-beta_hi*abszeta05_hi*a296_hi-tail_hi
    assert lower>Q(1,1000), 'conditional d>=296 exclusion not certified'
    a295_lo=Q(scaled_root_lower(4,295,4),DEN)
    neg_main_upper=zeta15_hi-beta_lo*abszeta05_lo*a295_lo
    assert neg_main_upper<0, 'd=295 main-term negative control failed'
    for k,v in [('Beta lower',beta_lo),('Beta upper',beta_hi),
                ('abs(zeta(1/2)) upper',abszeta05_hi),
                ('zeta(3/2) lower',zeta15_lo),
                ('a^-1/2 upper at d=296',a296_hi),
                ('Bessel tail upper',tail_hi),
                ('zeta_K(3/4) lower d>=296',lower),
                ('Epstein main upper at d=295',neg_main_upper)]:
        print(k, ':', float(v))
    print('EXACT RATIONAL PASS: ZF(3/4) + h=1 => d<=295')
    return lower


if __name__=='__main__':
    certificate()
