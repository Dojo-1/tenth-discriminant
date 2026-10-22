# Lean components - checked matrix, jet and local multiplicity layers

**This is a partial formalization, not a Lean proof of the class-number-one classification.**

The project uses **Lean 4.19.0** and **Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b`**. No toolchain upgrade or newest-version claim is involved.

## Current verified boundary

The code/test snapshot `9c41b2482fc69d8e53f906c2d0dd4357dc4909ef` passed [run 39789129577](https://github.com/Dojo-1/tenth-discriminant/actions/runs/39789129577), job `119860130933`: source linkage, build, compiled axiom audit and the expanded controls. Its PR synthetic merge `b83a39e17fe29cd826959e83bf385c5559631e09` has the same source tree. A later green summary must still be tied to its exact revision.

The newest theorem proves that an m-fold root of a nonzero specialization F(Z,w) forces `(W-w)^(m-1)` to divide the **original fixed-size Sylvester determinant of F and F_Z**, even if the leading degree drops at w. An explicit determinant-one Taylor coordinate change makes the required rows vanish. See [SYLVESTER_MULTIPLICITY.md](SYLVESTER_MULTIPLICITY.md) for the theorem, proof map, controls and unresolved links.

This local divisibility theorem does **not** show that the determinant polynomial is nonzero. That distinction is essential before using its degree to bound the number of contacts. The full jet-uniqueness criterion in [JET_NONVANISHING.md](JET_NONVANISHING.md) remains a conventional derivation, not a Lean theorem.

## Actual matrix and jet boundary

`GramMatrix.lean` assembles the existing `traceGramEntry` into the full finite real matrix. Its rows are actual complex derivative rows, not an assumed positive matrix. For every finite complex point set, natural derivative cutoff, and finite row-label family, it proves:

```text
G = 2 (A A^T + B B^T), with A and B the real and imaginary row coordinates;
x^T G x = 2 sum_c ((sum_i A_ic x_i)^2 + (sum_i B_ic x_i)^2);
G is positive semidefinite;
0 <= det G <= product_i G_ii.
```

The upper bound is also stated using the exact diagonal moments. `GramHadamard.lean` derives the real PSD diagonal-product bound using Mathlib's volume-form inequality and PSD factorization. The origin, repeated labels, zero derivative range and empty dimensions are not excluded by the universal statements.

`JetKernel.lean` identifies the actual Gram kernel with invisible **real** coefficient jets and proves the equivalence between positive definiteness and real jet uniqueness. It also identifies those rows with Mathlib's actual iterated polynomial derivative with W held fixed. Complex jet independence is sufficient, not necessary: a checked control has complex rank one and real trace-Gram determinant four.

**Positive semidefinite does not mean nonsingular.** No geometric uniqueness premise is discharged merely by expressing it as a conditional determinant theorem.

## Component map

| Module | Exact scope |
|---|---|
| `Arithmetic`, `FloorSum` | Principal-form integer bounds, strict cutoffs, valuation-weight endpoint controls, sum-of-minima and quotient/remainder floor sum. |
| `Radial`, `MomentMatrix` | Weighted-moment correlation and two-by-two determinant bound, moment-class sharpness/hypothesis controls and normalized pair-gain ceiling. |
| `TraceGram` | Complex derivative rows, exact diagonal and radial cross moments, lattice norm embedding, origin and unmatched-column controls. |
| `GramHadamard`, `GramMatrix` | Full real trace matrix, exact factorization and quadratic identity, PSD, nonnegative determinant, Hadamard and exact moment-diagonal upper bound. |
| `JetKernel` | Actual real jet/energy/kernel equivalences, polynomial derivative correspondence, observation monotonicity and circle/real-complex controls. |
| `DeterminantMultiplicity`, `SylvesterLocal` | Explicit Taylor coordinate matrix, row-factor extraction, fixed-size Sylvester local multiplicity including degree loss, nonzero-specialization corollary and sharp/repeated-factor examples. |
| `Coverage`, `RecordedCoverage` | Exact interval stitching and kernel-reduced verification of the saved endpoint chain. |
| `Envelope`, `EnvelopeDecay` | The `15/64` coefficient, actual C=80 error decay and propagation conditional on endpoint positivity. |

See [FORMALIZATION.md](FORMALIZATION.md) for the complete claim map. Fields/class groups, small-prime inertness, global jet uniqueness, Gram integrality and determinant divisibility, aggregate `upper_B`, full factorial/Legendre estimates, numerical certificates, CRT/reduced-form closure and the full Fischer product remain open. No surrogate predicate or assumed structure field supplies `h(-D)=1 -> D<=163`.

## Verification, controls and provenance

The successful audit examined **145 compiled theorem entries, including generated auxiliaries**. That is inventory, not 145 independent mathematical results or a completion percentage. Only `propext`, `Classical.choice` and `Quot.sound` are allowed, including transitive dependencies. The source linkage still matches all 250 saved interval endpoint pairs; it does not certify their Arb inequalities.

All **13 matched mathematical positive/negative pairs** and four axiom-audit probes passed. The suite also retains the six exact Gram examples, 64 seeded Gram cases, 96 modular jet cases, four dropped-jet controls and four earlier resultant controls. The new multiplicity campaign has three exact reference formulas and 48 planted-root cases: 24 degree drops, but only 22 cases with a positive required exponent, nine of which also drop degree. Finite counts do not replace the universal proofs.

The new negative probes must fail with an arithmetic contradiction, not a setup/type error. Hidden incomplete proofs, custom axioms and native-evaluation dependencies are rejected by the existing audit controls. Two nonfatal tactic-style warnings remain in `TraceGram.lean` and `SylvesterLocal.lean`.

Historical verified snapshots are preserved: matrix `c64a865` / [39774302749](https://github.com/Dojo-1/tenth-discriminant/actions/runs/39774302749), jets `561b294` / [39781264061](https://github.com/Dojo-1/tenth-discriminant/actions/runs/39781264061), and earlier foundations `2048b9a` / [39758347058](https://github.com/Dojo-1/tenth-discriminant/actions/runs/39758347058). Their theorem inventories belong to those snapshots only. Failed drafts and their repairs remain in Git history; checks were not bypassed.

PR #6 merged into main, but the stacked PR #7 merged into its feature branch after that. The main-targeted PR #8 carries the jet layer and this local multiplicity layer together, preserving both histories. Its existence is not a merge confirmation.

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

The final command invokes the Gram, jet and multiplicity controls. Deliberately invalid probes are generated in temporary files, never imported into the proof library.

Lean is a separately implemented proof checker, not an independent judge of whether every intended theorem was encoded. Proof selection, tests and interpretation share authorship. The next bounded target is nonzero fixed determinant plus its W-degree bound for the intended irreducible factors; the global class-number chain remains open.
