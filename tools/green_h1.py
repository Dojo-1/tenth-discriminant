"""[SUPERSEDED by cover.py for certificates; kept for history. Review F2/F4 guards added.]
Explicit Green-type determinant bound specialised to class number one.

Track: GREEN-H1 (status: DERIVED, unreviewed; numerics in Arb ball arithmetic).

Hypothesis to refute: D > 163 prime, D = 3 mod 8, h(-D) = 1.
Character chi(p) = (-D | p). Inert odd primes = odd primes p != D that do not split.

Ingredients (each must become a ledger node):
 [G1] Green, Lemma 3.1 + Schwarz-Zippel: rows v_{r,s} (0<=r<R, 0<=s<S) of derivatives
      d^j/dz^j (z^r z'^s), 0<=j<J, at points P=(x+y*sqrt(-D), x-y*sqrt(-D)), 0<=x,y<N,
      are independent if J >= N and N^2 > 2RS/J + R + S.  => det G >= 1 (G Gram matrix).
 [G2] Hadamard: log det G <= sum_rows log ||v||^2, ||v||^2 <= 2 N^2 J max|entry|^2,
      |z|,|z'| <= B := (N-1) sqrt(1+D),  |d^j z^r z'^s| <= r^j B^(r+s-j).
 [G3] Green Lemma 5.1: for odd inert p, v_p(det G) >= 2 F(p),
      F(p) = sum_{r<R} g(floor(r/p)),  g(k) = sum_{t<S} min(k,t).
 [H1] h=1 => every split prime p equals x^2+xy+((D+1)/4)y^2, y != 0, giving 4 representations;
      lattice count => #split primes <= t is <= (2t + sqrt t)/sqrt D, and every split p >= (D+1)/4.
 [P1] theta(x) > x(1 - 1/(2 log x)) for x >= 563   (Rosser-Schoenfeld 1962, Thm 4)  [CITED-pending]
 Contradiction if  2 * (inert prime mass weighted by F) * log  >  Hadamard upper bound.
"""
import sys, math
import numpy as np
from flint import arb

def primes_upto(n):
    s = np.ones(n + 1, bool); s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]: s[i*i::i] = False
    return np.nonzero(s)[0]

def G_sum(a, S):
    """sum_{k=0}^{a} g(k) exactly (integers)."""
    if a < 0: return 0
    b = min(a, S - 1)
    tot = S * b * (b + 1) // 2 - b * (b + 1) * (b + 2) // 6
    if a > S - 1: tot += (a - (S - 1)) * (S * (S - 1) // 2)
    return tot

def g(k, S):
    return k * S - k * (k + 1) // 2 if k <= S - 1 else S * (S - 1) // 2

def F_exact(p, R, S):
    K, m = divmod(R, p)        # r = 0..R-1 ; blocks k=0..K-1 full (size p), block K has m elements
    return p * G_sum(K - 1, S) + m * g(K, S)

def upper(R, S, J, N, D):
    B = arb(N - 1) * arb(1 + D).sqrt()
    U = arb(R * S) * (arb(2 * N * N * J)).log()
    U += 2 * B.log() * arb(S * R * (R - 1) // 2 + R * S * (S - 1) // 2)
    if R > B:   # sum_{r<R} max(0, log(r/B)) <= int_B^R log(t/B) dt + log(R/B)
        L = (arb(R) / B).log()
        U += 2 * S * (J - 1) * (arb(R) * L - R + B + L)
    return U

def lower(R, S, D, P0, primes):
    # exact part: odd primes p <= min(P0, R)
    tot = arb(0)
    for p in primes:
        p = int(p)
        if p == 2: continue
        if p > R: break
        tot += arb(p).log() * F_exact(p, R, S)
    # tail (P0, T]: F(p) >= Gl(p) = a/p - b/p^2 - c  valid for p >= R/S (all k <= S-1)
    a = arb(S) * R * (R - 1) / 2 - arb(R) ** 2 / 4
    b = arb(R) ** 3 / 6
    c = arb(S) * R
    P0a = arb(P0)
    T = None
    if R > P0 and P0 >= R / S and P0 >= 563:
        # largest T with Gl(T) >= 0: c T^2 - a T + b <= 0
        disc = a * a - 4 * b * c
        if not disc > 0: return 2 * tot, None   # Review F4: domain guard (no nan)
        Tr = (a + disc.sqrt()) / (2 * c)
        T = min(float(Tr.lower()), R)
        if T > P0:
            Ta = arb(T)
            theta_P0 = sum(math.log(int(p)) for p in primes if p <= P0)   # float; replaced below
            thP0 = arb(0)
            for p in primes:
                if p > P0: break
                thP0 += arb(int(p)).log()
            Gl = lambda t: a / t - b / (t * t) - c
            thlow = lambda t: t * (1 - 1 / (2 * t.log()))
            tail = Gl(Ta) * thlow(Ta) - Gl(P0a) * thP0
            tail += a * (Ta.log() - P0a.log()) - a / 2 * (Ta.log().log() - P0a.log().log()) \
                    - 2 * b * (1 / P0a - 1 / Ta)
            tot += tail
    # subtract the ramified prime D and all split primes (upper bounds)
    if D <= R: tot -= arb(D).log() * F_exact(D, R, S)
    t = arb(D + 1) / 4
    sd = arb(D).sqrt()
    split = arb(0)
    while t < R:   # dyadic blocks [t,2t): count <= A(2t), log p / p <= log t / t, F(p) <= S R^2/(2p)
        A2 = (4 * t + (2 * t).sqrt()) / sd
        split += A2 * t.log() / t * arb(S) * R * R / 2
        t = 2 * t
    tot -= split
    return 2 * tot, T

def check(D, R, S, J, N, P0, primes):
    assert J >= N and N * N * J > 2 * R * S + J * (R + S), "independence condition fails"
    U = upper(R, S, J, N, D)
    L, T = lower(R, S, D, P0, primes)
    return L, U, T

if __name__ == "__main__":
    D = int(float(sys.argv[1])); R = int(float(sys.argv[2])); S = int(float(sys.argv[3]))
    J = int(float(sys.argv[4])); P0 = int(float(sys.argv[5]))
    N = int(math.isqrt(2 * R * S // J + R + S)) + 1
    J = max(J, N)
    pr = primes_upto(P0)
    L, U, T = check(D, R, S, J, N, P0, pr)
    print(f"D={D:.3e} R={R:.3e} S={S} J={J} N={N} T={T}")
    print("lower", L.mid().str(5), " upper", U.mid().str(5), " L>U certified:", bool(L > U), " ratio", (L / U).mid().str(5))
