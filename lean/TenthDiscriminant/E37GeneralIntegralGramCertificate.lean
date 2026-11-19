import TenthDiscriminant.E36UnimodularMovingRowFrame

/-!
# E37 — Arbitrary-rank integral moving-frame determinant certificate

The previous two-row E34-E36 witnesses are now generalized to ALL
finite ranks n, but WITHOUT silently identifying an ambient quotient
kernel with a factor of the original sampled trace Gram.

(1) Algebraic lemma: U integral unimodular (det U = ±1), and an
exact diagonal factorization of U*G*Uᵀ, force the square of the
diagonal product to divide det G.

(2) Original source: G is EXACTLY integerRectangularTraceGram
Q D J R S, with its actual integer rows and trace convention.
A certified factorization of this entire G yields the same divisor.

(3) Conditional jet bridge: an integral source evaluation E,
positive trace B, equality E*B*Eᵀ=the ACTUAL original Gram,
and source row factorization U*E=Delta*F yield the divisor.
The identity E*B*Eᵀ=G is a transparent HYPOTHESIS, not a
theorem pretending that an arbitrary E is the real ordinary
jet-evaluation matrix.

(4) E36's legitimate moving frame instantiates n=2; the
nonunimodular fake is explicitly ineligible.
Nothing here sharpens 307^4 or proves existence of any
extra row factor on the actual large thin ellipse.
-/

namespace TenthDiscriminant.E37
set_option autoImplicit false
noncomputable section

/-- A finite integral row frame is accepted only if its determinant
is one of the two units of Z. The fake E36 scaling has determinant 5. -/
def IntegerUnimodular {n : Nat}
    (U : Matrix (Fin n) (Fin n) Int) : Prop :=
  U.det = 1 ∨ U.det = -1

private theorem det_unimodular_congruence {n : Nat}
    (U G : Matrix (Fin n) (Fin n) Int)
    (hU : IntegerUnimodular U) :
    (U * G * U.transpose).det = G.det := by
  rw [Matrix.det_mul, Matrix.det_mul, Matrix.det_transpose]
  rcases hU with hu | hu
  · rw [hu]
    ring
  · rw [hu]
    ring

private theorem det_diagonal_congruence {n : Nat}
    (d : Fin n → Int)
    (H : Matrix (Fin n) (Fin n) Int) :
    (Matrix.diagonal d * H * Matrix.diagonal d).det =
      (∏ i : Fin n, d i)^2 * H.det := by
  rw [Matrix.det_mul, Matrix.det_mul, Matrix.det_diagonal,
    Matrix.det_diagonal]
  ring

/-- General rank: a COMPLETE same-source Gram factorization by
integral unimodular congruence implies a genuine determinant divisor. -/
theorem arbitrary_rank_gram_factor {n : Nat}
    (U G H : Matrix (Fin n) (Fin n) Int)
    (d : Fin n → Int)
    (hU : IntegerUnimodular U)
    (hFactor : U * G * U.transpose =
      Matrix.diagonal d * H * Matrix.diagonal d) :
    ((∏ i : Fin n, d i)^2) ∣ G.det := by
  have hdet : G.det =
      (∏ i : Fin n, d i)^2 * H.det := by
    calc
      G.det = (U * G * U.transpose).det :=
        (det_unimodular_congruence U G hU).symm
      _ = (Matrix.diagonal d * H * Matrix.diagonal d).det :=
        congrArg Matrix.det hFactor
      _ = _ := det_diagonal_congruence d H
  exact ⟨H.det, hdet⟩

/-- No surrogate: the matrix is the actual original integer
rectangular trace Gram, with ALL R*S rows in original order. -/
theorem original_full_gram_factor
    (Q : Finset (Int × Int)) (D J R S : Nat)
    (U H : Matrix (Fin (R*S)) (Fin (R*S)) Int)
    (d : Fin (R*S) → Int)
    (hU : IntegerUnimodular U)
    (hFactor : U * integerRectangularTraceGram Q D J R S *
        U.transpose = Matrix.diagonal d * H * Matrix.diagonal d) :
    ((∏ i : Fin (R*S), d i)^2) ∣
      (integerRectangularTraceGram Q D J R S).det := by
  exact arbitrary_rank_gram_factor U
    (integerRectangularTraceGram Q D J R S) H d hU hFactor

