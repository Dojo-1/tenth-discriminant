import Mathlib

/-!
# Analytic closure schema
This proves the order-theoretic step, not the instantiated Ender error bounds.
The antitonicity and endpoint hypotheses remain explicit parameters.
-/
namespace TenthDiscriminant

theorem positive_envelope (a b u₀ : ℝ) (E : ℝ → ℝ) (ha : 0 ≤ a)
    (hE : AntitoneOn E (Set.Ici u₀)) (hstart : 0 < a*u₀-b-E u₀) :
    ∀ u, u₀ ≤ u → 0 < a*u-b-E u := by
  intro u hu
  have he := hE (by simp) (by simpa using hu) hu
  have hm := mul_le_mul_of_nonneg_left hu ha
  linarith

theorem ender_slope : (1 : ℝ) - (3/4 + 5/(4*80)) = 15/64 := by norm_num

theorem ender_slope_positive : (0 : ℝ) < 15/64 := by norm_num

end TenthDiscriminant
