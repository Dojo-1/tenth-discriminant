import TenthDiscriminant.E26ArithmeticHolonomy

/-!
# E27 — Arithmetic moving-moving-frame naturality on the actual source Gram

The source quadratic algebra/order can change via the square-index
embedding, while an independent within-regime conjugation holonomy
acts at BOTH ends. Their square commutes on every integer witness,
and the original ordinary-jet Gram agrees along both paths.

The complete source-lattice image is transported. No field equivalence
for unrelated square classes or order-surjective inverse is asserted.
-/
namespace TenthDiscriminant.E27
set_option autoImplicit false
noncomputable section

/-- The actual order morphism intertwines source and target conjugation
automorphisms. This is a moving-observer naturality square. -/
theorem algebraHolonomy_natural (k : Nat) (p : Int × Int) :
    E24.squareOrderEmbed k (pairConj p) =
      pairConj (E24.squareOrderEmbed k p) :=
  E24.squareOrderEmbed_conj k p

/-- First move source observations by their conjugation holonomy,
then change arithmetic regime; the original Gram is unchanged. -/
theorem conjugate_then_change_regime_originalGram
    (Q : Finset (Int × Int))
    (D k J R S : Nat) (hk : 0 < k) :
    integerRectangularTraceGram
      ((Q.image pairConj).image (E24.squareOrderEmbed k))
        D J R S =
    integerRectangularTraceGram Q (D*k*k) J R S := by
  calc
    _ = integerRectangularTraceGram
        (Q.image pairConj) (D*k*k) J R S :=
      E24.squareOrderEmbed_originalGram
        (Q.image pairConj) D k J R S hk
    _ = integerRectangularTraceGram Q (D*k*k) J R S :=
      integerRectangularTraceGram_conj Q (D*k*k) J R S

/-- First change arithmetic regime, then transport the target
conjugation holonomy; this second route has the same source Gram. -/
theorem change_regime_then_conjugate_originalGram
    (Q : Finset (Int × Int))
    (D k J R S : Nat) (hk : 0 < k) :
    integerRectangularTraceGram
      ((Q.image (E24.squareOrderEmbed k)).image pairConj)
        D J R S =
    integerRectangularTraceGram Q (D*k*k) J R S := by
  calc
    _ = integerRectangularTraceGram
        (Q.image (E24.squareOrderEmbed k)) D J R S :=
      integerRectangularTraceGram_conj
        (Q.image (E24.squareOrderEmbed k)) D J R S
    _ = integerRectangularTraceGram Q (D*k*k) J R S :=
      E24.squareOrderEmbed_originalGram Q D k J R S hk

/-- Both moving-frame paths preserve the original integer Gram.
This is a SOURCE-EXACT commuting-square result, not a numerical
similarity of two independently generated observations. -/
theorem moving_arithmetic_holonomy_originalGram_coherence
    (Q : Finset (Int × Int))
    (D k J R S : Nat) (hk : 0 < k) :
    integerRectangularTraceGram
      ((Q.image pairConj).image (E24.squareOrderEmbed k))
        D J R S =
    integerRectangularTraceGram
      ((Q.image (E24.squareOrderEmbed k)).image pairConj)
        D J R S := by
  exact (conjugate_then_change_regime_originalGram Q D k J R S hk).trans
    (change_regime_then_conjugate_originalGram Q D k J R S hk).symm

/-- The corresponding determinants agree, with the original row
order, number of derivative channels, and integer trace unchanged. -/
theorem moving_arithmetic_holonomy_det_coherence
    (Q : Finset (Int × Int))
    (D k J R S : Nat) (hk : 0 < k) :
    (integerRectangularTraceGram
      ((Q.image pairConj).image (E24.squareOrderEmbed k))
        D J R S).det =
    (integerRectangularTraceGram Q (D*k*k) J R S).det := by
  rw [conjugate_then_change_regime_originalGram Q D k J R S hk]

end
end TenthDiscriminant.E27

#print axioms TenthDiscriminant.E27.algebraHolonomy_natural
#print axioms TenthDiscriminant.E27.conjugate_then_change_regime_originalGram
#print axioms TenthDiscriminant.E27.moving_arithmetic_holonomy_originalGram_coherence
#print axioms TenthDiscriminant.E27.moving_arithmetic_holonomy_det_coherence
