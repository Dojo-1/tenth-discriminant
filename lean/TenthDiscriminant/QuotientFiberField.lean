import TenthDiscriminant.QuotientFiberChecked
import TenthDiscriminant.QuotientFiberParameters
import TenthDiscriminant.FusedWheelFieldBridge

/-! The FULL original interval is reduced to one complete all-fiber
certificate. This module does not assert that certificate has passed. -/
namespace TenthDiscriminant
set_option autoImplicit false

theorem phase36_moduli_eq :
    phase36Entries.map QuotientPattern.modulus=phase34Extra.map Prod.fst := by decide +kernel

theorem phase36_prime_bounds :
    phase34Extra.all (fun e => decide (4*e.1≤1000000))=true := by decide +kernel

theorem quotient_classNumber_one_retains (d : Nat) [Fact (0<d)]
    (hsq : Squarefree d) (hc : NumberField.classNumber (ImaginaryQuadraticField d)=1)
    (hlo : 1000000≤d) (hhi : d<700000000000) :
    (quotientFilter (d%892371480) (quotientInitial (d%892371480)) phase36Entries).testBit
      (d/892371480)=true := by
  have heq : d%892371480+892371480*(d/892371480)=d := Nat.mod_add_div d _
  have hmod := imaginaryQuadratic_classNumber_one_mod_eight d hsq (by omega) hc
  have hps : checkedOddPrimes (phase36Entries.map QuotientPattern.modulus)=true := by
    rw [phase36_moduli_eq]
    exact phase35_extra_primes_checked
  have ht := guardedPrimeTests_of_classNumber_one d hsq hc hmod _ hps
  apply quotient_full_range_retains
  · exact Nat.mod_lt _ (by decide)
  · simpa only [heq] using hlo
  · simpa only [heq] using hhi
  · exact phase36_patterns_checked
  · intro e he
    have hm : e.modulus∈phase34Extra.map Prod.fst := by
      rw [←phase36_moduli_eq]
      exact List.mem_map.mpr ⟨e,he,rfl⟩
    obtain ⟨old, hold, hp⟩ := List.mem_map.mp hm
    have hb : 4*old.1≤1000000 :=
      of_decide_eq_true (List.all_eq_true.mp phase36_prime_bounds old hold)
    have hbind : 4*e.modulus≤d := by omega
    have htest := List.all_eq_true.mp ht e.modulus (List.mem_map.mpr ⟨e,he,rfl⟩)
    simpa only [heq, guardedPrimeTest, if_pos hbind, Bool.not_eq_true'] using htest

theorem quotient_classNumber_ne_one_of_all_fibers
    (hcert : phase35Seeds.all phase36Seed=true)
    (d : Nat) [Fact (0<d)] (hsq : Squarefree d)
    (hlo : 1000000≤d) (hhi : d<700000000000) :
    NumberField.classNumber (ImaginaryQuadraticField d)≠1 := by
  intro hc
  have hr := phase35_classNumber_one_mem_wheel d hsq hc hlo
  change phase35Seeds.all (fun seed => maskWheelVisit phase35Prefix 184 seed phase36Leaf)=true at hcert
  rw [phase35_partition] at hcert
  have hleaf := List.all_eq_true.mp hcert (d%892371480) hr
  have hz : quotientFilter (d%892371480) (quotientInitial (d%892371480)) phase36Entries=0 := by
    simpa only [phase36Leaf, beq_iff_eq] using hleaf
  have hb := quotient_classNumber_one_retains d hsq hc hlo hhi
  rw [hz] at hb
  simp at hb

end TenthDiscriminant
