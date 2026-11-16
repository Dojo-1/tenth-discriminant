# Phase333 exact-head failure and correction ledger

## First verification — 16 November 2026

- Source head: `389fc34998b7fd50e8dc9125c29b4b645522348a`.
- Workflow: [run 43945824234](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43945824234).
- Exact Python controls: **PASS**.
- Lean target: **FAIL** in `Phase333ClassicalLocalLattice.lean:104`.
- Failed step: `odd_modulus_dvd_of_dvd_two_mul`, at
  `y=(q/2+1)*(2*y)-q*y := by rw [hodd]; ring`.
- Diagnostic: `rw [hodd]` rewrites an occurrence of `q` under
  `q/2`, leaving a complicated integer-division expression that
  polynomial normalization cannot close. This is a proof-script failure,
  not a discovered odd-modulus counterexample.
- The error temporarily gave the dependent odd-divisibility theorem
  `sorryAx`; therefore the old file is **not** an accepted Lean proof.
- The range/parity, same-source positive trace-pairing, and exact
  original Gram determinant equality declarations printed ordinary
  logical axioms only in this run. They remain subject to full
  exact-head confirmation after the correction.

**Repair target:** derive `2*(q/2+1)-q=1` by integer arithmetic from
`q%2=1`, then multiply by `y`; do not rewrite `q` under integer
division. Keep every theorem statement, source sample, derivative,
Gram matrix, threshold and verifier configuration unchanged.

This record is retained even after a successful retry.
