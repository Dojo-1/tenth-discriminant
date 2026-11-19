import TenthDiscriminant.E37GeneralIntegralGramCertificate

/-!
# E40 — Three-row exact ordinary-jet clock controls at one original source

The SAME original Q={(1,0),(6,0),(11,0)}, D=25, R=3,S=1,
is observed at J=1,2,3 ordinary Z-derivative depths. Its integer
rectangular trace Grams differ because THE ACTUAL SOURCE J CLOCK
differs; no source points, conjugate convention or trace metric change.

The binomial integer U for the polynomial basis (1,Z-1,(Z-1)^2)
is unimodular. With this same U the original Gram factors are:
  J=1: diag(1,5,25) * H1 * diag(1,5,25), detG=500000, v5=6;
  J=2: diag(1,1,5) * H2 * diag(1,1,5), detG=784400, v5=2;
  J=3: detG=799664, v5=0.
These are exact fixed finite checks, NOT a universal n,J
Vandermonde theorem, new 307^4 bound, or hardness result.
-/

namespace TenthDiscriminant.E40
set_option autoImplicit false
noncomputable section

def clockSource : Finset (Int × Int) := {(1,0),(6,0),(11,0)}
def clockFrame : Matrix (Fin 3) (Fin 3) Int :=
  !![1,0,0;-1,1,0;1,-2,1]

theorem clock_frame_unimodular :
    E37.IntegerUnimodular clockFrame := by
  left
  decide

theorem clock_J1_original_gram :
    integerRectangularTraceGram clockSource 25 1 3 1 =
      !![6,36,316;36,316,3096;316,3096,31876] := by
  decide

theorem clock_J2_original_gram :
    integerRectangularTraceGram clockSource 25 2 3 1 =
      !![6,36,316;36,322,3168;316,3168,33140] := by
  decide

theorem clock_J3_original_gram :
    integerRectangularTraceGram clockSource 25 3 3 1 =
      !![6,36,316;36,322,3168;316,3168,33164] := by
  decide

theorem clock_J1_original_det :
    (integerRectangularTraceGram clockSource 25 1 3 1).det =
      (500000 : Int) := by
  rw [clock_J1_original_gram]
  decide

theorem clock_J2_original_det :
    (integerRectangularTraceGram clockSource 25 2 3 1).det =
      (784400 : Int) := by
  rw [clock_J2_original_gram]
  decide

theorem clock_J3_original_det :
    (integerRectangularTraceGram clockSource 25 3 3 1).det =
      (799664 : Int) := by
  rw [clock_J3_original_gram]
  decide

def d1 : Fin 3 → Int := fun i => if i = 0 then 1 else if i = 1 then 5 else 25
def d2 : Fin 3 → Int := fun i => if i = 0 then 1 else if i = 1 then 1 else 5
def H1 : Matrix (Fin 3) (Fin 3) Int :=
  !![6,6,10;6,10,18;10,18,34]
def H2 : Matrix (Fin 3) (Fin 3) Int :=
  !![6,30,50;30,256,462;50,462,890]

/-- The COMPLETE original sampled J=1 Gram, no selected minor or
modified derivative, has a certified integral factorization. -/
theorem clock_J1_original_factorization :
    clockFrame *
      integerRectangularTraceGram clockSource 25 1 3 1 *
      clockFrame.transpose = Matrix.diagonal d1 * H1 *
      Matrix.diagonal d1 := by
  rw [clock_J1_original_gram]
  decide

/-- At derivative depth J=2 the factor grade decreases because the
additional original ordinary derivative carries less p-divisibility. -/
theorem clock_J2_original_factorization :
    clockFrame *
      integerRectangularTraceGram clockSource 25 2 3 1 *
      clockFrame.transpose = Matrix.diagonal d2 * H2 *
      Matrix.diagonal d2 := by
  rw [clock_J2_original_gram]
  decide

/-- Explicitly instantiate E37 arbitrary-rank theorem, rather
than merely numerically checking two three-by-three determinants. -/
theorem clock_J1_generic_factor :
    ((∏ i : Fin 3, d1 i)^2) ∣
      (integerRectangularTraceGram clockSource 25 1 3 1).det := by
  exact E37.original_full_gram_factor clockSource 25 1 3 1
    clockFrame H1 d1 clock_frame_unimodular
    clock_J1_original_factorization

theorem clock_J2_generic_factor :
    ((∏ i : Fin 3, d2 i)^2) ∣
      (integerRectangularTraceGram clockSource 25 2 3 1).det := by
  exact E37.original_full_gram_factor clockSource 25 2 3 1
    clockFrame H2 d2 clock_frame_unimodular
    clock_J2_original_factorization

/-- Exact finite p-adic grades of the ORIGINAL determinants.
They are stronger than the generic lower bound alone in that
the next power provably does not divide each determinant. -/
theorem clock_J1_exact_power :
    ((5 : Int)^6 ∣
      (integerRectangularTraceGram clockSource 25 1 3 1).det) ∧
    ¬ ((5 : Int)^7 ∣
      (integerRectangularTraceGram clockSource 25 1 3 1).det) := by
  rw [clock_J1_original_det]
  decide

theorem clock_J2_exact_power :
    ((5 : Int)^2 ∣
      (integerRectangularTraceGram clockSource 25 2 3 1).det) ∧
    ¬ ((5 : Int)^3 ∣
      (integerRectangularTraceGram clockSource 25 2 3 1).det) := by
  rw [clock_J2_original_det]
  decide

theorem clock_J3_no_five_factor :
    ¬ (5 : Int) ∣
      (integerRectangularTraceGram clockSource 25 3 3 1).det := by
  rw [clock_J3_original_det]
  decide

/-- Fixed sample support and positive trace, with different actual
derivative clocks. This is a finite typed arithmetic contrast. -/
theorem same_source_three_clock_profiles :
    ((5 : Int)^6 ∣
      (integerRectangularTraceGram clockSource 25 1 3 1).det) ∧
    ((5 : Int)^2 ∣
      (integerRectangularTraceGram clockSource 25 2 3 1).det) ∧
    (¬ (5 : Int) ∣
      (integerRectangularTraceGram clockSource 25 3 3 1).det) := by
  exact ⟨clock_J1_exact_power.1, clock_J2_exact_power.1,
    clock_J3_no_five_factor⟩

end
end TenthDiscriminant.E40

#print axioms TenthDiscriminant.E40.clock_frame_unimodular
#print axioms TenthDiscriminant.E40.clock_J1_original_factorization
#print axioms TenthDiscriminant.E40.clock_J2_original_factorization
#print axioms TenthDiscriminant.E40.clock_J1_generic_factor
#print axioms TenthDiscriminant.E40.clock_J2_generic_factor
#print axioms TenthDiscriminant.E40.same_source_three_clock_profiles
