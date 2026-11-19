import TenthDiscriminant.E38CoherentKernelThread

/-!
# E39 — Original two-point Vandermonde determinant and integer translations

For two DISTINCT original integer samples x,y on the REAL axis and
original D,J=1,R=2,S=1 ordinary-Z jet rows 1,Z, the complete
positive integer trace Gram has determinant 4*(y-x)^2.

This strengthens E31/E34/E36 from isolated examples to an entire
exact source family and explains why relative separation is the
right arithmetic datum in this particular 2-point regime.

The support is a FINSET. Distinctness matters: repeated coordinates
collapse to one original sample and cannot be counted twice.

Translation x->x+c, y->y+c is accompanied by the exact integral
unimodular row change Z->Z-c. The actual original determinant
is invariant; raw entries and individual jet coefficients need not be.

No new higher-dimensional or full thin-ellipse bound is claimed.
-/

namespace TenthDiscriminant.E39
set_option autoImplicit false
noncomputable section

def realTwoSource (x y : Int) : Finset (Int × Int) :=
  {(x,0),(y,0)}

/-- Actual original two-point positive Gram for any D, retaining
ordinary derivative rows 1 and Z. Its restriction to distinct
points is NOT an arbitrary algebraic surrogate Gram. -/
theorem real_two_source_original_gram
    (D : Nat) (x y : Int) (hxy : x ≠ y) :
    integerRectangularTraceGram (realTwoSource x y) D 1 2 1 =
      !![4, 2*(x+y); 2*(x+y), 2*(x*x+y*y)] := by
  have hne : ((x,0) : Int × Int) ≠ (y,0) := by
    intro h
    exact hxy (congrArg Prod.fst h)
  have hne' : ((y,0) : Int × Int) ≠ (x,0) := Ne.symm hne
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [integerRectangularTraceGram, integerTraceGramMatrix,
      integerTraceGramEntry, integerDerivativeRow, integerPairTrace,
      pairPow, pairMul, pairScale, pairConj, realTwoSource,
      Finset.sum_range_succ, hne, hne'] <;> ring

/-- The determinant is a SQUARED SEPARATION, not a function
of the two absolute real coordinates independently. -/
theorem real_two_source_original_gram_det
    (D : Nat) (x y : Int) (hxy : x ≠ y) :
    (integerRectangularTraceGram (realTwoSource x y) D 1 2 1).det =
      4*(y-x)^2 := by
  rw [real_two_source_original_gram D x y hxy]
  simp [Matrix.det_fin_two]
  ring

/-- A prime factor of the actual original sample difference forces
a squared factor of the ACTUAL original positive trace Gram. -/
theorem source_separation_forces_prime_square
    (D : Nat) (x y p : Int) (hxy : x ≠ y)
    (hsep : p ∣ y-x) :
    p^2 ∣
      (integerRectangularTraceGram (realTwoSource x y) D 1 2 1).det := by
  rw [real_two_source_original_gram_det D x y hxy]
  rcases hsep with ⟨k,hk⟩
  refine ⟨4*k^2, ?_⟩
  rw [hk]
  ring

/-- A true integral moving row basis: 1, Z-c. -/
def translateRowFrame (c : Int) : Matrix (Fin 2) (Fin 2) Int :=
  !![1,0;-c,1]

theorem translateRowFrame_det_one (c : Int) :
    (translateRowFrame c).det = 1 := by
  simp [translateRowFrame, Matrix.det_fin_two]

/-- Entire original Gram covariance under simultaneous sample
translation and the corresponding integer row basis change. -/
theorem translated_original_gram_naturality
    (D : Nat) (x y c : Int) (hxy : x ≠ y) :
    translateRowFrame c *
      integerRectangularTraceGram
        (realTwoSource (x+c) (y+c)) D 1 2 1 *
      (translateRowFrame c).transpose =
    integerRectangularTraceGram (realTwoSource x y) D 1 2 1 := by
  have hxyc : x+c ≠ y+c := by omega
  rw [real_two_source_original_gram D (x+c) (y+c) hxyc,
    real_two_source_original_gram D x y hxy]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [translateRowFrame, Matrix.mul_apply, Matrix.transpose_apply,
      Fin.sum_univ_two] <;> ring

/-- The source finite set does not count duplicate nodes twice.
The distinctness premise on the two-point Gram is load-bearing. -/
theorem repeated_source_collapses (x : Int) :
    (realTwoSource x x).card = 1 := by
  simp [realTwoSource]

/-- E31/E34/E36 small controls are recovered numerically by
the same separation-based determinant theorem. -/
theorem three_original_source_det_regressions :
    (integerRectangularTraceGram (realTwoSource 0 1) 25 1 2 1).det = 4 ∧
    (integerRectangularTraceGram (realTwoSource 0 5) 25 1 2 1).det = 100 ∧
    (integerRectangularTraceGram (realTwoSource 1 6) 25 1 2 1).det = 100 := by
  constructor
  · rw [real_two_source_original_gram_det 25 0 1 (by decide)]
    norm_num
  constructor
  · rw [real_two_source_original_gram_det 25 0 5 (by decide)]
    norm_num
  · rw [real_two_source_original_gram_det 25 1 6 (by decide)]
    norm_num

end
end TenthDiscriminant.E39

#print axioms TenthDiscriminant.E39.real_two_source_original_gram
#print axioms TenthDiscriminant.E39.real_two_source_original_gram_det
#print axioms TenthDiscriminant.E39.source_separation_forces_prime_square
#print axioms TenthDiscriminant.E39.translated_original_gram_naturality
#print axioms TenthDiscriminant.E39.repeated_source_collapses
