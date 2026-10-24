import TenthDiscriminant.LogEnclosure

/-!
# Eight-term logarithm enclosures with raw integer denominators

These formulas represent the same proved rational prefix and remainder.
They avoid normalizing a separate large rational proof at every table row.
All Boolean evidence is still checked by Lean's kernel, not native_decide.
-/

namespace TenthDiscriminant
set_option autoImplicit false
noncomputable section

def rawLogPrefixNum (a b : Nat) : Nat :=
  2 * a * (45045 * b ^ 14 + 15015 * a ^ 2 * b ^ 12 +
    9009 * a ^ 4 * b ^ 10 + 6435 * a ^ 6 * b ^ 8 +
    5005 * a ^ 8 * b ^ 6 + 4095 * a ^ 10 * b ^ 4 +
    3465 * a ^ 12 * b ^ 2 + 3003 * a ^ 14)

def rawLogPrefixDen (b : Nat) : Nat := 45045 * b ^ 15
def rawLogUpperNum (a b : Nat) : Nat :=
  17 * (b ^ 2 - a ^ 2) * rawLogPrefixNum a b + 90090 * a ^ 17
def rawLogUpperDen (a b : Nat) : Nat := 17 * rawLogPrefixDen b * (b ^ 2 - a ^ 2)

theorem rawLogPrefixDen_pos (b : Nat) (hb : 0 < b) : 0 < rawLogPrefixDen b :=
  Nat.mul_pos (by decide) (Nat.pow_pos hb)

theorem rawLogUpperDen_pos (a b : Nat) (hab : a < b) : 0 < rawLogUpperDen a b := by
  have hb : 0 < b := by omega
  have hsq : a ^ 2 < b ^ 2 := Nat.pow_lt_pow_left hab (by decide : 2 ≠ 0)
  exact Nat.mul_pos (Nat.mul_pos (by decide) (rawLogPrefixDen_pos b hb))
    (Nat.sub_pos_of_lt hsq)

theorem rawLogPrefix_eq (a b : Nat) (hb : 0 < b) :
    (rawLogPrefixNum a b : Real) / rawLogPrefixDen b =
      oddLogPrefix 8 ((a : Real) / b) := by
  have hbr : (0 : Real) < b := by exact_mod_cast hb
  unfold rawLogPrefixNum rawLogPrefixDen oddLogPrefix oddLogTerm
  norm_num [Finset.sum_range_succ]
  field_simp [ne_of_gt hbr]
  ring

theorem rawLogUpper_eq (a b : Nat) (hab : a < b) :
    (rawLogUpperNum a b : Real) / rawLogUpperDen a b =
      oddLogPrefix 8 ((a : Real) / b) + oddLogRemainder 8 ((a : Real) / b) := by
  have hb : 0 < b := by omega
  have hbr : (0 : Real) < b := by exact_mod_cast hb
  have habr : (a : Real) < b := by exact_mod_cast hab
  have har : (0 : Real) ≤ a := Nat.cast_nonneg a
  have hsq : a ^ 2 ≤ b ^ 2 := Nat.pow_le_pow_left hab.le 2
  have hdiff : (0 : Real) < (b : Real) ^ 2 - (a : Real) ^ 2 := by nlinarith
  have hratio : (a : Real) / b < 1 := (div_lt_one hbr).mpr habr
  have hrnonneg : (0 : Real) ≤ (a : Real) / b := by positivity
  have hratden : (0 : Real) < 1 - ((a : Real) / b) ^ 2 := by nlinarith
  rw [← rawLogPrefix_eq a b hb]
  unfold rawLogUpperNum rawLogUpperDen rawLogPrefixDen oddLogRemainder
  push_cast [Nat.cast_sub hsq]
  norm_num only [Nat.cast_ofNat]
  field_simp [ne_of_gt hbr, ne_of_gt hdiff, ne_of_gt hratden]
  ring

def rawLogA (n d k : Nat) : Nat := n - d * 2 ^ k
def rawLogB (n d k : Nat) : Nat := n + d * 2 ^ k

def rawBinaryLowerNum (n d k : Nat) : Nat :=
  k * rawLogPrefixNum 1 3 * rawLogPrefixDen (rawLogB n d k) +
    rawLogPrefixNum (rawLogA n d k) (rawLogB n d k) * rawLogPrefixDen 3
