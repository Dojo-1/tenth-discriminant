# Phase 11 preregistration: a quadratic root defines an order quotient

Date: 2026-10-24. Base: draft PR #28 head `34f7690`, open and
unmerged. This protocol precedes new proof edits.

## Exact bounded target

For `D : Nat` with `(D : Int) % 4 = 3`, define the monic integer
polynomial `F_D(T)=T²-T+(D+1)/4`. For an odd prime `p` and a root
`z²=-D` in `ZMod p`, set `t=(1+z)/2`. Prove in Lean that `F_D(t)=0`,
then use the pinned `AdjoinRoot.lift` universal property to construct
an actual ring homomorphism

    AdjoinRoot F_D →+* ZMod p

which sends the adjoined root to `t`. Check the relation between `z`
and `t` in both directions (`2t-1=z`). This order-level map is the
field-specific source of the abstract quotient used in Phase 10.

If an exact free-basis norm formula is readily available, prove it
for `x+yT`: multiplication by that element has determinant
`x²+xy+((D+1)/4)y²`. Do not claim this order equals the maximal
ring of integers or that its PID property follows from the field's
class number one; those identifications are separate proof obligations.

## Controls, stop rule and verification

`D=15,p=3,z=0` is a ramified-root control. An odd prime is essential
for dividing by two; make the guard explicit, not an implicit field
operation at `p=2`. Retain the strict Ender endpoint and the prior
`D=15,p=3` failure of principal norm lifting: the mere existence of
this new order map must not be presented as a norm-`p` element.

Log failed proof steps and any mathematical counterexample. Run
targeted Lean, full pinned build, source correspondence, compiled
dependency audit and inherited negative controls; keep the PR draft
and do not merge. Update the human guide and current status with the
maximal-order boundary. No numerical experiment or cutoff changes.

## Execution record

`HalfOrderResidue.lean` proves the integer coefficient identity,
odd-prime invertibility of `2`, the root relation for
`t=(1+z)/2`, and the actual `AdjoinRoot.lift` ring map. Lean checks
its value on the adjoined root, recovers `z=2t-1`, and proves
surjectivity. The `D=15,p=3,z=0` control constructs such a map even
though Phase 9 proves that principal norm lifting fails there.

The first Lean attempts failed on noncomputability declarations,
integer-cast transport, a polynomial constant evaluation normal form,
and the elaboration of `lift_root`; these were proof-script issues.
An attempted extra control that normalized `(1:ZMod 3)/2` to `2`
stalled at modular inverse evaluation. It was removed because the
preregistered control requires the quotient map, not that incidental
normal form; the final control proves a surjective map exists.

Targeted `lake env lean TenthDiscriminant/HalfOrderResidue.lean`
passed. Full `lake build` completed 6702 steps; `python
verify_sources.py` passed from `lean/` with its endpoint-only scope;
`git diff --check` and task-state JSON validation passed. The
optional algebraic norm formula was **not** proved. The order's
identification with the maximal integer ring remains open. Pinned
Linux CI, compiled dependency audit and inherited negative controls
on the final head are to be reported separately.
