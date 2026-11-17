import TenthDiscriminant.Phase347UpperScalars307
import TenthDiscriminant.Phase347SourcePositivity307
import TenthDiscriminant.Phase346Radius307
import TenthDiscriminant.Phase346Radius307

/-!
Phase347 (candidate, UNVERIFIED): this is an exact 307-domain re-derivation
of the source geometry or inequality, not an assumed weakening of a 307 theorem.
No new prime factor or mixed-H valuation is permitted. Retain original Qthin.
# Phase337 — SAME original thin-Q ordinary-jet Gram: 307-domain
# Hadamard upper using the VERIFIED stronger 17/20 radius contraction.

This is NOT a source-determinant reduction between Qthin and Qold;
the padded ellipse is used ONLY as the existing cardinality majorant.
No prime valuation, source lattice, row count or observation changes.
-/
namespace TenthDiscriminant.Phase347
open TenthDiscriminant.FirstCertificate
open scoped BigOperators Classical
set_option autoImplicit false
noncomputable section

private def oldCountUpper (D : Nat) : Real :=
  ellipsePaddedUpperCount D (Tuned.rho D)
    (ellipseVerticalBound D (Tuned.rho D))

/-- Same ORIGINAL Qthin, ordinary-jet trace Gram and row normalization,
with the old node-count majorant only as the n input to the original
Hadamard upper. No obsolete 450^4 premise is called. -/
theorem thin_production_normalized_upper_stronger_307 (D : Nat)
    (hD : (307 : Nat)^4 ≤ D) :
    Real.log ((integerRectangularTraceGram
      (ellipsePairs D (Tuned.thinRadius D)) D
      (Tuned.S D) (Tuned.R D) (Tuned.S D)).det : Real) /
      comparisonScale (Tuned.R D) (Tuned.S D) ≤
      (4/5 : Real)*Real.log D-1923/2000 := by
  have hd := Tuned.dimensions_307 D hD
  have hS : 100 ≤ Tuned.S D := by omega
  have h25 : 25*Tuned.S D ≤ Tuned.R D := by
    unfold Tuned.S
    omega
  have h26 : Tuned.R D ≤ 26*Tuned.S D := by
    unfold Tuned.S
    omega
  have hD0 : 0 < D := by omega
  have hcard := Tuned.thin_radius_interpolation_count_307 D hD
  obtain ⟨h10, hsmaller, hRrho⟩ := Tuned.thin_radius_guards_307 D hD
  have hn : ((ellipsePairs D (Tuned.thinRadius D)).card : Real) ≤
      oldCountUpper D := by
    exact Tuned.thin_card_le_old_padded_majorant_307 D hD
  have hnpos : (0 : Real) < oldCountUpper D := by
    exact Tuned.old_padded_majorant_pos_307 D hD
  have hbound (q : Int × Int)
      (hq : q ∈ ellipsePairs D (Tuned.thinRadius D)) :
      ‖pairEval D q‖ ≤ Tuned.thinRadius D := by
    apply ellipsePoint_norm_le D (Tuned.thinRadius D) hD0
    exact Finset.mem_image.mpr ⟨q,hq,rfl⟩
  have hupper := TightRadialSaving.normalized_integer_upper_tight
    (ellipsePairs D (Tuned.thinRadius D)) D
    (Tuned.R D) (Tuned.S D) (Tuned.thinRadius D)
    (oldCountUpper D)
    hD0 hS h25 h26 h10 hRrho hcard hnpos hn hbound
  have hsave := Tuned.upperB_strong_17_20_saving
    (Tuned.R D) (Tuned.S D) (Tuned.rho D)
    (Tuned.thinRadius D) (oldCountUpper D)
    (by omega) (by omega) h25
    (Tuned.radius_pos_307 D hD) (by omega)
    (Tuned.thin_radius_fraction_17_20_307 D hD)
  have hold := Tuned.normalized_upper_307 D hD
  dsimp only [oldCountUpper] at hupper hsave hn hnpos
  linarith


end
end TenthDiscriminant.Phase347

#print axioms TenthDiscriminant.Phase347.thin_production_normalized_upper_stronger_307
