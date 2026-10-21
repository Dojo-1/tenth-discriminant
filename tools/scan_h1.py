import sys, math
sys.path.insert(0, 'tools')
from green_h1 import check, primes_upto
pr = primes_upto(10**6)
D = int(float(sys.argv[1]))
best = None
for e in [2,3,4,5,6,8,10,12,14]:
    for C in [10,20,40,80,160,320]:
        R = int(D * 10**e); S = R // C; J = S
        N = math.isqrt(2*R*S//J + R + S) + 1
        if J < N: continue
        L, U, T = check(D, R, S, J, N, 10**6, pr)
        r = float((L/U).mid())
        if best is None or r > best[0]: best = (r, e, C, bool(L > U))
print(D, "best ratio %.5f at R=D*1e%d C=%d certified=%s" % best)
