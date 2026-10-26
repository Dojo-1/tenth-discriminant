import TenthDiscriminant.SieveWheel
import TenthDiscriminant.ResidueMaskCore
import Mathlib.Data.Nat.Bitwise

/-! A computational change of coordinates, not a new arithmetic criterion.
Each root search and its bit query have identical Boolean meaning. -/
namespace TenthDiscriminant
set_option autoImplicit false

theorem residueBits_testBit (rs : List Nat) (t : Nat) :
    (residueBits rs).testBit t=true ↔ t∈rs := by
  induction rs with
  | nil => simp [residueBits]
  | cons r rs ih =>
    rw [residueBits, List.mem_cons, Nat.testBit_or, Nat.testBit_two_pow]
    simp only [Bool.or_eq_true, decide_eq_true_eq, ih]
    tauto

theorem negative_residue_iff (a d p : Nat) (hp : 0<p) :
    (a+d)%p=0 ↔ (p-a%p)%p=d%p := by
  rw [Nat.add_mod]
  have ha := Nat.mod_lt a hp
  have hd := Nat.mod_lt d hp
  by_cases hzero : a%p=0
  · simp [hzero, eq_comm]
  · have hneg : p-a%p<p := by omega
    rw [Nat.mod_eq_of_lt hneg]
    by_cases hs : a%p+d%p<p
    · rw [Nat.mod_eq_of_lt hs]
      omega
    · rw [Nat.mod_eq_sub_mod (by omega : p≤a%p+d%p)]
      rw [Nat.mod_eq_of_lt (by omega : a%p+d%p-p<p)]
      omega

/-- Uniform in d and p; primality is not needed for representation change.
The positive-modulus hypothesis excludes the empty root list at p=0. -/
theorem maskRootTest_eq (d p : Nat) (hp : 0<p) :
    maskRootTest d p (negativeSquareMask p)=modularRootTest d p := by
  apply Bool.eq_iff_iff.mpr
  rw [maskRootTest, negativeSquareMask, residueBits_testBit]
  simp only [List.mem_map, List.mem_range, modularRootTest, List.any_eq_true,
    beq_iff_eq]
  constructor
  · rintro ⟨r, hr, heq⟩
    exact ⟨r, hr, (negative_residue_iff (r*r) d p hp).mpr heq⟩
  · rintro ⟨r, hr, heq⟩
    exact ⟨r, hr, (negative_residue_iff (r*r) d p hp).mp heq⟩

theorem maskGuardedTest_eq (d p : Nat) (hp : 0<p) :
    maskGuardedTest d p (negativeSquareMask p)=guardedPrimeTest d p := by
  simp [maskGuardedTest, guardedPrimeTest, maskRootTest_eq d p hp]

theorem maskTests_eq (d : Nat) (es : List (Nat×Nat))
    (hp : ∀ e∈es, 0<e.1)
    (hm : ∀ e∈es, e.2=negativeSquareMask e.1) :
    maskTests d es=guardedPrimeTests d (es.map Prod.fst) := by
  have heq : ∀ e∈es, maskGuardedTest d e.1 e.2=guardedPrimeTest d e.1 := by
    intro e he
    rw [hm e he]
    exact maskGuardedTest_eq d e.1 (hp e he)
  apply Bool.eq_iff_iff.mpr
  simp only [maskTests, guardedPrimeTests, List.all_map, List.all_eq_true,
    Function.comp_apply]
  constructor
  · intro h e he
    rw [←heq e he]
    exact h e he
  · intro h e he
    rw [heq e he]
    exact h e he

theorem maskWheelMod_eq (es : List (Nat×Nat)) :
    maskWheelMod es=wheelMod (es.map Prod.fst) := by
  induction es with
  | nil => rfl
  | cons e es ih => simp only [maskWheelMod, List.map_cons, wheelMod, ih]

/-- The fast wheel has exactly the old list, not merely the same length.
Thus the old no-loss coverage proof can be reused without trusting a generator. -/
theorem maskWheelResidues_eq (es : List (Nat×Nat))
    (hp : ∀ e∈es, 0<e.1)
    (hm : ∀ e∈es, e.2=negativeSquareMask e.1) :
    maskWheelResidues es=wheelResidues (es.map Prod.fst) := by
  induction es with
  | nil => rfl
  | cons e es ih =>
    have ih' := ih (fun q hq => hp q (List.mem_cons_of_mem e hq))
      (fun q hq => hm q (List.mem_cons_of_mem e hq))
    simp only [maskWheelResidues, List.map_cons, wheelResidues, wheelLift,
      maskWheelMod_eq, ih', hm e List.mem_cons_self]
    congr 1
    funext d
    rw [maskRootTest_eq d e.1 (hp e List.mem_cons_self)]

theorem mask_nonprime_controls :
    negativeSquareMask 1=1 ∧ negativeSquareMask 4=9 := by decide +kernel

theorem mask_zero_residue_control : maskRootTest 9 3 (negativeSquareMask 3)=true := by
  decide +kernel

theorem mask_mutation_control :
    maskRootTest 3 3 0≠modularRootTest 3 3 := by decide +kernel

theorem mask_zero_modulus_control :
    maskRootTest 0 0 1≠modularRootTest 0 0 := by decide +kernel

theorem mask_strict_endpoint_control :
    maskGuardedTest 163 41 (negativeSquareMask 41)=true ∧
    maskRootTest 163 41 (negativeSquareMask 41)=true := by decide +kernel

/-- A checked translate excludes every in-range member. Whole-range use
still needs all quotient indices and complete wheel coverage. -/
theorem maskTranslateClear_excludes (rs : List Nat) (period lo hi k r : Nat)
    (es : List (Nat×Nat))
    (hc : maskTranslateClear rs period lo hi k es=true)
    (hr : r∈rs) (hlo : lo≤r+period*k) (hhi : r+period*k<hi) :
    maskTests (r+period*k) es=false := by
  have h := List.all_eq_true.mp hc r hr
  simpa only [hlo, hhi, and_self, ↓reduceIte, Bool.not_eq_true'] using h

end TenthDiscriminant
