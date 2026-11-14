# Tenth Discriminant — research fabric, Phases269–320

> A determinant is the end of a chain of structures, not a place to add every defect we can name.
>
> Keep the source, the lattice, the pairing, the local Smith filtration and the global ideal class visible all the way through.

This is the reader index for the research-only consolidation. It is deliberately not a competing publication endpoint. The canonical public theorem remains on `main); the research branches preserve finite experiments, formal bridges, negative controls and open hypotheses.

## The lines

### Phase269–270 — finite inert-sieve / CRT bridge

- Bounded finite 321-scale inertness regressions and a Lean bridge.
- C++ and NumPy independent implementations.
- This is a finite certificate, not by itself a theorem for all totally complex quadratic class-number-one fields.

Entry points: `research/phase269/FINITE_INERT_SIEVE_321.md`, `tools/finite321_inert_sieve.cpp`, `tools/finite321_inert_sieve_numpy.py`, and `lean/TenthDiscriminant/Phase269Finite321Certified.lean`.

### Phase277–292 — primitive pairing, Noether and Smith

- Phase277–278: matched primitive p-adic pairing and the safe first-layer bound. Evaluation-index and pairing defects overlap; they cannot simply be added.
- Phase287–290: four-dimensional moving-frame theta models, integral Noether transport, Fischer/Schur comparisons and prime-local wall modules.
- Phase291–292: full D563 700-row primitive gate, D563/D587/D583 matched controls and parity-resolved five-row Schur extension.

Reader guide: `research/phase277-292/README.md`.

### Phase293–303 — Hermite/Frobenius, Picard and maximal-order bridges

- Graded Jordan and source-moment transport.
- W-equivariant jet obstructions and affine-semilinear moving frames.
- Integral Schur projection, composable cokernel remainders and discriminant gluing.
- Joint same-parity saturation and primitive-line Hensel flags.
- Maximal-order source, residue and field-bridge controls.

The key warning from the matched fields: primitive nondegeneracy in one fixed geometry is not a class-number-one detector. D163 and D187 can share a full primitive rank while their class numbers differ.

### Phase306–319 — source transport and wild-ray realization

- Phase306–310: source transport, Picard minors and split-trace boundary.
- Phase311–318: inert trace, conductor-125 wild logarithms, exact local lifts, radical pencils and exact global norm-fibre vetoes.
- Phase319: full maximal-order completion of the D163 second-wild normal-map experiment.

Phase319's central distinction: the one-dimensional radical-normal channel on the 109-point even-coordinate source disappears on the 225-point full maximal-order support. The full symmetric local differential span remains nonzero.

Reader guide: `research/phase319/README.md`.

### Phase320 — cross-field second-wild normal maps

D163, D187 and D203 have class numbers 1, 2 and 4, while 5 is inert in all three. The experiment compares:
- matched (R=40,J=1) supports;
- native row/jet geometries;
- even-b index-two suborders versus full maximal-order supports;
- primitive Gram ranks, radicals, Smith layers, full differential spans and radical-normal images.

Phase320-A and Phase320-B are separately preregistered. The current local arithmetic-kernel cross-check is explicitly provisional; the full Phase315 conductor-125 log replay and first-wild-digit gates remain mandatory before merging Phase320.

Reader guide: `research/phase320/README.md`.

## What is already merged into research parents

- Phase277–292 constituent PRs #167, #170, #178–#182 merged into `research/phase277-292-noether-smith-fabric`.
- Phase293–303 integration PR #213 merged into that same research fabric.
- Phase306–319 constituent research PRs merged into `research/phase309-original-source-picard-minors`.
- The Phase269 finite certificate was integrated into the unified research branch, not promoted to main.

The current umbrella integration PR is #217. It remains a research-only consolidation and is not to be merged until the Phase320 full local-log and exact-head checks are complete.

## The open mathematical boundary

1. **Global ideal arithmetic for class number greater than one.** D163's principal split-prime generator family does not exhaust D187/D203 prime ideals. A continuation must use ideal-aware ray class arithmetic, not element division as a proxy.
2. **Source completion versus local equivalence.** A 5-adic unit coordinate change does not identify finite norm-ball supports. Even-b suborders and full maximal orders must remain distinct samples.
3. **Primitive residual pairing.** A raw Gram radical is not additive valuation mass. The actual primitive pairing and its Smith filtration must be reconstructed on the same source.
4. **Uniformity.** Finite D163/D187/D203 computations do not establish a uniform class-number-one valuation or a new discriminant cutoff.
5. **321^4.** PR #157 remains a separate candidate with its own proof and independent semantic-review obligations. The accepted (322^4) theorem remains the publication endpoint.

## Evidence labels

- **P:** exact algebraic identities under stated hypotheses.
- **M:** finite source-specific computations after exact-head tests.
- **H:** field-uniform arithmetic or analytic statements still requiring proof.
- **R:** source conflation, double-counting, nonprincipal ideal omission, or residue-to-valuation promotion.

No branch in this research fabric changes `main`. No additional determinant valuation is inferred from a changed residue modulo 25.


### Phase321 — ideal-aware ray class groups (preregistered)

The next global step is now preregistered in `research/phase321/PRE_REGISTERED_IDEAL_AWARE_RAY_CLASS_GROUP.md`. It constructs the full ray class groups modulo (125) for class numbers 1, 2 and 4, using reduced-form ideal representatives and an exact cocycle. The predicted orders are 7,500, 15,000 and 30,000. The extension is not assumed to split, and nonprincipal split-prime ideals are retained. This is the missing bridge before any honest global character comparison across D163, D187 and D203.
