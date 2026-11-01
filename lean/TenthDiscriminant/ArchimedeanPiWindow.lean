import Mathlib.Analysis.Real.Pi.Bounds

/-!
# Phase157: certified rational pi window for the original jet ellipse

These are source-independent classical and rational gates. They DO NOT prove
the Frobenius rank, Voronoi area comparisons, or any numerical class-number
field endpoint. Importing the library's pi bounds avoids a new numerical axiom.
-/
namespace TenthDiscriminant
set_option autoImplicit false

/-- Mathematically certified Archimedean area coefficient: use 157/50
instead of 3 in the original disk-volume argument. -/
theorem pi_jet_area_window :
    (157 / 50 : Real) < Real.pi ∧ Real.pi < (63 / 20 : Real) := by
  constructor
  · convert Real.pi_gt_d2 using 1 <;> norm_num
  · convert Real.pi_lt_d2 using 1 <;> norm_num

/-- Frozen exact rational outer cell-area gate at D^(1/4)>265.
The full lattice geometry is a separate theorem obligation. -/
theorem jet_area_ratio_gate :
    ((63 / 20 : Rat) / (157 / 50)) *
        (1 + (39 / (10 * 265) : Rat) + 4 / 265 ^ 3) ^ 2 <
      26 / 25 := by
  norm_num

/-- Frozen exact rational normalized radius gate. -/
theorem jet_radius_ratio_gate :
    (5 / (4 * 265) : Rat) *
        (1 + (39 / (20 * 265) : Rat) + 4 / 265 ^ 3) *
        (1 + (1 / (10 ^ 9) : Rat)) < 1 / 200 := by
  norm_num

end TenthDiscriminant
