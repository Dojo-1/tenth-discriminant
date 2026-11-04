#!/usr/bin/env python3
"""Inert prime two-jet Hermite witness, prospectively registered in Issue #133.

The residue algebra is the FIELD F_(p^2), NOT split F_p x F_p.
Do not transport this J=2 rotation into the production J=S(D) source.
Exact stdlib arithmetic; no floating point or outside prime inputs.
"""
from math import prod


def pilot(p, D):
    assert (p, D) in ((3, 7), (5, 3))
    assert pow((-D) % p, (p - 1) // 2, p) == p - 1
    zero, one = (0, 0), (1, 0)

    def add(z, w):
        return ((z[0] + w[0]) % p, (z[1] + w[1]) % p)

    def sub(z, w):
        return ((z[0] - w[0]) % p, (z[1] - w[1]) % p)

    def mul(z, w):
        return ((z[0]*w[0] - D*z[1]*w[1]) % p,
                (z[0]*w[1] + z[1]*w[0]) % p)

    def scale(n, z):
        return (n*z[0] % p, n*z[1] % p)

    def power(z, n):
        a = one
        for _ in range(n):
            a = mul(a, z)
        return a

    def inverse(z):
        denom = (z[0]*z[0] + D*z[1]*z[1]) % p
        assert denom
        coeff = pow(denom, -1, p)
        return (z[0]*coeff % p, -z[1]*coeff % p)

    nodes = [(a, b) for a in range(p) for b in range(p)]
    q, n = len(nodes), 2*len(nodes)
    H = [[zero]*n for _ in range(n)]
    for t, z in enumerate(nodes):
        for r in range(n):
            H[2*t][r] = power(z, r)
            H[2*t+1][r] = scale(r, power(z, r-1)) if r else zero

    def inv_matrix(A):
        aug = [list(row) + [one if i == j else zero for j in range(n)]
               for i, row in enumerate(A)]
        for j in range(n):
            t = next((i for i in range(j, n) if aug[i][j] != zero), None)
            assert t is not None, "Hermite matrix singular"
            aug[j], aug[t] = aug[t], aug[j]
            z = inverse(aug[j][j])
            aug[j] = [mul(z, x) for x in aug[j]]
            for i in range(n):
                if i != j and aug[i][j] != zero:
                    a = aug[i][j]
                    aug[i] = [sub(x, mul(a, y)) for x, y in zip(aug[i], aug[j])]
        assert all(aug[i][j] == (one if i == j else zero)
                   for i in range(n) for j in range(n))
        return [row[n:] for row in aug]

    HI = inv_matrix(H)
    OH = []
    for t in range(q):
        OH.append(H[2*t+1])
        OH.append([scale(-1, z) for z in H[2*t]])

    U = [[zero]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            z = zero
            for k in range(n):
                if HI[i][k] != zero and OH[k][j] != zero:
                    z = add(z, mul(HI[i][k], OH[k][j]))
            U[i][j] = z
    assert all(b == 0 for row in U for a, b in row), "no Frobenius descent"
    Um = [[z[0] for z in row] for row in U]
    assert all(sum(Um[i][k]*Um[k][j] for k in range(n)) % p ==
               (-int(i == j)) % p for i in range(n) for j in range(n))

    def determinant(A):
        A = [row[:] for row in A]
        d = 1
        for j in range(n):
            t = next((i for i in range(j, n) if A[i][j] % p), None)
            assert t is not None
            if t != j:
                A[j], A[t] = A[t], A[j]
                d = -d
            pivot = A[j][j] % p
            d = d*pivot % p
            z = pow(pivot, -1, p)
            for i in range(j+1, n):
                a = A[i][j]*z % p
                if a:
                    for k in range(j+1, n):
                        A[i][k] = (A[i][k]-a*A[j][k]) % p
                    A[i][j] = 0
        return d % p

    assert determinant(Um) == 1

    # Both the Frobenius and fixed-W ordinary derivative conventions.
    for z in nodes:
        w = power(z, p)
        assert w == (z[0], (-z[1]) % p)
        assert power(z, p*p) == z
        for s in range(2):
            ww = power(w, s)
            v0 = [mul(power(z, r), ww) for r in range(n)]
            v1 = [scale(r, mul(power(z, r-1), ww)) if r else zero
                  for r in range(n)]
            mapped0 = [(sum(Um[r][t]*v0[r][0] for r in range(n)) % p,
                        sum(Um[r][t]*v0[r][1] for r in range(n)) % p)
                       for t in range(n)]
            mapped1 = [(sum(Um[r][t]*v1[r][0] for r in range(n)) % p,
                        sum(Um[r][t]*v1[r][1] for r in range(n)) % p)
                       for t in range(n)]
            assert mapped0 == v1
            assert mapped1 == [scale(-1, x) for x in v0]

    assert 2 % p != 0   # Second derivative of g at each node is 2, not zero.
    print("INERT_HERMITE", {"p": p, "D": D, "nodes": q,
        "Hermite_dimension": n, "U_entries": n*n,
        "U_over_Fp": True, "U_squared": "-I", "detU": 1,
        "ordinary_J2_every_node": True, "j2_not_covered": True})


if __name__ == "__main__":
    pilot(3, 7)
    pilot(5, 3)
    print("PASS inert original-jet two-jet Hermite pilots")
