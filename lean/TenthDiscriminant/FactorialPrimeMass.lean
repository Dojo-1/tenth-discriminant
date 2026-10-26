import TenthDiscriminant.EllipseUpperCount
import TenthDiscriminant.FloorSum

/-!
# The finite factorial mass behind Ender's prime estimate

Factorial prime factorization and Legendre's formula give an exact finite
identity. Prime two belongs to this identity; its later removal from the
determinant lower bound requires the explicit subtraction in Ender's estimate.
-/

namespace TenthDiscriminant
set_option autoImplicit false
noncomputable section

def factorialMass (R : Nat) : Real :=
  ∑ r ∈ Finset.range R, Real.log (r.factorial : Real)

def factorialProduct (R : Nat) : Nat :=
  ∏ r ∈ Finset.range R, r.factorial

def factorialPrimesBelow (R : Nat) : Finset Nat :=
  (Finset.range R).filter Nat.Prime

def factorialPowerSum (R p : Nat) : Nat :=
  ∑ j ∈ (Finset.Ico 1 R).filter (fun j => p ^ j < R), floorSum R (p ^ j)

theorem factorialMass_eq_log_product (R : Nat) :
    factorialMass R = Real.log (factorialProduct R : Real) := by
  unfold factorialMass factorialProduct
  rw [Nat.cast_prod, Real.log_prod]
  intro r hr
  exact_mod_cast Nat.factorial_ne_zero r

/-- A prime appearing in any row factorial is already below the common
row bound, so extending its finite factorization support adds only zeros. -/
theorem factorial_support_subset_primesBelow (r R : Nat) (hr : r < R) :
    (r.factorial.factorization).support ⊆ factorialPrimesBelow R := by
  intro p hp
  have hp' := Nat.mem_primeFactors.mp hp
  exact Finset.mem_filter.mpr ⟨Finset.mem_range.mpr
    (lt_of_le_of_lt (hp'.1.dvd_factorial.mp hp'.2.1) hr), hp'.1⟩

theorem log_factorial_eq_legendre (r R : Nat) (hr : r < R) :
    Real.log (r.factorial : Real) =
      ∑ p ∈ factorialPrimesBelow R,
        (((∑ j ∈ Finset.Ico 1 R, r / p ^ j : Nat) : Real) * Real.log (p : Real)) := by
  have hlog : Real.log (r.factorial : Real) =
      ∑ p ∈ factorialPrimesBelow R,
        ((r.factorial.factorization p : Real) * Real.log (p : Real)) := by
    rw [Real.log_nat_eq_sum_factorization]
    exact Finsupp.sum_of_support_subset _
      (factorial_support_subset_primesBelow r R hr) _ (fun _ _ => by simp)
  rw [hlog]
  apply Finset.sum_congr rfl
  intro p hp
  have hprime := (Finset.mem_filter.mp hp).2
  letI : Fact p.Prime := ⟨hprime⟩
  rw [Nat.factorization_def _ hprime,
    padicValNat_factorial ((Nat.log_le_self p r).trans_lt hr)]

theorem floorSum_eq_zero_of_le (R q : Nat) (hRq : R ≤ q) : floorSum R q = 0 := by
  unfold floorSum
  apply Finset.sum_eq_zero
  intro r hr
  exact Nat.div_eq_of_lt (lt_of_lt_of_le (Finset.mem_range.mp hr) hRq)

theorem factorialPowerSum_eq_unfiltered (R p : Nat) :
    factorialPowerSum R p = ∑ j ∈ Finset.Ico 1 R, floorSum R (p ^ j) := by
  unfold factorialPowerSum
  apply Finset.sum_subset (Finset.filter_subset _ _)
  intro j hj hjnot
  have hpow : R ≤ p ^ j := by
    by_contra h
    exact hjnot (Finset.mem_filter.mpr ⟨hj, by omega⟩)
  exact floorSum_eq_zero_of_le R (p ^ j) hpow

/-- Ender's exact factorial/Legendre identity, with explicit finite
prime and prime-power ranges and the same production floor sum. -/
theorem factorialMass_eq_prime_power_sum (R : Nat) :
    factorialMass R = ∑ p ∈ factorialPrimesBelow R,
      ((factorialPowerSum R p : Real) * Real.log (p : Real)) := by
  unfold factorialMass
  calc
    _ = ∑ r ∈ Finset.range R, ∑ p ∈ factorialPrimesBelow R,
        (((∑ j ∈ Finset.Ico 1 R, r / p ^ j : Nat) : Real) *
          Real.log (p : Real)) := by
      apply Finset.sum_congr rfl
      intro r hr
      exact log_factorial_eq_legendre r R (Finset.mem_range.mp hr)
    _ = ∑ p ∈ factorialPrimesBelow R, ∑ r ∈ Finset.range R,
        (((∑ j ∈ Finset.Ico 1 R, r / p ^ j : Nat) : Real) *
          Real.log (p : Real)) := by rw [Finset.sum_comm]
    _ = _ := by
      apply Finset.sum_congr rfl
      intro p hp
      rw [← Finset.sum_mul, factorialPowerSum_eq_unfiltered]
      congr 1
      have hnat : (∑ r ∈ Finset.range R, ∑ j ∈ Finset.Ico 1 R, r / p ^ j) =
          ∑ j ∈ Finset.Ico 1 R, floorSum R (p ^ j) := by
        rw [Finset.sum_comm]
        rfl
      exact_mod_cast hnat

