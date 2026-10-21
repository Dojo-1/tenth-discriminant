# Review round 2 — class number <= H, elementary route (for an independent model; rules of REVIEW_BRIEF.md apply)

Phase 1 (BLIND: read only this file, flow/c.md, and Green hexagon:2610.00311v2). Claim: every imaginary quadratic field with
D = |disc| >= 7*10^4 has h > 2, via Green's derivative Gram determinant on the points of O_K in a disc |z| <= rho,
Frobenius divisibility at odd inert primes, and the bound
  #{split p <= t} <= H*pi*t/(2 sqrt D) + H*(3D)^(-1/4)*sqrt(t) + H/4   (all reduced forms; 4 reps per split prime in total),
ramified primes <= 1 + log2 H, Dusart 2010 theta(x) >= x(1-0.2/ln^2 x), x >= 3 594 641.
 B1 Prove/refute the split-count bound (Dirichlet's r(n) = 2 sum_{d|n} chi(d); per-form lattice counts; line counts).
 B2 Prove/refute O_K point count A-2rho-M <= n <= A+2rho+M with A = 2 pi rho^2/sqrt D, M = 2 floor(2 rho/sqrt D)+1.
 B3 Do Green's independence and p-adic lemmas hold on O_K = Z[(1+sqrt -D)/2] and Z[sqrt -m] (even discriminants)?
 B4 Is "omega(D) <= 1 + log2 h" (genus theory) correctly applied? Is p = 2 correctly excluded everywhere?
Phase 2 (AUDIT): tools/cover.py split_mass (partial summation, N3'), tools/cover_h.py, tools/asymptotic_h.py,
ledger/coverage_h2.txt, ledger/finite_h2.txt, flow/PREREG_H2.md. Check every endpoint/monotonicity claim, the gamma=H/4 term,
the treatment of floors, and rerun verify_exact_ok.py, verify_split_h.py, asymptotic_h.py 2, cover_h.py 2 7e4 1e6 1.3.
Final line: VERDICT: FATAL FOUND | GAPS ONLY | NO ISSUES FOUND. Write only under review/.
