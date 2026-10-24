import TenthDiscriminant.NormalizedComparison

/-! A dimension-uniform lower envelope. The D-dependent upper envelope and
chosen-radius geometry are separate obligations, not premises hidden here. -/
namespace TenthDiscriminant.FirstCertificate
set_option autoImplicit false
noncomputable section

theorem log_predecessor_lower (r : Real) (hr : 1000000 ≤ r) :
    Real.log r - 2/1000000 ≤ Real.log (r-1) := by
  have hp : 0 < r-1 := by linarith
  have hrp : 0 < r := by linarith
  have hratio : 0 < (r-1)/r := div_pos hp hrp
  have h := Real.one_sub_inv_le_log_of_pos hratio
  rw [Real.log_div hp.ne' hrp.ne'] at h
  have hi : ((r-1)/r)⁻¹ = r/(r-1) := by field_simp
  rw [hi] at h
  have he : r/(r-1) ≤ 1+2/1000000 := by
    apply (div_le_iff₀ hp).2
    linarith
  linarith

theorem factorialLower_uniform (R : Nat) (hR : 1000000 ≤ R)
    (hlog : 2 ≤ Real.log R) :
    (R : Real)^2/2*((999999/1000000 : Real)^2*Real.log R-1500004/1000000) ≤
      factorialLower R := by
  have hr : (1000000 : Real) ≤ R := by exact_mod_cast hR
  have hlogp := log_predecessor_lower R hr
  have hpred : (999999/1000000 : Real)*R ≤ (R : Real)-1 := by linarith
  have hsq : ((999999/1000000 : Real)*R)^2 ≤ ((R : Real)-1)^2 := by
    apply pow_le_pow_left₀ (by positivity) hpred
  have hp : 0 ≤ Real.log R-2/1000000 := by linarith
  have hm := mul_le_mul_of_nonneg_right hsq hp
  have hl := mul_le_mul_of_nonneg_left hlogp (sq_nonneg ((R : Real)-1))
  have hnorm : ((R : Real)-1)^2 ≤ (R : Real)^2 := by nlinarith
  unfold factorialLower
  rw [Nat.cast_sub (by omega : 1 ≤ R)]
  simp only [Nat.cast_one]
  nlinarith [sq_nonneg (R : Real)]

/-- Coarse rounding is in the safe direction, with an explicit positive tail. -/
theorem fixed_constants_coarse :
    0 ≤ factorialConstantUpper+FirstEnderInterval.tailBudget-linearConstantLower ∧
    factorialConstantUpper+FirstEnderInterval.tailBudget-linearConstantLower ≤ 17921/10000 ∧
    0 ≤ errorConstantUpper ∧ errorConstantUpper ≤ 9900 ∧
    0 ≤ squareConstantUpper+FirstEnderInterval.tailBudget ∧
    squareConstantUpper+FirstEnderInterval.tailBudget ≤ 168/1250 := by
  norm_num [factorialConstantUpper, linearConstantLower, squareConstantUpper,
    errorConstantUpper, FirstEnderInterval.tailBudget]

theorem rawPrimeMassLower_uniform (R S : Nat) (hR : 100000000 ≤ R)
    (hS : 500000 ≤ S) (hRS : R ≤ 21*S) (hlog : 2 ≤ Real.log R) :
    comparisonScale R S*((999997/1000000 : Real)*Real.log R-4235/1000) ≤
      rawPrimeMassLower R S FirstEnderInterval.tailBudget := by
  have hr : (100000000 : Real) ≤ R := by exact_mod_cast hR
  have hs : (500000 : Real) ≤ S := by exact_mod_cast hS
  have hrs : (R : Real) ≤ 21*S := by exact_mod_cast hRS
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
  have hw0 := squareMass_nonneg R
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
  have hdim := mul_le_mul_of_nonneg_right hrs (sq_nonneg (R : Real))
  have hquad : squareMass R*(squareConstantUpper+FirstEnderInterval.tailBudget) ≤
      comparisonScale R S*(1176/1250) := by
    unfold comparisonScale
    nlinarith only [hwprod, hdim]
  unfold rawPrimeMassLower
  unfold comparisonScale at hmain hlin hquad ⊢
  nlinarith only [hmain, hloss, hlin, hquad,
    mul_nonneg (sq_nonneg (R : Real)) hs0]

theorem rawPrimeMassLower_uniform_normalized (R S : Nat) (hR : 100000000 ≤ R)
    (hS : 500000 ≤ S) (hRS : R ≤ 21*S) (hlog : 2 ≤ Real.log R) :
    (999997/1000000 : Real)*Real.log R-4235/1000 ≤
      rawPrimeMassLower R S FirstEnderInterval.tailBudget/comparisonScale R S := by
  apply (le_div_iff₀ (comparisonScale_pos R S (by omega) (by omega))).2
  simpa only [mul_comm] using rawPrimeMassLower_uniform R S hR hS hRS hlog

end
end TenthDiscriminant.FirstCertificate
