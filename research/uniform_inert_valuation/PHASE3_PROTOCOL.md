# Phase 3 preregistration: exact rectangular exponent bridge

Date: 2026-10-23. Base: merged PR #22, `origin/main` at `7bc3ec8`.
This protocol precedes Phase 3 proof edits. The user requests the
closest feasible checked cutoff/classification progress within one or
two turns and an honest Tao-facing account; a candidate cutoff must
not be promoted by an abstract algebra lemma alone.

## Fixed theorem target

Define the basis exponent at row-major index `i : Fin (R*S)` by

`k(i) = min ((i.val / S) / p) (S-1-(i.val % S))`.

Prove in Lean that `sum_i k(i) = valuationWeight R S p`, where the
existing Ender weight is `sum_(r<R,t<S) min (r/p) t`. Handle `R=0`,
`S=0`, and `p=0` according to Lean's natural-number conventions; the
mathematical inert-prime application will later require `p` odd prime.

Then specialize the existing unimodular two-sided determinant theorem
to `integerRectangularTraceGram Q D J R S`: if an integral matrix `U`
has determinant `1` and a witness `K` gives exactly
`U*G*U.transpose = diag(p^k)*K*diag(p^k)`, conclude
`p^(2*valuationWeight R S p) | det G`.

The hypothesis is a **missing construction**, not an inert-prime
theorem. This cycle must not assert that inertness supplies `U,K`, nor
that the analytic or class-number chains are closed. A purely
conditional theorem is useful only if the documentation names its
unproved hypothesis conspicuously.

## Falsifiers and verification

Check the row-major indexing, especially `S=0` and the highest `s`;
the transformed polynomial must not leave the rectangle. Confirm
the reflected finite sum exactly matches Ender's original weight,
not a shifted or stronger exponent. Keep the `D=2,p=3` noninert
negative control from Phase 2. Run targeted Lean, full `lake build`,
source correspondence, and pinned CI with dependency and negative
controls. Record all failures. No automatic merge or Tao submission.
