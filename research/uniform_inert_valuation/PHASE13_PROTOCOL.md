# Phase 13 preregistration: identify the chart with algebraic norm

Date: 2026-10-24. Base: draft PR #28 at `4133023`, open and
unmerged. This protocol is committed before proof edits.

## Exact target

For every integer `c`, set `A_c = AdjoinRoot (X²-X+C c)` over `ℤ`
and `T = AdjoinRoot.root`. Prove in Lean that `A_c` has the two-element
power basis `(1,T)` and, for integers `x,y`,

    Algebra.norm ℤ (of x + of y * T) = x² + xy + cy².

The prior phase checks the quotient relation, the nontrivial
multiplication column and the integer determinant. This phase must
connect that matrix to the *actual* `Algebra.norm` through
`AdjoinRoot.powerBasis'` and `Algebra.norm_eq_matrix_det`, or an
equivalent verified basis argument. No arbitrary replacement norm.

## Controls and stop rule

Check `c=4` (`D=15`) and a coordinate sample such as `(x,y)=(0,1)`:
the norm is `4`. Check the constant coordinate `y=0`, whose norm is
`x²`; this guards matrix orientation and rank. A false universal
lifting claim remains refuted by `D=15,p=3` from Phase 9.

If pinned Mathlib's basis transport requires a substantial new
theory, stop after a bounded attempt and preserve the exact failed
lemma and errors. Do not state the norm theorem unless Lean accepts
it. Even a proved order norm does not identify `A_c` with the maximal
integer ring of `ℚ(√-D)`; this is a separate obligation. Nor does it
close the chosen-radius area proof, analytic cutoff or classification.

Run targeted Lean, full pinned build, source correspondence, compiled
dependency audit and negative controls on any final proof head. Keep
the human guide and current status claim-safe, keep PR #28 draft,
and do not merge or alter numerical certificates.
