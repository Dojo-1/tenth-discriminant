import TenthDiscriminant.Arithmetic

/-! Universal agreement with tools/ender.py:floor_sum; not just sampled tests. -/
namespace TenthDiscriminant

/-- Scaled closed form, avoiding truncated subtraction in the induction. -/
theorem floorSum_scaled (R q : ℕ) :
    2 * floorSum R q + q * (R/q) = q * (R/q)^2 + 2*(R/q)*(R%q) := by
  induction R with
  | zero => simp [floorSum]
  | succ R ih =>
      by_cases hd : q ∣ R+1
      · have hdiv := Nat.succ_div_of_dvd hd
        have hmod := Nat.mod_eq_zero_of_dvd hd
        have hrem : R%q + 1 = q := by
          have h₁ := Nat.div_add_mod R q
          have h₂ := Nat.div_add_mod (R+1) q
          rw [hdiv,hmod] at h₂
          nlinarith
        have hmul := congrArg (fun t : ℕ => (R/q)*t) hrem
        rw [floorSum_succ,hdiv,hmod]
        nlinarith
      · have hdiv := Nat.succ_div_of_not_dvd hd
        have hmod : (R+1)%q = R%q+1 := by
          have h₁ := Nat.div_add_mod R q
          have h₂ := Nat.div_add_mod (R+1) q
          rw [hdiv] at h₂
          omega
        rw [floorSum_succ,hdiv,hmod]
        nlinarith

/-- This is the exact expression evaluated by the Python implementation. -/
theorem floorSum_closed (R q : ℕ) :
    floorSum R q = q*(R/q)*(R/q-1)/2 + (R/q)*(R%q) := by
  have h := floorSum_scaled R q
  generalize hk : R/q = k at *
  generalize hm : R%q = m at *
  cases k with
  | zero =>
      simp at h ⊢
      omega
  | succ k =>
      simp only [Nat.succ_eq_add_one, Nat.add_sub_cancel] at h ⊢
      have h₂ : 2*floorSum R q = q*(k+1)*k + 2*((k+1)*m) := by nlinarith
      omega

end TenthDiscriminant
