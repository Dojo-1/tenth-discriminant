"""Moment-only Fischer bounds; derivation and limits in ledger/radial_bounds.txt."""
import json
import math
from fractions import Fraction

from flint import arb, ctx
from sympy import legendre_symbol, primerange

from green_h1 import F_exact


def radial_moments(D, points, degree):
    if D <= 0 or degree < 0 or not points or len(set(points)) != len(points):
        raise ValueError("need D>0, degree>=0 and distinct nonempty points")
    moments = [0] * (degree + 1)
    for x, y in points:
        t, power = x * x + D * y * y, 1
        for k in range(degree + 1):
            moments[k] += power
            power *= t
    return moments


def diagonal(moments, r, s, J):
    if min(r, s) < 0 or J < 1 or len(moments) <= r + s:
        raise ValueError("invalid row, derivative order or moment degree")
    return 2 * sum(math.perm(r, j) ** 2 * moments[r + s - j]
                   for j in range(min(r, J - 1) + 1))


def cross(moments, r, s, J):
    """Inner product of (r,s) and (r+1,s+1), including all shared columns."""
    if min(r, s) < 0 or J < 1 or len(moments) <= r + s + 1:
        raise ValueError("invalid row, derivative order or moment degree")
    return 2 * sum(math.perm(r, j) * math.perm(r + 1, j) * moments[r + s + 1 - j]
                   for j in range(min(r, J - 1) + 1))


def correlation_ratio_bound(a, b, r, J):
    """Upper bound on block/(diagonal product), not on the correlation."""
    if not (0 < a <= b and J >= 1 and r >= J - 1):
        raise ValueError("need 0<a<=b and r>=J-1")
    K = Fraction(b * (r + 1), a * (r + 2 - J))
    return ((K - 1) / (K + 1)) ** 2


def radial_partition(R, S, J):
    if min(R, S, J) < 1:
        raise ValueError("positive dimensions and derivative order required")
    unused = set((r, s) for r in range(R) for s in range(S))
    pairs = []
    for r in range(2 * (J - 1), R - 1):
        for s in range(S - 1):
            first, second = (r, s), (r + 1, s + 1)
            if first in unused and second in unused:
                pairs.append((first, second))
                unused.difference_update((first, second))
    return pairs, sorted(unused)


def annulus_points(D):
    if D < 1:
        raise ValueError("need D>=1")
    radius2 = 36 * D
    return [(x, y) for y in range(-6, 7)
            for x in range(-math.isqrt(radius2 - D * y * y),
                           math.isqrt(radius2 - D * y * y) + 1)
            if 2 * (x * x + D * y * y) >= radius2]


def certify_radial(D, points, R, S, J):
    if D <= 0 or min(R, S, J) < 1 or not points or len(set(points)) != len(points):
        raise ValueError("need positive parameters and distinct nonempty points")
    radii = [x * x + D * y * y for x, y in points]
    a, b = min(radii), max(radii)
    if a <= 0 or 2 * a < b:
        raise ValueError("need a positive annulus with max radius squared <=2*min")
    lines = {}
    for x, y in points:
        lines[y] = lines.get(y, 0) + 1
    sufficient = (J >= max(lines.values()) + len(lines)
                  and len(points) * J > 2 * R * S + J * (R + S))
    result = {"D": D, "R": R, "S": S, "J": J, "rows": R * S,
              "points": len(points), "radius_squared": [a, b],
              "independence_sufficient": sufficient, "strict_cutoff": 4 * R < D + 1}
    if not sufficient:
        result["status"] = "no certificate; sufficient rank condition failed"
        return result
    moments = radial_moments(D, points, R + S - 2)
    diagonals = {(r, s): diagonal(moments, r, s, J)
                 for r in range(R) for s in range(S)}
    pairs, singles = radial_partition(R, S, J)
    covered = [row for pair in pairs for row in pair] + singles
    assert len(covered) == R * S and set(covered) == set(diagonals)
    hadamard = math.prod(diagonals.values())
    blocks = math.prod(diagonals[row] for row in singles)
    for (r, s), other in pairs:
        product = diagonals[r, s] * diagonals[other]
        minor = product - cross(moments, r, s, J) ** 2
        ratio = correlation_ratio_bound(a, b, r, J)
        assert 0 < minor and minor * ratio.denominator <= product * ratio.numerator
        assert ratio <= Fraction(9, 25)
        blocks *= minor
    count = len(pairs)
    assert blocks * 25 ** count <= hadamard * 9 ** count
    # Actual inert primes only: this is not an h=1 inertness assumption.
    lower = math.prod(int(p) ** (2 * F_exact(int(p), R, S))
                      for p in primerange(3, R + 1) if legendre_symbol(-D, p) == -1)
    assert lower <= blocks <= hadamard
    guaranteed = arb(count) * (arb(25) / 9).log()
    scale = R * R * S
    result.update({
        "status": "certified by sufficient rank and moment identities",
        "pairs": count,
        "normalized_gaps": {
            "moment_block": ((arb(blocks) / lower).log() / scale).str(12),
            "uniform_block": (((arb(hadamard) / lower).log() - guaranteed) / scale).str(12),
            "hadamard": ((arb(hadamard) / lower).log() / scale).str(12),
        },
        "normalized_gain": {
            "moment": ((arb(hadamard) / blocks).log() / scale).str(12),
            "guaranteed": (guaranteed / scale).str(12),
        },
        "chain": "inert_product <= det G <= moment_block <= uniform_block <= Hadamard",
    })
    return result


def campaign():
    cases = certified = improvements = 0
    for D in (19, 43, 163):
        points = annulus_points(D)
        lines = {}
        for x, y in points:
            lines[y] = lines.get(y, 0) + 1
        J = max(lines.values()) + len(lines)
        for R in (64, 128, 256):
            for S in (2, 4):
                result = certify_radial(D, points, R, S, J)
                print(json.dumps(result, sort_keys=True), flush=True)
                cases += 1
                certified += result["independence_sufficient"]
                improvements += result.get("pairs", 0) > 0
    print(json.dumps({"summary": {"cases": cases, "certified": certified,
                                "strict_improvements": improvements},
                      "scope": "uniform guaranteed normalized gain is O(1/R), not a new slope"},
                     sort_keys=True))


if __name__ == "__main__":
    ctx.prec = 160
    campaign()
