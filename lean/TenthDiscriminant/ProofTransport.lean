import TenthDiscriminant.RadialAction
import TenthDiscriminant.InertFrobenius

/-!
# Mixed arithmetic/radial observation frames: the same original Gram

These theorems use the repository's *actual* integer binomial frame and radial
frame on the original row-major rectangular jet Gram. No new prime condition,
cutoff, sample family, or formalized hyperbolic connection is introduced.

The tiny noncommutation control prevents interpreting two paths with the same
determinant as identical matrices. This file does not assert a new analytic bound.
-/
namespace TenthDiscriminant.ProofTransport
open Matrix
set_option autoImplicit false
noncomputable section

/-- The arithmetic frame followed by a radial frame is unimodular. -/
theorem radial_arithmetic_det_one
    (R S p : Nat) (hp : 0 < p) (a : Int) :
    (RadialOperator.matrix R S a * rectangularBasisMatrix R S p).det = 1 := by
  rw [Matrix.det_mul, RadialOperator.determinant_one,
    rectangularBasisMatrix_det R S p hp]
  norm_num

/-- Reversing the frame order also preserves the integer lattice index. -/
theorem arithmetic_radial_det_one
    (R S p : Nat) (hp : 0 < p) (a : Int) :
    (rectangularBasisMatrix R S p * RadialOperator.matrix R S a).det = 1 := by
  rw [Matrix.det_mul, RadialOperator.determinant_one,
    rectangularBasisMatrix_det R S p hp]
  norm_num

/-- One concrete mixed-frame route preserves the original determinant. -/
theorem radial_arithmetic_same_gram_det
    (Q : Finset (Int × Int)) (D J R S p : Nat)
    (hp : 0 < p) (a : Int) :
    let T := RadialOperator.matrix R S a * rectangularBasisMatrix R S p
    (T * integerRectangularTraceGram Q D J R S * T.transpose).det =
      (integerRectangularTraceGram Q D J R S).det := by
  dsimp
  simp only [Matrix.det_mul, Matrix.det_transpose,
    radial_arithmetic_det_one R S p hp a, one_mul, mul_one]

/-- The opposite order has the same determinant despite different frames. -/
theorem arithmetic_radial_same_gram_det
    (Q : Finset (Int × Int)) (D J R S p : Nat)
    (hp : 0 < p) (a : Int) :
    let T := rectangularBasisMatrix R S p * RadialOperator.matrix R S a
    (T * integerRectangularTraceGram Q D J R S * T.transpose).det =
      (integerRectangularTraceGram Q D J R S).det := by
  dsimp
  simp only [Matrix.det_mul, Matrix.det_transpose,
    arithmetic_radial_det_one R S p hp a, one_mul, mul_one]

/-- Transport does not destroy the guarded prime-power divisor. -/
theorem radial_arithmetic_inert_divisor
    (Q : Finset (Int × Int)) (D J R S p : Nat)
    [Fact p.Prime] (hp2 : p ≠ 2)
    (hns : ¬ IsSquare (-(D : ZMod p))) (a : Int) :
    let T := RadialOperator.matrix R S a * rectangularBasisMatrix R S p
    (p : Int) ^ (2 * valuationWeight R S p) ∣
      (T * integerRectangularTraceGram Q D J R S * T.transpose).det := by
  dsimp
  rw [radial_arithmetic_same_gram_det Q D J R S p
    (Fact.out : p.Prime).pos a]
  exact rectangularTraceGram_valuation_of_nonsquare
    Q D J R S p hp2 hns

/-- The reverse order preserves the same arithmetic divisor. -/
theorem arithmetic_radial_inert_divisor
    (Q : Finset (Int × Int)) (D J R S p : Nat)
    [Fact p.Prime] (hp2 : p ≠ 2)
    (hns : ¬ IsSquare (-(D : ZMod p))) (a : Int) :
    let T := rectangularBasisMatrix R S p * RadialOperator.matrix R S a
    (p : Int) ^ (2 * valuationWeight R S p) ∣
      (T * integerRectangularTraceGram Q D J R S * T.transpose).det := by
  dsimp
  rw [arithmetic_radial_same_gram_det Q D J R S p
    (Fact.out : p.Prime).pos a]
  exact rectangularTraceGram_valuation_of_nonsquare
    Q D J R S p hp2 hns

/-- Same determinant does NOT mean the arithmetic and radial frames commute.
For R=5,S=2,p=3,a=1 the old row-major indices 8 and 0 witness the defect. -/
theorem two_frame_noncommutation_control :
    (RadialOperator.matrix 5 2 1 * rectangularBasisMatrix 5 2 3) 8 0 = 0 ∧
    (rectangularBasisMatrix 5 2 3 * RadialOperator.matrix 5 2 1) 8 0 = 1 := by
  decide

/-- A split-prime control: z=t in Z[sqrt(-2)], t^3-conj(t)=-t, not in 3A. -/
theorem split_prime_frobenius_control :
    ¬ (3 : Int) ∣
      (pairPow 2 (0, 1) 3).2 - (pairConj (0, 1)).2 := by
  decide

/-- The original derivative convention is load-bearing, not an optional chart. -/
theorem hasse_convention_control :
    ¬ (3 : Int) ∣
      ((Polynomial.hasseDeriv 3)
        (Polynomial.X ^ 3 : Polynomial Int)).eval 0 :=
  hasse_derivative_negative_control

end
end TenthDiscriminant.ProofTransport
