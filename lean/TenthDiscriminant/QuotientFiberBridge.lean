import TenthDiscriminant.ResidueMaskBridge
import TenthDiscriminant.QuotientFiberCore

/-! Pull a local root constraint back along k -> r+M*k, and preserve every
surviving k-bit through intersections. No concrete full-range claim here. -/
namespace TenthDiscriminant
set_option autoImplicit false

theorem periodicBits_testBit (p mask width k : Nat) :
    (periodicBits p mask width).testBit k=true ↔
      k<width ∧ mask.testBit (k%p)=true := by
  rw [periodicBits, residueBits_testBit]
  simp only [List.mem_filter, List.mem_range, and_comm]

theorem periodicBits_testBit_eq (p mask width k : Nat) (hk : k<width) :
    (periodicBits p mask width).testBit k=mask.testBit (k%p) := by
  apply Bool.eq_iff_iff.mpr
  rw [periodicBits_testBit]
  simp only [hk, true_and]

private theorem fiber_mod_zero_iff_cast (n p : Nat) : n%p=0 ↔ (n : ZMod p)=0 := by
  constructor
  · intro h
    exact (CharP.cast_eq_zero_iff (ZMod p) p n).2 (Nat.dvd_of_mod_eq_zero h)
  · intro h
    exact Nat.mod_eq_zero_of_dvd ((CharP.cast_eq_zero_iff (ZMod p) p n).1 h)

theorem affine_root_zero_iff (M a t r k p : Nat) (hu : M*a%p=1) :
    (t*t+(r+M*k))%p=0 ↔ (a*(t*t)+(k+a*r))%p=0 := by
  have hu' : ((M*a : Nat) : ZMod p)=1 := by
    calc
      ((M*a : Nat) : ZMod p)=(((M*a)%p : Nat) : ZMod p) := (ZMod.natCast_mod _ _).symm
      _=1 := by rw [hu]; simp
  have hunit : (M : ZMod p)*(a : ZMod p)=1 := by simpa only [Nat.cast_mul] using hu'
  rw [fiber_mod_zero_iff_cast, fiber_mod_zero_iff_cast]
  push_cast
  constructor
  · intro h
    linear_combination (a : ZMod p)*h-(k : ZMod p)*hunit
  · intro h
    linear_combination (M : ZMod p)*h-((t : ZMod p)*(t : ZMod p)+(r : ZMod p))*hunit

theorem scaledNegativeMask_eq (M a r k p : Nat) (hp : 0<p) (hu : M*a%p=1) :
    (scaledNegativeMask p a).testBit ((k+a*r)%p)=modularRootTest (r+M*k) p := by
  apply Bool.eq_iff_iff.mpr
  rw [scaledNegativeMask, residueBits_testBit]
  simp only [List.mem_map, List.mem_range, modularRootTest, List.any_eq_true, beq_iff_eq]
  constructor
  · rintro ⟨t, ht, heq⟩
    refine ⟨t, ht, ?_⟩
    exact (affine_root_zero_iff M a t r k p hu).mpr
      ((negative_residue_iff (a*(t*t)) (k+a*r) p hp).mpr heq)
  · rintro ⟨t, ht, heq⟩
    refine ⟨t, ht, ?_⟩
    exact (negative_residue_iff (a*(t*t)) (k+a*r) p hp).mp
      ((affine_root_zero_iff M a t r k p hu).mp heq)

theorem quotientWide_shift_eq (M a r k p : Nat) (hp : 0<p) (hu : M*a%p=1)
    (hk : k<785) :
    (quotientWidePattern p a >>> ((a*r)%p)).testBit k= !modularRootTest (r+M*k) p := by
  rw [Nat.testBit_shiftRight]
  have ho := Nat.mod_lt (a*r) hp
  rw [quotientWidePattern, periodicBits_testBit_eq p _ _ _ (by omega)]
  have hidx : ((a*r)%p+k)%p=(k+a*r)%p := by simp [Nat.add_mod, Nat.add_comm]
  rw [hidx, scaledAllowedMask, Nat.testBit_xor, Nat.testBit_two_pow_sub_one]
  have hj := Nat.mod_lt (k+a*r) hp
  rw [scaledNegativeMask_eq M a r k p hp hu]
  cases hb : modularRootTest (r+M*k) p <;> simp [hj]

theorem quotientBand_testBit (lo hi k : Nat) (hle : lo≤hi) :
    (quotientBand lo hi).testBit k=true ↔ lo≤k ∧ k<hi := by
  rw [quotientBand, Nat.testBit_shiftLeft, Nat.testBit_two_pow_sub_one]
  simp only [Bool.and_eq_true_iff, decide_eq_true_eq]
  omega

