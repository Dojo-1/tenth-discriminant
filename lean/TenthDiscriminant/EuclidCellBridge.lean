import TenthDiscriminant.EllipseCellArea
import TenthDiscriminant.EnderUpperB

/-!
# E3 — Euclidean cell counting as an original-Gram analytic interface

The EXISTING lattice ellipse and ORIGINAL ordinary-Z derivatives are retained.
A strict area certificate replaces the stronger Ender-radius sufficiency guard
as the proof of the required count. Neither the integral Gram nor its
arithmetic prime factors is changed. This is not a discriminant improvement.
-/

namespace TenthDiscriminant
set_option autoImplicit false
noncomputable section

/-- Use the original cell-area theorem directly, without a separate
Ender radius guard. No change to the lattice or to sample multiplicity. -/
theorem ellipse_card_gt_of_strict_cell_area
    (D rho q : Nat) (hD : 0 < D)
    (hrho : (1 + Real.sqrt D) / 2 ≤ (rho : Real))
    (hstrict : (q : Real) * Real.sqrt D <
      Real.pi * ((rho : Real) - (1 + Real.sqrt D) / 2)^2) :
    q < (ellipsePairs D rho).card := by
  have harea := ellipsePairs_cell_area_bound D rho hD hrho
  have hs : 0 < Real.sqrt (D : Real) :=
    Real.sqrt_pos.2 (by exact_mod_cast hD)
  have hlt : (q : Real) * Real.sqrt D <
      ((ellipsePairs D rho).card : Real) * Real.sqrt D :=
    lt_of_lt_of_le hstrict harea
  have hq : (q : Real) < ((ellipsePairs D rho).card : Real) :=
    (mul_lt_mul_right hs).mp hlt
  exact_mod_cast hq

/-- The exact point-count premise is sufficient for positivity and
the original diagonal Hadamard upper expression. The old sufficient
radius guard is NOT mathematically necessary for this interface. -/
theorem ellipse_log_diag_upper_of_count
    (D rho R S : Nat) (n : Real)
    (hD : 0 < D) (hR : 1 ≤ R) (hS : 1 ≤ S)
    (hrho : 0 < rho) (hRrho : rho < R)
    (hn : ((ellipsePairs D rho).card : Real) ≤ n)
    (hcount : 2 * (R - 1) + (S - 1) < (ellipsePairs D rho).card) :
    Real.log (Finset.univ.prod (fun i =>
      rectangularTraceGram (ellipsePoints D rho) S R S i i)) ≤
      enderUpperB R S S rho n := by
  have hcard : 2 * (R - 1) + (S - 1) <
      (ellipsePoints D rho).card := by
    rwa [ellipsePoints_card D rho hD]
  have hpd := rectangularTraceGram_posDef_of_point_count
    (ellipsePoints D rho) S R S hR hS le_rfl hcard
  have hn' : ((ellipsePoints D rho).card : Real) ≤ n := by
    rwa [ellipsePoints_card D rho hD]
  have hNpos : 0 < (ellipsePoints D rho).card := by omega
  have hNposReal : (0 : Real) < (ellipsePoints D rho).card := by
    exact_mod_cast hNpos
  have hnpos : 0 < n := lt_of_lt_of_le hNposReal hn'
  exact rectangularTraceGram_log_diag_le_upperB
    (ellipsePoints D rho) S R S rho n hrho hRrho
    (by omega) hnpos hn'
    (fun z hz => ellipsePoint_norm_le D rho hD z hz)
    (fun i => real_posDef_diagonal_pos (R * S) _ hpd i)

end
end TenthDiscriminant

#print axioms TenthDiscriminant.ellipse_card_gt_of_strict_cell_area
#print axioms TenthDiscriminant.ellipse_log_diag_upper_of_count
