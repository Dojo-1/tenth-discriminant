import TenthDiscriminant.DeterminantMultiplicity

/-! Coefficient-level affine changes; exact bridge to the existing matrix below. -/
namespace TenthDiscriminant
open Matrix Polynomial
noncomputable section
section Coefficients
variable {R : Type*} [CommRing R]

/-- Finite coefficient matrix, with no determinant property built into its definition. -/
def coefficientMatrix {n : Nat} (cols : Fin n -> Polynomial R) :
    Matrix (Fin n) (Fin n) R := fun i j => (cols j).coeff i.val

def affinePolynomial (u h : R) : Polynomial R := Polynomial.C u * Polynomial.X + Polynomial.C h

def affineBasisMatrix (n : Nat) (u h : R) : Matrix (Fin n) (Fin n) R :=
  coefficientMatrix (fun j => (affinePolynomial u h)^j.val)

/-- This ordering uses m shifts of F, then n shifts of G. -/
def sylvesterColumns (F G : Polynomial R) (m n : Nat)
    (j : Fin (m+n)) : Polynomial R :=
  if j.val < m then Polynomial.X^j.val * F
    else Polynomial.X^(j.val-m) * G

def sylvesterCoefficients (F G : Polynomial R) (m n : Nat) :
    Matrix (Fin (m+n)) (Fin (m+n)) R := coefficientMatrix (sylvesterColumns F G m n)

