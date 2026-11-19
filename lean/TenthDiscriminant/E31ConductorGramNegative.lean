import TenthDiscriminant.E30FiniteKernelTransition

/-!
# E31 — Conductor information loss does NOT force an original-Gram prime factor

Source-locked adversarial control against an invalid arithmetic lower
bound. The index-five frame is noninjective modulo five, yet the
ORIGINAL ordinary-Z-jets, the ORIGINAL integer trace pairing, and the
transported two-point support give an exact positive 2x2 Gram of
determinant 4, a unit modulo 5.

The theorem does not falsify any already-proved field cutoff, since
this tiny source does not meet the large-ellipse/class-number premises.
It kills only the unrestricted implication
"ambient conductor kernel ⇒ p divides the sampled original Gram".
-/

namespace TenthDiscriminant.E31
set_option autoImplicit false
noncomputable section

/-- Two original integer lattice witnesses, with positive real span.
No auxiliary complex minor or changed derivative convention. -/
def realSource : Finset (Int × Int) :=
  {(0,0),(1,0)}

/-- Index-five frame leaves these two REAL original source witnesses
unchanged. The map is not surjective on the ambient target lattice. -/
theorem realSource_image_five :
    realSource.image (E24.squareOrderEmbed 5) = realSource := by
  decide

/-- Exact original 2x2 rectangular integer trace Gram, with
ordinary derivative order J=1, rows 1 and Z, and source D=25. -/
theorem actual_original_gram_matrix :
    integerRectangularTraceGram realSource 25 1 2 1 =
      !![4,2;2,2] := by
  decide

/-- This is the actual original determinant, not a selected minor
or continuous lattice-shape approximation. -/
theorem actual_original_gram_det_four :
    (integerRectangularTraceGram realSource 25 1 2 1).det = 4 := by
  rw [actual_original_gram_matrix]
  norm_num [Matrix.det_fin_two]

/-- E24 exact support transport recovers the SAME entire Gram in D=1. -/
theorem original_gram_image_transport :
    integerRectangularTraceGram
        (realSource.image (E24.squareOrderEmbed 5)) 1 1 2 1 =
      integerRectangularTraceGram realSource 25 1 2 1 := by
  simpa using
    (E24.squareOrderEmbed_originalGram realSource 1 5 1 2 1 (by decide))

theorem target_original_gram_det_four :
    (integerRectangularTraceGram
        (realSource.image (E24.squareOrderEmbed 5)) 1 1 2 1).det = 4 := by
  rw [original_gram_image_transport]
  exact actual_original_gram_det_four

/-- The coefficient observer modulo five has a genuine lost fiber. -/
theorem mod5_conductor_five_collision :
    E28.residueFrame 5 5 (0,0) =
        E28.residueFrame 5 5 (0,1) ∧
      ((0,0) : ZMod 5 × ZMod 5) ≠ (0,1) := by
  constructor <;> decide

theorem mod5_conductor_five_not_injective :
    ¬ Function.Injective (E28.residueFrame 5 5) := by
  intro hi
  exact mod5_conductor_five_collision.2
    (hi mod5_conductor_five_collision.1)

/-- Yet the determinant of the original integer Gram is NOT
divisible by the very same bad conductor prime. -/
theorem original_gram_det_not_divisible_five :
    ¬ (5 : Int) ∣
      (integerRectangularTraceGram
        (realSource.image (E24.squareOrderEmbed 5)) 1 1 2 1).det := by
  rw [target_original_gram_det_four]
  norm_num

/-- The explicit counterexample refutes the UNRESTRICTED implication
from local coefficient-information loss to positive 5-adic valuation
of the sampled source determinant. -/
theorem ambient_kernel_does_not_force_gram_five :
    (¬ Function.Injective (E28.residueFrame 5 5)) ∧
      ¬ (5 : Int) ∣
        (integerRectangularTraceGram
          (realSource.image (E24.squareOrderEmbed 5)) 1 1 2 1).det := by
  exact ⟨mod5_conductor_five_not_injective,
    original_gram_det_not_divisible_five⟩

end
end TenthDiscriminant.E31

#print axioms TenthDiscriminant.E31.realSource_image_five
#print axioms TenthDiscriminant.E31.actual_original_gram_matrix
#print axioms TenthDiscriminant.E31.actual_original_gram_det_four
#print axioms TenthDiscriminant.E31.original_gram_image_transport
#print axioms TenthDiscriminant.E31.mod5_conductor_five_not_injective
#print axioms TenthDiscriminant.E31.ambient_kernel_does_not_force_gram_five
