# Lean components — checked foundations, global theorem open

**This is a partial formalization, not a Lean proof of the class-number-one classification.**

At base commit `6ac874f` this repository had no Lean files or Lake project. The new layer is pinned to **Lean 4.19.0** and **Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b`**. No claim to the newest toolchain is made.

## Verified snapshot

At source commit [`2048b9a`](https://github.com/Dojo-1/tenth-discriminant/tree/2048b9a5f14229d118cae7e70050db54cd006281/lean), [workflow run 39758347058](https://github.com/Dojo-1/tenth-discriminant/actions/runs/39758347058) completed successfully:

| Check | Recorded result | What it does not establish |
|---|---|---|
| `lake build` | All project modules compiled. One nonfatal tactic-style linter warning in `TraceGram.lean`. | That every claim in the mathematical argument has been encoded. |
| `verify_sources.py` | Source digest and all **250 interval endpoint pairs** match the exact Lean recurrence. | Correctness of the Arb margin values or of the inequalities they summarize. |
| `audit.py` | **86 compiled theorem entries, including generated auxiliaries**, depend only on `propext`, `Classical.choice`, and `Quot.sound`. | 86 distinct mathematical contributions, or independent assurance of specification fidelity. |
| `negative_controls.py` | Three valid mathematical controls accepted and three false strengthenings rejected; a valid private proof accepted and hidden `sorry`, custom-axiom and native-evaluation dependencies rejected. | Exhaustive mutation coverage or general security against malicious Lean extensions. |

The 86 entries include 47 explicit theorem declarations and compiler-generated equation/auxiliary proofs. Counts are inventory, **not a completion percentage**. Subsequent CI runs must be read against their exact commit; this recorded run is not a blanket approval of later edits.

## What is proved here

| Module | Exact scope |
|---|---|
| `Arithmetic`, `FloorSum` | Principal-form integer norm bound, strict integer cutoffs, valuation-weight endpoint regressions, the finite sum-of-minima identity, and the universal quotient/remainder formula for the floor sum. |
| `Radial`, `MomentMatrix` | Weighted-moment correlation and the `9/25` bound for an actual two-by-two moment matrix, a sharpness example in that moment class, a dropped-hypothesis counterexample, derivative-parameter inequality, and normalized pair-gain ceiling. |
| `TraceGram` | Actual complex derivative rows; exact diagonal and radial cross-entry moment identities without angular symmetry; the lattice norm-squared embedding; origin and unmatched-derivative-column controls. |
| `Coverage`, `RecordedCoverage` | Sound exact interval stitching and kernel-reduced verification of the recorded 250-pair chain. |
| `Envelope`, `EnvelopeDecay` | The `15/64` coefficient, decay of the actual `C=80` error function, and positivity propagation **conditional on endpoint positivity**. |

Read [FORMALIZATION.md](FORMALIZATION.md) for the claim-to-declaration map and all unresolved links.

## What is not proved here

The connection to actual quadratic fields, fundamental discriminants and class groups; small-prime inertness; the complete integer derivative Gram construction and its integrality, nonvanishing and inert-prime divisibility; ellipse counts and interpolation; the full factorial/Legendre prime-mass inequality; kernel-checkable replacements for the numerical inequalities; the full CRT sieve and reduced-form/class-group correspondence; the determinant-to-envelope inequalities and numerical starting margin; and the full disjoint-block Fischer product remain open in this project.

The derivative-row moment identities are now proved, but their application through bounded multipliers to the weighted-moment determinant inequality still needs a separate bridge. A formula for Gram entries does not prove that the full matrix is nonsingular.

These are documented obligations, **not assumed axioms or disguised theorem parameters**. No declaration here asserts `h(-D)=1` implies `D <= 163`.

## Run from the repository root

```sh
cd lean
lake update
lake exe cache get
python3 verify_sources.py
lake build
python3 audit.py
python3 negative_controls.py
```

The axiom audit enumerates the compiled `TenthDiscriminant` namespace, including private names and generated theorem entries. A source scan supplements that check; it is not the proof checker. Deliberately invalid probes exist only as strings in the negative-control script and are executed in temporary files, never imported into the proof library.

## Review boundary

Build success is necessary, not sufficient: compare each declaration's hypotheses and conclusion with its source ledger. Lean provides a distinct, independently implemented proof-checking mechanism; the specification, source interpretation and test selection were authored in the same development loop. No independent semantic or human mathematical review is claimed.

Two earlier build failures are preserved in Git history: the floor-sum proof needed explicit quotient/remainder generalization, and the audit utility used the reserved identifier `prefix`. Both were repaired without weakening the mathematical statements or bypassing the audit. The proof-stage branch remains separate from `main` until reviewed.
