# Independent adversarial review — instructions for the reviewing model

You are reviewing a claimed proof. Your job is to **break it**, not to confirm it. A review that finds
nothing must say exactly which steps were re-derived independently and which were only read.

## Phase 1 — BLIND (do this before opening STATUS.md, LEDGER.md, tools/ or any docstring)

Read only: this file, `lit/fetch.sh` (to obtain sources), Green's note `hexagon:2610.00311v2` (5 pages).

**Claim.** Let D > 163 be a prime, D ≡ 3 (mod 8), and suppose h(−D) = 1. Then a contradiction follows from:
1. Green's Gram-determinant construction, but evaluated on the lattice points
   {x + y√−D : x, y ∈ ℤ, x² + Dy² ≤ ρ²} instead of Green's N×N grid;
2. Green's p-adic lemma (v_p(det G) ≥ 2 Σ_{r,s} min(⌊r/p⌋, S−1−s)) for odd inert p;
3. the fact that, when h = 1, every split prime equals x² + xy + ((D+1)/4)y² with y ≠ 0
   (so split primes up to t number at most about 2t/√D) — **no L-functions, no Siegel zero**;
4. Hadamard's inequality and Dusart's bound θ(x) ≥ x(1 − 0.006788/log x) for x ≥ 10 544 111.
The claim is that this yields h(−D) ≠ 1 for all D ≥ 2·10⁵, and a sieve handles smaller D.

**Tasks (record your own derivation for each):**
- B1. Is item 3 correct? (Genus theory: does h = 1 with |disc| > 8 force disc = −D, D prime ≡ 3 mod 4?
  Do split primes really have exactly 4 representations, all with y ≠ 0? Is p ≥ (D+1)/4?)
- B2. Green's Lemma 3.1 uses Schwarz–Zippel on a grid. For the ellipse set, the claimed substitute is:
  the points lie on M horizontal lines with ≤ L points each, so a nonzero F of total degree k vanishes on
  ≤ k(L+M) of them; hence J ≥ L+M suffices. Is this valid? Does anything else in Lemma 3.1 depend on the grid?
- B3. Green's p-adic lemma: does it need the grid, x, y ≥ 0, or anything the ellipse set breaks (negative x, y)?
- B4. Without looking at our numbers: derive, in your own notation, the inequality that must hold for a
  contradiction, and estimate the threshold D₀. Compare later with ours (~2·10⁵).
- B5. Is anything circular — does any step secretly use the classification of class-number-one fields,
  Heegner/Baker/Stark, GRH, or an ineffective constant?
- B6. Is this already known? Search the literature (and the comments on Tao's posts of 19–20 Oct 2026).

Write Phase 1 findings to `review/PHASE1_<model>.md` **before** Phase 2.

## Phase 2 — AUDIT

Now read `LEDGER.md`, `STATUS.md`, and `tools/`. For each ledger node N1–N10:
- re-derive or refute; mark AGREE / DISAGREE / CANNOT-VERIFY with reasons;
- check every inequality's direction, validity range, and monotonicity claim in `tools/cover.py` and
  `tools/asymptotic.py` (in particular: is each "decreasing in D / u" claim actually true? are floor
  effects S = ⌊R/C⌋ handled? does the interval argument in cover.py correctly take worst cases at D1/D2?);
- run `tools/verify_exact.py`, `tools/mutation_test.py`, `tools/asymptotic.py` and try to make them fail with
  new cases (other D, other shapes, larger R, S).
- Check Dusart (1999) against the primary source if you can access it.

Write to `review/PHASE2_<model>.md`. Severity scale: FATAL (claim false) / GAP (unproved step) /
SLOPPY (true but argued wrongly) / NIT.

## Rules
- Do not edit existing files; only add files under `review/`.
- Disclose your model name/version and any tools used.
- Fluency is not evidence. If you agree with a step, show the derivation, not the sentence "this is standard".
