import TenthDiscriminant.JetPrecisionBridge

/-!
# Phase272 — a sharp *negative* transport test for ordinary jets modulo p

Historical inspiration: the Leibniz/SDG infinitesimal coefficient view
versus Newton's moving-frame intuition. All actual arithmetic uses the
repository's ORIGINAL integer-pair ordinary Z-jet, W held fixed.

Existing JetPrecisionBridge.lean already formalizes the factorial seam.
The new claim is a one-example *no-descended-translation* obstruction:
after reduction modulo 3, x^3 and the zero polynomial are indistinguishable
by ordinary jets at zero, but not at one. This is NOT a new field bound.
This tests a genuine representation-loss phenomenon, not holonomy.
-/

namespace TenthDiscriminant.Phase272
set_option autoImplicit false

/-- The 0..3 ordinary derivative values of Z³ at a real-axis point.
A subcase of the same integer pair jet source that defines the
tenth-discriminant positive trace Gram. -/
def cubicOrdinaryJet (a : Int) : Fin 4 → ZMod 3 :=
  fun j => ((integerDerivativeRow 19 3 0 j.val (a, 0)).1 : ZMod 3)

/-- Hasse/Taylor coefficient jets, a DIAGNOSTIC representation,
not a replacement for the original ordinary-jet production Gram. -/
def cubicHasseJet (a : Int) : Fin 4 → ZMod 3 :=
  fun j => ((integerHasseCoefficientRow 19 3 0 j.val (a, 0)).1 : ZMod 3)

def zeroJet : Fin 4 → ZMod 3 := fun _ => 0

/-- Every ordinary Z-derivative of the cubic at zero vanishes mod 3,
including the third derivative 3!=6. -/
theorem cubic_ordinary_origin_zero :
    cubicOrdinaryJet 0 = zeroJet := by
  funext j
  fin_cases j <;> decide

/-- After translating the observation by +1, its zeroth derivative is 1. -/
theorem cubic_ordinary_one_value :
    cubicOrdinaryJet 1 (0 : Fin 4) = 1 := by decide

theorem cubic_ordinary_one_ne_zero :
    cubicOrdinaryJet 1 ≠ zeroJet := by
  intro h
  have hh : cubicOrdinaryJet 1 (0 : Fin 4) = zeroJet 0 :=
    congrArg (fun f : Fin 4 → ZMod 3 => f 0) h
  have hbad : cubicOrdinaryJet 1 (0 : Fin 4) ≠ zeroJet 0 := by decide
  exact hbad hh

/-- The third Hasse coefficient of the cubic is still 1, on BOTH
sides of the translation. Its information is not erased modulo 3. -/
theorem cubic_hasse_third_at_zero :
    cubicHasseJet 0 (3 : Fin 4) = 1 := by decide

theorem cubic_hasse_third_at_one :
    cubicHasseJet 1 (3 : Fin 4) = 1 := by decide

/-- No FUNCTION on reduced ordinary-jet vectors can correctly transport
both the zero polynomial and Z³ from point zero to point one.
This directly refutes the false claim that ordinary modular jet data
has a universal basepoint-translation action above the p-th order.

The assumptions are two required source behaviors, not surrogates for
the class-number-one hypotheses. -/
theorem no_mod_three_ordinary_jet_transport
    (F : (Fin 4 → ZMod 3) → (Fin 4 → ZMod 3))
    (hzero : F zeroJet = zeroJet)
    (hcubic : F (cubicOrdinaryJet 0) = cubicOrdinaryJet 1) :
    False := by
  rw [cubic_ordinary_origin_zero, hzero] at hcubic
  exact cubic_ordinary_one_ne_zero hcubic.symm

/-- A new normalization cannot be attributed to the old ordinary jet
unless it accounts for the original factorial. Reuse the existing,
original-source bridge, rather than silently changing derivative type. -/
theorem cubic_source_factorial_control :
    integerDerivativeRow 19 3 0 3 (0, 0) =
      pairScale (3.factorial : Int)
        (integerHasseCoefficientRow 19 3 0 3 (0, 0)) :=
  integerDerivativeRow_eq_factorial_hasse 19 3 0 3 (0, 0)

#print axioms TenthDiscriminant.Phase272.no_mod_three_ordinary_jet_transport
#print axioms TenthDiscriminant.Phase272.cubic_source_factorial_control
end TenthDiscriminant.Phase272
