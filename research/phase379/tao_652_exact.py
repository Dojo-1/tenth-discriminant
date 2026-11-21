#!/usr/bin/env python3
"""A rational-only envelope for the familiar ZF(7/8) => d<=652 bridge.

This program does not prove the external analytic identities (Epstein/Poisson,
Hasse eta, Bessel K, Dedekind factorization, class-number formulas).
It certifies all *finite rational* inequalities used by a conditional argument.
No floating point is used by its acceptance checks.
"""
from fractions import Fraction as Q
from math import comb, isqrt, factorial

DEN = 10**11
TERMS = 48


def lower_inv_three_quarters(n):
    """floor(DEN / n^(3/4)); integer exact."""
    assert n >= 1
    z = isqrt(isqrt(DEN**4 // n**3))
    assert z**4*n**3 <= DEN**4 < (z+1)**4*n**3
    return z


def lower_scaled_root(N, D, power):
    """floor(DEN*(N/D)^(1/power)); integer exact."""
    assert N > 0 and D > 0 and power > 0
    target = N*DEN**power
    lo, hi = 0, DEN*max(2, N+1)
    while hi**power*D <= target:
        hi *= 2
    while hi-lo>1:
        mid = (lo+hi)//2
        if mid**power*D <= target:
            lo=mid
        else:
            hi=mid
    assert lo**power*D <= target < (lo+1)**power*D
    return lo


def eta_enclosure(s_num, nterms=TERMS):
    """Rational lower/upper enclosures for eta(s) at s=3/4,7/4.

    Euler transformed eta: sum_n 2^(-n-1) sum_k (-1)^k C(n,k)/(k+1)^s.
    For s>0, each inner sum is the integral of a function in [0,1],
    hence the tail is in [0,2^(-nterms)].
    """
    assert s_num in (3,7)
    vals=[]
    for k in range(nterms):
        n=k+1; z=lower_inv_three_quarters(n)
        vals.append((Q(z,DEN*n if s_num==7 else DEN),
                     Q(z+1,DEN*n if s_num==7 else DEN)))
    lower=Q(0); upper=Q(0)
    for n in range(nterms):
        dl=Q(0); du=Q(0)
        for k in range(n+1):
            f_lo, f_hi = vals[k]
            weight = comb(n,k)
            if k%2 == 0:
                dl += weight*f_lo
                du += weight*f_hi
            else:
                dl -= weight*f_hi
                du -= weight*f_lo
        lower += dl/Q(2**(n+1)); upper += du/Q(2**(n+1))
    return lower, upper + Q(1,2**nterms)


def beta_enclosure(nterms=TERMS):
    """B(3/8,1/2) via splitting the Euler beta integral at t=1/2.

    For 0<a,b<1, B(a,b)=2^-a sum_{k>=0} (1-b)_k/k! 2^-k/(a+k)
                                    +2^-b sum_{k>=0} (1-a)_k/k! 2^-k/(b+k).
    Every binomial coefficient in these sums lies in [0,1].
    """
    a,b=Q(3,8),Q(1,2)
    c1=c2=Q(1); s1=s2=Q(0)
    for k in range(nterms):
        s1 += c1/(2**k*(a+k))
        s2 += c2/(2**k*(b+k))
        c1 *= (k+1-b)/(k+1)
        c2 *= (k+1-a)/(k+1)
    e1=Q(2,2**nterms)/(a+nterms)
    e2=Q(2,2**nterms)/(b+nterms)
    # 2^(-3/8) = (1/8)^(1/8); 2^(-1/2) = (1/2)^(1/2)
    r1=lower_scaled_root(1,8,8)
    r2=lower_scaled_root(1,2,2)
    beta_lo=Q(r1,DEN)*s1 + Q(r2,DEN)*s2
    beta_hi=Q(r1+1,DEN)*(s1+e1) + Q(r2+1,DEN)*(s2+e2)
    return beta_lo,beta_hi


def certificate():
    eta3_lo,eta3_hi=eta_enclosure(3)
    eta7_lo,eta7_hi=eta_enclosure(7)
    assert 0 < eta3_lo < eta3_hi and 0 < eta7_lo < eta7_hi

    # 2^(1/4), 2^(-3/4) with exact fourth-power brackets.
    root2=lower_scaled_root(2,1,4)
    inv2_3_4=lower_inv_three_quarters(2)
    # |zeta(3/4)|=eta(3/4)/(2^(1/4)-1), and
    # zeta(7/4)=eta(7/4)/(1-2^(-3/4)).
    z3_abs_hi=eta3_hi/(Q(root2,DEN)-1)
    z7_lo=eta7_lo/(1-Q(inv2_3_4,DEN))
    beta_lo,beta_hi=beta_enclosure()
    root_654=lower_scaled_root(4**3,654**3,8)
    apower_hi=Q(root_654+1,DEN)

    # d>=654 => a=sqrt(d)/2>=12 and 2*pi*a>72>30.
    # exp(30)>30^10/10!>10^8, hence r=exp(-2*pi*a)<10^-8.
    assert Q(30**10,factorial(10))>10**8
    tail_hi=Q(24*10**8,(10**8-1)**2)
    assert tail_hi<Q(1,10**6)

    lower=z7_lo-beta_hi*z3_abs_hi*apower_hi-tail_hi
    print('Tao 7/8 rational acceptance gate')
    for name,val in [('B(3/8,1/2) upper',beta_hi),
                     ('abs(zeta(3/4)) upper',z3_abs_hi),
                     ('zeta(7/4) lower',z7_lo),
                     ('a^(-3/4) upper at d=654',apower_hi),
                     ('Bessel tail upper',tail_hi),
                     ('zeta_K(7/8) lower for all d>=654',lower)]:
        print(f'{name}: {float(val):.15g}')
    assert lower>Q(1,100000), 'The rational envelope does not certify d>=654 exclusion.'
    # Negative controls: check that the sign gate would be *absent* if d=653
    # (not a fundamental negative discriminant), using similarly valid brackets.
    r653=lower_scaled_root(4**3,653**3,8)
    apower653_lo=Q(r653,DEN)
    neg_control_upper=eta7_hi/(1-Q(inv2_3_4+1,DEN)) - beta_lo*(eta3_lo/(Q(root2+1,DEN)-1))*apower653_lo
    print('Upper bound on Epstein main term at d=653:',float(neg_control_upper))
    assert neg_control_upper<0, 'Near-threshold negative control failed'
    return lower

if __name__=='__main__':
    certificate()
