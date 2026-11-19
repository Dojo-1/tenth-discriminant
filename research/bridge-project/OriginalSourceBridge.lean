import TenthDiscriminant.IntegerTraceGram
import HardnessKernel.GaussianSourceAdapter

/-!
# E39 / HK-035 — Actual two-package positive-trace and original-jet bridge

This file IMPORTS declarations from both repositories, using the
same Lean v4.19.0 toolchain and an explicit local Lake dependency
workspace. It closes the former copied-formula limitation of HK-034.

The original source is TenthDiscriminant.integerDerivativeRow,
integerPairTrace and integerRectangularTraceGram. HK's gpair must
receive the CONJUGATE of its second Gaussian input. No Q, ordinary
jet, trace weight, row enumeration or signed metric is substituted.
-/

namespace OriginalSourceBridge

open HardnessKernel.GaussianPrime
open HardnessKernel.GaussianSourceAdapter

set_option autoImplicit false
noncomputable section

/-- Exact source-carrier multiplication, using both REAL package
declarations, not copied proof surrogates. -/
theorem gaussian_mul_is_original_pair_mul (a b : Int × Int) :
    asPair (gmul (fromPair a) (fromPair b)) =
      TenthDiscriminant.pairMul 1 a b := by
  rw [pair_multiplication_exact]
  rcases a with ⟨a,b⟩
  rcases b with ⟨c,d⟩
  simp [asPair_fromPair, sourcePairMul, TenthDiscriminant.pairMul]

/-- The original conjugation operation is preserved exactly. -/
theorem gaussian_conj_is_original_pair_conj (a : Int × Int) :
    asPair (gconj (fromPair a)) =
      TenthDiscriminant.pairConj a := by
  rw [pair_conjugation_exact]
  rcases a with ⟨a,b⟩
  simp [sourcePairConj, asPair_fromPair, TenthDiscriminant.pairConj]

/-- THE cross-repository corrected positive trace identity:
HK's unconjugated gpair needs its second Gaussian input conjugated. -/
theorem gaussian_positive_trace_is_original_trace
    (a b : Int × Int) :
    gpair (fromPair a) (gconj (fromPair b)) =
      TenthDiscriminant.integerPairTrace 1 a b := by
  have h := gaussian_conjugated_trace_is_source_positive_trace
    (fromPair a) (fromPair b)
  simpa [sourcePairTrace, asPair_fromPair,
    TenthDiscriminant.integerPairTrace] using h

/-- Explicit negative control: direct un-conjugated HK trace is
NOT the positive original trace at i. -/
theorem wrong_unconjugated_source_metric :
    gpair (fromPair (0,1)) (fromPair (0,1)) = -2 ∧
      TenthDiscriminant.integerPairTrace 1 (0,1) (0,1) = 2 := by
  decide

/-- Read the HK-corrected positive trace on the actual original
Tenth ordinary derivatives, not on replacement derivatives. -/
def hkOriginalEntry
    (Q : Finset (Int × Int)) (J r s t u : Nat) : Int :=
  (Finset.range J).sum (fun j =>
    Q.sum (fun q =>
      gpair
        (fromPair (TenthDiscriminant.integerDerivativeRow 1 r s j q))
        (gconj (fromPair
          (TenthDiscriminant.integerDerivativeRow 1 t u j q)))))

/-- Each original source entry agrees at arbitrary Q,J and row
labels, including all ordinary derivative j and integer q witnesses. -/
theorem hk_entry_equals_original_entry
    (Q : Finset (Int × Int)) (J r s t u : Nat) :
    hkOriginalEntry Q J r s t u =
      TenthDiscriminant.integerTraceGramEntry Q 1 J r s t u := by
  unfold hkOriginalEntry TenthDiscriminant.integerTraceGramEntry
  apply Finset.sum_congr rfl
  intro j hj
  apply Finset.sum_congr rfl
  intro q hq
  exact gaussian_positive_trace_is_original_trace
    (TenthDiscriminant.integerDerivativeRow 1 r s j q)
    (TenthDiscriminant.integerDerivativeRow 1 t u j q)

/-- Entire HK representation of the original rectangular integer
trace Gram. Full row-major R*S, not a single minor. -/
def hkOriginalRectangularGram
    (Q : Finset (Int × Int)) (J R S : Nat) :
    Matrix (Fin (R*S)) (Fin (R*S)) Int :=
  fun a b => hkOriginalEntry Q J
    (a.val/S) (a.val%S) (b.val/S) (b.val%S)

/-- COMPLETE same-original-source equality between two actual
Lean packages, at D=1 and all finite Q,J,R,S. -/
theorem hk_entire_original_gram_bridge
    (Q : Finset (Int × Int)) (J R S : Nat) :
    hkOriginalRectangularGram Q J R S =
      TenthDiscriminant.integerRectangularTraceGram Q 1 J R S := by
  ext a b
  exact hk_entry_equals_original_entry Q J
    (a.val/S) (a.val%S) (b.val/S) (b.val%S)

/-- Determinant equality is an exact corollary on the SAME
original integer Gram, not a field class number or valuation gain. -/
theorem hk_entire_original_gram_det_bridge
    (Q : Finset (Int × Int)) (J R S : Nat) :
    (hkOriginalRectangularGram Q J R S).det =
      (TenthDiscriminant.integerRectangularTraceGram Q 1 J R S).det := by
  rw [hk_entire_original_gram_bridge]

end
end OriginalSourceBridge

#print axioms OriginalSourceBridge.gaussian_mul_is_original_pair_mul
#print axioms OriginalSourceBridge.gaussian_conj_is_original_pair_conj
#print axioms OriginalSourceBridge.gaussian_positive_trace_is_original_trace
#print axioms OriginalSourceBridge.wrong_unconjugated_source_metric
#print axioms OriginalSourceBridge.hk_entire_original_gram_bridge
#print axioms OriginalSourceBridge.hk_entire_original_gram_det_bridge
