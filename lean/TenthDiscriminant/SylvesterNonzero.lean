import TenthDiscriminant.SylvesterLocal

/-!
# Nonzero fixed Sylvester determinants from coprimality

The field-level coefficient matrix is bridged explicitly to the existing
nested-polynomial matrix. No determinant nonzero or injectivity assumption
appears in the public coprimality result. Exact degree is not an upper bound.
-/
namespace TenthDiscriminant
namespace NonzeroBridge
open Polynomial Matrix
noncomputable section

variable {L : Type*} [Field L]

/-- Coefficients in a bounded multiplier space, including its zero-dimensional case. -/
def boundedPolynomial {n : Nat} (v : Fin n -> L) : Polynomial L :=
  Finset.univ.sum (fun i => Polynomial.C (v i) * Polynomial.X^i.val)

theorem boundedPolynomial_coeff {n : Nat} (v : Fin n -> L) (i : Fin n) :
    (boundedPolynomial v).coeff i.val = v i := by
  classical
  unfold boundedPolynomial
  rw [Polynomial.finset_sum_coeff]
  have ht (j : Fin n) :
      (Polynomial.C (v j) * Polynomial.X^j.val).coeff i.val =
        if j = i then v j else 0 := by
    rw [Polynomial.coeff_C_mul, Polynomial.coeff_X_pow]
    by_cases hj : j = i
    - subst j; simp
    - have hv : j.val ≠ i.val := fun h => hj (Fin.ext h)
      simp [hj, hv]
  simp_rw [ht]
  simp

theorem boundedPolynomial_high_coeff {n : Nat} (v : Fin n -> L) (k : Nat)
    (hk : n <= k) : (boundedPolynomial v).coeff k = 0 := by
  classical
  unfold boundedPolynomial
  rw [Polynomial.finset_sum_coeff]
  apply Finset.sum_eq_zero
  intro i hi
  have hv : i.val ≠ k := by have := i.isLt; omega
  simp [Polynomial.coeff_C_mul, Polynomial.coeff_X_pow, hv]

/-- m shifts of F followed by n shifts of G. -/
def columns (F G : Polynomial L) (m n : Nat) (j : Fin (m+n)) : Polynomial L :=
  if j.val < m then Polynomial.X^j.val * F
    else Polynomial.X^(j.val-m) * G

def coeffMatrix (F G : Polynomial L) (m n : Nat) : Matrix (Fin (m+n)) (Fin (m+n)) L :=
  fun i j => (columns F G m n j).coeff i.val

theorem columns_degree (F G : Polynomial L) (m n : Nat)
    (hF : F.natDegree <= n) (hG : G.natDegree <= m) (j : Fin (m+n)) :
    (columns F G m n j).natDegree < m+n := by
  unfold columns
  split_ifs with hj
  - have hd : (Polynomial.X^j.val * F).natDegree <=
        (Polynomial.X^j.val : Polynomial L).natDegree + F.natDegree :=
      Polynomial.natDegree_mul_le
    have hx : (Polynomial.X^j.val : Polynomial L).natDegree <= j.val := by simp
    omega
  - have hd : (Polynomial.X^(j.val-m) * G).natDegree <=
        (Polynomial.X^(j.val-m) : Polynomial L).natDegree + G.natDegree :=
      Polynomial.natDegree_mul_le
    have hx : (Polynomial.X^(j.val-m) : Polynomial L).natDegree <= j.val-m := by simp
    have hjn := j.isLt
    omega

