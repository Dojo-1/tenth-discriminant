import TenthDiscriminant.Phase385CentralSign
import Mathlib.NumberTheory.LSeries.DirichletContinuation

/-! Phase386 — actual complex Dirichlet L-function bridge.

Complex differentiability of a nontrivial character's L-function proves
continuity of its real part. Converting a real-part zero to a complex zero
requires a separate explicit imaginary-part hypothesis. The field-character
map, Dedekind factorization and the analytic sign are not proved here. -/
namespace TenthDiscriminant.Phase386
set_option autoImplicit false
noncomputable section
variable {N : ℕ} [NeZero N]

def realDirichletL (χ : DirichletCharacter ℂ N) (s : ℝ) : ℝ :=
  (DirichletCharacter.LFunction χ (s : ℂ)).re

theorem realDirichletL_continuous
    (χ : DirichletCharacter ℂ N) (hχ : χ ≠ 1) :
    Continuous (realDirichletL χ) := by
  have hc : Continuous (DirichletCharacter.LFunction χ) :=
    (DirichletCharacter.differentiable_LFunction hχ).continuous
  exact Complex.continuous_re.comp (hc.comp Complex.continuous_ofReal)

theorem realPart_zero_and_imag_zero
    (χ : DirichletCharacter ℂ N) (s : ℝ)
    (hre : realDirichletL χ s = 0)
    (him : (DirichletCharacter.LFunction χ (s : ℂ)).im = 0) :
    DirichletCharacter.LFunction χ (s : ℂ) = 0 := by
  apply Complex.ext
  · simpa only [realDirichletL, Complex.zero_re] using hre
  · simpa only [Complex.zero_im] using him

theorem actual_dirichlet_real_zero_of_sign
    (χ : DirichletCharacter ℂ N) (hχ : χ ≠ 1)
    (zetaHalf dedekindHalf : ℝ)
    (hzeta : zetaHalf < 0) (hDedekind : 0 < dedekindHalf)
    (hfactor : dedekindHalf = zetaHalf * realDirichletL χ (1 / 2))
    (hone : 0 < realDirichletL χ 1)
    (hImagZero : ∀ s : ℝ, (1 / 2 : ℝ) < s → s < 1 →
        (DirichletCharacter.LFunction χ (s : ℂ)).im = 0) :
    ∃ β : ℝ, (1 / 2 : ℝ) < β ∧ β < 1 ∧
      DirichletCharacter.LFunction χ (β : ℂ) = 0 := by
  obtain ⟨β, hleft, hright, hzero⟩ :=
    Phase385.positive_dedekind_half_forces_real_zero
      (realDirichletL χ) zetaHalf dedekindHalf
      hzeta hDedekind hfactor hone
      (realDirichletL_continuous χ hχ).continuousOn
  exact ⟨β, hleft, hright,
    realPart_zero_and_imag_zero χ β hzero (hImagZero β hleft hright)⟩

theorem actual_dirichlet_zero_free_bound
    (d : ℕ)
    (χ : DirichletCharacter ℂ N) (hχ : χ ≠ 1)
    (zetaHalf dedekindHalf : ℝ)
    (hzeta : zetaHalf < 0)
    (hfactor : dedekindHalf = zetaHalf * realDirichletL χ (1 / 2))
    (hone : 0 < realDirichletL χ 1)
    (hImagZero : ∀ s : ℝ, (1 / 2 : ℝ) < s → s < 1 →
        (DirichletCharacter.LFunction χ (s : ℂ)).im = 0)
    (hlarge_sign : 200 ≤ d → 0 < dedekindHalf)
    (hZF : ∀ β : ℝ, (1 / 2 : ℝ) < β → β < 1 →
        DirichletCharacter.LFunction χ (β : ℂ) ≠ 0) :
    d ≤ 199 := by
  by_contra hnot
  have hd : 200 ≤ d := by omega
  obtain ⟨β, hleft, hright, hzero⟩ :=
    actual_dirichlet_real_zero_of_sign
      χ hχ zetaHalf dedekindHalf hzeta (hlarge_sign hd)
      hfactor hone hImagZero
  exact (hZF β hleft hright) hzero

theorem real_part_only_is_insufficient :
    (Complex.I).re = 0 ∧ Complex.I ≠ 0 := by
  simp

end
end TenthDiscriminant.Phase386

#check TenthDiscriminant.Phase386.realDirichletL_continuous
#check TenthDiscriminant.Phase386.actual_dirichlet_real_zero_of_sign
#check TenthDiscriminant.Phase386.actual_dirichlet_zero_free_bound
#print axioms TenthDiscriminant.Phase386.actual_dirichlet_real_zero_of_sign
#print axioms TenthDiscriminant.Phase386.actual_dirichlet_zero_free_bound
