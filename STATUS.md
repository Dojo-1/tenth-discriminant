# Status — 2026-10-23

For a concise mathematical overview of the checked result and the open
bridge, read [one determinant, two kinds of information](lean/MATHEMATICAL_SPINE.md).
For a comparison with Tao's challenge and a separate accounting of useful
side results, see [the current objective ledger](TAO_OBJECTIVES_CURRENT.md).

## 2026-10-23: local–global determinant bridge (bounded pilot)

For `D>0`, Lean identifies the integer-pair coordinates with the selected
quadratic order `ℤ[√(-D)]`; this does not identify the full ring of integers
for every D.
It also computes the derivative trace-Gram matrix independently in residue
coordinates. For any modulus `m>0`, the local determinant equals the reduction
of the existing integer determinant, and vanishes exactly when `m` divides
that determinant. Samples remain indexed by the original integer-point set:
colliding residues retain their multiplicities. Registered controls check both
this collision issue and the asymmetric `D=3` determinant `12` modulo `3` and
`5`. Separately, a checked fixed-grid theorem proves `9 | det G` for the
canonical `D=19`, `R=4`, `S=2` integer Gram for every finite sample set and
derivative cutoff. For `ellipsePairs 19 5`, `J=2`, its determinant is also
strictly positive. A `D=2`, `p=3` control refutes dropping inertness. This
one-prime toy theorem does not imply Ender's uniform prime-adic lower bound.
The proof and limitations are reported in the
[guide](lean/HUMAN_GUIDE.md#11-local-and-global-arithmetic-views-of-one-gram-matrix)
and [protocol](research/local_global_gram/PROTOCOL.md); the general valuation
bridge and class-number classification remain open.

## 2026-10-23: integer-coordinate trace-Gram bridge

For any finite set of distinct integer pairs and positive D, Lean now proves
that the integer-pair derivative trace-Gram matrix, cast entrywise to Real, is
the existing complex `traceGramMatrix` on the image points. Its row-major
rectangular specialization and determinant cast equality follow. On the
integer-radius ellipse this identifies the same determinant whose positivity
the interpolation theorem controls. The proof preserves conjugate W,
ordinary Z-derivatives, zero high-order columns and factor two.

This is **matrix identification**, not inert-prime divisibility. It does not
equate the integer-radius `ellipsePairs` generator with the verifier's
half-integer-radius historical generator, or turn AI review/CI into a full
classification proof. [Proof guide](lean/HUMAN_GUIDE.md#10-the-same-gram-matrix-in-integer-and-complex-coordinates) ·
[protocol](research/integer_gram_bridge/PROTOCOL.md).

## 2026-10-23: geometric count for Ender's chosen radius

The registered [radius proof](research/ender_radius_bridge/PROOF.md) uses
unit-by-√D lattice cells to establish the inherited lower count for every
integer D≥1 and radius rho≥0. For the exact radius chosen by Ender it yields
`card(ellipsePairs D rho) > 3R+S`; at finite intervals the count transfers
from D2 to every D≤D2 by exact set inclusion. Lean now checks that inclusion,
the cardinality transfer and the existing Gram application, plus a D=19,
rho=5 exact control with 21 points. **The cell-area estimate itself remains
unformalized.** Neither this count nor a green build establishes the integer
matrix's inert-prime divisibility, the analytic contradiction, or class-number
classification. The earlier numerical records are unchanged.

## 2026-10-23: bounded formal ellipse bridge

The registered attempt in `research/lattice_bridge_r1/PROTOCOL.md` adds
`LatticeEllipse.lean`. For positive natural D and integer radius rho, Lean
proves that its bounded finite construction is the full set of integer pairs
with x²+D y²≤rho², that distinct pairs give distinct complex points, and
that the image has the same cardinality. The original rectangular trace-Gram
determinant is positive and satisfies Hadamard **conditional on** the explicit
count `2*(R-1)+(S-1) < card(ellipsePairs D rho)`, R,S≥1 and J≥S. A D=rho=1
control checks all five boundary/axis points. This earlier result was a proof
bridge, not a point-count estimate. The chosen-radius count and integer-matrix
identification were advanced later, as described above; valuation and
classification remain open.

Verification of this exact revision is reported in the associated PR; no
earlier green CI run is evidence for it. The 22 October numerical claims below
are unchanged.

## 2026-10-23: Tao-objective audit and bounded radial replay

`TAO_OBJECTIVE_AUDIT.md` now compares the project's twelve-item status table
with Tao's 20 October challenge and the frozen repository evidence. The main
correction is operational: PR #15 and PR #16 are no longer drafts; they landed
on current `main` at `47ec647` and `4c034f9`. Their checked interpolation
theorem and apparatus audit do not close the arithmetic-to-classification
bridge.

The fixed radial-control suite from `flow/PREREG_RADIAL.txt` was rerun with
Python 3.13.16, python-flint 0.9.0, and SymPy 1.14.0: 9 tests passed in
1.525 seconds. This is a bounded reproducibility check, not a rerun of the
18-case campaign or new numerical evidence. Its registered $O(1/R)$ ceiling
still rules out a cutoff-improvement claim from this bound alone.

The audit labels the Ender route and its $7\times10^{11}$ cutoff as a
**candidate** rather than an achieved classification, keeps the $h\le2$ track
unreviewed, and records that no repository-supported evidence of a Tao-comment
submission was found. See `TAO_OBJECTIVE_AUDIT.md` for the full table and
precise evidence boundaries.

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
