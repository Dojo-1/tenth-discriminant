import TenthDiscriminant.PrimeTail

/-!
# Finite rational enclosures from the odd-power logarithm series

The remainder is proved by domination of the shifted series by a geometric
series. A truncated positive sum alone is not an upper bound.
-/

namespace TenthDiscriminant
set_option autoImplicit false
noncomputable section

def oddLogTerm (z : Real) (k : Nat) : Real :=
  2 * (1 / (2 * (k : Real) + 1)) * z ^ (2 * k + 1)

def oddLogPrefix (N : Nat) (z : Real) : Real := ∑ k ∈ Finset.range N, oddLogTerm z k

def oddLogRemainder (N : Nat) (z : Real) : Real :=
  2 * z ^ (2 * N + 1) / ((2 * (N : Real) + 1) * (1 - z ^ 2))

theorem oddLog_hasSum (z : Real) (hz : 0 ≤ z) (hzlt : z < 1) :
    HasSum (oddLogTerm z) (Real.log (1 + z) - Real.log (1 - z)) := by
  exact Real.hasSum_log_sub_log_of_abs_lt_one (by simpa [abs_of_nonneg hz])

theorem oddLogPrefix_le (N : Nat) (z : Real) (hz : 0 ≤ z) (hzlt : z < 1) :
    oddLogPrefix N z ≤ Real.log (1 + z) - Real.log (1 - z) := by
  exact sum_le_hasSum (Finset.range N) (fun k hk => by unfold oddLogTerm; positivity)
    (oddLog_hasSum z hz hzlt)

theorem oddLog_tail_term_le (N k : Nat) (z : Real) (hz : 0 ≤ z) :
    oddLogTerm z (k + N) ≤
      (2 * (1 / (2 * (N : Real) + 1)) * z ^ (2 * N + 1)) * (z ^ 2) ^ k := by
  have hcoeff : (1 : Real) / (2 * ((k + N : Nat) : Real) + 1) ≤
      1 / (2 * (N : Real) + 1) := by
    apply one_div_le_one_div_of_le (by positivity)
    push_cast
    have hk : (0 : Real) ≤ (k : Real) := Nat.cast_nonneg k
    linarith
  have hexp : 2 * (k + N) + 1 = (2 * N + 1) + 2 * k := by omega
  unfold oddLogTerm
  rw [hexp, pow_add, pow_mul]
  have hmul := mul_le_mul_of_nonneg_right
    (mul_le_mul_of_nonneg_left hcoeff (by norm_num : (0 : Real) ≤ 2))
    (show (0 : Real) ≤ z ^ (2 * N + 1) * (z ^ 2) ^ k by positivity)
  simpa only [mul_assoc] using hmul

