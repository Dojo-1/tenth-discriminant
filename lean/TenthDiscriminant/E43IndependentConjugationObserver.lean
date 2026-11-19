import TenthDiscriminant.E41ComplexSourceSignObserver
import TenthDiscriminant.ObservationConjugation

/-!
# E43 — Independent per-point conjugation observer quotient

The existing ObservationConjugation theorem already proves that
conjugating ALL original samples leaves the full trace Gram
unchanged for arbitrary D,J,R,S. This module extends the
source-data result in a distinct direction:

Given ANY map f that takes each original q in finite Q either
to q itself or to pairConj q, if f is INJECTIVE ON THE ORIGINAL Q,
the entire original positive trace Gram is unchanged.

This is a per-observation fiber symmetry of the ORIGINAL ordinary
jet/trace source, not a new curvature, ring or determinant theorem.
Its hypotheses prevent silently collapsing two finite samples
into one under a noninjective partial conjugation.

It proves that the E41 sign-observer collision survives ALL
rectangular ordinary-jet row counts and derivative orders,
not just the 1,Z toy regime. Matched collision control shows why
injectivity is mandatory.
-/

namespace TenthDiscriminant.E43
set_option autoImplicit false
noncomputable section

/-- For the ORIGINAL source set and ordinary jet trace, any independent
per-point conjugation that is injective on Q is entirely invisible to
the full rectangular Gram, for all D,J,R,S. -/
theorem original_gram_invariant_under_injective_pointwise_conjugations
    (Q : Finset (Int × Int)) (D J R S : Nat)
    (f : Int × Int → Int × Int)
    (hinj : Set.InjOn f Q)
    (hflip : ∀ q ∈ Q, f q = q ∨ f q = pairConj q) :
    integerRectangularTraceGram (Q.image f) D J R S =
      integerRectangularTraceGram Q D J R S := by
  ext i k
  change
    integerTraceGramEntry (Q.image f) D J
      (i.val / S) (i.val % S) (k.val / S) (k.val % S) =
    integerTraceGramEntry Q D J
      (i.val / S) (i.val % S) (k.val / S) (k.val % S)
  unfold integerTraceGramEntry
  apply Finset.sum_congr rfl
  intro j hj
  rw [Finset.sum_image hinj]
  apply Finset.sum_congr rfl
  intro q hq
  rcases hflip q hq with heq | heq
  · rw [heq]
  · rw [heq]
    exact integerPairTrace_derivatives_conj D
      (i.val / S) (i.val % S) (k.val / S) (k.val % S)
      j q

/-- Toggle only the sample with real coordinate 1; this is NOT
conjugation of the whole source. -/
def flipRealOne (q : Int × Int) : Int × Int :=
  if q.1 = 1 then pairConj q else q

theorem flipRealOne_involution (q : Int × Int) :
    flipRealOne (flipRealOne q) = q := by
  rcases q with ⟨x,y⟩
  by_cases hx : x = 1
  · simp [flipRealOne, pairConj, hx]
  · simp [flipRealOne, pairConj, hx]

theorem flipRealOne_injective :
    Function.Injective flipRealOne := by
  intro a b h
  have hh := congrArg flipRealOne h
  simpa only [flipRealOne_involution] using hh

theorem flipRealOne_is_partial_conjugation
    (q : Int × Int) :
    flipRealOne q = q ∨ flipRealOne q = pairConj q := by
  by_cases h : q.1 = 1
  · right
    simp [flipRealOne, h]
  · left
    simp [flipRealOne, h]

/-- Two truly different source supports are identified by exactly
one per-point conjugation, not by global conjugation. -/
theorem partial_flip_source_image :
    (E41.complexTwoSource 0 1 1 1).image flipRealOne =
      E41.complexTwoSource 0 1 1 (-1) := by
  decide

theorem partial_flip_not_global_conjugation :
    E41.complexTwoSource 0 1 1 (-1) ≠
      (E41.complexTwoSource 0 1 1 1).image pairConj := by
  decide

/-- Stronger than E41: no choice of R,S,J under the ORIGINAL
pointwise positive trace Gram distinguishes these two supports. -/
theorem non_global_partial_sign_collision_all_original_jets
    (D J R S : Nat) :
    integerRectangularTraceGram
      (E41.complexTwoSource 0 1 1 (-1)) D J R S =
    integerRectangularTraceGram
      (E41.complexTwoSource 0 1 1 1) D J R S := by
  rw [← partial_flip_source_image]
  exact original_gram_invariant_under_injective_pointwise_conjugations
    (E41.complexTwoSource 0 1 1 1) D J R S
    flipRealOne flipRealOne_injective.injOn
    (by
      intro q hq
      exact flipRealOne_is_partial_conjugation q)

/-- Collision control: toggling only one point of a conjugate pair
maps it onto the OTHER point and destroys one original Finset member.
This is why injectivity in the general theorem cannot be dropped. -/
def flipOnlyPositiveImag (q : Int × Int) : Int × Int :=
  if q = (0,1) then pairConj q else q

def collidingSource : Finset (Int × Int) :=
  {(0,1),(0,-1)}

theorem noninjective_partial_flip_collapses_support :
    collidingSource.image flipOnlyPositiveImag = {(0,-1)} := by
  decide

theorem noninjective_flip_changes_original_gram :
    integerRectangularTraceGram
      (collidingSource.image flipOnlyPositiveImag) 3 1 2 1 ≠
    integerRectangularTraceGram collidingSource 3 1 2 1 := by
  decide

end
end TenthDiscriminant.E43

#print axioms TenthDiscriminant.E43.original_gram_invariant_under_injective_pointwise_conjugations
#print axioms TenthDiscriminant.E43.flipRealOne_involution
#print axioms TenthDiscriminant.E43.non_global_partial_sign_collision_all_original_jets
#print axioms TenthDiscriminant.E43.noninjective_flip_changes_original_gram
