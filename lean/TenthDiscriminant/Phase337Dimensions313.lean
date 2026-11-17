import TenthDiscriminant.Lower315
import TenthDiscriminant.Phase332Log313Certificate
import TenthDiscriminant.Phase332SourceGeometry313

/-!
# Phase337 — source-exact 313^4 dimension and logarithmic guards

Transports only the classical floor relations for the UNCHANGED
R=floor(D/4), S=floor(R/25), at root 313 instead of root 315.
Does not transport source Gram lower or analytic upper by assumption.
-/
namespace TenthDiscriminant.FirstCertificate.Tuned
open TenthDiscriminant.RadialCutoff
set_option autoImplicit false
noncomputable section

theorem dimensions_313 (D : Nat) (hD : (313 : Nat)^4 ≤ D) :
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

/-- Reprove the floor-ratio logarithm at 313^4; do not weaken the
existing 322-domain theorem. -/
theorem log_R_lower_313 (D : Nat) (hD : (313 : Nat)^4 ≤ D) :
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
theorem log_R_bounds_313 (D : Nat) (hD : (313 : Nat)^4 ≤ D) :
    Real.log D-13904/10000 ≤ Real.log (R D) ∧
    Real.log (R D) ≤ Real.log D-138/100 := by
  have hd := dimensions_313 D hD
  have hp : (0 : Real) < D := by exact_mod_cast (show 0<D by omega)
  have hRpos : (0 : Real) < R D := by exact_mod_cast (show 0<R D by omega)
  constructor
  · exact log_R_lower_313 D hD
  · have hl := Real.log_le_log hRpos hd.2.2.2.2.2.1
    rw [Real.log_div hp.ne' (by norm_num : (4 : Real) ≠ 0)] at hl
    have h4 : Real.log (4 : Real)=2*Real.log 2 := by
      have he : (4 : Real)=2^2 := by norm_num
      rw [he,Real.log_pow]
      norm_num
    rw [h4] at hl
    linarith [Real.log_two_gt_d9]


end
end TenthDiscriminant.FirstCertificate.Tuned

#print axioms TenthDiscriminant.FirstCertificate.Tuned.dimensions_313
#print axioms TenthDiscriminant.FirstCertificate.Tuned.log_R_bounds_313
