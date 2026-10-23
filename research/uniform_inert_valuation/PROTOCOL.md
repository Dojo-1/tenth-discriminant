# Preregistration: uniform inert-prime valuation bridge

Date: 2026-10-23. Base: `8ab2be0`; accounting branch commit `9b976cb`.
This protocol precedes proof edits. It changes no numerical parameters or saved certificates.

## Fixed target and expected mechanism

For the existing integer rectangular trace-Gram matrix with rows
`Z^r W^s` (`0 <= r < R`, `0 <= s < S`), finite selected lattice sample
set `Q`, and ordinary `Z`-derivative orders `0 <= j < J`, prove for an
odd inert prime `p` that

`p^(2*F(p)) | det G`, where
`F(p) = sum_(r<R,s<S) min(floor(r/p), S-1-s)`.

The proposed basis row is
`B_(r,s) = Z^(r-p*k) W^s (Z^p-W)^k`,
`k = min(floor(r/p), S-1-s)`. Its expansion is `Z^r W^s` plus
terms `Z^(r-p*i) W^(s+i)` with smaller `r` and still `s+i<S`.
Therefore the transition is integral unitriangular, with determinant 1.
If `Z^p-W` and **every ordinary Z-derivative** evaluate to multiples
of `p` at `(z,bar z)`, then the transformed row jets have a factor
`p^k`; bilinearity gives a two-sided integral Gram factor. The exponent
sum agrees with Ender's `F(p)` after `t=S-1-s`.

The local arithmetic condition must be proved, not assumed from the
word "inert": in the selected order, reduction mod `p` must satisfy
`z^p = bar z` for every sample. For odd `p`, irreducibility of
`X^2+D` modulo `p` is the intended sufficient condition. Keep distinct
the conditional algebraic theorem and its field-theoretic hypothesis.

## Bounded execution and falsifiers

This cycle may produce (1) an explicit human-checkable proof, (2) a
small Lean theorem for the uniform *abstract matrix* factor if feasible,
and (3) tests of the basis/exponent for small rectangles and the
existing `D=19,p=3` positive/noninert controls. Full class-number or
analytic formalization is outside this cycle. A paper proof must be
labelled paper, not Lean-checked.

Falsify or downgrade the claim if a basis term leaves the rectangle,
the change-of-basis determinant is not a unit, a `Z`-derivative loses
one of the `p` factors, a shared Gram pivot supplies only one `p`, or
the local Frobenius congruence fails for an allegedly inert example.
Use `D=2,p=3` as a noninert negative control. Do not generalize from
the fixed `D=19,p=3` pilot alone.

Verification target: pinned `python verify_sources.py`, `lake build`,
`python audit.py`, and `python negative_controls.py` through GitHub CI.
Report exact checked commit, failures, and whether the valuation is
paper-only, Lean-conditional, or fully Lean-proved. No automatic merge
and no full-classification claim.
