"""Exact attack on O1, O2, O4 for the maximal order O_K (composite and even discriminants).
K = Q(sqrt(-m)), m squarefree. Elements as exact pairs (a, b) = a + b sqrt(-m), a, b in (1/2)Z.
O_K basis: m = 3 mod 4 -> (1, w), w = (1+sqrt(-m))/2, disc -m;  else (1, sqrt(-m)), disc -4m.
Points z = x + y*e2 with |z| <= rho; 'lines' = fixed y.  Gram entry = sum 2 Re(alpha conj beta) (integer).
Checks: hypothesis, det > 0, Hadamard, v_p(det) >= 2F(p) for odd inert p <= R, O2 count bounds.
"""
import sys, math, subprocess
from fractions import Fraction as Fr
sys.path.insert(0, 'tools')
from green_h1 import F_exact
from sympy import primerange, factorint

def setup(m):
    if m % 4 == 3: return m, (Fr(1, 2), Fr(1, 2))    # disc = -m
    return 4 * m, (Fr(0), Fr(1))                      # disc = -4m

def mul(u, v, m): return (u[0] * v[0] - m * u[1] * v[1], u[0] * v[1] + u[1] * v[0])

def points(m, rho):
    D, e2 = setup(m); P = []
    Y = int(2 * rho / math.sqrt(D)) + 2
    for y in range(-Y, Y + 1):
        b = y * e2[1]; a0 = y * e2[0]
        for x in range(-int(rho) - 2, int(rho) + 3):
            a = x + a0
            if a * a + m * b * b <= rho * rho: P.append((x, y, (a, b)))
    return D, P

def gram(P, R, S, J, m):
    rows = []
    for r in range(R):
        for s in range(S):
            row = []
            for (_, _, z) in P:
                zb = (z[0], -z[1])
                for j in range(J):
                    if j > r: row.append((Fr(0), Fr(0))); continue
                    t = (Fr(1), Fr(0))
                    for _ in range(r - j): t = mul(t, z, m)
                    for _ in range(s): t = mul(t, zb, m)
                    c = math.perm(r, j); row.append((c * t[0], c * t[1]))
            rows.append(row)
    G = [[sum(2 * (a[0] * b[0] + m * a[1] * b[1]) for a, b in zip(u, v)) for v in rows] for u in rows]
    assert all(g.denominator == 1 for row in G for g in row), "Gram entry not an integer"
    return [[int(g) for g in row] for row in G]

def det(M):
    s = "matdet(Mat([" + ";".join(",".join(map(str, r)) for r in M) + "]))"
    res = subprocess.run(["gp", "-q", "-D", "colors=no", "-s", "1G"], input=s, capture_output=True, text=True)
    if res.returncode or res.stderr.strip(): raise RuntimeError(res.stderr)
    return int(res.stdout.strip())

def kron(Dneg, p):
    res = subprocess.run(["gp", "-q", "-D", "colors=no"], input=f"kronecker({Dneg},{p})", capture_output=True, text=True)
    return int(res.stdout.strip())

def vp(n, p):
    k = 0
    while n % p == 0: n //= p; k += 1
    return k

if __name__ == "__main__":
    fails = tested = 0
    for m in [15, 35, 39, 55, 95, 5, 6, 14, 21, 30, 3*5*7*11 - 0 if False else 105]:
        D, _ = setup(m)
        for rho in [3.5, 5.2]:
            D, P = points(m, rho)
            lines = {}
            for (x, y, _) in P: lines[y] = lines.get(y, 0) + 1
            L, M, n = max(lines.values()), len(lines), len(P)
            A = 2 * math.pi * rho ** 2 / math.sqrt(D)
            Mf = 2 * math.floor(2 * rho / math.sqrt(D)) + 1
            o2 = A - 2 * rho - Mf <= n <= A + 2 * rho + Mf and M <= Mf
            for (R, S) in [(9, 2), (12, 3)]:
                J = L + M
                if not n * J > 2 * R * S + J * (R + S): continue
                G = gram(P, R, S, J, m); d = det(G)
                inert = [p for p in primerange(3, R + 1) if D % p and kron(-D, p) == -1]
                ok = d > 0 and d <= math.prod(G[i][i] for i in range(len(G))) and o2 \
                     and all(vp(d, p) >= 2 * F_exact(p, R, S) for p in inert)
                tested += 1; fails += not ok
                print(f"disc=-{D:4d} (ramified {sorted(factorint(D))}) rho={rho} n={n} R={R} S={S} J={J} inert={inert}: {'ok' if ok else 'FAIL'}")
    print(f"{tested} cases, {fails} failures")
