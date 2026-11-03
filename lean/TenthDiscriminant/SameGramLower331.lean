import TenthDiscriminant.SourcePositivity331
import TenthDiscriminant.Lower331
import TenthDiscriminant.BinaryGap375

/-!
# Phase186 — same-original-Gram lower at fourth-root 331

This file assembles the PREVIOUSLY PROVED once-counted binary factor and
the Phase185 original odd-prime mass on the identical Phase184 positive
integer ordinary-Z-jet thin-Q Gram. It does not prove a 331 analytic
upper, class-number exclusion, or discriminant cutoff.

The reusable "normalized_binary_quarter" theorem happens to be imported
from BinaryGap375, but has NO D >= 375 hypothesis: its input is just R,S>0.
No older field cutoff is transplanted here.
-/
namespace TenthDiscriminant
open FirstCertificate
open scoped BigOperators Classical
set_option autoImplicit false
noncomputable section

/-- Under the original odd squarefree class-number-one hypothesis, the
same positive thin-Q trace Gram has both the old odd and the single old
binary logarithmic lower, already normalized by the original R² S. -/
theorem thin_original_odd_plus_binary_normalized_lower_331
    (D : Nat) (hD : (331 : Nat)^4 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hc : NumberField.classNumber
       (QuadraticField (((D : Int)+1)/4))=1) :
    (999997/1000000 : Real)*Real.log D-5739/1000+
      Real.log 2/4 ≤
    Real.log ((integerRectangularTraceGram
       (ellipsePairs D (FirstCertificate.Tuned.thinRadius D)) D
       (FirstCertificate.Tuned.S D) (FirstCertificate.Tuned.R D)
       (FirstCertificate.Tuned.S D)).det : Real) /
      comparisonScale
        (FirstCertificate.Tuned.R D) (FirstCertificate.Tuned.S D) := by
  have hd := FirstCertificate.Tuned.dimensions_331 D hD
  have hp := comparisonScale_pos
    (FirstCertificate.Tuned.R D) (FirstCertificate.Tuned.S D)
    (by omega) (by omega)
  have hpositive := FirstCertificate.Tuned.thin_original_gram_pos_331 D hD
  have hsource := BinaryThinLogBridge.original_binary_and_exact_odd_mass_log_of_pos
    (ellipsePairs D (FirstCertificate.Tuned.thinRadius D)) D
    (FirstCertificate.Tuned.R D) (FirstCertificate.Tuned.S D)
    hsq hc (FirstCertificate.Tuned.strict_inertness D) hpositive
  have hodd := FirstCertificate.Tuned.recovered_mass_le_exact_odd_331 D hD
  have hmass :
      (binaryNullGramExponent
         (FirstCertificate.Tuned.R D) (FirstCertificate.Tuned.S D) : Real)*
        Real.log 2 +
      recoveredPrimeMassLower
        (FirstCertificate.Tuned.R D) (FirstCertificate.Tuned.S D)
        FirstEnderInterval.tailBudget ≤
      Real.log ((integerRectangularTraceGram
         (ellipsePairs D (FirstCertificate.Tuned.thinRadius D)) D
         (FirstCertificate.Tuned.S D) (FirstCertificate.Tuned.R D)
         (FirstCertificate.Tuned.S D)).det : Real) := by
    linarith
  have hdiv := div_le_div_of_nonneg_right hmass hp.le
  rw [add_div] at hdiv
  have hlower := FirstCertificate.Tuned.recovered_normalized_lower_331 D hD
  have hbin := normalized_binary_quarter
    (FirstCertificate.Tuned.R D) (FirstCertificate.Tuned.S D)
    (by omega) (by omega)
  have hjoint :
      (999997/1000000 : Real)*Real.log D-5739/1000 +
        Real.log 2/4 ≤
      Real.log ((integerRectangularTraceGram
         (ellipsePairs D (FirstCertificate.Tuned.thinRadius D)) D
         (FirstCertificate.Tuned.S D) (FirstCertificate.Tuned.R D)
         (FirstCertificate.Tuned.S D)).det : Real) /
        comparisonScale
          (FirstCertificate.Tuned.R D) (FirstCertificate.Tuned.S D) := by
    linarith
  exact hjoint

end
end TenthDiscriminant
