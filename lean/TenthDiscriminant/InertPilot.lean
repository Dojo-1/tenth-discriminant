import TenthDiscriminant.IntegerTraceGram
import TenthDiscriminant.GramDivisibility

/-!
# An odd-inert-prime pilot for the actual integer trace-Gram matrix

This fixed `D = 19`, `p = 3`, `R = 4`, `S = 2` calculation tests the
local derivative-row mechanism. It is not Ender's general valuation theorem.
-/
namespace TenthDiscriminant

private theorem cube_sub_self_dvd_three (x : Int) : (3 : Int) ∣ x ^ 3 - x := by
  have h : ∀ z : ZMod 3, z ^ 3 = z := by decide
  apply (ZMod.intCast_zmod_eq_zero_iff_dvd (x ^ 3 - x) 3).mp
  simp [h]

/-- The transformed row `Z^3-W` at a selected lattice point, derivative in `Z`. -/
def inertPilotJet (p : Int × Int) (j : Nat) : Int × Int :=
  ((integerDerivativeRow 19 3 0 j p).1 - (integerDerivativeRow 19 0 1 j p).1,
   (integerDerivativeRow 19 3 0 j p).2 - (integerDerivativeRow 19 0 1 j p).2)

private theorem inertPilotJet_zero (x y : Int) :
    inertPilotJet (x, y) 0 =
      (x ^ 3 - x - 57 * x * y ^ 2, 3 * x ^ 2 * y - 19 * y ^ 3 + y) := by
  simp [inertPilotJet, integerDerivativeRow, pairScale, pairMul, pairPow,
    pairConj, Nat.descFactorial]
  ring_nf
  tauto

