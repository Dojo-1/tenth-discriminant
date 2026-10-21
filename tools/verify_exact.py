"""Exact verifier for the determinant ingredients, for ANY finite point set in Z[sqrt(-D)].

For a point set P (pairs (x,y) meaning x + y sqrt(-D)) and parameters (R,S,J) it computes the Gram
matrix G exactly and checks, against exact integers, every inequality the bound relies on:

  [A] independence hypothesis holds        J >= (points per line) + (#lines),  nJ > 2RS + J(R+S)
  [B] det G > 0                            (Green Lemma 3.1)
  [C] det G <= prod G_ii                   (Hadamard)
  [D] log prod G_ii <= U(R,S,J,n,B)        (my aggregated upper bound, B = max |z|)
  [E] v_p(det G) >= 2 F(p), inert p <= R   (Green Lemma 5.1)
  [F] n_low <= n <= n_up                   (ellipse point count, ellipse shapes only)

One exact computation, six independent ways for the argument to be wrong.
"""
import sys, math, subprocess
sys.path.insert(0, 'tools')
from flint import arb
from sympy import primerange, legendre_symbol
from green_h1 import F_exact
from green_h1_ellipse import upper_B

# ---------- point sets ----------
def square(N):            # Green's grid
    return [(x, y) for x in range(N) for y in range(N)]

def ellipse(D, Y0):       # lattice points of x^2 + D y^2 <= rho^2, rho = (Y0 + 1/2) sqrt D
    rho2 = (Y0 + 0.5) ** 2 * D
    return [(x, y) for y in range(-Y0, Y0 + 1)
            for x in range(-math.isqrt(int(rho2)), math.isqrt(int(rho2)) + 1)
            if x * x + D * y * y <= rho2]

# ---------- exact algebra in Z[sqrt(-D)] ----------
def mul(u, v, D): return (u[0] * v[0] - D * u[1] * v[1], u[0] * v[1] + u[1] * v[0])

def powers(u, n, D):
    out = [(1, 0)]
    for _ in range(n): out.append(mul(out[-1], u, D))
    return out

def gram(P, R, S, J, D):
    zp = [powers((x, y), R, D) for (x, y) in P]      # z = x + y w
    zq = [powers((x, -y), S, D) for (x, y) in P]     # z' = x - y w
    rows = []
    for r in range(R):
        for s in range(S):
            row = []
            for i in range(len(P)):
                for j in range(J):
                    if j > r: row.append((0, 0)); continue
                    c = math.perm(r, j)
                    t = mul(zp[i][r - j], zq[i][s], D)
                    row.append((c * t[0], c * t[1]))
            rows.append(row)
    return [[sum(2 * (a[0] * b[0] + D * a[1] * b[1]) for a, b in zip(u, v)) for v in rows] for u in rows]

def det(M):
    # Review F4: Mat(...) so a 1x1 input is a matrix, not a vector; surface gp errors instead of discarding them.
    s = "matdet(Mat([" + ";".join(",".join(map(str, r)) for r in M) + "]))"
    res = subprocess.run(["gp", "-q", "-D", "colors=no", "-s", "1G"], input=s, capture_output=True, text=True)
    if res.returncode or res.stderr.strip() or not res.stdout.strip():
        raise RuntimeError("gp failed: " + res.stderr.strip())
    return int(res.stdout.strip())

def vp(n, p):
    k = 0
    while n % p == 0: n //= p; k += 1
    return k

# ---------- one case ----------
def run(shape, D, R, S, J, P, Y0=None):
    n = len(P)
    lines = {}
    for (x, y) in P: lines.setdefault(y, 0); lines[y] += 1
    L, M = max(lines.values()), len(lines)
    ok = {}
    ok["A"] = J >= L + M and n * J > 2 * R * S + J * (R + S)
    if not ok["A"]:
        return None
    G = gram(P, R, S, J, D)
    d = det(G)
    diag = [G[i][i] for i in range(len(G))]
    ok["B"] = d > 0
    ok["C"] = d <= math.prod(diag)
    B = max(arb(x * x + D * y * y).sqrt() for (x, y) in P)
    # Review F4: Arb throughout (no float logs); certified comparison of balls.
    lhs = sum((arb(g).log() for g in diag), arb(0))
    ok["D"] = bool(lhs < upper_B(R, S, J, arb(n), B))
    inert = [p for p in primerange(3, R + 1) if D % p and legendre_symbol((-D) % p, p) == -1]
    ok["E"] = all(vp(d, p) >= 2 * F_exact(p, R, S) for p in inert)
    if shape == "ellipse":
        sd = arb(D).sqrt(); rho = (arb(Y0) + arb(1) / 2) * sd   # Review F4: Arb, certified
        ok["F"] = bool(arb.pi() * rho * rho / sd - 2 * rho / sd <= n) and bool(arb(n) <= arb.pi() * rho * rho / sd + 2 * rho + M)
    strength = max([2 * F_exact(p, R, S) for p in inert], default=0)
    return ok, n, L + M, inert, strength

if __name__ == "__main__":
    cases = []
    for D in [7, 11, 19, 23, 43, 67]:
        for Y0 in [1, 2]:
            P = ellipse(D, Y0)
            for (R, S) in [(6, 2), (9, 3), (12, 3)]:
                lines = {}
                for (_, y) in P: lines[y] = lines.get(y, 0) + 1
                J = max(lines.values()) + len(lines)
                cases.append(("ellipse", D, R, S, J, P, Y0))
        for (R, S, N) in [(9, 3, 5), (12, 3, 6)]:
            cases.append(("square", D, R, S, 2 * N, square(N), None))
    fails = 0; tested = 0
    print(f"{'shape':8} {'D':>3} {'R':>3} {'S':>2} {'J':>3} {'n':>4}  checks            inert  max 2F(p)")
    for c in cases:
        res = run(*c)
        if res is None: continue
        ok, n, LM, inert, strength = res
        tested += 1; bad = [k for k, v in ok.items() if not v]; fails += bool(bad)
        flags = " ".join(k + ("✓" if v else "✗") for k, v in ok.items())
        print(f"{c[0]:8} {c[1]:>3} {c[2]:>3} {c[3]:>2} {c[4]:>3} {n:>4}  {flags:17} {str(inert):12} {strength}")
    print(f"\n{tested} cases, {fails} failures")
