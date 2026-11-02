import TenthDiscriminant.ThinRadiusAnalyticGain
import TenthDiscriminant.TightRadialEndpoint

/-!
# Phase143: integrated thin-ellipse argument for the ACTUAL field discriminant

Unlike a row-frame change, the thin ellipse changes the integer observation
matrix. Both the upper bound and the original arithmetic prime-mass lower
are therefore proved about the SAME NEW positive integer trace Gram.

No theorem below asserts that the thin and old Gram determinants are equal.
The older 47-billion theorem is unchanged.
-/
namespace TenthDiscriminant.ThinIntegratedEndpoint
open FirstCertificate RadialCutoff
set_option autoImplicit false
noncomputable section

private def oldCountUpper (D : Nat) : Real :=
  ellipsePaddedUpperCount D (Tuned.rho D)
    (ellipseVerticalBound D (Tuned.rho D))

/-- Every original ordinary derivative is retained. The old padded
point-count upper still bounds the smaller ellipse. Combined with the
verified 1/10 radius gain and the existing 23/2000 diagonal saving,
this gives the new analytic upper on the NEW integer Gram. -/
theorem thin_production_normalized_upper (D : Nat)
    (hD : 41006250000 ≤ D) :
    Real.log ((integerRectangularTraceGram
       (ellipsePairs D (Tuned.thinRadius D)) D
       (Tuned.S D) (Tuned.R D) (Tuned.S D)).det : Real) /
         comparisonScale (Tuned.R D) (Tuned.S D) ≤
      (4/5 : Real) * Real.log D-1849/2000 := by
  obtain ⟨hS,h25,h26,_⟩ := SharpRadialDetBound.production_guards D hD
  have hd := Tuned.dimensions D hD
  have hD0 : 0 < D := by omega
  have hcard := Tuned.thin_radius_interpolation_count D hD
  obtain ⟨h10, hsmaller, hRrho⟩ := Tuned.thin_radius_guards D hD
  have hcountOld := ellipsePairs_card_gt_of_ender_radius D (Tuned.rho D)
    (3*Tuned.R D+Tuned.S D) hD0 (by omega) (Tuned.chosen_radius D hD)
  have hnold := ellipsePairs_card_le_padded_upper_count D D (Tuned.rho D)
    (ellipseVerticalBound D (Tuned.rho D)) hD0 le_rfl le_rfl
  have hcardmono := Tuned.ellipsePairs_card_mono_radius D
    (Tuned.thinRadius D) (Tuned.rho D) hD0 (Nat.le_of_lt hsmaller)
  have hn : ((ellipsePairs D (Tuned.thinRadius D)).card : Real) ≤
      oldCountUpper D := by
    have hc : ((ellipsePairs D (Tuned.thinRadius D)).card : Real) ≤
        (ellipsePairs D (Tuned.rho D)).card := by
      exact_mod_cast hcardmono
    exact hc.trans hnold
  have hnpos : (0 : Real) < oldCountUpper D := by
    have hpositive : (0 : Real) <
        (ellipsePairs D (Tuned.rho D)).card := by
      exact_mod_cast (show 0 < (ellipsePairs D (Tuned.rho D)).card by omega)
    exact hpositive.trans_le hnold
  have hbound (q : Int × Int)
      (hq : q ∈ ellipsePairs D (Tuned.thinRadius D)) :
      ‖pairEval D q‖ ≤ Tuned.thinRadius D := by
    apply ellipsePoint_norm_le D (Tuned.thinRadius D) hD0
    exact Finset.mem_image.mpr ⟨q,hq,rfl⟩
  have hupper := TightRadialSaving.normalized_integer_upper_tight
    (ellipsePairs D (Tuned.thinRadius D)) D
    (Tuned.R D) (Tuned.S D) (Tuned.thinRadius D)
    (oldCountUpper D)
    hD0 hS h25 h26 h10 hRrho hcard hnpos hn hbound
  have hsave := Tuned.upperB_tenth_saving
    (Tuned.R D) (Tuned.S D) (Tuned.rho D)
    (Tuned.thinRadius D) (oldCountUpper D)
    (by omega) (by omega) h25
    (Tuned.radius_pos D hD) (by omega)
    (Tuned.thin_radius_fraction D hD)
  have hold := Tuned.normalized_upper D hD
  dsimp only [oldCountUpper] at hupper hsave hn hnpos
  linarith

