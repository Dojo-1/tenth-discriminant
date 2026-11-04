#!/usr/bin/env python3
"""Phase201 exact, finite original-Z-jet complex-minor/real-Gram control.

Computes in Z[sqrt(-D)] without floating point, arbitrary precision Python
integers only. This checks one explicit small semantic mapping; it is NOT
the uniform 322^4 theorem and does NOT establish source equivalence with
twinheterodox's distinct parameter choice or full O_K sampling lattice.
"""

from math import prod


def mul(a, b, d):
    return a[0] * b[0] - d * a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def power(z, k, d):
    v = (1, 0)
    for _ in range(k):
        v = mul(v, z, d)
    return v


def jet(r, s, j, x, y, d):
    """Ordinary d^j/dZ^j Z^r W^s, hold W fixed, W=conj(Z)."""
    if j > r:
        return 0, 0
    falling = prod(range(r - j + 1, r + 1))
    a, b = mul(power((x, y), r - j, d), power((x, -y), s, d), d)
    return falling * a, falling * b


def determinant(rows):
    """Fraction-free Bareiss determinant with pivot row swaps."""
    a = [list(map(int, row)) for row in rows]
    n = len(a)
    if n == 0:
        return 1
    prev = 1
    sign = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot_row = next((i for i in range(k + 1, n) if a[i][k]), None)
            if pivot_row is None:
                return 0
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = a[i][j] * pivot - a[i][k] * a[k][j]
                assert num % prev == 0, "Bareiss integrality violated"
                a[i][j] = num // prev
            a[i][k] = 0
        prev = pivot
    return sign * a[-1][-1]


def main():
    d, rho, rmax, smax, depth = 3, 2, 2, 2, 2
    points = [(x, y) for x in range(-rho, rho + 1)
              for y in range(-rho, rho + 1)
              if x * x + d * y * y <= rho * rho]
    rows = [(r, s) for r in range(rmax) for s in range(smax)]
    cols = [(j, x, y) for j in range(depth) for x, y in points]
    evals = [[jet(r, s, j, x, y, d) for j, x, y in cols]
             for r, s in rows]
    gram = [[sum(2 * (a * c + d * b * e)
                 for (a, b), (c, e) in zip(left, right))
             for right in evals] for left in evals]
    expected_gram = [
        [22, 0, 0, 64],
        [0, 64, -8, 0],
        [0, -8, 86, 0],
        [64, 0, 0, 296],
    ]
    assert len(points) == 11 and len(cols) == 22
    assert gram == expected_gram, (gram, expected_gram)
    det_g = determinant(gram)
    assert det_g == 13143040 and det_g % 5 == 0

    selected = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0)]
    minor_pairs = [[jet(r, s, j, x, y, d) for j, x, y in selected]
                   for r, s in rows]
    assert all(b == 0 for row in minor_pairs for _, b in row)
    minor = [[a for a, _ in row] for row in minor_pairs]
    expected_minor = [
        [1, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 1, 1, 1],
        [0, 0, 1, 1],
    ]
    assert minor == expected_minor
    det_m = determinant(minor)
    assert det_m == -1 and det_m % 5 != 0
    assert 2 ** len(rows) * det_m ** 2 <= det_g

    print("PASS: original ordinary-Z-jet finite trace Gram is exactly:")
    for row in gram:
        print(" ", row)
    print(f"det(G)={det_g} (mod 5 = {det_g % 5})")
    print(f"selected complex minor det(M)={det_m} (mod 5 = {det_m % 5})")
    print("Complex minor mod-5 nonvanishing DOES NOT force real trace-Gram "
          "determinant mod-5 nonvanishing.")
    print("Boundary: small D=3, not an inert-prime valuation counterexample "
          "or an application of the 322^4 field theorem.")


if __name__ == "__main__":
    main()
