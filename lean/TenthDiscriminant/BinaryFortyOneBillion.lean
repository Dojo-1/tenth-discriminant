import TenthDiscriminant.BinaryMassLog
import TenthDiscriminant.TightRadialEndpoint

/-!
# An actual-field 41,006,250,000 target from a new BINARY divisor

The source is the SAME original integer ordinary-Z-jet Gram, with the
same existing Tuned radius and all existing odd-prime assumptions.
The stronger number-field conclusion is valid only if all imported
arithmetic/analytic and bridge theorems compile against pinned Mathlib.
No new prime interval, radius, field identification or fourth generator.
-/
namespace TenthDiscriminant.BinaryFortyOneBillion
open FirstCertificate RadialCutoff
set_option autoImplicit false
noncomputable section

/-- The existing production scale and radius are already certified at
this endpoint. The binary mass adds at least 1/8 normalized, which is
more than the former deficit even using the old weak log D >= 24 gate. -/
theorem odd_large_classNumber_ne_one_41006250000
    (D : Nat) (hD : 41006250000 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D) :
    NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) ≠ 1 := by
  intro hc
  let R := Tuned.R D
  let S := Tuned.S D
  let Q := ellipsePairs D (Tuned.rho D)
  let z := (integerRectangularTraceGram Q D S R S).det
  have hd := Tuned.dimensions D hD
  have hs : 1 ≤ S := by
    dsimp [S]
    omega
  have hR : 15 ≤ R := by
    dsimp [R]
    omega
  have hp : 0 < comparisonScale R S :=
    comparisonScale_pos R S (by omega) (by omega)
  have hcount := ellipsePairs_card_gt_of_ender_radius D (Tuned.rho D)
    (3*R+S) (by omega) (by omega) (Tuned.chosen_radius D hD)
  have hcard : 2*(R-1)+(S-1) < Q.card := by
    dsimp [Q]
    omega
  have hz : 0 < z := by
    dsimp [z,Q,R,S]
    exact integer_det_positive (ellipsePairs D (Tuned.rho D))
      D (Tuned.R D) (Tuned.S D)
      (by omega) (by omega) (by omega) (by simpa only [Q,R,S] using hcard)
  have hprime := binaryOddMass_log_le_of_det_pos Q D R S hz
    hsq hc (Tuned.strict_inertness D)
  have hrec :
      recoveredPrimeMassLower R S FirstEnderInterval.tailBudget ≤
      recoveredPrimeMassLower R S (enderTailIntegral 10000) := by
    unfold recoveredPrimeMassLower
    linarith
  have hprod := recoveredPrimeMassLower_le_production R S
      (enderTailIntegral 10000) (by omega) hs
  have hodd := enderPrimeMassLower_le_exact_production R S 10000
      (by omega) hs (by decide) hd.2.2.2.1
  have hchain :
      recoveredPrimeMassLower R S FirstEnderInterval.tailBudget ≤
        exactOddPrimeMass R S :=
    hrec.trans (hprod.trans hodd)
  have hboth :
      recoveredPrimeMassLower R S FirstEnderInterval.tailBudget +
        (binaryNullGramExponent R S : Real)*Real.log 2 ≤
        Real.log (z : Real) := by
    linarith
  have hbothnorm :
      recoveredPrimeMassLower R S FirstEnderInterval.tailBudget/
          comparisonScale R S +
        ((binaryNullGramExponent R S : Real)*Real.log 2)/
          comparisonScale R S ≤ Real.log (z : Real)/comparisonScale R S := by
    have h := div_le_div_of_nonneg_right hboth hp.le
    rw [add_div] at h
    exact h
  have hbinary :
      (1/8 : Real) ≤
        ((binaryNullGramExponent R S : Real)*Real.log 2)/
          comparisonScale R S :=
    binaryNull_normalized_gain_eighth R S hR (by omega)
  have hlower := recovered_normalized_lower D hD
  have hupper := TightRadialSaving.production_normalized_upper_tight D hD
  have hlog := Tuned.log_large_geometry D hD
  dsimp [R,S,Q,z] at hlower hupper hbothnorm hbinary
  linarith

/-- The even chart is unchanged. All the new arithmetic gain belongs
to the previously checked odd maximal-order chart. -/
theorem imaginaryQuadratic_large_classNumber_ne_one_41006250000
    (d : Nat) [Fact (0<d)] (hsq : Squarefree d)
    (hd : 41006250000 ≤ d) :
    NumberField.classNumber (ImaginaryQuadraticField d) ≠ 1 := by
  rcases squarefree_mod_four_cases d hsq with ho | he
  · letI : Fact ((d : Int)%4=3) := ⟨ho⟩
    intro hc
    have hh := classNumber_one_of_field_equiv _ _
      (quadraticChartEquiv d) hc
    exact odd_large_classNumber_ne_one_41006250000 d hd hsq hh
  · letI : Fact ((d : Int)%4=1 ∨ (d : Int)%4=2) := ⟨he⟩
    exact even_classNumber_ne_one d hsq (by omega)

/-- The actual FIELD discriminant, never the auxiliary trace-Gram det. -/
theorem imaginaryQuadratic_classNumber_one_discriminant_bound_41006250000
    (d : Nat) [Fact (0<d)] (hsq : Squarefree d)
    (hc : NumberField.classNumber (ImaginaryQuadraticField d)=1) :
    (NumberField.discr (ImaginaryQuadraticField d)).natAbs <
      41006250000 := by
  have hrad : d < 41006250000 := by
    by_contra h
    exact imaginaryQuadratic_large_classNumber_ne_one_41006250000 d hsq
      (by omega) hc
  rw [imaginaryQuadratic_discr_natAbs d hsq]
  rcases squarefree_mod_four_cases d hsq with ho | he
  · simpa [absoluteDiscriminantParameter, ho] using hrad
  · letI : Fact ((d : Int)%4=1 ∨ (d : Int)%4=2) := ⟨he⟩
    have hn := even_classNumber_one_only_one_or_two d hsq hc
    have hnot : ¬ (d : Int)%4=3 := by omega
    simp only [absoluteDiscriminantParameter, if_neg hnot]
    omega

/-- Complete totally complex degree-two field, no fixed generator. -/
theorem totallyComplex_degree_two_classNumber_one_discriminant_bound_41006250000
    (K : Type*) [Field K] [NumberField K] [NumberField.IsTotallyComplex K]
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
  exact imaginaryQuadratic_classNumber_one_discriminant_bound_41006250000
    d hsq hcan

end
end TenthDiscriminant.BinaryFortyOneBillion