/-- The recovered prime product applies to any finite Q with the
original interpolation guard. This generic interface prevents an
incorrect inference that divisibility of det G_old entails divisibility
of det G_thin. The prime factors are REAPPLIED to the new determinant. -/
theorem recovered_mass_le_eligible_gram_log
    (Q : Finset (Int × Int)) (D : Nat)
    (hD : 41006250000 ≤ D)
    (hcard : 2*(Tuned.R D-1)+(Tuned.S D-1) < Q.card)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hclass : NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4))=1) :
    recoveredPrimeMassLower (Tuned.R D) (Tuned.S D)
      FirstEnderInterval.tailBudget ≤
      Real.log ((integerRectangularTraceGram Q D
        (Tuned.S D) (Tuned.R D) (Tuned.S D)).det : Real) := by
  have hd := Tuned.dimensions D hD
  have hs : 1 ≤ Tuned.S D := by omega
  have htail := certifiedPrimeMassLower_antitone_tail
    (Tuned.R D) (Tuned.S D) hs FirstEnderInterval.tail_le_budget
  have hrec : recoveredPrimeMassLower (Tuned.R D) (Tuned.S D)
      FirstEnderInterval.tailBudget ≤
      recoveredPrimeMassLower (Tuned.R D) (Tuned.S D)
        (enderTailIntegral 10000) := by
    unfold recoveredPrimeMassLower
    linarith
  have hprod := recoveredPrimeMassLower_le_production
    (Tuned.R D) (Tuned.S D) (enderTailIntegral 10000)
    (by omega) hs
  have hmass := enderPrimeMassLower_le_exact_production
    (Tuned.R D) (Tuned.S D) 10000
    (by omega) hs (by decide) hd.2.2.2.1
  exact hrec.trans (hprod.trans
    (hmass.trans
      (prime_mass_log_lower Q D (Tuned.R D) (Tuned.S D)
        (by omega) (by omega) hs hcard hsq hclass
        (Tuned.strict_inertness D))))

theorem recovered_mass_le_thin_log (D : Nat)
    (hD : 41006250000 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hclass : NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4))=1) :
    recoveredPrimeMassLower (Tuned.R D) (Tuned.S D)
      FirstEnderInterval.tailBudget ≤
      Real.log ((integerRectangularTraceGram
        (ellipsePairs D (Tuned.thinRadius D)) D
        (Tuned.S D) (Tuned.R D) (Tuned.S D)).det : Real) := by
  exact recovered_mass_le_eligible_gram_log
    (ellipsePairs D (Tuned.thinRadius D)) D hD
    (Tuned.thin_radius_interpolation_count D hD) hsq hclass

/-- A rational log bracket at the exact geometry floor 450^4.
Only this declared value, not a floating-point approximation, enters
the final strict separation. -/
theorem endpoint_certificate :
    checkPositiveLogBounds 5 41006250000 35
      (241/10) (245/10) = true := by
  norm_num [checkPositiveLogBounds, binaryLogLowerRat,
    binaryLogUpperRat, oddLogPrefixRat, oddLogRemainderRat,
    Finset.sum_range_succ]

theorem endpoint_log_lower (D : Nat) (hD : 41006250000 ≤ D) :
    (241/10 : Real) ≤ Real.log D := by
  have hc := (checkPositiveLogBounds_sound 5 41006250000 35
    (241/10) (245/10) endpoint_certificate).1
  norm_num at hc
  have hb : (41006250000 : Real) ≤ D := by exact_mod_cast hD
  convert hc.trans (Real.log_le_log
    (by norm_num : (0 : Real) < 41006250000) hb)
    using 1 <;> norm_num

