# Phase193 — original thin-ellipse geometry at fourth root 328

*3 November 2026 · scoped Lean theorem targets, not a field cutoff.*

The work here changes **only the lower fourth-root threshold**. The evaluation support, derivative convention, integer lattice, trace pairing, and polynomial dimensions remain the source definitions:

- \(R=\lfloor D/4\rfloor,\quad S=\lfloor R/25\rfloor\)
- \(Q_{\mathrm{thin}}=\mathrm{ellipsePairs}(D,\mathrm{thinRadius}(D))\)
- \(Q_{\mathrm{old}}=\mathrm{ellipsePairs}(D,\rho(D))\), used **only** to provide a padded point-count majorant and its separate positivity statement
- \(G_Q=E_QB_QE_Q^{\mathsf T}\), with the original ordinary-\(Z\) jets holding \(W\) fixed and original trace weights \(2,2D\).

The checked \(331^4\) construction is a source template, not permission to weaken its hypotheses automatically. Each new 328 statement must compile with its *own* explicit \(D\ge328^4\) premise.

## Actual geometry question

The elementary cell-covering *sufficient* interpolation-radius criterion requires the nonnegative remainder

~~~math
\left(\frac{11}{25}-\frac{1001}{1000}\frac{407}{1000}\right)t-10
=\frac{32593}{1000000}t-10,\qquad t=D^{1/4}.
~~~

Its exact values are \(+0.690504\) at \(t=328\), \(+0.006051\) at \(307\), and \(-0.026542\) at \(306\). These values concern **this sufficient guard**, not actual rank failure or an impossibility theorem for smaller roots.

In [SourceGeometry328.lean](../../lean/TenthDiscriminant/SourceGeometry328.lean) the original point-count proof is reconstructed with \(t\ge328\); the existing \(R\ge80t^3\) estimate uses only \(t-320\ge8\), not the older \(t-320\ge11\). It also checks the old padded radius ratio and the unaltered \(8/9\) thin-radius relation. In [SourcePositivity328.lean](../../lean/TenthDiscriminant/SourcePositivity328.lean) the original interpolation count then yields **positivity of the same integer thin trace Gram**, while inclusion of the thin support in the larger original padded support yields the separate padded positivity and count majorant.

If these modules compile with their exact-head source checks, the step from 331 to 328 for *rank and positivity* is independently closed. That still leaves a matching original thin-Gram analytic upper, the arithmetic specialization and field return. The arithmetic half is separately checked in [Phase191](https://github.com/Dojo-1/tenth-discriminant/tree/research/phase191-328-arithmetic-preflight) and the improved floor ratio in [Phase192](https://github.com/Dojo-1/tenth-discriminant/tree/research/phase192-tight-floor-recovery), without adding new primes.

## Evidence ledger and falsifiers

- **P, already in main**: the \(331^4\) actual-field theorem; Phase190's original-prime \(0.0879\) gain.
- **P, standalone exact-head CI:** Phase191's \(328^4\) conditional odd-plus-binary source lower and scalar separator, and Phase192's stronger \(0.0895\) generic source-floor recovery. These are not yet integrated field theorems.
- **H until exact-head focused CI:** source count, radius and positivity on the **original** \(328^4\) thin support.
- **H even after this CI:** the matching normalized analytic Hadamard upper and field-discriminant return at 328.
- **R (prohibited):** replacing the thin determinant with a padded one; changing ordinary derivatives into another derivative convention; importing a \(331^4\) theorem as if it held at 328; claiming the cell-covering guard fails as a theorem about actual interpolation.

**Kill conditions:** a counterexample to an exact original support inclusion or point-count premise; a failed Lean build; a changed source definition; extra mathematical axiom; or a mismatch between the Gram in the arithmetic and analytic branches. Independent mathematical reconstruction remains [Issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50).
