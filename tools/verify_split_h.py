"""O5 attack: (i) total representations of a split prime over all reduced forms of disc -D equals 4;
(ii) #{split p <= t} <= alpha t + beta sqrt t + gamma with H = h(-D)."""
import math
from sympy import primerange, isprime
from sympy.ntheory import legendre_symbol
def kron(Dn, p):   # Kronecker (Dn / p), p odd prime
    return legendre_symbol(Dn % p, p) if Dn % p else 0
def reduced_forms(D):
    out = []
    for a in range(1, int(math.isqrt(D // 3)) + 2):
        for b in range(-a + 1, a + 1):
            if (b * b + D) % (4 * a): continue
            c = (b * b + D) // (4 * a)
            if c < a or (c == a and b < 0) or math.gcd(math.gcd(a, abs(b)), c) != 1: continue
            out.append((a, b, c))
    return out
def reps(f, n):
    a, b, c = f; D = 4 * a * c - b * b; cnt = 0
    Y = int(math.isqrt(4 * a * n // D)) + 1
    for y in range(-Y, Y + 1):
        X = int(math.isqrt(4 * c * n // D)) + 2   # crude bound on |x|
        for x in range(-X - abs(b * y) // (2 * a) - 2, X + abs(b * y) // (2 * a) + 3):
            if a * x * x + b * x * y + c * y * y == n: cnt += 1
    return cnt
bad = 0
for D in [15, 20, 23, 39, 47, 56, 71, 84, 95, 119, 143, 167, 191, 239, 251, 311, 359]:
    F = reduced_forms(D); h = len(F)
    split = [p for p in primerange(3, 600) if D % p and kron(-D, p) == 1]
    tot = {p: sum(reps(f, p) for f in F) for p in split[:25]}
    ok4 = all(v == 4 for v in tot.values())
    worst = 0
    for t in [50, 100, 200, 400, 599]:
        A = sum(1 for p in split if p <= t)
        B = h * math.pi / (2 * math.sqrt(D)) * t + h * (3 * D) ** -0.25 * math.sqrt(t) + h / 4
        worst = max(worst, A / B)
    bad += (not ok4) or worst > 1
    print(f"disc=-{D:3d} h={h:2d}: reps==4 for all split p tested: {ok4};  max A/bound = {worst:.3f}")
print("FAILURES:", bad)
