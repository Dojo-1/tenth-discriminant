import TenthDiscriminant.Phase387QuadraticReality
import Mathlib.Analysis.Analytic.Uniqueness
import Mathlib.Analysis.Complex.CauchyIntegral
import Mathlib.Analysis.Calculus.Deriv.Basic

/-!
# Phase388 — Schwarz reflection for an actual quadratic Dirichlet L-function

Target: remove Phase386's explicit imaginary-part hypothesis by an
identity-theorem argument in the pinned Lean4/Mathlib environment.
No primitive field-character construction, Epstein formula, or GRH proof.
-/

open ComplexConjugate Complex Filter Topology Set

namespace TenthDiscriminant.Phase388
set_option autoImplicit false
noncomputable section
variable {N : ℕ} [NeZero N]

/-- Local backport of the double-conjugation derivative principle. -/
private theorem reflected_hasDerivAt {f : ℂ → ℂ} {x d : ℂ}
    (hf : HasDerivAt f d (conj x)) :
    HasDerivAt (fun z : ℂ => conj (f (conj z))) (conj d) x := by
  have ht : Tendsto
      (fun z : ℂ => ‖conj z - conj x‖⁻¹ *
        ‖f (conj z) - f (conj x) - (conj z - conj x) * d‖)
      (𝓝 x) (𝓝 (0 : ℝ)) := by
    simpa only [smul_eq_mul, Function.comp_apply] using
      (hasDerivAt_iff_tendsto.mp hf).comp (Complex.continuous_conj.tendsto x)
  apply hasDerivAt_iff_tendsto.mpr
  change Tendsto
      (fun z : ℂ => ‖z - x‖⁻¹ *
        ‖conj (f (conj z)) - conj (f (conj x)) - (z - x) * conj d‖)
      (𝓝 x) (𝓝 (0 : ℝ))
  convert ht using 1
  funext z
  have hnorm : ‖conj z - conj x‖ = ‖z - x‖ := by
    calc
      _ = ‖conj (z - x)‖ := by simp
      _ = ‖z - x‖ := by simp
  have hnum :
      ‖conj (f (conj z)) - conj (f (conj x)) - (z - x) * conj d‖ =
      ‖f (conj z) - f (conj x) - (conj z - conj x) * d‖ := by
    calc
      _ = ‖conj (f (conj z) - f (conj x) - (conj z - conj x) * d)‖ := by
        congr 1
        simp
      _ = _ := by simp
  rw [hnum, hnorm]

private theorem reflected_differentiable {f : ℂ → ℂ}
    (hf : Differentiable ℂ f) :
    Differentiable ℂ (fun z : ℂ => conj (f (conj z))) := by
  intro z
  exact (reflected_hasDerivAt (hf (conj z)).hasDerivAt).differentiableAt

theorem quadratic_coeff_conj (χ : DirichletCharacter ℂ N)
    (hquad : χ ^ 2 = 1) (n : ℕ) :
    conj (χ n) = χ n := by
  rcases Phase387.quadratic_coeff_trichotomy χ hquad n with h | h | h <;>
    simp [h]

