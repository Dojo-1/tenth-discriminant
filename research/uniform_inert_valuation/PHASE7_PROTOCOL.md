# Phase 7 preregistration: act on the actual derivative rows

Date: 2026-10-23. Base: merged PR #25, `a4da896`. This file is committed
before new proof edits. The target is not a newly chosen Gram matrix.

## Exact target

For arbitrary `D,R,S,p,J`, `p>0`, row `i : Fin (R*S)`, original pair
sample `a`, and ordinary derivative order `j`, set `r=i/S`, `s=i%S`,
`k=rectangularBasisExponent R S p i`, `z=pairZsqrtdEquiv D a`. Prove
the samplewise row identity

```
Σ h, rectangularBasisMatrix R S p i h •
  pairZsqrtdEquiv D (integerDerivativeRow D (h/S) (h%S) j a)
=
((derivative^[j])
  (X^(r-p*k) * C(star z)^s * (X^p-C(star z))^k)).eval z.
```

The finite sum is over **all original columns**, and the same sample is
used on both sides. The proposed proof factors into (1) an exact
canonical monomial/ordinary-jet identity, (2) an exact binomial
polynomial identity with the rectangle guards, and (3) reindexing
against the already checked integer coefficient matrix. If all three
close, instantiate the existing trace pairing bilinearly to construct
the actual two-sided Gram factor, then invoke the conditional valuation
theorem. This last step must not be claimed from the row identity alone.

## Falsifiers and scope

Check empty rectangles, `j>r` derivatives, the `4×2,p=3` row-six
identity `Z³-W`, and a non-real sample so `W` cannot be mistaken for
`Z`. Preserve the original finite sample indexing; reduction modulo p
may collide samples. Ordinary, not Hasse, derivatives are required.
Record failed Lean steps and any remaining equation in full. Do not
promote the paper proof, radius count, analytic cutoff or class-number
classification to a checked theorem. Run targeted Lean, source
correspondence, full build, dependency audit and negative controls;
publish only a draft PR and do not merge.

## Execution record

The preregistered row identity is in
`lean/TenthDiscriminant/RectangularRowAction.lean`. It identifies every
original integer-coordinate ordinary derivative row with its jet in
`ℤ[√(-D)]`, proves the guarded binomial polynomial identity, reindexes
the explicit integer basis matrix, and then proves the samplewise
commuting identity. The actual-row coordinate divisibility theorem uses
the explicit zero-order Frobenius premise; no inertness is inferred.

`lean/TenthDiscriminant/RectangularGramFactor.lean` proves bilinearity for
the unchanged factor-two trace, uses the original `Q` indexing to show
`UGUᵀ=D_p K D_p` for an integer `K`, and invokes the earlier checked
determinant-one and exponent-sum theorems. The final theorem states
`p^(2*valuationWeight R S p) | det G` for all finite `Q`, natural
`D,J,R,S`, and `p>0`, **assuming** the universal coordinatewise
Frobenius congruence on integer pairs. Empty grids and high derivatives
are inside these universal statements; no nonempty-grid or depth guard
was added. The previously checked `4×2,p=3` and non-real sample controls
remain in their original modules. These are not a general inertness proof.

Proof-script corrections during development included the high-derivative
zero branch, binomial-sum reindexing and quotient/remainder row labels,
fourfold finite-sum order in Gram bilinearity, and diagonal-scale
association. The first versions failed elaboration or goal closure; the
repaired general files compiled. An optional specialized `D=19,p=3`
corollary caused a prolonged silent local compilation after adding
extra imports. It was removed rather than counted as a successful new
control; the general conditional theorem does not depend on it.

The remaining bridge is precise: derive the universal Frobenius premise
from the intended inert-prime hypotheses in the selected quadratic order,
then connect it to the class-number-one and analytic hypotheses. The
cell-area count is still a paper argument, not a Lean theorem. No checked
cutoff or classification is claimed here.

Local verification: `cd lean; lake env lean
TenthDiscriminant/RectangularRowAction.lean`, the analogous command for
`RectangularGramFactor.lean`, and `lake build` passed (6697 steps).
`cd lean; python verify_sources.py` passed; it verifies source/endpoint
correspondence, not Arb inequalities. A first source-check invocation from
the repository root failed because the script lives in `lean/`; this was
corrected and is not counted as a mathematical failure. The dependency
audit, inherited negative controls and pinned Linux CI are to be reported
separately for the final commit.
