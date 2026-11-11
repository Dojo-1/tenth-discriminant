import TenthDiscriminant.OneNodeTraceControls
import TenthDiscriminant.Phase275TwoSidedTube

/-!
# Phase276 — support breathing does not preserve local p-adic depth

Exact original ordinary-Z-jet trace Gram on the complete (not selected)
ellipsePairs 163 rho, with R=S=J=1. This is a deliberately small
source-domain counterexample, NOT the production R=floor(D/4) source.

Here the only row is the constant monomial 1, so the exact real Gram
increases with the number of samples. But its p-adic determinant depth
need not increase: the SAME nested ellipses move in opposite directions
at two inert primes p=3 and p=5.

This supplements existing Phase167 one/two/empty-node tests and the
Phase205 p-local radical/Smith work. No novelty claim for general
number theory or improved class-number bound.
-/
namespace TenthDiscriminant.Phase276
set_option autoImplicit false
set_option maxRecDepth 4096
set_option maxHeartbeats 1000000

private def Q1 : Finset (Int × Int) := ellipsePairs 163 1
private def Q2 : Finset (Int × Int) := ellipsePairs 163 2
private def Q3 : Finset (Int × Int) := ellipsePairs 163 3

/-- These are all points of the SAME complete ellipse at each radius. -/
theorem source_nesting : Q1 ⊆ Q2 ∧ Q2 ⊆ Q3 := by decide

theorem exact_sample_counts :
    Q1.card = 3 ∧ Q2.card = 5 ∧ Q3.card = 7 := by decide

/-- The *unchanged original* one-row integer trace Gram.
No Hasse jets, modified weights, or selected maximal minor. -/
theorem exact_original_determinants :
    (integerRectangularTraceGram Q1 163 1 1 1).det = 6 ∧
    (integerRectangularTraceGram Q2 163 1 1 1).det = 10 ∧
    (integerRectangularTraceGram Q3 163 1 1 1).det = 14 := by
  constructor
  · decide
  constructor
  · decide
  · decide

theorem real_gram_strictly_increases :
    (integerRectangularTraceGram Q1 163 1 1 1).det <
    (integerRectangularTraceGram Q2 163 1 1 1).det ∧
    (integerRectangularTraceGram Q2 163 1 1 1).det <
    (integerRectangularTraceGram Q3 163 1 1 1).det := by
  obtain ⟨h1,h2,h3⟩ := exact_original_determinants
  rw [h1,h2,h3]
  norm_num

/-- Both -163 mod 3 and -163 mod 5 are nonsquares, so both primes
are inert. This is an arithmetic control, NOT a class-number theorem. -/
theorem inert_three_five_checked :
    (∀ x : ZMod 3, x^2 ≠ -(163 : ZMod 3)) ∧
    (∀ x : ZMod 5, x^2 ≠ -(163 : ZMod 5)) := by decide

/-- The first two *nested full ellipses* reverse their p-local depths:
3 | det(Q1) but not det(Q2), and 5 | det(Q2) but not det(Q1).
An inert-prime support expansion has NO uniform valuation direction. -/
theorem opposite_inert_valuation_changes :
    (3 : Int) ∣ (integerRectangularTraceGram Q1 163 1 1 1).det ∧
    ¬ (3 : Int) ∣ (integerRectangularTraceGram Q2 163 1 1 1).det ∧
    ¬ (5 : Int) ∣ (integerRectangularTraceGram Q1 163 1 1 1).det ∧
    (5 : Int) ∣ (integerRectangularTraceGram Q2 163 1 1 1).det := by
  obtain ⟨h1,h2,_⟩ := exact_original_determinants
  rw [h1,h2]
  norm_num

/-- Even after another support expansion, the p=5 factor is LOST. -/
theorem five_factor_disappears_on_next_breath :
    (5 : Int) ∣ (integerRectangularTraceGram Q2 163 1 1 1).det ∧
    ¬ (5 : Int) ∣ (integerRectangularTraceGram Q3 163 1 1 1).det := by
  obtain ⟨_,h2,h3⟩ := exact_original_determinants
  rw [h2,h3]
  norm_num

#print axioms TenthDiscriminant.Phase276.opposite_inert_valuation_changes
#print axioms TenthDiscriminant.Phase276.five_factor_disappears_on_next_breath
end TenthDiscriminant.Phase276
