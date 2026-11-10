import TenthDiscriminant.Phase269Finite321Data

/-!
# Phase269: exhaustive local-to-global transport at a fixed CRT period through the merged 322^4 endpoint

The only data-specific global premise is that ALL nine seed checks hold.
The result does not import the existing nine-field classification.
The guard for 164 <= d <= 436 is checked separately, because the last
tested prime 109 is not always below d/4 there.
-/
namespace TenthDiscriminant.Phase269
set_option autoImplicit false

theorem wheel269_mod : wheelMod basePrimes269 = wheel269 := by decide +kernel
theorem base269_primes_checked : checkedOddPrimes basePrimes269 = true := by decide +kernel
theorem base269_subset :
    basePrimes269.all (fun p => decide (p ∈ finite321Primes)) = true := by decide +kernel
theorem base269_bound :
    basePrimes269.all (fun p => decide (p ≤ 19)) = true := by decide +kernel
theorem base269_positive :
    base269.all (fun e => decide (0 < e.1)) = true := by decide +kernel
theorem base269_masks :
    base269.all (fun e => decide (e.2 = negativeSquareMask e.1)) = true := by decide +kernel

theorem extra269_subset :
    extraPrimes269.all (fun p => decide (p ∈ finite321Primes)) = true := by decide +kernel
theorem extra269_bound :
    extraPrimes269.all (fun p => decide (p ≤ 109)) = true := by decide +kernel
theorem entries269_moduli :
    entries269.map QuotientPattern.modulus = extraPrimes269 := by decide +kernel

theorem chunk0_checked :
    quotientPatternsCheck wheel269 entries269Chunk0 = true := by decide +kernel
theorem chunk1_checked :
    quotientPatternsCheck wheel269 entries269Chunk1 = true := by decide +kernel
theorem chunk2_checked :
    quotientPatternsCheck wheel269 entries269Chunk2 = true := by decide +kernel

theorem entries269_checked : quotientPatternsCheck wheel269 entries269 = true := by
  simp only [entries269, quotientPatternsCheck_append,
    chunk0_checked, chunk1_checked, chunk2_checked, Bool.and_self]

