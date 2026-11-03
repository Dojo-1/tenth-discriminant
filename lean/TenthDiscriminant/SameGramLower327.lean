import TenthDiscriminant.SourcePositivity327
import TenthDiscriminant.SourceOddBinary327

/-!
# Phase195 — specialize the ORIGINAL 327 source arithmetic to its thin positive Gram

Original ellipsePairs, original ordinary-Z jets holding W fixed,
original trace weights 2,2D, unchanged R,S. The generic arithmetic
source lower carries an explicit Gram positivity premise; Phase193
supplies exactly that premise. No additional prime, padded determinant,
or higher-root premise is inserted.
This is a theorem target until exact-head Lean CI passes.
-/
namespace TenthDiscriminant
open FirstCertificate
open scoped BigOperators Classical
set_option autoImplicit false
noncomputable section

theorem thin_original_odd_plus_binary_normalized_lower_327
    (D : Nat) (hD : (327 : Nat)^4 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hc : NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4))=1) :
    (999997/1000000 : Real)*Real.log D-57305/10000+
      Real.log 2/4 ≤
    Real.log ((integerRectangularTraceGram
       (ellipsePairs D (FirstCertificate.Tuned.thinRadius D)) D
       (FirstCertificate.Tuned.S D) (FirstCertificate.Tuned.R D)
       (FirstCertificate.Tuned.S D)).det : Real) /
      comparisonScale
        (FirstCertificate.Tuned.R D) (FirstCertificate.Tuned.S D) := by
  have hp := FirstCertificate.Tuned.thin_original_gram_pos_327 D hD
  exact original_source_odd_plus_binary_normalized_lower_of_pos_327
    (ellipsePairs D (FirstCertificate.Tuned.thinRadius D))
    D hD hsq hc hp

end
end TenthDiscriminant
