import TenthDiscriminant.ThinUpper377
import TenthDiscriminant.BinaryGap377
import TenthDiscriminant.Lower377
import TenthDiscriminant.SourcePositivity377
import TenthDiscriminant.ThinIntegratedEndpoint

/-!
# Phase178: actual-field 377^4 endpoint — theorem TARGET

Evidence boundary: H until exact-head pinned Lean, source correspondence,
axiom and known-false negative controls and independent semantic review.

The proof uses the EXACT SAME original thin-Q integer ordinary-jet trace
Gram in the odd-prime plus binary lower and the real analytic upper.
The full quadratic-field chart is the original maximal-order field
equivalence and the final conclusion is the ACTUAL field discriminant.

No new prime factors, traces, derivatives, observation lattices, or
surrogate determinants have been introduced. Do not promote this claim
merely because the earlier component branches individually compiled.
-/
namespace TenthDiscriminant.Threshold377
open FirstCertificate
open scoped BigOperators Classical
set_option autoImplicit false
noncomputable section

/-- Same-source log determinant is squeezed between the original
odd-plus-binary arithmetic lower and original analytic upper.
This is the load-bearing candidate for the odd quadratic chart. -/
theorem odd_large_classNumber_ne_one_377
    (D : Nat) (hD : (377 : Nat)^4 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D) :
    NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) ≠ 1 := by
  intro hc
  have hd := FirstCertificate.Tuned.dimensions_377 D hD
  have hp := comparisonScale_pos
    (FirstCertificate.Tuned.R D) (FirstCertificate.Tuned.S D)
    (by omega) (by omega)
  have hpositive := FirstCertificate.Tuned.thin_original_gram_pos_377 D hD
  have hsource := BinaryThinLogBridge.original_binary_and_exact_odd_mass_log_of_pos
    (ellipsePairs D (FirstCertificate.Tuned.thinRadius D)) D
    (FirstCertificate.Tuned.R D) (FirstCertificate.Tuned.S D)
    hsq hc (FirstCertificate.Tuned.strict_inertness D) hpositive
  have hodd := FirstCertificate.Tuned.recovered_mass_le_exact_odd_377 D hD
  have hmass :
      (binaryNullGramExponent
         (FirstCertificate.Tuned.R D) (FirstCertificate.Tuned.S D) : Real)*
        Real.log 2 +
      recoveredPrimeMassLower
        (FirstCertificate.Tuned.R D) (FirstCertificate.Tuned.S D)
        FirstEnderInterval.tailBudget ≤
      Real.log ((integerRectangularTraceGram
         (ellipsePairs D (FirstCertificate.Tuned.thinRadius D)) D
         (FirstCertificate.Tuned.S D) (FirstCertificate.Tuned.R D)
         (FirstCertificate.Tuned.S D)).det : Real) := by
    linarith
  have hdiv := div_le_div_of_nonneg_right hmass hp.le
  rw [add_div] at hdiv
  have hlower := FirstCertificate.Tuned.recovered_normalized_lower_377 D hD
  have hbin := normalized_binary_quarter
    (FirstCertificate.Tuned.R D) (FirstCertificate.Tuned.S D)
    (by omega) (by omega)
  have hjoint :
      (999997/1000000 : Real)*Real.log D-5739/1000 +
        Real.log 2/4 ≤
      Real.log ((integerRectangularTraceGram
         (ellipsePairs D (FirstCertificate.Tuned.thinRadius D)) D
         (FirstCertificate.Tuned.S D) (FirstCertificate.Tuned.R D)
         (FirstCertificate.Tuned.S D)).det : Real) /
        comparisonScale
          (FirstCertificate.Tuned.R D) (FirstCertificate.Tuned.S D) := by
    linarith
  have hupper := ThinUpper377.thin_production_normalized_upper_377 D hD
  exact no_shared_scalar_interval_377 D hD _ hupper hjoint

/-- Preserve the original odd/even maximal-order quadratic field
case split, rather than treating a quadratic generator as the field. -/
theorem imaginaryQuadratic_large_classNumber_ne_one_377
    (d : Nat) [Fact (0 < d)] (hsq : Squarefree d)
    (hd : (377 : Nat)^4 ≤ d) :
    NumberField.classNumber (ImaginaryQuadraticField d) ≠ 1 := by
  rcases squarefree_mod_four_cases d hsq with ho | he
  · letI : Fact ((d : Int)%4=3) := ⟨ho⟩
    intro hc
    have hh := classNumber_one_of_field_equiv _ _
      (quadraticChartEquiv d) hc
    exact odd_large_classNumber_ne_one_377 d hd hsq hh
  · letI : Fact ((d : Int)%4=1 ∨ (d : Int)%4=2) := ⟨he⟩
    exact even_classNumber_ne_one d hsq (by omega)

/-- Bounds the actual absolute field discriminant, not a source Gram
determinant or an arbitrary quadratic radicand. -/
theorem imaginaryQuadratic_classNumber_one_discriminant_bound_377
    (d : Nat) [Fact (0 < d)] (hsq : Squarefree d)
    (hc : NumberField.classNumber (ImaginaryQuadraticField d)=1) :
    (NumberField.discr (ImaginaryQuadraticField d)).natAbs <
      (377 : Nat)^4 := by
  have hrad : d < (377 : Nat)^4 := by
    by_contra h
    exact imaginaryQuadratic_large_classNumber_ne_one_377 d hsq
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
theorem totallyComplex_degree_two_classNumber_one_discriminant_bound_377
    (K : Type*) [Field K] [NumberField K]
    [NumberField.IsTotallyComplex K]
    (hdegree : Module.finrank Rat K = 2)
    (hc : NumberField.classNumber K = 1) :
    (NumberField.discr K).natAbs < (377 : Nat)^4 := by
  obtain ⟨d,hd,hsq,a,ha⟩ :=
    exists_squarefree_root_of_totallyComplex_degree_two K hdegree
  letI : Fact (0<d) := ⟨hd⟩
  let e := imaginaryQuadraticEquivOfRoot d K a ha hdegree
  have hcan := classNumber_one_of_field_equiv K
    (ImaginaryQuadraticField d) e.symm hc
  rw [NumberField.discr_eq_discr_of_algEquiv K e.symm]
  exact imaginaryQuadratic_classNumber_one_discriminant_bound_377
    d hsq hcan

/-- Exact numeric regression; it is not a proof of the field theorem. -/
theorem fourth_power_377_control :
    (377 : Nat)^4 = 20200652641 ∧
    (20200652641 : Nat) < 41006250000 := by
  norm_num

end
end TenthDiscriminant.Threshold377
