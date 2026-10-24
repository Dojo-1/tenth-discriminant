# Phase 15 preregistration: a genuine quadratic field chart

Date: 2026-10-24. Base: draft PR #28 at `8d15fbb`, pinned CI
`40039967991` and CodeQL passed. This protocol precedes proof edits.

## Target

For positive `D ≡ 3 (mod 4)`, let `c=(D+1)/4` and
`f=X²-X+c ∈ ℚ[X]`. Prove in Lean that `f` is irreducible over `ℚ`,
so `AdjoinRoot f` is a field, and establish a rank-two rational basis
`(1,T)` with `T²=T-c`. Connect an arbitrary field element to unique
rational coefficients. This field chart should be the precise target
for Phase 14's rational trace/norm criterion and Phase 13's integer
order, not a new numerical or class-number claim.

If the pinned API permits, prove the actual integral-closure/order
equivalence. The full objective is that equivalence; field existence
and rational coordinates alone are progress, not a substitute.

## Routes and falsifiers

Route A: use the monic degree-two irreducibility criterion and the
negative discriminant `1-4c=-D<0`; then `AdjoinRoot.powerBasis'`.
Route B: show a rational root would make a nonnegative square equal
`-D`, contradicting positivity. Explicitly test `D=15,c=4`.
As a negative boundary, `D=-1,c=0` (outside the positive hypothesis)
has `X²-X` reducible. Do not generalize irreducibility to arbitrary
integer `D` or conflate an integral order with its field.

Stop after a bounded attempt if the field-to-maximal-order transport
requires a substantial new theory. Retain the strongest checked
theorem, exact failed attempts and next obligation. Run targeted Lean,
full pinned build, source correspondence, dependency audit and
negative controls on the proof head. Update human documentation,
keep the PR draft and do not merge.

## Execution (2026-10-24)

The full target compiled in `QuadraticFieldChart.lean`. Negative
discriminant gives irreducibility; `AdjoinRoot` supplies the genuine
number field and its rational `(1,T)` basis. The existing integer
order maps injectively into this field and its ring of integers.
Trace and norm of an arbitrary field coordinate pair are computed
from the actual left-multiplication matrix. Mathlib's integrality
of trace/norm and Phase 14's squarefree/parity lemma force integer
coordinates for every algebraic integer. Hence the map is onto:
`halfOrderEquivRingOfIntegers` is a checked ring equivalence.
`halfOrder_ringOfIntegers_norm` identifies the maximal-ring norm of
the explicit coordinates with the repository's `principalNorm`.

The `D=15,c=4` irreducibility control and `c=0` reducibility
counterexample compile. Initial failed scripts exposed a needed
noncomputable field declaration, a degree-cast mismatch, ring-hom
constructor field order, and basis-projection normalization; all
were repaired. This equivalence does **not** itself prove that class
number one supplies `SmallPrimeNormLifting`: the quotient and norm
steps still need composition, including the sign of the norm.
The chosen-radius area, analytic comparison and classification also
remain open.
