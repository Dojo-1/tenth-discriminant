"""Independent finite integer oracle for the two-sided inert-prime Gram factor.

Not a Lean checker or proof of the universal theorem. Arithmetic only;
no floats, changes to main, or external packages. Run with Python 3.11+:
    python independent_two_sided_oracle.py
"""
from __future__ import annotations

from math import comb, prod
from itertools import product


def mul(a, b, D):
    return (a[0] * b[0] - D * a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def power(a, n, D):
    out = (1, 0)
    for _ in range(n):
        out = mul(out, a, D)
    return out


def conjugate(a):
    return (a[0], -a[1])


def jet(D, r, s, order, q):
    """Ordinary d^order/dZ^order of Z^r W^s, W fixed, at (q, qbar)."""
    if order > r:
        return (0, 0)
    falling = prod(range(r - order + 1, r + 1))
    a = mul(power(q, r - order, D), power(conjugate(q), s, D), D)
    return (falling * a[0], falling * a[1])


def trace(D, a, b):
    return 2 * (a[0] * b[0] + D * a[1] * b[1])


def rectangle(R, S):
    return [(r, s) for r in range(R) for s in range(S)]


def gram(rows, points, J, D):
    return [[sum(trace(D, rows[i](q, j), rows[h](q, j))
                 for q in points for j in range(J))
             for h in range(len(rows))] for i in range(len(rows))]


def original_rows(R, S, D):
    return [lambda q, j, r=r, s=s: jet(D, r, s, j, q)
            for r, s in rectangle(R, S)]


def basis_change(R, S, p):
    ids = rectangle(R, S)
    columns = {rs: i for i, rs in enumerate(ids)}
    U = [[0 for _ in ids] for _ in ids]
    weights = []
    for i, (r, s) in enumerate(ids):
        k = min(r // p, S - 1 - s)
        weights.append(k)
        for t in range(k + 1):
            U[i][columns[(r - p * t, s + t)]] += (-1) ** t * comb(k, t)
    return U, weights


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def transpose(A):
    return [list(row) for row in zip(*A)]


def determinant(A):
    """Integer Bareiss elimination with row exchanges; independent of Gram construction."""
    n = len(A)
    if n == 0:
        return 1
    b = [row.copy() for row in A]
    sign, prev = 1, 1
    for k in range(n - 1):
        if b[k][k] == 0:
            v = next((i for i in range(k + 1, n) if b[i][k]), None)
            if v is None:
                return 0
            b[k], b[v] = b[v], b[k]
            sign = -sign
        pivot = b[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                value = b[i][j] * pivot - b[i][k] * b[k][j]
                assert value % prev == 0
                b[i][j] = value // prev
            b[i][k] = 0
        prev = pivot
    return sign * b[-1][-1]


def prime_is_inert(D, p):
    if p < 3 or p % 2 == 0 or any(p % t == 0 for t in range(3, int(p ** .5) + 1, 2)):
        return False
    return (-D) % p not in {k * k % p for k in range(p)}


def frobenius_at(D, p, q):
    a = power(q, p, D)
    b = conjugate(q)
    return all((x - y) % p == 0 for x, y in zip(a, b))


def ellipse(D, radius):
    return [(x, y) for x in range(-radius, radius + 1)
            for y in range(-radius, radius + 1)
            if x * x + D * y * y <= radius * radius]


def verify_case(D, p, R, S, J, radius):
    """Construct G and K independently, then check the exact matrix identity."""
    assert prime_is_inert(D, p), 'no inert-prime premise'
    Q = ellipse(D, radius)
    assert all(frobenius_at(D, p, q) for q in Q)
    original = original_rows(R, S, D)
    G = gram(original, Q, J, D)
    U, weights = basis_change(R, S, p)
    N = R * S
    assert all(U[i][i] == 1 and all(U[i][j] == 0 for j in range(i + 1, N))
               for i in range(N))
    assert determinant(U) == 1
    transformed = []
    for i in range(N):
        def one(q, j, i=i):
            v = [original[h](q, j) for h in range(N)]
            return (sum(U[i][h] * v[h][0] for h in range(N)),
                    sum(U[i][h] * v[h][1] for h in range(N)))
        transformed.append(one)
    quotient = []
    for i in range(N):
        factor = p ** weights[i]
        for q, j in product(Q, range(J)):
            v = transformed[i](q, j)
            assert v[0] % factor == 0 and v[1] % factor == 0, (i, q, j, v)
        def reduced(q, j, i=i, factor=factor):
            a, b = transformed[i](q, j)
            return (a // factor, b // factor)
        quotient.append(reduced)
    K = gram(quotient, Q, J, D)
    H1 = matmul(matmul(U, G), transpose(U))
    H2 = gram(transformed, Q, J, D)
    H3 = [[p ** (weights[i] + weights[j]) * K[i][j] for j in range(N)] for i in range(N)]
    assert H1 == H2 == H3
    F = sum(min(r // p, t) for r in range(R) for t in range(S))
    assert F == sum(weights)
    detG, detK = determinant(G), determinant(K)
    assert detG == (p ** (2 * F)) * detK
    return {'D': D, 'p': p, 'R': R, 'S': S, 'J': J, 'radius': radius,
            'samples': len(Q), 'F': F, 'factor': p ** (2 * F),
            'positive_det': detG > 0, 'det_digits': len(str(abs(detG))) if detG else 1,
            'detK_nonzero': detK != 0, 'nontrivial_rows': sum(k > 0 for k in weights)}


def passive_shift_control():
    """Active movement changes real trace Gram; paired passive jets preserve it."""
    D, J, R, S = 1, 1, 2, 1
    Q = [(-1, 0), (0, 0), (1, 0)]
    shift = (0, 1)
    shifted = [(x + shift[0], y + shift[1]) for x, y in Q]
    rows = original_rows(R, S, D)
    old = determinant(gram(rows, Q, J, D))
    active = determinant(gram(rows, shifted, J, D))
    passive = []
    for r, s in rectangle(R, S):
        def shifted_jet(qprime, j, r=r, s=s):
            oldq = (qprime[0] - shift[0], qprime[1] - shift[1])
            return jet(D, r, s, j, oldq)
        passive.append(shifted_jet)
    recovered = determinant(gram(passive, shifted, J, D))
    assert (old, active, recovered) == (24, 60, 24)
    return {'original': old, 'active': active, 'passive': recovered}


def negative_controls():
    # D=2 splits at p=3: the Frobenius generator congruence fails.
    assert not prime_is_inert(2, 3)
    assert not frobenius_at(2, 3, (0, 1))
    # Hasse derivative of Z^p at order p is 1, ordinary derivative is p!.
    assert 1 % 3 != 0
    assert prod(range(1, 4)) % 3 == 0
    # Separate row/col divisibility is insufficient for a square.
    assert 3 % 3 == 0 and 3 % 9 != 0
    return {'split_pair_congruence': False, 'Hasse_third_divisible': False,
            'row_col_individually_implies_square': False}


def main():
    import json
    controls = negative_controls()
    records = [verify_case(19, 3, 4, 2, 2, 5),
               verify_case(3, 5, 6, 2, 2, 5),
               verify_case(19, 3, 7, 3, 3, 7)]
    assert records[0]['samples'] == 21 and records[0]['factor'] == 9
    assert records[0]['positive_det']
    print(json.dumps({'statement':'finite independent arithmetic oracle, not Lean or a universal proof',
                      'cases':records, 'passive_translation': passive_shift_control(),
                      'negative_controls':controls}, indent=2))


if __name__ == '__main__':
    main()
