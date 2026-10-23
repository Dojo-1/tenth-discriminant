# Phase 12 preregistration: the explicit order's norm

Date: 2026-10-24. Base: draft PR #28 head `5beb7d7`, open and
unmerged. This protocol precedes proof edits.

## Exact bounded target

For `D ≡ 3 (mod 4)`, let `c=(D+1)/4` and
`A=ℤ[T]/(T²-T+c)`. Prove in Lean that the algebraic norm of
`x+yT ∈ A` over `ℤ` is `x²+xy+cy²`. The intended proof is the
two-dimensional multiplication matrix in the basis `(1,T)`:

    [x   -cy]
    [y   x+y]

whose determinant is the stated quadratic form. If a pinned Mathlib
API makes the literal norm theorem disproportionate, prove the exact
matrix/determinant identity and report the unclosed norm transport,
without substituting a numerical check.

This does **not** identify `A` with the maximal ring of integers of
`ℚ(√-D)`. It does not prove the class-number-one to principal-form
lifting theorem for that field, a checked cutoff, or classification.

## Controls and stop rule

Check `D=15`, where `c=4`: the form is `x²+xy+4y²`.
Preserve the Phase 9 `D=15,p=3` negative lifting control. Do not
infer maximality or PID from the order-level norm formula. Stop after
one bounded Lean proof attempt if the required basis/norm transport
needs a new large theory; document the precise remaining lemma.

Run targeted Lean, full pinned build, source correspondence, compiled
dependency audit, and inherited negative controls on any proof head.
Update current status and the human guide. Keep the PR draft and do
not merge; do not change numerical certificates or cutoff constants.
