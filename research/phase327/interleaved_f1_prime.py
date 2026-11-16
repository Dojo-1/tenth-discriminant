#!/usr/bin/env python3
"""Phase327 — signed F1-like carrier and two orthogonal spin-frame clocks.

NO ordinary field of characteristic one is asserted.
The proposed signed pointed-monoid presentation has group Q8 x H_D,
a zero, and a marked central sign s. Its *integral linearization* is

  A_D = Z[Q8 x H_D]/(s + 1)  ~=  LipschitzQuaternion_Z tensor Z[H_D].

The arithmetic coefficient fibers F_ell tensor_Z A_D are not all
fields, and the characteristic-2 fiber loses the scalar sign.

All executable controls below are exact integer/quaternion arithmetic.
The 360 x 360 sweep indexes COUNTS OF ORTHOGONAL HALF-TURN PULSES,
not a false exact one-degree trigonometric model. Separate assertions
check one and two complete 360-degree turns in Spin(3).

No new discriminant bound or integral action on the original jet Gram.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import gcd
from collections import defaultdict

Q = tuple[int, int, int, int]
ZERO: Q = (0, 0, 0, 0)
ONE: Q = (1, 0, 0, 0)
NEG_ONE: Q = (-1, 0, 0, 0)
I: Q = (0, 1, 0, 0)
J: Q = (0, 0, 1, 0)
K: Q = (0, 0, 0, 1)
BASIS: tuple[Q, ...] = (ONE, I, J, K)
Q8: tuple[Q, ...] = (ONE, NEG_ONE, I, tuple(-x for x in I),
                          J, tuple(-x for x in J),
                          K, tuple(-x for x in K))
RAY_GROUP_ORDERS = {163: 7500, 187: 15000, 203: 30000}


def add(a: Q, b: Q) -> Q:
    return tuple(a[t] + b[t] for t in range(4))  # type: ignore[return-value]


def scale(c: int, a: Q) -> Q:
    return tuple(c * a[t] for t in range(4))  # type: ignore[return-value]


def product(a: Q, b: Q) -> Q:
    """Integral Hamilton product; no floating precision assumptions."""
    x, y, z, w = a
    u, v, t, s = b
    return (
        x * u - y * v - z * t - w * s,
        x * v + y * u + z * s - w * t,
        x * t - y * s + z * u + w * v,
        x * s + y * t - z * v + w * u,
    )


def conjugate(a: Q) -> Q:
    return (a[0], -a[1], -a[2], -a[3])


def norm(a: Q) -> int:
    return product(a, conjugate(a))[0]


def scalar_inner(a: Q, b: Q) -> int:
    return product(a, conjugate(b))[0]


def reduce_mod(a: Q, characteristic: int) -> Q:
    if characteristic < 2:
        raise ValueError("Coefficient characteristic must be a prime >= 2")
    return tuple(x % characteristic for x in a)  # type: ignore[return-value]


def product_mod(a: Q, b: Q, characteristic: int) -> Q:
    return reduce_mod(product(a, b), characteristic)


def power(a: Q, exponent: int) -> Q:
    if exponent < 0:
        raise ValueError("Use a group inverse for negative exponents")
    r = ONE
    base = a
    while exponent:
        if exponent & 1:
            r = product(r, base)
        base = product(base, base)
        exponent //= 2
    return r


def moving_frame(u: Q, a: Q) -> Q:
    """Conjugation by a unit quaternion (norm u=1), exact."""
    if norm(u) != 1:
        raise ValueError("Frame must be a norm-one quaternion")
    return product(product(u, a), conjugate(u))


def quaternion_basis_product(a: int, b: int) -> tuple[int, int]:
    if a not in range(4) or b not in range(4):
        raise ValueError("Quaternion basis index outside 0,1,2,3")
    v = product(BASIS[a], BASIS[b])
    nonzero = [(t, z) for t, z in enumerate(v) if z]
    assert len(nonzero) == 1 and abs(nonzero[0][1]) == 1
    t, sign = nonzero[0]
    return sign, t


def small_group_algebra_product(
    a: dict[tuple[int, int], int],
    b: dict[tuple[int, int], int],
    group_order: int,
    characteristic: int | None = None,
) -> dict[tuple[int, int], int]:
    """Toy shadow of A_D with H=C_n. Not a reconstruction of H_D."""
    if group_order < 1:
        raise ValueError("Must have nonempty finite group")
    out: defaultdict[tuple[int, int], int] = defaultdict(int)
    for (qa, ga), va in a.items():
        for (qb, gb), vb in b.items():
            assert 0 <= ga < group_order and 0 <= gb < group_order
            sign, qc = quaternion_basis_product(qa, qb)
            out[(qc, (ga + gb) % group_order)] += va * vb * sign
    if characteristic is not None:
        return {k: v % characteristic for k, v in out.items()
                if v % characteristic}
    return {k: v for k, v in out.items() if v}


def crt_2_7(a: int, b: int) -> int:
    """CRT element mod 14, 7=a-selector mod 2, 8=b-selector mod 7."""
    return (7 * (a % 2) + 8 * (b % 7)) % 14


def is_prime(p: int) -> bool:
    if p < 2:
        return False
    for q in range(2, int(p ** 0.5) + 1):
        if p % q == 0:
            return False
    return True


@dataclass(frozen=True)
class FrobeniusPrime:
    """Rational prime whose splitting is studied; distinct from ell."""
    p: int

    def __post_init__(self) -> None:
        if not is_prime(self.p):
            raise ValueError("Frobenius label must be a prime")


@dataclass(frozen=True)
class CoefficientPrime:
    """Prime characteristic of the coefficient fiber F_ell."""
    ell: int

    def __post_init__(self) -> None:
        if not is_prime(self.ell):
            raise ValueError("Finite coefficient fiber requires prime ell")


@dataclass(frozen=True)
class RayConductor:
    """Integer conductor for the ray-class group, never a coefficient."""
    modulus: int

    def __post_init__(self) -> None:
        if self.modulus < 1:
            raise ValueError("Ray conductor must be positive")


def typed_prime_context(
    p: FrobeniusPrime,
    ell: CoefficientPrime,
    m: RayConductor,
    D: int,
) -> tuple[int, int, int]:
    if not isinstance(p, FrobeniusPrime) or not isinstance(ell, CoefficientPrime):
        raise TypeError("Do not mix Frobenius prime p and coefficient prime ell")
    if not isinstance(m, RayConductor):
        raise TypeError("Ray conductor is a third, independent parameter")
    if gcd(p.p, D * m.modulus) != 1:
        raise ValueError("Arithmetic Frobenius requires unramified p coprime to conductor")
    return (p.p, ell.ell, m.modulus)


def semisimple_group_algebra_characteristic(D: int, ell: CoefficientPrime) -> bool:
    """Checks Maschke's divisibility hypothesis, not a proof of semisimplicity."""
    return (2 * RAY_GROUP_ORDERS[D]) % ell.ell != 0


