"""BEAN asymptotic closure: h(-D) != 1 for all D >= 1e36.   R = floor((D+1)/4), S = floor(R/C), J = S, C = 80,
rho = 1.001 sqrt((3R+S) sqrt D/pi) + 10 sqrt D.   Normalize by R^2 S; u = log D; Lam = log R in [u - log4 - 4/D, u - log4 + 1/D].
LOWER (all odd p <= R inert; drop p <= P1; Dusart tail on [P1, R/3]):
   L >= Lam - log3 - log P1 - theta(P1)/P1 - eta/log P1 - 2C/(3P1) - 2 eps Lam,      eps = 1/(2R) + 1/(4S)
UPPER (as asymptotic.py):
   U <= (1+1/C) log rho + (2/C) log(R/rho) - 2/C + log(2nJ)/R + (2/C)(rho/R + log(R/rho)/R)
   log rho <= Lam/2 + u/4 + log(1.001 sqrt((3+1/C)/pi) + 10 D^(-1/4) R^(-1/2) D^(1/2)... ) — see c_rho below
   log(R/rho) <= Lam/2 - u/4 + (1/2) log(pi/(3+1/C))
=> (L-U) >= A u + B - E(u0) with A = 1 - (3/4)(1+1/C) - (2/C)(1/4) = 15/64 - ..., E decreasing; check at u0.
No split-prime or ramified terms appear: that is the point of the route.
"""
import sys
sys.path.insert(0, 'tools')
from flint import arb
from green_h1 import primes_upto

C, P1, ETA = 80, 10544111, arb("0.2")
u0 = arb(10).log() * 36; D0 = u0.exp(); pi, log3, log4 = arb.pi(), arb(3).log(), arb(4).log()
theta_P1 = sum((arb(int(p)).log() for p in primes_upto(P1)), arb(0))

R0 = (D0 + 1) / 4 - 1; S0 = R0 / C - 1                       # lower values (floors)
Lam_lo = R0.log(); Lam_hi = ((D0 + 1) / 4).log()
cst = (3 + arb(1) / C) / pi
# rho <= 1.001 sqrt(cst R sqrt D) + 10 sqrt D  = sqrt(R sqrt D) [1.001 sqrt(cst) + 10 D^(1/4) R^(-1/2)],  D^(1/4) R^(-1/2) <= 2.1 D^(-1/4)
c_rho = (arb("1.001") * cst.sqrt() + 10 * arb("2.1") * D0 ** (-arb(1) / 4)).log()
c_Rr = -(cst.sqrt()).log() / 1                                # log(R/rho) <= Lam/2 - u/4 + c_Rr  (rho >= sqrt(cst R sqrt D))
rho0 = (Lam_hi / 2 + u0 / 4 + c_rho).exp()

A = 1 - arb(3) / 4 * (1 + arb(1) / C) - arb(2) / C / 4
# write Lam = u - log4 + delta, |delta| <= 4/D0; collect constants
B = (-log4 - log3 - arb(P1).log() - theta_P1 / P1 - ETA / arb(P1).log() - arb(2 * C) / (3 * P1)) \
    - (1 + arb(1) / C) * (-log4 / 2 + c_rho) - (arb(2) / C) * (-log4 / 2 + c_Rr) + arb(2) / C
eps0 = 1 / (2 * R0) + 1 / (4 * S0)
E = 2 * eps0 * Lam_hi + (2 * R0 ** 3).log() / R0 + (arb(2) / C) * (rho0 / R0 + Lam_hi / R0) + 8 / D0
h0 = A * u0 + B - E

need = 3 * R0 + S0
rho_lo = arb("1.001") * (need * D0.sqrt() / pi).sqrt()
n_low = pi * rho_lo ** 2 / D0.sqrt() - 2 * rho_lo / D0.sqrt() - 6 * rho_lo
hyp = {
    "J >= L+M": bool(S0 > 2 * rho0 + 1 + 2 * rho0 / D0.sqrt() + 1),
    "nJ > 2RS+J(R+S)": bool(n_low > need + 1),
    "R/3 > P1 >= C": bool(R0 / 3 > P1),
    "G(R/3) > 0": bool((arb(1) / 2 - 3 * eps0) * 3 / R0 - arb(9) * C / (6 * R0 ** 2) - 1 / R0 > 0),
    "2b/a <= P1": bool(arb(2 * C) / 3 / (1 - 2 * eps0) <= P1),
    "every odd p <= R inert (R < (D+1)/4)": True,
}
print("slope A =", A.str(6), "  h(u0) =", h0.str(6), " at D0 = 1e36")
for k, v in hyp.items(): print(f"  {k:38} {v}")
print("BEAN ASYMPTOTIC CLOSURE CERTIFIED:", bool(h0 > 0) and bool(A > 0) and all(hyp.values()))
