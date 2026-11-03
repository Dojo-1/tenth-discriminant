import TenthDiscriminant.Lower323
import TenthDiscriminant.BinaryGap375

/-!
# Phase191 — original positive source-Gram arithmetic lower at fourth-root 323

This file assembles Phase190's stronger p=3,5 odd-prime mass and the
once-counted original binary factor on ANY user-supplied positive
integer ordinary-Z-jet source Gram. Positivity is an explicit premise. It does not prove 323 original thin support positivity, an analytic
upper, class-number exclusion, or a field discriminant cutoff.

The reusable "normalized_binary_quarter" theorem happens to be imported
from BinaryGap375, but has NO D >= 375 hypothesis: its input is just R,S>0.
No older field cutoff is transplanted here.
-/
namespace TenthDiscriminant
open FirstCertificate
open scoped BigOperators Classical
set_option autoImplicit false
noncomputable section

/-- Under the original odd squarefree class-number-one hypothesis, any
chosen support Q with a positive ORIGINAL trace Gram carries both the
sharpened odd-prime mass and exactly one existing binary exponent.
This is conditional on Gram positivity; no thin-ellipse geometry is inferred. -/
theorem original_source_odd_plus_binary_normalized_lower_of_pos_323
    (Q : Finset (Int × Int))
    (D : Nat) (hD : (323 : Nat)^4 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hc : NumberField.classNumber
       (QuadraticField (((D : Int)+1)/4))=1)
    (hpositive : 0 < (integerRectangularTraceGram Q D
       (FirstCertificate.Tuned.S D) (FirstCertificate.Tuned.R D)
       (FirstCertificate.Tuned.S D)).det) :
    (999997/1000000 : Real)*Real.log D-57205/10000+
      Real.log 2/4 ≤
    Real.log ((integerRectangularTraceGram
       Q D
       (FirstCertificate.Tuned.S D) (FirstCertificate.Tuned.R D)
       (FirstCertificate.Tuned.S D)).det : Real) /
      comparisonScale
        (FirstCertificate.Tuned.R D) (FirstCertificate.Tuned.S D) := by
  have hd := FirstCertificate.Tuned.dimensions_323 D hD
  have hp := comparisonScale_pos
    (FirstCertificate.Tuned.R D) (FirstCertificate.Tuned.S D)
    (by omega) (by omega)
  have hsource := BinaryThinLogBridge.original_binary_and_exact_odd_mass_log_of_pos
    Q D
    (FirstCertificate.Tuned.R D) (FirstCertificate.Tuned.S D)
    hsq hc (FirstCertificate.Tuned.strict_inertness D) hpositive
  have hodd := FirstCertificate.Tuned.recovered_mass_le_exact_odd_323 D hD
  have hmass :
      (binaryNullGramExponent
         (FirstCertificate.Tuned.R D) (FirstCertificate.Tuned.S D) : Real)*
        Real.log 2 +
      recoveredPrimeMassLower
        (FirstCertificate.Tuned.R D) (FirstCertificate.Tuned.S D)
        FirstEnderInterval.tailBudget ≤
      Real.log ((integerRectangularTraceGram
         Q D
         (FirstCertificate.Tuned.S D) (FirstCertificate.Tuned.R D)
         (FirstCertificate.Tuned.S D)).det : Real) := by
    linarith
  have hdiv := div_le_div_of_nonneg_right hmass hp.le
  rw [add_div] at hdiv
  have hlower := FirstCertificate.Tuned.recovered_normalized_lower_323 D hD
  have hbin := normalized_binary_quarter
    (FirstCertificate.Tuned.R D) (FirstCertificate.Tuned.S D)
    (by omega) (by omega)
  have hjoint :
      (999997/1000000 : Real)*Real.log D-57205/10000 +
        Real.log 2/4 ≤
      Real.log ((integerRectangularTraceGram
         Q D
         (FirstCertificate.Tuned.S D) (FirstCertificate.Tuned.R D)
         (FirstCertificate.Tuned.S D)).det : Real) /
        comparisonScale
          (FirstCertificate.Tuned.R D) (FirstCertificate.Tuned.S D) := by
    linarith
  exact hjoint

end
end TenthDiscriminant
