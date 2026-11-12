#!/usr/bin/env python3
"""Phase284: source-exact overlap of nine raw Bockstein witnesses and old p3 Frobenius rows.

Frozen in PRE_REGISTERED_FROBENIUS_OVERLAP.md at 8a9153f before this script.
Only original D403 integer ordinary Z-jets (W held fixed). NO extra Gram factor.
"""
from functools import lru_cache
from math import comb
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve()
ROOT = HERE.parents[2]
for sub in ("phase206", "phase204"):
    sys.path.insert(0, str(HERE.parents[1] / sub))

from source_probe import params, rank_mod
from ordinary_jet_filtration import jet

D, P, R, S, J, QLEN = 403, 3, 100, 4, 4, 219
FROZEN_BLOBS = {
    "research/phase206/source_probe.py": "3f954b59d9f86b06ad53667c869b5b24f2e6c7f6",
    "research/phase204/ordinary_jet_filtration.py": "dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8",
}


def old_k(r, s):
    assert 0 <= r < R and 0 <= s < S
    return min(r // P, S - 1 - s)


def frozen_source():
    for path, blob in FROZEN_BLOBS.items():
        actual = subprocess.check_output(
            ["git", "rev-parse", "HEAD:" + path], cwd=ROOT, text=True
        ).strip()
        assert actual == blob, ("unexpected original-source helper", path, actual, blob)
    rho, r, s, j, q = params(D)
    assert (rho, r, s, j, len(q)) == (40, R, S, J, QLEN)
    assert {y for x, y in q} == {-1, 0, 1}
    assert len({(x % P, y % P) for x, y in q}) == 9
    assert (-D) % P == 2  # irreducible u^2 + D at p3
    assert sum(old_k(r, s) for r in range(R) for s in range(S)) == 570
    return q


def original_jet(r, s, j, point):
    return jet(D, r, s, j, point)


@lru_cache(None)
def framed_jet(r, s, k, j, point):
    """Exact INTEGER original jet of Z^(r-3k)*W^s*(Z^3-W)^k."""
    assert 0 <= r < R and 0 <= s < S and k == old_k(r, s)
    v = (0, 0)
    for h in range(k + 1):
        rr, ss = r - P * h, s + h
        assert 0 <= rr < R and 0 <= ss < S
        term = original_jet(rr, ss, j, point)
        coef = comb(k, h) * (-1 if h % 2 else 1)
        v = (v[0] + coef * term[0], v[1] + coef * term[1])
    return v


def f_jet(a, j, point):
    v = original_jet(a + P, 0, j, point)
    w = original_jet(a, 1, j, point)
    return (v[0] - w[0], v[1] - w[1])


def source_terms(a):
    q, b = divmod(a, P)
    assert 0 <= q <= 2 and 0 <= b <= 2
    terms = []
    for t in range(q + 1):
        k = q + 1 - t
        r, s = b + P * k, t
        assert k == old_k(r, s), ("not the old legal Frobenius row", a, r, s, k)
        terms.append((comb(q, t), r, s, k))
    assert len(terms) == q + 1 and terms[-1] == (1, b + P, q, 1)
    return b, q, terms


def pair_mul_mod(z, w, p=P):
    return ((z[0] * w[0] - D * z[1] * w[1]) % p,
            (z[0] * w[1] + z[1] * w[0]) % p)


def pair_pow_mod(z, n, p=P):
    v, z = (1, 0), (z[0] % p, z[1] % p)
    while n:
        if n % 2:
            v = pair_mul_mod(v, z, p)
        z = pair_mul_mod(z, z, p)
        n //= 2
    return v


def independent_rank(a, p):
    """Second finite-field rank routine: column sweep with row swaps."""
    A = [[v % p for v in row] for row in a]
    if not A:
        return 0
    rows, columns, i = len(A), len(A[0]), 0
    for j in range(columns):
        z = next((ii for ii in range(i, rows) if A[ii][j]), None)
        if z is None:
            continue
        A[i], A[z] = A[z], A[i]
        inv = pow(A[i][j], -1, p)
        A[i][j:] = [(v * inv) % p for v in A[i][j:]]
        for ii in range(i + 1, rows):
            c = A[ii][j]
            if c:
                A[ii][j:] = [
                    (v - c * pivot) % p
                    for v, pivot in zip(A[ii][j:], A[i][j:])
                ]
        i += 1
        if i == rows:
            break
    return i


def verify_all_jets(points):
    k1_labels = set()
    normalized_j3 = []
    source_j3 = []
    exact_checks = 0
    max_depth = 0
    for a in range(9):
        b, q, terms = source_terms(a)
        distinguished = (b + P, q)
        assert distinguished not in k1_labels
        k1_labels.add(distinguished)
        assert old_k(*distinguished) == 1
        max_depth = max(max_depth, max(k for _, _, _, k in terms))
        row_last = []
        source_last = []
        for j in range(J):
            for point in points:
                direct = f_jet(a, j, point)
                expanded = [0, 0]
                weighted = [0, 0]
                distinguished_normalized = None
                for c, r, s, k in terms:
                    value = framed_jet(r, s, k, j, point)
                    assert value[0] % (P ** k) == 0
                    assert value[1] % (P ** k) == 0
                    norm = (value[0] // P ** k, value[1] // P ** k)
                    for v in (0, 1):
                        expanded[v] += c * value[v]
                        weighted[v] += c * (P ** (k - 1)) * norm[v]
                    if k == 1:
                        assert (r, s) == distinguished
                        distinguished_normalized = norm
                assert tuple(expanded) == direct, ("incorrect integral frame identity", a, j, point)
                assert direct[0] % P == 0 and direct[1] % P == 0
                lhs = (direct[0] // P, direct[1] // P)
                assert tuple(weighted) == lhs, ("quotient not transported exactly", a, j, point)
                assert distinguished_normalized is not None
                assert tuple(x % P for x in lhs) == tuple(x % P for x in distinguished_normalized), (
                    "unaccounted first-lift class", a, j, point
                )
                if j == 3:
                    expected = pair_pow_mod(point, a)
                    expected = ((2 * expected[0]) % P, (2 * expected[1]) % P)
                    assert tuple(v % P for v in distinguished_normalized) == expected
                    assert tuple(v % P for v in lhs) == expected
                    row_last.extend(v % P for v in distinguished_normalized)
                    source_last.extend(v % P for v in lhs)
                exact_checks += 1
        assert len(row_last) == len(source_last) == 2 * QLEN
        normalized_j3.append(row_last)
        source_j3.append(source_last)
    assert len(k1_labels) == 9
    assert max_depth == 3
    assert normalized_j3 == source_j3
    assert rank_mod(normalized_j3, P) == independent_rank(normalized_j3, P) == 9
    # Unimodular shear within the k=1 frame is an invariant rank check.
    shear = [row[:] for row in normalized_j3]
    shear[1] = [(v + w) % P for v, w in zip(shear[1], shear[0])]
    assert rank_mod(shear, P) == independent_rank(shear, P) == 9
    return exact_checks, sorted(k1_labels), max_depth


def negative_controls():
    assert old_k(9, 0) == 3 != 1  # not all transformed rows have one p factor
    # With S=2, q=2 would require W^2 in the source rectangle: illegal.
    q = 2
    assert not all(t < 2 for t in range(q + 1))
    z = (0, 1)
    v = original_jet(11, 0, 0, z)
    w = original_jet(0, 1, 0, z)
    assert (v[1] - w[1]) % 11 == 2  # split p11 is not the inert quotient
    assert original_jet(3, 0, 3, (0, 0)) == (6, 0)  # ordinary
    assert comb(3, 3) % P == 1  # different Hasse coefficient
    assert all(original_jet(r, 0, 3, (0, 0))[0] % P == 0 for r in range(R))


def main():
    points = frozen_source()
    exact, k1, depth = verify_all_jets(points)
    negative_controls()
    print("PHASE284_FROBENIUS_OVERLAP", {
        "D": D, "p": P, "R": R, "S": S, "J": J, "Q": len(points),
        "source_exact_jet_point_witness_checks": exact,
        "raw_first_bockstein_witnesses": 9,
        "matched_old_k1_frame_rows": k1,
        "highest_old_frame_k_seen": depth,
        "old_counted_F3": 570,
        "matched_witness_rank": 9,
        "NEW_valuation_units_from_these_witnesses": 0,
        "primitive_pairing_computed": False,
    }, flush=True)
    print("PASS Phase284: all nine raw Bockstein classes lie in old Frobenius k1 layer", flush=True)


if __name__ == "__main__":
    main()
