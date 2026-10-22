# Status — 2026-10-21

## 2026-10-22: analytic radial correlation follow-up

Derived a moment-only formula and a uniform annulus correlation lemma:
eligible disjoint row pairs contribute a block/diagonal ratio at most
9/25, with sufficient independence checked on the actual point set.
The 18-case campaign certifies 16 cases; 8 have strict savings and 2
fail the sufficient rank guard. The guaranteed normalized saving is
O(1/R), so this bound alone does not improve Ender's leading slope.
No global cutoff or Ender certificate was changed.
Derivation, failures and commands: `ledger/radial_bounds.txt`;
raw output: `ledger/radial_bounds.jsonl`.

## 2026-10-22: determinant structure / prime-power lifts

A separate preregistered finite experiment now varies matrix size,
derivative order and sampling geometry, and measures nested Smith
prime-power layers and disjoint-block Fischer bounds. Of 108 cases,
101 are nonsingular and all 101 improve on ordinary Hadamard.
A genuine h=1 control with strict cutoff and sufficient independence
has v_3(det G)=2F(3), ruling out a uniform extra two units of valuation.
These are finite observations, not an all-dimensional improvement or
a change to Ender's proof. Details, commands and limitations:
`ledger/determinant_lifts.txt`; raw results: `ledger/determinant_lifts.jsonl`.

## Latest: ENDER / FORMIC

Ender's computational campaign is complete: factorials and Legendre's identity replace Dusart, without any prime-distribution estimate.
There are 250 certified intervals on [7e11,1e36], a floor-safe all-D envelope above 1e36 (slope 15/64, initial margin 7.84016),
and a fresh CRT run on [92,7e11) returning only 163. Formic rechecks local arithmetic, geometry, mutations and interval stitching.
Proof, commands and limitations: `ledger/ender.txt`; outputs: `ledger/coverage_ender.txt`, `ledger/asymptotic_ender.txt`,
`ledger/sieve_ender.txt`, `ledger/formic.txt`.
The separate BEAN audit returned GAPS ONLY (`review/BEAN_AUDIT.txt`); the old point-based asymptotic claim is not thereby validated.
Ender's analytic re-audit found no mathematical defect in the new factorial and universal-envelope derivations (`review/ENDER_AUDIT.txt`).
This remains a candidate mathematical argument, not a formalized or human-reviewed theorem. Historical entries below are not the latest status.

## Track GREEN-H1: an L-function-free route to class number one (HYPOTHESIS → under test)

**Idea.** Green's determinant argument (hexagon:2610.00311v2) needs one input: inert primes carry
almost all of the prime mass sum log p / p up to X. Usually that comes from a Siegel zero.
For h(-D)=1 it has an elementary source: every split prime is x^2+xy+((D+1)/4)y^2 with y != 0,
so a lattice-point count bounds split primes up to t by (2t+sqrt t)/sqrt D. No L-functions needed.

**Calculator:** `tools/green_h1.py` (Arb ball arithmetic). Point checks certify a contradiction
(h(-D)=1 impossible) at sample D = 1e6, 1e8, 1e10, 1e14 with R = D*1e14, S = J = R/80.

**Controls passed** (all FAILURES = 0):
- `control_heegner.py`: no contradiction for D = 19, 43, 67, 163 (weak: lower bound is vacuous there).
- `bruteforce_green.py`: exact Gram determinants (PARI) satisfy det>0, det <= Hadamard, v_p(det) >= 2F(p), 21 instances.
- `control_bounds.py`: my aggregated upper bound >= exact log prod G_ii (16 instances); split-count bound and
  min split prime >= (D+1)/4 hold for all genuine h=1 fields up to 1e6 (bound is ~2x loose).
- Tail inequality Gl(p) <= F(p) checked at 7 primes.

**NOT yet established:**
1. Coverage of *every* D >= D0 (only sample points so far) — needs interval version + asymptotic argument.
2. [P1] Rosser–Schoenfeld theta(x) > x(1-1/(2 log x)), x >= 563: quoted from memory, must be checked against the paper.
3. Independent review of each derivation (fresh model / human), then Lean.
4. Below D0: sieve endgame (`tools/sieve_h1.py`, verified to 1e10).
Nothing here may be reported externally until 1–3 close.

## 2026-10-21 (later): ellipse variant GREEN-H1-E (suggested by J. Vilela)
Replace Green's N x N grid by lattice points inside the norm ellipse x^2 + D y^2 <= rho^2 (a disc in C).
Max point size drops by ~D^{1/4}; zero bound via horizontal lines (J >= points/line + #lines).
Point checks (`tools/green_h1_ellipse.py`), certified margins L/U:
square grid: 1.09-1.21 (D=1e6..1e14)  ->  ellipse: 1.26 (1e6), 1.49 (1e8), 1.50 (1e10), 1.47 (1e14), 1.44 (1e20).
Crossover now between D=1e5 (0.91) and 1e6. Same open items 1-4 apply; new ingredients E1-E3 need review + brute-force control.

## 2026-10-21 (evening): self-audit + exact verification
- Rule-0 audit table of the chain recorded in conversation; new ledger nodes needed: genus-theory lemma
  (h=1, |disc|>8 => disc=-D, D prime = 3 mod 4), and the line-slicing zero bound for general point sets.
- `tools/verify_exact.py`: one exact verifier for any point set; checks hypothesis, det>0, Hadamard,
  my aggregated bound, v_p(det)>=2F(p), ellipse point count. 46 cases (ellipse + square, D=7..67): 0 failures.
- `tools/mutation_test.py`: verifier rejects a too-strong valuation claim (M1) and shows det=0 when the
  independence hypothesis is dropped (M3) — the hypothesis is not decorative.
- M2 (Hadamard x1e-6 stronger) NOT caught => Hadamard is loose. Measured slack log(prod G_ii)/log det:
  square ~18-20%, ellipse ~6-10%. The round point set also makes rows closer to orthogonal.
  Open lever: replace Hadamard by a sharper determinant bound.

## Parked
- Track F (function-field calibration over F_q[T]): RH known there (Weil); use to test the method against
  ground truth. Needs Hasse derivatives (char p). Start after integer coverage. MacRae 1971 citation unverified.

## 2026-10-21 18:40: deeper probe
- `tools/verify_exact_large.gp`: exact checks (det>0, Hadamard, v_p >= 2F) on ellipse sets with general rho,
  matrices up to 160 rows, up to 9 inert primes, valuations up to 380: 9 cases, 0 failures (4.5 min).
  Hadamard loss at this scale: log(prod G_ii)/log det = 1.03-1.06.
- Bottleneck at D=1e5 is the split-prime subtraction (7.3 of 24.7 normalized units); N3 bound is ~2x loose
  (2t/sqrt D vs area pi t/(2 sqrt D)). Tightening N3 is the next lever for D0.

## 2026-10-21 22:20 — class number <= 2, elementary route (pre-registered, flow/PREREG_H2.md)
Result (unreviewed): every imaginary quadratic field with |disc| >= 7e4 has h > 2, with no L-functions; below 7e4 PARI
returns exactly the 9 + 18 known fields. Not found in the thread snapshot (higher h there only via QRH or Siegel-zero routes).
Next: independent review of cover_h / asymptotic_h / N3' before any external statement.
