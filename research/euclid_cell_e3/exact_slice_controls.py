#!/usr/bin/env python3
"""Exact E3 source-parameter lattice controls (standard-library only).

These are bounded tests, not a proof of the universal D>=14^4/300^4
claims. Rational threshold inequalities are checked independently of
any floating-point fourth root or plotted triangulation.
"""
from fractions import Fraction as F
from math import isqrt


def ceil_scaled_three_quarters(D: int, a: int, b: int) -> int:
    """ceil(a/b * D**(3/4)) via exact fourth-power comparisons."""
    assert D > 0 and 0 < a < b
    lo, hi = 0, D + 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if (b * mid) ** 4 >= a**4 * D**3:
            hi = mid
        else:
            lo = mid
    assert hi == 0 or (b * (hi - 1)) ** 4 < a**4 * D**3
    return hi


def ellipse_count(D: int, rho: int) -> int:
    assert D > 0 and rho >= 0
    Y = isqrt((rho * rho) // D)
    return 2 * rho + 1 + 2 * sum(
        2 * isqrt(rho * rho - D * y * y) + 1
        for y in range(1, Y + 1)
    )


def count_required(D: int) -> int:
    R = D // 4
    S = R // 25
    return 2 * (R - 1) + (S - 1)


def test_rational_barriers() -> None:
    # sqrt(D)=t^2 exactly; delta=(1+sqrt(D))/2.
    c14 = F(11, 25) - F(1, 28) - F(1, 2 * 14**3)
    c300 = F(81, 200) - F(1, 600) - F(1, 2 * 300**3)
    assert c14 == F(55443, 137200)
    assert F(157, 50) * c14**2 > F(51, 100)
    assert c300 > F(4033, 10000)
    assert F(157, 50) * F(4033, 10000)**2 > F(51, 100)
    # The cover needs rho >= delta: omitting it fails at D=1, rho=0.
    assert F(157, 50) * (F(0) - F(1))**2 > 1


def test_exact_slices() -> None:
    expected = {
        14: (23585, 19795),
        300: (4925304253, 4174269347),
        307: (5402763825, 4577892081),
        313: (5837373405, 4945461735),
    }
    for t, (old_expected, candidate_expected) in expected.items():
        D = t**4
        old = ceil_scaled_three_quarters(D, 11, 25)
        candidate = ceil_scaled_three_quarters(D, 81, 200)
        old_count = ellipse_count(D, old)
        candidate_count = ellipse_count(D, candidate)
        assert old_count == old_expected, (t, old_count)
        assert candidate_count == candidate_expected, (t, candidate_count)
        assert candidate_count > count_required(D)
        assert old_count > candidate_count
        print(f"t={t} D={D}: original={old_count}, candidate={candidate_count}, "
              f"required={count_required(D)}")
    # Counterworld: shrinking to 0.400 D^(3/4) breaks the count at t=300.
    D = 300**4
    too_small = ceil_scaled_three_quarters(D, 2, 5)
    assert ellipse_count(D, too_small) < count_required(D)


if __name__ == "__main__":
    test_rational_barriers()
    test_exact_slices()
    print("E3 exact controls passed (finite, not universal).")
