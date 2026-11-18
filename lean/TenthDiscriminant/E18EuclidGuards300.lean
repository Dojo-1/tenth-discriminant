import TenthDiscriminant.E16Integrated300

/-!
# E18 — Universal elementary guards for the E6 reduced ellipse, D>=300^4

R=floor(D/4), S=floor(R/25), r=ceil((81/200) D^(3/4)).
No field, number-theoretic, or changed-jet assumptions occur here.
These are preparatory guards, not the complete E17 analytic separator.
-/
namespace TenthDiscriminant.E18
open TenthDiscriminant
open TenthDiscriminant.FirstCertificate
set_option autoImplicit false
noncomputable section

theorem fourthRoot_ge_300 (D : Nat) (hD : (300 : Nat)^4 ≤ D) :
    (300 : Real) ≤ fourthRoot D := by
  unfold fourthRoot
  apply Real.le_sqrt_of_sq_le
  apply Real.le_sqrt_of_sq_le
  exact_mod_cast (show (300 : Nat)^2^2 ≤ D by omega)

/-- Exact ceiling buffer: 0.405*t^3 <= radius <= 0.406*t^3. -/
theorem euclid_radius_coeff_300 (D : Nat)
    (hD : (300 : Nat)^4 ≤ D) :
    (81/200 : Real)*fourthRoot D^3 ≤
      (FirstCertificate.Tuned.euclidRadius D : Real) ∧
    (FirstCertificate.Tuned.euclidRadius D : Real) ≤
      (203/500 : Real)*fourthRoot D^3 := by
  have ht := fourthRoot_ge_300 D hD
  have hcube : (300 : Real)^3 ≤ fourthRoot D^3 :=
    pow_le_pow_left₀ (by norm_num) ht 3
  have hceil : (FirstCertificate.Tuned.euclidRadius D : Real) <
      (81/200 : Real)*fourthRoot D^3+1 := by
    unfold FirstCertificate.Tuned.euclidRadius
    exact Nat.ceil_lt_add_one (by positivity)
  constructor
  · unfold FirstCertificate.Tuned.euclidRadius
    exact Nat.le_ceil _
  · nlinarith only [hcube,hceil]

/-- Integer-dimension-to-radius control, uniform across ceiling jumps. -/
theorem euclid_hundred_radius_le_R_300 (D : Nat)
    (hD : (300 : Nat)^4 ≤ D) :
    100 * FirstCertificate.Tuned.euclidRadius D ≤
      FirstCertificate.Tuned.R D := by
  have ht := fourthRoot_ge_300 D hD
  have h4 := (fourthRoot_identities D).2.2
  have hr := (euclid_radius_coeff_300 D hD).2
  have hfloor : D ≤ 5*FirstCertificate.Tuned.R D := by
    unfold FirstCertificate.Tuned.R envelopeR
    omega
  have hfloorR : (D : Real) ≤
      5*(FirstCertificate.Tuned.R D : Real) := by
    exact_mod_cast hfloor
  have hgap : (0 : Real) ≤
      (fourthRoot D-203)*fourthRoot D^3 :=
    mul_nonneg (by linarith) (pow_nonneg (fourthRoot_identities D).1 3)
  have h100 : (100 : Real)*(FirstCertificate.Tuned.euclidRadius D : Real) ≤
      (FirstCertificate.Tuned.R D : Real) := by
    nlinarith only [hr,hfloorR,h4,hgap]
  exact_mod_cast h100

/-- Actual E17 small radius/R upper. -/
theorem euclid_radius_over_R_300 (D : Nat)
    (hD : (300 : Nat)^4 ≤ D) :
    (FirstCertificate.Tuned.euclidRadius D : Real) /
      FirstCertificate.Tuned.R D ≤ 1/100 := by
  have h100 := euclid_hundred_radius_le_R_300 D hD
  have hdim := FirstCertificate.Tuned.dimensions_300 D hD
  have hrpos : (0 : Real) < FirstCertificate.Tuned.R D := by
    have hp : 0 < FirstCertificate.Tuned.R D := by omega
    exact_mod_cast hp
  apply (div_le_iff₀ hrpos).2
  have hreal : (100 : Real)*FirstCertificate.Tuned.euclidRadius D ≤
      FirstCertificate.Tuned.R D := by
    exact_mod_cast h100
  linarith

theorem euclid_S_over_R_300 (D : Nat)
    (hD : (300 : Nat)^4 ≤ D) :
    (FirstCertificate.Tuned.S D : Real)/FirstCertificate.Tuned.R D ≤
      1/25 := by
  have hdim := FirstCertificate.Tuned.dimensions_300 D hD
  have hrpos : (0 : Real) < FirstCertificate.Tuned.R D := by
    exact_mod_cast (show 0 < FirstCertificate.Tuned.R D by omega)
  have h25 : 25 * FirstCertificate.Tuned.S D ≤ FirstCertificate.Tuned.R D := by
    unfold FirstCertificate.Tuned.S
    omega
  have hreal : (25 : Real)*FirstCertificate.Tuned.S D ≤
      FirstCertificate.Tuned.R D := by exact_mod_cast h25
  apply (div_le_iff₀ hrpos).2
  linarith

/-- E17 ratio logarithm lower: follows from the much stronger
radius <=R/100 and rational lower for log 2. -/
theorem euclid_log_ratio_ge_one_300 (D : Nat)
    (hD : (300 : Nat)^4 ≤ D) :
    (1 : Real) ≤ Real.log
      ((FirstCertificate.Tuned.R D : Real) /
       FirstCertificate.Tuned.euclidRadius D) := by
  have h100 := euclid_hundred_radius_le_R_300 D hD
  have hpositive := (FirstCertificate.Tuned.euclid_radius_guards_252 D
    (by omega : (252 : Nat)^4 ≤ D)).1
  have hρpos : (0 : Real) < FirstCertificate.Tuned.euclidRadius D := by
    exact_mod_cast (show 0 < FirstCertificate.Tuned.euclidRadius D by omega)
  have h100real : (100 : Real)*FirstCertificate.Tuned.euclidRadius D ≤
      FirstCertificate.Tuned.R D := by exact_mod_cast h100
  have hfour :
      (4 : Real) ≤ (FirstCertificate.Tuned.R D : Real) /
        FirstCertificate.Tuned.euclidRadius D := by
    apply (le_div_iff₀ hρpos).2
    linarith
  have hl := Real.log_le_log (by norm_num : (0 : Real) < 4) hfour
  have h4 : (4 : Real)=2^2 := by norm_num
  rw [h4, Real.log_pow] at hl
  norm_num only [Nat.cast_ofNat] at hl
  linarith [Real.log_two_gt_d9]

theorem euclid_log_radius_nonneg_300 (D : Nat)
    (hD : (300 : Nat)^4 ≤ D) :
    0 ≤ Real.log (FirstCertificate.Tuned.euclidRadius D : Real) := by
  have hrho := (FirstCertificate.Tuned.euclid_radius_guards_252 D
    (by omega : (252 : Nat)^4 ≤ D)).1
  apply Real.log_nonneg
  exact_mod_cast (show 1 ≤ FirstCertificate.Tuned.euclidRadius D by omega)

end
end TenthDiscriminant.E18

#print axioms TenthDiscriminant.E18.euclid_radius_coeff_300
#print axioms TenthDiscriminant.E18.euclid_radius_over_R_300
#print axioms TenthDiscriminant.E18.euclid_log_ratio_ge_one_300
