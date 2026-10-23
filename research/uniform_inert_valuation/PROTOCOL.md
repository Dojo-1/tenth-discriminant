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

## Execution record (append-only)

- The exact polynomial-basis argument is written in `PROOF.md`; its
  general concrete instantiation remains **paper-only**. Lean checks
  `pow_dvd_det_of_unimodular_gram_factor`, the conditional matrix step.
- Bounded arithmetic controls: `(R,S,p)=(4,2,3),(11,4,3),(12,3,5)`
  gave matching exponent sums `1,36,16` and all binomial terms stayed
  in their rectangles. `D=19,p=3` passed the local cube congruence on
  all 49 pairs with `-3<=x,y<=3`; the noninert `D=2,p=3` sample
  `(x,y)=(0,1)` gave second-coordinate difference `-1`, not a multiple
  of `3`. These finite checks do not establish the theorem.
- `lake env lean TenthDiscriminant/GramDivisibility.lean` passed.
  `python verify_sources.py` passed source/250-interval endpoint
  correspondence, not Arb inequality truth. `lake build` completed
  successfully (6690 steps; inherited linter warnings).
- The preregistration-only commit `09b6455` was pushed before proof
  edits and opened as draft PR #21. Its pinned CI was still running at
  the time of this entry. Final-head CI is a separate obligation.
