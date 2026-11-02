import TenthDiscriminant.RadialDetBound
import TenthDiscriminant.PrimeTail
import TenthDiscriminant.ImaginaryQuadraticRepresentation

/-! Phase120: arithmetic lower bound on the same integer and actual field cutoff.
The preceding118+119 bodies are exact accepted local dependencies. -/
namespace TenthDiscriminant.RadialCutoff
open FirstCertificate
open scoped BigOperators Classical
set_option autoImplicit false
noncomputable section

theorem integer_det_positive (Q : Finset (Int × Int)) (D R S : Nat)
    (hD : 0 < D) (hR : 1 ≤ R) (hS : 1 ≤ S)
    (hcard : 2*(R-1)+(S-1) < Q.card) :
    0 < (integerRectangularTraceGram Q D S R S).det := by
  have hcount : 2*(R-1)+(S-1) < (Q.image (pairEval D)).card := by
    rw [Finset.card_image_of_injective _ (show Function.Injective (pairEval D) from
      latticePoint_injective D hD)]
    exact hcard
  have hp : (0 : Real) < ((integerRectangularTraceGram Q D S R S).det : Real) := by
    rw [integerRectangularTraceGram_det_cast Q D S R S hD]
    exact (rectangularTraceGram_posDef_of_point_count (Q.image (pairEval D)) S R S
      hR hS le_rfl hcount).det_pos
  exact_mod_cast hp

/-- Prime mass acts on the SAME original integer Gram, with positivity supplied
directly rather than inferred from a sufficient interpolation cardinality guard.
No claim about how positivity for a new observation support is established. -/
theorem prime_mass_log_lower_of_det_pos (Q : Finset (Int × Int)) (D R S : Nat)
    (hD : 0 < D) (hR : 1 ≤ R) (hS : 1 ≤ S)
    (hdet : 0 < (integerRectangularTraceGram Q D S R S).det)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hclass : NumberField.classNumber (QuadraticField (((D : Int)+1)/4))=1)
    (hRcut : (R : Int) < ((D : Int)+1)/4) :
    exactOddPrimeMass R S ≤ Real.log ((integerRectangularTraceGram Q D S R S).det : Real) := by
  let P := oddPrimesBelow R
  let z := (integerRectangularTraceGram Q D S R S).det
  have hz : 0 < z := hdet
  have hprime (p : Nat) (hp : p ∈ P) : p.Prime := (Finset.mem_filter.mp hp).2.1
  have hlocal (p : Nat) (hp : p ∈ P) : (p : Int)^(2*valuationWeight R S p) ∣ z := by
    letI : Fact p.Prime := ⟨hprime p hp⟩
    have hodd : p ≠ 2 := (Finset.mem_filter.mp hp).2.2
    have hpr : p < R := Finset.mem_range.mp (Finset.mem_filter.mp hp).1
    have hpri : (p : Int) < R := by exact_mod_cast hpr
    exact rectangularTraceGram_valuation_of_classNumber_one Q D S R S p hsq hodd
      (hpri.trans hRcut) hclass
  have hnat := primePowerProduct_le_det P (fun p => 2*valuationWeight R S p) z hz hprime hlocal
  have hint : ((∏ p ∈ P,p^(2*valuationWeight R S p) : Nat) : Int) ≤ z := by
    have h : ((∏ p ∈ P,p^(2*valuationWeight R S p) : Nat) : Int) ≤ (z.natAbs : Int) := by
      exact_mod_cast hnat
    simpa only [Int.natCast_natAbs,abs_of_pos hz] using h
  have hreal : ((∏ p ∈ P,p^(2*valuationWeight R S p) : Nat) : Real) ≤ (z : Real) := by
    exact_mod_cast hint
  have hppos (p : Nat) (hp : p ∈ P) : (0 : Real) < p := by exact_mod_cast (hprime p hp).pos
  have hprodpos : (0 : Real) < ((∏ p ∈ P,p^(2*valuationWeight R S p) : Nat) : Real) := by
    exact_mod_cast Finset.prod_pos (fun p hp => pow_pos (hprime p hp).pos (2*valuationWeight R S p))
  have hlog := Real.log_le_log hprodpos hreal
  have he : Real.log ((∏ p ∈ P,p^(2*valuationWeight R S p) : Nat) : Real)=
      exactOddPrimeMass R S := by
    simp only [Nat.cast_prod,Nat.cast_pow]
    rw [Real.log_prod]
    · simp only [Real.log_pow,exactOddPrimeMass,P]
    · intro p hp
      exact (pow_pos (hppos p hp) _).ne'
  rw [he] at hlog
  exact hlog


