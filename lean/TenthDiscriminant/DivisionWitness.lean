import TenthDiscriminant.NumericalWeights

/-! Division-free certificates for finite floor sums. The witnesses are untrusted:
their Euclidean division equations and scaled sums are checked exactly. -/
namespace TenthDiscriminant
set_option autoImplicit false

structure FloorWitness where
  quotient : Nat
  remainder : Nat
  value : Nat
deriving DecidableEq, Repr

def checkFloorWitness (R q : Nat) (w : FloorWitness) : Bool := decide (
  0 < q ∧ w.remainder < q ∧ w.remainder + q * w.quotient = R ∧
    2 * w.value + q * w.quotient =
      q * w.quotient ^ 2 + 2 * w.quotient * w.remainder)

theorem checkFloorWitness_sound (R q : Nat) (w : FloorWitness)
    (hc : checkFloorWitness R q w = true) : w.value = floorSum R q := by
  rcases of_decide_eq_true hc with ⟨hq, hm, hR, hv⟩
  have hd := (Nat.div_mod_unique hq).mpr ⟨hR, hm⟩
  have hs := floorSum_scaled R q
  rw [hd.1, hd.2] at hs
  nlinarith

def powerMass (R p q : Nat) : Nat → Nat
  | 0 => 0
  | n + 1 => floorSum R q + powerMass R p (q * p) n

def checkPowerWitnesses (R p q : Nat) : Nat → List FloorWitness → Bool
  | 0, ws => decide (ws = [])
  | _ + 1, [] => decide (R ≤ q)
  | n + 1, w :: ws => checkFloorWitness R q w && checkPowerWitnesses R p (q * p) n ws

theorem powerMass_zero (R p q n : Nat) (hp : 1 ≤ p) (hq : R ≤ q) :
    powerMass R p q n = 0 := by
  induction n generalizing q with
  | zero => rfl
  | succ n ih =>
    rw [powerMass, floorSum_eq_zero_of_le R q hq,
      ih (q * p) (hq.trans (by nlinarith)), zero_add]

theorem checkPowerWitnesses_sound (R p q n : Nat) (ws : List FloorWitness)
    (hp : 1 ≤ p) (hc : checkPowerWitnesses R p q n ws = true) :
    (ws.map FloorWitness.value).sum = powerMass R p q n := by
  induction n generalizing q ws with
  | zero =>
    have hw : ws = [] := of_decide_eq_true hc
    subst ws
    rfl
  | succ n ih =>
    cases ws with
    | nil =>
      have hq : R ≤ q := of_decide_eq_true hc
      simp only [List.map_nil, List.sum_nil, powerMass_zero R p q (n+1) hp hq]
    | cons w ws =>
      have hh : checkFloorWitness R q w = true ∧
          checkPowerWitnesses R p (q*p) n ws = true := by
        simpa only [checkPowerWitnesses, Bool.and_eq_true] using hc
      simp only [List.map_cons, List.sum_cons, powerMass]
      rw [checkFloorWitness_sound R q w hh.1, ih (q*p) ws hh.2]

theorem powerMass_eq_sum (R p q n : Nat) :
    powerMass R p q n = ∑ i ∈ Finset.range n, floorSum R (q * p ^ i) := by
  induction n generalizing q with
  | zero => simp [powerMass]
  | succ n ih =>
    rw [powerMass, ih, Finset.sum_range_succ']
    simp only [pow_zero, mul_one]
    rw [add_comm]
    congr 1
    apply Finset.sum_congr rfl
    intro i hi
    congr 1
    ring

theorem first_powerMass (p : Nat) (hp : 2 ≤ p) :
    powerMass 175000000000 p p 37 = factorialPowerSum 175000000000 p := by
  rw [first_factorial_coefficient p hp, factorialCoefficient, Finset.sum_Ico_eq_sum_range]
  rw [powerMass_eq_sum]
  apply Finset.sum_congr rfl
  intro i hi
  change floorSum 175000000000 (p * p ^ i) =
    p ^ (1+i) * (175000000000 / p ^ (1+i)) * (175000000000 / p ^ (1+i) - 1) / 2 +
      (175000000000 / p ^ (1+i)) * (175000000000 % p ^ (1+i))
  rw [← floorSum_closed]
  congr 1
  simp [pow_succ, Nat.add_comm, Nat.mul_comm]

/-- A fixed square sum, established once rather than divided in every row. -/
theorem first_squareMass : squareMass 175000000000 = (1786458333318020833333362500000000 : Real) := by
  norm_num [squareMass]

def checkWitnessWeight (S p w A W : Nat) : Bool := decide (
  w = 0 ∨ 2 * p ^ 2 * w + W ≤ (2 * S - 1) * A * p ^ 2)

theorem checkWitnessWeight_sound (R S p w A W : Nat)
    (hS : 1 ≤ S) (hp : 0 < p) (hA : A = floorSum R p)
    (hW : (W : Real) = squareMass R)
    (hc : checkWitnessWeight S p w A W = true) : (w : Real) ≤ valuationWeight R S p := by
  rcases of_decide_eq_true hc with hz | hw
  · subst w
    exact_mod_cast Nat.zero_le (valuationWeight R S p)
  · have htwo : 1 ≤ 2 * S := by omega
    have hr : ((2 * p ^ 2 * w + W : Nat) : Real) ≤
        (((2 * S - 1) * A * p ^ 2 : Nat) : Real) := by exact_mod_cast hw
    push_cast [Nat.cast_sub htwo] at hr
    rw [hA, hW] at hr
    have hppos : (0 : Real) < p := by exact_mod_cast hp
    have hden : (0 : Real) < 2 * (p : Real) ^ 2 := by positivity
    have hb : (w : Real) ≤ ((S : Real) - 1 / 2) * floorSum R p -
        squareMass R / (2 * (p : Real) ^ 2) := by
      apply (le_sub_iff_add_le).mpr
      apply (mul_le_mul_right hden).mp
      have hcancel := div_mul_cancel₀ (squareMass R) (ne_of_gt hden)
      nlinarith
    exact hb.trans (valuationWeight_ge_floor_bound R S p)

theorem corrupt_division_witness_rejected :
    checkFloorWitness 11 3 ⟨3, 1, 15⟩ = false := by decide

theorem omitted_power_witness_rejected :
    checkPowerWitnesses 11 3 3 37 [] = false := by decide

end TenthDiscriminant