/-- Conjugation symmetry in the absolutely convergent open half-plane. -/
theorem quadratic_LFunction_conj_of_one_lt
    (χ : DirichletCharacter ℂ N) (hquad : χ ^ 2 = 1)
    (z : ℂ) (hz : 1 < z.re) :
    conj (DirichletCharacter.LFunction χ (conj z)) =
      DirichletCharacter.LFunction χ z := by
  have hz' : 1 < (conj z).re := by simpa using hz
  rw [DirichletCharacter.LFunction_eq_LSeries χ hz',
      DirichletCharacter.LFunction_eq_LSeries χ hz]
  change conj (∑' n : ℕ, LSeries.term (χ ·) (conj z) n) =
    (∑' n : ℕ, LSeries.term (χ ·) z n)
  rw [Complex.conj_tsum]
  apply tsum_congr
  intro n
  rw [LSeries.term_def, LSeries.term_def]
  by_cases hn : n = 0
  · simp [hn]
  · simp only [if_neg hn]
    have hnarg : (n : ℂ).arg ≠ π := by
      rw [Complex.natCast_arg]
      positivity
    rw [map_div₀, quadratic_coeff_conj χ hquad n,
      ← Complex.conj_cpow (n : ℂ) z hnarg, Complex.conj_natCast]

/-- Identity theorem propagates reflection from the open half-plane. -/
theorem quadratic_LFunction_reflection
    (χ : DirichletCharacter ℂ N)
    (hquad : χ ^ 2 = 1) (hχ : χ ≠ 1) (z : ℂ) :
    conj (DirichletCharacter.LFunction χ (conj z)) =
      DirichletCharacter.LFunction χ z := by
  have hf : Differentiable ℂ (DirichletCharacter.LFunction χ) :=
    DirichletCharacter.differentiable_LFunction hχ
  have hg : Differentiable ℂ
      (fun w : ℂ => conj (DirichletCharacter.LFunction χ (conj w))) :=
    reflected_differentiable hf
  have hf_an : AnalyticOnNhd ℂ (DirichletCharacter.LFunction χ) univ :=
    hf.differentiableOn.analyticOnNhd isOpen_univ
  have hg_an : AnalyticOnNhd ℂ
      (fun w : ℂ => conj (DirichletCharacter.LFunction χ (conj w))) univ :=
    hg.differentiableOn.analyticOnNhd isOpen_univ
  have hmem : {w : ℂ | 1 < w.re} ∈ 𝓝 (2 : ℂ) :=
    (isOpen_lt continuous_const Complex.continuous_re).mem_nhds (by norm_num)
  have hnear :
      (fun w : ℂ => conj (DirichletCharacter.LFunction χ (conj w))) =ᶠ[𝓝 (2 : ℂ)]
        (DirichletCharacter.LFunction χ) := by
    filter_upwards [hmem] with w hw
    exact quadratic_LFunction_conj_of_one_lt χ hquad w hw
  have heq : (fun w : ℂ => conj (DirichletCharacter.LFunction χ (conj w))) =
      (DirichletCharacter.LFunction χ) :=
    hg_an.eq_of_eventuallyEq hf_an hnear
  exact congrFun heq z

/-- Previously assumed real-axis reality, now obtained from reflection. -/
theorem quadratic_LFunction_im_zero
    (χ : DirichletCharacter ℂ N)
    (hquad : χ ^ 2 = 1) (hχ : χ ≠ 1) (s : ℝ) :
    (DirichletCharacter.LFunction χ (s : ℂ)).im = 0 := by
  apply Complex.conj_eq_iff_im.mp
  simpa using quadratic_LFunction_reflection χ hquad hχ (s : ℂ)

/-- A complex Dirichlet zero with no imaginary-part hypothesis. -/
theorem quadratic_real_zero_of_sign
    (χ : DirichletCharacter ℂ N)
    (hquad : χ ^ 2 = 1) (hχ : χ ≠ 1)
    (zetaHalf dedekindHalf : ℝ)
    (hzeta : zetaHalf < 0) (hDedekind : 0 < dedekindHalf)
    (hfactor : dedekindHalf = zetaHalf * Phase386.realDirichletL χ (1 / 2))
    (hone : 0 < Phase386.realDirichletL χ 1) :
    ∃ β : ℝ, (1 / 2 : ℝ) < β ∧ β < 1 ∧
      DirichletCharacter.LFunction χ (β : ℂ) = 0 := by
  apply Phase386.actual_dirichlet_real_zero_of_sign
    χ hχ zetaHalf dedekindHalf hzeta hDedekind hfactor hone
  intro s _ _
  exact quadratic_LFunction_im_zero χ hquad hχ s

end
end TenthDiscriminant.Phase388

#check TenthDiscriminant.Phase388.quadratic_LFunction_reflection
#check TenthDiscriminant.Phase388.quadratic_LFunction_im_zero
#check TenthDiscriminant.Phase388.quadratic_real_zero_of_sign
#print axioms TenthDiscriminant.Phase388.quadratic_real_zero_of_sign