def rawBinaryLowerDen (n d k : Nat) : Nat := rawLogPrefixDen 3 * rawLogPrefixDen (rawLogB n d k)
def rawBinaryUpperNum (n d k : Nat) : Nat :=
  k * rawLogUpperNum 1 3 * rawLogUpperDen (rawLogA n d k) (rawLogB n d k) +
    rawLogUpperNum (rawLogA n d k) (rawLogB n d k) * rawLogUpperDen 1 3
def rawBinaryUpperDen (n d k : Nat) : Nat :=
  rawLogUpperDen 1 3 * rawLogUpperDen (rawLogA n d k) (rawLogB n d k)

theorem rawLog_transform (n d k : Nat) (hd : 0 < d) (hn : d * 2 ^ k ≤ n) :
    ((((n : Real) / d) / (2 : Real) ^ k - 1) /
      (((n : Real) / d) / (2 : Real) ^ k + 1)) =
        (rawLogA n d k : Real) / rawLogB n d k := by
  have hdr : (0 : Real) < d := by exact_mod_cast hd
  have hpow : (0 : Real) < (2 : Real) ^ k := by positivity
  unfold rawLogA rawLogB
  push_cast [Nat.cast_sub hn]
  have hsum : (0 : Real) < (n : Real) + d * (2 : Real) ^ k := by positivity
  field_simp [ne_of_gt hdr, ne_of_gt hpow, ne_of_gt hsum]

theorem rawLog_ab_bounds (n d k : Nat) (hd : 0 < d) (hn : d * 2 ^ k ≤ n) :
    rawLogA n d k < rawLogB n d k ∧ 0 < rawLogB n d k := by
  have hp : 0 < d * 2 ^ k := Nat.mul_pos hd (by positivity)
  unfold rawLogA rawLogB
  omega

theorem rawBinaryLower_eq (n d k : Nat) (hd : 0 < d) (hn : d * 2 ^ k ≤ n) :
    (rawBinaryLowerNum n d k : Real) / rawBinaryLowerDen n d k =
      binaryLogLower 8 ((n : Real) / d) k := by
  have hab := rawLog_ab_bounds n d k hd hn
  have hb : (0 : Real) < rawLogPrefixDen (rawLogB n d k) := by
    exact_mod_cast rawLogPrefixDen_pos (rawLogB n d k) hab.2
  have hthreeEq := rawLogPrefix_eq 1 3 (by decide)
  norm_num only [Nat.cast_ofNat] at hthreeEq
  unfold binaryLogLower
  rw [rawLog_transform n d k hd hn, ← rawLogPrefix_eq (rawLogA n d k) (rawLogB n d k) hab.2,
    ← hthreeEq]
  unfold rawBinaryLowerNum rawBinaryLowerDen
  push_cast
  have hthree : (0 : Real) < rawLogPrefixDen 3 := by norm_num [rawLogPrefixDen]
  field_simp [ne_of_gt hb, ne_of_gt hthree]

theorem rawBinaryUpper_eq (n d k : Nat) (hd : 0 < d) (hn : d * 2 ^ k ≤ n) :
    (rawBinaryUpperNum n d k : Real) / rawBinaryUpperDen n d k =
      binaryLogUpper 8 ((n : Real) / d) k := by
  have hab := rawLog_ab_bounds n d k hd hn
  have hb : (0 : Real) < rawLogUpperDen (rawLogA n d k) (rawLogB n d k) := by
    exact_mod_cast rawLogUpperDen_pos (rawLogA n d k) (rawLogB n d k) hab.1
  have hthree : (0 : Real) < rawLogUpperDen 1 3 := by norm_num [rawLogUpperDen, rawLogPrefixDen]
  have hthreeEq := rawLogUpper_eq 1 3 (by decide)
  norm_num only [Nat.cast_ofNat] at hthreeEq
  unfold binaryLogUpper
  rw [rawLog_transform n d k hd hn]
  rw [← hthreeEq]
  have hgroup : (k : Real) * ((rawLogUpperNum 1 3 : Real) / rawLogUpperDen 1 3) +
      oddLogPrefix 8 ((rawLogA n d k : Real) / rawLogB n d k) +
      oddLogRemainder 8 ((rawLogA n d k : Real) / rawLogB n d k) =
      (k : Real) * ((rawLogUpperNum 1 3 : Real) / rawLogUpperDen 1 3) +
        (rawLogUpperNum (rawLogA n d k) (rawLogB n d k) : Real) /
          rawLogUpperDen (rawLogA n d k) (rawLogB n d k) := by
    rw [rawLogUpper_eq _ _ hab.1]
    ring
  rw [hgroup]
  unfold rawBinaryUpperNum rawBinaryUpperDen
  push_cast
  field_simp [ne_of_gt hb, ne_of_gt hthree]

