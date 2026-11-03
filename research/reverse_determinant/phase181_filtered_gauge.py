#!/usr/bin/env python3
"""Finite Phase181 follow-up: filtered gauges and passive normalization.

The source metric, supports and original ordinary jets are unchanged.
Tests anchored extraction, moving extraction and prime-local Smith data.
No new discriminant bound or hardness theorem is claimed.
"""
from __future__ import annotations

from fractions import Fraction
from math import comb, gcd


def mul(a, b):
    assert a and b and len(a[0]) == len(b)
    return [[sum(x * b[k][j] for k, x in enumerate(row))
             for j in range(len(b[0]))] for row in a]


def tr(a):
    return [list(v) for v in zip(*a)]


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def shear(n, i, j, c):
    assert i != j
    a = eye(n)
    a[i][j] = c
    return a


def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def snf2(a):
    g = 0
    for row in a:
        for v in row:
            assert isinstance(v, (int, Fraction)) and Fraction(v).denominator == 1
            g = gcd(g, int(v))
    assert g
    return g, int(abs(det2(a)) // g)


def weighted(a, k):
    """Rational matrix K = Delta^-1 A Delta, without floating point."""
    return [[Fraction(a[i][j] * 2 ** k[j], 2 ** k[i])
             for j in range(len(k))] for i in range(len(k))]


def compatible(a, k):
    """Equivalent entrywise criterion for integral K."""
    return all(a[i][j] % (2 ** (k[i] - k[j])) == 0
               for i in range(len(k)) for j in range(len(k))
               if k[i] > k[j])


def all_integral(a):
    return all(x.denominator == 1 if isinstance(x, Fraction)
               else isinstance(x, int) for row in a for x in row)


def toy():
    delta = [[1, 0], [0, 2]]
    n = [[2, 0], [0, 2]]
    e = mul(delta, n)
    g = mul(mul(e, [[2, 0], [0, 2]]), tr(e))
    h = mul(n, tr(n))
    assert snf2(g) == (8, 32) and snf2(h) == (4, 4)
    trials = [("accepted", shear(2, 0, 1, 1), (4, 4)),
              ("rejected", shear(2, 1, 0, 1), (1, 16))]
    for name, v, expected in trials:
        k = weighted(v, [0, 1])
        assert (name == "accepted") == compatible(v, [0, 1])
        assert (name == "accepted") == all_integral(k)
        ep = mul(v, e)
        np = mul(k, n)
        assert all_integral(np)  # A rational gauge may preserve this one quotient.
        gp = mul(mul(ep, [[2, 0], [0, 2]]), tr(ep))
        hp = mul(np, tr(np))
        assert snf2(gp) == snf2(g) and snf2(hp) == expected
        vinv = shear(2, 0, 1, -1) if name == "accepted" else shear(2, 1, 0, -1)
        assert mul(vinv, ep) == e  # Passively transported extractor.
        print("TOY", name, "original", snf2(gp),
              "fixed-extractor", snf2(hp),
              "transported-extractor", snf2(h), flush=True)

    cases = 0
    for k0 in range(4):
        for k1 in range(4):
            for i, j in [(0, 1), (1, 0)]:
                for c in [-3, -2, -1, 0, 1, 2, 3, 4]:
                    a = shear(2, i, j, c)
                    assert compatible(a, [k0, k1]) == all_integral(weighted(a, [k0, k1]))
                    cases += 1
    assert cases == 256
    print("EXACT_FILTER_GATE_PASS", cases, "independent matrix controls", flush=True)


def source_d19():
    """Frozen D19 six-point ordinary-jet source from Phases159/181."""
    from phase159_observation_continuum import ordinary_effective
    from phase159_padic_gram import gram_mod_2_power, smith_exponents_2
    from phase181_normalized_binary_filtration import source_normalize

    d, r, s = 19, 8, 4
    q = [(-2, -1), (-1, -1), (-1, 0), (0, -1), (0, 0), (1, -1)]
    e, weights, _ = ordinary_effective(q, d, r, s)
    n, k = source_normalize(e, r, s)
    m = r * s
    u = [[0] * m for _ in range(m)]
    for rr in range(r):
        kk = rr // 4
        for ss in range(s):
            i = rr * s + ss
            for t in range(kk + 1):
                u[i][(rr - 2*t)*s+ss] = (-1)**t * comb(kk, t)
    assert mul(u, e) == [[(2**k[i])*v for v in row] for i, row in enumerate(n)]
    ui = [[0] * m for _ in range(m)]
    for i in range(m):
        assert u[i][i] == 1
        ui[i][i] = 1
        for j in range(i):
            ui[i][j] = -sum(u[i][z] * ui[z][j] for z in range(j, i))
    assert mul(u, ui) == eye(m) and mul(ui, u) == eye(m)

    lower, higher = 0, 4*s
    assert k[lower] == 0 and k[higher] == 1
    cmetric = [w//2 for w in weights]
    h = gram_mod_2_power(n, cmetric, 64)
    original_barcode, unknown = smith_exponents_2(h, 64)
    assert unknown == 0 and sum(original_barcode) == 102

    for name, c, expect_allowed in [("compatible", 2, True),
                                     ("incompatible", 1, False)]:
        a = shear(m, higher, lower, c)
        v = mul(mul(ui, a), u)
        vi = mul(mul(ui, shear(m, higher, lower, -c)), u)
        assert mul(v, vi) == eye(m)
        assert compatible(a, k) == expect_allowed
        ep = mul(v, e)
        transformed = mul(u, ep)
        assert transformed == mul(a, mul(u, e))
        ns = [[Fraction(x, 2**k[i]) for x in row]
              for i, row in enumerate(transformed)]
        assert all_integral(ns) == expect_allowed
        if expect_allowed:
            ktrans = weighted(a, k)
            assert all_integral(ktrans) and ns == mul(ktrans, n)
            hp = gram_mod_2_power([[int(x) for x in row] for row in ns], cmetric, 64)
            barcode_p, unknown_p = smith_exponents_2(hp, 64)
            assert unknown_p == 0 and barcode_p == original_barcode
        # Moving U with V^-1 always reconstructs the original quotient.
        up = mul(u, vi)
        assert mul(up, ep) == mul(u, e)
        assert [[Fraction(x, 2**k[i]) for x in row]
                for i, row in enumerate(mul(up, ep))] == n
        print("D19_SOURCE", name, "fixed_integral", all_integral(ns),
              "passively_transportable", True, flush=True)
    print("PHASE181_FILTERED_TRANSPORT_PASS: finite only", flush=True)


if __name__ == "__main__":
    import sys
    assert sys.argv[1:] in ([], ["--toy-only"])
    toy()
    if not sys.argv[1:]:
        source_d19()  # Fail closed if the original source import/check fails.
