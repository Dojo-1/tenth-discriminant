# Pre-registration — elementary exclusion for class number <= 2   (written BEFORE computing; 21 Oct 2026 22:05)

## Claim (C2)
There is an explicit X such that every imaginary quadratic field with D = |disc| >= X has h > 2, proved by the
O_K-ellipse Green determinant + split count over all reduced forms + Dusart 2010, with NO L-functions, Siegel zeros,
GRH/QRH, Heegner/Baker/Stark, or class-number tables. Below X: direct class-number computation (PARI qfbclassno),
which must return exactly the 9 h=1 and 18 h=2 fields (largest: 163 and 427).

## Procedure (fixed now)
1. Interval certificates with cover_h.certify_h(D1, D2, H=2, ...) from X upward, contiguous, to 1e102.
2. Asymptotic closure for D >= 1e102: asymptotic.py adapted by (i) split term x H, (ii) ramified term for
   omega <= 1 + log2 H odd primes, (iii) O_K point count (area 2 pi rho^2/sqrt D) — each change listed in the diff.
3. Finite range D < X by PARI, independent of the analytic code.
4. Exact brute-force controls rerun (verify_exact_ok.py, verify_split_h.py).

## Success
X <= 10^6 (finite range trivial), all certificates pass, finite range returns exactly the known 27 fields.

## Kill / failure conditions (any one stops the claim)
K1  any certificate covering a D with h(-D) <= 2 (FATAL; checked against PARI for D < 2e6).
K2  X > 10^9 (report as negative result; do not tune toward success after seeing outcomes).
K3  asymptotic closure fails with the pre-stated parameters (K=1e17, C=80) — report, then may re-register new ones.
K4  any brute-force control failure.

## Not claimed
- Novelty beyond "not found in the thread snapshot of 21 Oct ~21:00"; independent review pending; no Lean.
- Parameters may be optimized for X only within the families listed in cover_h (e in 6..22, C in {40,80,160}).
