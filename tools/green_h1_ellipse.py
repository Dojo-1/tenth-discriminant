"""Variant GREEN-H1-E: evaluation points = lattice points of Z[sqrt(-D)] inside the norm ellipse
x^2 + D y^2 <= rho^2 (a disc of radius rho in C), instead of Green's N x N square grid.
Changes vs green_h1.py:
 [E1] zero bound: points lie on M = 2Y0+1 horizontal lines y=c, each with <= L = 2*floor(rho)+1 points;
      nonzero F of degree k vanishes on <= k(L+M) of them  => need J >= L + M.
 [E2] count: with rho = (Y0+1/2) sqrt D, concavity (midpoint rule) gives n >= pi rho^2/sqrt D - 2 rho/sqrt D.
 [E3] archimedean: |z| = |z'| <= rho, so B = rho.
Lower bound (inert prime mass) is unchanged."""
import sys, math
sys.path.insert(0, 'tools')
from flint import arb
from green_h1 import lower, primes_upto

def upper_B(R, S, J, n, B):
    U = arb(R * S) * (arb(2) * n * J).log()
    U += 2 * B.log() * arb(S * R * (R - 1) // 2 + R * S * (S - 1) // 2)
    if R > B:
        Lg = (arb(R) / B).log()
        U += 2 * S * (J - 1) * (arb(R) * Lg - R + B + Lg)
    return U

def check_ellipse(D, R, S, P0, primes):
    sd = arb(D).sqrt()
    # smallest Y0 with n_low * J > 2RS + J(R+S), J = S
    J = S
    need = (arb(2 * R * S) + arb(J) * (R + S)) / J
    Y0 = 1
    while True:
        rho = (arb(Y0) + arb(1) / 2) * sd
        n_low = arb.pi() * rho * rho / sd - 2 * rho / sd
        if n_low > need: break
        Y0 = int(Y0 * 1.01) + 1
    L = 2 * int(rho.upper().floor().unique_fmpz()) + 1
    M = 2 * Y0 + 1
    assert J >= L + M, ("E1 fails", J, L + M)
    n_up = arb.pi() * rho * rho / sd + 2 * rho + M   # sum of concave f <= integral + max f, plus 1 per line
    U = upper_B(R, S, J, n_up, rho)
    Lo, T = lower(R, S, D, P0, primes)
    return Lo, U

if __name__ == "__main__":
    pr = primes_upto(10**6)
    for D in [10**4, 10**5, 10**6, 10**8, 10**10, 10**14, 10**20]:
        best = None
        for e in range(0, 20):
            for C in [10, 20, 40, 80, 160, 320]:
                R = int(D * 10**e) if e else D; R = int(R); S = R // C
                try:
                    Lo, U = check_ellipse(D, R, S, 10**6, pr)
                except AssertionError:
                    continue
                r = float((Lo / U).mid())
                if best is None or r > best[0]: best = (r, e, C, bool(Lo > U))
        print(f"D=1e{round(math.log10(D))}: best ratio {best[0]:.4f} at R=D*1e{best[1]} C={best[2]} certified={best[3]}")
