import TenthDiscriminant.FusedWheelBridge
import TenthDiscriminant.FusedWheelPrimes

/-! Connect a complete translate certificate to the ACTUAL class number.
This generic interface does not assert that a translate has been checked. -/
namespace TenthDiscriminant
set_option autoImplicit false

theorem phase35_moduli_positive :
    ((phase34Base++phase34Extra).all (fun e => decide (0<e.1)))=true := by decide +kernel

theorem phase35_base_primes : phase34Base.map Prod.fst=crtBasePrimes := by decide +kernel

private theorem phase35_positive (e : Nat×Nat) (he : e∈phase34Base++phase34Extra) : 0<e.1 :=
  of_decide_eq_true (List.all_eq_true.mp phase35_moduli_positive e he)

private theorem phase35_correct (e : Nat×Nat) (he : e∈phase34Base++phase34Extra) :
    e.2=negativeSquareMask e.1 := by
  have h : negativeSquareMask e.1=e.2 := by
    simpa only [beq_iff_eq] using List.all_eq_true.mp phase35_masks_checked e he
  exact h.symm

theorem phase35_classNumber_one_mem_wheel (d : Nat) [Fact (0<d)]
    (hsq : Squarefree d) (hc : NumberField.classNumber (ImaginaryQuadraticField d)=1)
    (hlo : 1000000≤d) : d%892371480∈maskWheelResidues phase34Base := by
  have hmod := imaginaryQuadratic_classNumber_one_mod_eight d hsq (by omega) hc
  have ht := guardedPrimeTests_of_classNumber_one d hsq hc hmod _ crtBasePrimes_checked
  have hr : d%wheelMod crtBasePrimes∈wheelResidues crtBasePrimes := by
    apply wheelResidues_cover crtBasePrimes (d := d) (hmod := hmod)
    · intro p hp
      have hpair : p.Prime ∧ p≠2 :=
        of_decide_eq_true (List.all_eq_true.mp crtBasePrimes_checked p hp)
      exact hpair.1.pos
    · intro p hp
      have htest := List.all_eq_true.mp ht p hp
      simpa only [guardedPrimeTests, guardedPrimeTest,
        if_pos (crtBasePrime_test_binds d p (by omega) hp), Bool.not_eq_true'] using htest
  rw [maskWheelResidues_eq phase34Base
    (fun e he => phase35_positive e (List.mem_append_left _ he))
    (fun e he => phase35_correct e (List.mem_append_left _ he)), phase35_base_primes]
  have hm : wheelMod crtBasePrimes=892371480 := by decide +kernel
  simpa only [hm] using hr

theorem phase35_classNumber_one_extra_tests (d : Nat) [Fact (0<d)]
    (hsq : Squarefree d) (hc : NumberField.classNumber (ImaginaryQuadraticField d)=1)
    (hlo : 1000000≤d) : maskTests d phase34Extra=true := by
  have hmod := imaginaryQuadratic_classNumber_one_mod_eight d hsq (by omega) hc
  rw [maskTests_eq d phase34Extra
    (fun e he => phase35_positive e (List.mem_append_right _ he))
    (fun e he => phase35_correct e (List.mem_append_right _ he))]
  exact guardedPrimeTests_of_classNumber_one d hsq hc hmod _ phase35_extra_primes_checked

theorem phase35_classNumber_ne_one_of_translate (k : Nat)
    (hcheck : maskTranslateClear (maskWheelResidues phase34Base)
      892371480 1000000 700000000000 k phase34Extra=true)
    (d : Nat) [Fact (0<d)] (hsq : Squarefree d)
    (hlo : 1000000≤d) (hhi : d<700000000000) (hq : d/892371480=k) :
    NumberField.classNumber (ImaginaryQuadraticField d)≠1 := by
  intro hc
  have hr := phase35_classNumber_one_mem_wheel d hsq hc hlo
  have ht := phase35_classNumber_one_extra_tests d hsq hc hlo
  have heq : d%892371480+892371480*k=d := by
    rw [←hq]
    exact Nat.mod_add_div d 892371480
  have hb := maskTranslateClear_excludes _ _ _ _ k (d%892371480) phase34Extra
    hcheck hr (by simpa only [heq] using hlo) (by simpa only [heq] using hhi)
  rw [heq, ht] at hb
  contradiction

end TenthDiscriminant
