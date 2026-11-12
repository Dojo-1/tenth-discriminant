#!/usr/bin/env python3
"""Phase286-B: exact rational normalized dual Gaussian theta at a special t_D.

Registered at 988080b, after Phase286-A focused success and before this code.
This is an exact finite enclosure of a classical Poisson dual SERIES, not an
independent numerical verification of Poisson's functional identity.
"""
from fractions import Fraction

D_SET=(19,403)
C=4
BOX=4


def dyadic(exp):
    assert isinstance(exp,int) and exp>=0
    return Fraction(1,1<<exp)


def first_oracle(D,N):
    """Sum all Z^2 box dual modes, allowing only m+n even."""
    return sum(
        (dyadic(C*(D*m*m+n*n))
         for m in range(-N,N+1)
         for n in range(-N,N+1)
         if (m+n)%2==0),
        Fraction(0)
    )


def second_oracle(D,N):
    """Independently factor the dual theta into two parity-filtered 1D sums."""
    result=Fraction(0)
    for m in range(-N,N+1):
        x=dyadic(C*D*m*m)
        y=sum((dyadic(C*n*n) for n in range(-N,N+1)
               if n%2==m%2),Fraction(0))
        result+=x*y
    return result


def dual_bound(N):
    K=N+1
    q=Fraction(K+1,K)*dyadic(C*(2*K+1))
    assert 0<q<1
    B=Fraction(8*K,1)*dyadic(C*K*K)/(1-q)
    return q,B


def audit(D):
    assert D>=1 and D%4==3
    N=BOX
    observed=first_oracle(D,N)
    assert observed==second_oracle(D,N),("dual sum oracle mismatch",D)
    q,B=dual_bound(N)
    assert B<dyadic(94),("dual tail wider than preregistered",D,B)
    # Both modes (m,n)=(0,2),(0,-2) contribute 2^(-16) each.
    assert Fraction(1)+dyadic(15)<observed
    assert observed+B<Fraction(1)+dyadic(14)
    assert observed>1
    # Wrong dual source includes forbidden odd m+n; the pair (0,+/-1)
    # adds exactly 2*2^(-4)=1/8, with other nonnegative terms.
    wrong=sum((dyadic(C*(D*m*m+n*n))
        for m in range(-N,N+1) for n in range(-N,N+1)),Fraction(0))
    assert wrong-observed>=dyadic(3),("missing half-coset parity ignored",D)
    # The dual series is positive: the rigorous interval is [observed, observed+B].
    assert observed+B>observed
    print("PHASE286_DUAL_EXACT",{
        "D":D,
        "c":C,
        "box_radius":N,
        "dual_parity_constraint":"m+n even",
        "rational_sum_oracles_equal":True,
        "strict_dual_unknown_tail_lt_2_pow_minus":94,
        "normalized_theta_excess_between":"2^-15 and 2^-14",
        "wrong_parity_excess_at_least":"2^-3",
        "primal_theta_time":"pi^2/(4*D*ln2)",
        "no_float_or_pi_evaluation":True,
        "not_an_independent_Poisson_numeric_test":True,
        "not_an_L_zero_theorem":True,
    },flush=True)


def main():
    for D in D_SET:
        audit(D)
    print("PASS Phase286-B exact normalized dual-Poisson dyadic enclosure",flush=True)


if __name__=="__main__":
    main()