/-- A zero coefficient image is exactly a bounded polynomial syzygy. -/
theorem kernel_syzygy (F G : Polynomial L) (m n : Nat)
    (hF : F.natDegree <= n) (hG : G.natDegree <= m)
    (v : Fin (m+n) -> L) (hv : (coeffMatrix F G m n).mulVec v = 0) :
    boundedPolynomial (fun i : Fin m => v (Fin.castAdd n i)) * F +
    boundedPolynomial (fun i : Fin n => v (Fin.natAdd m i)) * G = 0 := by
  classical
  have hsum : Finset.univ.sum (fun j : Fin (m+n) =>
      Polynomial.C (v j) * columns F G m n j) = 0 := by
    ext k
    simp only [Polynomial.finset_sum_coeff, Polynomial.coeff_C_mul, Polynomial.coeff_zero]
    by_cases hk : k < m+n
    - have hh := congrFun hv (show Fin (m+n) from ⟨k,hk⟩)
      simpa [Matrix.mulVec, dotProduct, coeffMatrix, mul_comm] using hh
    - apply Finset.sum_eq_zero
      intro j hj
      rw [Polynomial.coeff_eq_zero_of_natDegree_lt
        ((columns_degree F G m n hF hG j).trans_le (Nat.le_of_not_lt hk)), mul_zero]
  rw [Fin.sum_univ_add] at hsum
  have hl (i : Fin m) :
      Polynomial.C (v (Fin.castAdd n i)) * columns F G m n (Fin.castAdd n i) =
      (Polynomial.C (v (Fin.castAdd n i)) * Polynomial.X^i.val) * F := by
    simp [columns, i.isLt, mul_assoc]
  have hr (i : Fin n) :
      Polynomial.C (v (Fin.natAdd m i)) * columns F G m n (Fin.natAdd m i) =
      (Polynomial.C (v (Fin.natAdd m i)) * Polynomial.X^i.val) * G := by
    simp [columns, mul_assoc]
  simp_rw [hl, hr] at hsum
  simpa only [boundedPolynomial, Finset.sum_mul] using hsum

/-- Coprimality and exact degree kill every bounded syzygy. -/
theorem coeffMatrix_kernel_eq_zero (F G : Polynomial L) (m n : Nat)
    (hF0 : F ≠ 0) (hF : F.natDegree = n) (hG : G.natDegree <= m)
    (hcop : IsCoprime F G) (v : Fin (m+n) -> L)
    (hv : (coeffMatrix F G m n).mulVec v = 0) : v = 0 := by
  classical
  let A := boundedPolynomial (fun i : Fin m => v (Fin.castAdd n i))
  let B := boundedPolynomial (fun i : Fin n => v (Fin.natAdd m i))
  have hrel : A * F + B * G = 0 := kernel_syzygy F G m n hF.le hG v hv
  have hdiv : F ∣ B * G := by
    refine ⟨-A, ?_⟩
    linear_combination hrel
  have hBdiv : F ∣ B := hcop.dvd_of_dvd_mul_right hdiv
  have hB : B = 0 := by
    by_contra hB0
    have hle : n <= B.natDegree := by
      simpa only [hF] using Polynomial.natDegree_le_of_dvd hBdiv hB0
    apply hB0
    apply Polynomial.leadingCoeff_eq_zero.mp
    change B.coeff B.natDegree = 0
    exact boundedPolynomial_high_coeff _ _ hle
  have hA : A = 0 := by
    have hh : A * F = 0 := by simpa [hB] using hrel
    exact (mul_eq_zero.mp hh).resolve_right hF0
  funext j
  refine Fin.addCases (fun i => ?_) (fun i => ?_) j
  - have hh := congrArg (fun p : Polynomial L => p.coeff i.val) hA
    simpa only [A, boundedPolynomial_coeff, Polynomial.coeff_zero, Pi.zero_apply] using hh
  - have hh := congrArg (fun p : Polynomial L => p.coeff i.val) hB
    simpa only [B, boundedPolynomial_coeff, Polynomial.coeff_zero, Pi.zero_apply] using hh

/-- Field-level nonsingularity is proved by the actual coefficient kernel. -/
theorem coeffMatrix_det_ne_zero (F G : Polynomial L) (m n : Nat)
    (hF0 : F ≠ 0) (hF : F.natDegree = n) (hG : G.natDegree <= m)
    (hcop : IsCoprime F G) : (coeffMatrix F G m n).det ≠ 0 := by
  classical
  have hinj : Function.Injective (coeffMatrix F G m n).mulVec := by
    intro x y hxy
    apply sub_eq_zero.mp
    apply coeffMatrix_kernel_eq_zero F G m n hF0 hF hG hcop (x-y)
    simpa only [Matrix.mulVec_sub, hxy, sub_self]
  exact ((Matrix.isUnit_iff_isUnit_det _).mp
    (Matrix.mulVec_injective_iff_isUnit.mp hinj)).ne_zero

end
end NonzeroBridge
end TenthDiscriminant
