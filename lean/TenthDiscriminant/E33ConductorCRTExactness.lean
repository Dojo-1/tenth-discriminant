import TenthDiscriminant.E32RegimeNilpotentSplit

/-!
# E33 — Elementary exact sequence for conductor transport and split-prime observers

At the conductor prime 5, the source ring A25/5 has a nilpotent
coefficient direction. The target Gaussian ring A1/5 splits into two
prime-labelled F5 observations. The exact ORIGINAL E28 conductor map
kills exactly the source nilpotent direction. The target's missing
direction can be read by the difference of the two split-prime labels.

This file encodes ELEMENTWISE exactness of an F5-additive sequence:
  0 -> F5 -> A25/5 -> A1/5 -> F5 -> 0.
It does NOT instantiate the full Mathlib exact-sequence API or claim
the final prime-gap map is a ring homomorphism. No p-adic valuation
or source-Gram determinant factor is inferred.
-/

namespace TenthDiscriminant.E33
set_option autoImplicit false
noncomputable section

/-- The explicit source nilpotent coefficient direction. -/
def epsilonInclude (b : ZMod 5) : ZMod 5 × ZMod 5 :=
  (0,b)

/-- The EXACT E28 conductor-five modular coefficient frame. -/
def conductor (p : ZMod 5 × ZMod 5) : ZMod 5 × ZMod 5 :=
  E28.residueFrame 5 5 p

/-- The target's two different Gaussian split-prime labels define
an additive residual direction (difference, not a ring map). -/
def primeGap (p : ZMod 5 × ZMod 5) : ZMod 5 :=
  E28.splitMinus p - E28.splitPlus p

theorem epsilonInclude_injective :
    Function.Injective epsilonInclude := by
  intro b c h
  have hs := congrArg Prod.snd h
  simpa [epsilonInclude] using hs

/-- Exactly the original conductor-frame kernel, nothing larger. -/
theorem conductor_kernel_iff_epsilon_image :
    ∀ p : ZMod 5 × ZMod 5,
      conductor p = (0,0) ↔
        ∃ b : ZMod 5, epsilonInclude b = p := by
  decide

/-- The two prime-labelled target residues agree exactly on the
image of the nonmaximal source, rather than on arbitrary target points. -/
theorem prime_gap_kernel_iff_conductor_image :
    ∀ q : ZMod 5 × ZMod 5,
      primeGap q = 0 ↔
        ∃ p : ZMod 5 × ZMod 5, conductor p = q := by
  decide

/-- The missing target direction is actually observable and
unconstrained: every F5 prime-label difference occurs. -/
theorem prime_gap_surjective :
    Function.Surjective primeGap := by
  decide

/-- Both composites vanish, as they must for the claimed exactness. -/
theorem conductor_kills_epsilon (b : ZMod 5) :
    conductor (epsilonInclude b) = (0,0) := by
  have hz : (5 : ZMod 5) = 0 := by decide
  simp [conductor, epsilonInclude, E28.residueFrame, hz]

theorem prime_gap_kills_conductor (p : ZMod 5 × ZMod 5) :
    primeGap (conductor p) = 0 := by
  have hz : (5 : ZMod 5) = 0 := by decide
  rcases p with ⟨a,b⟩
  simp [primeGap, conductor, E28.residueFrame,
    E28.splitMinus, E28.splitPlus, hz]

/-- Full elementary witness-level exactness (kernel=image at
both middle terms, with injective first and surjective last). -/
theorem conductor_prime_exact_sequence :
    Function.Injective epsilonInclude ∧
      (∀ p : ZMod 5 × ZMod 5,
        conductor p = (0,0) ↔
          ∃ b : ZMod 5, epsilonInclude b = p) ∧
      (∀ q : ZMod 5 × ZMod 5,
        primeGap q = 0 ↔
          ∃ p : ZMod 5 × ZMod 5, conductor p = q) ∧
      Function.Surjective primeGap := by
  exact ⟨epsilonInclude_injective,
    conductor_kernel_iff_epsilon_image,
    prime_gap_kernel_iff_conductor_image,
    prime_gap_surjective⟩

/-- Retain the actual arithmetic source map; its multiplication
compatibility comes directly from E28. The additive exact sequence
does not substitute a new number-field or ideal API. -/
theorem conductor_preserves_source_multiplication
    (p q : ZMod 5 × ZMod 5) :
    conductor (E28.residueMul 5 25 p q) =
      E28.residueMul 5 1 (conductor p) (conductor q) := by
  simpa [conductor] using E28.residueFrame_mul 5 1 5 p q

/-- This is the exact CRT information readout: the two
split-prime residues coincide after a conductor-five frame. -/
theorem conductor_image_prime_labels_coincide
    (p : ZMod 5 × ZMod 5) :
    E28.splitMinus (conductor p) =
      E28.splitPlus (conductor p) := by
  have hgap := prime_gap_kills_conductor p
  exact sub_eq_zero.mp hgap

end
end TenthDiscriminant.E33

#print axioms TenthDiscriminant.E33.epsilonInclude_injective
#print axioms TenthDiscriminant.E33.conductor_kernel_iff_epsilon_image
#print axioms TenthDiscriminant.E33.prime_gap_kernel_iff_conductor_image
#print axioms TenthDiscriminant.E33.prime_gap_surjective
#print axioms TenthDiscriminant.E33.conductor_prime_exact_sequence
#print axioms TenthDiscriminant.E33.conductor_preserves_source_multiplication
