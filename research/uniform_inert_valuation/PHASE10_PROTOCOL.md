# Phase 10 preregistration: class number one turns a residue quotient into a norm

Date: 2026-10-23. Base: Phase 9 proof head `ed70043`, draft PR #28,
open and unmerged. Register this protocol before any new proof edits.

## Exact target

In pinned Mathlib, prove the following statement for an arbitrary number
field `K`: if `NumberField.classNumber K = 1` and there is a ring
homomorphism `f : 𝓞 K →+* ZMod p` for prime `p`, then there is an
`a : 𝓞 K` with `Int.natAbs (Algebra.norm ℤ a) = p`. Use the existing
`classNumber_eq_one_iff` to obtain principality, the kernel quotient
isomorphism to `ZMod p`, and the existing absolute-norm formula for a
principal ideal. If automatic surjectivity of `f` is unavailable, make
surjectivity an explicit hypothesis instead of assuming it.

This is the ideal-theoretic middle step, not a class-number-one to
`SmallPrimeNormLifting` theorem. The latter still requires (1) a ring
map from each root of `X²+D` modulo odd `p` to the maximal order of
the specific imaginary quadratic field, and (2) a checked coordinate
identity connecting `Algebra.norm ℤ a` with `principalNorm D x y`.

## Controls and stop rule

Retain the Phase 9 `D=15,p=3` counterexample to any unconditional
lifting claim. A field with class number greater than one may have a
residue quotient without a norm-`p` generator; do not drop the class
number hypothesis. Keep the absolute value: this abstract theorem
does not know the field is imaginary quadratic, so it cannot assert a
positive signed norm. Check `K=ℚ,p=3` as a positive toy instance if
the library supports it without a disproportionate detour.

Log failed proof attempts. Run targeted Lean, full pinned build, source
correspondence, compiled dependency audit and inherited negative
controls. Update human-facing documentation with the exact remaining
two arrows. No saved certificates or cutoff change; do not merge.

## Execution record

Pending.
