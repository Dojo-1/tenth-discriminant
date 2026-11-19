import TenthDiscriminant.E39OriginalTwoPointSeparation

/-!
# E41 — Nonreal source geometry and lost imaginary-sign information

The E39 real-axis formula det G=4*(x-u)^2 does NOT generalize
as a Euclidean squared-distance formula on an imaginary quadratic
integer-pair source.

For two DISTINCT original sample pairs a=(x,y), b=(u,v), the
UNCHANGED positive integer trace Gram for ordinary Z jets
J=1,R=2,S=1 has:
  G = [[4, 2(x+u)],
       [2(x+u), 2(x²+u²+D(y²+v²))]]
  det G = 4*((x-u)^2 + D*(y-v)^2 + D*(y+v)^2).

The last term is an observer-dependent conjugate-sum remainder,
NOT a new curvature invariant or a squarefree field theorem.
It prevents the naive real-axis Vandermonde from being transported
unmodified into the complex carrier.

The original Gram also cannot recover the sign of EACH point's
imaginary coefficient: an explicit pair of distinct sources has
the same full original Gram. This is source-to-observer
noninjectivity, not conductor information loss.

This source uses the actual named integerRectangularTraceGram,
ordinary derivatives, original 2-positive trace and exact Finset.
-/

namespace TenthDiscriminant.E41
set_option autoImplicit false
noncomputable section

def complexTwoSource (x y u v : Int) : Finset (Int × Int) :=
  {(x,y),(u,v)}

/-- No auxiliary Gram: this is the ENTIRE original two-row
ordinary-jet trace Gram on the original two-point Finset. -/
theorem complex_two_original_gram
    (D : Nat) (x y u v : Int)
    (hneq : ((x,y) : Int × Int) ≠ (u,v)) :
    integerRectangularTraceGram (complexTwoSource x y u v)
      D 1 2 1 =
      !![4, 2*(x+u);
         2*(x+u), 2*(x*x+u*u+(D : Int)*(y*y+v*v))] := by
  have hneq' : ((u,v) : Int × Int) ≠ (x,y) := Ne.symm hneq
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [integerRectangularTraceGram, integerTraceGramMatrix,
      integerTraceGramEntry, integerDerivativeRow, integerPairTrace,
      pairPow, pairMul, pairScale, pairConj, complexTwoSource,
      Finset.sum_range_succ, hneq, hneq'] <;> ring

/-- Exact nonreal two-point determinant: a squared difference
PLUS an independently surviving conjugate-sum channel. -/
theorem complex_two_original_gram_det
    (D : Nat) (x y u v : Int)
    (hneq : ((x,y) : Int × Int) ≠ (u,v)) :
    (integerRectangularTraceGram
      (complexTwoSource x y u v) D 1 2 1).det =
    4*((x-u)^2+(D : Int)*(y-v)^2+(D : Int)*(y+v)^2) := by
  rw [complex_two_original_gram D x y u v hneq]
  simp [Matrix.det_fin_two]
  ring

/-- Difference between the original-Gram determinant and the
naively lifted Euclidean squared-distance formula. -/
theorem complex_naive_separation_missing_term
    (D : Nat) (x y u v : Int)
    (hneq : ((x,y) : Int × Int) ≠ (u,v)) :
    (integerRectangularTraceGram
      (complexTwoSource x y u v) D 1 2 1).det -
    4*((x-u)^2+(D : Int)*(y-v)^2) =
    4*(D : Int)*(y+v)^2 := by
  rw [complex_two_original_gram_det D x y u v hneq]
  ring

/-- Concrete falsifier to the naive complex squared-distance
formula: two distinct source points sharing nonzero imaginary
coefficient yield original Gram det=52, not 4. -/
theorem same_imag_nonzero_complex_counterexample :
    (integerRectangularTraceGram
      (complexTwoSource 0 1 1 1) 3 1 2 1).det = 52 ∧
    4*((0-1 : Int)^2 + (3 : Int)*(1-1)^2) = 4 := by
  constructor
  · rw [complex_two_original_gram_det 3 0 1 1 1 (by decide)]
    norm_num
  · norm_num

/-- The entire original Gram does not resolve the imaginary sign
of the second sample. Both supports have two distinct points. -/
theorem different_sources_same_entire_original_gram :
    complexTwoSource 0 1 1 1 ≠ complexTwoSource 0 1 1 (-1) ∧
    integerRectangularTraceGram
      (complexTwoSource 0 1 1 1) 3 1 2 1 =
    integerRectangularTraceGram
      (complexTwoSource 0 1 1 (-1)) 3 1 2 1 := by
  constructor
  · decide
  · rw [complex_two_original_gram 3 0 1 1 1 (by decide),
        complex_two_original_gram 3 0 1 1 (-1) (by decide)]
    decide

/-- On the nonreal source, real-coordinate translations still
have the same unimodular original row action: imaginary
coordinates are not silently shifted or reinterpreted. -/
theorem complex_real_translation_naturality
    (D : Nat) (x y u v c : Int)
    (hneq : ((x,y) : Int × Int) ≠ (u,v)) :
    E39.translateRowFrame c *
      integerRectangularTraceGram
        (complexTwoSource (x+c) y (u+c) v) D 1 2 1 *
      (E39.translateRowFrame c).transpose =
    integerRectangularTraceGram
      (complexTwoSource x y u v) D 1 2 1 := by
  have hneqc : ((x+c,y) : Int × Int) ≠ (u+c,v) := by
    intro h
    apply hneq
    apply Prod.ext
    · have hx := congrArg Prod.fst h
      dsimp at hx
      omega
    · exact congrArg Prod.snd h
  rw [complex_two_original_gram D (x+c) y (u+c) v hneqc,
      complex_two_original_gram D x y u v hneq]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [E39.translateRowFrame, Matrix.mul_apply,
      Matrix.transpose_apply, Fin.sum_univ_two] <;> ring

end
end TenthDiscriminant.E41

#print axioms TenthDiscriminant.E41.complex_two_original_gram
#print axioms TenthDiscriminant.E41.complex_two_original_gram_det
#print axioms TenthDiscriminant.E41.complex_naive_separation_missing_term
#print axioms TenthDiscriminant.E41.different_sources_same_entire_original_gram
#print axioms TenthDiscriminant.E41.complex_real_translation_naturality
