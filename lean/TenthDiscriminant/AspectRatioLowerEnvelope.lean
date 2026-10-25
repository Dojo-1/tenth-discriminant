import TenthDiscriminant.UniformLowerEnvelope

/-! The same prime-mass budget with an explicit aspect-ratio cost.
This is a lower bound, not a new chosen-radius or class-number cutoff. -/
namespace TenthDiscriminant.FirstCertificate
set_option autoImplicit false
noncomputable section

/-- Thinner rectangles pay linearly in `K` for the quadratic prime loss. -/
theorem rawPrimeMassLower_aspect_ratio (R S : Nat) (K : Real)
    (hR : 100000000 ≤ R) (hS : 500000 ≤ S) (_hK : 0 ≤ K)
    (hRS : (R : Real) ≤ K*S) (hlog : 2 ≤ Real.log R) :
    (999997/1000000 : Real)*Real.log R-(3294/1000+(56/1250)*K) ≤
      rawPrimeMassLower R S FirstEnderInterval.tailBudget/comparisonScale R S := by
  have hr : (100000000 : Real) ≤ R := by exact_mod_cast hR
  have hs : (500000 : Real) ≤ S := by exact_mod_cast hS
  have hr0 : (0 : Real) ≤ R := Nat.cast_nonneg _
  have hs0 : (0 : Real) ≤ S := Nat.cast_nonneg _
  have ha : (999999/1000000 : Real)*S ≤ (S : Real)-1/2 := by linarith
  have hahi : (S : Real)-1/2 ≤ S := by linarith
  have ha0 : 0 ≤ (S : Real)-1/2 := by linarith
  have hf := factorialLower_uniform R (by omega) hlog
  have hbase : 0 ≤ (R : Real)^2/2*
      ((999999/1000000 : Real)^2*Real.log R-1500004/1000000) := by
    apply mul_nonneg (by positivity)
    linarith
  have hfa := mul_le_mul_of_nonneg_left hf (show 0 ≤ 2*((S : Real)-1/2) by linarith)
  have hscale := mul_le_mul_of_nonneg_right ha hbase
  have hmain : comparisonScale R S*
      ((999997/1000000 : Real)*Real.log R-150001/100000) ≤
      2*((S : Real)-1/2)*factorialLower R := by
    have hsl := mul_nonneg (show 0 ≤ Real.log R by linarith)
      (show 0 ≤ (R : Real)^2*S by positivity)
    unfold comparisonScale
    nlinarith only [hfa, hscale, hsl]
  have hv0 := triangularMass_nonneg R
  have hv : triangularMass R ≤ (R : Real)^2/2 := by
    unfold triangularMass
    nlinarith
  have hw : squareMass R ≤ (R : Real)^3/3 := by
    unfold squareMass
    nlinarith [sq_nonneg ((R : Real)-1)]
  obtain ⟨hk0, hk, he0, he, hc0, hc⟩ := fixed_constants_coarse
  have hvprod := mul_le_mul hahi hv hv0 hs0
  have hloss := mul_le_mul hvprod hk hk0 (by positivity : 0 ≤ (S : Real)*((R : Real)^2/2))
  have hlinear := mul_le_mul_of_nonneg_left he
    (by positivity : 0 ≤ 2*((S : Real)-1/2)*R)
  have hlin : 2*((S : Real)-1/2)*R*errorConstantUpper ≤
      comparisonScale R S/1000 := by
    have hsr := mul_nonneg hs0 hr0
    have hh := mul_le_mul_of_nonneg_left hahi (by positivity : (0 : Real) ≤ 19800*R)
    have hrr := mul_le_mul_of_nonneg_left (show (19800 : Real) ≤ (R : Real)/1000 by linarith) hsr
    unfold comparisonScale
    nlinarith only [hlinear, hh, hrr]
  have hwprod := mul_le_mul hw hc hc0 (by positivity : (0 : Real) ≤ (R : Real)^3/3)
  have hdim := mul_le_mul_of_nonneg_right hRS (sq_nonneg (R : Real))
  have hquad : squareMass R*(squareConstantUpper+FirstEnderInterval.tailBudget) ≤
      comparisonScale R S*((56/1250)*K) := by
    unfold comparisonScale
    nlinarith only [hwprod, hdim]
  apply (le_div_iff₀ (comparisonScale_pos R S (by omega) (by omega))).2
  unfold rawPrimeMassLower
  unfold comparisonScale at hmain hlin hquad ⊢
  nlinarith only [hmain, hloss, hlin, hquad,
    mul_nonneg (sq_nonneg (R : Real)) hs0]

theorem aspect_ratio_21_control (R S : Nat)
    (hR : 100000000 ≤ R) (hS : 500000 ≤ S) (hRS : R ≤ 21*S)
    (hlog : 2 ≤ Real.log R) :
    (999997/1000000 : Real)*Real.log R-4235/1000 ≤
      rawPrimeMassLower R S FirstEnderInterval.tailBudget/comparisonScale R S := by
  have hr : (R : Real) ≤ 21*S := by exact_mod_cast hRS
  have h := rawPrimeMassLower_aspect_ratio R S 21 hR hS (by norm_num) hr hlog
  linarith

theorem aspect_ratio_25_point_1_control (R S : Nat)
    (hR : 100000000 ≤ R) (hS : 500000 ≤ S)
    (hRS : (R : Real) ≤ (251/10)*S) (hlog : 2 ≤ Real.log R) :
    (999997/1000000 : Real)*Real.log R-4419/1000 ≤
      rawPrimeMassLower R S FirstEnderInterval.tailBudget/comparisonScale R S := by
  have h := rawPrimeMassLower_aspect_ratio R S (251/10) hR hS (by norm_num) hRS hlog
  linarith

theorem candidate_aspect_affine_separation (u : Real) (hu : 253/10 ≤ u) :
    (4/5 : Real)*u-813/1000 < (999997/1000000 : Real)*u-5820/1000 := by
  linarith

theorem candidate_aspect_log25_rejected :
    ¬ (4/5 : Real)*25-813/1000 < (999997/1000000 : Real)*25-5820/1000 := by
  norm_num

theorem aspect_ratio_floor25_equality_rejected :
    ¬ 100000024 ≤ 25*(100000024/25 : Nat) := by norm_num

end
end TenthDiscriminant.FirstCertificate
