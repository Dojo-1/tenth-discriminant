"""Control 3: my aggregated upper bound >= log prod G_ii (exact), and split-prime count bound [H1]."""
import sys, math
sys.path.insert(0, 'tools')
from bruteforce_green import rows, gram
from green_h1 import upper
from sympy import primerange, legendre_symbol
bad = 0
for D in [7, 19, 43, 163]:
    for (R, S, J, N) in [(5,2,4,4), (8,2,6,4), (12,3,6,6), (20,4,8,8)]:
        G = gram(rows(R, S, J, N, D), D)
        lhs = sum(math.log(G[i][i]) for i in range(len(G)))
        U = float(upper(R, S, J, N, D).lower())
        bad += lhs > U
        print(f"D={D} R={R} S={S} J={J} N={N}: log prod G_ii={lhs:.2f} <= U={U:.2f} {lhs <= U}")
# H1: for genuine h=1 fields, #split primes <= t  vs (2t+sqrt t)/sqrt D, and min split prime >= (D+1)/4
for D in [11, 19, 43, 67, 163]:
    sp = [p for p in primerange(3, 10**6) if p != D and legendre_symbol((-D) % p, p) == 1]
    worst = max(sum(1 for p in sp if p <= t) / ((2*t + t**0.5) / D**0.5) for t in [10**k for k in range(2, 7)])
    print(f"D={D}: min split prime {sp[0]} >= (D+1)/4={(D+1)/4} {sp[0] >= (D+1)/4};  max count/bound = {worst:.3f} (<=1 required)")
    bad += sp[0] < (D+1)/4 or worst > 1
print("FAILURES:", bad)
