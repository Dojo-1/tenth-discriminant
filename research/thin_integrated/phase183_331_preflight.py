#!/usr/bin/env python3
"""Phase183: exact-rational bounded preflight for 331 as fourth-root target.

Necessary scalar and geometric checks only. No field-discriminant theorem,
determinant inequality, Lean certification, new prime or floating-point gate.
"""
from __future__ import annotations
from fractions import Fraction as F


def odd_prefix(z: F, n: int = 5) -> F:
    assert 0 <= z < 1 and n >= 1
    return sum((2 * z ** (2 * k + 1) / (2 * k + 1)
                for k in range(n)), F(0))


def odd_remainder(z: F, n: int = 5) -> F:
    assert 0 <= z < 1 and n >= 1
    return 2 * z ** (2 * n + 1) / ((2 * n + 1) * (1 - z * z))


def positive_binary_log_enclosure(x: int, k: int = 8, n: int = 5) -> tuple[F, F]:
    """Rational bounds matching LogEnclosure.lean's proven series and remainder."""
    assert x > 0 and 2 ** k <= x < 2 ** (k + 1)
    z = F(x - 2 ** k, x + 2 ** k)
    z2 = F(1, 3)
    lo = k * odd_prefix(z2, n) + odd_prefix(z, n)
    hi = k * (odd_prefix(z2, n) + odd_remainder(z2, n))
    hi += odd_prefix(z, n) + odd_remainder(z, n)
    assert 0 < lo <= hi
    return lo, hi


def normalized_gap(u: F, log_two: F) -> F:
    """Existing unstrengthened lower minus upper on the SAME original Gram."""
    return ((F(999997, 1000000) - F(4, 5)) * u
            - F(5739, 1000) + F(1849, 2000) + log_two / 4)


def report(label: str, value: F) -> None:
    print(f"{label}: exact={value.numerator}/{value.denominator}, "
          f"decimal={float(value):.12f}", flush=True)


def main() -> None:
    t = 331
    log331 = positive_binary_log_enclosure(t)
    assert log331[0] >= F(5802, 1000)
    assert log331[1] <= F(5803, 1000)
    log330 = positive_binary_log_enclosure(330)
    assert log330[0] >= F(5799, 1000)
    assert log330[1] <= F(5800, 1000)
    log2 = positive_binary_log_enclosure(2, 1)
    assert log2[0] >= F(6931, 10000)
    assert log2[1] <= F(6932, 10000)

    # The unchanged 51%-channel bound and existing pi > 3.14 suffice.
    pi_floor = F(314, 100)
    a = F(407, 1000)
    pi_margin = pi_floor * a * a - F(51, 100)
    cell_margin = (F(11, 25) - F(1001, 1000) * a) * t - 10
    assert pi_margin > 0 and cell_margin > 0
    # Old 413/1000 coefficient fails in the 331-domain.
    assert (F(11, 25) - F(1001, 1000) * F(413, 1000)) * t - 10 < 0

    # 4*floor(D/4) >= D-3; 80-cube guard follows from t^3*(t-320)>=3.
    floor_margin = t ** 3 * (t - 320) - 3
    assert floor_margin > 0
    assert t ** 3 * (t - 360) - 3 < 0  # old 90-cube premise fails

    endpoint_sum = F(521, 80000) + F(1, 9000)
    assert endpoint_sum < F(1, 100)
    # The log(D)/R <= 1/9000 premise still requires a new Lean-domain proof.

    gap331 = normalized_gap(4 * F(5802, 1000), F(6931, 10000))
    assert gap331 > 0
    assert gap331 < F(98, 1000)  # old optional +0.098 is false here

    gap330_max = normalized_gap(4 * F(5800, 1000), F(6932, 10000))
    assert gap330_max < 0
    assert t ** 4 == 12003612721

    report("PI_MULTIPLICATIVE_MARGIN", pi_margin)
    report("CELL_COUNT_MARGIN_AT_331", cell_margin)
    report("RADIUS_ERROR_SUM_UPPER", endpoint_sum)
    report("AFFINE_GAP_LOWER_AT_331", gap331)
    report("AFFINE_GAP_UPPER_AT_330", gap330_max)
    report("LOG_331_LOWER", log331[0])
    report("LOG_331_UPPER", log331[1])
    print("PHASE183_PREFLIGHT_PASS: finite necessary inequalities only; "
          "no original-Gram field theorem yet", flush=True)


if __name__ == "__main__":
    main()
