import TenthDiscriminant.IntegerTraceGram

/-!
Phase204-A, preregistered in Issue #136. Original integer-pair ordinary-Z
jets, original trace factor 2, and exact J-depth source. No Hasse jets.
No field classification, new p-adic determinant valuation, or cutoff.
-/
namespace TenthDiscriminant.Phase204
set_option autoImplicit false

theorem pair_trace_biscaled
    (D : Nat) (a b : Int) (x y : Int × Int) :
    integerPairTrace D (pairScale a x) (pairScale b y) =
      a * b * integerPairTrace D x y := by
  simp only [integerPairTrace, pairScale]
  ring

theorem ordinary_jet_factorial
    (D r s j : Nat) (z : Int × Int) (hj : j ≤ r) :
    integerDerivativeRow D r s j z =
      pairScale (j.factorial : Int) <|
        pairScale (r.choose j : Int) <|
          pairMul D (pairPow D z (r-j)) (pairPow D (pairConj z) s) := by
  simp [integerDerivativeRow, hj, pairScale,
    Nat.descFactorial_eq_factorial_mul_choose, mul_assoc]

/-- Exact same-source increment, with NO change of Q or derivatives. -/
theorem original_gram_depth_step
    (Q : Finset (Int × Int)) (D J r s t u : Nat) :
    integerTraceGramEntry Q D (J+1) r s t u =
      integerTraceGramEntry Q D J r s t u +
        Q.sum (fun z => integerPairTrace D
          (integerDerivativeRow D r s J z)
          (integerDerivativeRow D t u J z)) := by
  simp only [integerTraceGramEntry, Finset.sum_range_succ]

/-- Every source J-th trace summand includes both ordinary J! factors
and the source trace 2; zero derivatives are handled explicitly. -/
theorem trace_jet_factorial_factor
    (D r s t u j : Nat) (z : Int × Int) :
    ∃ c : Int,
      integerPairTrace D
        (integerDerivativeRow D r s j z)
        (integerDerivativeRow D t u j z) =
          2 * (j.factorial : Int)^2 * c := by
  by_cases hr : j ≤ r
  · by_cases ht : j ≤ t
    · let a : Int × Int :=
        pairScale (r.choose j : Int)
          (pairMul D (pairPow D z (r-j)) (pairPow D (pairConj z) s))
      let b : Int × Int :=
        pairScale (t.choose j : Int)
          (pairMul D (pairPow D z (t-j)) (pairPow D (pairConj z) u))
      refine ⟨a.1*b.1+(D:Int)*a.2*b.2, ?_⟩
      rw [ordinary_jet_factorial D r s j z hr,
          ordinary_jet_factorial D t u j z ht]
      simp only [integerPairTrace, pairScale]
      ring
    · refine ⟨0, ?_⟩
      simp [integerDerivativeRow, ht, integerPairTrace]
  · refine ⟨0, ?_⟩
    simp [integerDerivativeRow, hr, integerPairTrace]

end TenthDiscriminant.Phase204

#print axioms TenthDiscriminant.Phase204.ordinary_jet_factorial
#print axioms TenthDiscriminant.Phase204.original_gram_depth_step
#print axioms TenthDiscriminant.Phase204.trace_jet_factorial_factor
