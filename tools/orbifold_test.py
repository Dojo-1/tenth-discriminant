"""Orbifold test: the ellipse set P is invariant under G = <z->-z, z->conj z>. Rows z^r conj(z)^s have parity (-1)^(r+s)
under z->-z, so for P = -P the Gram matrix is block diagonal (even/odd sectors): det G = det G_even * det G_odd.
Question: does one sector alone give a better ratio  (p-adic lower bound) / (log det)  than the full matrix?"""
import sys, math, subprocess
sys.path.insert(0, 'tools')
from verify_exact import ellipse, gram, det, vp
from green_h1 import F_exact
from sympy import primerange, legendre_symbol
def sector(G, R, S, par):
    idx = [r * S + s for r in range(R) for s in range(S) if (r + s) % 2 == par]
    return [[G[i][j] for j in idx] for i in idx], idx
for D in [7, 19, 43]:
    P = ellipse(D, 2); R, S = 12, 3
    lines = {}
    for (_, y) in P: lines[y] = lines.get(y, 0) + 1
    J = max(lines.values()) + len(lines)
    G = gram(P, R, S, J, D)
    off = max(abs(G[i][j]) for i in range(R*S) for j in range(R*S) if ((i//S)+(i%S)) % 2 != ((j//S)+(j%S)) % 2)
    d = det(G); Ge, ie = sector(G, R, S, 0); Go, io = sector(G, R, S, 1); de, do = det(Ge), det(Go)
    inert = [p for p in primerange(3, R + 1) if D % p and legendre_symbol((-D) % p, p) == -1]
    def report(name, dd, rows):
        pv = sum(vp(dd, p) * math.log(p) for p in inert); 
        return f"{name}: rows={len(rows):2d} log det={math.log(dd):8.1f}  inert-prime part of log det={pv:7.1f}  share={pv/math.log(dd):.3f}"
    print(f"D={D}: max off-sector entry = {off} (0 => orbifold splitting exact);  det = det_even*det_odd: {d == de*do}")
    for line in [report("full", d, range(R*S)), report("even", de, ie), report("odd ", do, io)]: print("   ", line)