/-- Every ordinary `Z`-derivative of `Z^3-W`, evaluated at `W=conj z`, is
three-divisible in both selected integer coordinates. -/
theorem inertPilotJet_dvd_three (p : Int × Int) (j : Nat) :
    (3 : Int) ∣ (inertPilotJet p j).1 ∧
      (3 : Int) ∣ (inertPilotJet p j).2 := by
  rcases p with ⟨x, y⟩
  by_cases h0 : j = 0
  · subst j
    rw [inertPilotJet_zero]
    have hx := cube_sub_self_dvd_three x
    have hy := cube_sub_self_dvd_three y
    constructor
    · have h57 : (3 : Int) ∣ 57 * x * y ^ 2 := by
        apply dvd_mul_of_dvd_left
        · apply dvd_mul_of_dvd_left
          norm_num
      convert dvd_sub hx h57 using 1
    · have h18 : (3 : Int) ∣ 18 * y ^ 3 := by
        apply dvd_mul_of_dvd_left
        norm_num
      have h19 : (3 : Int) ∣ 19 * y ^ 3 - y := by
        convert dvd_add h18 hy using 1
        ring
      have hfirst : (3 : Int) ∣ 3 * x ^ 2 * y := ⟨x ^ 2 * y, by ring⟩
      convert dvd_sub hfirst h19 using 1
      ring
  · have hcases : j = 1 ∨ j = 2 ∨ j = 3 ∨ 3 < j := by omega
    rcases hcases with h1 | h2 | h3 | h4
    · subst j
      simp [inertPilotJet, integerDerivativeRow, pairScale, pairMul, pairPow,
        pairConj, Nat.descFactorial]
    · subst j
      simp [inertPilotJet, integerDerivativeRow, pairScale, pairMul, pairPow,
        pairConj, Nat.descFactorial]
      constructor
      · exact ⟨2 * x, by ring⟩
      · exact ⟨2 * y, by ring⟩
    · subst j
      simp [inertPilotJet, integerDerivativeRow, pairScale, pairMul, pairPow,
        pairConj, Nat.descFactorial]
    · have h3 : ¬ j ≤ 3 := by omega
      have h0' : ¬ j ≤ 0 := by omega
      simp [inertPilotJet, integerDerivativeRow, h3, h0']

/-- The unique quotient of the three-divisible transformed jet. -/
noncomputable def inertPilotJetQuot (p : Int × Int) (j : Nat) : Int × Int :=
  (Classical.choose (inertPilotJet_dvd_three p j).1,
   Classical.choose (inertPilotJet_dvd_three p j).2)

theorem inertPilotJet_scale (p : Int × Int) (j : Nat) :
    inertPilotJet p j = pairScale 3 (inertPilotJetQuot p j) := by
  apply Prod.ext
  · exact Classical.choose_spec (inertPilotJet_dvd_three p j).1
  · exact Classical.choose_spec (inertPilotJet_dvd_three p j).2

/-- Canonical row-major jet labels for the fixed `4 × 2` rectangle. -/
def inertPilotRow (i : Fin 8) (p : Int × Int) (j : Nat) : Int × Int :=
  integerDerivativeRow 19 (i.val / 2) (i.val % 2) j p

theorem inertPilotRow_six (p : Int × Int) (j : Nat) :
    inertPilotRow 6 p j = integerDerivativeRow 19 3 0 j p := by
  rfl

theorem inertPilotRow_one (p : Int × Int) (j : Nat) :
    inertPilotRow 1 p j = integerDerivativeRow 19 0 1 j p := by
  rfl

/-- The selected shear is exactly the difference of canonical rows 6 and 1. -/
theorem inertPilotJet_eq_row_difference (p : Int × Int) (j : Nat) :
    inertPilotJet p j =
      ((inertPilotRow 6 p j).1 - (inertPilotRow 1 p j).1,
       (inertPilotRow 6 p j).2 - (inertPilotRow 1 p j).2) := by
  rfl

private theorem integerPairTrace_scale_two (D : Nat) (c d : Int)
    (a b : Int × Int) :
    integerPairTrace D (pairScale c a) (pairScale d b) =
      c * d * integerPairTrace D a b := by
  simp [integerPairTrace, pairScale]
  ring

/-- A Gram assembly over the *original* finite set of selected pairs. -/
def inertPilotGram (Q : Finset (Int × Int)) (J : Nat)
    (V : Fin 8 → Int × Int → Nat → Int × Int) : Matrix (Fin 8) (Fin 8) Int :=
  fun a b => (Finset.range J).sum (fun j =>
    Q.sum (fun p => integerPairTrace 19 (V a p j) (V b p j)))

theorem inertPilotGram_canonical (Q : Finset (Int × Int)) (J : Nat) :
    inertPilotGram Q J inertPilotRow = integerRectangularTraceGram Q 19 J 4 2 := by
  rfl

/-- At zero-based index 6, subtract row 1 (`W`) from row 6 (`Z³`). -/
def inertPilotShearedRow (i : Fin 8) (p : Int × Int) (j : Nat) : Int × Int :=
  if i = 6 then inertPilotJet p j else inertPilotRow i p j

/-- Divide the sheared jet in the selected row by three. -/
noncomputable def inertPilotNormalizedRow (i : Fin 8) (p : Int × Int)
    (j : Nat) : Int × Int :=
  if i = 6 then inertPilotJetQuot p j else inertPilotRow i p j

theorem inertPilotShearedRow_scale (i : Fin 8) (p : Int × Int) (j : Nat) :
    inertPilotShearedRow i p j =
      pairScale (pivotScale (6 : Fin 8) 3 i) (inertPilotNormalizedRow i p j) := by
  by_cases hi : i = 6
  · subst i
    simp only [inertPilotShearedRow, inertPilotNormalizedRow, pivotScale, if_true]
    exact inertPilotJet_scale p j
  · simp [inertPilotShearedRow, inertPilotNormalizedRow, pivotScale, hi, pairScale]

private theorem inertPilotGram_scale (Q : Finset (Int × Int)) (J : Nat)
    (V W : Fin 8 → Int × Int → Nat → Int × Int) (d : Fin 8 → Int)
    (h : ∀ i p j, V i p j = pairScale (d i) (W i p j)) :
    inertPilotGram Q J V = Matrix.diagonal d * inertPilotGram Q J W * Matrix.diagonal d := by
  ext a b
  simp only [Matrix.mul_diagonal, Matrix.diagonal_mul, inertPilotGram]
  simp_rw [h, integerPairTrace_scale_two]
  simp [Finset.mul_sum, Finset.sum_mul]
  ring

private theorem inertPilotShear_entry (A : Matrix (Fin 8) (Fin 8) Int)
    (a b : Fin 8) :
    gramShear A 6 1 (-1) a b =
      A a b - (if a = 6 then A 1 b else 0) -
        (if b = 6 then A a 1 else 0) +
        (if a = 6 ∧ b = 6 then A 1 1 else 0) := by
  classical
  by_cases ha : a = 6 <;> by_cases hb : b = 6 <;>
    simp [gramShear, Matrix.updateCol_apply, Matrix.updateRow_apply, ha, hb]
    <;> ring

private theorem inertPilotTrace_diff_left (p : Int × Int) (j : Nat)
    (v : Int × Int) :
    integerPairTrace 19 (inertPilotJet p j) v =
      integerPairTrace 19 (inertPilotRow 6 p j) v -
        integerPairTrace 19 (inertPilotRow 1 p j) v := by
  rw [inertPilotJet_eq_row_difference]
  simp [integerPairTrace]
  ring

private theorem inertPilotTrace_diff_right (p : Int × Int) (j : Nat)
    (v : Int × Int) :
    integerPairTrace 19 v (inertPilotJet p j) =
      integerPairTrace 19 v (inertPilotRow 6 p j) -
        integerPairTrace 19 v (inertPilotRow 1 p j) := by
  rw [inertPilotJet_eq_row_difference]
  simp [integerPairTrace]
  ring

theorem inertPilotGram_shear (Q : Finset (Int × Int)) (J : Nat) :
    inertPilotGram Q J inertPilotShearedRow =
      gramShear (integerRectangularTraceGram Q 19 J 4 2) 6 1 (-1) := by
  ext a b
  rw [inertPilotShear_entry]
  by_cases ha : a = 6 <;> by_cases hb : b = 6
  · subst a
    subst b
    simp only [inertPilotGram, inertPilotShearedRow, if_true,
      integerRectangularTraceGram, integerTraceGramMatrix,
      integerTraceGramEntry]
    simp_rw [inertPilotTrace_diff_left, inertPilotTrace_diff_right,
      Finset.sum_sub_distrib]
    simp [inertPilotRow]
    ring
  · subst a
    simp only [inertPilotGram, inertPilotShearedRow, if_true, if_neg hb,
      integerRectangularTraceGram, integerTraceGramMatrix,
      integerTraceGramEntry]
    simp_rw [inertPilotTrace_diff_left, Finset.sum_sub_distrib]
    simp [inertPilotRow, hb]
  · subst b
    simp only [inertPilotGram, inertPilotShearedRow, if_true, if_neg ha,
      integerRectangularTraceGram, integerTraceGramMatrix,
      integerTraceGramEntry]
    simp_rw [inertPilotTrace_diff_right, Finset.sum_sub_distrib]
    simp [inertPilotRow, ha]
  · simp [inertPilotGram, inertPilotShearedRow, ha, hb,
      integerRectangularTraceGram, integerTraceGramMatrix,
      integerTraceGramEntry, inertPilotRow]

/-- The sheared *integer* Gram has one factor of three on each side. -/
theorem inertPilotGram_factor (Q : Finset (Int × Int)) (J : Nat) :
    gramShear (integerRectangularTraceGram Q 19 J 4 2) 6 1 (-1) =
      Matrix.diagonal (pivotScale (6 : Fin 8) 3) *
        inertPilotGram Q J inertPilotNormalizedRow *
          Matrix.diagonal (pivotScale (6 : Fin 8) 3) := by
  rw [← inertPilotGram_shear]
  exact inertPilotGram_scale Q J inertPilotShearedRow inertPilotNormalizedRow
    (pivotScale (6 : Fin 8) 3) inertPilotShearedRow_scale

/-- A genuine fixed-grid divisibility theorem for the *canonical* matrix,
valid for every finite sample set and every derivative cutoff. -/
theorem inertPilot_nine_dvd_det (Q : Finset (Int × Int)) (J : Nat) :
    (9 : Int) ∣ (integerRectangularTraceGram Q 19 J 4 2).det := by
  have hij : (6 : Fin 8) ≠ 1 := by decide
  have h := sq_dvd_det_of_gramShear_factor
    (integerRectangularTraceGram Q 19 J 4 2)
    (inertPilotGram Q J inertPilotNormalizedRow) hij (-1) 3
    (inertPilotGram_factor Q J)
  norm_num at h ⊢
  exact h

/-- The registered ellipse control has enough distinct points for a strictly
positive determinant: the divisibility theorem is not explained by zero. -/
theorem inertPilot_nineteen_five_det_pos :
    0 < (integerRectangularTraceGram (ellipsePairs 19 5) 19 2 4 2).det := by
  exact ellipseIntegerTraceGram_det_pos_of_count 19 5 2 4 2
    (by decide) (by decide) (by decide) (by decide)
    (by norm_num [ellipsePairs_nineteen_five_control])

/-- Inertness matters: at `D=2`, `p=3`, the imaginary coordinate of
`Z³-W` at `Z=√(-2)` equals `-1`, not a multiple of three. -/
theorem inertPilot_noninert_negative_control :
    ¬ (3 : Int) ∣
      ((integerDerivativeRow 2 3 0 0 (0, 1)).2 -
        (integerDerivativeRow 2 0 1 0 (0, 1)).2) := by
  norm_num [integerDerivativeRow, pairScale, pairMul, pairPow, pairConj,
    Nat.descFactorial]

end TenthDiscriminant
