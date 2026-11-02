import TenthDiscriminant.ThinIntegratedEndpoint
import TenthDiscriminant.BinaryNullTraceGram

/-!
# Phase164: the odd and binary arithmetic certificates on ONE thin Gram

Human explanation:
* Build the original ordinary-derivative integer matrix at the NEW thin
  ellipse Q. The metric still has weights 2 and 2D.
* The same rank/count guard makes the determinant a POSITIVE INTEGER.
* Phase162 proves a power of two divides that very determinant.
* The old class-number-one argument proves an ODD-prime product divides it.
* Coprimality combines them into a single integer divisor; no prime is
  multiplied twice. A positive integer divisible by N is at least N.

This file does not add a new numerical discriminant cutoff. In particular,
the count/radius theorem still needs D >= 41006250000. See issue #82.
-/

namespace TenthDiscriminant.BinaryThinGramBridge
open RadialCutoff
set_option autoImplicit false

/-- Identical observation set for the p-adic and real estimates. -/
private def thinQ (D : Nat) : Finset (Int × Int) :=
  ellipsePairs D (Tuned.thinRadius D)

/-- The existing thin interpolation count certifies positivity of the
unchanged original ordinary-Z-jet trace Gram. -/
theorem thin_original_gram_pos (D : Nat)
    (hD : 41006250000 ≤ D) :
    0 < (integerRectangularTraceGram (thinQ D) D
      (Tuned.S D) (Tuned.R D) (Tuned.S D)).det := by
  have hd := Tuned.dimensions D hD
  have hS : 1 ≤ Tuned.S D := by omega
  have hR : 1 ≤ Tuned.R D := by omega
  exact integer_det_positive (thinQ D) D (Tuned.R D) (Tuned.S D)
    (by omega) hR hS (by
      simpa only [thinQ] using Tuned.thin_radius_interpolation_count D hD)

/-- The combined local power of 2 and the already certified *odd-only*
prime mass divide the SAME thin-Q integer Gram. The field prerequisites
are not weakened, and the four-generator 1358 exponent is NOT used. -/
theorem thin_binary_odd_original_gram_dvd (D : Nat)
    (hD : 41006250000 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hclass : NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) = 1) :
    ((2 ^ binaryNullGramExponent (Tuned.R D) (Tuned.S D) *
      ∏ p ∈ oddPrimesBelow (Tuned.R D),
        p ^ (2 * valuationWeight (Tuned.R D) (Tuned.S D) p) : Nat) : Int) ∣
      (integerRectangularTraceGram (thinQ D) D
        (Tuned.S D) (Tuned.R D) (Tuned.S D)).det := by
  exact originalGram_binary_oddMass_unconditional
    (thinQ D) D (Tuned.R D) (Tuned.S D)
    hsq hclass (Tuned.strict_inertness D)

/-- A strict POSITIVE determinant and the exact divisor supply an
integer lower bound. There are no floating-point operations here. -/
theorem thin_binary_odd_le_original_gram (D : Nat)
    (hD : 41006250000 ≤ D)
    [Fact ((D : Int)%4=3)] (hsq : Squarefree D)
    (hclass : NumberField.classNumber
      (QuadraticField (((D : Int)+1)/4)) = 1) :
    ((2 ^ binaryNullGramExponent (Tuned.R D) (Tuned.S D) *
      ∏ p ∈ oddPrimesBelow (Tuned.R D),
        p ^ (2 * valuationWeight (Tuned.R D) (Tuned.S D) p) : Nat) : Int) ≤
      (integerRectangularTraceGram (thinQ D) D
        (Tuned.S D) (Tuned.R D) (Tuned.S D)).det := by
  exact Int.le_of_dvd (thin_original_gram_pos D hD)
    (thin_binary_odd_original_gram_dvd D hD hsq hclass)

end TenthDiscriminant.BinaryThinGramBridge
