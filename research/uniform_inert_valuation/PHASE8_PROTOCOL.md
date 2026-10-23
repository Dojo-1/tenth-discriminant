# Phase 8 preregistration: inert residue to universal Frobenius

Date: 2026-10-23. Base: PR #27 proof head `b70cc3b` (draft,
unmerged). This protocol precedes new proof edits. The bridge uses the
existing selected pair order and the existing integer Gram, not a new
determinant.

## Exact target

For an odd prime `p`, and `D : Nat` with `-D : ZMod p` nonsquare,
prove first that the residue generator `t=(0,1)` satisfying `t²=-D`
obeys `t^p=-t` in the repository's `residuePairPow` coordinates. Derive
this from Euler's criterion (or its equivalent exact power statement),
not from a finite example. Then prove for every `a : Int × Int` that
`residuePair p (pairPow D a p) = residuePair p (pairConj a)`;
equivalently both integer coordinates of `a^p-conjugate(a)` are divisible
by `p`. Compose this **proved universal premise** with Phase 7's actual
integer Gram theorem to obtain `p^(2F(p)) | det G` for arbitrary finite
samples, rectangle and derivative cutoff.

The extension from `t` to every `x+yt` requires a genuine characteristic-
`p` Freshman's-dream argument in the same residue algebra, including
Fermat on coefficients. If the existing representation blocks that step,
stop at a precisely stated checked generator theorem and record the
remaining equation; do not silently promote the general congruence.

## Falsifiers and limits

Retain the checked `D=19,p=3` inert pilot and `D=2,p=3` split
counterexample. Test the odd-prime guard and empty sample/grid cases.
Nonsquareness of `-D` in this selected order is the local hypothesis;
do not replace it by a bare field-inertness assertion when the conductor
may be divisible by `p`. This phase does not formalize class groups,
the cell-area estimate, the analytic cutoff, or classification. Record
failed Lean steps. Run targeted Lean, source correspondence, full build,
compiled dependency audit and inherited negative controls on pinned CI.
Keep the PR draft and do not merge.
