# E45 — full ellipse orientation rigidity and zero aggregate CRT gap

**Date:** 19 November 2026. **Status:** H pending fresh exact-head Lean and transitive axiom checks. Research draft stacked over E44 / PR #256. Do not merge for a discriminant bound.

## Source and result
The **same original** `ellipsePairs D rho`, with the original ordinary-Z jets, trace and rectangular Gram left untouched, is closed under `(x,y) -> (x,-y)`. For any finite conjugation-saturated support, if a pointwise identity-or-conjugation map is injective on that support, then its image is the SAME support. This strengthens E43's interpretation in precisely the regime used by the large original thin ellipse, without asserting a new source-bound improvement.

The original ellipse has `sum(q.2)=0`. At D=1, E44's native extra labelled Gaussian CRT aggregate `totalPrimeGap(Q)=4*sum(q.2) mod 5` consequently vanishes on every complete ellipse, even though E44's sparse positive-control has gap 3.

**Important:** Zero aggregate gap does NOT mean that each individual labelled prime observation is zero, or that a richer ordered observer is useless. Nor does it mean all information relevant to determinant valuation vanishes. The E44 probe is a different measurement and remains separate from the original Gram determinant.

## Falsification and controls
- Exact finite oracle on D=1,2,3,5 and rho=1,2,3,4 found closure and zero imaginary sum in all 16 tested full sources.
- Exhaustive independent conjugation choices on small positive-imaginary source pairs supported the finite injectivity restriction.
- Source-level negative control: E43 noninjective partial toggle collapses two original points and is NOT covered by this theorem.
- E44 sparse-source positive control still gives CRT gap=3.
- The theorem is not a new field cutoff, p-adic factor or numerical complexity lower bound.

## E45 -> arithmetic gate (not discharged)
A new original-Gram p-factor requires a single valid source-specific integral unimodular row transformation U and universal divisibility of each original ordinary-jet coefficient in that transformed row for **every** q in the original full thin ellipse and all required derivative indices j. If the source contains q=(0,0) and degree-0 row 1, no positive p divides its constant evaluation; any row-factor theorem must explicitly account for unimodular mixing and the whole row family. Test near-axis / boundary samples as adversarial controls.

## Other independent branches
Phase352 / PR #249 supplies a five-band uniform paper-level source-count argument for D>=274^4; it is NOT a formal 274^4 actual-field theorem. The maximal-order/field-chart source-reconstruction issue #50 remains open.

Proof target: `lean/TenthDiscriminant/E45FullEllipseOrientationNull.lean`; focused CI: `.github/workflows/e45-full-ellipse-orientation-null.yml`.