/-- Algebraic bridge for a source-correct ordinary-jet evaluation
factorization. The hOriginalGram obligation is explicit: the
user MUST construct E and B from the ACTUAL original source. -/
theorem original_jet_evaluation_factor
    (Q : Finset (Int × Int)) (D J R S m : Nat)
    (E F : Matrix (Fin (R*S)) (Fin m) Int)
    (B : Matrix (Fin m) (Fin m) Int)
    (U : Matrix (Fin (R*S)) (Fin (R*S)) Int)
    (d : Fin (R*S) → Int)
    (hU : IntegerUnimodular U)
    (hOriginalGram : E * B * E.transpose =
      integerRectangularTraceGram Q D J R S)
    (hSourceRows : U * E = Matrix.diagonal d * F) :
    ((∏ i : Fin (R*S), d i)^2) ∣
      (integerRectangularTraceGram Q D J R S).det := by
  let G := integerRectangularTraceGram Q D J R S
  have hFactor : U * G * U.transpose =
      Matrix.diagonal d * (F * B * F.transpose) *
        Matrix.diagonal d := by
    change U * (integerRectangularTraceGram Q D J R S) *
      U.transpose = _
    rw [← hOriginalGram]
    calc
      U * (E * B * E.transpose) * U.transpose =
          (U * E) * B * (U * E).transpose := by
            simp only [Matrix.transpose_mul, Matrix.mul_assoc]
      _ = (Matrix.diagonal d * F) * B *
          (Matrix.diagonal d * F).transpose := by rw [hSourceRows]
      _ = Matrix.diagonal d * (F * B * F.transpose) *
          Matrix.diagonal d := by
            simp [Matrix.transpose_mul, Matrix.mul_assoc]
  exact original_full_gram_factor Q D J R S U
    (F * B * F.transpose) d hU hFactor

/-- In E36, the integral change (1,Z)→(1,Z-1) is truly
unimodular and has a complete original-Gram factorization. -/
def shiftedFactorDiagonal : Fin 2 → Int :=
  fun i => if i = 0 then 1 else 5

theorem shifted_unimodular_certificate :
    IntegerUnimodular E36.integerMovingRowFrame := by
  left
  exact E36.moving_row_frame_unimodular

theorem shifted_original_factorization :
    E36.integerMovingRowFrame *
      integerRectangularTraceGram E36.shiftedRealSource 25 1 2 1 *
      E36.integerMovingRowFrame.transpose =
        Matrix.diagonal shiftedFactorDiagonal *
          integerRectangularTraceGram E31.realSource 25 1 2 1 *
          Matrix.diagonal shiftedFactorDiagonal := by
  rw [E36.moved_same_original_gram_equals_positive_control,
      E34.original_five_gram_matrix, E31.actual_original_gram_matrix]
  decide

/-- Positive test of the generic factor theorem, on the actual
sampled original Gram of Qshift; 25 is exposed with no resampling. -/
theorem shifted_original_factor_via_generic_rank :
    ((∏ i : Fin 2, shiftedFactorDiagonal i)^2) ∣
      (integerRectangularTraceGram E36.shiftedRealSource 25 1 2 1).det := by
  exact original_full_gram_factor E36.shiftedRealSource 25 1 2 1
    E36.integerMovingRowFrame
    (integerRectangularTraceGram E31.realSource 25 1 2 1)
    shiftedFactorDiagonal shifted_unimodular_certificate
    shifted_original_factorization

theorem diagonal_product_is_five :
    (∏ i : Fin 2, shiftedFactorDiagonal i) = 5 := by
  decide

theorem shifted_original_factor_is_twentyfive :
    ((5 : Int)*5) ∣
      (integerRectangularTraceGram E36.shiftedRealSource 25 1 2 1).det := by
  have h := shifted_original_factor_via_generic_rank
  rw [diagonal_product_is_five] at h
  simpa [pow_two] using h

/-- Excludes the E36 fake p=5 row scaler from ALL generic n-row
certificates: a terminal matrix alone is not source provenance. -/
theorem fake_scaler_not_eligible :
    ¬ IntegerUnimodular E36.fakeRowScaler := by
  intro h
  rcases h with h | h
  · exact E36.fake_scaler_fails_unimodularity.1 h
  · exact E36.fake_scaler_fails_unimodularity.2 h

end
end TenthDiscriminant.E37

#print axioms TenthDiscriminant.E37.arbitrary_rank_gram_factor
#print axioms TenthDiscriminant.E37.original_full_gram_factor
#print axioms TenthDiscriminant.E37.original_jet_evaluation_factor
#print axioms TenthDiscriminant.E37.shifted_original_factor_via_generic_rank
#print axioms TenthDiscriminant.E37.shifted_original_factor_is_twentyfive
#print axioms TenthDiscriminant.E37.fake_scaler_not_eligible
