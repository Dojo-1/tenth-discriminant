import TenthDiscriminant.Phase209OrbitSum
import TenthDiscriminant.Phase209ConjugateFold

/-!
Phase209: exact folding of the ENTIRE ORIGINAL integer ordinary-Z trace-Gram
entry across the ORIGINAL conjugation-stable ellipsePairs source.

The sum of ordinary derivatives on the two conjugate observations is
preserved entrywise. We replace only redundant real/imag observation
columns with integer metric weights 2,4,4D. This module does not prove
the Frobenius row action or weighted Cauchy-Binet p-valuation.
-/
namespace TenthDiscriminant.Phase209WholeGramFold

open TenthDiscriminant

theorem original_real_point_jet_im_zero (D r s j : Nat)
    (q : Int × Int) (hq : q.2 = 0) :
    (integerDerivativeRow D r s j q).2 = 0 := by
  have hfixed : pairConj q = q := by
    rcases q with ⟨x, y⟩
    simp only [Prod.snd] at hq
    simp only [pairConj, Prod.mk.injEq]
    constructor
    · rfl
    · omega
  have hder := integerDerivativeRow_conj D r s j q
  rw [hfixed] at hder
  have him := congrArg Prod.snd hder
  change (integerDerivativeRow D r s j q).2 =
    -(integerDerivativeRow D r s j q).2 at him
  omega

def originalFoldedGramEntry (D rho J r s t u : Nat) : Int :=
  ∑ j ∈ Finset.range J,
    (∑ q ∈ (ellipsePairs D rho).filter (fun q => q.2 = 0),
        2 * (integerDerivativeRow D r s j q).1 *
            (integerDerivativeRow D t u j q).1) +
    (∑ q ∈ (ellipsePairs D rho).filter (fun q => 0 < q.2),
        4 * (integerDerivativeRow D r s j q).1 *
            (integerDerivativeRow D t u j q).1 +
        (4*(D : Int)) * (integerDerivativeRow D r s j q).2 *
            (integerDerivativeRow D t u j q).2)

theorem original_trace_gram_entry_fold (D rho J r s t u : Nat)
    (hD : 0 < D) :
    integerTraceGramEntry (ellipsePairs D rho) D J r s t u =
      originalFoldedGramEntry D rho J r s t u := by
  classical
  unfold integerTraceGramEntry originalFoldedGramEntry
  apply Finset.sum_congr rfl
  intro j hj
  let f : Int × Int → Int := fun q =>
    integerPairTrace D (integerDerivativeRow D r s j q)
      (integerDerivativeRow D t u j q)
  have hf : ∀ q : Int × Int, f (pairConj q) = f q := by
    intro q
    exact integerPairTrace_derivatives_conj D r s t u j q
  have hs := sum_original_ellipse_orbits D rho hD f hf
  have hreal :
      (∑ q ∈ (ellipsePairs D rho).filter (fun q => q.2 = 0), f q) =
      (∑ q ∈ (ellipsePairs D rho).filter (fun q => q.2 = 0),
          2 * (integerDerivativeRow D r s j q).1 *
              (integerDerivativeRow D t u j q).1) := by
    apply Finset.sum_congr rfl
    intro q hq
    have h0 := (Finset.mem_filter.mp hq).2
    have ha := original_real_point_jet_im_zero D r s j q h0
    have hb := original_real_point_jet_im_zero D t u j q h0
    dsimp only [f]
    simp only [integerPairTrace, ha, hb, mul_zero, zero_mul, add_zero]
    ring
  have hpos :
      2 * (∑ q ∈ (ellipsePairs D rho).filter (fun q => 0 < q.2), f q) =
      (∑ q ∈ (ellipsePairs D rho).filter (fun q => 0 < q.2),
        4 * (integerDerivativeRow D r s j q).1 *
            (integerDerivativeRow D t u j q).1 +
        (4*(D : Int)) * (integerDerivativeRow D r s j q).2 *
            (integerDerivativeRow D t u j q).2) := by
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro q hq
    dsimp only [f]
    simp only [integerPairTrace]
    ring
  calc
    (∑ q ∈ ellipsePairs D rho, f q) =
      (∑ q ∈ (ellipsePairs D rho).filter (fun q => q.2 = 0), f q) +
      2 * (∑ q ∈ (ellipsePairs D rho).filter (fun q => 0 < q.2), f q) := hs
    _ = _ := by rw [hreal, hpos]

def originalFoldedRectangularGram (D rho J R S : Nat) :
    Matrix (Fin (R*S)) (Fin (R*S)) Int :=
  fun i k =>
    originalFoldedGramEntry D rho J
      (i.val / S) (i.val % S) (k.val / S) (k.val % S)

theorem original_rectangular_gram_folds (D rho J R S : Nat) (hD : 0 < D) :
    integerRectangularTraceGram (ellipsePairs D rho) D J R S =
      originalFoldedRectangularGram D rho J R S := by
  ext i k
  exact original_trace_gram_entry_fold D rho J
    (i.val / S) (i.val % S) (k.val / S) (k.val % S) hD

end TenthDiscriminant.Phase209WholeGramFold

#print axioms TenthDiscriminant.Phase209WholeGramFold.original_trace_gram_entry_fold
#print axioms TenthDiscriminant.Phase209WholeGramFold.original_rectangular_gram_folds
