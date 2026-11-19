#!/usr/bin/env python3
"""E40: exact, bounded oracle for original J=1, R=2, S=1 trace Gram.

This script is an independent integer implementation of the original
ordinary-Z-jet trace definition on two distinct lattice points.
It is NOT a Lean proof, field-discriminant bound, or geometric lift.

Run: python3 research/e40_original_gram_oracle.py
"""
from itertools import product
import json

DS = (1, 2, 5)
COORDS = range(-2, 3)
REAL_COORDS = range(-10, 11)
TRANSLATIONS = range(-5, 6)


def transpose(M):
    return [list(row) for row in zip(*M)]


def matmul(A, B):
    return [
        [sum(A[i][k] * B[k][j] for k in range(len(B)))
         for j in range(len(B[0]))]
        for i in range(len(A))
    ]


def det2(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


def original_pair_trace(D, a, b):
    # Original positive 2 * (real-real + D * imag-imag) pairing.
    return 2 * (a[0] * b[0] + D * a[1] * b[1])


def original_gram(D, z1, z2):
    assert z1 != z2, "original Finset collapses duplicate samples"
    # Original ordinary Z-jet rows are 1 and Z at j=0.
    e = (((1, 0), z1), ((1, 0), z2))
    # Sum over both original sample points; no matrix shortcut.
    return [[sum(original_pair_trace(D, e[k][i], e[k][j])
                 for k in range(2)) for j in range(2)] for i in range(2)]


def test_real_translation():
    cases = 0
    for x, y, c in product(REAL_COORDS, REAL_COORDS, TRANSLATIONS):
        if x == y:
            continue
        G = original_gram(1, (x, 0), (y, 0))
        assert det2(G) == 4 * (y - x) ** 2
        U = [[1, 0], [-c, 1]]
        shifted = original_gram(1, (x + c, 0), (y + c, 0))
        assert matmul(matmul(U, shifted), transpose(U)) == G
        assert det2(U) == 1
        cases += 1
    return cases


def test_complex_source():
    tested = naive_false = naive_true = 0
    for D in DS:
        for x, y, u, v in product(COORDS, repeat=4):
            if (x, y) == (u, v):
                continue
            G = original_gram(D, (x, y), (u, v))
            actual = det2(G)
            source_exact = 4 * ((x - u)**2 + D*(y - v)**2 + D*(y + v)**2)
            naive = 4 * ((x - u)**2 + D*(y - v)**2)
            assert actual == source_exact
            assert actual >= naive
            naive_false += actual != naive
            naive_true += actual == naive
            tested += 1
    return tested, naive_false, naive_true


def test_fake_transport():
    U = [[1, 0], [-1, 1]]
    V = [[1, 0], [0, 5]]
    Gshift = original_gram(25, (1, 0), (6, 0))
    Gunit = original_gram(25, (0, 0), (1, 0))
    GU = matmul(matmul(U, Gshift), transpose(U))
    GV = matmul(matmul(V, Gunit), transpose(V))
    assert GU == GV == [[4, 10], [10, 50]]
    assert det2(Gshift) == 100
    assert det2(Gunit) == 4
    assert (det2(U), det2(V)) == (1, 5)


def main():
    real = test_real_translation()
    complex_cases, naive_false, naive_true = test_complex_source()
    test_fake_transport()
    assert real == 4620
    assert (complex_cases, naive_false, naive_true) == (1800, 1440, 360)
    print(json.dumps({
        "evidence": "M-bounded-exact-integer-oracle",
        "complex_cases": complex_cases,
        "naive_squared_distance_failures": naive_false,
        "naive_squared_distance_matches": naive_true,
        "real_translation_cases": real,
        "fake_unimodular_null": "rejected",
        "outcome": "pass",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
