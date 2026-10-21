"""CRT sieve for class number one (Rabinowitsch): if h(-n)=1 and n > 163 then n = 3 (mod 8) and (-n | q) = -1 for every
odd prime q < (n+1)/4.  Enumerate n in [lo, hi) whose residues mod 8*3*5*...*23 pass, then filter by further primes q
(each constraint applied only when q < (n+1)/4).  Survivors are printed; for a tenth discriminant there must be one."""
import sys, numpy as np
from sympy import primerange

BASE = [3, 5, 7, 11, 13, 17, 19, 23]
MOD = 8 * int(np.prod(BASE))

def nonres(q):
    ok = np.ones(q, bool); ok[(np.arange(q) ** 2) % q] = False
    return ok                                   # ok[a] iff a is a nonzero non-residue mod q

def classes():
    n = np.arange(3, MOD, 8, dtype=np.int64)
    for q in BASE: n = n[nonres(q)[(-n) % q]]
    return n

def sieve(lo, hi, extra=200):
    cls = classes(); filt = [(q, nonres(q)) for q in list(primerange(29, 10**5))[:extra]]
    out = []; start = (lo // MOD) * MOD
    for b in range(start, hi, MOD * 64):
        n = (np.arange(b, min(b + MOD * 64, hi + MOD), MOD, dtype=np.int64)[:, None] + cls[None, :]).ravel()
        n = n[(n >= lo) & (n < hi)]
        for q, ok in filt:
            if n.size == 0: break
            n = n[ok[(-n) % q] | (n < 4 * q)]
        out.extend(n.tolist())
    return out, len(cls)

if __name__ == "__main__":
    lo, hi = int(float(sys.argv[1])), int(float(sys.argv[2]))
    s, nc = sieve(lo, hi)
    print(f"classes per period: {nc} (period {MOD}); survivors in [{lo}, {hi}): {s}")
