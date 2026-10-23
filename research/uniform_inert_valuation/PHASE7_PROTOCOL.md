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
