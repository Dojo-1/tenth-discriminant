# Constant ledger — Track GREEN-H1-E (class number one without L-functions)

Tags: CITED (primary checked) · CITED-2 (secondary source only) · DERIVED (ours, unreviewed) ·
BRUTE (exact computation on small cases) · CERTIFIED (Arb ball arithmetic) · OPEN.

| Node | Statement | Status | Evidence |
|---|---|---|---|
| N1 ✔GPT | h(-D)=1, \|disc\|>8 ⇒ disc=-D, D prime ≡ 3 (mod 8) | DERIVED (genus theory; standard) | needs write-up + Lean |
| N2 ✔GPT | split p ⇒ p = x²+xy+((D+1)/4)y², y≠0, 4 reps; p ≥ (D+1)/4 | DERIVED | BRUTE: all h=1 fields, p<10⁶ |
| N3 ✔GPT | #split p ≤ t is ≤ (2t+√t)/√D (v1, used in asymptotic.py) | DERIVED | BRUTE (bound ~2x loose) |
| N3' | #split p ≤ t is ≤ (π/2)t/√D + √(t/D); split mass by exact partial summation (cover.py v2) | DERIVED | BRUTE: h=1 fields, t ≤ 2·10⁶, 0 failures |
| N4 ✔GPT | rows independent if J ≥ L+M, nJ > 2RS+J(R+S) (Green L3.1 + line slicing) | DERIVED from Green | BRUTE 46 cases; mutation M3 |
| N5 ✔GPT | det G ≤ ∏ G_ii (Hadamard), G_ii ≤ 2nJ·max\|entry\|² | CITED (classical) | BRUTE |
| N6 ✔GPT | aggregated upper bound U(R,S,J,n,B) | DERIVED | BRUTE (D in 46 cases) |
| N7 ✔GPT | v_p(det G) ≥ 2F(p), p odd inert | Green L5.1 | BRUTE; mutation M1 |
| N8 ✔GPT | ellipse count: πρ²/√D − 2ρ/√D − 6ρ ≤ n ≤ πρ²/√D + 2ρ + M | DERIVED | BRUTE (F, aligned ρ only) — general-ρ form OPEN to brute |
| N9 | θ(x) ≥ x(1 − 0.006788/log x), x ≥ 10 544 111 (Dusart 1999) | CITED-2 (arXiv:2002.11068, Table 2) | primary OPEN |
| N10 | tail partial summation, G ≤ F on p ≥ R/S | DERIVED; G≤F proved by reviewer for all params | Review F1/F2 fixed (guarded tail, T=R//3) |

## Coverage
- D ≤ 10¹⁰: sieve (`tools/sieve_h1.py`) finds only 11,19,43,67,163 — matches PARI to 10⁶. (Sieve itself: OPEN to formal check.)
- v3 (post-review fixes): [1.5·10⁴, 10¹⁰²] contiguous, 43/43, `ledger/coverage_v3.txt` (bottom margin 1.040). Below 10⁴ the bound fails.
- v2 (pre-fix, superseded): `ledger/coverage_v2.txt`.
- ✔GPT = independently re-derived by GPT-6.1 Sol (review/PHASE1, PHASE2).
- v1 (superseded, kept): [10⁶, 10¹⁰²], `ledger/coverage_1e6_1e100.txt`.
- D > 10¹⁰²: OPEN — needs an analytic (pen-and-paper) asymptotic argument; margin heuristically → ~4/3.
