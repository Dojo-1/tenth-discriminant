import TenthDiscriminant.BinaryThinLogBridge
import TenthDiscriminant.OneNodeTraceControls
import TenthDiscriminant.SmallPositiveClassNumber

/-!
# Phase168: a genuinely realizable odd-chart arithmetic witness at D=7

We reuse the repo's existing proof that Q(sqrt(-7)) has class number 1,
transport it through the ACTUAL odd quadratic-field equivalence, and
apply Phase166's arbitrary-original-Q logarithmic theorem to a small,
positive original integer Gram.

Unlike a D>=450^4 class-number-one hypothesis (already excluded by
the current field theorem), these prerequisites really have a model.
No new discriminant cutoff, no new jet normalization or metric.
-/

namespace TenthDiscriminant.SevenActualFieldWitness
open RadialCutoff
set_option autoImplicit false
set_option maxRecDepth 4096
set_option maxHeartbeats 400000

private instance sevenPositive : Fact (0 < (7 : Nat)) := ⟨by decide⟩
private instance sevenOddChart : Fact ((7 : Int) % 4 = 3) := ⟨by norm_num⟩
private instance sevenMaximalFieldFact :
    Fact (0 < 4 * (((7 : Int) + 1) / 4) - 1) := ⟨by norm_num⟩

/-- This is the CORRECT maximal odd chart for D=7, not the smaller
nonmaximal integer order Z[sqrt(-7)]. The field equivalence transports
the already checked class-number-one fact. -/
theorem seven_maximal_odd_chart_class_number_one :
    NumberField.classNumber
      (QuadraticField (((7 : Int) + 1) / 4)) = 1 := by
  letI : Fact ((((7 : Nat) : Int) % 4) = 3) := ⟨by norm_num⟩
  exact classNumber_one_of_field_equiv
    (ImaginaryQuadraticField 7)
    (QuadraticField (((7 : Int) + 1) / 4))
    (quadraticChartEquiv 7)
    seven_classNumber_one

/-- The original one-by-one integer trace Gram of the order-zero
ordinary Z-jet of the constant polynomial is [2], not a replacement
real/Hasse Gram. This explicit positivity is the generic theorem's
separate hypothesis. -/
theorem seven_singleton_source_gram_positive :
    0 < (integerRectangularTraceGram
      ({(0, 0)} : Finset (Int × Int)) 7 1 1 1).det := by
  have hdet :
      (integerRectangularTraceGram
        ({(0, 0)} : Finset (Int × Int)) 7 1 1 1).det = 2 := by
    decide
  omega

/-- A genuine low-D instance of Phase166's arbitrary-Q original-source
theorem: ALL number-field assumptions are now proved, not asserted;
its source integer is positive for the concrete sample. -/
theorem seven_actual_class_one_original_log_bound :
    (binaryNullGramExponent 1 1 : Real) * Real.log 2 +
      exactOddPrimeMass 1 1 ≤
      Real.log ((integerRectangularTraceGram
        ({(0, 0)} : Finset (Int × Int)) 7 1 1 1).det : Real) := by
  have hsq : Squarefree (7 : Nat) :=
    (by norm_num : Nat.Prime 7).squarefree
  have hRcut : (1 : Int) < ((7 : Int) + 1) / 4 := by
    norm_num
  letI : Fact ((((7 : Nat) : Int) % 4) = 3) := ⟨by norm_num⟩
  exact BinaryThinLogBridge.original_binary_and_exact_odd_mass_log_of_pos
    ({(0, 0)} : Finset (Int × Int)) 7 1 1
    hsq seven_maximal_odd_chart_class_number_one
    hRcut seven_singleton_source_gram_positive

/-- An independent direct numeric check: the new low-D arithmetic bound
is exactly tight, log 2 <= log 2, for the constant one-row source. -/
theorem seven_actual_source_log_equality :
    (binaryNullGramExponent 1 1 : Real) * Real.log 2 +
      exactOddPrimeMass 1 1 =
      Real.log ((integerRectangularTraceGram
        ({(0, 0)} : Finset (Int × Int)) 7 1 1 1).det : Real) := by
  have hd :
      (integerRectangularTraceGram
        ({(0, 0)} : Finset (Int × Int)) 7 1 1 1).det = 2 := by
    decide
  have hb : binaryNullGramExponent 1 1 = 1 := by decide
  have hp : oddPrimesBelow 1 = ∅ := by decide
  have hodd : exactOddPrimeMass 1 1 = 0 := by
    simp [exactOddPrimeMass, hp]
  rw [hb, hodd, hd]
  norm_num

end TenthDiscriminant.SevenActualFieldWitness