/-- Every source member satisfying the original base guards reaches the
same bit position in the full wheel; no assumption about d being prime. -/
theorem in_wheel269 (d : Nat) (hbig : 437 ≤ d) (hmod : d % 8 = 3)
    (htests : guardedPrimeTests d finite321Primes = true) :
    d % wheel269 ∈ maskWheelResidues base269 := by
  have hplain : d % wheelMod basePrimes269 ∈ wheelResidues basePrimes269 := by
    apply wheelResidues_cover basePrimes269
    · intro p hp
      have hpair : p.Prime ∧ p ≠ 2 :=
        of_decide_eq_true ((List.all_eq_true.mp base269_primes_checked) p hp)
      exact hpair.1.pos
    · exact hmod
    · intro p hp
      have hmem : p ∈ finite321Primes :=
        of_decide_eq_true ((List.all_eq_true.mp base269_subset) p hp)
      have hmax : p ≤ 19 :=
        of_decide_eq_true ((List.all_eq_true.mp base269_bound) p hp)
      have hb : 4 * p ≤ d := by omega
      have htest := (List.all_eq_true.mp htests) p hmem
      simpa only [guardedPrimeTest, if_pos hb, Bool.not_eq_true'] using htest
  have hpos : ∀ e ∈ base269, 0 < e.1 := by
    intro e he
    exact of_decide_eq_true ((List.all_eq_true.mp base269_positive) e he)
  have hm : ∀ e ∈ base269, e.2 = negativeSquareMask e.1 := by
    intro e he
    exact of_decide_eq_true ((List.all_eq_true.mp base269_masks) e he)
  rw [maskWheelResidues_eq base269 hpos hm]
  simpa only [basePrimes269, wheel269_mod] using hplain

/-- All suffix moduli are now inside the valid d/4 inertness range. -/
theorem suffix269_no_root (d : Nat) (hbig : 437 ≤ d)
    (htests : guardedPrimeTests d finite321Primes = true) :
    ∀ e ∈ entries269, modularRootTest d e.modulus = false := by
  intro e he
  have hm : e.modulus ∈ extraPrimes269 := by
    rw [← entries269_moduli]
    exact List.mem_map.mpr ⟨e, he, rfl⟩
  have hin : e.modulus ∈ finite321Primes :=
    of_decide_eq_true ((List.all_eq_true.mp extra269_subset) e.modulus hm)
  have hmax : e.modulus ≤ 109 :=
    of_decide_eq_true ((List.all_eq_true.mp extra269_bound) e.modulus hm)
  have hbind : 4 * e.modulus ≤ d := by omega
  have ht := (List.all_eq_true.mp htests) e.modulus hin
  simpa only [guardedPrimeTest, if_pos hbind, Bool.not_eq_true'] using ht

/-- Exact quotient band with all endpoint cases: no missing or phantom
index at k=0 or k=273. -/
theorem initial269_bit (r k : Nat) (hr : r < wheel269) :
    (initial269 r).testBit k = true ↔
      437 ≤ r + wheel269 * k ∧ r + wheel269 * k < (322 : Nat)^4 := by
  unfold initial269
  rw [quotientBand_testBit _ _ _ (by split_ifs <;> omega)]
  unfold wheel269 at *
  split_ifs <;> omega

/-- The small interval is a separate kernel computation, so no
spurious inertness at p >= d/4 is ever imposed. -/
theorem small269_checked :
    (List.range 273).all (fun t =>
      if (164 + t) % 8 = 3 then
        !guardedPrimeTests (164 + t) finite321Primes else true) = true := by
  decide +kernel

theorem small269_false (d : Nat) (hlo : 163 < d)
    (hhi : d < 437) (hmod : d % 8 = 3) :
    guardedPrimeTests d finite321Primes = false := by
  have hk : d - 164 ∈ List.range 273 := List.mem_range.mpr (by omega)
  have hb := (List.all_eq_true.mp small269_checked) (d - 164) hk
  have heq : 164 + (d - 164) = d := by omega
  simpa only [heq, if_pos hmod, Bool.not_eq_true'] using hb

/-- The nine subtrees partition every residue of the base CRT wheel.
A proof of each subtree is needed, not merely nine sample points. -/
theorem partition269 :
    seeds269.all seed269 = (maskWheelResidues base269).all leaf269 := by
  change seeds269.all
    (fun seed => maskWheelVisit prefix269 152 seed leaf269) =
      (maskWheelResidues base269).all leaf269
  rw [maskWheelVisit_all]
  rfl

/-- Close the bounded finite claim given actual exhaustive nine-seed
kernel checks. No class-number theorem or classification conclusion is used. -/
theorem finite269_of_all_seeds
    (hblocks : seeds269.all seed269 = true) :
    ∀ d : Nat, 163 < d → d < (322 : Nat)^4 → d % 8 = 3 →
      guardedPrimeTests d finite321Primes = false := by
  intro d hlo hhi hmod
  by_cases hsmall : d < 437
  · exact small269_false d hlo hsmall hmod
  · have hbig : 437 ≤ d := by omega
    cases htests : guardedPrimeTests d finite321Primes with
    | false => rfl
    | true =>
      have hw := in_wheel269 d hbig hmod htests
      have hall : (maskWheelResidues base269).all leaf269 = true := by
        rw [← partition269]
        exact hblocks
      have hleaf : leaf269 (d % wheel269) = true :=
        (List.all_eq_true.mp hall) (d % wheel269) hw
      have hdqr : d % wheel269 + wheel269 * (d / wheel269) = d :=
        Nat.mod_add_div d wheel269
      have hr : d % wheel269 < wheel269 :=
        Nat.mod_lt d (by decide)
      have hstart : (initial269 (d % wheel269)).testBit (d / wheel269) = true := by
        apply (initial269_bit _ _ hr).mpr
        simpa only [hdqr] using (show 437 ≤ d ∧ d < (322 : Nat)^4 from ⟨hbig,hhi⟩)
      have hk : d / wheel269 < 785 := by
        apply (Nat.div_lt_iff_lt_mul (by decide : 0 < wheel269)).mpr
        unfold wheel269
        omega
      have hno : ∀ e ∈ entries269,
          modularRootTest (d % wheel269 + wheel269 * (d / wheel269)) e.modulus = false := by
        simpa only [hdqr] using suffix269_no_root d hbig htests
      have hret := quotientFilter_retains wheel269 (d % wheel269)
        (d / wheel269) (initial269 (d % wheel269)) entries269
        hk (quotientPatternsCheck_sound _ _ entries269_checked) hno hstart
      have hz : quotientFilter (d % wheel269) (initial269 (d % wheel269))
          entries269 = 0 := by
        simpa only [leaf269, beq_iff_eq] using hleaf
      rw [hz] at hret
      simp at hret

end TenthDiscriminant.Phase269
