# Phase184 — positivity of the same original Grams at fourth-root 331

*3 November 2026 · source-specific Lean proof target, not a new field-discriminant theorem.*

The [Phase183 geometry](https://github.com/Dojo-1/tenth-discriminant/pull/106) is enough to attempt another indispensable step without changing what the Tenth Discriminant proof is about: positivity of the **original integer trace-Gram matrices**. No alternate polynomial, sampling set, or weighting is introduced.

## Freeze both source objects

For $D\ge331^4$, retain the original dimensions and radii:

~~~math
R=\lfloor D/4\rfloor,\quad S=\lfloor R/25\rfloor,\quad
r=\lceil(11/25)D^{3/4}\rceil,\quad
\rho=\lceil(13/25)D^{3/4}\rceil.
~~~

The original integer ordinary-$Z$-jet matrix $E_Q$ uses the old $J=S$ derivative convention, $W$ fixed, and trace weights $2,2D$.

The two distinct original observation sets must remain distinct:

~~~math
Q_{\mathrm{thin}}=\mathrm{ellipsePairs}(D,r),\qquad
Q_{\mathrm{padded}}=\mathrm{ellipsePairs}(D,\rho).
~~~

Their Grams $G_{\mathrm{thin}}$ and $G_{\mathrm{padded}}$ are *different matrices*. A monotone point-count argument does **not** assert equal or ordered determinants.

## Proof targets

The source geometry [SourceGeometry331.lean](../../lean/TenthDiscriminant/SourceGeometry331.lean) copies the previously compiled Phase183 source-ellipse declarations into an importable Lean module. The standalone research copy is retained as historical evidence and CI asserts byte-for-byte equality to prevent divergence.

The new [SourcePositivity331.lean](../../lean/TenthDiscriminant/SourcePositivity331.lean) uses the same established source machinery to prove:

1. The original thin radius is at most the original padded radius.
2. The proved thin interpolation count transports to the *padded point count* by inclusion.
3. The existing padded cardinality majorant bounds the thin point count.
4. The original thin and padded integer trace-Gram determinants are strictly positive, using the original integer-jet positivity theorem with the already checked point-count prerequisites.

These are **geometry and positivity** statements; no logarithmic determinant inequality or class-number contradiction is asserted.

## Evidence and promotion

- **P (pre-existing):** the original integer Gram positivity theorem, ellipse support definition, and source-specific Phase162–183 foundations under their exact Lean imports and permitted assumptions.
- **H (new target):** the Phase184 source-specific positivity lemmas until exact-head Lean compilation and source checks succeed.
- **M:** the earlier exact rational and original-ellipse finite controls have their own receipts; no production-range performance measurement is claimed here.
- **R:** the old stronger $3R+S$ padded interpolation premise at 331 is not reused; support inclusion does not imply Gram determinant comparison.
- **Open:** the odd-prime plus once-counted binary lower, the normalized analytic upper on this *same* thin Gram, and the actual-field return at 331 remain separate obligations.

**Kill:** altered jet source, altered trace weights, replacing point-count monotonicity by a Gram determinant inequality, any new axiom, source mismatch, or failed focused compilation. **Stop:** do not promote a 331 field bound until the original lower and upper are linked to the very same positive determinant and full axioms/source/known-false controls pass.

Independent semantic reconstruction remains [Issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50). The latest merged field theorem stays at $375^4$.