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
