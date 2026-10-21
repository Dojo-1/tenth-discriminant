"""Interval certification for GREEN-H1-E: prove h(-D) != 1 for EVERY D in [D1, D2].

Fixed parameters (R, S, J=S, rho) and the point set {x^2 + D y^2 <= rho^2}. Dependence on D:
  - archimedean size B = rho: independent of D            -> upper bound independent of D
    (except the point count n inside a log term: use n_up at D1)
  - point count n decreases in D                           -> hypotheses checked with n_low at D2
  - lines M = 2 floor(rho/sqrt D)+1 decreases in D         -> zero-bound J >= L+M checked at D1
  - split-prime mass decreases in D                        -> subtract the D1 bound
  - ramified term F(D) log D:  F decreasing, log increasing -> subtract F(D1) log D2
  - exact + tail prime mass: independent of D              -> computed once, cached
Point count, general rho (a = rho/sqrt D, Y0 = floor a):
  n >= sum_{|y|<=Y0-1} (2w(y)-1) >= int_{-a}^{a} (2w-1) - 2*1.5*2rho = pi rho^2/sqrt D - 2a - 6 rho   (midpoint rule, concave w)
  n <= pi rho^2/sqrt D + 2 rho + M                                                                 (unimodal sum <= integral + max)
Prime-sum input [P1]: Dusart 1999, theta(x) >= x(1 - 0.006788/log x) for x >= 10 544 111 (CITED, secondary).
"""
import sys, math, functools
sys.path.insert(0, 'tools')
from flint import arb
from green_h1 import primes_upto, F_exact
from green_h1_ellipse import upper_B

P0 = 10**7 + 1                     # exact enumeration up to here; tail uses Dusart (needs P0 >= 10 544 111? see below)
PR = None
M1, X1 = arb("0.006788"), 10544111  # Dusart 1999

def primes():
    global PR
    if PR is None: PR = primes_upto(12 * 10**6)
    return PR

@functools.lru_cache(maxsize=None)
def prime_mass(R, S):
    """2 * [ sum_{odd p<=P} log p F(p) + certified tail lower bound ]  — D-independent part."""
    pr = primes(); P = int(pr[-1]) if R > pr[-1] else R
    P = max(int(p) for p in pr if p <= min(R, 12 * 10**6))
    tot = arb(0); th = arb(0)
    for p in pr:
        p = int(p)
        if p > P: break
        lp = arb(p).log(); th += lp
        if p > 2: tot += lp * F_exact(p, R, S)
    if R > P:
        assert P >= X1 and P >= R / S
        a = arb(S) * R * (R - 1) / 2 - arb(R) ** 2 / 4; b = arb(R) ** 3 / 6; c = arb(S) * R
        G = lambda t: a / t - b / (t * t) - c
        # Review F1/F2 (GPT-6.1, review/PHASE2): T is the exact integer R//3 (no float rounding), and the
        # tail is added ONLY if every partial-summation hypothesis is certified in Arb:
        #   T > P (non-empty range),  G(T) > 0,  P >= 2b/a (so -G' >= 0 on [P,T]).  Otherwise no tail (valid: terms >= 0).
        T = arb(R // 3)
        Pa = arb(P)
        if not (T > Pa and G(T) > 0 and Pa >= 2 * b / a):
            return 2 * tot
        thlow = lambda t: t * (1 - M1 / t.log())
        # sum_{P<p<=T} log p G(p) >= G(T) thlow(T) - G(P) theta(P) + int_P^T thlow(t) (-G'(t)) dt
        # (a/t - 2b/t^2)(1 - M1/log t) >= a/t - a M1/(t log t) - 2b/t^2
        tail = G(T) * thlow(T) - G(Pa) * th + a * (T.log() - Pa.log()) \
               - a * M1 * (T.log().log() - Pa.log().log()) - 2 * b * (1 / Pa - 1 / T)
        tot += tail
    return 2 * tot

def split_mass(R, S, D1):
    """2 * upper bound for sum_{split p <= R} log p * F(p), with F(p) <= c/p, c = S R^2/2.
    [N3'] A(t) := #{split p <= t} <= alpha t + beta sqrt t, alpha = pi/(2 sqrt D), beta = 1/sqrt D
          (reps of y != 0 under x^2+xy+((D+1)/4)y^2 <= t: sum of interval lengths <= ellipse area 2 pi t/sqrt D,
           plus one per line (<= 4 sqrt(t/D) lines), divided by 4 reps per prime).
    Partial summation, w(t) = c log t / t decreasing for t >= e, A = 0 below t0 = (D+1)/4:
      sum <= w(R) A(R) + int_{t0}^{R} A(t) (-w'(t)) dt,  -w'(t) = c (log t - 1)/t^2.
      int alpha t (-w') = alpha c [log^2 t / 2 - log t];   int beta sqrt t (-w') = beta c [-2 (log t + 1)/sqrt t]."""
    c = arb(S) * R * R / 2; sd = arb(D1).sqrt()
    al, be = arb.pi() / (2 * sd), 1 / sd
    t0, Ra = arb(D1 + 1) / 4, arb(R)
    if not Ra > t0: return arb(0)
    lt0, lR = t0.log(), Ra.log()
    I1 = al * c * ((lR * lR - lt0 * lt0) / 2 - (lR - lt0))
    I2 = be * c * (-2 * (lR + 1) / Ra.sqrt() + 2 * (lt0 + 1) / t0.sqrt())
    end = c * lR / Ra * (al * Ra + be * Ra.sqrt())
    return 2 * (end + I1 + I2)

def certify(D1, D2, R, S, rho):
    """True iff h(-D) = 1 is impossible for every prime D in [D1, D2] (given the cited inputs)."""
    J = S; rho = arb(rho)
    s1, s2 = arb(D1).sqrt(), arb(D2).sqrt()
    n_low = arb.pi() * rho * rho / s2 - 2 * rho / s2 - 6 * rho
    if not n_low * J > 2 * R * S + J * (R + S): return False, "n"
    L = 2 * int(rho.upper().floor().unique_fmpz()) + 1
    M = 2 * int((rho / s1).upper().floor().unique_fmpz()) + 1
    if J < L + M: return False, "J"
    n_up = arb.pi() * rho * rho / s1 + 2 * rho + M
    U = upper_B(R, S, J, n_up, rho)
    Lo = prime_mass(R, S) - split_mass(R, S, D1)
    if D1 <= R: Lo -= 2 * arb(D2).log() * F_exact(D1, R, S)
    return bool(Lo > U), float((Lo / U).mid())

def rho_for(D2, R, S, slack=1.0):
    """smallest-ish rho making the point-count hypothesis hold at D2, times slack."""
    need = (2 * R * S + S * (R + S)) / S
    r = math.sqrt(need * math.sqrt(D2) / math.pi) * 1.001 + 10 * math.sqrt(D2)
    return r * slack

if __name__ == "__main__":
    D1 = int(float(sys.argv[1])); Dend = int(float(sys.argv[2])); Q = float(sys.argv[3]) if len(sys.argv) > 3 else 10
    while D1 < Dend:
        D2 = int(D1 * Q); done = False
        for e in range(9, 22):
            for C in [40, 80, 160, 320]:
                R = D1 * 10**e; S = R // C
                ok, info = certify(D1, D2, R, S, rho_for(D2, R, S))
                if ok:
                    print(f"[{D1:.3e}, {D2:.3e}]  CERTIFIED  R=D1*1e{e} C={C}  margin={info:.3f}", flush=True)
                    done = True; break
            if done: break
        if not done:
            print(f"[{D1:.3e}, {D2:.3e}]  FAILED"); break
        D1 = D2
