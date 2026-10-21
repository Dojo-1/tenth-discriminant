"""Mutation test: the exact verifier must REJECT deliberately wrong claims."""
import sys, math
sys.path.insert(0, 'tools')
from verify_exact import ellipse, gram, det, vp
from green_h1 import F_exact
from sympy import primerange, legendre_symbol
caught = {}
# M1: claim v_p(det) >= 2F(p) + 2  (too strong)  -> should be violated somewhere
# M2: claim det <= prod G_ii / 10^6 (too strong Hadamard) -> should be violated somewhere
# M3: drop the independence hypothesis (J far too small) -> det should become 0 somewhere
for D in [7, 19, 43]:
    P = ellipse(D, 1)
    for (R, S) in [(9, 3), (12, 3)]:
        J = 18
        G = gram(P, R, S, J, D); d = det(G)
        inert = [p for p in primerange(3, R + 1) if D % p and legendre_symbol((-D) % p, p) == -1]
        if any(vp(d, p) < 2 * F_exact(p, R, S) + 2 for p in inert): caught["M1 v_p too strong"] = True
        if d > math.prod(G[i][i] for i in range(len(G))) // 10**6: caught["M2 Hadamard too strong"] = True
        for Jbad in [1, 2]:
            if det(gram(P, R, S, Jbad, D)) == 0: caught["M3 hypothesis dropped -> det=0"] = True
for m in ["M1 v_p too strong", "M2 Hadamard too strong", "M3 hypothesis dropped -> det=0"]:
    print(f"{m:34} caught: {caught.get(m, False)}")
