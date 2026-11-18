import TenthDiscriminant.E16Integrated300
import TenthDiscriminant.LogEnclosure

/-!
# E17: Scalar lower versus a simple upper envelope, D>=300^4

The source arithmetic expression is unchanged. A field contradiction
requires the separate, EXPLICIT analytic upper envelope premise;
no change to ordinary Z jets, integer Gram or prime factors.
-/

namespace TenthDiscriminant.E17
open TenthDiscriminant
open TenthDiscriminant.FirstCertificate
set_option autoImplicit false
noncomputable section

theorem log_300_rational_enclosure :
    (57/10 : Real) ≤ Real.log 300 ∧
      Real.log 300 ≤ (571/100 : Real) := by
  have hc :
      checkPositiveLogBounds 5 300 8
        (57/10) (571/100) = true := by
    norm_num [checkPositiveLogBounds, binaryLogLowerRat,
      binaryLogUpperRat, oddLogPrefixRat, oddLogRemainderRat,
      Finset.sum_range_succ]
  have h := checkPositiveLogBounds_sound 5 300 8
    (57/10) (571/100) hc
  norm_num at h
  rcases h with ⟨hlo,hhi⟩
  constructor
  · linarith
  · linarith

theorem log_floor_from_300_fourth_power (D : Nat)
    (hD : (300 : Nat)^4 ≤ D) :
    (114/5 : Real) ≤ Real.log (D : Real) := by
  have hsmall : (0 : Real) <
      (((300 : Nat)^4 : Nat) : Real) := by norm_num
  have hDreal : (((300 : Nat)^4 : Nat) : Real) ≤ (D : Real) := by
    exact_mod_cast hD
  have hm := Real.log_le_log hsmall hDreal
  rw [Nat.cast_pow, Real.log_pow] at hm
  have hlo := log_300_rational_enclosure.1
  linarith

/-- Exact lower expression: all three explicit correction terms are
nonnegative for D>=300^4, with floors kept intact. -/
theorem euclid_lower_ge_affine_300 (D : Nat)
    (hD : (300 : Nat)^4 ≤ D) :
    (999997/1000000 : Real)*Real.log D-5546025/1000000 ≤
      E16.euclidArithmeticLower D := by
  have hDnat : 8100000000 ≤ D := by
    have he : (300 : Nat)^4 = 8100000000 := by norm_num
    simpa only [he] using hD
  have hRnat : 2025000000 ≤ Tuned.R D := by
    unfold Tuned.R envelopeR
    omega
  have hDr : (8100000000 : Real) ≤ (D : Real) := by
    exact_mod_cast hDnat
  have hRr : (2025000000 : Real) ≤ (Tuned.R D : Real) := by
    exact_mod_cast hRnat
  have hRpos : (0 : Real) < Tuned.R D := by linarith
  have hDden : (0 : Real) < 625000*(D : Real) := by positivity
  have hodd :
      (16895455 : Real)/(625000*(D : Real)) ≤ 4659/625000 := by
    apply (div_le_iff₀ hDden).2
    nlinarith only [hDr]
  have hbin :
      (2 : Real)/(Tuned.R D : Real) ≤ 6931/1000000 := by
    apply (div_le_iff₀ hRpos).2
    nlinarith only [hRr]
  have hten :
      (40 : Real)/(Tuned.R D : Real) ≤ 873747/250000000 := by
    apply (div_le_iff₀ hRpos).2
    nlinarith only [hRr]
  have hlog2 := TenthDiscriminant.log_two_rational_control.1
  unfold E16.euclidArithmeticLower
  linarith only [hodd,hbin,hten,hlog2]

theorem euclid_lower_gt_simple_upper_300 (D : Nat)
    (hD : (300 : Nat)^4 ≤ D) :
    (4/5 : Real)*Real.log D - 103/100 <
      E16.euclidArithmeticLower D := by
  have hlo := euclid_lower_ge_affine_300 D hD
  have hlog := log_floor_from_300_fourth_power D hD
  linarith only [hlo,hlog]

theorem scalar_separation_of_analytic_upper_guard (D : Nat)
    (hD : (300 : Nat)^4 ≤ D)
    (hupper : E16.euclidAnalyticUpper D ≤
      (4/5 : Real)*Real.log D - 103/100) :
    E16.euclidAnalyticUpper D < E16.euclidArithmeticLower D :=
  lt_of_le_of_lt hupper (euclid_lower_gt_simple_upper_300 D hD)

/-- This theorem is conditional: the analytic upper guard must be
proved uniformly before any field-discriminant cutoff is asserted. -/
theorem no_one_of_analytic_upper_guard (D : Nat)
    (hD : (300 : Nat)^4 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hupper : E16.euclidAnalyticUpper D ≤
      (4/5 : Real)*Real.log D - 103/100) :
    NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) ≠ 1 := by
  intro hc
  exact E16.contradiction_of_scalar_separation D hD hsq hc
    (scalar_separation_of_analytic_upper_guard D hD hupper)

end
end TenthDiscriminant.E17

#print axioms TenthDiscriminant.E17.log_floor_from_300_fourth_power
#print axioms TenthDiscriminant.E17.euclid_lower_ge_affine_300
#print axioms TenthDiscriminant.E17.euclid_lower_gt_simple_upper_300
#print axioms TenthDiscriminant.E17.no_one_of_analytic_upper_guard
