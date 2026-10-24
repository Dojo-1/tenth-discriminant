# Phase 19 preregistration: assemble local factors on the actual determinant

Date: 2026-10-24. Base: draft PR #28 head `ce60ba4`, pinned Lean CI
`40074461750` and CodeQL passed. This protocol precedes proof edits.

## Exact target

For positive squarefree `D ≡ 3 (mod 4)`, class number one of the actual
imaginary quadratic field, positive `R,S`, and Ender's unchanged integer
radius at an interval upper endpoint, use the **same**
`integerRectangularTraceGram (ellipsePairs D rho) D S R S` throughout.
For any finite set of distinct odd primes `p < R` satisfying
`p < (D+1)/4`, prove that the product of the existing factors
`p^(2*valuationWeight R S p)` divides its positive integer determinant.
Then derive the exact real sandwich: that product is at most the
determinant, which is at most the existing Hadamard diagonal product.
The point-count premise must come from the checked chosen-radius theorem,
not from an assumed injectivity or substituted matrix.

The intended local-to-global operator is coprime product assembly: distinct
prime powers are pairwise coprime. The real comparison uses the existing
integer-to-real determinant cast. A logarithmic corollary may be added only
if positivity of every logarithm argument is proved.

## Scope and falsifiers

Do not infer the factorial lower estimate, the numerical interval
contradictions, the all-`D` envelope, or a class-number classification from
this product inequality. Keep `p=2` outside the prime set. Preserve strict
`p < (D+1)/4`: an equality or larger endpoint cannot inherit the local
theorem. Test the empty set (product one), a concrete single-prime case,
and reject a proposed product theorem lacking distinct-prime/coprimality
guards. The `D=15,p=3` global obstruction remains an inherited negative
control. No `sorry`, new axiom, or unproved imported numerical premise.

If the full specialization does not compile, retain only checked abstract
assembly lemmas and record the exact remaining bridge. Run targeted Lean,
the full pinned build/audit/negative controls, source correspondence,
and report exact head and PR status without merging.

## Execution (2026-10-24)

Protocol-only commit `65bbaed` preceded Lean edits. The target now compiles
in `PrimeMassAssembly.lean`: the coprime product divides the original
integer ellipse Gram; the checked chosen-radius count makes it positive;
the determinant cast and Hadamard give the exact product sandwich and finite
sum-of-logs inequality for **all** odd primes below `R`. Empty, singleton,
and duplicate-factor controls compile. A first targeted check exposed only
proof-interface errors (quadratic-field `Fact` guard, an unsupported `on`
notation, and a Nat/Int cast); the guard was retained and the proof repaired.
No mathematical claim was weakened. Factorial, aggregate analytic, Arb,
universal-envelope, and classification links remain open. Targeted Lean,
the full 6709-step `lake build`, and endpoint-only source correspondence
pass locally. Final-head pinned CI status is recorded separately in the
task state.
