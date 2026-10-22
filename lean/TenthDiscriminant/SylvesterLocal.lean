import TenthDiscriminant.DeterminantMultiplicity

/-! # Nonzero specialization and sharp local controls
The root-order bound is derived from nonzero specialization, not assumed.
No nonzero-resultant theorem or global point-count criterion is asserted.
-/
namespace TenthDiscriminant
open Polynomial Matrix
noncomputable section

/-- The local F/F_Z multiplicity statement with the necessary specialization premise. -/
theorem fixedDerivativeSylvester_multiplicity_at_nonzero
    {K : Type*} [Field K] (F : Polynomial (Polynomial K)) (a : Nat)
    (hF : F.natDegree <= a) (w z : K) (m : Nat)
    (hne : F.map (Polynomial.evalRingHom w) ≠ 0)
    (hroot : (Polynomial.X - Polynomial.C z)^m ∣ F.map (Polynomial.evalRingHom w)) :
    (Polynomial.X - Polynomial.C w)^(m-1) ∣
      (fixedSylvesterMatrix F F.derivative a (a-1)).det := by
  have hd := Polynomial.natDegree_le_of_dvd hroot hne
  have hm : m <= a := by
    have hmap : (F.map (Polynomial.evalRingHom w)).natDegree <= F.natDegree :=
      Polynomial.natDegree_map_le
    simp only [Polynomial.natDegree_pow, Polynomial.natDegree_X_sub_C, one_mul] at hd
    omega
  exact fixedDerivativeSylvester_multiplicity F a hF w z m hm hroot

/-- A genuine double root pays only one determinant factor: the local exponent is sharp. -/
theorem quadratic_fixedSylvester_det :
    let F : Polynomial (Polynomial Rat) := Polynomial.X^2 - Polynomial.C Polynomial.X
    (fixedSylvesterMatrix F F.derivative 2 1).det = -4 * Polynomial.X := by
  norm_num [fixedSylvesterMatrix, polynomialCoefficientMatrix, fixedSylvesterColumns,
    Matrix.det_fin_three, Polynomial.derivative_X_sq] <;> ring

/-- Exact counter-control for treating multiplicity m-1 as m. -/
theorem quadratic_fixedSylvester_linear_coefficient :
    let F : Polynomial (Polynomial Rat) := Polynomial.X^2 - Polynomial.C Polynomial.X
    ((fixedSylvesterMatrix F F.derivative 2 1).det).coeff 1 = -4 := by
  rw [quadratic_fixedSylvester_det]
  norm_num

/-- A globally repeated factor gives an identically zero determinant. -/
theorem repeated_fixedSylvester_det :
    let F : Polynomial (Polynomial Rat) := Polynomial.X^2
    (fixedSylvesterMatrix F F.derivative 2 1).det = 0 := by
  norm_num [fixedSylvesterMatrix, polynomialCoefficientMatrix, fixedSylvesterColumns,
    Matrix.det_fin_three, Polynomial.derivative_X_sq]

end
end TenthDiscriminant
