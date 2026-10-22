import TenthDiscriminant.GramMatrix

/-!
# Invisible polynomial jets and the actual trace-Gram kernel

The real Gram matrix detects REAL coefficient combinations. Complex row
independence is sufficient, not necessary, for positive definiteness.
The global point-count/resultant criterion is NOT assumed or proved here.
-/
namespace TenthDiscriminant
open Matrix
open scoped ComplexConjugate
noncomputable section

/-- The actual sampled complex jet of a real linear combination of rows. -/
def realJet {n : Nat} (P : Finset Complex) (J : Nat)
    (rows : Fin n -> Nat × Nat) (x : Fin n -> Real) (c : Fin J × P) : Complex :=
  Finset.univ.sum (fun i => (x i : Complex) *
    derivativeRow (rows i).1 (rows i).2 c.1 c.2)

theorem realJet_re {n : Nat} (P : Finset Complex) (J : Nat)
    (rows : Fin n -> Nat × Nat) (x : Fin n -> Real) (c : Fin J × P) :
    (realJet P J rows x c).re =
      Finset.univ.sum (fun i => traceRealFeatures P J rows i c * x i) := by
  simp [realJet, traceRealFeatures, Complex.mul_re, mul_comm]

theorem realJet_im {n : Nat} (P : Finset Complex) (J : Nat)
    (rows : Fin n -> Nat × Nat) (x : Fin n -> Real) (c : Fin J × P) :
    (realJet P J rows x c).im =
      Finset.univ.sum (fun i => traceImagFeatures P J rows i c * x i) := by
  simp [realJet, traceImagFeatures, Complex.mul_im, mul_comm]

/-- Exact energy identity, with the original trace normalization. -/
theorem traceGramMatrix_jet_energy {n : Nat} (P : Finset Complex) (J : Nat)
    (rows : Fin n -> Nat × Nat) (x : Fin n -> Real) :
    dotProduct x ((traceGramMatrix P J rows).mulVec x) =
      2 * Finset.univ.sum (fun c => Complex.normSq (realJet P J rows x c)) := by
  rw [traceGramMatrix_quadratic]
  congr 1
  apply Finset.sum_congr rfl
  intro c hc
  rw [Complex.normSq_apply, realJet_re, realJet_im]
  ring

/-- Exact nullspace identification; neither direction assumes independence. -/
theorem traceGramMatrix_kernel_iff {n : Nat} (P : Finset Complex) (J : Nat)
    (rows : Fin n -> Nat × Nat) (x : Fin n -> Real) :
    (traceGramMatrix P J rows).mulVec x = 0 <->
      forall c, realJet P J rows x c = 0 := by
  classical
  constructor
  · intro hx c
    have he := traceGramMatrix_jet_energy P J rows x
    rw [hx, dotProduct_zero] at he
    have hs : Finset.univ.sum (fun c => Complex.normSq (realJet P J rows x c)) = 0 := by
      linarith
    have hle : Complex.normSq (realJet P J rows x c) <=
        Finset.univ.sum (fun c => Complex.normSq (realJet P J rows x c)) :=
      Finset.single_le_sum (fun d hd => Complex.normSq_nonneg _) (Finset.mem_univ c)
    apply Complex.normSq_eq_zero.mp
    exact le_antisymm (hs ▸ hle) (Complex.normSq_nonneg _)
  · intro h
    have he : dotProduct x ((traceGramMatrix P J rows).mulVec x) = 0 := by
      rw [traceGramMatrix_jet_energy]
      simp [h]
    apply ((traceGramMatrix_posSemidef P J rows).dotProduct_mulVec_zero_iff x).mp
    simpa only [star_trivial] using he

/-- Positive definiteness is precisely absence of invisible real coefficients. -/
theorem traceGramMatrix_posDef_iff {n : Nat} (P : Finset Complex) (J : Nat)
    (rows : Fin n -> Nat × Nat) :
    (traceGramMatrix P J rows).PosDef <->
      forall x, (forall c, realJet P J rows x c = 0) -> x = 0 := by
  classical
  constructor
  · intro h x hx
    by_contra hn
    have hk := (traceGramMatrix_kernel_iff P J rows x).mpr hx
    have hp := h.2 x hn
    rw [hk, dotProduct_zero] at hp
    exact (lt_irrefl 0) hp
  · intro h
    constructor
    · exact (traceGramMatrix_posSemidef P J rows).isHermitian
    · intro x hx
      have hw : ∃ c, realJet P J rows x c ≠ 0 := by
        by_contra hn
        push_neg at hn
        exact hx (h x hn)
      obtain ⟨c, hc⟩ := hw
      have hp := Complex.normSq_pos.mpr hc
      have hle : Complex.normSq (realJet P J rows x c) <=
          Finset.univ.sum (fun c => Complex.normSq (realJet P J rows x c)) :=
        Finset.single_le_sum (fun d hd => Complex.normSq_nonneg _) (Finset.mem_univ c)
      have he := traceGramMatrix_jet_energy P J rows x
      have hh : 0 < dotProduct x ((traceGramMatrix P J rows).mulVec x) := by
        nlinarith
      simpa only [star_trivial] using hh

/-- A named conditional bridge, not a proof of the geometric uniqueness premise. -/
theorem traceGramMatrix_det_pos_of_jet_unique {n : Nat} (P : Finset Complex) (J : Nat)
    (rows : Fin n -> Nat × Nat)
    (h : forall x, (forall c, realJet P J rows x c = 0) -> x = 0) :
    0 < (traceGramMatrix P J rows).det :=
  ((traceGramMatrix_posDef_iff P J rows).mpr h).det_pos

