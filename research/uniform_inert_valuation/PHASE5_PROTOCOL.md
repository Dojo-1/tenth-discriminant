# Phase 5 preregistration: the sample-independent basis matrix

Date: 2026-10-23. Base: merged PR #23, `origin/main` at `d0d421f`.
This protocol precedes new Lean proof edits. The candidate cutoff and
classification status do not change by proving a basis determinant.

## Fixed bounded target

For `R,S,p : Nat` with `p>0`, put `k_i = rectangularBasisExponent R S p i`
at the existing row-major index `i : Fin (R*S)`. Construct one **integer
matrix independent of samples, D and derivative order** whose row `i`
contains the binomial coefficients of

`Z^(r-p*k_i) W^s (Z^p-W)^k_i`

against the canonical rectangular monomials `Z^r W^s`. Prove it is
lower triangular with diagonal entries `1`, hence determinant `1`.
The proof must establish `p*t≤r` and `s+t<S` for each active term;
out-of-rectangle terms or a mere numerical determinant check fail the
target. Empty rectangles must be handled, and the `4×2,p=3` row-six
pilot must give `Z³-W` (coefficient `1` in column six and `-1` in
column one).

If practical, also identify the matrix action on the existing integer
derivative rows. That is a **separate stretch target**: a theorem about
an abstract polynomial family or a replacement Gram cannot be reported
as the actual row identification. The later two-sided factorization
and uniform inertness deduction require this stretch target plus the
already checked jet-power and Frobenius interfaces.

## Falsifiers and verification

- Check row-major direction: every off-diagonal active term must lie
  strictly **below** the source row when `p>0`.
- Check the highest `s` row has `k=0`, and do not erase contributions
  when distinct integer samples collide after reduction.
- A diagonal-only identity matrix would pass the determinant test but
  fail the binomial coefficient and row-six pilot; retain both controls.
- Record any failed Lean attempt or false stronger statement.

Run targeted Lean, source correspondence, full `lake build`, pinned
dependency audit and inherited negative controls. Keep README/STATUS/
FORMALIZATION and the human guide aligned with the exact theorem. Do
not merge automatically or post a bound claim to Tao.

## Execution record

Protocol-only commit `75ee2c0` preceded Lean edits. The first targeted
compilation exposed an invalid simplification of a `Fin` bound and an
unproved quotient–remainder identity; both were corrected by naming
the existing bounds and `Nat.div_add_mod'`. The next compilation
exposed a polymorphic `OrderDual` type and a `t<k+1` versus `t≤k`
elaboration gap; both were repaired. A whole-row pilot first failed
because `decide` was asked to close a free index; quantifying the
finite index repaired it. These are proof-script failures, not
counterexamples to the basis construction.

Lean now checks the term bounds, that each active target is an actual
canonical column, strict earlier-column property,
lower-triangularity, diagonal one, determinant one, and whole
`4×2,p=3` pilot rows. It does **not** prove the stretch target:
polynomial expansion into the original integer derivative rows,
or the consequent actual-Gram factorization. Targeted Lean, source
correspondence and the final 6694-step full build passed. Pinned CI
on the final commit remains pending.
