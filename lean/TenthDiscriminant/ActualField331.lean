import TenthDiscriminant.ThinUpper331
import TenthDiscriminant.SameGramLower331
import TenthDiscriminant.Scalar331
import TenthDiscriminant.ThinIntegratedEndpoint

/-!
# Phase188 — candidate actual-field 331^4 endpoint

This declaration is a theorem TARGET until the upstream same-source
Phase186 odd-plus-once-counted-binary lower and Phase187 original thin
analytic upper compile on the exact head, the whole-root build/axiom/source
and known-false audits pass, and independent semantic review occurs.

The odd chart uses the same original integer ordinary-Z-jet trace Gram,
same Qthin, trace pairing, dimensions and maximal-order transport.
No additional primes, Gram substitutions, surrogate determinant or
independent new field-classification argument are introduced.
-/
namespace TenthDiscriminant.Threshold331
open FirstCertificate
open scoped BigOperators Classical
set_option autoImplicit false
noncomputable section

/-- Original odd class-number-one chart: the exact same source Gram
cannot lie above the arithmetic mass lower and below the analytic upper
at the sound 331^4 scalar threshold. -/
theorem odd_large_classNumber_ne_one_331
    (D : Nat) (hD : (331 : Nat)^4 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D) :
    NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) ≠ 1 := by
  intro hc
  have hupper := ThinUpper331.thin_production_normalized_upper_331 D hD
  have hlower := TenthDiscriminant.thin_original_odd_plus_binary_normalized_lower_331
    D hD hsq hc
  exact TenthDiscriminant.no_abstract_scalar_overlap_331
    D hD _ hupper hlower

/-- Preserve the original odd/even maximal-order quadratic field
case split, rather than treating a quadratic generator as the field. -/
theorem imaginaryQuadratic_large_classNumber_ne_one_331
    (d : Nat) [Fact (0 < d)] (hsq : Squarefree d)
    (hd : (331 : Nat)^4 ≤ d) :
    NumberField.classNumber (ImaginaryQuadraticField d) ≠ 1 := by
  rcases squarefree_mod_four_cases d hsq with ho | he
  · letI : Fact ((d : Int)%4=3) := ⟨ho⟩
    intro hc
    have hh := classNumber_one_of_field_equiv _ _
      (quadraticChartEquiv d) hc
    exact odd_large_classNumber_ne_one_331 d hd hsq hh
  · letI : Fact ((d : Int)%4=1 ∨ (d : Int)%4=2) := ⟨he⟩
    exact even_classNumber_ne_one d hsq (by omega)

/-- Bounds the actual absolute field discriminant, not a source Gram
determinant or an arbitrary quadratic radicand. -/
theorem imaginaryQuadratic_classNumber_one_discriminant_bound_331
    (d : Nat) [Fact (0 < d)] (hsq : Squarefree d)
    (hc : NumberField.classNumber (ImaginaryQuadraticField d)=1) :
    (NumberField.discr (ImaginaryQuadraticField d)).natAbs <
      (331 : Nat)^4 := by
  have hrad : d < (331 : Nat)^4 := by
    by_contra h
    exact imaginaryQuadratic_large_classNumber_ne_one_331 d hsq
      (by omega) hc
  rw [imaginaryQuadratic_discr_natAbs d hsq]
  rcases squarefree_mod_four_cases d hsq with ho | he
  · simpa [absoluteDiscriminantParameter,ho] using hrad
  · letI : Fact ((d : Int)%4=1 ∨ (d : Int)%4=2) := ⟨he⟩
    have hn := even_classNumber_one_only_one_or_two d hsq hc
    have hnot : ¬ (d : Int)%4=3 := by omega
    simp only [absoluteDiscriminantParameter,if_neg hnot]
    omega

/-- The intended actual-field theorem for all totally complex degree
two number fields, transported through the original field equivalence. -/
theorem totallyComplex_degree_two_classNumber_one_discriminant_bound_331
    (K : Type*) [Field K] [NumberField K]
    [NumberField.IsTotallyComplex K]
    (hdegree : Module.finrank Rat K = 2)
    (hc : NumberField.classNumber K = 1) :
    (NumberField.discr K).natAbs < (331 : Nat)^4 := by
  obtain ⟨d,hd,hsq,a,ha⟩ :=
    exists_squarefree_root_of_totallyComplex_degree_two K hdegree
  letI : Fact (0<d) := ⟨hd⟩
  let e := imaginaryQuadraticEquivOfRoot d K a ha hdegree
  have hcan := classNumber_one_of_field_equiv K
    (ImaginaryQuadraticField d) e.symm hc
  rw [NumberField.discr_eq_discr_of_algEquiv K e.symm]
  exact imaginaryQuadratic_classNumber_one_discriminant_bound_331
    d hsq hcan

/-- Exact numeric regression; it is not a proof of the field theorem. -/
theorem fourth_power_331_control :
    (331 : Nat)^4 = 12003612721 ∧
    (12003612721 : Nat) < 41006250000 := by
  norm_num

end
end TenthDiscriminant.Threshold331