/-- Adding derivative samples cannot destroy already established PD. -/
theorem traceGramMatrix_posDef_mono_jets {n : Nat} (P : Finset Complex) (J K : Nat)
    (rows : Fin n -> Nat × Nat) (hJK : J <= K)
    (h : (traceGramMatrix P J rows).PosDef) :
    (traceGramMatrix P K rows).PosDef := by
  apply (traceGramMatrix_posDef_iff P K rows).mpr
  intro x hx
  apply (traceGramMatrix_posDef_iff P J rows).mp h x
  intro c
  exact hx (⟨⟨c.1.val, lt_of_lt_of_le c.1.isLt hJK⟩, c.2⟩)

/-- Adding points cannot destroy already established PD. -/
theorem traceGramMatrix_posDef_mono_points {n : Nat} (P Q : Finset Complex) (J : Nat)
    (rows : Fin n -> Nat × Nat) (hPQ : P ⊆ Q)
    (h : (traceGramMatrix P J rows).PosDef) :
    (traceGramMatrix Q J rows).PosDef := by
  apply (traceGramMatrix_posDef_iff Q J rows).mpr
  intro x hx
  apply (traceGramMatrix_posDef_iff P J rows).mp h x
  intro c
  exact hx (⟨c.1, ⟨c.2.val, hPQ c.2.property⟩⟩)

/-- Keep w fixed: this is the polynomial whose z-jets the code samples. -/
def rowSection {n : Nat} (rows : Fin n -> Nat × Nat)
    (coeff : Fin n -> Complex) (w : Complex) : Polynomial Complex :=
  Finset.univ.sum (fun i => Polynomial.C (coeff i * w ^ (rows i).2) *
    Polynomial.X ^ (rows i).1)

/-- Genuine formal polynomial differentiation agrees with the actual row formula. -/
theorem rowSection_iterate_eval {n : Nat} (rows : Fin n -> Nat × Nat)
    (coeff : Fin n -> Complex) (z : Complex) (j : Nat) :
    ((Polynomial.derivative^[j]) (rowSection rows coeff (conj z))).eval z =
      Finset.univ.sum (fun i => coeff i * derivativeRow (rows i).1 (rows i).2 j z) := by
  classical
  unfold rowSection
  rw [Polynomial.iterate_derivative_sum, Polynomial.eval_finset_sum]
  apply Finset.sum_congr rfl
  intro i hi
  rw [Polynomial.iterate_derivative_C_mul, Polynomial.iterate_derivative_X_pow_eq_C_mul]
  by_cases hj : j <= (rows i).1
  · simp only [derivativeRow, if_pos hj, Polynomial.eval_mul, Polynomial.eval_C,
      Polynomial.eval_pow, Polynomial.eval_X]
    push_cast
    ring
  · have hz : (rows i).1.descFactorial j = 0 :=
      Nat.descFactorial_eq_zero_iff_lt.mpr (Nat.lt_of_not_ge hj)
    simp [derivativeRow, hj, hz]

/-- Specialization of the polynomial identity to the real Gram coefficients. -/
theorem realJet_eq_polynomial_jet {n : Nat} (P : Finset Complex) (J : Nat)
    (rows : Fin n -> Nat × Nat) (x : Fin n -> Real) (c : Fin J × P) :
    realJet P J rows x c =
      ((Polynomial.derivative^[c.1.val])
        (rowSection rows (fun i => (x i : Complex)) (conj (c.2 : Complex)))).eval c.2 := by
  rw [rowSection_iterate_eval]
  rfl

/-- Dropping J>=S admits a genuine nonzero polynomial on a unit-circle sample. -/
theorem circle_power_jet_zero (z w : Complex) (hzw : z*w=1)
    (m j : Nat) (hj : j < m) :
    ((Polynomial.derivative^[j])
      ((Polynomial.C w * Polynomial.X - 1)^m)).eval z = 0 := by
  obtain ⟨q,hq⟩ := Polynomial.pow_sub_dvd_iterate_derivative_pow
    (Polynomial.C w * Polynomial.X - 1) m j
  rw [hq, Polynomial.eval_mul, Polynomial.eval_pow]
  have hp : (Polynomial.C w * Polynomial.X - 1).eval z = 0 := by
    simp [mul_comm w z, hzw]
  rw [hp, zero_pow (by omega), zero_mul]

theorem circle_power_nonzero (z w : Complex) (hzw : z*w=1) (m : Nat) :
    (Polynomial.C w * Polynomial.X - 1)^m ≠ (0 : Polynomial Complex) := by
  apply pow_ne_zero
  intro h
  have hc := congrArg (fun p : Polynomial Complex => p.coeff 1) h
  have hw : w = 0 := by simpa using hc
  simp [hw] at hzw

/-- Complex row dependence is NOT equivalent to a real trace-Gram kernel. -/
theorem traceGramMatrix_real_complex_control :
    (traceGramMatrix {Complex.I} 1 (fun i : Fin 2 => (i.val,0))).det = 4 := by
  norm_num [Matrix.det_fin_two, traceGramMatrix, traceGramEntry, derivativeRow,
    Finset.sum_range_succ, Nat.descFactorial]

theorem complex_row_relation_control :
    (-Complex.I) * derivativeRow 0 0 0 Complex.I +
      derivativeRow 1 0 0 Complex.I = 0 := by
  norm_num [derivativeRow, Nat.descFactorial]

end
end TenthDiscriminant
