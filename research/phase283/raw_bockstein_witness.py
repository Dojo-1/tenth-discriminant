#!/usr/bin/env python3
"""Phase283: original D403 raw first-Bockstein p3 witnesses.

Predictions and falsifiers preregistered at commit b79b3af, before this script.
No normalized C0, Gram metric, determinant bound or exceptional-zero claim.
"""
from pathlib import Path
from math import comb
import subprocess
import sys

HERE = Path(__file__).resolve()
ROOT = HERE.parents[2]
for sub in ("phase206", "phase204"):
    sys.path.insert(0, str(HERE.parents[1] / sub))

from source_probe import params, mul, fall, rank_mod
from ordinary_jet_filtration import jet

D, P, R, S, J, NUM_POINTS = 403, 3, 100, 4, 4, 219
SOURCE_BLOBS = {
    "research/phase206/source_probe.py": "3f954b59d9f86b06ad53667c869b5b24f2e6c7f6",
    "research/phase204/ordinary_jet_filtration.py": "dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8",
}

def frozen_helpers():
    for path, expected in SOURCE_BLOBS.items():
        actual = subprocess.check_output(
            ["git", "rev-parse", "HEAD:" + path], cwd=ROOT, text=True
        ).strip()
        assert actual == expected, ("helper source drift", path, actual, expected)

def pair_pow_mod(z, n, p):
    """Separate residue-ring exponentiation, not the original-jet oracle."""
    out = (1, 0)
    base = (z[0] % p, z[1] % p)
    while n:
        if n & 1:
            out = mul(out, base, D, p)
        base = mul(base, base, D, p)
        n //= 2
    return out

def rank_second(matrix, p):
    """Independent column-sweep Gaussian elimination, pivoting over all rows."""
    a = [[int(x) % p for x in row] for row in matrix]
    if not a:
        return 0
    n, m = len(a), len(a[0])
    r = 0
    for j in range(m):
        pivot = next((i for i in range(r, n) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][j], -1, p)
        a[r][j:] = [(v * inv) % p for v in a[r][j:]]
        for i in range(r + 1, n):
            factor = a[i][j]
            if factor:
                a[i][j:] = [
                    (u - factor * v) % p
                    for u, v in zip(a[i][j:], a[r][j:])
                ]
        r += 1
        if r == n:
            break
    return r

def original_f_jet(a, j, z):
    """Exact original INTEGER jet of Z^(a+3) - Z^a W, W held fixed."""
    b = jet(D, a + P, 0, j, z)
    c = jet(D, a, 1, j, z)
    return b[0] - c[0], b[1] - c[1]

def check_full_source(Q):
    full = []
    last = []
    for a in range(9):
        assert a + P < R and 1 < S
        quotient = []
        third = []
        for j in range(J):
            for x, y in Q:
                z = (x, y)
                v = original_f_jet(a, j, z)
                assert all(n % P == 0 for n in v), ("nonintegral quotient", a, j, z)
                q = tuple((n // P) % P for n in v)
                quotient.extend(q)
                if j == 3:
                    power = pair_pow_mod((x, y), a, P)
                    expected = ((2 * power[0]) % P, (2 * power[1]) % P)
                    assert q == expected, ("wrong quotient third jet", a, z, q, expected)
                    third.extend(q)
        assert len(quotient) == 2 * J * NUM_POINTS
        assert len(third) == 2 * NUM_POINTS
        full.append(quotient)
        last.append(third)
    return full, last

def rank_controls(Q, full, last):
    assert rank_mod(last, P) == rank_second(last, P) == 9
    assert rank_mod(full, P) == rank_second(full, P) == 9

    # Nine distinct F9 nodes: representative 2-coordinate projections.
    reps = {}
    for qi, (x, y) in enumerate(Q):
        reps.setdefault((x % P, y % P), qi)
    assert len(reps) == 9
    witness = [
        [value for qi in reps.values() for value in row[2*qi:2*qi+2]]
        for row in last
    ]
    assert rank_mod(witness, P) == rank_second(witness, P) == 9

    # Unimodular shear in the nine-dimensional witness lattice.
    sheared = [row[:] for row in last]
    sheared[1] = [(a + b) % P for a, b in zip(sheared[1], sheared[0])]
    assert rank_mod(sheared, P) == rank_second(sheared, P) == 9
    return len(reps)

def lift_independence(Q):
    """Replacing a lift f by f+3g changes beta by raw T(g) mod3."""
    a = 4
    for j in range(J):
        for z in Q:
            orig = original_f_jet(a, j, z)
            source = jet(D, 7, 2, j, z)  # legitimate original rectangle row
            modified = tuple(v + P*w for v, w in zip(orig, source))
            assert all(v % P == 0 for v in modified)
            change = [((u // P) - (v // P)) % P
                      for u, v in zip(modified, orig)]
            assert change == [w % P for w in source]
            if j == 3:
                # Entire RAW j3 source is 0 mod3: coker projection is well-defined.
                assert change == [0, 0]
    assert all(fall(r, 3) % P == 0 for r in range(R))

def negative_controls():
    # Toy T=diag(1,3,9): two kernel classes, but only one first grade.
    assert rank_mod([[1, 0, 0], [0, 0, 0], [0, 0, 0]], P) == 1
    quotient_images = [[0, 1, 0], [0, 0, P]]
    assert rank_mod(quotient_images, P) == rank_second(quotient_images, P) == 1

    # D403, p11 split: (Z^11-W)(u,-u) = 2u, not divisible by 11.
    z = (0, 1)
    left = jet(D, 11, 0, 0, z)
    right = jet(D, 0, 1, 0, z)
    discrepancy = tuple(a-b for a, b in zip(left, right))
    assert discrepancy[1] % 11 == 2, discrepancy

    # Ordinary third derivative != Hasse third coefficient in characteristic 3.
    ordinary = jet(D, 3, 0, 3, (0, 0))
    assert ordinary == (6, 0) and comb(3, 3) % P == 1
    assert ordinary[0] % P == 0 and ordinary[0] // P % P == 2

def main():
    frozen_helpers()
    rho, R0, S0, J0, Q = params(D)
    assert (rho, R0, S0, J0, len(Q)) == (40, R, S, J, NUM_POINTS)
    assert (-D) % P == 2  # nonsquare in F3: inert
    assert {y for _,y in Q} == {-1, 0, 1}
    residues = {(x % P, y % P) for x, y in Q}
    assert len(residues) == 9
    full, last = check_full_source(Q)
    classes = rank_controls(Q, full, last)
    lift_independence(Q)
    negative_controls()
    print("PHASE283_RAW_BOCKSTEIN", {
        "D": D, "prime": P, "source_rows": R * S,
        "source_columns": 2 * J * len(Q),
        "number_of_witnesses": len(full),
        "distinct_residue_nodes": classes,
        "rank_j3_quotients": 9,
        "certified_raw_beta1_rank_at_least": 9,
        "gram_valuation_added": 0,
        "first_bockstein_not_primitive_pairing": True,
    }, flush=True)
    print("PASS Phase283 raw exact-integer first-lift witnesses and all controls", flush=True)

if __name__ == "__main__":
    main()
