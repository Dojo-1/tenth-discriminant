# Lean components - checked matrix bounds, global theorem open

**This is a partial formalization, not a Lean proof of the class-number-one classification.**

The project uses **Lean 4.19.0** and **Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b`**. No toolchain upgrade or newest-version claim is involved. The matrix follow-up starts from merged PR #5 (`c1dbf68`).

## The new matrix boundary

`GramMatrix.lean` assembles the existing `traceGramEntry` into a full finite real matrix. Its rows are actual complex derivative rows, not an assumed positive matrix. For every finite complex point set, natural derivative cutoff, and finite row-label family, it proves:

```text
G = 2 (A A^T + B B^T), with A and B the real and imaginary row coordinates;
x^T G x = 2 sum_c ((sum_i A_ic x_i)^2 + (sum_i B_ic x_i)^2);
G is positive semidefinite;
0 <= det G <= product_i G_ii.
```

The upper bound is also stated using the exact diagonal-moment formula from `TraceGram.lean`. `GramHadamard.lean` derives the real PSD diagonal-product bound using Mathlib's volume-form inequality and PSD factorization. The origin, repeated labels, zero derivative range and empty dimensions are not excluded by the universal statements.

**Positive semidefinite does not mean nonsingular.** Duplicate actual derivative rows have determinant zero. No theorem here claims strict positivity without independence. The geometric nonvanishing proof, integer implementation correspondence, integrality, inert-prime valuation and aggregate `upper_B` estimate remain separate obligations.

## Verification record

Read the CI result for the exact source commit. The matrix snapshot is `c64a8655bed0aa0a9c12def30a47d89aaf12e827`; its run is [39774302749](https://github.com/Dojo-1/tenth-discriminant/actions/runs/39774302749). **All four gates completed successfully on that snapshot.** Later commits require their own CI check or an explicit code-identity comparison.

The successful gates were `verify_sources.py`, `lake build`, `audit.py`, and `negative_controls.py`. The audit examined 105 compiled theorem entries, including generated auxiliaries; this is not 105 independent mathematical results. The source check still matches all 250 saved interval endpoint pairs; it does not certify the numerical inequalities inside those intervals. The compiled axiom audit permits only `propext`, `Classical.choice`, and `Quot.sound`, including transitive dependencies and generated/private theorem entries.

The negative-control suite retains the three earlier mathematical pairs and four axiom-audit probes, and adds three actual Gram good/bad pairs: duplicate-row positivity, a dropped unmatched derivative column, and the trace factor of two. Setup/type errors are not accepted as mathematical counterstatement rejection. `exact_gram_controls.py`, also run by that suite, exercises six known-answer and 64 fixed-seed Gaussian-integer cases with exact rational elimination. It checks point/row reordering and extra zero derivative columns. These are finite same-author controls, not universal proofs or independent semantic review.

For historical comparison, [run 39758347058](https://github.com/Dojo-1/tenth-discriminant/actions/runs/39758347058) checked the earlier `2048b9a` component snapshot. Its 47 explicit declarations / 86 compiled entries belong to that snapshot, not to a completion percentage or the current inventory.

## Component map

| Module | Exact scope |
|---|---|
| `Arithmetic`, `FloorSum` | Principal-form integer bounds, strict cutoffs, valuation-weight endpoint controls, sum-of-minima identity and quotient/remainder floor sum. |
| `Radial`, `MomentMatrix` | Weighted-moment correlation and two-by-two determinant bound, moment-class sharpness/hypothesis controls and normalized pair-gain ceiling. |
| `TraceGram` | Complex derivative rows, exact diagonal and radial cross moments, lattice norm embedding, origin and unmatched-column controls. |
| `GramHadamard`, `GramMatrix` | Full real trace matrix, exact real/imaginary factorization and quadratic identity, PSD, determinant nonnegativity, Hadamard bound and exact moment-diagonal upper bound. |
| `Coverage`, `RecordedCoverage` | Exact interval stitching and kernel-reduced verification of the saved endpoint chain. |
| `Envelope`, `EnvelopeDecay` | The `15/64` coefficient, actual `C=80` error decay and propagation conditional on endpoint positivity. |

See [FORMALIZATION.md](FORMALIZATION.md) for the claim-to-declaration map. The field/class-group links, small-prime inertness, interpolation and determinant divisibility, complete factorial/Legendre estimates, numerical certificates, CRT/reduced-form closure and full Fischer block product remain open. No surrogate predicate or assumed structure field supplies `h(-D)=1 -> D<=163`.

## Reproduce from the repository root

```sh
cd lean
lake update
lake exe cache get
python3 verify_sources.py
lake build
python3 audit.py
python3 negative_controls.py
```

Deliberately invalid probes are temporary files generated by the test script, never imports in the proof library. Earlier failed builds remain in history. The matrix follow-up required explicit finite-subtype/range sum transport and function extensionality; theorem statements were not weakened to repair those failures. One inherited tactic-style warning in `TraceGram.lean` is nonfatal.

Lean is a separately implemented proof checker, not an independent judge of whether every intended theorem was encoded. Proof selection, tests and interpretation share authorship. The next mathematical target is the actual independence/nonvanishing bridge; no global cutoff is improved by this component change.
