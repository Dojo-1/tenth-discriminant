"""Class number <= H, elementary route (flow/x.md obligations O1-O8). Status: GUESS under attack.

certify_h(D1, D2, H, R, S, rho): True => every imaginary quadratic field with D1 <= |disc| <= D2 has h > H.
Lattice O_K = Z[w] (covolume sqrt(D)/2), points |z| <= rho. Differences from cover.py (h = 1, Z[sqrt -D]):
  O2  point count: area A = 2 pi rho^2/sqrt D;  A - 2rho - M <= n <= A + 2rho + M;  M = 2 floor(2rho/sqrt D) + 1 lines.
  O5  #{split p <= t} <= alpha t + beta sqrt t + gam,  alpha = H pi/(2 sqrt D),
      beta = H (3D)^(-1/4),  gam = H/4      (sum over H forms of [area + one per line], / 4 reps)
  O6  ramified: subtract sum over the omega <= 1 + log2 H smallest odd primes of log p F(p)  (worst case).
Upper bound and the inert-prime mass (O3, O7) are reused unchanged from cover.py.
"""
import sys, math
sys.path.insert(0, 'tools')
from flint import arb
from cover import prime_mass
from green_h1 import F_exact
from green_h1_ellipse import upper_B
from sympy import prime

def split_mass_h(R, S, D, H):
    c = arb(S) * R * R / 2; sd = arb(D).sqrt()
    al = arb(H) * arb.pi() / (2 * sd)
    be = arb(H) * (3 * arb(D)) ** (-arb(1) / 4)
    ga = arb(H) / 4
    t0, Ra = arb(3), arb(R)
    lt0, lR = t0.log(), Ra.log()
    I1 = al * c * ((lR * lR - lt0 * lt0) / 2 - (lR - lt0))
    I2 = be * c * (-2 * (lR + 1) / Ra.sqrt() + 2 * (lt0 + 1) / t0.sqrt())
    I3 = ga * c * (lt0 / t0 - lR / Ra)                     # int gam (-w') = gam (w(t0) - w(R))
    end = c * lR / Ra * (al * Ra + be * Ra.sqrt() + ga)
    return 2 * (end + I1 + I2 + I3)

def ramified_mass_h(R, S, H):
    om = 1 + int(math.floor(math.log2(H))) if H >= 1 else 1
    return 2 * sum((arb(prime(k)).log() * F_exact(prime(k), R, S) for k in range(2, om + 2)), arb(0))  # odd primes 3,5,7,...

def certify_h(D1, D2, H, R, S, rho):
    J = S; rho = arb(rho)
    s1, s2 = arb(D1).sqrt(), arb(D2).sqrt()
    M1 = 2 * int((2 * rho / s1).upper().floor().unique_fmpz()) + 1        # max lines (at D1)
    M2 = 2 * int((2 * rho / s2).lower().floor().unique_fmpz()) + 1        # min lines (at D2)
    n_low = 2 * arb.pi() * rho * rho / s2 - 2 * rho - M1                 # A(D2) - 2rho - M (M at its max: safe)
    if not n_low * J > 2 * R * S + J * (R + S): return False, "n"
    L = 2 * int(rho.upper().floor().unique_fmpz()) + 2                  # <= 2 rho + 1 per line, +1 for half-integer shift
    if J < L + M1: return False, "J"
    n_up = 2 * arb.pi() * rho * rho / s1 + 2 * rho + M1
    U = upper_B(R, S, J, n_up, rho)
    Lo = prime_mass(R, S) - split_mass_h(R, S, D1, H) - ramified_mass_h(R, S, H)
    return bool(Lo > U), float((Lo / U).mid())

def rho_for_h(D2, R, S):
    need = (2 * R * S + S * (R + S)) / S
    return math.sqrt(need * math.sqrt(D2) / (2 * math.pi)) * 1.001 + 10 * math.sqrt(D2)

def threshold(H, lo=10**2, hi=10**40):
    """smallest-ish D (bisection on log scale) where a point check D1=D2 certifies."""
    def ok(D):
        for e in range(6, 24, 2):
            for C in [40, 80, 160]:
                R = D * 10**e; S = R // C
                if certify_h(D, D, H, R, S, rho_for_h(D, R, S))[0]: return True
        return False
    while hi / lo > 1.2:
        mid = int((lo * hi) ** 0.5)
        if ok(mid): hi = mid
        else: lo = mid
    return hi

def cover(H, D1, Dend, Q):
    out = []
    while D1 < Dend:
        D2 = int(D1 * Q); hit = None
        for e in range(6, 24):
            for C in [40, 80, 160]:
                R = D1 * 10**e; S = R // C
                ok, info = certify_h(D1, D2, H, R, S, rho_for_h(D2, R, S))
                if ok: hit = (e, C, info); break
            if hit: break
        line = f"[{D1:.4e}, {D2:.4e}]  " + (f"CERTIFIED R=D1*1e{hit[0]} C={hit[1]} margin={hit[2]:.4f}" if hit else "FAILED")
        print(line, flush=True); out.append(line)
        if not hit: break
        D1 = D2
    return out

if __name__ == "__main__":
    H = int(sys.argv[1]); D1 = int(float(sys.argv[2])); Dend = int(float(sys.argv[3])); Q = float(sys.argv[4])
    cover(H, D1, Dend, Q)