def checkIntegerLogBounds (n d k lo hi scale : Nat) : Bool := decide (
  0 < d ∧ d * 2 ^ k ≤ n ∧ 0 < scale ∧
    lo * rawBinaryLowerDen n d k ≤ rawBinaryLowerNum n d k * scale ∧
    rawBinaryUpperNum n d k * scale ≤ hi * rawBinaryUpperDen n d k)

theorem checkIntegerLogBounds_sound (n d k lo hi scale : Nat)
    (hc : checkIntegerLogBounds n d k lo hi scale = true) :
    (lo : Real) / scale ≤ Real.log ((n : Real) / d) ∧
      Real.log ((n : Real) / d) ≤ (hi : Real) / scale := by
  rcases of_decide_eq_true hc with ⟨hd, hn, hs, hlo, hhi⟩
  have hab := rawLog_ab_bounds n d k hd hn
  have hnr : (0 : Real) < n := by
    exact_mod_cast (lt_of_lt_of_le (Nat.mul_pos hd (by positivity : 0 < 2 ^ k)) hn)
  have hdr : (0 : Real) < d := by exact_mod_cast hd
  have hsr : (0 : Real) < scale := by exact_mod_cast hs
  have hnorm : (1 : Real) ≤ ((n : Real) / d) / (2 : Real) ^ k := by
    apply (le_div_iff₀ (by positivity : (0 : Real) < (2 : Real) ^ k)).mpr
    apply (le_div_iff₀ hdr).mpr
    have hh : (d : Real) * (2 : Real) ^ k ≤ n := by exact_mod_cast hn
    simpa [mul_comm] using hh
  have hbounds := binaryLog_bounds 8 ((n : Real) / d) k (div_pos hnr hdr) hnorm
  have hld : (0 : Real) < rawBinaryLowerDen n d k := by
    exact_mod_cast Nat.mul_pos (rawLogPrefixDen_pos 3 (by decide))
      (rawLogPrefixDen_pos (rawLogB n d k) hab.2)
  have hud : (0 : Real) < rawBinaryUpperDen n d k := by
    exact_mod_cast Nat.mul_pos (rawLogUpperDen_pos 1 3 (by decide))
      (rawLogUpperDen_pos (rawLogA n d k) (rawLogB n d k) hab.1)
  have hl : (lo : Real) / scale ≤ (rawBinaryLowerNum n d k : Real) / rawBinaryLowerDen n d k :=
    (div_le_div_iff₀ hsr hld).mpr (by exact_mod_cast hlo)
  have hu : (rawBinaryUpperNum n d k : Real) / rawBinaryUpperDen n d k ≤ (hi : Real) / scale :=
    (div_le_div_iff₀ hud hsr).mpr (by exact_mod_cast hhi)
  rw [rawBinaryLower_eq n d k hd hn] at hl
  rw [rawBinaryUpper_eq n d k hd hn] at hu
  exact ⟨hl.trans hbounds.1, hbounds.2.trans hu⟩

theorem integer_log_two_control :
    checkIntegerLogBounds 2 1 1 693147179548 693147180574 1000000000000 = true := by decide

theorem integer_log_largest_prime_control :
    checkIntegerLogBounds 9973 1 13 9207636707249 9207636720574 1000000000000 = true := by decide

theorem integer_log_one_control : checkIntegerLogBounds 1 1 0 0 0 1000000000000 = true := by decide

theorem integer_log_bad_upper_control :
    checkIntegerLogBounds 9973 1 13 0 0 1000000000000 = false := by decide

end
end TenthDiscriminant
