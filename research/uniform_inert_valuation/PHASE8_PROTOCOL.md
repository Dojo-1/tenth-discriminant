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

## Execution record

`QuadraticResidueRing.lean` gives the already used residue coordinate
pair a commutative-ring chart. Its multiplication and powers are proved
equal to `residuePairMul` and `residuePairPow`; the chart is injective,
so an equality proved there returns to the **same two coordinates**.
This is not a replacement Gram or a discarded-residue sample set.

`InertFrobenius.lean` proves the generator's even/odd powers directly,
uses Euler's criterion to obtain `t^p=-t` from nonsquareness of `-D`,
and applies characteristic-`p` Freshman's dream plus Fermat to
`x+yt`. It transports that identity back to both integer coordinates
of `a^p-conjugate(a)`, then applies Phase 7's actual integer Gram
valuation theorem. The resulting exponent is the pre-existing exact
`2*valuationWeight R S p`; no new cutoff is inferred. The `D=19,p=3`
nonsquare and `D=2,p=3` square controls are checked.

First Lean attempts failed on coordinate extensionality, unfolding the
new ring operations, subtraction in the conjugate chart, the nonsquare
zero witness, a dependent rewrite of `p`, and an integer-to-`ZMod`
cast of subtraction. These were proof-script failures, not failed
mathematical claims; the repaired targeted files compile. The odd-prime
guard remains explicit, and nonsquareness is a hypothesis, not silently
identified with field inertness for arbitrary `D` or a prime dividing
the conductor. Class-number-one to local nonsquareness, cell-area
formalization, analytic cutoff and finite classification remain open.

Local verification from `lean/`: `lake env lean
TenthDiscriminant/QuadraticResidueRing.lean`, the analogous command for
`InertFrobenius.lean`, `lake build` (6699 steps), and
`python verify_sources.py` passed. The source check verifies endpoint
correspondence, not Arb inequalities. `git diff --check`, task-state JSON
parsing and the proof-placeholder scan passed. The final-head compiled
dependency audit and inherited negative controls belong to pinned Linux
CI and must be reported separately.
