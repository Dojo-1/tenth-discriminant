"""Phase323 finite source check, independent of the Lean proof script.

Checks the true ordinary-Z derivatives of a bidirectional binary-null
polynomial against the original integer-pair row action. All operations
are exact, using Python integers. This is bounded M evidence, not a
uniform determinant theorem.
"""
from __future__ import annotations

from functools import lru_cache
from math import comb, factorial
import unittest

Pair = tuple[int, int]


def add(a: Pair, b: Pair) -> Pair:
    return a[0] + b[0], a[1] + b[1]


def scale(n: int, a: Pair) -> Pair:
    return n * a[0], n * a[1]


def mul(D: int, a: Pair, b: Pair) -> Pair:
    return a[0] * b[0] - D * a[1] * b[1], a[0] * b[1] + a[1] * b[0]


@lru_cache(maxsize=None)
def power(D: int, a: Pair, n: int) -> Pair:
    assert n >= 0
    result, base = (1, 0), a
    while n:
        if n & 1:
            result = mul(D, result, base)
        base = mul(D, base, base)
        n >>= 1
    return result


def falling(n: int, j: int) -> int:
    return factorial(n) // factorial(n - j) if j <= n else 0


def original_ordinary_jet(D: int, z: Pair, w: Pair,
                          r: int, s: int, j: int) -> Pair:
    if j > r:
        return 0, 0
    return scale(falling(r, j), mul(D, power(D, z, r - j),
                                   power(D, w, s)))


def double_matrix_row(D: int, z: Pair, w: Pair,
                      r: int, s: int, j: int) -> Pair:
    """Explicit U_Z U_W on the unchanged ordinary jets."""
    k, ell = r // 4, s // 4
    answer = 0, 0
    for t in range(k + 1):
        for u in range(ell + 1):
            coefficient = (-1) ** (t + u) * comb(k, t) * comb(ell, u)
            answer = add(answer, scale(coefficient,
                original_ordinary_jet(D, z, w, r - 2*t, s - 2*u, j)))
    return answer


def polynomial_derivative(D: int, z: Pair, w: Pair,
                          r: int, s: int, j: int) -> Pair:
    """Independent polynomial multiplication and differentiation.

    Start with X^(r-4k), multiply by (X^4-X^2) k times,
    differentiate by ordinary falling factorial, and multiply by
    W^(s-4ell) (W^4-W^2)^ell (constant in X).
    """
    k, ell = r // 4, s // 4
    coefficients = {r - 4*k: 1}
    for _ in range(k):
        nxt: dict[int, int] = {}
        for degree, coef in coefficients.items():
            nxt[degree + 4] = nxt.get(degree + 4, 0) + coef
            nxt[degree + 2] = nxt.get(degree + 2, 0) - coef
        coefficients = nxt

    null_w = add(power(D, w, 4), scale(-1, power(D, w, 2)))
    const = mul(D, power(D, w, s - 4*ell), power(D, null_w, ell))
    total = (0, 0)
    for degree, coef in coefficients.items():
        if j <= degree:
            total = add(total, scale(coef * falling(degree, j),
                mul(D, power(D, z, degree - j), const)))
    return total


class BidirectionalBinaryPilot(unittest.TestCase):
    def test_all_86400_original_source_cases(self) -> None:
        n = 0
        strict_two_factor_cases = 0
        for D in (2, 3, 163):
            for x in range(-2, 3):
                for y in range(-2, 3):
                    z, w = (x, y), (x, -y)
                    for r in range(12):
                        for s in range(12):
                            e = r // 4 + s // 4
                            for j in range(8):
                                actual = double_matrix_row(D, z, w, r, s, j)
                                direct = polynomial_derivative(D, z, w, r, s, j)
                                self.assertEqual(actual, direct,
                                    (D, x, y, r, s, j))
                                self.assertEqual(actual[0] % (2**e), 0,
                                    (D, x, y, r, s, j))
                                self.assertEqual(actual[1] % (2**e), 0,
                                    (D, x, y, r, s, j))
                                n += 1
                                if e >= 2:
                                    strict_two_factor_cases += 1
        self.assertEqual(n, 86400)
        self.assertEqual(strict_two_factor_cases, 57600)

    def test_bad_quadratic_W_null_rejected(self) -> None:
        w = (0, -1)
        wrong = add(power(3, w, 2), scale(-1, w))
        self.assertNotEqual(wrong[1] % 2, 0)

    def test_separate_two_adic_divisors_do_not_add(self) -> None:
        self.assertEqual(4 % (2**2), 0)
        self.assertEqual(4 % (2**2), 0)
        self.assertNotEqual(4 % (2**4), 0)


if __name__ == "__main__":
    unittest.main()
