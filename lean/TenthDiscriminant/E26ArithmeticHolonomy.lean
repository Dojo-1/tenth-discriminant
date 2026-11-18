import TenthDiscriminant.ObservationConjugation
import TenthDiscriminant.E25NestedArithmeticFrames

/-!
# E26 — Arithmetic holonomy: invariant Gram, changing witness channel

A closed source-frame loop may act by the nontrivial quadratic conjugation
automorphism. The ORIGINAL ordinary-jet trace Gram is invariant on the
fully transported sampling support, but the underlying witness and an
orientation-sensitive future operation are not.

This is NOT a proof that nontrivial holonomy implies Riemannian curvature,
nontrivial Galois action between unrelated fields, or a class-number bound.
-/
namespace TenthDiscriminant.E26
set_option autoImplicit false
noncomputable section

/-- The norm is an arithmetic observation of the selected pair lattice. -/
def quadraticNorm (D : Nat) (p : Int × Int) : Int :=
  p.1*p.1 + (D : Int)*p.2*p.2

/-- Conjugation preserves the observed norm at every source point. -/
theorem quadraticNorm_conj (D : Nat) (p : Int × Int) :
    quadraticNorm D (pairConj p) = quadraticNorm D p := by
  simp [quadraticNorm, pairConj]
  ring

/-- This path loop is a genuine nonidentity arithmetic automorphism. -/
theorem conjugation_loop_moves_witness :
    pairConj (0,1) ≠ ((0,1) : Int × Int) := by
  decide

/-- A fully transported source sample support preserves the original
rectangular integer Gram, while actual source witnesses can move. -/
theorem nontrivial_witness_motion_with_same_original_gram
    (Q : Finset (Int × Int)) (D J R S : Nat) :
    pairConj (0,1) ≠ ((0,1) : Int × Int) ∧
      quadraticNorm D (pairConj (0,1)) =
        quadraticNorm D (0,1) ∧
      integerRectangularTraceGram (Q.image pairConj) D J R S =
        integerRectangularTraceGram Q D J R S := by
  exact ⟨conjugation_loop_moves_witness,
    quadraticNorm_conj D (0,1),
    integerRectangularTraceGram_conj Q D J R S⟩

/-- A future partial observer remembers the orientation omitted by the
norm. It is not forced to be invariant under arithmetic conjugation. -/
def positiveHalfObservation (p : Int × Int) : Option Int :=
  if 0 < p.2 then some p.1 else none

theorem positiveHalfObservation_before :
    positiveHalfObservation (0,1) = some 0 := by
  norm_num [positiveHalfObservation]

theorem positiveHalfObservation_after :
    positiveHalfObservation (pairConj (0,1)) = none := by
  norm_num [positiveHalfObservation, pairConj]

theorem conjugation_changes_future_definedness :
    positiveHalfObservation (pairConj (0,1)) ≠
      positiveHalfObservation (0,1) := by
  rw [positiveHalfObservation_after, positiveHalfObservation_before]
  decide

/-- Same current quadratic norm does not permit reconstruction of a
future partial action, because the original witness fiber contains
the distinct +y and -y orientations. -/
theorem norm_observer_cannot_decode_future (D : Nat) :
    ¬ ∃ f : Int → Option Int,
        ∀ p : Int × Int,
          f (quadraticNorm D p) = positiveHalfObservation p := by
  rintro ⟨f,hf⟩
  have hp := hf (0,1)
  have hn := hf (0,-1)
  have hnorm : quadraticNorm D (0,1) =
      quadraticNorm D (0,-1) := by
    norm_num [quadraticNorm]
  rw [hnorm] at hp
  have hsame : positiveHalfObservation (0,1) =
      positiveHalfObservation (0,-1) :=
    hp.symm.trans hn
  norm_num [positiveHalfObservation] at hsame

/-- The Gram is a coarser observer than the ORIGINAL derivative channel:
exact Gram invariance is not channel-by-channel identity. -/
theorem source_channel_not_pointwise_invariant :
    integerDerivativeRow 3 0 1 0 (0,1) ≠
      integerDerivativeRow 3 0 1 0 (0,-1) :=
  integerDerivativeRow_conj_changes_channel

end
end TenthDiscriminant.E26

#print axioms TenthDiscriminant.E26.quadraticNorm_conj
#print axioms TenthDiscriminant.E26.nontrivial_witness_motion_with_same_original_gram
#print axioms TenthDiscriminant.E26.conjugation_changes_future_definedness
#print axioms TenthDiscriminant.E26.norm_observer_cannot_decode_future
#print axioms TenthDiscriminant.E26.source_channel_not_pointwise_invariant
