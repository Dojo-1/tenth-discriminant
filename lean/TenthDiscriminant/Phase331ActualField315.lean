import TenthDiscriminant.Phase331SameGramLower315
import TenthDiscriminant.Phase331ScalarOverlap315
import TenthDiscriminant.Phase323ThinUpper315
import TenthDiscriminant.SourcePositivity315
import TenthDiscriminant.ThinIntegratedEndpoint

/-!
# Phase331 research-only target: actual totally-complex quadratic fields
# and fourth-root cutoff 315

All source determinants in the lower and upper are literally:
 integerRectangularTraceGram
   (ellipsePairs D (Tuned.thinRadius D)) D (Tuned.S D)
   (Tuned.R D) (Tuned.S D).

Neither a padded Gram nor an alternate ordinary-jet convention enters.
The lower comes from ONE joint 2-adic unimodular row basis and the
original complete odd-prime product, with 3,5 and ten further
p² horizontal contributions counted once each.

Proving this Lean declaration alone does not validate independent
semantic fidelity of the original determinant model or historical
novelty. The file must compile at exact head with no sorryAx before
being promoted to a formally checked research result.
-/
namespace TenthDiscriminant.Threshold315
open FirstCertificate
open scoped BigOperators Classical
set_option autoImplicit false
noncomputable section

/-- The odd imaginary quadratic maximal-order chart, using the
actual 315 source support and the identical positive integer Gram
in the arithmetic and Hadamard inequalities. -/
theorem odd_large_classNumber_ne_one_315
    (D : Nat) (hD : (315 : Nat)^4 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D) :
    NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) ≠ 1 := by
  intro hc
  have hupper := TenthDiscriminant.ThinUpper315.thin_production_normalized_upper_315 D hD
  have hpositive := Tuned.thin_original_gram_pos_315 D hD
  have hlower := TenthDiscriminant.Phase331.original_source_joint_normalized_lower_315
    (ellipsePairs D (Tuned.thinRadius D)) D hD hsq hc hpositive
  exact TenthDiscriminant.Phase331.no_same_gram_scalar_overlap_315
    D hD _ hupper hlower

/-- Preserve the original odd/even maximal-order chart split. -/
theorem imaginaryQuadratic_large_classNumber_ne_one_315
    (d : Nat) [Fact (0 < d)] (hsq : Squarefree d)
    (hd : (315 : Nat)^4 ≤ d) :
    NumberField.classNumber (ImaginaryQuadraticField d) ≠ 1 := by
  rcases squarefree_mod_four_cases d hsq with ho | he
  · letI : Fact ((d : Int)%4=3) := ⟨ho⟩
    intro hc
    have hh := classNumber_one_of_field_equiv _ _
      (quadraticChartEquiv d) hc
    exact odd_large_classNumber_ne_one_315 d hd hsq hh
  · letI : Fact ((d : Int)%4=1 ∨ (d : Int)%4=2) := ⟨he⟩
    exact even_classNumber_ne_one d hsq (by omega)

/-- Bound on the ACTUAL absolute field discriminant, not on a
source-parameter or determinant substituted for that field invariant. -/
theorem imaginaryQuadratic_classNumber_one_discriminant_bound_315
    (d : Nat) [Fact (0 < d)] (hsq : Squarefree d)
    (hc : NumberField.classNumber (ImaginaryQuadraticField d)=1) :
    (NumberField.discr (ImaginaryQuadraticField d)).natAbs <
      (315 : Nat)^4 := by
  have hrad : d < (315 : Nat)^4 := by
    by_contra h
    exact imaginaryQuadratic_large_classNumber_ne_one_315 d hsq
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
theorem totallyComplex_degree_two_classNumber_one_discriminant_bound_315
    (K : Type*) [Field K] [NumberField K]
    [NumberField.IsTotallyComplex K]
    (hdegree : Module.finrank Rat K = 2)
    (hc : NumberField.classNumber K = 1) :
    (NumberField.discr K).natAbs < (315 : Nat)^4 := by
  obtain ⟨d,hd,hsq,a,ha⟩ :=
    exists_squarefree_root_of_totallyComplex_degree_two K hdegree
  letI : Fact (0<d) := ⟨hd⟩
  let e := imaginaryQuadraticEquivOfRoot d K a ha hdegree
  have hcan := classNumber_one_of_field_equiv K
    (ImaginaryQuadraticField d) e.symm hc
  rw [NumberField.discr_eq_discr_of_algEquiv K e.symm]
  exact imaginaryQuadratic_classNumber_one_discriminant_bound_315
    d hsq hcan

/-- Exact rational fourth-power regression. -/
theorem fourth_power_315_control :
    (315 : Nat)^4 = 9845600625 ∧
    9845600625 < (321 : Nat)^4 := by
  norm_num

end
end TenthDiscriminant.Threshold315

#print axioms TenthDiscriminant.Threshold315.totallyComplex_degree_two_classNumber_one_discriminant_bound_315