def factorialEnvelope (x : Real) : Real := x * Real.log x - x + 1

/-- The elementary row-factorial lower bound, with its positive-index
guard. Induction uses `log(1+1/n) <= 1/n`. -/
theorem factorialEnvelope_le_log_factorial (n : Nat) (hn : 1 ≤ n) :
    factorialEnvelope (n : Real) ≤ Real.log (n.factorial : Real) := by
  induction n with
  | zero => omega
  | succ n ih =>
    by_cases hnzero : n = 0
    · subst n
      norm_num [factorialEnvelope]
    have hnpos : (0 : Real) < n := by exact_mod_cast Nat.pos_of_ne_zero hnzero
    have hi := ih (by omega)
    have hlog := Real.log_le_sub_one_of_pos
      (by positivity : (0 : Real) < ((n : Real) + 1) / n)
    have hmul := mul_le_mul_of_nonneg_left hlog hnpos.le
    have hratio : (n : Real) * (((n : Real) + 1) / n - 1) = 1 := by
      field_simp
    rw [hratio, Real.log_div (by positivity) (ne_of_gt hnpos)] at hmul
    rw [Nat.factorial_succ, Nat.cast_mul,
      Real.log_mul (by positivity) (by positivity)]
    unfold factorialEnvelope at hi ⊢
    push_cast
    nlinarith

theorem factorialEnvelope_hasDerivAt (x : Real) (hx : 0 < x) :
    HasDerivAt factorialEnvelope (Real.log x) x := by
  have h := ((Real.hasDerivAt_mul_log (ne_of_gt hx)).sub (hasDerivAt_id x)).add_const 1
  simpa only [factorialEnvelope, add_sub_cancel_right] using h

theorem factorialEnvelope_monotoneOn : MonotoneOn factorialEnvelope (Set.Ici 1) := by
  apply monotoneOn_of_hasDerivWithinAt_nonneg (convex_Ici 1)
  · exact ((Real.continuous_mul_log.sub continuous_id).add continuous_const).continuousOn
  · intro x hx
    have hxone : (1 : Real) ≤ x := interior_subset hx
    exact (factorialEnvelope_hasDerivAt x (by linarith)).hasDerivWithinAt
  · intro x hx
    have hxone : (1 : Real) ≤ x := interior_subset hx
    exact Real.log_nonneg hxone

def factorialEnvelopePrimitive (x : Real) : Real :=
  x ^ 2 / 2 * Real.log x - 3 * x ^ 2 / 4 + x

theorem factorialEnvelopePrimitive_hasDerivAt (x : Real) (hx : 0 < x) :
    HasDerivAt factorialEnvelopePrimitive (factorialEnvelope x) x := by
  have hp := (hasDerivAt_id x).pow 2
  have h := (((hp.div_const 2).mul (Real.hasDerivAt_log (ne_of_gt hx))).sub
    ((hp.const_mul 3).div_const 4)).add (hasDerivAt_id x)
  convert h using 1
  unfold factorialEnvelope
  simp only [pow_one, mul_one]
  field_simp
  ring

theorem integral_factorialEnvelope (N : Real) (hN : 1 ≤ N) :
    (∫ x in (1 : Real)..N, factorialEnvelope x) =
      N ^ 2 / 2 * Real.log N - 3 * N ^ 2 / 4 + N - 1 / 4 := by
  have hint : IntervalIntegrable factorialEnvelope MeasureTheory.volume 1 N :=
    ((Real.continuous_mul_log.sub continuous_id).add continuous_const).intervalIntegrable 1 N
  have hderiv : ∀ x ∈ Set.uIcc (1 : Real) N,
      HasDerivAt factorialEnvelopePrimitive (factorialEnvelope x) x := by
    intro x hx
    rw [Set.uIcc_of_le hN] at hx
    exact factorialEnvelopePrimitive_hasDerivAt x (by linarith [hx.1])
  rw [intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv hint]
  norm_num [factorialEnvelopePrimitive]

