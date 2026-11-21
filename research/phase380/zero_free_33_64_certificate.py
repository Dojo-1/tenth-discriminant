#!/usr/bin/env python3
"""Strict rational certificate for a conditional Dirichlet-GRH consequence.

Under ZF(33/64), the standard Epstein/Poisson expansion and class-number-one
principal-ideal identity imply: h(K)=1 => |disc(K)| <= 199.

The code checks ONLY exact rational enclosures/finite controls; it does not
prove the external analytic continuation, positivity formula, or ZF(33/64).
"""
from fractions import Fraction as Q
from math import comb, factorial

DEN = 10**14
NTERMS = 72


def lower_scaled_root(numer: int, denom: int, index: int) -> int:
    """Floor DEN*(numer/denom)^(1/index) by exact integer arithmetic."""
    assert numer > 0 and denom > 0 and index >= 1
    num = numer * DEN**index
    lo, hi = 0, DEN * 2
    while hi**index * denom <= num:
        hi *= 2
    while hi - lo > 1:
        md = (lo + hi) // 2
        if md**index * denom <= num:
            lo = md
        else:
            hi = md
    assert lo**index * denom <= num < (lo+1)**index * denom
    return lo


def inv32(n):
    v=lower_scaled_root(1,n,32)
    return Q(v,DEN),Q(v+1,DEN)


def eta_interval(numerator, nterms=NTERMS):
    """Eta(numerator/32) via Hasse/Euler alternating transform.

    The n-th forward difference = E[(1-exp(-T))^n] for a Gamma
    distribution T of shape numerator/32. It is in [0,1], so the
    omitted tail is between 0 and 2^-nterms.
    """
    assert numerator in (1,33)
    powers=[]
    for k in range(nterms):
        lo,hi=inv32(k+1)
        if numerator==33:
            lo/=k+1; hi/=k+1
        powers.append((lo,hi))
    lower=upper=Q(0)
    for n in range(nterms):
        inner_lo=inner_hi=Q(0)
        for k in range(n+1):
            lo,hi=powers[k]
            b=comb(n,k)
            if k%2:
                inner_lo-=b*hi; inner_hi-=b*lo
            else:
                inner_lo+=b*lo; inner_hi+=b*hi
        lower += inner_lo / 2**(n+1)
        upper += inner_hi / 2**(n+1)
    return lower,upper + Q(1,2**nterms)


def beta_interval(nterms=NTERMS):
    """Beta(1/64,1/2) by exact binomial series split at t=1/2."""
    a,b=Q(1,64),Q(1,2)
    c1=c2=Q(1); s1=s2=Q(0)
    for k in range(nterms):
        s1+=c1/(2**k*(a+k))
        s2+=c2/(2**k*(b+k))
        c1*= (k+1-b)/(k+1)
        c2*= (k+1-a)/(k+1)
    # (1-b)_k/k! and (1-a)_k/k! lie between zero and one.
    e1=Q(2,2**nterms)/(a+nterms)
    e2=Q(2,2**nterms)/(b+nterms)
    p1=lower_scaled_root(1,2,64)
    p2=lower_scaled_root(1,2,2)
    lo=Q(p1,DEN)*s1+Q(p2,DEN)*s2
    hi=Q(p1+1,DEN)*(s1+e1)+Q(p2+1,DEN)*(s2+e2)
    return lo,hi


def test_certificate():
    eta1_lo,eta1_hi=eta_interval(1)
    eta33_lo,eta33_hi=eta_interval(33)
    assert eta1_lo>0 and eta33_lo>0
    rt=lower_scaled_root(2,1,32)  # 2^(1/32)
    rlo,rhi=Q(rt,DEN), Q(rt+1,DEN)
    assert 1<rlo<rhi<2
    assert 0 < (1-1/rlo) < (1-1/rhi)
    # 1-1/r is increasing in r, so the LOWER zeta quotient must
    # use the UPPER denominator at rhi. Reversing this direction
    # would give a false lower enclosure despite passing sign tests.
    zeta33_lo = eta33_lo / (1 - 1/rhi)
    zeta33_hi = eta33_hi / (1 - 1/rlo)
    zeta1_abs_hi = eta1_hi / (2/rhi - 1)
    zeta1_abs_lo = eta1_lo / (2/rlo - 1)
    blo,bhi=beta_interval()
    # (sqrt(d)/2)^(-1/32)=(4/d)^(1/64)
    r200=lower_scaled_root(4,200,64)
    factor200_hi=Q(r200+1,DEN)
    # 2*pi*a > 42 > 30 for a=sqrt(d)/2 and d>=200.
    # Gamma(s)>=1/e for 0<s<=1; 1/Gamma(s)<e<3.
    # pi^s<4 and Bessel K_nu<=K_1/2 (0<nu<1/2)
    # lead to |E|<24*r/(1-r)^2, r<1e-8.
    assert Q(30**10,factorial(10)) > 10**8
    eps=Q(24*10**8,(10**8-1)**2)
    assert eps < Q(1,10**6)
    lower=zeta33_lo-bhi*zeta1_abs_hi*factor200_hi-eps
    assert lower > Q(1,1000), ('positive bound too weak',float(lower))
    # Near-boundary negative control: main term at d=199 remains <0.
    r199=lower_scaled_root(4,199,64)
    factor199_lo=Q(r199,DEN)
    main199_upper=zeta33_hi-blo*zeta1_abs_lo*factor199_lo
    assert main199_upper < 0,('negative control too weak',float(main199_upper))
    print('EXACT RATIONAL PASS: ZF(33/64) and standard Epstein identities imply class-number-one d<=199')
    print('Certified main-minus-Bessel lower bound at d>=200:',float(lower))
    print('Certified upper main term at d=199:',float(main199_upper))
    print('Beta interval:',float(blo), float(bhi))
    print('Zeta 33/32 lower:',float(zeta33_lo),'abs(zeta 1/32) upper:',float(zeta1_abs_hi))
    return lower,main199_upper

if __name__ == '__main__':
    test_certificate()
