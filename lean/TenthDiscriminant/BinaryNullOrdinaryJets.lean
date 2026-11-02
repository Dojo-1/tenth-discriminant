import TenthDiscriminant.BinaryNullPolynomial
import TenthDiscriminant.JetPower

/-!
# Every ordinary derivative of the binary null polynomial

The original jet convention differentiates in Z while W is fixed.
This file supplies the missing all-derivative input to the existing
jet_power_dvd theorem. It does NOT change the production row basis or
claim that the complete Gram determinant factor has been formalized.
-/
namespace TenthDiscriminant
open Polynomial
set_option autoImplicit false

/-- The integer-coordinate computation is really a divisibility
statement inside the selected quadratic order, not merely a norm. -/
theorem binaryNull_value_dvd_zsqrtd (D : Nat) (a : Int × Int) :
    (2 : Zsqrtd (-(D : Int))) ∣
      (pairZsqrtdEquiv D a) ^ 4 - (pairZsqrtdEquiv D a) ^ 2 := by
  rw [← pairZsqrtd_pow D a 4, ← pairZsqrtd_pow D a 2]
  apply (zsqrtd_natCast_dvd_iff (-(D : Int)) 2 _).2
  simpa [pairZsqrtdEquiv] using binaryNullPower_even D a

/-- In the source order, every ordinary jet of F=Z^4-Z^2 has a
factor two. Order zero uses binary parity of the actual sample;
positive orders use the factor in the ordinary derivative coefficient. -/
theorem binaryNull_allOrdinaryJets_dvd (D : Nat) (a : Int × Int) (j : Nat) :
    (2 : Zsqrtd (-(D : Int))) ∣
      (derivative^[j] (X ^ 4 - X ^ 2 :
        (Zsqrtd (-(D : Int)))[X])).eval (pairZsqrtdEquiv D a) := by
  by_cases hj : j = 0
  · subst j
    simpa using binaryNull_value_dvd_zsqrtd D a
  · rw [iterate_derivative_sub, eval_sub]
    have h4 : (4 : Zsqrtd (-(D : Int))) ∣
        (derivative^[j] (X ^ 4 :
          (Zsqrtd (-(D : Int)))[X])).eval (pairZsqrtdEquiv D a) :=
      dvd_iterate_derivative_pow X 4 _ hj
    have htwo : (2 : Zsqrtd (-(D : Int))) ∣ (4 : Zsqrtd (-(D : Int))) := by
      refine ⟨2, ?_⟩
      norm_num
    have h2 : (2 : Zsqrtd (-(D : Int))) ∣
        (derivative^[j] (X ^ 2 :
          (Zsqrtd (-(D : Int)))[X])).eval (pairZsqrtdEquiv D a) :=
      dvd_iterate_derivative_pow X 2 _ hj
    exact (dvd_trans htwo h4).sub h2

/-- All powers of F retain their full binary factor through every
ordinary derivative. The reusable Leibniz induction is jet_power_dvd
in the existing JetPower.lean, not a new parallel proof. -/
theorem binaryNull_power_allOrdinaryJets_dvd
    (D : Nat) (a : Int × Int)
    (B : (Zsqrtd (-(D : Int)))[X]) (k j : Nat) :
    (2 : Zsqrtd (-(D : Int))) ^ k ∣
      (derivative^[j] (B * (X ^ 4 - X ^ 2) ^ k)).eval
        (pairZsqrtdEquiv D a) :=
  jet_power_dvd B (X ^ 4 - X ^ 2)
    (pairZsqrtdEquiv D a) (2 : Zsqrtd (-(D : Int)))
    (fun t => binaryNull_allOrdinaryJets_dvd D a t) k j

end TenthDiscriminant