/-- The existing point-count lemma is a conservative sufficient positivity
certificate; retain the public interface so all established callers and
field-level theorems continue to use their original assumptions. -/
theorem prime_mass_log_lower (Q : Finset (Int × Int)) (D R S : Nat)
    (hD : 0 < D) (hR : 1 ≤ R) (hS : 1 ≤ S)
    (hcard : 2*(R-1)+(S-1) < Q.card) [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hclass : NumberField.classNumber (QuadraticField (((D : Int)+1)/4))=1)
    (hRcut : (R : Int) < ((D : Int)+1)/4) :
    exactOddPrimeMass R S ≤ Real.log ((integerRectangularTraceGram Q D S R S).det : Real) := by
  exact prime_mass_log_lower_of_det_pos Q D R S hD hR hS
    (integer_det_positive Q D R S hD hR hS hcard) hsq hclass hRcut


/-- A genuine arithmetic/geometry meeting point: the original positive
integer Gram is simultaneously bounded below by the class-number-one
prime-mass theorem and above by the unchanged ordinary-jet radial estimate.
Any strict separation excludes that class number. The geometric positivity
witness can be Frobenius rank, not the old sufficient point-count guard. -/
theorem classNumber_ne_one_of_posDef_budget_gap
    (Q : Finset (Int × Int)) (D R S rho : Nat) (n : Real)
    (hD : 0 < D) (hR : 2 ≤ R) (hS : 1 ≤ S)
    (hRS : R ≤ 10000 * S)
    (hrho : 5 ≤ rho) (hRrho : rho < R)
    (hpos : ((RadialOperator.gram Q D S R S (rho^2/2 : Nat)).map
      (Int.castRingHom Real)).PosDef)
    (hnpos : 0 < n) (hn : (Q.card : Real) ≤ n)
    (hbound : ∀ q ∈ Q, ‖pairEval D q‖ ≤ rho)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hRcut : (R : Int) < ((D : Int)+1)/4)
    (hgap : enderUpperB R S S rho n <
      rawPrimeMassLower R S FirstEnderInterval.tailBudget) :
    NumberField.classNumber (QuadraticField (((D : Int)+1)/4)) ≠ 1 := by
  intro hclass
  have he :
      ((RadialOperator.gram Q D S R S (rho^2/2 : Nat)).map
        (Int.castRingHom Real)).det =
      ((integerRectangularTraceGram Q D S R S).det : Real) := by
    simpa only [RadialOperator.gram_det] using
      ((Int.castRingHom Real).map_det
        (RadialOperator.gram Q D S R S (rho^2/2 : Nat))).symm
  have hpositiveReal := hpos.det_pos
  rw [he] at hpositiveReal
  have hdet : 0 < (integerRectangularTraceGram Q D S R S).det := by
    exact_mod_cast hpositiveReal
  have hmass := prime_mass_log_lower_of_det_pos Q D R S hD
    (by omega) hS hdet hsq hclass hRcut
  have hraw := rawPrimeMassLower_le_certified R S FirstEnderInterval.tailBudget
  have htail := certifiedPrimeMassLower_antitone_tail R S hS
    FirstEnderInterval.tail_le_budget
  have hcert := certifiedPrimeMassLower_le_production R S
    (enderTailIntegral 10000) hR hS
  have hprod := enderPrimeMassLower_le_exact_production R S 10000
    hR hS (by decide) hRS
  have hlower :
      rawPrimeMassLower R S FirstEnderInterval.tailBudget ≤
      Real.log ((integerRectangularTraceGram Q D S R S).det : Real) :=
    hraw.trans (htail.trans (hcert.trans (hprod.trans hmass)))
  have hu := RadialDetBound.integer_log_upper_of_posDef
    Q D R S rho n hD (by omega) hS hrho hRrho hpos hnpos hn hbound
  have hp : 0 ≤
      (R-9*S : Nat)*(S : Real)*(S-1 : Nat)*Real.log (20/13 : Real) := by
    have hlog : 0 ≤ Real.log (20/13 : Real) :=
      Real.log_nonneg (by norm_num)
    positivity
  have hupper :
      Real.log ((integerRectangularTraceGram Q D S R S).det : Real) ≤
      enderUpperB R S S rho n := by
    linarith
  exact (not_lt_of_ge hlower) (lt_of_le_of_lt hupper hgap)

