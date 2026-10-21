"""BEAN — class number one with no split-prime counting.

If h(-D) = 1 (D > 163), every prime p < (D+1)/4 is inert (Rabinowitsch).  Take R <= (D+1)/4: then every odd prime <= R is
inert, so the inert-prime mass is the WHOLE prime mass up to R — nothing to subtract.  Green's determinant on the norm ellipse
{z in Z[sqrt(-D)] : |z| <= rho} then gives a contradiction once  prime_mass(R,S) > Hadamard bound.

certify(D1, D2):  True  =>  h(-D) != 1 for every D in [D1, D2].
  R = (D1+1)//4 works for all D >= D1;  rho is fixed, so the upper bound uses n_up(D1), the hypotheses use n_low(D2).
"""
import sys
sys.path.insert(0, 'tools')
from flint import arb
from cover import prime_mass, rho_for
from green_h1_ellipse import upper_B

def certify(D1, D2, C):
    R = (D1 + 1) // 4; S = R // C; J = S
    rho = arb(rho_for(D2, R, S)); s1, s2 = arb(D1).sqrt(), arb(D2).sqrt()
    n_low = arb.pi() * rho * rho / s2 - 2 * rho / s2 - 6 * rho
    L = 2 * int(rho.upper().floor().unique_fmpz()) + 1
    M = 2 * int((rho / s1).upper().floor().unique_fmpz()) + 1
    if not (n_low * J > 2 * R * S + J * (R + S) and J >= L + M): return False, 0.0
    U = upper_B(R, S, J, arb.pi() * rho * rho / s1 + 2 * rho + M, rho)
    Lo = prime_mass(R, S)
    return bool(Lo > U), float((Lo / U).mid())

def cover(D1, Dend, Q):
    while D1 < Dend:
        D2 = int(D1 * Q)
        hit = next(((C, m) for C in (20, 40, 80, 160) for ok, m in [certify(D1, D2, C)] if ok), None)
        print(f"[{D1:.4e}, {D2:.4e}]  " + (f"CERTIFIED C={hit[0]} margin={hit[1]:.4f}" if hit else "FAILED"), flush=True)
        if not hit: return
        D1 = D2

if __name__ == "__main__":
    cover(int(float(sys.argv[1])), int(float(sys.argv[2])), float(sys.argv[3]))
