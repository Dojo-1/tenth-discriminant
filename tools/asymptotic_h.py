"""Asymptotic closure for class number <= H, all D >= 1e102 (pre-registered parameters K=1e17, C=80).
Changes vs asymptotic.py (h=1), as listed in flow/PREREG_H2.md:
 (i)  O_K lattice: area 2 pi rho^2/sqrt D, so rho = 1.001 sqrt((3R+S) sqrt D/(2 pi)) + 10 sqrt D;
      lines M <= 2*(2 rho/sqrt D) + 1, points per line <= 2 rho + 2.
 (ii) split mass (normalized by R^2 S, c/(R^2S)=1/2), from cover_h.split_mass_h with
      alpha = H pi/(2 sqrt D), beta = H (3D)^(-1/4), gamma = H/4:
        SPLIT <= alpha (Lam + Lam^2/2) + beta (Lam/sqrt R + 2(log 3+1)/sqrt 3) + gamma (Lam/R + log 3/3)
      every term except gamma log3/3 decreases in u; that one is a constant moved into B.
 (iii) ramified: <= sum over the omega-1 <= floor(log2 H)+1 smallest odd primes of log p/p (F(p) <= S R^2/(2p)); constant -> B.
Lower prime mass and upper bound otherwise identical to asymptotic.py (Dusart 2010, eta = 0.2, x >= 3 594 641).
"""
import sys, math
sys.path.insert(0, 'tools')
from flint import arb
from green_h1 import primes_upto
from sympy import prime

H = int(sys.argv[1]) if len(sys.argv) > 1 else 2
K, C, P1 = arb(10) ** 17, 80, 10544111
ETA2 = arb("0.2")
u0 = arb(10).log() * 102
D0 = u0.exp()
logK, log3, pi = K.log(), arb(3).log(), arb.pi()
theta_P1 = sum((arb(int(p)).log() for p in primes_upto(P1)), arb(0))

Lam0 = u0 + logK
R0 = K * D0; S0 = R0 / C
cst = (3 + arb(1) / C) / (2 * pi)                                   # rho^2 ~ cst R sqrt D
c_rho = (arb("1.001") * cst.sqrt() + 10 * D0 ** (-arb(1) / 4) / K.sqrt()).log()
c_Rr = -(cst.sqrt()).log()                                          # log(R/rho) <= Lam/2 - u/4 + c_Rr
rho0 = (Lam0 / 2 + u0 / 4 + c_rho).exp()

A = 1 - arb(3) / 4 * (1 + arb(1) / C) - arb(2) / C / 4
om = int(math.floor(math.log2(H))) + 1
RAM = sum((arb(prime(k)).log() / prime(k) for k in range(2, om + 2)), arb(0))
GAMMA_CONST = arb(H) / 4 * log3 / 3
B = (logK - log3 - arb(P1).log() - theta_P1 / P1 - ETA2 / arb(P1).log() - arb(2 * C) / (3 * P1)) \
    - (1 + arb(1) / C) * (logK / 2 + c_rho) - (arb(2) / C) * (logK / 2 + c_Rr) + arb(2) / C \
    - RAM - GAMMA_CONST

eps0 = 1 / (2 * R0) + 1 / (4 * S0)
al0 = arb(H) * pi / (2 * D0.sqrt()); be0 = arb(H) * (3 * D0) ** (-arb(1) / 4); ga = arb(H) / 4
SPLIT_dec = al0 * (Lam0 + Lam0 ** 2 / 2) + be0 * (Lam0 / R0.sqrt() + 2 * (log3 + 1) / arb(3).sqrt()) + ga * Lam0 / R0
E = 2 * eps0 * Lam0 + SPLIT_dec + (2 * R0 ** 3).log() / R0 + (arb(2) / C) * (rho0 / R0 + Lam0 / R0)
h0 = A * u0 + B - E

# hypotheses at u0, each monotone improving in D
need = 3 * R0 + S0
rho_lo = arb("1.001") * (need * D0.sqrt() / (2 * pi)).sqrt()
n_low = 2 * pi * rho_lo ** 2 / D0.sqrt() - 2 * rho_lo - (4 * rho_lo / D0.sqrt() + 1)
L_plus_M = 2 * rho0 + 2 + 4 * rho0 / D0.sqrt() + 1
hyp = {
    "J >= L+M": bool(S0 > L_plus_M),
    "n J > 2RS+J(R+S)": bool(n_low > need),
    "T=R/3 > P1 >= C": bool(R0 / 3 > P1) and P1 >= C,
    "G(T) > 0": bool((arb(1) / 2 - 3 * eps0) * 3 / R0 - arb(9) * C / (6 * R0 ** 2) - 1 / R0 > 0),
    "2b/a <= P1": bool(arb(2 * C) / 3 / (1 - 2 * eps0) <= P1),
}
print(f"H={H}: slope A = {A.str(6)};  constants RAM={RAM.str(4)}, gamma-term={GAMMA_CONST.str(4)}")
print("h(u0) lower bound =", h0.str(6), " (u0 = log 1e102); monotone: A > 0 and E decreasing")
for k, v in hyp.items(): print(f"  hypothesis {k:18} {v}")
print("ASYMPTOTIC CLOSURE CERTIFIED:", bool(h0 > 0) and bool(A > 0) and all(hyp.values()))
