import TenthDiscriminant.AffineTransport
import TenthDiscriminant.SylvesterLocal

/-! Matched concrete controls for the actual affine-transport theorem. -/
namespace TenthDiscriminant
open Polynomial Matrix
noncomputable section

def affineControlPolynomial : Polynomial (Polynomial Rat) :=
  Polynomial.X^2 - Polynomial.C Polynomial.X

theorem affine_control_degree : affineControlPolynomial.natDegree = 2 := by
  unfold affineControlPolynomial
  compute_degree
  norm_num

theorem affine_control_source_det :
    fixedDerivativeDeterminant affineControlPolynomial 2 = -4 * Polynomial.X := by
  exact quadratic_fixedSylvester_det

/-- All five frame parameters active, including the inverse evaluation point. -/
theorem affine_control_combined_value :
    (fixedDerivativeDeterminant
      (affineTransportPolynomial affineControlPolynomial 3 2 5 7 (-2)) 2).eval (3/7) = -1728 := by
  have hd : (fixedDerivativeDeterminant affineControlPolynomial 2).eval 1 = -4 := by
    rw [affine_control_source_det]
    norm_num
  have hh := affineTransport_witness_value affineControlPolynomial 2 (by decide)
    affine_control_degree 3 2 5 7 (-2) 1 (-4) (by norm_num) (by norm_num) hd
  norm_num at hh
  exact hh

/-- Direct coefficient calculation, without the transport theorem: the slope contributes power four. -/
theorem affine_control_slope_direct :
    let F : Polynomial (Polynomial Rat) := 4 * Polynomial.X^2 - Polynomial.C Polynomial.X
    (fixedSylvesterMatrix F F.derivative 2 1).det = -64 * Polynomial.X := by
  dsimp only
  unfold fixedSylvesterMatrix polynomialCoefficientMatrix
  rw [Matrix.det_fin_three]
  norm_num [fixedSylvesterColumns, Polynomial.derivative_X_sq,
    Polynomial.derivative_mul, Polynomial.coeff_X, Polynomial.coeff_one,
    Polynomial.coeff_C, Polynomial.coeff_X_pow, Polynomial.coeff_C_mul,
    Polynomial.coeff_mul_X, Polynomial.coeff_X_mul]
  ring

/-- The same theorem gives the scalar power three, not four, in degree two. -/
theorem affine_control_scalar_value :
    (fixedDerivativeDeterminant
      (affineTransportPolynomial affineControlPolynomial 3 1 0 1 0) 2).eval 1 = -108 := by
  have hd : (fixedDerivativeDeterminant affineControlPolynomial 2).eval 1 = -4 := by
    rw [affine_control_source_det]
    norm_num
  have hh := affineTransport_witness_value affineControlPolynomial 2 (by decide)
    affine_control_degree 3 1 0 1 0 1 (-4) (by norm_num) (by norm_num) hd
  norm_num at hh
  exact hh

/-- A singular scale can erase a previously nonzero witness. -/
theorem affine_control_zero_scale :
    (fixedDerivativeDeterminant
      (affineTransportPolynomial affineControlPolynomial 0 1 0 1 0) 2).eval 1 = 0 := by
  have hd : (fixedDerivativeDeterminant affineControlPolynomial 2).eval 1 = -4 := by
    rw [affine_control_source_det]
    norm_num
  have hh := affineTransport_witness_value affineControlPolynomial 2 (by decide)
    affine_control_degree 0 1 0 1 0 1 (-4) (by norm_num) (by norm_num) hd
  norm_num at hh
  exact hh

/-- A zero resultant is not promoted to nonzero by an invertible frame change. -/
theorem affine_control_repeated :
    let F : Polynomial (Polynomial Rat) := Polynomial.X^2
    fixedDerivativeDeterminant (affineTransportPolynomial F 3 2 5 7 (-2)) 2 = 0 := by
  dsimp only
  rw [fixedDerivativeDeterminant_affine _ 2 (by decide) (by simp)
    3 2 5 7 (-2) (by norm_num)]
  change _ * (fixedDerivativeDeterminant (Polynomial.X^2) 2).comp _ = 0
  have hz : fixedDerivativeDeterminant (Polynomial.X^2 : Polynomial (Polynomial Rat)) 2 = 0 :=
    repeated_fixedSylvester_det
  rw [hz]
  simp

/-- Degree one, where the first Sylvester block is empty, is retained. -/
theorem affine_control_linear :
    let F : Polynomial (Polynomial Rat) := Polynomial.C Polynomial.X * Polynomial.X + 1
    fixedDerivativeDeterminant F 1 = Polynomial.X := by
  dsimp only
  simp [fixedDerivativeDeterminant, fixedSylvesterMatrix, polynomialCoefficientMatrix,
    fixedSylvesterColumns, Matrix.det_unique, Polynomial.derivative_C_mul]

end
end TenthDiscriminant
