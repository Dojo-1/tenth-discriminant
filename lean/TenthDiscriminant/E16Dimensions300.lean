import TenthDiscriminant.Lower315

/-!
Reconstructed E16 source dimension envelope for D >= 300^4.
No old 307-domain hypothesis is imported.
-/
namespace TenthDiscriminant.FirstCertificate.Tuned
open TenthDiscriminant.RadialCutoff
set_option autoImplicit false
noncomputable section

theorem dimensions_300 (D : Nat) (hD : (300 : Nat)^4 ≤ D) :
    100000000 ≤ R D ∧ 500000 ≤ S D ∧ 10*R D ≤ 251*S D ∧
    R D ≤ 10000*S D ∧ (D : Real)/5 ≤ R D ∧
    (R D : Real) ≤ (D : Real)/4 ∧ (S D : Real) ≤ (R D : Real)/25 := by
  have hlo : D ≤ 5*(D/4) := by omega
  have hhi : 4*(D/4) ≤ D := by omega
  have hs : 25*((D/4)/25) ≤ D/4 := by omega
  refine ⟨by unfold R envelopeR; omega, by unfold S R envelopeR; omega,
    by unfold S R envelopeR; omega, by unfold S R envelopeR; omega, ?_, ?_, ?_⟩
  · have h : (D : Real) ≤ 5*(D/4 : Nat) := by exact_mod_cast hlo
    change (D : Real)/5 ≤ (D/4 : Nat)
    linarith
  · have h : 4*((D/4 : Nat) : Real) ≤ D := by exact_mod_cast hhi
    change ((D/4 : Nat) : Real) ≤ (D : Real)/4
    linarith
  · have h : 25*(((D/4)/25 : Nat) : Real) ≤ (D/4 : Nat) := by exact_mod_cast hs
    change (((D/4)/25 : Nat) : Real) ≤ ((D/4 : Nat) : Real)/25
    linarith

/-- Reprove the floor-ratio logarithm at 300^4; do not weaken the
existing 322-domain theorem. -/
theorem log_R_lower_300 (D : Nat) (hD : (300 : Nat)^4 ≤ D) :
    Real.log D-13904/10000 ≤ Real.log (R D) := by
  have hn : 249*D ≤ 1000*R D := by
    simpa [R] using
      (FirstCertificate.envelope_floor_ratio D (by omega))
  have hr : (249 : Real)*D ≤ 1000*R D := by exact_mod_cast hn
  have hp : (0 : Real) < D := by exact_mod_cast (show 0 < D by omega)
  have hR : (D : Real)/(1000/249) ≤ R D := by
    apply (div_le_iff₀ (by norm_num : (0 : Real) < 1000/249)).2
    linarith
  have hl := Real.log_le_log (div_pos hp (by norm_num)) hR
  rw [Real.log_div hp.ne' (by norm_num : (1000/249 : Real) ≠ 0)] at hl
  linarith [TenthDiscriminant.log_floor_ratio_upper_13904]

/-- Both logarithmic bounds for the unchanged floor R=floor(D/4). -/
theorem log_R_bounds_300 (D : Nat) (hD : (300 : Nat)^4 ≤ D) :
    Real.log D-13904/10000 ≤ Real.log (R D) ∧
    Real.log (R D) ≤ Real.log D-138/100 := by
  have hd := dimensions_300 D hD
  have hp : (0 : Real) < D := by exact_mod_cast (show 0<D by omega)
  have hRpos : (0 : Real) < R D := by exact_mod_cast (show 0<R D by omega)
  constructor
  · exact log_R_lower_300 D hD
  · have hl := Real.log_le_log hRpos hd.2.2.2.2.2.1
    rw [Real.log_div hp.ne' (by norm_num : (4 : Real) ≠ 0)] at hl
    have h4 : Real.log (4 : Real)=2*Real.log 2 := by
      have he : (4 : Real)=2^2 := by norm_num
      rw [he,Real.log_pow]
      norm_num
    rw [h4] at hl
    linarith [Real.log_two_gt_d9]



/-- Elementary log(R)>=2, using the unchanged R>=100 million dimension bound. -/
theorem log_R_ge_two_300 (D : Nat) (hD : (300 : Nat)^4 ≤ D) :
    2 ≤ Real.log (R D) := by
  have hd := dimensions_300 D hD
  have hr : (16 : Real) ≤ (R D : Real) := by
    exact_mod_cast (show 16 ≤ R D by omega)
  have hl := Real.log_le_log (by norm_num : (0 : Real) < 16) hr
  have he : (16 : Real) = 2^4 := by norm_num
  rw [he, Real.log_pow] at hl
  norm_num only [Nat.cast_ofNat] at hl
  linarith [Real.log_two_gt_d9]

end
end TenthDiscriminant.FirstCertificate.Tuned

#print axioms TenthDiscriminant.FirstCertificate.Tuned.dimensions_300
#print axioms TenthDiscriminant.FirstCertificate.Tuned.log_R_bounds_300
