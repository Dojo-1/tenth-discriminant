import TenthDiscriminant.LogEnclosure
import TenthDiscriminant.IntegerLogCheck
import TenthDiscriminant.NumericalWeights

/-!
# Sound aggregation of a complete first-interval prime table

Candidate data are untrusted. Coverage and every row must be proved before
these theorems turn the table's integer sums into real inequalities.
-/

namespace TenthDiscriminant.FirstCertificate
set_option autoImplicit false
noncomputable section

structure Row where
  p : Nat
  k : Nat
  lo : Nat
  hi : Nat
  coefficient : Nat
  weight : Nat
deriving DecidableEq, Repr

def scale : Nat := 1000000000000
def primeList : List Nat := (List.range 10001).filter (fun p => decide p.Prime)

def checkRow (r : Row) : Bool := decide (
  2 ≤ r.p ∧ r.coefficient = factorialCoefficient 175000000000 r.p 38 ∧
  (r.p = 2 → r.weight = 0) ∧
  checkIntegerLogBounds r.p 1 r.k r.lo r.hi scale = true ∧
  checkIntegerValuationLower 175000000000 8750000000 r.p r.weight = true)

theorem checkRow_sound (r : Row) (hc : checkRow r = true) :
    r.coefficient = factorialPowerSum 175000000000 r.p ∧
      ((r.lo : Real) / scale ≤ Real.log r.p ∧ Real.log r.p ≤ (r.hi : Real) / scale) ∧
      (r.weight : Real) ≤ valuationWeight 175000000000 8750000000 r.p ∧
      (r.p = 2 → r.weight = 0) := by
  rcases of_decide_eq_true hc with ⟨hp, hcoeff, hzero, hlog, hw⟩
  have hl := checkIntegerLogBounds_sound r.p 1 r.k r.lo r.hi scale hlog
  simp only [Nat.cast_one, div_one] at hl
  exact ⟨hcoeff.trans (first_factorial_coefficient r.p hp).symm, hl,
    checkIntegerValuationLower_sound _ _ _ _ (by decide) (by omega) hw, hzero⟩

theorem primeList_nodup : primeList.Nodup := by
  exact (show (List.range 10001).Nodup from List.nodup_range).filter _

theorem primeList_toFinset : primeList.toFinset = productionSmallPrimes 10000 := by
  ext p
  simp [primeList, productionSmallPrimes]

theorem rows_sum_eq (rows : List Row) (hc : rows.map Row.p = primeList) (f : Nat → Real) :
    (rows.map (fun r => f r.p)).sum = ∑ p ∈ productionSmallPrimes 10000, f p := by
  calc
    _ = ((rows.map Row.p).map f).sum := by simp only [List.map_map]; rfl
    _ = (primeList.map f).sum := by rw [hc]
    _ = _ := by rw [← List.sum_toFinset f primeList_nodup, primeList_toFinset]

theorem list_upper_units (f : Row → Real) (u : Row → Nat) :
    ∀ rows : List Row, (∀ r ∈ rows, f r ≤ (u r : Real) / scale) →
      (rows.map f).sum ≤ ((rows.map u).sum : Nat) / (scale : Real)
  | [], h => by simp
  | r :: rs, h => by
      have hh := h r (by simp)
      have ht := list_upper_units f u rs (fun x hx => h x (by simp [hx]))
      simp only [List.map_cons, List.sum_cons, Nat.cast_add]
      rw [add_div]
      exact add_le_add hh ht

theorem list_lower_units (f : Row → Real) (u : Row → Nat) :
    ∀ rows : List Row, (∀ r ∈ rows, (u r : Real) / scale ≤ f r) →
      ((rows.map u).sum : Nat) / (scale : Real) ≤ (rows.map f).sum
  | [], h => by simp
  | r :: rs, h => by
      have hh := h r (by simp)
      have ht := list_lower_units f u rs (fun x hx => h x (by simp [hx]))
      simp only [List.map_cons, List.sum_cons, Nat.cast_add]
      rw [add_div]
      exact add_le_add hh ht

/-- Validity of the whole table is a hypothesis here; generated JSON or
an evaluated Python comparison does not supply it. -/
theorem table_mass_bounds (rows : List Row)
    (hcover : rows.map Row.p = primeList) (hrows : ∀ r ∈ rows, checkRow r = true) :
    factorialSmallMass 175000000000 10000 ≤
        ((rows.map (fun r => r.coefficient * r.hi)).sum : Nat) / (scale : Real) ∧
      (((rows.map (fun r => r.weight * r.lo)).sum : Nat) : Real) / scale ≤
        smallOddValuationMass 175000000000 8750000000 10000 := by
  constructor
  · rw [factorialSmallMass_eq_padded, ← rows_sum_eq rows hcover]
    apply list_upper_units
    intro r hr
    have hs := checkRow_sound r (hrows r hr)
    rw [← hs.1]
    have h := mul_le_mul_of_nonneg_left hs.2.1.2 (Nat.cast_nonneg r.coefficient)
    simpa only [Nat.cast_mul, mul_div_assoc] using h
  · rw [smallOddValuationMass_eq_padded, Finset.sum_filter, ← rows_sum_eq rows hcover]
    apply list_lower_units
    intro r hr
    have hs := checkRow_sound r (hrows r hr)
    by_cases hp : r.p = 2
    · simp [hp, hs.2.2.2 hp]
    · rw [if_pos hp]
      have hw := mul_le_mul_of_nonneg_right hs.2.2.1
        (show (0 : Real) ≤ (r.lo : Real) / scale by positivity)
      have hl := mul_le_mul_of_nonneg_left hs.2.1.1
        (show (0 : Real) ≤ (valuationWeight 175000000000 8750000000 r.p : Real) by positivity)
      simpa only [Nat.cast_mul, mul_div_assoc] using hw.trans hl

theorem empty_table_coverage_false : ([] : List Row).map Row.p ≠ primeList := by
  intro h
  have htwo : 2 ∈ primeList := by norm_num [primeList]
  rw [← h] at htwo
  simp at htwo

end
end TenthDiscriminant.FirstCertificate
