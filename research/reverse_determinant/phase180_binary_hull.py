#!/usr/bin/env python3
"""Phase180: binary hull of the ORIGINAL odd-D ordinary-jet trace Gram.

Exact four-support D=3 test, two evaluators, direct F2 hull enumeration,
integer determinant and unimodular-gauge controls. No new field bound.
"""
from __future__ import annotations

from itertools import product
from math import factorial
from sympy import Matrix, diag
from phase159_observation_continuum import ordinary_effective


def multiply(z, w, D):
    a, b = z
    c, d = w
    return (a*c-D*b*d, a*d+b*c)


def power(z, n, D):
    out = (1, 0)
    for _ in range(n):
        out = multiply(out, z, D)
    return out


def independent_ordinary(Q, D, R, S):
    """Independently reconstruct rows (r,s), columns (point,j,real/imag)."""
    cols, weights = [], []
    for x, y in Q:
        z, w = (x, y), (x, -y)
        for j in range(S):
            re, im = [], []
            for r in range(R):
                for s in range(S):
                    if j > r:
                        a, b = 0, 0
                    else:
                        a, b = multiply(power(z, r-j, D),
                                        power(w, s, D), D)
                        factor = factorial(r)//factorial(r-j)
                        a *= factor
                        b *= factor
                    re.append(a)
                    im.append(b)
            cols.append(re)
            weights.append(2)
            if y:
                cols.append(im)
                weights.append(2*D)
    return Matrix.hstack(*(Matrix(c) for c in cols)), weights


def binary_rank(rows):
    """Independent elementary F2 Gaussian rank, no SymPy rank oracle."""
    a = [[int(v) & 1 for v in row] for row in rows]
    m, n, pivots = len(a), len(a[0]), 0
    for j in range(n):
        pivot = next((i for i in range(pivots, m) if a[i][j]), None)
        if pivot is None:
            continue
        a[pivots], a[pivot] = a[pivot], a[pivots]
        for i in range(m):
            if i != pivots and a[i][j]:
                for t in range(j, n):
                    a[i][t] ^= a[pivots][t]
        pivots += 1
        if pivots == m:
            break
    return pivots


def hull_by_enumeration(E):
    """Enumerate distinct binary codewords for these bounded m=4 cases."""
    m, n = E.shape
    assert m == 4
    binary = [[int(E[i, j]) & 1 for j in range(n)] for i in range(m)]
    code = set()
    for bits in product((0, 1), repeat=m):
        word = tuple(sum(bits[i]*binary[i][j] for i in range(m)) & 1
                     for j in range(n))
        code.add(word)
    hull = {w for w in code if all(
        sum(w[j]*binary[i][j] for j in range(n)) % 2 == 0
        for i in range(m))}
    assert hull and len(hull) & (len(hull)-1) == 0
    return (len(hull).bit_length()-1), len(code).bit_length()-1


def v2(n):
    n = abs(int(n))
    assert n > 0
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return k


def check(Q, expected):
    D, R, S = 3, 2, 2
    E, weights = independent_ordinary(Q, D, R, S)
    ref, original_weights, _ = ordinary_effective(Q, D, R, S)
    assert E == Matrix(ref) and weights == original_weights
    assert all(w % 2 == 0 and (w//2) % 2 == 1 for w in weights)
    m, n = E.shape
    G = E*diag(*weights)*E.T
    H = E*diag(*(w//2 for w in weights))*E.T
    assert G == 2*H
    det = int(G.det(method="domain-ge"))
    assert det > 0
    r = binary_rank([[E[i,j] for j in range(n)] for i in range(m)])
    rank_H = binary_rank([[H[i,j] for j in range(m)] for i in range(m)])
    hull, rank_by_enum = hull_by_enumeration(E)
    assert r == rank_by_enum
    assert rank_H == r-hull
    lower = m+(m-r)+hull
    valuation = v2(det)
    assert valuation >= lower
    got = (n, r, hull, lower, valuation, det)
    assert got == expected, (Q,got,expected)

    # Preserve exact integer Gram and hull under unimodular *row* gauge.
    U = Matrix.eye(m)
    U[0,1] = 1
    assert U.det() == 1
    transported = U*E
    moved = transported*diag(*weights)*transported.T
    assert moved == U*G*U.T and int(moved.det()) == det
    moved_rank = binary_rank([[transported[i,j] for j in range(n)]
                              for i in range(m)])
    moved_hull, _ = hull_by_enumeration(transported)
    assert (moved_rank, moved_hull) == (r, hull)
    print("PHASE180_SOURCE", Q, dict(
        channels=n, binary_rank=r, hull=hull,
        valuation_lower=lower, actual_v2=valuation, det=det), flush=True)


def main():
    C = [(0,2)]
    A = C + [(-2,1)]
    B = C + [(-1,0)]
    AB = C + [(-2,1),(-1,0)]
    check(C, (4,2,0,6,8,2304))
    check(A, (8,4,1,5,5,122656))
    check(B, (6,4,0,4,4,74896))
    check(AB, (10,4,1,5,5,622368))
    print("PHASE180_BINARY_HULL_PASS: exact bounded only", flush=True)


if __name__ == "__main__":
    main()
