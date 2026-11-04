import TenthDiscriminant.UpperScalars322
import TenthDiscriminant.SourcePositivity322
import TenthDiscriminant.ThinIntegratedEndpoint

/-!
# Phase200: same ORIGINAL thin integer trace-Gram analytic upper at 322^4

This theorem targets the SAME original integerRectangularTraceGram that
receives the already-proved odd-prime and binary divisibility bounds.
No change of ordinary Z-jets, trace pairing, integer-pair observations,
or Gram normalization is allowed.

The padded ellipse enters only through its original CARDINALITY
majorant n; no equality or inequality between the two Gram determinants
is ever assumed. The original thin-source positivity/cardinality
certificate comes from merged Phase170 plus Phase174.

The analytic scalar estimates are rederived under the 322-domain source
conditions in UpperScalars322. This is a research candidate until exact-head
Lean and source-identity checks pass.
-/
namespace TenthDiscriminant.ThinUpper322
open FirstCertificate
open scoped BigOperators Classical
set_option autoImplicit false
noncomputable section

private def oldCountUpper (D : Nat) : Real :=
  ellipsePaddedUpperCount D (Tuned.rho D)
    (ellipseVerticalBound D (Tuned.rho D))

/-- Same ORIGINAL Qthin, ordinary-jet trace Gram and row normalization,
with the old node-count majorant only as the n input to the original
Hadamard upper. No obsolete 450^4 premise is called. -/
theorem thin_production_normalized_upper_322 (D : Nat)
    (hD : (322 : Nat)^4 ≤ D) :
    Real.log ((integerRectangularTraceGram
      (ellipsePairs D (Tuned.thinRadius D)) D
      (Tuned.S D) (Tuned.R D) (Tuned.S D)).det : Real) /
      comparisonScale (Tuned.R D) (Tuned.S D) ≤
      (4/5 : Real)*Real.log D-1853/2000 := by
  have hd := Tuned.dimensions_322 D hD
  have hS : 100 ≤ Tuned.S D := by omega
  have h25 : 25*Tuned.S D ≤ Tuned.R D := by
    unfold Tuned.S
    omega
  have h26 : Tuned.R D ≤ 26*Tuned.S D := by
    unfold Tuned.S
    omega
  have hD0 : 0 < D := by omega
  have hcard := Tuned.thin_radius_interpolation_count_322 D hD
  obtain ⟨h10, hsmaller, hRrho⟩ := Tuned.thin_radius_guards_322 D hD
  have hn : ((ellipsePairs D (Tuned.thinRadius D)).card : Real) ≤
      oldCountUpper D := by
    exact Tuned.thin_card_le_old_padded_majorant_322 D hD
  have hnpos : (0 : Real) < oldCountUpper D := by
    exact Tuned.old_padded_majorant_pos_322 D hD
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
  have hsave := Tuned.upperB_tenth_saving
    (Tuned.R D) (Tuned.S D) (Tuned.rho D)
    (Tuned.thinRadius D) (oldCountUpper D)
    (by omega) (by omega) h25
    (Tuned.radius_pos_322 D hD) (by omega)
    (Tuned.thin_radius_fraction_322 D hD)
  have hold := Tuned.normalized_upper_322 D hD
  dsimp only [oldCountUpper] at hupper hsave hn hnpos
  linarith

end
end TenthDiscriminant.ThinUpper322
