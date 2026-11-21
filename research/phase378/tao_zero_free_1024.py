#!/usr/bin/env python3
"""Phase378: exact rational certificate for a CONDITIONAL Tao challenge bridge.

Mathematical input, NOT proved by this script: quadratic Dirichlet L-functions
have no real zero in (7/8, 1); the Epstein/Poisson expansion, Bessel bound,
Euler alternating eta identity, quadratic class-number identities, and Gauss's
classification of reduced binary quadratic forms.

Checked here: every rational inequality in the explicit d < 1024 reduction,
then independent finite class-number computations for all fundamental
negative discriminants with abs(D)<1024.

No Lean proof, no new Siegel-zero proof, no claim of independence from GRH.
"""

from fractions import Fraction as F
from math import factorial, gcd, isqrt

CUTOFF = 1024
EXPECTED = (3, 4, 7, 8, 11, 19, 43, 67, 163)
Q = 10**6


def floor_scaled_inverse_three_quarters(n: int) -> int:
    """floor(Q/n**(3/4)) using ONLY integer fourth-root comparisons."""
    assert n > 0
    result = isqrt(isqrt(Q**4 // n**3))
    assert result**4 * n**3 <= Q**4 < (result + 1)**4 * n**3
    return result


def certify_analytic_rationals() -> None:
    # beta(3/8,1/2) via Cauchy-Schwarz/log-convexity between
    # beta(1/4,1/2) and beta(1/2,1/2)=pi.
    # beta(1/4,1/2) = 4*int_0^(pi/2) [1+sin(theta)**2]**(-1/2) dtheta
    # <= pi*(1+1/sqrt(2)), by the secant bound for a convex function.
    # With pi < 22/7, 1/sqrt(2) < 5/7, conclude
    # beta(3/8,1/2)**2 < (22/7)^2*(12/7) < (33/8)^2.
    assert 7**2 < 2*5**2  # 1/sqrt(2) < 5/7
    assert F(22, 7) ** 2 * F(12, 7) < F(33, 8) ** 2

    # eta(.75) <= its 61st partial sum (positive alternating series),
    # with each reciprocal fourth-root bracketed by exact integer powers.
    eta_upper = F(0)
    for n in range(1, 62):
        lower = floor_scaled_inverse_three_quarters(n)
        eta_upper += F(lower + 1, Q) if n % 2 else -F(lower, Q)
    assert eta_upper < F(27, 40), ("eta upper", float(eta_upper))
    assert 19**4 < 2 * 16**4  # 2**(1/4)-1 > 3/16
    # zeta(3/4)=-eta(3/4)/(2**(1/4)-1): abs(zeta(3/4)) < 18/5.

    # zeta(7/4) > sum_{1<=n<=4} n^(-7/4) + (4/3)*5^(-3/4)
    # > 19/10. Lower bounds use integer-fourth-root comparisons.
    zeta_lower = sum(
        (F(floor_scaled_inverse_three_quarters(n), Q*n) for n in range(1, 5)),
        F(0),
    )
    zeta_lower += F(4, 3) * F(floor_scaled_inverse_three_quarters(5), Q)
    assert zeta_lower > F(19, 10), ("zeta lower", float(zeta_lower))

    # For a=sqrt(d)/2 >= 16,  a^(-3/4) <= 16^(-3/4)=1/8.
    # Thus the magnitude of the negative constant term is < 297/160.
    neg_upper = F(33, 8) * F(18, 5) / 8
    assert neg_upper == F(297, 160)

    # Bessel K_{3/8}(x) <= K_{1/2}(x), x>0, and standard gamma bound
    # imply the nonzero Fourier-mode tail <= 24 * r/(1-r)^2
    # with r=exp(-2*pi*a).  For a >= 16, pi>3 gives 2*pi*a>96>16.
    # Partial Taylor sum verifies e**16>10000, hence r<1/10000.
    assert sum((F(16**k, factorial(k)) for k in range(6)), F()) > 10000
    tail_upper = F(24*10000, 9999**2)
    assert tail_upper < F(1, 100)

    margin = F(19, 10) - neg_upper - F(1, 100)
    assert margin == F(27, 800) and margin > 0
    print("Exact rational certificate: PASS")
    print("eta(3/4) odd-partial upper:", float(eta_upper), "<27/40")
    print("zeta(7/4) finite+integral lower:", float(zeta_lower), ">19/10")
    print("zeta_K(7/8) conditional positivity margin: >", margin)


def squarefree_sieve(limit: int) -> list[bool]:
    out = [True] * (limit + 1)
    out[0] = False
    for p in range(2, isqrt(limit) + 1):
        for k in range(p*p, limit + 1, p*p):
            out[k] = False
    return out


def is_fundamental(D: int, squarefree: list[bool]) -> bool:
    if D >= 0:
        return False
    if D % 4 == 1:
        return squarefree[-D]
    if D % 4 == 0:
        m = D // 4
        return m % 4 in (2, 3) and squarefree[-m]
    return False


def count_reduced_primitive_forms(D: int) -> int:
    """Unrestricted Gauss reduced-form enumeration, including tie orientation."""
    assert D < 0 and D % 4 in (0, 1)
    count = 0
    for a in range(1, isqrt((-D)//3) + 1):
        for b in range(-a, a+1):
            if (b*b-D) % (4*a):
                continue
            c = (b*b-D)//(4*a)
            if c < a or gcd(gcd(a, abs(b)), c) != 1:
                continue
            if b < 0 and (abs(b) == a or a == c):
                continue
            count += 1
    return count


def jacobi(a: int, n: int) -> int:
    """Reciprocity algorithm for Jacobi(a/n), n odd and positive."""
    assert n >= 1 and n % 2
    a %= n
    result = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    return result if n == 1 else 0


def kronecker_D_n(D: int, n: int) -> int:
    """Quadratic character for fundamental D<0 and positive integer n."""
    assert D < 0 and n >= 1
    power2_character = 0 if D % 2 == 0 else (-1 if D % 8 in (3, 5) else 1)
    multiplier = 1
    while n % 2 == 0:
        multiplier *= power2_character
        n //= 2
    return multiplier * jacobi(D, n)


def class_number_from_character(D: int) -> int:
    """Independent finite check via h=-(w/(2d))*sum_{a=1}^{d-1} a chi_D(a)."""
    d = -D
    w = 6 if d == 3 else (4 if d == 4 else 2)
    weighted_sum = sum(a * kronecker_D_n(D, a) for a in range(1, d))
    numerator = -w * weighted_sum
    assert numerator % (2 * d) == 0, (D, numerator)
    return numerator // (2*d)


def verify_finite_classification() -> None:
    sieve = squarefree_sieve(CUTOFF)
    survivors = []
    fundamental_count = 0
    for d in range(1, CUTOFF):
        D = -d
        if not is_fundamental(D, sieve):
            continue
        fundamental_count += 1
        h_forms = count_reduced_primitive_forms(D)
        h_character = class_number_from_character(D)
        assert h_forms == h_character, (D, h_forms, h_character)
        if h_forms == 1:
            survivors.append(d)
    assert tuple(survivors) == EXPECTED, survivors
    print("Independent finite class-number routes: PASS")
    print("Fundamental negative discriminants audited:", fundamental_count)
    print("Class-number-one absolute discriminants:", survivors)


if __name__ == "__main__":
    certify_analytic_rationals()
    verify_finite_classification()