theorem quotientInitial_testBit (r k : Nat) (hr : r<892371480) :
    (quotientInitial r).testBit k=true ↔
      1000000≤r+892371480*k ∧ r+892371480*k<700000000000 := by
  unfold quotientInitial
  rw [quotientBand_testBit _ _ _ (by split_ifs <;> omega)]
  split_ifs <;> omega

theorem quotientFilter_retains (M r k current : Nat) (es : List QuotientPattern)
    (hk : k<785)
    (hvalid : ∀ e∈es, 0<e.modulus ∧ M*e.inverse%e.modulus=1 ∧
      e.wide=quotientWidePattern e.modulus e.inverse)
    (hno : ∀ e∈es, modularRootTest (r+M*k) e.modulus=false)
    (hbit : current.testBit k=true) :
    (quotientFilter r current es).testBit k=true := by
  induction es generalizing current with
  | nil => exact hbit
  | cons e es ih =>
    have hn : current≠0 := by intro h; simp [h] at hbit
    rw [quotientFilter, if_neg hn]
    apply ih
    · intro q hq
      exact hvalid q (List.mem_cons_of_mem e hq)
    · intro q hq
      exact hno q (List.mem_cons_of_mem e hq)
    · obtain ⟨hp, hu, hw⟩ := hvalid e List.mem_cons_self
      rw [Nat.testBit_and, hbit, hw, quotientWide_shift_eq M e.inverse r k e.modulus hp hu hk,
        hno e List.mem_cons_self]
      rfl

theorem quotient_empty_filter_control : quotientFilter 163 7 []=7 := by rfl

theorem quotientFilter_bit_subset (r k current : Nat) (es : List QuotientPattern)
    (hbit : (quotientFilter r current es).testBit k=true) : current.testBit k=true := by
  induction es generalizing current with
  | nil => exact hbit
  | cons e es ih =>
    by_cases hz : current=0
    · simp [quotientFilter, hz] at hbit
    · rw [quotientFilter, if_neg hz] at hbit
      have h := ih _ hbit
      rw [Nat.testBit_and] at h
      exact (Bool.and_eq_true_iff.mp h).1

theorem quotientPatternsCheck_sound (M : Nat) (es : List QuotientPattern)
    (hc : quotientPatternsCheck M es=true) :
    ∀ e∈es, 0<e.modulus ∧ M*e.inverse%e.modulus=1 ∧
      e.wide=quotientWidePattern e.modulus e.inverse := by
  intro e he
  have h := List.all_eq_true.mp hc e he
  simpa only [quotientPatternCheck, Bool.and_eq_true_iff, decide_eq_true_eq,
    beq_iff_eq, and_assoc] using h

theorem quotientPatternsCheck_append (M : Nat) (xs ys : List QuotientPattern) :
    quotientPatternsCheck M (xs++ys)=
      (quotientPatternsCheck M xs && quotientPatternsCheck M ys) := by
  simp only [quotientPatternsCheck, List.all_append]

theorem quotient_full_range_retains (r k : Nat) (es : List QuotientPattern)
    (hr : r<892371480) (hlo : 1000000≤r+892371480*k)
    (hhi : r+892371480*k<700000000000)
    (hc : quotientPatternsCheck 892371480 es=true)
    (hno : ∀ e∈es, modularRootTest (r+892371480*k) e.modulus=false) :
    (quotientFilter r (quotientInitial r) es).testBit k=true := by
  apply quotientFilter_retains 892371480 r k (quotientInitial r) es
    (by omega) (quotientPatternsCheck_sound _ _ hc) hno
  exact (quotientInitial_testBit r k hr).mpr ⟨hlo,hhi⟩

theorem quotientFilter_no_phantom_bits (r k : Nat) (es : List QuotientPattern)
    (hr : r<892371480) (hk : 785≤k) :
    (quotientFilter r (quotientInitial r) es).testBit k=false := by
  cases h : (quotientFilter r (quotientInitial r) es).testBit k with
  | false => rfl
  | true =>
    have hi := quotientFilter_bit_subset r k (quotientInitial r) es h
    have hb := (quotientInitial_testBit r k hr).mp hi
    omega

theorem quotient_affine_controls :
    (quotientWidePattern 29 3 >>> 25).testBit 0=true ∧
    (quotientWidePattern 29 3 >>> 25).testBit 1=false ∧
    (quotientWidePattern 29 3 >>> 4).testBit 1=true ∧
    quotientPatternCheck 892371480 ⟨29,0,0⟩=false ∧
    quotientPatternCheck 892371480 ⟨3,1,0⟩=false := by decide +kernel
theorem quotient_initial_controls :
    (quotientInitial 163).testBit 0=false ∧
    (quotientInitial 1000000).testBit 0=true ∧
    (quotientInitial 380759680).testBit 784=false ∧
    (quotientInitial 380759679).testBit 784=true ∧
    (quotientInitial 3).testBit 785=false := by decide +kernel

end TenthDiscriminant
