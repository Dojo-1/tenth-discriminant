# Control 1: the calculator must NOT certify a contradiction for true h=1 discriminants.
import sys, math
sys.path.insert(0, 'tools')
from green_h1 import check, primes_upto
pr = primes_upto(10**6)
for D in [19, 43, 67, 163]:
    hits = 0; best = 0
    for e in range(0, 30):
        for C in [3,5,10,20,40,80,160,320,1000]:
            R = int(D * 10**e); S = max(1, R // C); J = S
            N = math.isqrt(2*R*S//J + R + S) + 1
            if J < N: continue
            L, U, T = check(D, R, S, J, N, 10**6, pr)
            best = max(best, float((L/U).mid()))
            hits += bool(L > U)
    print(f"D={D}: certified contradictions={hits} (must be 0), best ratio={best:.4f}")
