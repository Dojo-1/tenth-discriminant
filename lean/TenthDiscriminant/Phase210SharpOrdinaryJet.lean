import TenthDiscriminant.RectangularBasisMatrix
import TenthDiscriminant.IntegerTraceGram

/-!
# Phase210 — the first sharp ordinary-jet depth in the ACTUAL source

Pre-registered under Issue #154. For p=3, S=10 and r=9,s=0,
k=min(r/p,S-1-s)=3, so F_{9,0}=(Z^3-W)^3
  = Z^9 - 3 Z^6 W + 3 Z^3 W^2 - W^3.
At ordinary derivative order 9 (W fixed), only Z^9 survives.
The original integral p^3 factor leaves 9!/27=13440, divisible by 3,
but not by 9. This is only a sharp, source-exact FINITE witness for
E_3(9)=1, not the universal Taylor theorem or its determinant bridge.
-/
namespace TenthDiscriminant.Phase210SharpOrdinaryJet

open TenthDiscriminant

/-- Four ORIGINAL monomial ordinary-jet rows, not a substituted
polynomial-derivative convention. The coefficients are precisely
the binomial expansion of (Z^3-W)^3. -/
def originalP3NineJet (D : Nat) (a : Int × Int) : Int × Int :=
  ((integerDerivativeRow D 9 0 9 a).1
      - 3 * (integerDerivativeRow D 6 1 9 a).1
      + 3 * (integerDerivativeRow D 3 2 9 a).1
      - (integerDerivativeRow D 0 3 9 a).1,
   (integerDerivativeRow D 9 0 9 a).2
      - 3 * (integerDerivativeRow D 6 1 9 a).2
      + 3 * (integerDerivativeRow D 3 2 9 a).2
      - (integerDerivativeRow D 0 3 9 a).2)

/-- The original rectangular 10x10 basis assigns this row k=3. -/
theorem originalP3Nine_basis_weight :
    rectangularBasisExponent 10 10 3 (⟨90, by decide⟩ : Fin 100) = 3 := by
  decide

/-- Ordinary ninth derivative of this binomial row at EVERY original
pair sample is exactly 9!, including the imaginary coordinate zero. -/
theorem originalP3NineJet_exact (D : Nat) (a : Int × Int) :
    originalP3NineJet D a = (362880, 0) := by
  norm_num [originalP3NineJet, integerDerivativeRow,
    pairScale, pairMul, pairPow]

/-- The old factor is p^k=27; the normalized original ninth
ordinary derivative has precisely ONE ADDITIONAL 3-adic factor.
No factorial has been added twice. -/
theorem originalP3NineJet_depth_sharp (D : Nat) (a : Int × Int) :
    originalP3NineJet D a = pairScale 27 (13440, 0) ∧
    (3 : Int) ∣ (13440 : Int) ∧ ¬ (9 : Int) ∣ (13440 : Int) := by
  rw [originalP3NineJet_exact]
  norm_num [pairScale]

end TenthDiscriminant.Phase210SharpOrdinaryJet

#print axioms TenthDiscriminant.Phase210SharpOrdinaryJet.originalP3NineJet_exact
#print axioms TenthDiscriminant.Phase210SharpOrdinaryJet.originalP3NineJet_depth_sharp