theorem recovered_normalized_lower (D : Nat) (hD : 41006250000 ≤ D) :
    (999997/1000000 : Real)*Real.log D-5739/1000 ≤
      recoveredPrimeMassLower (Tuned.R D) (Tuned.S D) FirstEnderInterval.tailBudget /
        comparisonScale (Tuned.R D) (Tuned.S D) := by
  obtain ⟨hS,h25,h26,h5⟩ := RadialDetBound.production_guards D hD
  have hh := strong_raw_normalized_add_gain_le_recovered (Tuned.R D) (Tuned.S D)
    FirstEnderInterval.tailBudget hS h25 h26
  linarith [Tuned.normalized_lower D hD]

theorem recovered_mass_le_actual_log (D : Nat) (hD : 41006250000 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hclass : NumberField.classNumber (QuadraticField (((D : Int)+1)/4))=1) :
    recoveredPrimeMassLower (Tuned.R D) (Tuned.S D) FirstEnderInterval.tailBudget ≤
      Real.log ((integerRectangularTraceGram (ellipsePairs D (Tuned.rho D)) D
        (Tuned.S D) (Tuned.R D) (Tuned.S D)).det : Real) := by
  have hd := Tuned.dimensions D hD
  have hs : 1 ≤ Tuned.S D := by omega
  have htail := certifiedPrimeMassLower_antitone_tail (Tuned.R D) (Tuned.S D) hs
    FirstEnderInterval.tail_le_budget
  have hrec : recoveredPrimeMassLower (Tuned.R D) (Tuned.S D) FirstEnderInterval.tailBudget ≤
      recoveredPrimeMassLower (Tuned.R D) (Tuned.S D) (enderTailIntegral 10000) := by
    unfold recoveredPrimeMassLower
    linarith
  have hprod := recoveredPrimeMassLower_le_production (Tuned.R D) (Tuned.S D)
    (enderTailIntegral 10000) (by omega) hs
  have hmass := enderPrimeMassLower_le_exact_production (Tuned.R D) (Tuned.S D) 10000
    (by omega) hs (by decide) hd.2.2.2.1
  have hc := ellipsePairs_card_gt_of_ender_radius D (Tuned.rho D)
    (3*Tuned.R D+Tuned.S D) (by omega) (by omega) (Tuned.chosen_radius D hD)
  have hcard : 2*(Tuned.R D-1)+(Tuned.S D-1) < (ellipsePairs D (Tuned.rho D)).card := by omega
  exact hrec.trans (hprod.trans (hmass.trans (prime_mass_log_lower (ellipsePairs D (Tuned.rho D))
    D (Tuned.R D) (Tuned.S D) (by omega) (by omega) hs hcard hsq hclass (Tuned.strict_inertness D))))

theorem endpoint_log_controls : (6931/10000 : Real) ≤ Real.log 2 ∧
    (1609/1000 : Real) ≤ Real.log 5 := by
  have h2c : checkPositiveLogBounds 4 2 1 (6931/10000) (6932/10000)=true := by
    norm_num [checkPositiveLogBounds,binaryLogLowerRat,binaryLogUpperRat,
      oddLogPrefixRat,oddLogRemainderRat,Finset.sum_range_succ]
  have h5c : checkPositiveLogBounds 4 5 2 (1609/1000) (161/100)=true := by
    norm_num [checkPositiveLogBounds,binaryLogLowerRat,binaryLogUpperRat,
      oddLogPrefixRat,oddLogRemainderRat,Finset.sum_range_succ]
  have h2 := (checkPositiveLogBounds_sound 4 2 1 (6931/10000) (6932/10000) h2c).1
  have h5 := (checkPositiveLogBounds_sound 4 5 2 (1609/1000) (161/100) h5c).1
  norm_num at h2 h5
  exact ⟨h2,h5⟩

theorem endpoint_log_lower (D : Nat) (hD : 48000000000 ≤ D) :
    (245813/10000 : Real) ≤ Real.log D := by
  have hb : (48000000000 : Real) ≤ D := by exact_mod_cast hD
  have hl := Real.log_le_log (by norm_num : (0 : Real) < 48000000000) hb
  have he : (48000000000 : Real)=2^13*3*5^9 := by norm_num
  rw [he,Real.log_mul (by norm_num : (2 : Real)^13*3 ≠ 0) (by norm_num : (5 : Real)^9 ≠ 0),
    Real.log_mul (by norm_num : (2 : Real)^13 ≠ 0) (by norm_num : (3 : Real) ≠ 0),
    Real.log_pow,Real.log_pow] at hl
  norm_num only [Nat.cast_ofNat] at hl
  linarith [endpoint_log_controls.1,endpoint_log_controls.2,recovery_log_controls.1]