theorem oddLog_le_prefix_add_remainder (N : Nat) (z : Real)
    (hz : 0 ≤ z) (hzlt : z < 1) :
    Real.log (1 + z) - Real.log (1 - z) ≤ oddLogPrefix N z + oddLogRemainder N z := by
  have hs := oddLog_hasSum z hz hzlt
  have hshift : HasSum (fun k => oddLogTerm z (k + N))
      (Real.log (1 + z) - Real.log (1 - z) - oddLogPrefix N z) :=
    (hasSum_nat_add_iff' N).mpr hs
  have hzsq : |z ^ 2| < 1 := by rw [abs_of_nonneg (sq_nonneg z)]; nlinarith
  let C : Real := 2 * (1 / (2 * (N : Real) + 1)) * z ^ (2 * N + 1)
  have hg := (hasSum_geometric_of_abs_lt_one hzsq).mul_left C
  have hbound := hasSum_le (fun k => oddLog_tail_term_le N k z hz) hshift hg
  have heq : C * (1 - z ^ 2)⁻¹ = oddLogRemainder N z := by
    unfold C oddLogRemainder
    simp only [div_eq_mul_inv, mul_inv_rev, one_mul]
    ring
  rw [heq] at hbound
  linarith

theorem log_transform_identity (x : Real) (hx : 0 < x) :
    Real.log (1 + (x - 1) / (x + 1)) - Real.log (1 - (x - 1) / (x + 1)) =
      Real.log x := by
  have hden : 0 < x + 1 := by linarith
  have hplus : 1 + (x - 1) / (x + 1) = 2 * x / (x + 1) := by field_simp; ring
  have hminus : 1 - (x - 1) / (x + 1) = 2 / (x + 1) := by field_simp; ring
  rw [hplus, hminus, ← Real.log_div (by positivity) (by positivity)]
  congr 1
  field_simp

theorem log_binary_identity (x : Real) (hx : 0 < x) (k : Nat) :
    Real.log x = (k : Real) * Real.log 2 + Real.log (x / (2 : Real) ^ k) := by
  rw [Real.log_div (ne_of_gt hx) (by positivity), Real.log_pow]
  ring

def oddLogPrefixRat (N : Nat) (z : Rat) : Rat :=
  ∑ k ∈ Finset.range N, 2 * (1 / (2 * (k : Rat) + 1)) * z ^ (2 * k + 1)

def oddLogRemainderRat (N : Nat) (z : Rat) : Rat :=
  2 * z ^ (2 * N + 1) / ((2 * (N : Rat) + 1) * (1 - z ^ 2))

theorem oddLogPrefixRat_cast (N : Nat) (z : Rat) :
    (oddLogPrefixRat N z : Real) = oddLogPrefix N (z : Real) := by
  unfold oddLogPrefixRat oddLogPrefix oddLogTerm
  push_cast
  rfl

theorem oddLogRemainderRat_cast (N : Nat) (z : Rat) :
    (oddLogRemainderRat N z : Real) = oddLogRemainder N (z : Real) := by
  unfold oddLogRemainderRat oddLogRemainder
  push_cast
  rfl

def checkOddLogBounds (N : Nat) (z lo hi : Rat) : Bool :=
  decide (0 ≤ z ∧ z < 1 ∧ lo ≤ oddLogPrefixRat N z ∧
    oddLogPrefixRat N z + oddLogRemainderRat N z ≤ hi)

theorem checkOddLogBounds_sound (N : Nat) (z lo hi : Rat)
    (hc : checkOddLogBounds N z lo hi = true) :
    (lo : Real) ≤ Real.log (1 + (z : Real)) - Real.log (1 - (z : Real)) ∧
      Real.log (1 + (z : Real)) - Real.log (1 - (z : Real)) ≤ (hi : Real) := by
  have h := of_decide_eq_true hc
  rcases h with ⟨hz, hlt, hlo, hhi⟩
  have hzr : (0 : Real) ≤ (z : Real) := by exact_mod_cast hz
  have hltr : (z : Real) < 1 := by exact_mod_cast hlt
  have hlor : (lo : Real) ≤ oddLogPrefix N (z : Real) := by
    rw [← oddLogPrefixRat_cast]
    exact_mod_cast hlo
  have hhir : oddLogPrefix N (z : Real) + oddLogRemainder N (z : Real) ≤ (hi : Real) := by
    rw [← oddLogPrefixRat_cast, ← oddLogRemainderRat_cast]
    exact_mod_cast hhi
  exact ⟨hlor.trans (oddLogPrefix_le N z hzr hltr),
    (oddLog_le_prefix_add_remainder N z hzr hltr).trans hhir⟩

def binaryLogLower (N : Nat) (x : Real) (k : Nat) : Real :=
  (k : Real) * oddLogPrefix N (1 / 3) +
    oddLogPrefix N ((x / (2 : Real) ^ k - 1) / (x / (2 : Real) ^ k + 1))

def binaryLogUpper (N : Nat) (x : Real) (k : Nat) : Real :=
  (k : Real) * (oddLogPrefix N (1 / 3) + oddLogRemainder N (1 / 3)) +
    oddLogPrefix N ((x / (2 : Real) ^ k - 1) / (x / (2 : Real) ^ k + 1)) +
    oddLogRemainder N ((x / (2 : Real) ^ k - 1) / (x / (2 : Real) ^ k + 1))

theorem binaryLog_bounds (N : Nat) (x : Real) (k : Nat)
    (hx : 0 < x) (hrange : 1 ≤ x / (2 : Real) ^ k) :
    binaryLogLower N x k ≤ Real.log x ∧ Real.log x ≤ binaryLogUpper N x k := by
  let y : Real := x / (2 : Real) ^ k
  let z : Real := (y - 1) / (y + 1)
  have hyone : 1 ≤ y := hrange
  have hypos : 0 < y := by linarith
  have hz : 0 ≤ z := div_nonneg (sub_nonneg.mpr hyone) (by linarith)
  have hzlt : z < 1 := (div_lt_one (by linarith : 0 < y + 1)).mpr (by linarith)
  have hid2 : Real.log (1 + (1 / 3 : Real)) - Real.log (1 - (1 / 3 : Real)) = Real.log 2 := by
    convert log_transform_identity 2 (by norm_num) using 1
    norm_num
  have h2lo := oddLogPrefix_le N (1 / 3) (by norm_num) (by norm_num)
  have h2hi := oddLog_le_prefix_add_remainder N (1 / 3) (by norm_num) (by norm_num)
  rw [hid2] at h2lo h2hi
  have hyid : Real.log (1 + z) - Real.log (1 - z) = Real.log y :=
    log_transform_identity y hypos
  have hylo := oddLogPrefix_le N z hz hzlt
  have hyhi := oddLog_le_prefix_add_remainder N z hz hzlt
  rw [hyid] at hylo hyhi
  have hbin : Real.log x = (k : Real) * Real.log 2 + Real.log y := log_binary_identity x hx k
  have hk : (0 : Real) ≤ (k : Real) := Nat.cast_nonneg k
  constructor
  · change (k : Real) * oddLogPrefix N (1 / 3) + oddLogPrefix N z ≤ Real.log x
    rw [hbin]
    exact add_le_add (mul_le_mul_of_nonneg_left h2lo hk) hylo
  · change Real.log x ≤ (k : Real) * (oddLogPrefix N (1 / 3) + oddLogRemainder N (1 / 3)) +
      oddLogPrefix N z + oddLogRemainder N z
    rw [hbin]
    have h := add_le_add (mul_le_mul_of_nonneg_left h2hi hk) hyhi
    linarith

def binaryLogLowerRat (N : Nat) (x : Rat) (k : Nat) : Rat :=
  (k : Rat) * oddLogPrefixRat N (1 / 3) +
    oddLogPrefixRat N ((x / (2 : Rat) ^ k - 1) / (x / (2 : Rat) ^ k + 1))

def binaryLogUpperRat (N : Nat) (x : Rat) (k : Nat) : Rat :=
  (k : Rat) * (oddLogPrefixRat N (1 / 3) + oddLogRemainderRat N (1 / 3)) +
    oddLogPrefixRat N ((x / (2 : Rat) ^ k - 1) / (x / (2 : Rat) ^ k + 1)) +
    oddLogRemainderRat N ((x / (2 : Rat) ^ k - 1) / (x / (2 : Rat) ^ k + 1))

theorem binaryLogLowerRat_cast (N : Nat) (x : Rat) (k : Nat) :
    (binaryLogLowerRat N x k : Real) = binaryLogLower N (x : Real) k := by
  unfold binaryLogLowerRat binaryLogLower oddLogPrefixRat oddLogPrefix oddLogTerm
  push_cast
  rfl

theorem binaryLogUpperRat_cast (N : Nat) (x : Rat) (k : Nat) :
    (binaryLogUpperRat N x k : Real) = binaryLogUpper N (x : Real) k := by
  unfold binaryLogUpperRat binaryLogUpper oddLogPrefixRat oddLogPrefix oddLogTerm
    oddLogRemainderRat oddLogRemainder
  push_cast
  rfl

def checkPositiveLogBounds (N : Nat) (x : Rat) (k : Nat) (lo hi : Rat) : Bool :=
  decide (0 < x ∧ 1 ≤ x / (2 : Rat) ^ k ∧ x / (2 : Rat) ^ k < 2 ∧
    lo ≤ binaryLogLowerRat N x k ∧ binaryLogUpperRat N x k ≤ hi)

theorem checkPositiveLogBounds_sound (N : Nat) (x : Rat) (k : Nat) (lo hi : Rat)
    (hc : checkPositiveLogBounds N x k lo hi = true) :
    (lo : Real) ≤ Real.log (x : Real) ∧ Real.log (x : Real) ≤ (hi : Real) := by
  rcases of_decide_eq_true hc with ⟨hx, hrange, htwo, hlo, hhi⟩
  have hxr : (0 : Real) < (x : Real) := by exact_mod_cast hx
  have hrr : (1 : Real) ≤ (x : Real) / (2 : Real) ^ k := by
    have hh : (1 : Real) ≤ ((x / (2 : Rat) ^ k : Rat) : Real) := by exact_mod_cast hrange
    push_cast at hh
    exact hh
  have hb := binaryLog_bounds N x k hxr hrr
  have hl : (lo : Real) ≤ binaryLogLower N (x : Real) k := by
    rw [← binaryLogLowerRat_cast]
    exact_mod_cast hlo
  have hu : binaryLogUpper N (x : Real) k ≤ (hi : Real) := by
    rw [← binaryLogUpperRat_cast]
    exact_mod_cast hhi
  exact ⟨hl.trans hb.1, hb.2.trans hu⟩

theorem oddLog_zero_control (N : Nat) : oddLogPrefix N 0 = 0 ∧ oddLogRemainder N 0 = 0 := by
  simp [oddLogPrefix, oddLogTerm, oddLogRemainder]

theorem oddLog_empty_prefix_control (z : Real) : oddLogPrefix 0 z = 0 := by
  simp [oddLogPrefix]

theorem log_two_rational_control : (6931 / 10000 : Real) ≤ Real.log 2 ∧
    Real.log 2 ≤ (6932 / 10000 : Real) := by
  have h := checkOddLogBounds_sound 5 (1 / 3) (6931 / 10000) (6932 / 10000)
    (by norm_num [checkOddLogBounds, oddLogPrefixRat, oddLogRemainderRat, Finset.sum_range_succ])
  have hi := log_transform_identity 2 (by norm_num)
  norm_num at hi
  norm_num at h
  rw [hi] at h
  constructor <;> linarith [h.1, h.2]

theorem empty_prefix_upper_false : ¬ Real.log 2 ≤ oddLogPrefix 0 (1 / 3) := by
  rw [oddLog_empty_prefix_control]
  exact not_le_of_gt (Real.log_pos (by norm_num))

theorem invalid_log_enclosure_control : checkOddLogBounds 5 (1 / 3) 0 0 = false := by
  norm_num [checkOddLogBounds, oddLogPrefixRat, oddLogRemainderRat, Finset.sum_range_succ]

theorem binary_first_row_control :
    checkPositiveLogBounds 8 2 1 (693147179548 / 1000000000000)
      (693147180574 / 1000000000000) = true := by
  norm_num [checkPositiveLogBounds, binaryLogLowerRat, binaryLogUpperRat,
    oddLogPrefixRat, oddLogRemainderRat, Finset.sum_range_succ]

theorem binary_largest_prime_control :
    checkPositiveLogBounds 8 9973 13 (9207636707249 / 1000000000000)
      (9207636720574 / 1000000000000) = true := by
  norm_num [checkPositiveLogBounds, binaryLogLowerRat, binaryLogUpperRat,
    oddLogPrefixRat, oddLogRemainderRat, Finset.sum_range_succ]

end
end TenthDiscriminant
