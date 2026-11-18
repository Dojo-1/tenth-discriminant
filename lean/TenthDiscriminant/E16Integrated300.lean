import TenthDiscriminant.E16JointLower300
import TenthDiscriminant.E15EuclidUpper

/-!
# E16b: one original integer Gram, lower and upper on the same Euclid Q

This source-integrated research bridge imports E6/E15 unchanged from public
main into the Phase349/Phase331 research closure and combines the VERIFIED
arbitrary-Q 300-domain joint arithmetic lower with the VERIFIED direct E15
upper. No determinant of a different Q or prime valuation is substituted.

The strict scalar separation is an EXPLICIT premise; there is no theorem
asserting it yet, and no new field-discriminant bound is claimed.
-/

namespace TenthDiscriminant.E16
open scoped BigOperators Classical
open TenthDiscriminant
open TenthDiscriminant.FirstCertificate
set_option autoImplicit false
noncomputable section

/-- The same original positive integer Gram normalization on both sides. -/
private def euclidLogGram (D : Nat) : Real :=
  Real.log ((integerRectangularTraceGram
    (ellipsePairs D (Tuned.euclidRadius D)) D
    (Tuned.S D) (Tuned.R D) (Tuned.S D)).det : Real) /
      comparisonScale (Tuned.R D) (Tuned.S D)

/-- The unchanged Phase331/Phase348 joint binary-plus-odd source expression. -/
def euclidArithmeticLower (D : Nat) : Real :=
  (999997/1000000 : Real)*Real.log D-57193/10000 +
      Real.log 2/4 +
      ((4659/625000 : Real)-16895455/(625000*(D : Real))) +
      ((6931/1000000 : Real)-2/(Tuned.R D : Real)) +
      ((873747/250000000 : Real)-40/(Tuned.R D : Real))

/-- E15's direct sharpened upper on EXACTLY the same integer Gram. -/
def euclidAnalyticUpper (D : Nat) : Real :=
  enderUpperB (Tuned.R D) (Tuned.S D) (Tuned.S D)
    (Tuned.euclidRadius D)
    (ellipseUpperCount D (Tuned.euclidRadius D)) /
    comparisonScale (Tuned.R D) (Tuned.S D) - 23/2000

/-- The exact arbitrary-Q arithmetic theorem specialized to E6's
original Gram; the positivity argument is explicitly from E6. -/
theorem euclid_lower_300 (D : Nat)
    (hD : (300 : Nat)^4 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hc : NumberField.classNumber
       (QuadraticField (((D : Int)+1)/4)) = 1) :
    euclidArithmeticLower D ≤ euclidLogGram D := by
  have h252 : (252 : Nat)^4 ≤ D := by omega
  have hpos := Tuned.euclid_original_integer_gram_det_pos_252 D h252
  simpa only [euclidArithmeticLower,euclidLogGram] using
    (original_source_joint_normalized_lower_300
      (ellipsePairs D (Tuned.euclidRadius D)) D hD hsq hc hpos)

/-- Same Q, same J=S, same R*S row layout and same integer matrix. -/
theorem euclid_upper_300 (D : Nat)
    (hD : (300 : Nat)^4 ≤ D) :
    euclidLogGram D ≤ euclidAnalyticUpper D := by
  have h252 : (252 : Nat)^4 ≤ D := by omega
  simpa only [euclidLogGram,euclidAnalyticUpper] using
    (Tuned.euclid_normalized_upper_252 D h252)

/-- A fully typed original-source sandwich at the 300 fourth-root floor.
The field hypothesis appears ONLY on the arithmetic-lower side. -/
theorem euclid_same_source_sandwich_300 (D : Nat)
    (hD : (300 : Nat)^4 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hc : NumberField.classNumber
       (QuadraticField (((D : Int)+1)/4)) = 1) :
    euclidArithmeticLower D ≤ euclidLogGram D ∧
      euclidLogGram D ≤ euclidAnalyticUpper D :=
  ⟨euclid_lower_300 D hD hsq hc, euclid_upper_300 D hD⟩

/-- Precisely the remaining scalar obligation. This theorem DOES NOT
prove that it holds for D>=300^4; its hypothesis is not hidden. -/
theorem contradiction_of_scalar_separation
    (D : Nat) (hD : (300 : Nat)^4 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hc : NumberField.classNumber
       (QuadraticField (((D : Int)+1)/4)) = 1)
    (hsep : euclidAnalyticUpper D < euclidArithmeticLower D) : False := by
  obtain ⟨hl,hu⟩ := euclid_same_source_sandwich_300 D hD hsq hc
  linarith

end
end TenthDiscriminant.E16

#print axioms TenthDiscriminant.E16.euclid_same_source_sandwich_300
#print axioms TenthDiscriminant.E16.contradiction_of_scalar_separation