theorem integral_factorialEnvelope_le_mass (R : Nat) (hR : 2 ≤ R) :
    (∫ x in (1 : Real)..((R - 1 : Nat) : Real), factorialEnvelope x) ≤
      factorialMass R := by
  have hN : 1 ≤ R - 1 := by omega
  have hmono : MonotoneOn factorialEnvelope
      (Set.Icc (1 : Real) ((R - 1 : Nat) : Real)) :=
    factorialEnvelope_monotoneOn.mono (fun _ hx => hx.1)
  have hsum := MonotoneOn.integral_le_sum_Ico (f := factorialEnvelope) hN
    (by simpa only [Nat.cast_one] using hmono)
  have hshift := Finset.sum_Ico_add'
    (fun k : Nat => factorialEnvelope (k : Real)) 1 (R - 1) 1
  have hRsub : R - 1 + 1 = R := by omega
  simp only [Nat.reduceAdd, hRsub] at hshift
  rw [hshift] at hsum
  have hrows : (∑ r ∈ Finset.Ico 2 R, factorialEnvelope (r : Real)) ≤
      ∑ r ∈ Finset.Ico 2 R, Real.log (r.factorial : Real) := by
    apply Finset.sum_le_sum
    intro r hr
    exact factorialEnvelope_le_log_factorial r (by have h := (Finset.mem_Ico.mp hr).1; omega)
  have hsubset : Finset.Ico 2 R ⊆ Finset.range R := by
    intro r hr
    exact Finset.mem_range.mpr (Finset.mem_Ico.mp hr).2
  have hfull : (∑ r ∈ Finset.Ico 2 R, Real.log (r.factorial : Real)) ≤
      factorialMass R := by
    apply Finset.sum_le_sum_of_subset_of_nonneg hsubset
    intro r hr hrnot
    apply Real.log_nonneg
    exact_mod_cast (show 1 ≤ r.factorial from Nat.factorial_pos r)
  simpa only [Nat.cast_one] using hsum.trans (hrows.trans hfull)

/-- The unchanged expression evaluated by `tools/ender.py:factorial_lower`.
The application domain `R>=2` keeps `N=R-1` positive. -/
def factorialLower (R : Nat) : Real :=
  let N : Real := ((R - 1 : Nat) : Real)
  N ^ 2 / 2 * Real.log N - 3 * N ^ 2 / 4 + N / 2 + 1 / 4

theorem factorialLower_le_mass (R : Nat) (hR : 2 ≤ R) :
    factorialLower R ≤ factorialMass R := by
  have hN : (1 : Real) ≤ ((R - 1 : Nat) : Real) := by
    exact_mod_cast (by omega : 1 ≤ R - 1)
  have hi := integral_factorialEnvelope_le_mass R hR
  rw [integral_factorialEnvelope _ hN] at hi
  dsimp [factorialLower]
  linarith

/-- The production scalar lower bound now lies below the exact finite
prime-power floor sum. Tail removal is a later theorem. -/
theorem factorialLower_le_prime_power_sum (R : Nat) (hR : 2 ≤ R) :
    factorialLower R ≤ ∑ p ∈ factorialPrimesBelow R,
      ((factorialPowerSum R p : Real) * Real.log (p : Real)) := by
  rw [← factorialMass_eq_prime_power_sum R]
  exact factorialLower_le_mass R hR

theorem factorialMass_zero_control : factorialMass 0 = 0 := by
  simp [factorialMass]

theorem factorialMass_one_control : factorialMass 1 = 0 := by
  norm_num [factorialMass, Finset.sum_range_succ]

theorem factorialMass_two_control : factorialMass 2 = 0 := by
  norm_num [factorialMass, Finset.sum_range_succ]

theorem factorialLower_two_equality_control : factorialLower 2 = factorialMass 2 := by
  norm_num [factorialLower, factorialMass, Finset.sum_range_succ]

theorem factorialProduct_five_control : factorialProduct 5 = 288 := by decide

theorem factorialPowerSum_five_control :
    factorialPowerSum 5 2 = 5 ∧ factorialPowerSum 5 3 = 2 := by decide

/-- Removing two belongs to the later determinant estimate, not to
Legendre's factorial identity. Already `H(3)=log 2>0` detects the error. -/
theorem factorialMass_omit_two_false :
    factorialMass 3 ≠ ∑ p ∈ oddPrimesBelow 3,
      ((factorialPowerSum 3 p : Real) * Real.log (p : Real)) := by
  have hempty : oddPrimesBelow 3 = ∅ := by decide
  rw [hempty, Finset.sum_empty]
  have hmass : factorialMass 3 = Real.log 2 := by
    norm_num [factorialMass, Finset.sum_range_succ]
  rw [hmass]
  exact ne_of_gt (Real.log_pos (by norm_num))

/-- A composite index is not a prime factorization coordinate even when
its floor sum is positive. -/
theorem factorial_composite_index_control :
    (factorialProduct 5).factorization 4 = 0 ∧ floorSum 5 4 = 1 := by
  constructor
  · exact Nat.factorization_eq_zero_of_non_prime _ (by decide)
  · decide

theorem factorial_power_at_cutoff_control (R : Nat) : floorSum R R = 0 :=
  floorSum_eq_zero_of_le R R le_rfl

theorem factorialLower_without_R_guard_false :
    ¬ factorialLower 1 ≤ factorialMass 1 := by
  norm_num [factorialLower, factorialMass, Finset.sum_range_succ]

end
end TenthDiscriminant