theorem endpoint_separation (u : Real) (hu : 241/10 ≤ u) :
    (4/5*u-1849/2000)+1/500 ≤
       999997/1000000*u-5739/1000 := by
  linarith

theorem odd_large_classNumber_ne_one_41floor
    (D : Nat) (hD : 41006250000 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D) :
    NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) ≠ 1 := by
  intro hc
  have hd := Tuned.dimensions D hD
  have hp := comparisonScale_pos (Tuned.R D) (Tuned.S D)
    (by omega) (by omega)
  have hu := thin_production_normalized_upper D hD
  have ha := div_le_div_of_nonneg_right
    (recovered_mass_le_thin_log D hD hsq hc) hp.le
  have hl := recovered_normalized_lower D hD
  have hsep := endpoint_separation
    (Real.log D) (endpoint_log_lower D hD)
  linarith

theorem imaginaryQuadratic_large_classNumber_ne_one_41floor
    (d : Nat) [Fact (0<d)] (hsq : Squarefree d)
    (hd : 41006250000 ≤ d) :
    NumberField.classNumber (ImaginaryQuadraticField d) ≠ 1 := by
  rcases squarefree_mod_four_cases d hsq with ho | he
  · letI : Fact ((d : Int)%4=3) := ⟨ho⟩
    intro hc
    have hh := classNumber_one_of_field_equiv _ _
      (quadraticChartEquiv d) hc
    exact odd_large_classNumber_ne_one_41floor d hd hsq hh
  · letI : Fact ((d : Int)%4=1 ∨ (d : Int)%4=2) := ⟨he⟩
    exact even_classNumber_ne_one d hsq (by omega)

theorem imaginaryQuadratic_classNumber_one_discriminant_bound_41floor
    (d : Nat) [Fact (0<d)] (hsq : Squarefree d)
    (hc : NumberField.classNumber (ImaginaryQuadraticField d)=1) :
    (NumberField.discr (ImaginaryQuadraticField d)).natAbs <
      41006250000 := by
  have hrad : d < 41006250000 := by
    by_contra h
    exact imaginaryQuadratic_large_classNumber_ne_one_41floor d hsq
      (by omega) hc
  rw [imaginaryQuadratic_discr_natAbs d hsq]
  rcases squarefree_mod_four_cases d hsq with ho | he
  · simpa [absoluteDiscriminantParameter, ho] using hrad
  · letI : Fact ((d : Int)%4=1 ∨ (d : Int)%4=2) := ⟨he⟩
    have hn := even_classNumber_one_only_one_or_two d hsq hc
    have hnot : ¬ (d : Int)%4=3 := by omega
    simp only [absoluteDiscriminantParameter, if_neg hnot]
    omega

/-- Final intended object: ACTUAL absolute field discriminant, not a
trace-Gram determinant or a chosen quadratic generator. -/
theorem totallyComplex_degree_two_classNumber_one_discriminant_bound_41floor
    (K : Type*) [Field K] [NumberField K]
    [NumberField.IsTotallyComplex K]
    (hdegree : Module.finrank Rat K=2)
    (hc : NumberField.classNumber K=1) :
    (NumberField.discr K).natAbs < 41006250000 := by
  obtain ⟨d,hd,hsq,a,ha⟩ :=
    exists_squarefree_root_of_totallyComplex_degree_two K hdegree
  letI : Fact (0<d) := ⟨hd⟩
  let e := imaginaryQuadraticEquivOfRoot d K a ha hdegree
  have hcan := classNumber_one_of_field_equiv K
    (ImaginaryQuadraticField d) e.symm hc
  rw [NumberField.discr_eq_discr_of_algEquiv K e.symm]
  exact imaginaryQuadratic_classNumber_one_discriminant_bound_41floor
    d hsq hcan

/-- The final inequality has genuine strict numerical slack at the
declared log floor and is not a substituted Gram-determinant statement. -/
theorem endpoint_controls :
    (450 : Nat)^4=41006250000 ∧
    (41006250000 : Nat)<47000000000 ∧
    (0 : Real)<1/500 := by
  norm_num

end
end TenthDiscriminant.ThinIntegratedEndpoint
