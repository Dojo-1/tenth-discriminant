import TenthDiscriminant.InertFrobenius
import Mathlib.Algebra.Polynomial.BigOperators
import Mathlib.Algebra.Polynomial.Roots

/-!
# Phase223: finite-support minimal annihilator (source-linked)

This module proves the universal field-root bound and the degree of the
monic finite-support annihilator. It does not identify an arbitrary
quadratic residue ring with a field without the inertness hypothesis.
The finite D=19 witnesses are based on the ORIGINAL ellipsePairs support.
No numerical discriminant endpoint is asserted here.
-/

namespace TenthDiscriminant.Phase223

open Polynomial
open scoped BigOperators

/-- The monic annihilator of a finite subset of a field. -/
noncomputable def supportAnnihilator {K : Type*} [Field K]
    (S : Finset K) : Polynomial K :=
  ∏ a ∈ S, (Polynomial.X - Polynomial.C a)

/-- The number of distinct support elements is exactly the degree. -/
theorem supportAnnihilator_natDegree {K : Type*} [Field K]
    (S : Finset K) :
    (supportAnnihilator S).natDegree = S.card := by
  classical
  unfold supportAnnihilator
  rw [Polynomial.natDegree_prod]
  · simp
  · intro a ha
    exact Polynomial.X_sub_C_ne_zero a

/-- Each element of the support is an exact root. -/
theorem supportAnnihilator_eval_zero {K : Type*} [Field K]
    (S : Finset K) (a : K) (ha : a ∈ S) :
    Polynomial.eval a (supportAnnihilator S) = 0 := by
  classical
  unfold supportAnnihilator
  rw [Polynomial.eval_prod]
  apply Finset.prod_eq_zero ha
  simp

/-- Minimality among all nonzero polynomials vanishing on the same
finite field support. No claim of novelty: this is the classical root bound. -/
theorem supportAnnihilator_optimal {K : Type*} [Field K]
    (S : Finset K) (P : Polynomial K) (hP : P ≠ 0)
    (hvanish : ∀ a ∈ S, Polynomial.eval a P = 0) :
    (supportAnnihilator S).natDegree ≤ P.natDegree := by
  rw [supportAnnihilator_natDegree]
  apply Polynomial.card_le_degree_of_subset_roots
  intro a ha
  exact (Polynomial.mem_roots' (p := P) (a := a)).2
    ⟨hP, hvanish a ha⟩

/-- Exact original coordinate support, including complex conjugation. -/
def originalResidueSupport (D rho p : Nat) : Finset (ZMod p × ZMod p) :=
  (ellipsePairs D rho).image fun a =>
    ((a.1 : ZMod p), -(a.2 : ZMod p))

/-- D=19, p=13, rho=9: 49 distinct conjugate residue samples.
These are ORIGINAL integer-pair ellipse observations. -/
theorem original_residue_support_19_13_9 :
    (originalResidueSupport 19 9 13).card = 49 := by
  decide

/-- D=19, p=3, rho=9: all nine quadratic residue pairs are visited. -/
theorem original_residue_support_19_3_9 :
    originalResidueSupport 19 9 3 = Finset.univ := by
  decide

end TenthDiscriminant.Phase223

#print axioms TenthDiscriminant.Phase223.supportAnnihilator_natDegree
#print axioms TenthDiscriminant.Phase223.supportAnnihilator_eval_zero
#print axioms TenthDiscriminant.Phase223.supportAnnihilator_optimal
#print axioms TenthDiscriminant.Phase223.original_residue_support_19_13_9
#print axioms TenthDiscriminant.Phase223.original_residue_support_19_3_9
