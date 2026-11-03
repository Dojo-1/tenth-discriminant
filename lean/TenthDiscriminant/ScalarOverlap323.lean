import TenthDiscriminant.Phase199Scalar323

/-!
Phase196: scalar contradiction connector. Uses only sound 323 logarithm
enclosure and the proposed *matching* original-source bounds. The
existence of the determinant upper/lower bounds is NOT proved here.
-/
namespace TenthDiscriminant
set_option autoImplicit false
noncomputable section

theorem no_abstract_scalar_overlap_323
    (D : Nat) (hD : (323 : Nat)^4 ≤ D) (g : Real)
    (hUpper : g ≤ (4/5 : Real)*Real.log D-1851/2000)
    (hLower : (999997/1000000 : Real)*Real.log D-57205/10000+
      Real.log 2/4 ≤ g) : False := by
  have hu := log_floor_from_323_fourth_power D hD
  have hgap := strict_affine_separator_323 (Real.log D) hu
  linarith


end
end TenthDiscriminant
