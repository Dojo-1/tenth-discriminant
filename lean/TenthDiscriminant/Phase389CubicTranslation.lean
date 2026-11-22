import Mathlib

/-!
# Phase389 — the characteristic-three cubic translation identity

This is a FIRST formal bridge into the Phase388 source argument, NOT a
formal proof of the full 400x216 D403 matrix rank. The cubic statement is
valid in any commutative characteristic-three ring (including F9). The
integer-coordinate quotient-shift facts are about the literal quadratic
pair expressions; the required source-integrality and ordinary-jet
intertwining theorems remain separate obligations.

No sorry, axioms, or replaced Hasse jets.
-/

namespace TenthDiscriminant.Phase389
set_option autoImplicit false

section Cubic

variable {A : Type*} [CommRing A]

/-- A polynomial of degree at most three in a Frobenius-quotient coordinate. -/
def cubic (a₀ a₁ a₂ a₃ q : A) : A :=
  a₀ + a₁*q + a₂*q^2 + a₃*q^3

/-- The *formal ordinary* first derivative of cubic with respect to q. -/
def cubicFormalDeriv (a₁ a₂ a₃ q : A) : A :=
  a₁ + 2*a₂*q + 3*a₃*q^2

/-- Integer-coefficient factorisation proves the three-sample sum. -/
theorem cubic_three_point_sum
    (h3 : (3 : A) = 0) (a₀ a₁ a₂ a₃ q : A) :
    cubic a₀ a₁ a₂ a₃ q +
      cubic a₀ a₁ a₂ a₃ (q-1) +
      cubic a₀ a₁ a₂ a₃ (q-2) = 2*a₂ := by
  have hfactor :
      (cubic a₀ a₁ a₂ a₃ q +
        cubic a₀ a₁ a₂ a₃ (q-1) +
        cubic a₀ a₁ a₂ a₃ (q-2)) - 2*a₂ =
      (3 : A) * (a₀ + a₁*q-a₁ + a₂*q^2-2*a₂*q+a₂ +
                 a₃*q^3-3*a₃*q^2+5*a₃*q-3*a₃) := by
    dsimp [cubic]
    ring
  apply sub_eq_zero.mp
  rw [hfactor, h3]
  ring

/-- A second integer-coefficient factorisation proves derivative transport. -/
theorem cubic_formal_deriv_shift
    (h3 : (3 : A) = 0) (a₁ a₂ a₃ q t : A) :
    2 * (cubicFormalDeriv a₁ a₂ a₃ (q-t) -
          cubicFormalDeriv a₁ a₂ a₃ q) = 2*t*a₂ := by
  have hfactor :
      2 * (cubicFormalDeriv a₁ a₂ a₃ (q-t) -
            cubicFormalDeriv a₁ a₂ a₃ q) - 2*t*a₂ =
      (3 : A) * (-2*t*(a₂+2*a₃*q-a₃*t)) := by
    dsimp [cubicFormalDeriv]
    ring
  apply sub_eq_zero.mp
  rw [hfactor, h3]
  ring

/-- The characteristic-three S=4 three-point law, with no elliptic,
number-field, or determinant hypothesis hidden in its statement. -/
theorem cubic_three_point_translation
    (h3 : (3 : A) = 0) (a₀ a₁ a₂ a₃ q t : A) :
    2 * (cubicFormalDeriv a₁ a₂ a₃ (q-t) -
          cubicFormalDeriv a₁ a₂ a₃ q) =
      t * (cubic a₀ a₁ a₂ a₃ q +
           cubic a₀ a₁ a₂ a₃ (q-1) +
           cubic a₀ a₁ a₂ a₃ (q-2)) := by
  rw [cubic_formal_deriv_shift h3 a₁ a₂ a₃ q t,
      cubic_three_point_sum h3 a₀ a₁ a₂ a₃ q]
  ring

