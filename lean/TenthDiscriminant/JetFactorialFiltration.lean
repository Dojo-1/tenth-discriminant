import TenthDiscriminant.JetPrecisionBridge

/-!
Phase204-A — trace pairing of the ORIGINAL ordinary-Z jet source.
The factorial jet identity was already Lean-proved in JetPrecisionBridge.
This file uses that existing proof rather than independently re-proving it.
No Hasse replacement, cross-prime equivalence, or new number-field bound.
-/
namespace TenthDiscriminant.Phase204
set_option autoImplicit false

/-- The original integral trace is bilinear in both source channels. -/
theorem pair_trace_biscaled
    (D : Nat) (a b : Int) (x y : Int × Int) :
    integerPairTrace D (pairScale a x) (pairScale b y) =
      a * b * integerPairTrace D x y := by
  simp only [integerPairTrace, pairScale]
  ring

/-- The *existing*, already checked source theorem is the whole
ordinary-jet-versus-Taylor-factorial seam. No new proof is needed. -/
theorem ordinary_jet_factorial_from_existing_source
    (D r s j : Nat) (z : Int × Int) :
    integerDerivativeRow D r s j z =
      pairScale (j.factorial : Int)
        (integerHasseCoefficientRow D r s j z) :=
  integerDerivativeRow_eq_factorial_hasse D r s j z

/-- Exact same-source Gram depth increment; no support or jet substitution. -/
theorem original_gram_depth_step
    (Q : Finset (Int × Int)) (D J r s t u : Nat) :
    integerTraceGramEntry Q D (J+1) r s t u =
      integerTraceGramEntry Q D J r s t u +
        Q.sum (fun z => integerPairTrace D
          (integerDerivativeRow D r s J z)
          (integerDerivativeRow D t u J z)) := by
  simp only [integerTraceGramEntry, Finset.sum_range_succ]

/-- Every original j-th trace contribution contains two ordinary j!
factors PLUS the source trace factor 2. The Taylor coefficients appear
only as an explicit integral quotient of the ORIGINAL jets. -/
theorem trace_jet_factorial_factor
    (D r s t u j : Nat) (z : Int × Int) :
    ∃ c : Int,
      integerPairTrace D
        (integerDerivativeRow D r s j z)
        (integerDerivativeRow D t u j z) =
          2 * (j.factorial : Int)^2 * c := by
  let a := integerHasseCoefficientRow D r s j z
  let b := integerHasseCoefficientRow D t u j z
  refine ⟨a.1*b.1 + (D:Int)*a.2*b.2, ?_⟩
  rw [integerDerivativeRow_eq_factorial_hasse D r s j z,
      integerDerivativeRow_eq_factorial_hasse D t u j z,
      pair_trace_biscaled]
  simp only [integerPairTrace]
  ring

end TenthDiscriminant.Phase204

#print axioms TenthDiscriminant.Phase204.pair_trace_biscaled
#print axioms TenthDiscriminant.Phase204.original_gram_depth_step
#print axioms TenthDiscriminant.Phase204.trace_jet_factorial_factor
