"""Endgame sieve for class number one (status: HYPOTHESIS-grade tool, not certified).
Fact used (elementary, to be written up + Lean'd): if h(-D)=1, D>8 a fundamental
discriminant, then D=p prime, p≡3 (mod 8) for p>7, and (-p/l) = -1 for every prime l < (p+1)/4.
We keep only n in [lo,hi), n≡3 mod 8, such that -n is a non-residue mod each of the first k odd primes.
Survivors are then checked by PARI qfbclassno (independent route)."""
import sys, numpy as np
from sympy import primerange
def sieve(lo, hi, k=40):
    n = np.arange(lo - (lo % 8) + 3, hi, 8, dtype=np.int64)
    n = n[n >= lo]
    for l in list(primerange(3, 10**4))[:k]:
        nonres = np.ones(l, bool)
        nonres[(np.arange(l, dtype=np.int64)**2) % l] = False   # residues (incl. 0)
        keep = nonres[(-n) % l]
        keep |= (n < 4*l)            # constraint only binds when l < (n+1)/4
        n = n[keep]
    return n
if __name__ == "__main__":
    lo, hi = int(float(sys.argv[1])), int(float(sys.argv[2]))
    step = 8 * 10**7; out = []
    for a in range(lo, hi, step):
        out += sieve(a, min(a + step, hi)).tolist()
    print(" ".join(map(str, out)))
