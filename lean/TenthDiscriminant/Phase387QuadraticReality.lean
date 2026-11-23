import TenthDiscriminant.Phase386ComplexDirichlet
import Mathlib.NumberTheory.LSeries.Nonvanishing

/-!
Phase387: an independently testable coefficient-reality lemma and
absolute-convergence-half-plane check for genuine complex Dirichlet L-functions.

The continuation from s>1 to 1/2<s<1 is NOT proved here.
-/
namespace TenthDiscriminant.Phase387
set_option autoImplicit false
noncomputable section
variable {N : ℕ} [NeZero N]

/-- Quadratic characters have only the three real coefficient values. -/
theorem quadratic_coeff_trichotomy
    (χ : DirichletCharacter ℂ N) (hquad : χ ^ 2 = 1) (n : ℕ) :
    χ n = 0 ∨ χ n = 1 ∨ χ n = -1 := by
  exact (MulChar.isQuadratic_iff_sq_eq_one.mpr hquad) (n : ZMod N)

/-- No separate reality hypothesis is needed at the coefficient level. -/
theorem quadratic_coeff_im_zero
    (χ : DirichletCharacter ℂ N) (hquad : χ ^ 2 = 1) (n : ℕ) :
    (χ n).im = 0 := by
  rcases quadratic_coeff_trichotomy χ hquad n with h | h | h <;>
    simp [h]

/-- Each absolutely-convergent term is real for a real argument. -/
theorem quadratic_lseries_term_im_zero
    (χ : DirichletCharacter ℂ N) (hquad : χ ^ 2 = 1)
    (s : ℝ) (n : ℕ) :
    (LSeries.term (χ ·) (s : ℂ) n).im = 0 := by
  rw [LSeries.term_def]
  by_cases hn : n = 0
  · simp [hn]
  · rw [if_neg hn]
    have hpow : (n : ℂ) ^ (s : ℂ) = (((n : ℝ) ^ s : ℝ) : ℂ) := by
      simpa only [Complex.ofReal_natCast] using
        (Complex.ofReal_cpow (Nat.cast_nonneg n) s).symm
    rcases quadratic_coeff_trichotomy χ hquad n with h | h | h <;>
      simp [h, hpow]

/-- The actual continued Dirichlet L-function is real on the half-plane
where its defining Dirichlet series converges absolutely. -/
theorem quadratic_LFunction_im_zero_of_one_lt
    (χ : DirichletCharacter ℂ N) (hquad : χ ^ 2 = 1)
    (s : ℝ) (hs : 1 < s) :
    (DirichletCharacter.LFunction χ (s : ℂ)).im = 0 := by
  have hsC : 1 < Complex.re (s : ℂ) := by simpa using hs
  have hsum : LSeriesSummable (χ ·) (s : ℂ) :=
    DirichletCharacter.LSeriesSummable_of_one_lt_re χ hsC
  rw [DirichletCharacter.LFunction_eq_LSeries χ hsC]
  change (∑' n : ℕ, LSeries.term (χ ·) (s : ℂ) n).im = 0
  rw [Complex.im_tsum hsum]
  simp [quadratic_lseries_term_im_zero χ hquad]

/-- The pinned Mathlib proves nonvanishing at s=1 for nontrivial
characters; positivity is a separate theorem target. -/
theorem nontrivial_LFunction_one_ne_zero
    (χ : DirichletCharacter ℂ N) (hχ : χ ≠ 1) :
    DirichletCharacter.LFunction χ 1 ≠ 0 :=
  DirichletCharacter.LFunction_apply_one_ne_zero hχ

end
end TenthDiscriminant.Phase387

#check TenthDiscriminant.Phase387.quadratic_coeff_trichotomy
#check TenthDiscriminant.Phase387.quadratic_LFunction_im_zero_of_one_lt
#print axioms TenthDiscriminant.Phase387.quadratic_LFunction_im_zero_of_one_lt
