import TenthDiscriminant.E17ScalarLower300
import TenthDiscriminant.E17UpperAlgebra
import TenthDiscriminant.E20EuclidCountLog300

/-!
# E21: Uniform scalar comparison for the SAME source original integer Gram

The E17 upper guard hypotheses are discharged by E18-20 *universal* Lean
lemmas for the actual Euclid ellipse Q and radius. E17 arithmetic lower
is strict at D >= 300^4. No changed rows, Hasse jets, primes, observation
support or Gram occurs in the comparison.

This proves the odd quadratic-chart exclusion inside the Phase349 research
source closure, not yet an independently audited public-main field theorem.
-/
namespace TenthDiscriminant.E21
open TenthDiscriminant
open TenthDiscriminant.FirstCertificate
set_option autoImplicit false
noncomputable section

/-- All eight actual-source E17 guards are discharged without assuming
squarefreeness, a class number, or any sampled endpoint. -/
theorem euclid_analytic_upper_le_affine_300 (D : Nat)
    (hD : (300 : Nat)^4 ≤ D) :
    E16.euclidAnalyticUpper D ≤
      (4/5 : Real)*Real.log (D : Real)-103/100 := by
  have hd := Tuned.dimensions_300 D hD
  have hS : 1 ≤ Tuned.S D := by omega
  have hρ : 0 < Tuned.euclidRadius D := by
    have hh := (Tuned.euclid_radius_guards_252 D
      (by omega : (252 : Nat)^4 ≤ D)).1
    omega
  have hu := E17.enderUpperB_affine_from_guards
    D (Tuned.R D) (Tuned.S D) (Tuned.euclidRadius D)
    (ellipseUpperCount D (Tuned.euclidRadius D))
    hd.1 hS hρ
    (E18.euclid_S_over_R_300 D hD)
    (E18.euclid_log_radius_nonneg_300 D hD)
    (E19.euclid_log_radius_upper_300 D hD)
    (E18.euclid_log_ratio_ge_one_300 D hD)
    (E19.euclid_log_R_over_radius_upper_300 D hD)
    (E18.euclid_radius_over_R_300 D hD)
    (E20.euclid_log_ratio_over_R_300 D hD)
    (E20.euclid_count_log_over_R_300 D hD)
  have hmargin := E17.enderUpperB_affine_margin (Real.log (D : Real))
  dsimp [E16.euclidAnalyticUpper] at hu ⊢
  exact hu.trans hmargin.le

/-- The missing scalar comparison closes without squarefree or
class-number assumptions and with the original E6/E15 source constants. -/
theorem euclid_uniform_scalar_separation_300 (D : Nat)
    (hD : (300 : Nat)^4 ≤ D) :
    E16.euclidAnalyticUpper D < E16.euclidArithmeticLower D := by
  exact lt_of_le_of_lt
    (euclid_analytic_upper_le_affine_300 D hD)
    (E17.euclid_lower_gt_simple_upper_300 D hD)

/-- Odd quadratic maximal-order chart: class-number-one exclusion on
the original source. Full totally-complex degree-two field transport and
dependency closure audit are separate release obligations. -/
theorem odd_classNumber_ne_one_300
    (D : Nat) (hD : (300 : Nat)^4 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D) :
    NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) ≠ 1 := by
  intro hc
  exact E16.contradiction_of_scalar_separation D hD hsq hc
    (euclid_uniform_scalar_separation_300 D hD)

end
end TenthDiscriminant.E21

#print axioms TenthDiscriminant.E21.euclid_analytic_upper_le_affine_300
#print axioms TenthDiscriminant.E21.euclid_uniform_scalar_separation_300
#print axioms TenthDiscriminant.E21.odd_classNumber_ne_one_300
