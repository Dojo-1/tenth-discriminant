import TenthDiscriminant.SieveWheel

/-! Fixed Phase31 certificate. This initial part of the middle interval
does not stand in for the full interval up to the effective cutoff. -/
namespace TenthDiscriminant
set_option autoImplicit false

def millionPilotSurvivors : List Nat :=
  (intervalWheel (wheelMod millionWheelPrimes) (wheelResidues millionWheelPrimes)
    92 1000000).filter (fun d => guardedPrimeTests d millionExtraPrimes)

theorem millionPilotSurvivors_checked : millionPilotSurvivors=[163] := by decide +kernel

theorem millionWheel_candidate_count_control :
    (intervalWheel (wheelMod millionWheelPrimes) (wheelResidues millionWheelPrimes)
      92 1000000).length=3245 := by decide +kernel

theorem wheel_lift_translate_control : wheelLift 8 [3] 3=[19] := by decide +kernel

theorem wheel_halfopen_endpoint_control : intervalWheel 8 [3] 11 19=[11] := by decide +kernel

theorem wheel_omitted_quotient_control :
    (11 : Nat) ∉ ([3] : List Nat) ∧ 11 ∈ intervalWheel 8 [3] 11 19 := by decide +kernel

theorem wheel_omitted_residue_control :
    (163 : Nat) ∉ intervalWheel 9240 [] 92 1000000 := by decide +kernel

theorem millionPilot_retains_163_control : (163 : Nat) ∈ millionPilotSurvivors := by
  rw [millionPilotSurvivors_checked]
  simp

theorem classNumber_one_middle_below_million (d : Nat) [Fact (0 < d)]
    (hsq : Squarefree d) (hc : NumberField.classNumber (ImaginaryQuadraticField d)=1)
    (hlo : 92≤d) (hhi : d<1000000) : d=163 := by
  have hmod := imaginaryQuadratic_classNumber_one_mod_eight d hsq (by omega) hc
  have hm : d ∈ millionPilotSurvivors := List.mem_filter.mpr
    ⟨classNumber_one_mem_millionWheel d 1000000 hsq hc hlo hhi,
      guardedPrimeTests_of_classNumber_one d hsq hc hmod _ millionExtraPrimes_checked⟩
  simpa only [millionPilotSurvivors_checked, List.mem_singleton] using hm

theorem classNumber_one_candidates_below_million (d : Nat) [Fact (0 < d)]
    (hsq : Squarefree d) (hc : NumberField.classNumber (ImaginaryQuadraticField d)=1)
    (hhi : d<1000000) : d ∈ ([1,2,3,7,11,19,43,67,163] : List Nat) := by
  by_cases hd : d<92
  · have hm := classNumber_one_small_candidates d hsq hc hd
    simp only [List.mem_cons, List.not_mem_nil, or_false] at hm ⊢
    tauto
  · have heq := classNumber_one_middle_below_million d hsq hc (by omega) hhi
    simp [heq]

/-- The full remaining interval is explicit; this theorem does not supply
its certificate or the nine positive class-number equalities. -/
theorem classNumber_one_nine_candidates_of_upper_middle_certificate
    (extra : List Nat) (hextra : checkedOddPrimes extra=true)
    (hcertificate : ∀ d : Nat, 1000000≤d → d<700000000000 → d%8=3 →
      guardedPrimeTests d (crtBasePrimes++extra)=true → d=163)
    (d : Nat) [Fact (0 < d)] (hsq : Squarefree d)
    (hc : NumberField.classNumber (ImaginaryQuadraticField d)=1) :
    d ∈ ([1,2,3,7,11,19,43,67,163] : List Nat) := by
  by_cases hd : d<1000000
  · exact classNumber_one_candidates_below_million d hsq hc hd
  · have hhi := imaginaryQuadratic_classNumber_one_radicand_bound d hsq hc
    have hmod := imaginaryQuadratic_classNumber_one_mod_eight d hsq (by omega) hc
    have hp : checkedOddPrimes (crtBasePrimes++extra)=true := by
      rw [checkedOddPrimes_append, crtBasePrimes_checked, hextra]
      rfl
    have ht := guardedPrimeTests_of_classNumber_one d hsq hc hmod _ hp
    have heq := hcertificate d (by omega) hhi hmod ht
    simp [heq]

end TenthDiscriminant
