import TenthDiscriminant.Phase347ThinUpper307
import TenthDiscriminant.Phase348JointLower307
import TenthDiscriminant.Phase343Scalar307
import TenthDiscriminant.Phase347SourcePositivity307
import TenthDiscriminant.ThinIntegratedEndpoint

/-!
RESEARCH ONLY: 307-domain candidate, not a certificate until exact-head Lean CI
and independent source-fidelity inspection. Uses same original Qthin ordinary
Z jets and the same integer trace Gram as the 313-domain theorem.
# Phase349 — candidate actual-field discriminant cutoff 307^4

This is an UNVERIFIED research target until a fresh exact-head build
passes every lower/upper statement and the standard-axiom checker.

Arithmetic lower: one unchanged original ordinary-Z jet Gram on
Qthin, built from the existing joint unimodular binary action and
the already-proved odd-prime sources. No Phase332 mixed H gain.
Analytic upper: the SAME Qthin source Gram, rederived from the
original 307-domain geometry and stronger 17/20 radius contraction.
Both source bounds must be independently verified at 307.

Do NOT promote to main or claim an independently validated theorem
without compilation, source provenance, and human mathematical audit.
-/
namespace TenthDiscriminant.Threshold307
open FirstCertificate
open scoped BigOperators Classical
set_option autoImplicit false
noncomputable section

theorem odd_large_classNumber_ne_one_307
    (D : Nat) (hD : (307 : Nat)^4 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D) :
    NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) ≠ 1 := by
  intro hc
  have hupper := TenthDiscriminant.Phase347.thin_production_normalized_upper_stronger_307 D hD
  have hpositive := Tuned.thin_original_gram_pos_307 D hD
  have hlower := TenthDiscriminant.Phase348.original_source_joint_normalized_lower_307
    (ellipsePairs D (Tuned.thinRadius D)) D hD hsq hc hpositive
  exact TenthDiscriminant.Phase343.no_scalar_overlap_307_without_mixed
    D hD _ hupper hlower

/-- Preserve the original odd/even maximal-order chart split. -/
theorem imaginaryQuadratic_large_classNumber_ne_one_307
    (d : Nat) [Fact (0 < d)] (hsq : Squarefree d)
    (hd : (307 : Nat)^4 ≤ d) :
    NumberField.classNumber (ImaginaryQuadraticField d) ≠ 1 := by
  rcases squarefree_mod_four_cases d hsq with ho | he
  · letI : Fact ((d : Int)%4=3) := ⟨ho⟩
    intro hc
    have hh := classNumber_one_of_field_equiv _ _
      (quadraticChartEquiv d) hc
    exact odd_large_classNumber_ne_one_307 d hd hsq hh
  · letI : Fact ((d : Int)%4=1 ∨ (d : Int)%4=2) := ⟨he⟩
    exact even_classNumber_ne_one d hsq (by omega)

/-- Bound on the ACTUAL absolute field discriminant, not on a
source-parameter or determinant substituted for that field invariant. -/
theorem imaginaryQuadratic_classNumber_one_discriminant_bound_307
    (d : Nat) [Fact (0 < d)] (hsq : Squarefree d)
    (hc : NumberField.classNumber (ImaginaryQuadraticField d)=1) :
    (NumberField.discr (ImaginaryQuadraticField d)).natAbs <
      (307 : Nat)^4 := by
  have hrad : d < (307 : Nat)^4 := by
    by_contra h
    exact imaginaryQuadratic_large_classNumber_ne_one_307 d hsq
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
theorem totallyComplex_degree_two_classNumber_one_discriminant_bound_307
    (K : Type*) [Field K] [NumberField K]
    [NumberField.IsTotallyComplex K]
    (hdegree : Module.finrank Rat K = 2)
    (hc : NumberField.classNumber K = 1) :
    (NumberField.discr K).natAbs < (307 : Nat)^4 := by
  obtain ⟨d,hd,hsq,a,ha⟩ :=
    exists_squarefree_root_of_totallyComplex_degree_two K hdegree
  letI : Fact (0<d) := ⟨hd⟩
  let e := imaginaryQuadraticEquivOfRoot d K a ha hdegree
  have hcan := classNumber_one_of_field_equiv K
    (ImaginaryQuadraticField d) e.symm hc
  rw [NumberField.discr_eq_discr_of_algEquiv K e.symm]
  exact imaginaryQuadratic_classNumber_one_discriminant_bound_307
    d hsq hcan

/-- Exact rational fourth-power regression. -/
theorem fourth_power_307_control :
    (307 : Nat)^4 = 8882874001 ∧
    8882874001 < (315 : Nat)^4 := by
  norm_num

end
end TenthDiscriminant.Threshold307

#print axioms TenthDiscriminant.Threshold307.totallyComplex_degree_two_classNumber_one_discriminant_bound_307
