"""Finite determinant/Smith-layer experiment; see flow/PREREG_LIFTS.txt.

No observed valuation surplus is used as a general lower bound. Different
witnesses and nested prime-power layers are never added as independent data.
"""
import json
import math
from fractions import Fraction

from flint import arb, ctx, fmpz_mat
from sympy import isprime, legendre_symbol, primerange

from green_h1 import F_exact
from green_h1_ellipse import upper_B
from verify_exact import gram, square


def valuation(n, p):
    if n == 0 or not isprime(p):
        raise ValueError("need a nonzero integer and a prime")
    n, exponent = abs(n), 0
    while n % p == 0:
        n //= p
        exponent += 1
    return exponent


def smith_layers(factors, p):
    """Counts at successive p-power levels; their SUM is the valuation."""
    if not factors or any(s <= 0 for s in factors) or not isprime(p):
        raise ValueError("need positive Smith factors and a prime")
    exponents = [valuation(s, p) for s in factors]
    return [sum(e >= k for e in exponents)
            for k in range(1, max(exponents) + 1)]


def pair_partition(G):
    """Greedy disjoint pairing for a positive definite integer Gram matrix."""
    size = len(G)
    candidates = []
    for i in range(size):
        for j in range(i + 1, size):
            diagonal = G[i][i] * G[j][j]
            block = diagonal - G[i][j] ** 2
            if diagonal <= 0 or block <= 0:
                raise ValueError("positive definite input required")
            candidates.append((Fraction(block, diagonal), i, j))
    unused = set(range(size))
    blocks = []
    for ratio, i, j in sorted(candidates):
        if ratio < 1 and i in unused and j in unused:
            blocks.append((i, j))
            unused.difference_update((i, j))
    return blocks + [(i,) for i in sorted(unused)]


def principal_product(G, blocks):
    """Product of principal minors; an upper bound only when G is PSD."""
    indices = [i for block in blocks for i in block]
    if (sorted(indices) != list(range(len(G)))
            or any(len(block) not in (1, 2) for block in blocks)):
        raise ValueError("blocks must partition all indices exactly once")
    product = 1
    for block in blocks:
        i = block[0]
        value = G[i][i]
        if len(block) == 2:
            j = block[1]
            value = value * G[j][j] - G[i][j] * G[j][i]
        if value <= 0:
            raise ValueError("positive principal blocks required")
        product *= value
    return product


def ellipse_points(D):
    """Exact integer points satisfying 4(x^2+D*y^2)<=9D."""
    radius = math.isqrt(9 * D // 4)
    return [(x, y) for y in (-1, 0, 1)
            for x in range(-radius, radius + 1)
            if 4 * (x * x + D * y * y) <= 9 * D]


def analyze(D, points, R, S, J):
    if (D <= 0 or R < 1 or S < 1 or J < 1 or not points
            or len(set(points)) != len(points)):
        raise ValueError("need positive parameters and distinct nonempty points")
    lines = {}
    for x, y in points:
        lines[y] = lines.get(y, 0) + 1
    sufficient = (J >= max(lines.values()) + len(lines)
                  and len(points) * J > 2 * R * S + J * (R + S))
    G = gram(points, R, S, J, D)
    matrix = fmpz_mat(G)
    rank = matrix.rank()
    d = int(matrix.det())
    result = {
        "D": D, "R": R, "S": S, "J": J, "points": len(points),
        "rows": R * S, "rank": rank, "independence_sufficient": sufficient,
        "strict_cutoff": 4 * R < D + 1,
    }
    if rank < R * S:
        assert d == 0 and not sufficient
        result["status"] = "singular; no finite logdet or valuation"
        return result
    # This is a trace Gram matrix in a positive definite real inner product.
    assert d > 0
    smith = matrix.snf()
    factors = [abs(int(smith[i, i])) for i in range(R * S)]
    assert all(factors) and math.prod(factors) == d
    assert all(b % a == 0 for a, b in zip(factors, factors[1:]))
    blocks = pair_partition(G)
    block = principal_product(G, blocks)
    hadamard = math.prod(G[i][i] for i in range(R * S))
    inert = [int(p) for p in primerange(3, R + 1)
             if legendre_symbol(-D, p) == -1]
    prime_data, lower_product = [], 1
    for p in inert:
        layers = smith_layers(factors, p)
        exponent, green = valuation(d, p), 2 * F_exact(p, R, S)
        assert sum(layers) == exponent and exponent >= green
        assert all(a >= b for a, b in zip(layers, layers[1:]))
        lower_product *= p ** green
        prime_data.append({"p": p, "green": green, "valuation": exponent,
                           "layers": layers, "surplus": exponent - green})
    assert lower_product <= d <= block <= hadamard
    B = max(arb(x * x + D * y * y).sqrt() for x, y in points)
    aggregate = upper_B(R, S, J, arb(len(points)), B)
    assert arb(hadamard).log() <= aggregate
    scale = R * R * S
    result.update({
        "status": "positive", "prime_layers": prime_data,
        "blocks": blocks, "block_strictly_better": block < hadamard,
        "smith_product_matches": True,
        "exact_chain": "inert_product <= det <= block_product <= diagonal_product",
        "normalized_gaps": {
            "exact": ((arb(d) / lower_product).log() / scale).str(12),
            "block": ((arb(block) / lower_product).log() / scale).str(12),
            "hadamard": ((arb(hadamard) / lower_product).log() / scale).str(12),
            "aggregate": ((aggregate - arb(lower_product).log()) / scale).str(12),
        },
        "normalized_block_gain": ((arb(hadamard) / block).log() / scale).str(12),
    })
    return result


def campaign():
    count = positive = improvements = sufficient = 0
    for D in (7, 19, 23, 43, 67, 163):
        for shape, points in (("square", square(3)), ("ellipse", ellipse_points(D))):
            lines = {}
            for x, y in points:
                lines[y] = lines.get(y, 0) + 1
            for R, S in ((4, 2), (6, 2), (9, 3)):
                for J in (1, 2, max(lines.values()) + len(lines)):
                    result = analyze(D, points, R, S, J)
                    result["shape"] = shape
                    print(json.dumps(result, sort_keys=True), flush=True)
                    count += 1
                    positive += result["status"] == "positive"
                    improvements += result.get("block_strictly_better", False)
                    sufficient += result["independence_sufficient"]
    print(json.dumps({
        "summary": {"cases": count, "positive": positive,
                    "singular": count - positive, "sufficient": sufficient,
                    "strict_block_improvements": improvements},
        "scope": "finite observations, not a universal valuation improvement",
    }, sort_keys=True))


if __name__ == "__main__":
    ctx.prec = 160
    campaign()
