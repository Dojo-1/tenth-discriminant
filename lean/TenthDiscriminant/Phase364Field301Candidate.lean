import TenthDiscriminant.Phase362ThinUpper301
import TenthDiscriminant.Phase363JointLower301
import TenthDiscriminant.Phase361StrongerRadius301
import TenthDiscriminant.Phase362SourcePositivity301
import TenthDiscriminant.ThinIntegratedEndpoint

/-!
# Phase364 — proposed 301 source-to-field integration (RESEARCH ONLY)

A fresh combined-head theorem target, not yet kernel checked. Imports EXACT original
Phase362 thin Q integer trace-Gram analytic upper and Phase363 arithmetic lower,
then instantiates both on identical Qthin, D, J, R, S and comparisonScale.
The scalar incompatibility is the already checked Phase361 stronger-radius result.
Odd/even maximal-order chart and actual NumberField.discr transport are unchanged
in structure from Phase359, but must receive new exact-head checks and independent
number-theoretic source reconstruction before ANY promotion or publication.
Never infer an extra conductor-derived prime divisor, switch the Gram, or claim
new Siegel-zero consequences from this source comparison.
-/
namespace TenthDiscriminant.Threshold301
open FirstCertificate
open scoped BigOperators Classical
set_option autoImplicit false
noncomputable section

theorem odd_large_classNumber_ne_one_301
    (D : Nat) (hD : (301 : Nat)^4 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D) :
    NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) ≠ 1 := by
  intro hc
  have hupper := TenthDiscriminant.Phase362.thin_production_normalized_upper_stronger_301 D hD
  have hpositive := Tuned.thin_original_gram_pos_301 D hD
  have hlower := TenthDiscriminant.Phase348.original_source_joint_normalized_lower_301
    (ellipsePairs D (Tuned.thinRadius D)) D hD hsq hc hpositive
  exact TenthDiscriminant.Phase361.no_scalar_overlap_301_with_sharp_radius
    D hD _ hupper hlower

/-- Preserve the original odd/even maximal-order chart split. -/
theorem imaginaryQuadratic_large_classNumber_ne_one_301
    (d : Nat) [Fact (0 < d)] (hsq : Squarefree d)
    (hd : (301 : Nat)^4 ≤ d) :
    NumberField.classNumber (ImaginaryQuadraticField d) ≠ 1 := by
  rcases squarefree_mod_four_cases d hsq with ho | he
  · letI : Fact ((d : Int)%4=3) := ⟨ho⟩
    intro hc
    have hh := classNumber_one_of_field_equiv _ _
      (quadraticChartEquiv d) hc
    exact odd_large_classNumber_ne_one_301 d hd hsq hh
  · letI : Fact ((d : Int)%4=1 ∨ (d : Int)%4=2) := ⟨he⟩
    exact even_classNumber_ne_one d hsq (by omega)

/-- Bound on the ACTUAL absolute field discriminant, not on a
source-parameter or determinant substituted for that field invariant. -/
theorem imaginaryQuadratic_classNumber_one_discriminant_bound_301
    (d : Nat) [Fact (0 < d)] (hsq : Squarefree d)
    (hc : NumberField.classNumber (ImaginaryQuadraticField d)=1) :
    (NumberField.discr (ImaginaryQuadraticField d)).natAbs <
      (301 : Nat)^4 := by
  have hrad : d < (301 : Nat)^4 := by
    by_contra h
    exact imaginaryQuadratic_large_classNumber_ne_one_301 d hsq
      (by omega) hc
  rw [imaginaryQuadratic_discr_natAbs d hsq]
  rcases squarefree_mod_four_cases d hsq with ho | he
  · simpa [absoluteDiscriminantParameter,ho] using hrad
  · letI : Fact ((d : Int)%4=1 ∨ (d : Int)%4=2) := ⟨he⟩
    have hn := even_classNumber_one_only_one_or_two d hsq hc
    have hnot : ¬ (d : Int)%4=3 := by omega
    simp only [absoluteDiscriminantParameter,if_neg hnot]
    omega

/-- Research-target field statement; depends solely on the source
comparison and the existing maximal-order equivalence transport,
not on the classification of nine Heegner discriminants. -/
theorem totallyComplex_degree_two_classNumber_one_discriminant_bound_301
    (K : Type*) [Field K] [NumberField K]
    [NumberField.IsTotallyComplex K]
    (hdegree : Module.finrank Rat K = 2)
    (hc : NumberField.classNumber K = 1) :
    (NumberField.discr K).natAbs < (301 : Nat)^4 := by
  obtain ⟨d,hd,hsq,a,ha⟩ :=
    exists_squarefree_root_of_totallyComplex_degree_two K hdegree
  letI : Fact (0<d) := ⟨hd⟩
  let e := imaginaryQuadraticEquivOfRoot d K a ha hdegree
  have hcan := classNumber_one_of_field_equiv K
    (ImaginaryQuadraticField d) e.symm hc
  rw [NumberField.discr_eq_discr_of_algEquiv K e.symm]
  exact imaginaryQuadratic_classNumber_one_discriminant_bound_301
    d hsq hcan

/-- Exact rational fourth-power regression. -/
theorem fourth_power_301_control :
    (301 : Nat)^4 = 8208541201 ∧
    8208541201 < (315 : Nat)^4 := by
  norm_num

end
end TenthDiscriminant.Threshold301

#print axioms TenthDiscriminant.Threshold301.totallyComplex_degree_two_classNumber_one_discriminant_bound_301
