import TenthDiscriminant.Envelope

/-! Actual C=80 error terms from ledger/ender.txt, section 4.
Their monotonicity is proved; the numerical endpoint margin and the
bounds relating them to the determinant are NOT supplied as conclusions. -/
namespace TenthDiscriminant

theorem reciprocal_exp_antitone : Antitone (fun u : ℝ => 1 / Real.exp u) := by
  intro u v huv
  apply (div_le_div_iff₀ (Real.exp_pos v) (Real.exp_pos u)).2
  simpa using (Real.exp_le_exp.mpr huv)

theorem linear_exp_antitone : AntitoneOn (fun u : ℝ => u / Real.exp u) (Set.Ici 1) := by
  intro u hu v hv huv
  have hu1 : 1 ≤ u := hu
  have ht : 0 ≤ v-u := sub_nonneg.mpr huv
  have hl : v ≤ u*(1+(v-u)) := by
    nlinarith [mul_nonneg (sub_nonneg.mpr hu1) ht]
  have he : 1+(v-u) ≤ Real.exp (v-u) := by
    simpa [add_comm] using Real.add_one_le_exp (v-u)
  have hm := mul_le_mul_of_nonneg_left he (by linarith : 0 ≤ u)
  have hx : Real.exp v = Real.exp (v-u) * Real.exp u := by
    rw [← Real.exp_add]
    congr 1
    ring
  apply (div_le_div_iff₀ (Real.exp_pos v) (Real.exp_pos u)).2
  calc
    v * Real.exp u ≤ (u * Real.exp (v-u)) * Real.exp u :=
      mul_le_mul_of_nonneg_right (le_trans hl hm) (le_of_lt (Real.exp_pos u))
    _ = u * Real.exp v := by rw [hx]; ring

noncomputable def enderError (u : ℝ) : ℝ :=
  (5+5*(2*u+2)+5*80*u)/Real.exp u +
  5*(Real.log 8+2*u)/Real.exp u +
  (2/80 : ℝ)*(5*Real.exp (-u/4)+5*u/Real.exp u)

theorem enderError_expansion (u : ℝ) :
    enderError u = (15+5*Real.log 8)*(1/Real.exp u) +
      (3361/8 : ℝ)*(u/Real.exp u) + (1/8 : ℝ)*Real.exp (-u/4) := by
  unfold enderError
  ring

theorem enderError_antitone : AntitoneOn enderError (Set.Ici 1) := by
  intro u hu v hv huv
  have h₁ := reciprocal_exp_antitone huv
  have h₂ := linear_exp_antitone hu hv huv
  have h₃ : Real.exp (-v/4) ≤ Real.exp (-u/4) := Real.exp_le_exp.mpr (by linarith)
  have hc : 0 ≤ 15+5*Real.log 8 := by
    have hl := Real.log_nonneg (by norm_num : (1 : ℝ) ≤ 8)
    linarith
  have hp := mul_le_mul_of_nonneg_left h₁ hc
  rw [enderError_expansion, enderError_expansion]
  nlinarith

/-- Conditional closure with the actual error function. Endpoint positivity stays a hypothesis. -/
theorem ender_positive_from_endpoint (B u₀ : ℝ) (hu₀ : 1 ≤ u₀)
    (hstart : 0 < (15/64 : ℝ)*u₀-B-enderError u₀) :
    ∀ u, u₀ ≤ u → 0 < (15/64 : ℝ)*u-B-enderError u := by
  apply positive_envelope (15/64) B u₀ enderError (by norm_num) ?_ hstart
  intro u hu v hv huv
  exact enderError_antitone (le_trans hu₀ hu) (le_trans hu₀ hv) huv

end TenthDiscriminant
