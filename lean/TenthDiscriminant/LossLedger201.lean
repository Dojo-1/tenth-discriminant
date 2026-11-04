import Mathlib

/-!
# Round201 — the first certified non-injectivity of an arithmetic observation

Two distinct positive integer 2x2 test Grams have the same entrywise
divisibility-by-three pattern but determinant valuations of different depth.
This is a mathematically elementary regression, not the original D=19
ordinary-jet source and not a number-field discriminant theorem.

The claim deliberately uses only integer matrices and the exact determinant:
no F1 scheme, tropical bend object, generic kernel-cardinality theorem,
or undocumented field-theory assumption is smuggled into its statement.
-/

namespace TenthDiscriminant.LossLedger201
open Matrix
set_option autoImplicit false

def gramA : Matrix (Fin 2) (Fin 2) Int :=
  !![1, 1; 1, 4]

def gramB : Matrix (Fin 2) (Fin 2) Int :=
  !![1, 1; 1, 10]

theorem gramA_det : gramA.det = 3 := by
  norm_num [gramA, Matrix.det_fin_two]

theorem gramB_det : gramB.det = 9 := by
  norm_num [gramB, Matrix.det_fin_two]

/-- Every entry in both matrices is a 3-adic unit. Their coarse
entrywise mod-3 unit masks are identical. -/
theorem same_entry_three_divisibility :
    ∀ i j : Fin 2,
      ((3 : Int) ∣ gramA i j) ↔ ((3 : Int) ∣ gramB i j) := by
  intro i j
  fin_cases i <;> fin_cases j <;> norm_num [gramA, gramB]

/-- Their determinant valuations differ already at level 3^2.
This is a valuation-depth distinction, not merely det inequality. -/
theorem different_three_adic_det_depth :
    (3 : Int) ∣ gramA.det ∧ (3 : Int) ∣ gramB.det ∧
      ¬ (9 : Int) ∣ gramA.det ∧ (9 : Int) ∣ gramB.det := by
  norm_num [gramA_det, gramB_det]

/-- A universal reconstruction of the determinant from the binary
entry-divisibility mask is impossible, witnessed by the two matrices above. -/
theorem entry_three_mask_not_faithful :
    ¬ (∀ G H : Matrix (Fin 2) (Fin 2) Int,
        (∀ i j : Fin 2, ((3 : Int) ∣ G i j) ↔ ((3 : Int) ∣ H i j)) →
        G.det = H.det) := by
  intro reconstruction
  have h := reconstruction gramA gramB same_entry_three_divisibility
  rw [gramA_det, gramB_det] at h
  norm_num at h

end TenthDiscriminant.LossLedger201
