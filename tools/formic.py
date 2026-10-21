"""FORMIC: local, adversarial checks of the Ender proof interfaces.

Exact controls complement, but do not replace, the mathematical proof.
"""
import math
import re
from pathlib import Path

from flint import arb, ctx
from sympy import primerange

from ender import (
    P, CS, asymptotic, certify, factorial_lower, floor_sum, integer,
    prime_mass, tail_integral,
)
from green_h1 import F_exact


ROOT = Path(__file__).resolve().parents[1]


def reference_F(p, R, S):
    return sum((S - i) * (R - i * p)
               for i in range(1, min(S - 1, (R - 1) // p) + 1))


def arithmetic():
    controls = 0
    mutations = set()
    for R in range(2, 81):
        product = math.prod(math.factorial(r) for r in range(1, R))
        lower = factorial_lower(R)
        if R > 2:
            assert lower < arb(product).log()
        else:
            assert lower == 0
        reconstruction = 1
        for p in primerange(2, R):
            exponent, q = 0, p
            while q < R:
                direct = sum(r // q for r in range(R))
                assert floor_sum(R, q) == direct
                exponent += direct
                q *= p
            reconstruction *= p ** exponent
        assert reconstruction == product
        if arb(product).log() < lower + R * R:
            mutations.add("superfactorial lower bound strengthened")
        for S in (2, 3, max(2, R // 4)):
            if S > R:
                continue
            for p in primerange(2, R + 1):
                direct = sum(min(r // p, t) for r in range(R) for t in range(S))
                assert reference_F(p, R, S) == direct == F_exact(p, R, S)
                controls += 1
            actual = 2 * sum((arb(p).log() * reference_F(p, R, S)
                              for p in primerange(3, R + 1)), arb(0))
            claimed = prime_mass(R, S)
            assert actual.overlaps(claimed)
            if claimed + R * R * S > actual:
                mutations.add("prime-mass lower bound strengthened")
    for R in (P + 101, 2 * P + 3, 8 * P + 1):
        for C in CS:
            S = R // C
            actual = 2 * sum((arb(p).log() * reference_F(p, R, S)
                              for p in primerange(3, R + 1)), arb(0))
            assert prime_mass(R, S) < actual
            controls += 1
    for cutoff in (1, 2, 10, P):
        partial = sum((arb(m).log() / (m * (m - 1))
                       for m in range(cutoff + 1, cutoff + 1000)), arb(0))
        assert partial < tail_integral(cutoff)
    assert len(mutations) == 2
    print(f"arithmetic controls={controls}; mutation controls={sorted(mutations)}")


def geometry():
    count = 0
    for D in (3, 7, 11, 19, 43, 67, 163, 997):
        for radius in range(1, 41):
            n = sum(2 * math.isqrt(radius * radius - D * y * y) + 1
                    for y in range(-math.isqrt(radius * radius // D),
                                   math.isqrt(radius * radius // D) + 1))
            sd, rho = arb(D).sqrt(), arb(radius)
            area = arb.pi() * rho * rho / sd
            M = 2 * math.isqrt(radius * radius // D) + 1
            assert area - 2 * rho / sd - 6 * rho < n
            assert area + 2 * rho + M > n
            count += 1
    print(f"integer-radius ellipse controls={count}")


def small_discriminants():
    survivors = []
    for D in range(3, 92):
        m = D if D % 4 == 3 else D // 4
        fundamental = D % 4 == 3 or (D % 4 == 0 and m % 4 in (1, 2))
        if not fundamental or any(m % (p * p) == 0 for p in range(2, math.isqrt(m) + 1)):
            continue
        forms = []
        for a in range(1, math.isqrt(D // 3) + 1):
            for b in range(-a, a + 1):
                if (b * b + D) % (4 * a):
                    continue
                c = (b * b + D) // (4 * a)
                if c < a or (b < 0 and (abs(b) == a or a == c)):
                    continue
                if math.gcd(math.gcd(a, b), c) == 1:
                    forms.append((a, b, c))
        assert forms
        if len(forms) == 1:
            survivors.append(D)
    assert survivors == [3, 4, 7, 8, 11, 19, 43, 67]
    print(f"fundamental discriminants below 92 with one reduced form: {survivors}")


def coverage():
    path = ROOT / "ledger" / "coverage_ender.txt"
    previous, count = 700000000000, 0
    lines = path.read_text().splitlines()
    for line in lines[:-1]:
        match = re.fullmatch(r"CERTIFIED \[(\d+), (\d+)\] C=(\d+) margin=.*", line)
        assert match, f"invalid certificate line: {line}"
        start, stop, C = map(int, match.groups())
        assert start == previous and start < stop and C in CS
        assert 4 * (start // 4) < start + 1
        assert certify(start, stop, C)[0]
        previous = stop
        count += 1
    assert previous == 10**36 and count > 0
    assert lines[-1] == f"COMPLETE intervals={count} end={10**36}"
    print(f"contiguous coverage rechecked: {count} intervals")
    assert integer("1e36") == 10**36
    assert integer("1000000000000000000000000000000000001") == 10**36 + 1
    assert certify(700000000000, 700000000001, 20)[0]
    assert certify(10**36 - 1, 10**36, 80)[0]


if __name__ == "__main__":
    ctx.prec = 160
    arithmetic()
    geometry()
    small_discriminants()
    coverage()
    assert asymptotic()
    print("FORMIC: all controls passed (not a formal proof).")