/-- The new actual determinant upper and arithmetic lower are incompatible. -/
theorem odd_large_classNumber_ne_one_48b (D : Nat) (hD : 48000000000 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D) :
    NumberField.classNumber (QuadraticField (((D : Int)+1)/4))≠1 := by
  intro hc
  have hgeom : 41006250000 ≤ D := by omega
  have hd := Tuned.dimensions D hgeom
  have hp := comparisonScale_pos (Tuned.R D) (Tuned.S D) (by omega) (by omega)
  have hupper := RadialDetBound.production_normalized_upper D hgeom
  have hactual := div_le_div_of_nonneg_right (recovered_mass_le_actual_log D hgeom hsq hc) hp.le
  have hlower := recovered_normalized_lower D hgeom
  have hsep := RadialJetMajorant.endpoint_separation (Real.log D) (endpoint_log_lower D hD)
  linarith

theorem imaginaryQuadratic_large_classNumber_ne_one_48b (d : Nat)
    [Fact (0<d)] (hsq : Squarefree d) (hd : 48000000000 ≤ d) :
    NumberField.classNumber (ImaginaryQuadraticField d)≠1 := by
  rcases squarefree_mod_four_cases d hsq with ho | he
  · letI : Fact ((d : Int)%4=3) := ⟨ho⟩
    intro hc
    have hh := classNumber_one_of_field_equiv _ _ (quadraticChartEquiv d) hc
    exact odd_large_classNumber_ne_one_48b d hd hsq hh
  · letI : Fact ((d : Int)%4=1 ∨ (d : Int)%4=2) := ⟨he⟩
    exact even_classNumber_ne_one d hsq (by omega)

theorem imaginaryQuadratic_classNumber_one_discriminant_bound_48b
    (d : Nat) [Fact (0<d)] (hsq : Squarefree d)
    (hc : NumberField.classNumber (ImaginaryQuadraticField d)=1) :
    (NumberField.discr (ImaginaryQuadraticField d)).natAbs < 48000000000 := by
  have hrad : d < 48000000000 := by
    by_contra h
    exact imaginaryQuadratic_large_classNumber_ne_one_48b d hsq (by omega) hc
  rw [imaginaryQuadratic_discr_natAbs d hsq]
  rcases squarefree_mod_four_cases d hsq with ho | he
  · simpa [absoluteDiscriminantParameter,ho] using hrad
  · letI : Fact ((d : Int)%4=1 ∨ (d : Int)%4=2) := ⟨he⟩
    have hn := even_classNumber_one_only_one_or_two d hsq hc
    have hnot : ¬ (d : Int)%4=3 := by omega
    simp only [absoluteDiscriminantParameter,if_neg hnot]
    omega

/-- No caller-supplied generator: actual absolute discriminant of ANY such field. -/
theorem totallyComplex_degree_two_classNumber_one_discriminant_bound_48b
    (K : Type*) [Field K] [NumberField K] [NumberField.IsTotallyComplex K]
    (hdegree : Module.finrank Rat K=2) (hc : NumberField.classNumber K=1) :
    (NumberField.discr K).natAbs < 48000000000 := by
  obtain ⟨d,hd,hsq,a,ha⟩ := exists_squarefree_root_of_totallyComplex_degree_two K hdegree
  letI : Fact (0<d) := ⟨hd⟩
  let e := imaginaryQuadraticEquivOfRoot d K a ha hdegree
  have hcan := classNumber_one_of_field_equiv K (ImaginaryQuadraticField d) e.symm hc
  rw [NumberField.discr_eq_discr_of_algEquiv K e.symm]
  exact imaginaryQuadratic_classNumber_one_discriminant_bound_48b d hsq hcan

theorem endpoint_identity : (2 : Nat)^13*3*5^9=48000000000 := by norm_num

theorem negative_endpoint_control :
    ¬(4/5*(2458/100 : Real)-823/1000 < 999997/1000000*(2458/100)-5739/1000) := by
  exact RadialJetMajorant.negative_endpoint_control

theorem empty_prime_product_control (e : Nat → Nat) :
    (∏ p ∈ (∅ : Finset Nat),p^e p)=1 := by simp

theorem duplicate_prime_control : ¬ (3 : Int)^2 ∣ (3 : Int) := by norm_num

theorem actual_even_discriminant_control (d : Nat) [Fact (0<d)]
    (hsq : Squarefree d) (hd : d=1 ∨ d=2) :
    (NumberField.discr (ImaginaryQuadraticField d)).natAbs ≤ 8 := by
  rw [imaginaryQuadratic_discr_natAbs d hsq]
  rcases hd with rfl | rfl <;> norm_num [absoluteDiscriminantParameter]

end
end TenthDiscriminant.RadialCutoff
