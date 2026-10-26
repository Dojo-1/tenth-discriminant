import TenthDiscriminant.QuotientFiberField

/-! A stronger all-quotient certificate can discharge an old q0 statement
without recomputing it. These implications do not supply a certificate. -/
namespace TenthDiscriminant
set_option autoImplicit false

theorem quotient_old_test_no_roots (r : Nat) (hlo : 1000000≤r)
    (ht : maskTests r phase34Extra=true) :
    ∀ e∈phase36Entries, modularRootTest r e.modulus=false := by
  intro e he
  have hm : e.modulus∈phase34Extra.map Prod.fst := by
    rw [←phase36_moduli_eq]
    exact List.mem_map.mpr ⟨e,he,rfl⟩
  obtain ⟨old, hold, hlabel⟩ := List.mem_map.mp hm
  have hb : 4*old.1≤1000000 :=
    of_decide_eq_true (List.all_eq_true.mp phase36_prime_bounds old hold)
  have hp : 0<old.1 := by
    have hv := (quotientPatternsCheck_sound _ _ phase36_patterns_checked e he).1
    omega
  have hmask : negativeSquareMask old.1=old.2 := by
    simpa only [beq_iff_eq] using
      List.all_eq_true.mp phase35_masks_checked old (List.mem_append_right _ hold)
  have htest := List.all_eq_true.mp ht old hold
  rw [maskGuardedTest, if_pos (by omega : 4*old.1≤r), ←hmask, maskRootTest_eq r old.1 hp] at htest
  have hn : modularRootTest r old.1=false := by simpa only [Bool.not_eq_true'] using htest
  simpa only [hlabel] using hn

theorem quotient_leaf_implies_q0 (r : Nat) (hc : phase36Leaf r=true) : phase35Leaf 0 r=true := by
  have hz : quotientFilter r (quotientInitial r) phase36Entries=0 := by
    simpa only [phase36Leaf, beq_iff_eq] using hc
  by_cases hr : 1000000≤r ∧ r<700000000000
  · have hi : (quotientInitial r).testBit 0=true := by
      unfold quotientInitial
      rw [if_neg (by omega : ¬r<1000000)]
      split_ifs <;> decide +kernel
    by_cases ht : maskTests r phase34Extra=true
    · have hno := quotient_old_test_no_roots r hr.1 ht
      have hbit := quotientFilter_retains 892371480 r 0 (quotientInitial r) phase36Entries
        (by decide) (quotientPatternsCheck_sound _ _ phase36_patterns_checked)
        (by simpa only [Nat.mul_zero,Nat.add_zero] using hno) hi
      rw [hz] at hbit
      simp at hbit
    · have hf : maskTests r phase34Extra=false := Bool.eq_false_of_not_eq_true ht
      simp [phase35Leaf, hr, hf]
  · simp [phase35Leaf, hr]

theorem maskWheelVisit_eq_single_all (es : List (Nat×Nat)) (m seed : Nat) (f : Nat→Bool) :
    maskWheelVisit es m seed f=(maskWheelFromList es m [seed]).all f := by
  simpa only [List.all_cons,List.all_nil,Bool.and_true] using maskWheelVisit_all es m [seed] f

theorem maskWheelVisit_mono (es : List (Nat×Nat)) (m seed : Nat) (f g : Nat→Bool)
    (hfg : ∀ r, f r=true → g r=true) (hc : maskWheelVisit es m seed f=true) :
    maskWheelVisit es m seed g=true := by
  rw [maskWheelVisit_eq_single_all] at hc ⊢
  exact List.all_eq_true.mpr (fun r hr => hfg r (List.all_eq_true.mp hc r hr))

theorem quotient_old_seed_of_full (seed : Nat) (hc : phase36Seed seed=true) :
    phase35Block 0 seed=true := by
  exact maskWheelVisit_mono phase35Prefix 184 seed phase36Leaf (phase35Leaf 0)
    quotient_leaf_implies_q0 hc

end TenthDiscriminant
