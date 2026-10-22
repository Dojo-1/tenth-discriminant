#!/usr/bin/env python3
"""Finite exact controls for trace-Gram semantics, not a proof of the universal bound.

Uses only the standard library. Gaussian-integer rows exercise D=1 and avoid
floating-point tolerances. Same-author checking is not independent peer review.
"""
from fractions import Fraction
from math import factorial, prod
import json
import random


def mul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def power(z, n):
    result = (1, 0)
    for _ in range(n):
        result = mul(result, z)
    return result


def derivative(r, s, j, z):
    if j > r:
        return (0, 0)
    scale = factorial(r) // factorial(r - j)
    w = mul(power(z, r - j), power((z[0], -z[1]), s))
    return (scale * w[0], scale * w[1])


def gram(points, order, labels):
    columns = [(j, z) for j in range(order) for z in points]
    rows = [[derivative(r, s, j, z) for j, z in columns] for r, s in labels]
    entries = [[2 * sum(mul(a, (b[0], -b[1]))[0] for a, b in zip(u, v))
                for v in rows] for u in rows]
    return entries, rows


def determinant(a):
    b = [list(map(Fraction, row)) for row in a]
    result = Fraction(1)
    for i in range(len(b)):
        p = next((j for j in range(i, len(b)) if b[j][i]), None)
        if p is None:
            return Fraction(0)
        if p != i:
            b[i], b[p] = b[p], b[i]
            result = -result
        pivot = b[i][i]
        result *= pivot
        for j in range(i + 1, len(b)):
            ratio = b[j][i] / pivot
            for k in range(i + 1, len(b)):
                b[j][k] -= ratio * b[i][k]
    return result


def check_case(points, order, labels, coeffs):
    g, rows = gram(points, order, labels)
    n = len(labels)
    det = determinant(g)
    diagprod = prod(g[i][i] for i in range(n))
    assert 0 <= det <= diagprod
    quadratic = sum(coeffs[i] * g[i][j] * coeffs[j] for i in range(n) for j in range(n))
    squares = 0
    for c in range(len(points) * order):
        real = sum(coeffs[i] * rows[i][c][0] for i in range(n))
        imag = sum(coeffs[i] * rows[i][c][1] for i in range(n))
        squares += 2 * (real * real + imag * imag)
    assert quadratic == squares and quadratic >= 0
    reversed_g, _ = gram(points[::-1], order, labels)
    assert reversed_g == g
    permuted_g, _ = gram(points, order, labels[::-1])
    assert determinant(permuted_g) == det
    full_order = max([r for r, _ in labels], default=0) + 1
    if order >= full_order:
        extended_g, _ = gram(points, order + 1, labels)
        assert extended_g == g
    return int(det), int(diagprod)


def main():
    if not __debug__:
        raise SystemExit('Run without -O: exact controls require assertions to be enabled.')
    known = [
        ('single_origin', [(0, 0)], 2, [(0, 0)], [1], 2),
        ('duplicate_rows', [(0, 0)], 2, [(0, 0), (0, 0)], [1, -1], 0),
        ('unmatched_column', [(1, 0)], 2, [(0, 0), (1, 1)], [2, -1], 4),
        ('zero_derivatives', [(1, 0)], 0, [(0, 0), (1, 0)], [1, 1], 0),
        ('empty_points', [], 2, [(0, 0)], [1], 0),
        ('empty_rows', [(0, 0)], 2, [], [], 1),
    ]
    records = []
    for name, points, order, labels, coeffs, expected in known:
        det, diag = check_case(points, order, labels, coeffs)
        assert det == expected
        records.append({'case': name, 'determinant': det, 'diagonal_product': diag})
    rng = random.Random(20261022)
    grid = [(x, y) for x in range(-2, 3) for y in range(-2, 3)]
    for _ in range(64):
        points = rng.sample(grid, rng.randrange(7))
        labels = [(rng.randrange(4), rng.randrange(3)) for _ in range(rng.randrange(6))]
        check_case(points, rng.randrange(5), labels, [rng.randrange(-2, 3) for _ in labels])
    assert records[1]['determinant'] == 0
    assert records[2]['determinant'] == 4 != 0
    print(json.dumps({'known_cases': records, 'seeded_cases': 64, 'seed': 20261022,
                      'status': 'PASS', 'scope': 'finite exact controls only'}, indent=2))

if __name__ == '__main__':
    main()
