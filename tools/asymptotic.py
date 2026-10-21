"""Asymptotic closure: h(-D) != 1 for ALL D >= D* = 10^102, by one monotone inequality.

Parameters as functions of D:  R = K D (K = 10^17), C = 80, S = J = floor(R/C),
rho = 1.001 sqrt((3R+S) sqrt(D)/pi) + 10 sqrt(D)   (as in cover.rho_for). u := log D, P1 := 10 544 111.

Everything divided by R^2 S. Write Lam := log R = u + log K.

LOWER (drop all primes <= P1, use tail on [P1, T], T = R/3, Dusart theta >= x(1-M1/log x) for x >= P1):
  L/(R^2S) >= Lam - log 3 - log P1 - theta(P1)/P1 - M1 loglog(R/3) + M1 loglog P1 - 2C/(3 P1)
              - 2 eps Lam - SPLIT - RAM,
  eps = 1/(2R) + 1/(4S);  SPLIT <= nb (4 + sqrt2) Lam / sqrt D, nb = log2(4K)+2 dyadic blocks;
  RAM <= 2 u F(D)/(R^2 S) <= u / D.
UPPER:
  U/(R^2S) <= (1+1/C) log rho + (2/C) log(R/rho) - 2/C + log(2 n J)/R + (2/C)(rho/R + log(R/rho)/R),
  log rho   <= Lam/2 + u/4 + log(1.001 sqrt((3+1/C)/pi) + 10 D^(-1/4)/sqrt K)
  log(R/rho) <= Lam/2 - u/4 + (1/2) log(pi/(3+1/C)),   n <= R^2,  J <= R.
So (L-U)/(R^2S) >= A u + B(u0) - M1 log(u + log K - log 3) - E(u0)   for u >= u0, where
  A = 1 - (3/4)(1+1/C) - (2/C)(1/4),  E collects terms decreasing in u (evaluated at u0, valid for u>=u0).
h(u) := A u + B - E(u0) - M1 log(u + log K) is increasing once A > M1/(u0+log K - log 3); so h(u0) > 0 suffices.
Hypotheses (J >= L+M, n_low J > 2RS + J(R+S), T >= P1 >= R/S, G(T) >= 0, 2b/a = (2C/3)/(1-2eps) <= P1) are checked at u0
and each is monotone in D (ratios scale as positive powers of D).
"""
import sys
sys.path.insert(0, 'tools')
from flint import arb
from green_h1 import primes_upto

K, C, P1 = arb(10) ** 17, 80, 10544111
M1 = arb(0)        # log-log term no longer present (Dusart 2010, k=2 bound)
ETA2 = arb("0.2")  # Dusart 2010: theta(x) >= x(1 - 0.2/ln^2 x), x >= 3 594 641; P1 = 10 544 111 >= that
u0 = arb(10).log() * 102
D0 = u0.exp()
logK, log3, pi = K.log(), arb(3).log(), arb.pi()

theta_P1 = arb(0)
for p in primes_upto(P1):
    theta_P1 += arb(int(p)).log()

Lam0 = u0 + logK
R0 = K * D0
S0 = R0 / C           # floor changes only O(1/S) terms, absorbed in eps-type terms below
c_rho = (arb("1.001") * ((3 + arb(1) / C) / pi).sqrt() + 10 * D0 ** (-arb(1) / 4) / K.sqrt()).log()
c_Rr = ((pi / (3 + arb(1) / C)).log()) / 2
rho0 = (Lam0 / 2 + u0 / 4 + c_rho).exp()

A = 1 - arb(3) / 4 * (1 + arb(1) / C) - arb(2) / C / 4
# constant part B: coefficients of the u-independent pieces in L - U
B = (logK - log3 - arb(P1).log() - theta_P1 / P1 - ETA2 / arb(P1).log() - arb(2 * C) / (3 * P1)) \
    - (1 + arb(1) / C) * (logK / 2 + c_rho) - (arb(2) / C) * (logK / 2 + c_Rr) + arb(2) / C
# decreasing error terms at u0
eps0 = 1 / (2 * R0) + 1 / (4 * S0)
nb = (4 * K).log() / arb(2).log() + 2
E = 2 * eps0 * Lam0 + nb * (4 + arb(2).sqrt()) * Lam0 / D0.sqrt() + u0 / D0 \
    + (2 * R0 ** 3).log() / R0 + (arb(2) / C) * (rho0 / R0 + Lam0 / R0)
h0 = A * u0 + B - E - M1 * (Lam0 - log3).log()
deriv_ok = A > M1 / (Lam0 - log3)

# hypotheses at u0 (all monotone improving in D)
L_plus_M = 2 * rho0 + 1 + 2 * rho0 / D0.sqrt() + 1
need = 3 * R0 + S0
n_low = pi * rho0 ** 2 / D0.sqrt() - 2 * rho0 / D0.sqrt() - 6 * rho0   # rho0 is an upper value; use lower rho:
rho_lo = (arb("1.001") * (need * D0.sqrt() / pi).sqrt())
n_low = pi * rho_lo ** 2 / D0.sqrt() - 2 * rho_lo / D0.sqrt() - 6 * rho_lo
hyp = {
    "J >= L+M": bool(S0 > L_plus_M),
    "n J > 2RS+J(R+S)": bool(n_low > need),
    "T=R/3 >= P1 >= R/S=C": bool(R0 / 3 > P1) and P1 >= C,
    "G(T)>=0": bool((arb(1) / 2 - 3 * eps0) * 3 / R0 - arb(9) * C / (6 * R0 ** 2) - 1 / R0 > 0),
    # Review F3: 2b/a = (2C/3)/(1 - 2 eps), not 2C/3; eps decreases in D, so checking at u0 suffices.
    "2b/a=(2C/3)/(1-2eps) <= P1": bool(arb(2 * C) / 3 / (1 - 2 * eps0) <= P1),
}
print("A (slope in u)         =", A.str(6), " (= 15/64; bound ratio -> 64/49 for fixed C, per review A7)")
print("h(u0) lower bound      =", h0.str(6), " at u0 = log(1e102) =", u0.str(6))
print("monotone (A > M1/Lam)  =", bool(deriv_ok))
for k, v in hyp.items(): print(f"hypothesis {k:22} {v}")
print("ASYMPTOTIC CLOSURE CERTIFIED:", bool(h0 > 0) and bool(deriv_ok) and all(hyp.values()))
