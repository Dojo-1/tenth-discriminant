import TenthDiscriminant.E33ConductorCRTExactness

/-!
# E34 — The first source-locked prime-factor gate for the ORIGINAL integer Gram

The E31 counterexample proves that a conductor's ambient modular kernel
does NOT force a prime factor of the original sampled trace Gram.

E34 formalizes a sufficient condition on ENTRIES OF THE SAME ORIGINAL
integerRectangularTraceGram Q D J 2 1. If one row and column are p-divisible,
with its self-pair divisible by p², then p² divides the actual determinant.

We give two source-exact ordinary-jet, two-point experiments with
equal sampling cardinality in D=25, J=1, R=2, S=1:
  Qunit = {(0,0),(1,0)}  => G=[[4,2],[2,2]], det 4;
  Qfive = {(0,0),(5,0)} => G=[[4,10],[10,50]], det 100.
The difference is in the ORIGINAL sampled ordinary-Z evaluation
witnesses, not a conductor-frame rank statistic.

This small case is not the 307^4 field theorem. It does not justify
a new p-adic lower estimate without a corresponding original-jet
row-factor certificate on the actual thin ellipse.
-/

namespace TenthDiscriminant.E34

set_option autoImplicit false
noncomputable section

/-- Pure integer two-row determinant gate: both offdiagonal entries
must have one p factor, and the second diagonal entry two p factors. -/
theorem two_row_determinant_factor
    (p a b c d : Int)
    (hb : p ∣ b) (hc : p ∣ c) (hd : p*p ∣ d) :
    p*p ∣ a*d - b*c := by
  rcases hb with ⟨u, hu⟩
  rcases hc with ⟨v, hv⟩
  rcases hd with ⟨w, hw⟩
  refine ⟨a*w - u*v, ?_⟩
  rw [hu, hv, hw]
  ring

/-- Crucially, this uses the ACTUAL entire original integer trace Gram
with its original ordinary derivative rows. The theorem's inputs
are exact entry-wise source certificates, not ambient conductor data. -/
theorem original_two_row_gram_prime_factor
    (Q : Finset (Int × Int)) (D J : Nat) (p : Int)
    (h01 : p ∣ (integerRectangularTraceGram Q D J 2 1) 0 1)
    (h10 : p ∣ (integerRectangularTraceGram Q D J 2 1) 1 0)
    (h11 : p*p ∣ (integerRectangularTraceGram Q D J 2 1) 1 1) :
    p*p ∣ (integerRectangularTraceGram Q D J 2 1).det := by
  let G := integerRectangularTraceGram Q D J 2 1
  have hdet : G.det =
      G 0 0 * G 1 1 - G 0 1 * G 1 0 := by
    simp [Matrix.det_fin_two]
  change p*p ∣ G.det
  rw [hdet]
  exact two_row_determinant_factor p
    (G 0 0) (G 0 1) (G 1 0) (G 1 1) h01 h10 h11

/-- Original integer sampling at real coordinates 0 and 5. -/
def realFiveSource : Finset (Int × Int) := {(0,0),(5,0)}

/-- This stays in the E31 source algebra D=25 and original
rectangular ordinary-Z jet convention J=1,R=2,S=1. -/
theorem original_five_gram_matrix :
    integerRectangularTraceGram realFiveSource 25 1 2 1 =
      !![4,10;10,50] := by
  decide

theorem original_five_gram_det :
    (integerRectangularTraceGram realFiveSource 25 1 2 1).det = 100 := by
  rw [original_five_gram_matrix]
  simp [Matrix.det_fin_two] <;> ring

/-- The genuine sampled prime row produces exactly the required
offdiagonal and self-pair divisibilities. -/
theorem original_five_gram_prime_entry_certificate :
    (5 : Int) ∣ (integerRectangularTraceGram realFiveSource 25 1 2 1) 0 1 ∧
    (5 : Int) ∣ (integerRectangularTraceGram realFiveSource 25 1 2 1) 1 0 ∧
    ((5 : Int)*5) ∣ (integerRectangularTraceGram realFiveSource 25 1 2 1) 1 1 := by
  rw [original_five_gram_matrix]
  decide

/-- The integral source-entry gate can now be instantiated on
the exact original positive sampled Gram. -/
theorem original_five_gram_prime_squared_factor :
    ((5 : Int)*5) ∣
      (integerRectangularTraceGram realFiveSource 25 1 2 1).det := by
  rcases original_five_gram_prime_entry_certificate with ⟨h01,h10,h11⟩
  exact original_two_row_gram_prime_factor
    realFiveSource 25 1 5 h01 h10 h11

/-- The same support transported along E24's actual index-five
integral inclusion gives the exact same entire Gram and determinant. -/
theorem original_five_image_gram_det_invariant :
    (integerRectangularTraceGram
      (realFiveSource.image (E24.squareOrderEmbed 5)) 1 1 2 1).det =
      (integerRectangularTraceGram realFiveSource 25 1 2 1).det := by
  exact E24.squareOrderEmbed_originalGram_det realFiveSource
    1 5 1 2 1 (by decide)

/-- The old E31 negative source and the new positive source have
equal CARDINALITY, but not the same sampled arithmetic geometry. -/
theorem equal_number_of_original_samples :
    realFiveSource.card = E31.realSource.card := by
  decide

/-- Two opposite outcomes for exactly the same D,J,R,S
and the same cardinality; no field conclusion follows from either. -/
theorem arithmetic_sampling_not_ambient_conductor_controls_factor :
    (((5 : Int)*5) ∣
      (integerRectangularTraceGram realFiveSource 25 1 2 1).det) ∧
    (¬ (5 : Int) ∣
      (integerRectangularTraceGram E31.realSource 25 1 2 1).det) := by
  constructor
  · exact original_five_gram_prime_squared_factor
  · rw [E31.actual_original_gram_det_four]
    norm_num

end
end TenthDiscriminant.E34

#print axioms TenthDiscriminant.E34.two_row_determinant_factor
#print axioms TenthDiscriminant.E34.original_two_row_gram_prime_factor
#print axioms TenthDiscriminant.E34.original_five_gram_matrix
#print axioms TenthDiscriminant.E34.original_five_gram_prime_entry_certificate
#print axioms TenthDiscriminant.E34.original_five_gram_prime_squared_factor
#print axioms TenthDiscriminant.E34.original_five_image_gram_det_invariant
#print axioms TenthDiscriminant.E34.arithmetic_sampling_not_ambient_conductor_controls_factor
