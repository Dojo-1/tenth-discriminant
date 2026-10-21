# Status — 2026-10-21

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
