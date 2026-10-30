import TenthDiscriminant.TightRadialSaving
import TenthDiscriminant.SharpRadialEndpoint

/-! Phase133 proposed. The old 47.1b proof, arithmetic lower bound, original
integer ordinary-jet Gram, even chart and field equivalence are unchanged. -/
namespace TenthDiscriminant.TightRadialEndpoint
open FirstCertificate RadialCutoff
set_option autoImplicit false
noncomputable section

/-- Exact N=5 rational log bracket at 47 billion. N=4 is insufficient. -/
theorem endpoint_certificate :
    checkPositiveLogBounds 5 47000000000 35
      (24573/1000) (2458/100) = true := by
  norm_num [checkPositiveLogBounds,binaryLogLowerRat,binaryLogUpperRat,
    oddLogPrefixRat,oddLogRemainderRat,Finset.sum_range_succ]

theorem endpoint_log_lower (D : Nat) (hD : 47000000000 ≤ D) :
    (24573/1000 : Real) ≤ Real.log D := by
  have hc := (checkPositiveLogBounds_sound 5 47000000000 35
    (24573/1000) (2458/100) endpoint_certificate).1
  norm_num at hc
  have hb : (47000000000 : Real) ≤ D := by exact_mod_cast hD
  convert hc.trans (Real.log_le_log (by norm_num : (0 : Real) < 47000000000) hb)
    using 1 <;> norm_num

/-- Exact separation of the two normalized bounds, no decimals in proof. -/
theorem endpoint_separation (u : Real) (hu : 24573/1000 ≤ u) :
    (4/5*u-1649/2000)+26281/1000000000 ≤
      999997/1000000*u-5739/1000 := by
  linarith

theorem odd_large_classNumber_ne_one_47b
    (D : Nat) (hD : 47000000000 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D) :
    NumberField.classNumber (QuadraticField (((D : Int)+1)/4)) ≠ 1 := by
  intro hc
  have hgeom : 41006250000 ≤ D := by omega
  have hd := Tuned.dimensions D hgeom
  have hp := comparisonScale_pos (Tuned.R D) (Tuned.S D) (by omega) (by omega)
  have hupper := TightRadialSaving.production_normalized_upper_tight D hgeom
  have hactual := div_le_div_of_nonneg_right
    (recovered_mass_le_actual_log D hgeom hsq hc) hp.le
  have hlower := recovered_normalized_lower D hgeom
  have hsep := endpoint_separation (Real.log D) (endpoint_log_lower D hD)
  linarith

theorem imaginaryQuadratic_large_classNumber_ne_one_47b (d : Nat)
    [Fact (0<d)] (hsq : Squarefree d) (hd : 47000000000 ≤ d) :
    NumberField.classNumber (ImaginaryQuadraticField d) ≠ 1 := by
  rcases squarefree_mod_four_cases d hsq with ho | he
  · letI : Fact ((d : Int)%4=3) := ⟨ho⟩
    intro hc
    have hh := classNumber_one_of_field_equiv _ _
      (quadraticChartEquiv d) hc
    exact odd_large_classNumber_ne_one_47b d hd hsq hh
  · letI : Fact ((d : Int)%4=1 ∨ (d : Int)%4=2) := ⟨he⟩
    exact even_classNumber_ne_one d hsq (by omega)

/-- Actual discriminant of the imaginary quadratic field, not det(G). -/
theorem imaginaryQuadratic_classNumber_one_discriminant_bound_47b
    (d : Nat) [Fact (0<d)] (hsq : Squarefree d)
    (hc : NumberField.classNumber (ImaginaryQuadraticField d)=1) :
    (NumberField.discr (ImaginaryQuadraticField d)).natAbs < 47000000000 := by
  have hrad : d < 47000000000 := by
    by_contra h
    exact imaginaryQuadratic_large_classNumber_ne_one_47b d hsq
      (by omega) hc
  rw [imaginaryQuadratic_discr_natAbs d hsq]
  rcases squarefree_mod_four_cases d hsq with ho | he
  · simpa [absoluteDiscriminantParameter, ho] using hrad
  · letI : Fact ((d : Int)%4=1 ∨ (d : Int)%4=2) := ⟨he⟩
    have hn := even_classNumber_one_only_one_or_two d hsq hc
    have hnot : ¬ (d : Int)%4=3 := by omega
    simp only [absoluteDiscriminantParameter, if_neg hnot]
    omega

/-- Complete totally complex degree-two field; no chosen generator required. -/
theorem totallyComplex_degree_two_classNumber_one_discriminant_bound_47b
    (K : Type*) [Field K] [NumberField K] [NumberField.IsTotallyComplex K]
    (hdegree : Module.finrank Rat K=2)
    (hc : NumberField.classNumber K=1) :
    (NumberField.discr K).natAbs < 47000000000 := by
  obtain ⟨d,hd,hsq,a,ha⟩ :=
    exists_squarefree_root_of_totallyComplex_degree_two K hdegree
  letI : Fact (0<d) := ⟨hd⟩
  let e := imaginaryQuadraticEquivOfRoot d K a ha hdegree
  have hcan := classNumber_one_of_field_equiv K
    (ImaginaryQuadraticField d) e.symm hc
  rw [NumberField.discr_eq_discr_of_algEquiv K e.symm]
  exact imaginaryQuadratic_classNumber_one_discriminant_bound_47b
    d hsq hcan

theorem endpoint_controls :
    (41006250000 : Nat) ≤ 47000000000 ∧
    47000000000 < 47100000000 ∧
    (0 : Real) < 26281/1000000000 := by
  norm_num

end
end TenthDiscriminant.TightRadialEndpoint
