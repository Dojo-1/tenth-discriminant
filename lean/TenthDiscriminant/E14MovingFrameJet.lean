import TenthDiscriminant.IntegerTraceGram
import Mathlib.Algebra.Polynomial.Taylor

/-!
# E14: transport every original ordinary-Z jet across a moving frame

Moving chart: U=Z, V=W-Z. To hold W fixed when Z moves by T, the
chart path is (U+T,V-T), not (U+T,V). The transported polynomial is
certified coefficient-by-coefficient, then linked to integerDerivativeRow
from the original source. Hasse coefficients are multiplied by j!, so
the resulting jet is the ORIGINAL ordinary derivative, not a replacement.
-/
namespace TenthDiscriminant.E14

open Polynomial
open scoped ComplexConjugate
noncomputable section

/-- Source polynomial in Z, with W a frozen coefficient. -/
def frozenWPolynomial (w : Complex) (r s : Nat) : Polynomial Complex :=
  X ^ r * C (w ^ s)

/-- The original source monomial in the moving chart, displaced along
the fixed-W direction (U,V) -> (U+T,V-T). -/
def movingFramePath (u v : Complex) (r s : Nat) : Polynomial Complex :=
  (X + C u) ^ r *
    (((X + C u) + (C v - X)) ^ s)

private theorem frame_cancel (u v : Complex) :
    ((X + C u) + (C v - X) : Polynomial Complex) = C (u + v) := by
  simp only [map_add]
  ring

theorem movingFramePath_closed (u v : Complex) (r s : Nat) :
    movingFramePath u v r s =
      (X + C u) ^ r * C ((u + v) ^ s) := by
  unfold movingFramePath
  rw [frame_cancel]
  simp only [map_pow]

/-- Stronger than checking finitely many derivative orders: the complete
source Taylor polynomial is preserved by the transported path. -/
theorem movingFramePath_eq_taylor (u v : Complex) (r s : Nat) :
    movingFramePath u v r s =
      Polynomial.taylor u (frozenWPolynomial (u + v) r s) := by
  rw [movingFramePath_closed]
  simp [frozenWPolynomial, Polynomial.taylor_apply]

/-- Closed formula for the j-th Taylor coefficient of the moving path. -/
theorem movingFramePath_coeff (u v : Complex) (r s j : Nat) :
    (movingFramePath u v r s).coeff j =
      (r.choose j : Complex) * u ^ (r - j) * (u + v) ^ s := by
  rw [movingFramePath_closed]
  simp only [coeff_mul_C, coeff_X_add_C_pow]
  ring

/-- Every factorial-corrected jet is EXACTLY the original integer
ordinary-Z derivative row, evaluated in the quadratic complex chart.
No Hasse derivative is substituted for an ordinary derivative. -/
theorem movingFramePath_original_ordinary_jet
    (D r s j : Nat) (q : Int × Int) :
    (j.factorial : Complex) *
        (movingFramePath (pairEval D q)
          (conj (pairEval D q) - pairEval D q) r s).coeff j =
      pairEval D (integerDerivativeRow D r s j q) := by
  rw [movingFramePath_coeff]
  have hshift :
      pairEval D q + (conj (pairEval D q) - pairEval D q) =
        conj (pairEval D q) := by ring
  rw [hshift, integerDerivativeRow_eval]
  by_cases hj : j ≤ r
  · simp only [derivativeRow, if_pos hj, Nat.descFactorial_eq_factorial_mul_choose]
    push_cast
    ring
  · have hlt : r < j := by omega
    simp [derivativeRow, hj, Nat.choose_eq_zero_of_lt hlt]


/-- Integer coordinates induced by (Re U, Im V / sqrt D) on the
original conjugate lattice, where V = W - Z. -/
def frameIntegralCoordinates (q : Int × Int) : Int × Int :=
  (q.1, -2 * q.2)

theorem frameIntegralCoordinates_injective :
    Function.Injective frameIntegralCoordinates := by
  intro a b h
  apply Prod.ext
  · have hh : (frameIntegralCoordinates a).1 = (frameIntegralCoordinates b).1 :=
      congrArg (fun p : Int × Int => p.1) h
    simpa [frameIntegralCoordinates] using hh
  · have hh := congrArg Prod.snd h
    dsimp [frameIntegralCoordinates] at hh
    omega

/-- Exact image of the integer chart: the second component is even. -/
theorem frameIntegralCoordinates_range (p : Int × Int) :
    (∃ q, frameIntegralCoordinates q = p) ↔
      (∃ k : Int, p.2 = 2 * k) := by
  constructor
  · rintro ⟨q, hq⟩
    refine ⟨-q.2, ?_⟩
    have hh := congrArg Prod.snd hq
    dsimp [frameIntegralCoordinates] at hh
    omega
  · rintro ⟨k, hk⟩
    refine ⟨(p.1, -k), ?_⟩
    apply Prod.ext
    · rfl
    · dsimp [frameIntegralCoordinates]
      omega

/-- An unrestricted new Z x Z coordinate lattice would add spurious nodes. -/
theorem frameIntegralCoordinates_not_surjective :
    ¬ Function.Surjective frameIntegralCoordinates := by
  intro h
  obtain ⟨q, hq⟩ := h (0, 1)
  have hh := congrArg Prod.snd hq
  dsimp [frameIntegralCoordinates] at hh
  omega

/-- The ORIGINAL 2 and 2D integer trace weights, transported to the
index-two chart without illicit division or changed valuations. -/
theorem frame_pair_trace_metric (D : Nat) (p q : Int × Int) :
    4 * integerPairTrace D p q =
      8 * p.1 * q.1 +
        2 * (D : Int) *
          (frameIntegralCoordinates p).2 * (frameIntegralCoordinates q).2 := by
  simp only [integerPairTrace, frameIntegralCoordinates]
  ring

end
end TenthDiscriminant.E14

#print axioms TenthDiscriminant.E14.movingFramePath_eq_taylor
#print axioms TenthDiscriminant.E14.movingFramePath_coeff
#print axioms TenthDiscriminant.E14.movingFramePath_original_ordinary_jet
#print axioms TenthDiscriminant.E14.frameIntegralCoordinates_range
#print axioms TenthDiscriminant.E14.frame_pair_trace_metric
