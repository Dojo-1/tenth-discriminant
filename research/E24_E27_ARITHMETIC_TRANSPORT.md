# E24–E27 · THE LATTICE REMEMBERS
*Source-locked arithmetic worldlets · moving-moving-frame transport · 18 November 2026*

> The coordinates may move. The algebra can move. A valid witness does not move by fiat.

## Mathematical authority

The actual selected source lattice in TenthDiscriminant.IntegerTraceGram is the integer pair (x,y), interpreted as x+y sqrt(-D). The source explicitly says this is not necessarily the full ring of integers. Its native functions for multiplication, conjugation, ordinary-Z derivative rows, integer trace pairing, and original rectangular Gram remain unchanged.

E24, E25, E26 and E27 each passed an exact-head focused Lean 4.19 + Mathlib build and #print axioms verification on the research branch, using only propext, Classical.choice and Quot.sound; no sorryAx:

- [E24 original Gram and square-index order transport](https://github.com/Dojo-1/tenth-discriminant/actions/runs/44294303700).
- [E25 nested integer frames and partial reverse](https://github.com/Dojo-1/tenth-discriminant/actions/runs/44294937606).
- [E26 original Gram invariance and future observer obstruction](https://github.com/Dojo-1/tenth-discriminant/actions/runs/44295776014).
- [E27 square-index/conjugation naturality](https://github.com/Dojo-1/tenth-discriminant/actions/runs/44296414214).

**Full-root audit and PR release are separate checks. Do not promote the stack on the basis of focused CI alone.**

## The transport family

For positive k, the embedding of the selected quadratic suborder is

    iota_k: Z[sqrt(-D k^2)] -> Z[sqrt(-D)],
    iota_k(x,y) = (x,k y).

It is additive, multiplicative, unital, conjugation compatible, injective and original-jet preserving. This is NOT a surjective map of all integer-pair lattices for k>1. On any finite sample Q, ordinary jet order J and rectangular dimensions R,S:

    originalIntegerGram_(D k^2)(Q; J,R,S)
      = originalIntegerGram_D(iota_k(Q); J,R,S).

Every original integer trace entry is the same under the transported support. The number of rows, derivative convention, conjugate-frozen Z derivative, factor 2 and source rectangular enumeration have not changed.

Nested transports compose: iota_k after iota_l equals iota_(kl), including at the *intermediate observation support*. An inverse on the full target integer lattice does not exist for k>1.

## Two different determinants

The positive trace-with-conjugation pairing on the canonical selected basis has matrix diag(2,2D) and determinant 4D. Under the index-k basis change its determinant scales by k^2. E24 proves this exactly.

This is a determinant of an **integral basis trace form**; it is NOT the same observable as the determinant of the J-jet **sampling Gram** on matched observations. It is also not a theorem about the fundamental field discriminant.

For the explicit k=2, D=1 control, the rational field remains Q(i), but the selected integer orders are Z[i] and Z[2i]. The latter has index two. The example is deliberately nonfundamental at D=4; it is not an input to the D>=300^4 squarefree field theorem.

The source E14 normalization (x,y) -> (x,-2y) agrees as an INTEGER FUNCTION with iota_2 after conjugation. **Their typed algebraic interpretations are not automatically the same**: E14 is a fixed-D chart transform, E24 is a map between D*k^2 and D source multiplication laws.

## The counterworld

With J=1, source rows 1 and Z, and transported target support Q={(0,2)} at D=1, the original integer Gram is diag(2,8), determinant 16. Enlarging the target support to {(0,1),(0,2)} changes the Gram to diag(4,10), determinant 40.

The extra target node has no integral preimage in the source index-two order. This change is not a coordinate effect.

For k=2, E25 constructs the exact partial inverse. It returns Some(x,y/2) for even y and None for odd y. It proves a decoder using only x cannot reconstruct this future operation. The arithmetic obstruction concerns original witness existence and definedness, not Euclidean norm.

## Nontrivial arithmetic holonomy

Conjugation (x,y)->(x,-y) is nontrivial. The original observation-conjugation theorem preserves every source Gram entry when the entire support moves, and E26 proves the quadratic norm is unchanged. Yet the original jet channel and a later operation requiring y>0 change. The norm cannot decode that future partial operation.

E27 closes the moving-moving-frame square at the source, showing

    iota_k(conj p) = conj(iota_k p)

and *both* arithmetic/conjugation path orders yield the SAME original integer Gram and determinant. No independent new sampling set or field identification is injected.

This is a typed commuting-square theorem, not a claim of Riemannian curvature or nontrivial cohomology.

## Two different limits, two different remembered worlds

The descending order tower A_n=Z[2^n i], with inclusion A_(n+1)->A_n, has common inverse-limit witnesses exactly Z: an integer imaginary coefficient divisible by every 2^n must be zero.

By contrast, the inverse system of residue observations Z/2^nZ has limit Z_2, retaining an infinite compatible 2-adic digit history. Both are classical facts, but they use DIFFERENT carriers, arrows and observation semantics. These infinite-limit facts are not formalized by E24–E27 and must not be relabeled as their Lean theorems.

## Open typed remainder

We have **not** built field/order isomorphisms for different nonsquare quadratic classes; shown transport of ideal factorization or local prime valuations through nonmaximal suborders; proved the full E21 field cutoff from this transport; supplied a global sheaf/gerbe connection; or shown computational hardness improvements.

The next source-preserving goal is a typed arithmetic Worldlet/transport record with explicit algebra, integral order, normal or partial inverse, jet operator, trace metric, support and provenance. Only then should we pose universal compatibility or infinite-limit statements, with independent counterworld tests.

Reference links: [HK-029 observable holonomy](https://github.com/Dojo-1/Hardness-Kernel/pull/28) and [Tenth Discriminant research ledger #225](https://github.com/Dojo-1/tenth-discriminant/issues/225).
