import TenthDiscriminant.SharpRadialDetBound
import TenthDiscriminant.EndpointCutoff

/-!
# Phase132: a proposed 47.1-billion actual-field endpoint

This is a new theorem, not an edit of the existing 47.5-billion statement.
It reuses the original integer ordinary-jet determinant, the inherited
prime-mass lower bound and the new SharpRadialDetBound upper inequality.
The normalizing scale is identical on both sides. No surrogate field or
gram determinant has been introduced.

The 47.1-billion threshold is not a verified result until this module
compiles and its transitive axiom dependencies pass the root audit.
-/
namespace TenthDiscriminant.SharpRadialEndpoint
open FirstCertificate RadialCutoff
set_option autoImplicit false
noncomputable section

/-- A five-term rational log enclosure at 47.1 billion. Four terms
    do not give the requested lower bracket. -/
theorem endpoint_certificate :
    checkPositiveLogBounds 5 47100000000 35 (122877/5000) (2458/100) = true := by
  norm_num [checkPositiveLogBounds, binaryLogLowerRat, binaryLogUpperRat,
    oddLogPrefixRat, oddLogRemainderRat, Finset.sum_range_succ]

theorem endpoint_log_lower (D : Nat) (hD : 47100000000 ≤ D) :
    (122877/5000 : Real) ≤ Real.log D := by
  have hc := (checkPositiveLogBounds_sound 5 47100000000 35
    (122877/5000) (2458/100) endpoint_certificate).1
  norm_num at hc
  have hb : (47100000000 : Real) ≤ D := by exact_mod_cast hD
  convert hc.trans (Real.log_le_log (by norm_num : (0 : Real) < 47100000000) hb)
    using 1 <;> norm_num

/-- The exact margin is 31369/5000000000 = 0.0000062738.
    This is strictly positive, but small enough that rounding is unsafe. -/
theorem endpoint_separation (u : Real) (hu : 122877/5000 ≤ u) :
    (4/5*u-824/1000)+31369/5000000000 ≤
      999997/1000000*u-5739/1000 := by
  linarith

/-- Odd fundamental-discriminant chart: class number one contradicts
    the two bounds on the SAME actual positive integer determinant. -/
theorem odd_large_classNumber_ne_one_47_1b (D : Nat) (hD : 47100000000 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D) :
    NumberField.classNumber (QuadraticField (((D : Int)+1)/4)) ≠ 1 := by
  intro hc
  have hgeom : 41006250000 ≤ D := by omega
  have hd := Tuned.dimensions D hgeom
  have hp := comparisonScale_pos (Tuned.R D) (Tuned.S D) (by omega) (by omega)
  have hupper := SharpRadialDetBound.production_normalized_upper D hgeom
  have hactual := div_le_div_of_nonneg_right
    (recovered_mass_le_actual_log D hgeom hsq hc) hp.le
  have hlower := recovered_normalized_lower D hgeom
  have hsep := endpoint_separation (Real.log D) (endpoint_log_lower D hD)
  linarith

theorem imaginaryQuadratic_large_classNumber_ne_one_47_1b (d : Nat)
    [Fact (0<d)] (hsq : Squarefree d) (hd : 47100000000 ≤ d) :
    NumberField.classNumber (ImaginaryQuadraticField d) ≠ 1 := by
  rcases squarefree_mod_four_cases d hsq with ho | he
  · letI : Fact ((d : Int)%4=3) := ⟨ho⟩
    intro hc
    have hh := classNumber_one_of_field_equiv _ _ (quadraticChartEquiv d) hc
    exact odd_large_classNumber_ne_one_47_1b d hd hsq hh
  · letI : Fact ((d : Int)%4=1 ∨ (d : Int)%4=2) := ⟨he⟩
    exact even_classNumber_ne_one d hsq (by omega)

/-- Actual discriminant of the imaginary quadratic field, not det(G). -/
theorem imaginaryQuadratic_classNumber_one_discriminant_bound_47_1b
    (d : Nat) [Fact (0<d)] (hsq : Squarefree d)
    (hc : NumberField.classNumber (ImaginaryQuadraticField d)=1) :
    (NumberField.discr (ImaginaryQuadraticField d)).natAbs < 47100000000 := by
  have hrad : d < 47100000000 := by
    by_contra h
    exact imaginaryQuadratic_large_classNumber_ne_one_47_1b d hsq (by omega) hc
  rw [imaginaryQuadratic_discr_natAbs d hsq]
  rcases squarefree_mod_four_cases d hsq with ho | he
  · simpa [absoluteDiscriminantParameter, ho] using hrad
  · letI : Fact ((d : Int)%4=1 ∨ (d : Int)%4=2) := ⟨he⟩
    have hn := even_classNumber_one_only_one_or_two d hsq hc
    have hnot : ¬ (d : Int)%4=3 := by omega
    simp only [absoluteDiscriminantParameter, if_neg hnot]
    omega

/-- Complete degree-two totally complex field: the actual field discriminant.
    This does not derive a different small-field classification or new method. -/
theorem totallyComplex_degree_two_classNumber_one_discriminant_bound_47_1b
    (K : Type*) [Field K] [NumberField K] [NumberField.IsTotallyComplex K]
    (hdegree : Module.finrank Rat K=2) (hc : NumberField.classNumber K=1) :
    (NumberField.discr K).natAbs < 47100000000 := by
  obtain ⟨d,hd,hsq,a,ha⟩ :=
    exists_squarefree_root_of_totallyComplex_degree_two K hdegree
  letI : Fact (0<d) := ⟨hd⟩
  let e := imaginaryQuadraticEquivOfRoot d K a ha hdegree
  have hcan := classNumber_one_of_field_equiv K (ImaginaryQuadraticField d) e.symm hc
  rw [NumberField.discr_eq_discr_of_algEquiv K e.symm]
  exact imaginaryQuadratic_classNumber_one_discriminant_bound_47_1b d hsq hcan

theorem endpoint_controls :
    (41006250000 : Nat) ≤ 47100000000 ∧
    47100000000 < 47500000000 ∧
    (0 : Real) < 31369/5000000000 := by
  norm_num

end
end TenthDiscriminant.SharpRadialEndpoint
