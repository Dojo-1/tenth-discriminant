# Orbifold test (21 Oct 2026, exploratory; small exact cases D = 7, 19, 43; R=12, S=3)
Evaluation geometry: ellipse points P with P = -P, P = conj(P); G = <z->-z, z->conj z> acts; space C/G is an orbifold.
Facts (exact, all 3 cases):
- Gram matrix is block diagonal in the parity of r+s (even/odd sectors): off-sector entries are exactly 0; det G = det_even * det_odd.
- Frobenius respects the orbifold: the p-adic replacement shifts (r,s) -> (r-p i, s+i), changing r+s by -i(p-1), even for odd p,
  so Green's divisibility lemma holds inside each sector separately (DERIVED; one line).
- Inert-prime share of log det: even 0.111 / 0.051 / 0.112 vs full 0.108 / 0.048 / 0.108 vs odd 0.105 / 0.045 / 0.104.
  The even sector (functions on C/{±1}) is consistently ~3% more efficient than the full matrix in these cases.
Assessment: structural (exact factorization, sector-compatible Frobenius) — P/DERIVED; efficiency gain — M (small, 3 cases), not
yet visible in the analytic bound, which treats rows uniformly. Lever for later: a sector-aware Hadamard/row bound.
