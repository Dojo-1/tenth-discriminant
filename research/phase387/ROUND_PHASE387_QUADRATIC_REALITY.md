# Phase387 — Quadratic coefficient reality and the convergence barrier

**23 November 2026 | AI-assisted proof-engineering draft.**

## Mathematical target

For any complex Dirichlet character χ with χ²=1 and modulus N>0, show each coefficient χ(n) belongs to {-1,0,1}. Then show that the actual analytically continued Dirichlet function satisfies Im L(s,χ)=0 for real s>1, where Mathlib's LSeries is absolutely convergent and equal to LFunction.

Source targets in `lean/TenthDiscriminant/Phase387QuadraticReality.lean`:

- `quadratic_coeff_trichotomy`: applies pinned `MulChar.isQuadratic_iff_sq_eq_one`.
- `quadratic_coeff_im_zero`: finite coefficient reality, without an external hypothesis.
- `quadratic_lseries_term_im_zero`: denominator is a positive-real power.
- `quadratic_LFunction_im_zero_of_one_lt`: transport via pinned `DirichletCharacter.LFunction_eq_LSeries`, `DirichletCharacter.LSeriesSummable_of_one_lt_re` and `Complex.im_tsum`.
- `nontrivial_LFunction_one_ne_zero`: explicit reuse of pinned `DirichletCharacter.LFunction_apply_one_ne_zero` (not positivity).

The **convergence barrier** is genuine: at 1/2<s<1 the naive LSeries in this pinned Mathlib revision is defined through absolute convergence and cannot be substituted for the continued LFunction. Hence Phase387 does not yet discharge Phase386's `hImagZero` on that interval. It establishes a nonempty open half-plane on which the conjugation identity holds. The next target is a reflection/identity-theorem bridge for the analytically continued function.

**Evidence policy:** treat this Phase387 file as unverified H until focused Lean compilation succeeds. Do not imply that χ²=1 establishes a field-specific primitive quadratic χ_D, or that L(1)>0 follows from nonvanishing alone. The completed Phase381 finite and Phase385–386 conditional bridges remain independent. Original trace-Gram issue #50 remains open.