def two_full_turn_spin_signs() -> tuple[Q, Q, Q, Q]:
    """A 180-degree SO3 turn lifts to i or j in Spin3.

    Thus a 360-degree turn is i^2=j^2=-1 and two full turns
    (720 degrees) give i^4=j^4=+1.
    """
    return power(I, 2), power(J, 2), power(I, 4), power(J, 4)


def orthogonal_half_turn_word_counts() -> dict[str, int]:
    """360x360 exact sweep of half-turn PULSE COUNTS (a,b), not degrees.

    i^a j^b = (-1)^(a*b) j^b i^a.  This should never be
    generalized to commuting arbitrary partial-angle SO3 rotations.
    """
    pa = [power(I, a) for a in range(4)]
    pb = [power(J, b) for b in range(4)]
    commute = anti = 0
    for a in range(360):
        iword = pa[a % 4]
        for b in range(360):
            jword = pb[b % 4]
            lhs = product(iword, jword)
            rhs = product(jword, iword)
            sign = -1 if (a % 2 and b % 2) else 1
            assert lhs == scale(sign, rhs), (a, b)
            assert reduce_mod(lhs, 2) == reduce_mod(rhs, 2)
            assert reduce_mod(lhs, 7) == reduce_mod(scale(sign, rhs), 7)
            if sign == -1:
                assert lhs != rhs
                anti += 1
            else:
                assert lhs == rhs
                commute += 1
    assert anti + commute == 360 * 360
    return {"pairs": 360 * 360,
            "anticommuting_pairs": anti,
            "commuting_pairs": commute}
