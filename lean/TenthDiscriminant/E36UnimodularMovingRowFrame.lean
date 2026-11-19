import TenthDiscriminant.E35OriginalJetRowCertificate

/-!
# E36 — A moving unimodular row frame can reveal the source prime factor

The E35 raw second-row jet hypothesis is SUFFICIENT but not NECESSARY.
At original Q={(1,0),(6,0)}, D=25, J=1,R=2,S=1, the raw
ordinary-Z jet coordinates are not all divisible by five, and
the raw original trace Gram's offdiagonal value 14 is not a
multiple of five. Nevertheless its determinant is 100.

The exact unimodular integer row frame U=[[1,0],[-1,1]]
implements Z -> Z - 1 in the SAME two-row polynomial space,
with determinant U=1 and

    U * G(Q_shift) * U.transpose = [[4,10],[10,50]].

This is the same numerical matrix as G(Q_5), but E36 NEVER changes
the original Q_shift to prove the left-hand determinant factor.
It uses an integer congruence on its ACTUAL original source Gram.

No field-discriminant bound or general n-row equivalent is claimed.
-/

namespace TenthDiscriminant.E36
set_option autoImplicit false
noncomputable section

def shiftedRealSource : Finset (Int × Int) :=
  {(1,0),(6,0)}

/-- Same ORIGINAL ordinary-jet source D=25, J=1, R=2, S=1. -/
theorem shifted_original_gram_matrix :
    integerRectangularTraceGram shiftedRealSource 25 1 2 1 =
      !![4,14;14,74] := by
  decide

theorem shifted_original_gram_det :
    (integerRectangularTraceGram shiftedRealSource 25 1 2 1).det = 100 := by
  rw [shifted_original_gram_matrix]
  simp [Matrix.det_fin_two] <;> ring

/-- The actual source sampling has the same cardinality as E34 Q_five. -/
theorem matched_two_point_source_cardinality :
    shiftedRealSource.card = E34.realFiveSource.card := by
  decide

/-- The absolute raw-original-jet sufficient condition of E35
does NOT hold at this shifted original source. -/
theorem shifted_original_raw_jet_certificate_fails :
    ¬ E35.SecondRowJetDivisible shiftedRealSource 25 1 5 := by
  intro h
  have hj : 0 ∈ Finset.range 1 := by decide
  have hq : (1,0) ∈ shiftedRealSource := by decide
  have hh := (h 0 hj (1,0) hq).1
  have hnot : ¬ ((5 : Int) ∣
      (integerDerivativeRow 25 1 0 0 (1,0)).1) := by
    decide
  exact hnot hh

/-- The E34 raw-original Gram entry criterion fails as well. -/
theorem shifted_original_offdiagonal_not_divisible :
    ¬ (5 : Int) ∣
      (integerRectangularTraceGram shiftedRealSource 25 1 2 1) 0 1 := by
  rw [shifted_original_gram_matrix]
  decide

/-- Integral row transport Z -> Z-1 on the two-row polynomial span. -/
def integerMovingRowFrame : Matrix (Fin 2) (Fin 2) Int :=
  !![1,0;-1,1]

theorem moving_row_frame_unimodular :
    integerMovingRowFrame.det = 1 := by
  decide

/-- This keeps Q_shift and all original ordinary jets fixed; only the
row basis changes via an invertible INTEGRAL matrix. -/
theorem moved_same_original_gram_equals_positive_control :
    integerMovingRowFrame *
      (integerRectangularTraceGram shiftedRealSource 25 1 2 1) *
      integerMovingRowFrame.transpose =
      integerRectangularTraceGram E34.realFiveSource 25 1 2 1 := by
  rw [shifted_original_gram_matrix, E34.original_five_gram_matrix]
  decide

/-- The determinant's prime-square factor genuinely survives the
unimodular row change (or can be read directly from the original
verified determinant), despite the raw absolute row test failing. -/
theorem shifted_original_prime_squared_factor :
    ((5 : Int)*5) ∣
      (integerRectangularTraceGram shiftedRealSource 25 1 2 1).det := by
  rw [shifted_original_gram_det]
  norm_num

theorem e35_sufficient_gate_is_not_necessary :
    (¬ E35.SecondRowJetDivisible shiftedRealSource 25 1 5) ∧
      (((5 : Int)*5) ∣
        (integerRectangularTraceGram shiftedRealSource 25 1 2 1).det) := by
  exact ⟨shifted_original_raw_jet_certificate_fails,
    shifted_original_prime_squared_factor⟩

/-- An explicit integral moving-frame witness, not a heuristic scalar
or a changed source set, transports the original Gram into one where
the E34 entrywise divisibility certificate is visible. -/
theorem moved_original_gram_has_five_entry_certificate :
    ((5 : Int)*5) ∣
      (integerMovingRowFrame *
        integerRectangularTraceGram shiftedRealSource 25 1 2 1 *
        integerMovingRowFrame.transpose).det := by
  rw [moved_same_original_gram_equals_positive_control]
  exact E34.original_five_gram_prime_squared_factor


/-- A nonunimodular row scaler can make a spurious prime-square
factor out of a source determinant that is NOT even divisible by 5.
It is forbidden as a witness of arithmetic source divisibility. -/
def fakeRowScaler : Matrix (Fin 2) (Fin 2) Int :=
  !![1,0;0,5]

theorem fakeRowScaler_not_unimodular :
    fakeRowScaler.det = 5 := by
  decide

/-- This is the matched null: scaling Z to 5Z manufactures a determinant
factor on the E31 Q_unit original Gram, but does NOT preserve det(G). -/
theorem fake_scaling_manufactures_prime_square :
    (fakeRowScaler *
      (integerRectangularTraceGram E31.realSource 25 1 2 1) *
      fakeRowScaler.transpose).det = 100 ∧
    (integerRectangularTraceGram E31.realSource 25 1 2 1).det = 4 := by
  constructor
  · rw [E31.actual_original_gram_matrix]
    decide
  · exact E31.actual_original_gram_det_four

/-- No claim about integral unimodular congruence may admit the
fake row scaler: its determinant is 5 rather than +1 or -1. -/
theorem fake_scaler_fails_unimodularity :
    fakeRowScaler.det ≠ (1 : Int) ∧
      fakeRowScaler.det ≠ (-1 : Int) := by
  rw [fakeRowScaler_not_unimodular]
  decide

end
end TenthDiscriminant.E36

#print axioms TenthDiscriminant.E36.shifted_original_gram_matrix
#print axioms TenthDiscriminant.E36.moving_row_frame_unimodular
#print axioms TenthDiscriminant.E36.moved_same_original_gram_equals_positive_control
#print axioms TenthDiscriminant.E36.e35_sufficient_gate_is_not_necessary
#print axioms TenthDiscriminant.E36.moved_original_gram_has_five_entry_certificate

#print axioms TenthDiscriminant.E36.fakeRowScaler_not_unimodular
#print axioms TenthDiscriminant.E36.fake_scaling_manufactures_prime_square
#print axioms TenthDiscriminant.E36.fake_scaler_fails_unimodularity