/-- Exact finite coefficient reconstruction, including zero polynomials. -/
theorem finite_reconstruction (p : Polynomial R) (n : Nat) (hp : p.natDegree < n) :
    (Finset.univ.sum (fun k : Fin n => Polynomial.C (p.coeff k.val) * Polynomial.X^k.val)) = p := by
  rw [Fin.sum_univ_eq_sum_range (fun k => Polynomial.C (p.coeff k) * Polynomial.X^k) n]
  simpa only [Polynomial.C_mul_X_pow_eq_monomial] using (p.as_sum_range' n hp).symm

/-- Composition changes actual coefficient columns by the affine basis matrix. -/
theorem coefficientMatrix_comp {n : Nat} (cols : Fin n -> Polynomial R)
    (u h : R) (hdeg : forall j, (cols j).natDegree < n) :
    coefficientMatrix (fun j => (cols j).comp (affinePolynomial u h)) =
      affineBasisMatrix n u h * coefficientMatrix cols := by
  classical
  apply Matrix.ext
  intro i j
  have hp := (finite_reconstruction (cols j) n (hdeg j)).symm
  have hs (ps : Fin n -> Polynomial R) :
      (Finset.univ.sum ps).comp (affinePolynomial u h) =
        Finset.univ.sum (fun k => (ps k).comp (affinePolynomial u h)) :=
    (Polynomial.compRingHom (affinePolynomial u h)).map_sum ps Finset.univ
  have hc (ps : Fin n -> Polynomial R) :
      (Finset.univ.sum ps).coeff i.val = Finset.univ.sum (fun k => (ps k).coeff i.val) :=
    map_sum (Polynomial.lcoeff R i.val) ps Finset.univ
  change ((cols j).comp (affinePolynomial u h)).coeff i.val = _
  rw [hp, hs, hc]
  simp only [Polynomial.mul_comp, Polynomial.C_comp, Polynomial.pow_comp,
    Polynomial.X_comp, Polynomial.coeff_C_mul, Matrix.mul_apply,
    coefficientMatrix, affineBasisMatrix]
  apply Finset.sum_congr rfl
  intro k hk
  exact mul_comm _ _

/-- Both degree bounds are retained before and after specialization. -/
theorem sylvesterColumns_degree (F G : Polynomial R) (m n : Nat)
    (hF : F.natDegree <= n) (hG : G.natDegree <= m) (j : Fin (m+n)) :
    (sylvesterColumns F G m n j).natDegree < m+n := by
  unfold sylvesterColumns
  split_ifs with hj
  · have hd : (Polynomial.X^j.val * F).natDegree <=
        (Polynomial.X^j.val : Polynomial R).natDegree + F.natDegree :=
        Polynomial.natDegree_mul_le
    have hx : (Polynomial.X^j.val : Polynomial R).natDegree <= j.val := by simp
    omega
  · have hd : (Polynomial.X^(j.val-m) * G).natDegree <=
        (Polynomial.X^(j.val-m) : Polynomial R).natDegree + G.natDegree :=
        Polynomial.natDegree_mul_le
    have hx : (Polynomial.X^(j.val-m) : Polynomial R).natDegree <= j.val-m := by simp
    have hlt := j.isLt
    omega

/-- Separate affine coefficient changes on the two input multiplier spaces. -/
def sylvesterInputMatrix (m n : Nat) (u h : R) : Matrix (Fin (m+n)) (Fin (m+n)) R :=
  fun i j => if j.val < m then
    if i.val < m then ((affinePolynomial u h)^j.val).coeff i.val else 0
  else if i.val < m then 0
    else ((affinePolynomial u h)^(j.val-m)).coeff (i.val-m)


/-- A degree bound that does not assume nonzero slope. -/
theorem affinePolynomial_degree (u h : R) : (affinePolynomial u h).natDegree <= 1 := by
  unfold affinePolynomial
  compute_degree

theorem affine_power_degree (u h : R) (k : Nat) :
    ((affinePolynomial u h)^k).natDegree <= k := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [pow_succ]
    have hd : ((affinePolynomial u h)^k * affinePolynomial u h).natDegree <=
        ((affinePolynomial u h)^k).natDegree + (affinePolynomial u h).natDegree :=
      Polynomial.natDegree_mul_le
    have hq := affinePolynomial_degree u h
    omega

theorem affine_power_coeff (u h : R) (k : Nat) :
    ((affinePolynomial u h)^k).coeff k = u^k := by
  have hh := Polynomial.coeff_pow_of_natDegree_le (m := k) (n := 1)
    (affinePolynomial_degree u h)
  simpa [affinePolynomial, Polynomial.coeff_add, Polynomial.coeff_C_mul, Polynomial.coeff_X, Polynomial.coeff_C] using hh

def affinePowerProduct (n : Nat) (u : R) : R :=
  Finset.univ.prod (fun i : Fin n => u^i.val)

theorem affineBasisMatrix_det (n : Nat) (u h : R) :
    (affineBasisMatrix n u h).det = affinePowerProduct n u := by
  have ht : (affineBasisMatrix n u h).BlockTriangular id := by
    intro i j hij
    exact Polynomial.coeff_eq_zero_of_natDegree_lt
      ((affine_power_degree u h j.val).trans_lt hij)
  rw [Matrix.det_of_upperTriangular ht]
  apply Finset.prod_congr rfl
  intro i hi
  exact affine_power_coeff u h i.val

theorem sylvesterInputMatrix_det (m n : Nat) (u h : R) :
    (sylvesterInputMatrix m n u h).det = affinePowerProduct m u * affinePowerProduct n u := by
  have ht : (sylvesterInputMatrix m n u h).BlockTriangular id := by
    intro i j hij
    change j.val < i.val at hij
    unfold sylvesterInputMatrix
    split_ifs with hj hi hi
    all_goals first
      | rfl
      | exact Polynomial.coeff_eq_zero_of_natDegree_lt
          ((affine_power_degree u h j.val).trans_lt hij)
      | exact Polynomial.coeff_eq_zero_of_natDegree_lt
          ((affine_power_degree u h (j.val-m)).trans_lt (by omega))
      | omega
  have hd (i : Fin (m+n)) : sylvesterInputMatrix m n u h i i =
      if i.val < m then u^i.val else u^(i.val-m) := by
    unfold sylvesterInputMatrix
    split_ifs <;> exact affine_power_coeff u h _
  rw [Matrix.det_of_upperTriangular ht]
  simp_rw [hd]
  rw [Fin.prod_univ_add]
  congr 1
  · apply Finset.prod_congr rfl
    intro i hi
    simp [i.isLt]
  · apply Finset.prod_congr rfl
    intro i hi
    simp

/-- Input multipliers and output polynomials undergo the same affine substitution. -/
theorem sylvester_affine_matrix (F G : Polynomial R) (m n : Nat)
    (hF : F.natDegree <= n) (hG : G.natDegree <= m) (u h : R) :
    affineBasisMatrix (m+n) u h * sylvesterCoefficients F G m n =
      sylvesterCoefficients (F.comp (affinePolynomial u h))
        (G.comp (affinePolynomial u h)) m n * sylvesterInputMatrix m n u h := by
  classical
  rw [← coefficientMatrix_comp (sylvesterColumns F G m n) u h
    (sylvesterColumns_degree F G m n hF hG)]
  apply Matrix.ext
  intro i j
  have hsum (ps : Fin (m+n) -> Polynomial R) :
      (Finset.univ.sum ps).coeff i.val = Finset.univ.sum (fun k => (ps k).coeff i.val) :=
    map_sum (Polynomial.lcoeff R i.val) ps Finset.univ
  have hc : (sylvesterColumns F G m n j).comp (affinePolynomial u h) =
      Finset.univ.sum (fun k : Fin (m+n) =>
        Polynomial.C (sylvesterInputMatrix m n u h k j) *
          sylvesterColumns (F.comp (affinePolynomial u h))
            (G.comp (affinePolynomial u h)) m n k) := by
    rw [Fin.sum_univ_add]
    by_cases hj : j.val < m
    · have hl (k : Fin m) :
          Polynomial.C (sylvesterInputMatrix m n u h (Fin.castAdd n k) j) *
            sylvesterColumns (F.comp (affinePolynomial u h))
              (G.comp (affinePolynomial u h)) m n (Fin.castAdd n k) =
          (Polynomial.C (((affinePolynomial u h)^j.val).coeff k.val) * Polynomial.X^k.val) *
            F.comp (affinePolynomial u h) := by
        simp [sylvesterInputMatrix, sylvesterColumns, hj, k.isLt, mul_assoc]
      have hr (k : Fin n) :
          Polynomial.C (sylvesterInputMatrix m n u h (Fin.natAdd m k) j) *
            sylvesterColumns (F.comp (affinePolynomial u h))
              (G.comp (affinePolynomial u h)) m n (Fin.natAdd m k) = 0 := by
        simp [sylvesterInputMatrix, sylvesterColumns, hj]
      simp_rw [hl, hr]
      rw [Finset.sum_const_zero, add_zero, ← Finset.sum_mul,
        finite_reconstruction _ m ((affine_power_degree u h j.val).trans_lt hj)]
      simp [sylvesterColumns, hj, Polynomial.mul_comp]
    · have hl (k : Fin m) :
          Polynomial.C (sylvesterInputMatrix m n u h (Fin.castAdd n k) j) *
            sylvesterColumns (F.comp (affinePolynomial u h))
              (G.comp (affinePolynomial u h)) m n (Fin.castAdd n k) = 0 := by
        simp [sylvesterInputMatrix, sylvesterColumns, hj, k.isLt]
      have hr (k : Fin n) :
          Polynomial.C (sylvesterInputMatrix m n u h (Fin.natAdd m k) j) *
            sylvesterColumns (F.comp (affinePolynomial u h))
              (G.comp (affinePolynomial u h)) m n (Fin.natAdd m k) =
          (Polynomial.C (((affinePolynomial u h)^(j.val-m)).coeff k.val) * Polynomial.X^k.val) *
            G.comp (affinePolynomial u h) := by
        simp [sylvesterInputMatrix, sylvesterColumns, hj, mul_assoc]
      simp_rw [hl, hr]
      rw [Finset.sum_const_zero, zero_add, ← Finset.sum_mul,
        finite_reconstruction _ n ((affine_power_degree u h (j.val-m)).trans_lt (by have := j.isLt; omega))]
      simp [sylvesterColumns, hj, Polynomial.mul_comp]
  change ((sylvesterColumns F G m n j).comp (affinePolynomial u h)).coeff i.val = _
  rw [hc, hsum, Matrix.mul_apply]
  apply Finset.sum_congr rfl
  intro k hk
  simp only [Polynomial.coeff_C_mul, sylvesterCoefficients, coefficientMatrix]
  exact mul_comm _ _

theorem affinePowerProduct_add (m n : Nat) (u : R) :
    affinePowerProduct (m+n) u = affinePowerProduct m u * affinePowerProduct n u * u^(m*n) := by
  unfold affinePowerProduct
  rw [Fin.prod_univ_add]
  change (Finset.univ.prod (fun i : Fin m => u^i.val)) *
    (Finset.univ.prod (fun j : Fin n => u^(m+j.val))) = _
  simp only [pow_add, Finset.prod_mul_distrib,
    Finset.prod_const, Finset.card_univ, Fintype.card_fin, ← pow_mul]
  ring

variable [IsDomain R]

/-- Exact affine covariance of this coefficient-matrix convention. -/
theorem sylvesterCoefficients_affine (F G : Polynomial R) (m n : Nat)
    (hF : F.natDegree <= n) (hG : G.natDegree <= m)
    (u h : R) (hu : u ≠ 0) :
    (sylvesterCoefficients (F.comp (affinePolynomial u h))
      (G.comp (affinePolynomial u h)) m n).det =
      u^(m*n) * (sylvesterCoefficients F G m n).det := by
  have hd := congrArg Matrix.det (sylvester_affine_matrix F G m n hF hG u h)
  rw [Matrix.det_mul, Matrix.det_mul, affineBasisMatrix_det, sylvesterInputMatrix_det] at hd
  have hn : affinePowerProduct m u * affinePowerProduct n u ≠ 0 := by
    apply mul_ne_zero <;> apply Finset.prod_ne_zero_iff.mpr <;>
      intro i hi <;> exact pow_ne_zero _ hu
  apply mul_left_cancel₀ hn
  calc
    (affinePowerProduct m u * affinePowerProduct n u) *
        (sylvesterCoefficients (F.comp (affinePolynomial u h))
          (G.comp (affinePolynomial u h)) m n).det =
      (sylvesterCoefficients (F.comp (affinePolynomial u h))
          (G.comp (affinePolynomial u h)) m n).det *
        (affinePowerProduct m u * affinePowerProduct n u) := mul_comm _ _
    _ = affinePowerProduct (m+n) u * (sylvesterCoefficients F G m n).det := hd.symm
    _ = (affinePowerProduct m u * affinePowerProduct n u) *
        (u^(m*n) * (sylvesterCoefficients F G m n).det) := by
      rw [affinePowerProduct_add]
      ring

end Coefficients
end
end TenthDiscriminant
