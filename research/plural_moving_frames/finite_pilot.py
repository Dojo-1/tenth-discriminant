#!/usr/bin/env python3
"""Exact pre-registered pilots for moving-frame determinant profiles.

Research only: not a field-discriminant theorem. No third-party packages.
"""
from fractions import Fraction
from itertools import combinations
from math import gcd


def det(a):
    """Fraction-free Bareiss determinant of an integer matrix."""
    n = len(a)
    if n == 0:
        return 1
    b = [list(row) for row in a]
    sign, prev = 1, 1
    for k in range(n - 1):
        if b[k][k] == 0:
            pivot = next((i for i in range(k + 1, n) if b[i][k] != 0), None)
            if pivot is None:
                return 0
            b[k], b[pivot] = b[pivot], b[k]
            sign = -sign
        value = b[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = b[i][j] * value - b[i][k] * b[k][j]
                assert numerator % prev == 0, "Exact division failed"
                b[i][j] = numerator // prev
        for i in range(k + 1, n):
            b[i][k] = 0
        prev = value
    return sign * b[-1][-1]


def transpose(a):
    return [list(x) for x in zip(*a)]


def matmul(a, b):
    columns = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in columns] for row in a]


def divisor(a, k):
    n = len(a)
    g = 0
    for rows in combinations(range(n), k):
        for cols in combinations(range(n), k):
            g = gcd(g, abs(det([[a[i][j] for j in cols] for i in rows])))
    return g


def vp(n, p):
    assert n != 0
    n, e = abs(n), 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def real_jet_gram(samples):
    # Original ordinary Z-jets: rows 1 and Z; J=1; trace=2 Re.
    return [[2 * len(samples), 2 * sum(samples)],
            [2 * sum(samples), 2 * sum(x*x for x in samples)]]


def test_T1():
    a, b = real_jet_gram([1, 4]), real_jet_gram([1, 2, 4])
    assert a == [[4, 10], [10, 34]]
    assert b == [[6, 14], [14, 42]]
    assert det(a) == 36 and det(b) == 56
    assert vp(det(a), 3) == 2 and vp(det(b), 3) == 0
    # b-a = 2 * [1,2] * [1,2]^T is positive semidefinite.
    assert [[b[i][j] - a[i][j] for j in range(2)] for i in range(2)] == [[2, 4], [4, 8]]
    return {"small": a, "large": b, "determinants": [36, 56], "v3": [2, 0]}


def test_T2():
    p, exponents = 3, [0, 1, 2]
    middle = [[2, 1, 0], [1, 2, 1], [0, 1, 2]]
    diag = [[p**exponents[i] if i == j else 0 for j in range(3)] for i in range(3)]
    u = [[1, 1, 0], [0, 1, 1], [0, 0, 1]]
    inv = [[1, -1, 1], [0, 1, -1], [0, 0, 1]]
    identity = [[int(i == j) for j in range(3)] for i in range(3)]
    assert matmul(u, inv) == identity and det(u) == 1
    h = matmul(matmul(diag, middle), diag)
    g = matmul(matmul(inv, h), transpose(inv))
    assert matmul(matmul(u, g), transpose(u)) == h
    assert det(middle) == 4 and det(g) == 4 * p**6
    values = [divisor(g, k) for k in range(1, 4)]
    assert values == [divisor(h, k) for k in range(1, 4)]
    tau = [sum(sorted(exponents)[:k]) for k in range(1, 4)]
    assert tau == [0, 1, 3]
    assert all(values[k-1] % p**(2*tau[k-1]) == 0 for k in range(1, 4))
    return {"G": g, "divisors": values, "tau": tau, "v3": [vp(d, 3) for d in values]}


def test_T3():
    R, S, p = 4, 2, 3
    exponents = [min(r//p, S-1-s) for r in range(R) for s in range(S)]
    tau = [sum(sorted(exponents)[:k]) for k in range(1, R*S+1)]
    assert exponents == [0, 0, 0, 0, 0, 0, 1, 0]
    assert tau == [0, 0, 0, 0, 0, 0, 0, 1]
    return {"exponents": exponents, "tau": tau}


def test_T4():
    # det(U)=1, but U does not preserve the integral lattice.
    frame = [[Fraction(2), 0], [0, Fraction(1,2)]]
    gram = matmul(frame, transpose(frame))
    assert gram == [[4, 0], [0, Fraction(1,4)]]
    assert gram[0][0] * gram[1][1] == 1
    assert any(x.denominator != 1 for row in gram for x in row)
    return {"frame": [[str(x) for x in row] for row in frame],
            "gram": [[str(x) for x in row] for row in gram]}


if __name__ == "__main__":
    import json
    results = {"T1": test_T1(), "T2": test_T2(), "T3": test_T3(), "T4": test_T4()}
    print(json.dumps(results, indent=2, sort_keys=True))
    print("PASS: four exact finite pilots (not a universal proof)")
