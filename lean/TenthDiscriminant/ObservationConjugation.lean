import TenthDiscriminant.IntegerTraceGram

/-!
# Conjugation of the original integer observations

A point is the pair (x,y), representing x + y * sqrt(-D).
These lemmas keep the original ordinary Z-derivatives, with W held fixed,
and the original integer trace pairing with weights 2 and 2D.

Conjugating every observation changes the sign of the imaginary channel,
but not its weight or the resulting Gram matrix.

This is a genuine symmetry of the source object. It says nothing about
the rank of a smaller observation set or a new discriminant cutoff.
-/
namespace TenthDiscriminant
set_option autoImplicit false

/-- Conjugation is an involution on integer observation coordinates. -/
theorem pairConj_twice (q : Int × Int) :
    pairConj (pairConj q) = q := by
  rcases q with ⟨x, y⟩
  simp [pairConj]

theorem pairConj_injective : Function.Injective pairConj := by
  intro a b h
  have hh := congrArg pairConj h
  simpa only [pairConj_twice] using hh

/-- Conjugation respects multiplication in the selected quadratic order. -/
theorem pairConj_mul (D : Nat) (a b : Int × Int) :
    pairConj (pairMul D a b) =
      pairMul D (pairConj a) (pairConj b) := by
  apply Prod.ext
  · simp [pairConj, pairMul] <;> ring
  · simp [pairConj, pairMul] <;> ring

theorem pairConj_scale (c : Int) (a : Int × Int) :
    pairConj (pairScale c a) = pairScale c (pairConj a) := by
  rcases a with ⟨x, y⟩
  simp [pairConj, pairScale]

theorem pairConj_pow (D : Nat) (a : Int × Int) (n : Nat) :
    pairConj (pairPow D a n) = pairPow D (pairConj a) n := by
  induction n with
  | zero => simp [pairPow, pairConj]
  | succ n ih =>
      simp only [pairPow, pairConj_mul, ih]

/-- The *ordinary* derivative commutes with conjugation.
No Hasse/Taylor substitution or factorial inversion occurs here. -/
theorem integerDerivativeRow_conj (D r s j : Nat) (q : Int × Int) :
    integerDerivativeRow D r s j (pairConj q) =
      pairConj (integerDerivativeRow D r s j q) := by
  by_cases hj : j ≤ r
  · simp [integerDerivativeRow, hj, pairConj_scale,
      pairConj_mul, pairConj_pow, pairConj_twice]
  · simp [integerDerivativeRow, hj, pairConj]

/-- Trace weights 2 and 2D are unchanged when both arguments are conjugated. -/
theorem integerPairTrace_conj (D : Nat) (a b : Int × Int) :
    integerPairTrace D (pairConj a) (pairConj b) =
      integerPairTrace D a b := by
  simp [integerPairTrace, pairConj]

theorem integerPairTrace_derivatives_conj
    (D r s t u j : Nat) (q : Int × Int) :
    integerPairTrace D
      (integerDerivativeRow D r s j (pairConj q))
      (integerDerivativeRow D t u j (pairConj q)) =
    integerPairTrace D
      (integerDerivativeRow D r s j q)
      (integerDerivativeRow D t u j q) := by
  rw [integerDerivativeRow_conj, integerDerivativeRow_conj]
  exact integerPairTrace_conj D
    (integerDerivativeRow D r s j q)
    (integerDerivativeRow D t u j q)

/-- Conjugate *all* points: the original Gram entry is exactly unchanged. -/
theorem integerTraceGramEntry_conj
    (Q : Finset (Int × Int)) (D J r s t u : Nat) :
    integerTraceGramEntry (Q.image pairConj) D J r s t u =
      integerTraceGramEntry Q D J r s t u := by
  classical
  unfold integerTraceGramEntry
  apply Finset.sum_congr rfl
  intro j hj
  rw [Finset.sum_image (pairConj_injective.injOn)]
  apply Finset.sum_congr rfl
  intro q hq
  exact integerPairTrace_derivatives_conj D r s t u j q

/-- Equality for the SAME rectangular coefficient rows and ordinary jets. -/
theorem integerRectangularTraceGram_conj
    (Q : Finset (Int × Int)) (D J R S : Nat) :
    integerRectangularTraceGram (Q.image pairConj) D J R S =
      integerRectangularTraceGram Q D J R S := by
  ext i k
  exact integerTraceGramEntry_conj Q D J
    (i.val / S) (i.val % S) (k.val / S) (k.val % S)

/-- Negative control: conjugation is not equality of each imaginary channel. -/
theorem integerDerivativeRow_conj_changes_channel :
    integerDerivativeRow 3 0 1 0 (0, 1) ≠
      integerDerivativeRow 3 0 1 0 (0, -1) := by
  decide

end TenthDiscriminant