/-- A quartic violates the cubic identity. This guards the S=5,k=4
overgeneralization detected in Phase388. -/
theorem quartic_three_point_false :
    (2 : ZMod 3) *
      ((4 : ZMod 3) * (((0 : ZMod 3)-1)^3) -
       (4 : ZMod 3) * ((0 : ZMod 3)^3))
      ≠ (1 : ZMod 3) *
        ((0 : ZMod 3)^4 + (((0 : ZMod 3)-1)^4) +
          (((0 : ZMod 3)-2)^4)) := by
  decide

end Cubic

section QuadraticSourceShift

/-- Literal first coordinate of (z³-conj(z))/3 in the beta²=-D
quadratic source chart, with integer division. -/
def sourceQuotReal (D x y : ℤ) : ℤ :=
  (x^3-3*D*x*y^2-x)/3

/-- Literal beta coefficient of (z³-conj(z))/3 in the same chart.
The actual Frobenius source integrality requires D≡1 mod3. -/
def sourceQuotImag (D x y : ℤ) : ℤ :=
  (3*x^2*y-D*y^3+y)/3

/-- Exact integer difference when x changes by 3t. Holds even before
imposing the inert-source integrality condition. -/
theorem sourceQuotReal_shift (D x y t : ℤ) :
    sourceQuotReal D (x+3*t) y =
      sourceQuotReal D x y +
      (3*x^2*t+9*x*t^2+9*t^3-t-3*D*t*y^2) := by
  let a : ℤ := x^3-3*D*x*y^2-x
  let b : ℤ := 3*x^2*t+9*x*t^2+9*t^3-t-3*D*t*y^2
  change ((x+3*t)^3-3*D*(x+3*t)*y^2-(x+3*t))/3 = a/3+b
  have h : (x+3*t)^3-3*D*(x+3*t)*y^2-(x+3*t) =
      a+3*b := by
    dsimp [a, b]
    ring
  rw [h]
  omega

/-- Exact integer difference for the second quadratic-source coordinate. -/
theorem sourceQuotImag_shift (D x y t : ℤ) :
    sourceQuotImag D (x+3*t) y =
      sourceQuotImag D x y + 3*t*y*(3*t+2*x) := by
  let a : ℤ := 3*x^2*y-D*y^3+y
  let b : ℤ := 3*t*y*(3*t+2*x)
  change (3*(x+3*t)^2*y-D*y^3+y)/3 = a/3+b
  have h : 3*(x+3*t)^2*y-D*y^3+y = a+3*b := by
    dsimp [a, b]
    ring
  rw [h]
  omega

/-- The source Frobenius quotient changes by the scalar -t modulo 3.
This is NOT yet the claim that its values are the derivatives of every
normalized source frame row; that is the missing Phase389 interface. -/
theorem sourceQuotReal_shift_mod3 (D x y t : ℤ) :
    ((sourceQuotReal D (x+3*t) y : ℤ) : ZMod 3) =
      ((sourceQuotReal D x y : ℤ) : ZMod 3) - (t : ZMod 3) := by
  rw [sourceQuotReal_shift]
  push_cast
  have hthree : (3 : ZMod 3) = 0 := by decide
  have hnine : (9 : ZMod 3) = 0 := by decide
  simp [hthree, hnine]

theorem sourceQuotImag_shift_mod3 (D x y t : ℤ) :
    ((sourceQuotImag D (x+3*t) y : ℤ) : ZMod 3) =
      ((sourceQuotImag D x y : ℤ) : ZMod 3) := by
  rw [sourceQuotImag_shift]
  push_cast
  have hthree : (3 : ZMod 3) = 0 := by decide
  simp [hthree]

end QuadraticSourceShift
end TenthDiscriminant.Phase389

#print axioms TenthDiscriminant.Phase389.cubic_three_point_translation
#print axioms TenthDiscriminant.Phase389.quartic_three_point_false
#print axioms TenthDiscriminant.Phase389.sourceQuotReal_shift_mod3
#print axioms TenthDiscriminant.Phase389.sourceQuotImag_shift_mod3
