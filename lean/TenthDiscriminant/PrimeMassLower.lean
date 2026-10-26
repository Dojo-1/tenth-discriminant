import TenthDiscriminant.FactorialPrimeMass

/-!
# Changing factorial weights into determinant weights

This module isolates the finite algebra and clipping from the analytic
tail estimates. The two tail bounds are explicit hypotheses, not axioms.
-/

namespace TenthDiscriminant
set_option autoImplicit false
noncomputable section

def smallFactorialPrimes (R P : Nat) : Finset Nat :=
  (factorialPrimesBelow R).filter (fun p => p ≤ P)

def largeFactorialPrimes (R P : Nat) : Finset Nat :=
  (factorialPrimesBelow R).filter (fun p => P < p)

def floorSquareSum (R p : Nat) : Nat := ∑ r ∈ Finset.range R, (r / p) ^ 2

def factorialSmallMass (R P : Nat) : Real :=
  ∑ p ∈ smallFactorialPrimes R P, (factorialPowerSum R p : Real) * Real.log p

def factorialLargeLinearMass (R P : Nat) : Real :=
  ∑ p ∈ largeFactorialPrimes R P, (floorSum R p : Real) * Real.log p

def factorialLargeHigherMass (R P : Nat) : Real :=
  ∑ p ∈ largeFactorialPrimes R P,
    ((factorialPowerSum R p : Real) - floorSum R p) * Real.log p

def largeQuadraticLoss (R P : Nat) : Real :=
  ∑ p ∈ largeFactorialPrimes R P, (floorSquareSum R p : Real) * Real.log p

def smallOddValuationMass (R S P : Nat) : Real :=
  ∑ p ∈ (smallFactorialPrimes R P).filter (fun p => p ≠ 2),
    (valuationWeight R S p : Real) * Real.log p

def largeValuationMass (R S P : Nat) : Real :=
  ∑ p ∈ largeFactorialPrimes R P, (valuationWeight R S p : Real) * Real.log p

def exactOddPrimeMass (R S : Nat) : Real :=
  ∑ p ∈ oddPrimesBelow R, (2 * valuationWeight R S p : Nat) * Real.log p

def triangularMass (R : Nat) : Real := (R : Real) * ((R : Real) - 1) / 2

def squareMass (R : Nat) : Real :=
  (R : Real) * ((R : Real) - 1) * (2 * (R : Real) - 1) / 6

def enderTailIntegral (P : Nat) : Real :=
  Real.log ((P : Real) + 1) / P + Real.log (1 + 1 / (P : Real))

def enderTailLower (R S P : Nat) (I : Real) : Real :=
  ((S : Real) - 1 / 2) *
    (factorialLower R - factorialSmallMass R P - triangularMass R * I) -
      squareMass R * I / 2

/-- The mathematical clipping used by production; no Arb branch decision
is assumed by this definition. -/
def enderPrimeMassLower (R S P : Nat) (I : Real) : Real :=
  2 * (smallOddValuationMass R S P + max (enderTailLower R S P I) 0)

theorem factorialMass_split (R P : Nat) :
    factorialMass R = factorialSmallMass R P +
      factorialLargeLinearMass R P + factorialLargeHigherMass R P := by
  rw [factorialMass_eq_prime_power_sum]
  have hsplit := Finset.sum_filter_add_sum_filter_not (s := factorialPrimesBelow R)
    (p := fun p => p ≤ P)
    (f := fun p => (factorialPowerSum R p : Real) * Real.log p)
  have hlarge : (factorialPrimesBelow R).filter (fun p => ¬ p ≤ P) =
      largeFactorialPrimes R P := by
    ext p
    simp [largeFactorialPrimes, not_le]
  rw [hlarge] at hsplit
  unfold factorialSmallMass smallFactorialPrimes factorialLargeLinearMass
    factorialLargeHigherMass
  rw [add_assoc]
  rw [← Finset.sum_add_distrib]
  have heq : (∑ p ∈ largeFactorialPrimes R P,
      ((floorSum R p : Real) * Real.log p +
        ((factorialPowerSum R p : Real) - floorSum R p) * Real.log p)) =
      ∑ p ∈ largeFactorialPrimes R P, (factorialPowerSum R p : Real) * Real.log p := by
    apply Finset.sum_congr rfl
    intro p hp
    ring
  rw [heq]
  exact hsplit.symm

/-- The quotient guard is the mathematical purpose of `P*S>=R`. -/
theorem quotient_le_of_large_prime (R S P p r : Nat) (hP : 2 ≤ P)
    (hRS : R ≤ P * S) (hp : P < p) (hr : r < R) : r / p ≤ S := by
  have hppos : 0 < p := by omega
  have hle : r < p * S := lt_of_lt_of_le hr (hRS.trans (Nat.mul_le_mul_right S hp.le))
  exact (Nat.div_lt_iff_lt_mul hppos).2 (by simpa [Nat.mul_comm] using hle) |>.le

/-- Exact rectangular weight, including its indispensable quadratic loss. -/
theorem valuationWeight_eq_linear_sub_quadratic (R S p : Nat)
    (hquot : ∀ r < R, r / p ≤ S) :
    (valuationWeight R S p : Real) =
      ((S : Real) - 1 / 2) * floorSum R p - (floorSquareSum R p : Real) / 2 := by
  have hnat : 2 * valuationWeight R S p + floorSquareSum R p + floorSum R p =
      2 * S * floorSum R p := by
    unfold valuationWeight floorSquareSum floorSum
    simp only [Finset.mul_sum, ← Finset.sum_add_distrib]
    apply Finset.sum_congr rfl
    intro r hr
    rw [← Finset.mul_sum]
    have h := sum_min_identity S (r / p) (hquot r (Finset.mem_range.mp hr))
    nlinarith
  have hreal : 2 * (valuationWeight R S p : Real) + floorSquareSum R p + floorSum R p =
      2 * S * floorSum R p := by exact_mod_cast hnat
  nlinarith

theorem largeValuationMass_eq (R S P : Nat) (hP : 2 ≤ P) (hRS : R ≤ P * S) :
    largeValuationMass R S P =
      ((S : Real) - 1 / 2) * factorialLargeLinearMass R P -
        largeQuadraticLoss R P / 2 := by
  unfold largeValuationMass factorialLargeLinearMass largeQuadraticLoss
  rw [Finset.mul_sum, Finset.sum_div, ← Finset.sum_sub_distrib]
  apply Finset.sum_congr rfl
  intro p hp
  have hlarge := (Finset.mem_filter.mp hp).2
  rw [valuationWeight_eq_linear_sub_quadratic R S p
    (fun r hr => quotient_le_of_large_prime R S P p r hP hRS hlarge hr)]
  ring

theorem largeValuationMass_nonneg (R S P : Nat) : 0 ≤ largeValuationMass R S P := by
  apply Finset.sum_nonneg
  intro p hp
  have hprime := (Finset.mem_filter.mp (Finset.mem_filter.mp hp).1).2
  exact mul_nonneg (by positivity) (Real.log_nonneg (by exact_mod_cast hprime.one_le))

theorem exactOddPrimeMass_split (R S P : Nat) (hP : 2 ≤ P) :
    exactOddPrimeMass R S =
      2 * (smallOddValuationMass R S P + largeValuationMass R S P) := by
  have hsets : oddPrimesBelow R =
      ((smallFactorialPrimes R P).filter (fun p => p ≠ 2)) ∪ largeFactorialPrimes R P := by
    ext p
    by_cases hprime : p.Prime
    · simp only [oddPrimesBelow, smallFactorialPrimes, largeFactorialPrimes,
        factorialPrimesBelow, Finset.mem_filter, Finset.mem_range, Finset.mem_union, hprime,
        and_true, true_and]
      have hpone := hprime.two_le
      omega
    · simp [oddPrimesBelow, smallFactorialPrimes, largeFactorialPrimes,
        factorialPrimesBelow, hprime]
  have hdis : Disjoint ((smallFactorialPrimes R P).filter (fun p => p ≠ 2))
      (largeFactorialPrimes R P) := by
    apply Finset.disjoint_left.mpr
    intro p hs hl
    have hs' := (Finset.mem_filter.mp (Finset.mem_filter.mp hs).1).2
    have hl' := (Finset.mem_filter.mp hl).2
    omega
  unfold exactOddPrimeMass smallOddValuationMass largeValuationMass
  rw [hsets, Finset.sum_union hdis, mul_add, Finset.mul_sum, Finset.mul_sum]
  congr 1 <;> apply Finset.sum_congr rfl <;> intro p hp <;> push_cast <;> ring

/-- The finite lower-bound architecture. The two analytic tail bounds
remain visible; clipping is justified by the actual large-prime mass. -/
theorem enderPrimeMassLower_le_exact (R S P : Nat) (I : Real)
    (hR : 2 ≤ R) (hS : 1 ≤ S) (hP : 2 ≤ P) (hRS : R ≤ P * S)
    (hhigher : factorialLargeHigherMass R P ≤ triangularMass R * I)
    (hquadratic : largeQuadraticLoss R P ≤ squareMass R * I) :
    enderPrimeMassLower R S P I ≤ exactOddPrimeMass R S := by
  have hfac := factorialLower_le_mass R hR
  rw [factorialMass_split R P] at hfac
  have hlinear : factorialLower R - factorialSmallMass R P - triangularMass R * I ≤
      factorialLargeLinearMass R P := by linarith
  have hcoeff : (0 : Real) ≤ (S : Real) - 1 / 2 := by
    have hsreal : (1 : Real) ≤ S := by exact_mod_cast hS
    linarith
  have hmul := mul_le_mul_of_nonneg_left hlinear hcoeff
  have htail : enderTailLower R S P I ≤ largeValuationMass R S P := by
    rw [largeValuationMass_eq R S P hP hRS]
    unfold enderTailLower
    linarith
  have hclip : max (enderTailLower R S P I) 0 ≤ largeValuationMass R S P :=
    max_le htail (largeValuationMass_nonneg R S P)
  rw [exactOddPrimeMass_split R S P hP]
  unfold enderPrimeMassLower
  linarith

theorem sum_range_real_eq_triangularMass (R : Nat) :
    (∑ r ∈ Finset.range R, (r : Real)) = triangularMass R := by
  induction R with
  | zero => simp [triangularMass]
  | succ R ih =>
    rw [Finset.sum_range_succ, ih]
    unfold triangularMass
    push_cast
    ring

theorem sum_range_real_sq_eq_squareMass (R : Nat) :
    (∑ r ∈ Finset.range R, (r : Real) ^ 2) = squareMass R := by
  induction R with
  | zero => simp [squareMass]
  | succ R ih =>
    rw [Finset.sum_range_succ, ih]
    unfold squareMass
    push_cast
    ring

theorem floorSum_le_triangularMass_div (R p : Nat) :
    (floorSum R p : Real) ≤ triangularMass R / p := by
  unfold floorSum
  rw [Nat.cast_sum]
  calc
    _ ≤ ∑ r ∈ Finset.range R, (r : Real) / p :=
      Finset.sum_le_sum (fun r hr => Nat.cast_div_le)
    _ = _ := by rw [← Finset.sum_div, sum_range_real_eq_triangularMass]

theorem floorSquareSum_le_squareMass_div (R p : Nat) :
    (floorSquareSum R p : Real) ≤ squareMass R / (p : Real) ^ 2 := by
  unfold floorSquareSum
  rw [Nat.cast_sum]
  calc
    _ ≤ ∑ r ∈ Finset.range R, (r : Real) ^ 2 / (p : Real) ^ 2 := by
      apply Finset.sum_le_sum
      intro r hr
      have hd : ((r / p : Nat) : Real) ≤ (r : Real) / p := Nat.cast_div_le
      have hprod := mul_nonneg (sub_nonneg.mpr hd)
        (show (0 : Real) ≤ (r : Real) / p + ((r / p : Nat) : Real) by positivity)
      push_cast
      rw [← div_pow]
      nlinarith
    _ = _ := by rw [← Finset.sum_div, sum_range_real_sq_eq_squareMass]

theorem triangularMass_eq_production (R : Nat) :
    triangularMass R = ((R * (R - 1) / 2 : Nat) : Real) := by
  rw [← Finset.sum_range_id]
  simpa only [Nat.cast_sum] using (sum_range_real_eq_triangularMass R).symm

theorem squareMass_eq_production (R : Nat) :
    squareMass R = ((R * (R - 1) * (2 * R - 1) / 6 : Nat) : Real) := by
  by_cases hzero : R = 0
  · subst R
    norm_num [squareMass]
  have hRone : 1 ≤ R := by omega
  have htwo : 1 ≤ 2 * R := by omega
  have hsum : ((∑ r ∈ Finset.range R, r ^ 2 : Nat) : Real) = squareMass R := by
    simpa only [Nat.cast_sum, Nat.cast_pow] using sum_range_real_sq_eq_squareMass R
  have hcast : ((R * (R - 1) * (2 * R - 1) : Nat) : Real) = 6 * squareMass R := by
    push_cast [Nat.cast_sub hRone, Nat.cast_sub htwo]
    unfold squareMass
    ring
  have hnat : R * (R - 1) * (2 * R - 1) = 6 * (∑ r ∈ Finset.range R, r ^ 2) := by
    exact_mod_cast (show ((R * (R - 1) * (2 * R - 1) : Nat) : Real) =
        ((6 * (∑ r ∈ Finset.range R, r ^ 2) : Nat) : Real) by
      calc
        _ = 6 * squareMass R := hcast
        _ = _ := by simp only [Nat.cast_mul, Nat.cast_ofNat, hsum])
  have hdiv : R * (R - 1) * (2 * R - 1) / 6 = ∑ r ∈ Finset.range R, r ^ 2 := by omega
  rw [hdiv]
  exact hsum.symm

def productionSmallPrimes (P : Nat) : Finset Nat :=
  (Finset.range (P + 1)).filter Nat.Prime

theorem factorialPowerSum_eq_zero_of_le (R p : Nat) (hp : R ≤ p) :
    factorialPowerSum R p = 0 := by
  rw [factorialPowerSum_eq_unfiltered]
  apply Finset.sum_eq_zero
  intro j hj
  have hjpos : j ≠ 0 := by have h := (Finset.mem_Ico.mp hj).1; omega
  exact floorSum_eq_zero_of_le R (p ^ j) (hp.trans (Nat.le_self_pow hjpos p))

/-- Production enumerates all primes up to P. Primes beyond R are zero,
so this is the same exact finite small-prime subtraction. -/
theorem factorialSmallMass_eq_padded (R P : Nat) :
    factorialSmallMass R P = ∑ p ∈ productionSmallPrimes P,
      (factorialPowerSum R p : Real) * Real.log p := by
  have hsub : smallFactorialPrimes R P ⊆ productionSmallPrimes P := by
    intro p hp
    rcases Finset.mem_filter.mp hp with ⟨hf, hP⟩
    rcases Finset.mem_filter.mp hf with ⟨hR, hprime⟩
    exact Finset.mem_filter.mpr ⟨Finset.mem_range.mpr (by omega), hprime⟩
  apply Finset.sum_subset hsub
  intro p hp hnot
  rcases Finset.mem_filter.mp hp with ⟨hP, hprime⟩
  have hpR : R ≤ p := by
    by_contra h
    exact hnot (Finset.mem_filter.mpr ⟨Finset.mem_filter.mpr
      ⟨Finset.mem_range.mpr (by omega), hprime⟩, by have h := Finset.mem_range.mp hP; omega⟩)
  rw [factorialPowerSum_eq_zero_of_le R p hpR]
  simp

theorem smallOddValuationMass_eq_padded (R S P : Nat) :
    smallOddValuationMass R S P =
      ∑ p ∈ (productionSmallPrimes P).filter (fun p => p ≠ 2),
        (valuationWeight R S p : Real) * Real.log p := by
  have hsub : (smallFactorialPrimes R P).filter (fun p => p ≠ 2) ⊆
      (productionSmallPrimes P).filter (fun p => p ≠ 2) := by
    intro p hp
    rcases Finset.mem_filter.mp hp with ⟨hs, hodd⟩
    rcases Finset.mem_filter.mp hs with ⟨hf, hP⟩
    rcases Finset.mem_filter.mp hf with ⟨hR, hprime⟩
    exact Finset.mem_filter.mpr ⟨Finset.mem_filter.mpr
      ⟨Finset.mem_range.mpr (by omega), hprime⟩, hodd⟩
  apply Finset.sum_subset hsub
  intro p hp hnot
  rcases Finset.mem_filter.mp hp with ⟨hf, hodd⟩
  rcases Finset.mem_filter.mp hf with ⟨hP, hprime⟩
  have hpR : R ≤ p := by
    by_contra h
    exact hnot (Finset.mem_filter.mpr ⟨Finset.mem_filter.mpr
      ⟨Finset.mem_filter.mpr ⟨Finset.mem_range.mpr (by omega), hprime⟩,
        by have h := Finset.mem_range.mp hP; omega⟩, hodd⟩)
  rw [valuationWeight_eq_zero R S p hpR]
  simp

theorem enderTailLower_eq_production_coefficients (R S P : Nat) (I : Real) :
    enderTailLower R S P I = ((S : Real) - 1 / 2) *
      (factorialLower R - (∑ p ∈ productionSmallPrimes P,
        (factorialPowerSum R p : Real) * Real.log p) -
          ((R * (R - 1) / 2 : Nat) : Real) * I) -
            ((R * (R - 1) * (2 * R - 1) / 6 : Nat) : Real) * I / 2 := by
  rw [enderTailLower, factorialSmallMass_eq_padded, triangularMass_eq_production,
    squareMass_eq_production]

theorem enderPrimeMassLower_eq_production_branch (R S P : Nat) (I : Real) :
    enderPrimeMassLower R S P I =
      if 0 < enderTailLower R S P I then
        2 * ((∑ p ∈ (productionSmallPrimes P).filter (fun p => p ≠ 2),
          (valuationWeight R S p : Real) * Real.log p) + enderTailLower R S P I)
      else 2 * (∑ p ∈ (productionSmallPrimes P).filter (fun p => p ≠ 2),
        (valuationWeight R S p : Real) * Real.log p) := by
  classical
  rw [enderPrimeMassLower, smallOddValuationMass_eq_padded]
  by_cases ht : 0 < enderTailLower R S P I
  · simp [ht, max_eq_left ht.le]
  · simp [ht, max_eq_right (le_of_not_gt ht)]

theorem triangularMass_nonneg (R : Nat) : 0 ≤ triangularMass R := by
  rw [← sum_range_real_eq_triangularMass]
  exact Finset.sum_nonneg (fun r hr => Nat.cast_nonneg r)

theorem squareMass_nonneg (R : Nat) : 0 ≤ squareMass R := by
  rw [← sum_range_real_sq_eq_squareMass]
  exact Finset.sum_nonneg (fun r hr => sq_nonneg _)

theorem factorialHigherWeight_le (R p : Nat) (hR : 2 ≤ R) (hp : 2 ≤ p) :
    (factorialPowerSum R p : Real) - floorSum R p ≤
      triangularMass R / ((p : Real) * ((p : Real) - 1)) := by
  have hppos : (0 : Real) < p := by exact_mod_cast (by omega : 0 < p)
  have hpone : (1 : Real) < p := by exact_mod_cast (by omega : 1 < p)
  have hsplit : (factorialPowerSum R p : Real) - floorSum R p =
      ∑ j ∈ Finset.Ico 2 R, (floorSum R (p ^ j) : Real) := by
    rw [factorialPowerSum_eq_unfiltered,
      Finset.sum_eq_sum_Ico_succ_bot (by omega : 1 < R)]
    simp only [pow_one, Nat.cast_add, Nat.cast_sum, add_sub_cancel_left]
  have hgeom := geom_sum_Ico_le_of_lt_one (m := 2) (n := R)
    (show (0 : Real) ≤ 1 / (p : Real) by positivity)
    ((div_lt_one hppos).2 hpone)
  rw [hsplit]
  calc
    _ ≤ ∑ j ∈ Finset.Ico 2 R, triangularMass R / ((p ^ j : Nat) : Real) :=
      Finset.sum_le_sum (fun j hj => floorSum_le_triangularMass_div R (p ^ j))
    _ = triangularMass R * ∑ j ∈ Finset.Ico 2 R, (1 / (p : Real)) ^ j := by
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro j hj
      simp [Nat.cast_pow, div_pow, div_eq_mul_inv]
    _ ≤ triangularMass R * ((1 / (p : Real)) ^ 2 / (1 - 1 / (p : Real))) :=
      mul_le_mul_of_nonneg_left hgeom (triangularMass_nonneg R)
    _ = _ := by
      have hdenpos : (0 : Real) < 1 - 1 / (p : Real) :=
        sub_pos.mpr ((div_lt_one hppos).2 hpone)
      field_simp [ne_of_gt hppos, ne_of_gt (sub_pos.mpr hpone), ne_of_gt hdenpos]
      ring

def largeReciprocalTail (R P : Nat) : Real :=
  ∑ p ∈ largeFactorialPrimes R P, Real.log p / ((p : Real) * ((p : Real) - 1))

theorem factorialLargeHigherMass_le_tail (R P : Nat) (hR : 2 ≤ R) :
    factorialLargeHigherMass R P ≤ triangularMass R * largeReciprocalTail R P := by
  unfold factorialLargeHigherMass largeReciprocalTail
  rw [Finset.mul_sum]
  apply Finset.sum_le_sum
  intro p hp
  have hprime := (Finset.mem_filter.mp (Finset.mem_filter.mp hp).1).2
  have hlog := Real.log_nonneg (show (1 : Real) ≤ p by exact_mod_cast hprime.one_le)
  have h := mul_le_mul_of_nonneg_right (factorialHigherWeight_le R p hR hprime.two_le) hlog
  convert h using 1
  ring

theorem largeQuadraticLoss_le_tail (R P : Nat) :
    largeQuadraticLoss R P ≤ squareMass R * largeReciprocalTail R P := by
  unfold largeQuadraticLoss largeReciprocalTail
  rw [Finset.mul_sum]
  apply Finset.sum_le_sum
  intro p hp
  have hprime := (Finset.mem_filter.mp (Finset.mem_filter.mp hp).1).2
  have hpone : (1 : Real) < p := by exact_mod_cast hprime.one_lt
  have hlog := Real.log_nonneg hpone.le
  have hden : (0 : Real) < (p : Real) * ((p : Real) - 1) :=
    mul_pos (by linarith) (sub_pos.mpr hpone)
  have hrecip : Real.log p / (p : Real) ^ 2 ≤
      Real.log p / ((p : Real) * ((p : Real) - 1)) :=
    div_le_div_of_nonneg_left hlog hden (by nlinarith)
  calc
    _ ≤ (squareMass R / (p : Real) ^ 2) * Real.log p :=
      mul_le_mul_of_nonneg_right (floorSquareSum_le_squareMass_div R p) hlog
    _ = squareMass R * (Real.log p / (p : Real) ^ 2) := by ring
    _ ≤ _ := mul_le_mul_of_nonneg_left hrecip (squareMass_nonneg R)

/-- Only one analytic tail bound is needed for both losses. The finite
geometric series and floor-square estimates have already been proved. -/
theorem enderPrimeMassLower_le_exact_of_tail (R S P : Nat) (I : Real)
    (hR : 2 ≤ R) (hS : 1 ≤ S) (hP : 2 ≤ P) (hRS : R ≤ P * S)
    (htail : largeReciprocalTail R P ≤ I) :
    enderPrimeMassLower R S P I ≤ exactOddPrimeMass R S := by
  apply enderPrimeMassLower_le_exact R S P I hR hS hP hRS
  · exact (factorialLargeHigherMass_le_tail R P hR).trans
      (mul_le_mul_of_nonneg_left htail (triangularMass_nonneg R))
  · exact (largeQuadraticLoss_le_tail R P).trans
      (mul_le_mul_of_nonneg_left htail (squareMass_nonneg R))

/-- The finite lower expression reaches the actual counted upper formula,
but only after the displayed reciprocal-tail bound has been supplied. -/
theorem ellipse_enderPrimeMassLower_le_upperB
    (D₁ D D₂ rho R S Y P : Nat) (I : Real)
    (hD₁ : 0 < D₁) (hDlo : D₁ ≤ D) (hDhi : D ≤ D₂)
    (hR : 2 ≤ R) (hS : 1 ≤ S) (hP : 2 ≤ P) (hRS : R ≤ P * S)
    [Fact ((D : Int) % 4 = 3)] (hDsq : Squarefree D)
    (hclass : NumberField.classNumber
      (QuadraticField (((D : Int) + 1) / 4)) = 1)
    (hRcut : (R : Int) < ((D : Int) + 1) / 4) (hRrho : rho < R)
    (hY : ellipseVerticalBound D₁ rho ≤ Y)
    (hradius : (1001 / 1000 : Real) *
        Real.sqrt (((3 * R + S : Nat) : Real) * Real.sqrt D₂ / Real.pi) +
        10 * Real.sqrt D₂ ≤ (rho : Real))
    (htail : largeReciprocalTail R P ≤ I) :
    enderPrimeMassLower R S P I ≤
      enderUpperB R S S rho (ellipsePaddedUpperCount D₁ rho Y) := by
  exact (enderPrimeMassLower_le_exact_of_tail R S P I hR hS hP hRS htail).trans
    (ellipse_primeMass_log_le_counted_upperB D₁ D D₂ rho R S Y hD₁ hDlo hDhi
      (by omega) hS hDsq hclass hRcut hRrho hY hradius)

theorem weight_conversion_nonzero_loss_control :
    valuationWeight 5 2 3 = 2 ∧ floorSum 5 3 = 2 ∧ floorSquareSum 5 3 = 2 := by decide

theorem weight_conversion_endpoint_control :
    (valuationWeight 6 3 3 : Real) =
      ((3 : Real) - 1 / 2) * floorSum 6 3 - (floorSquareSum 6 3 : Real) / 2 := by
  apply valuationWeight_eq_linear_sub_quadratic
  intro r hr
  exact quotient_le_of_large_prime 6 3 2 3 r (by decide) (by decide) (by decide) hr

theorem prime_split_boundary_control :
    3 ∈ smallFactorialPrimes 5 3 ∧ 3 ∉ largeFactorialPrimes 5 3 := by decide

theorem empty_large_prime_control : largeFactorialPrimes 5 5 = ∅ := by decide

theorem clipping_nonpositive_control (R S P : Nat) (I : Real)
    (ht : enderTailLower R S P I ≤ 0) :
    enderPrimeMassLower R S P I = 2 * smallOddValuationMass R S P := by
  simp [enderPrimeMassLower, max_eq_right ht]

theorem clipping_nonnegative_control (R S P : Nat) (I : Real)
    (ht : 0 ≤ enderTailLower R S P I) :
    enderPrimeMassLower R S P I =
      2 * (smallOddValuationMass R S P + enderTailLower R S P I) := by
  rw [enderPrimeMassLower, max_eq_left ht]

theorem weight_without_quadratic_loss_false :
    (valuationWeight 5 2 3 : Real) ≠ ((2 : Real) - 1 / 2) * floorSum 5 3 := by
  norm_num [valuationWeight, floorSum, Finset.sum_range_succ]

theorem weight_without_quotient_guard_false :
    (valuationWeight 8 2 2 : Real) ≠
      ((2 : Real) - 1 / 2) * floorSum 8 2 - (floorSquareSum 8 2 : Real) / 2 := by
  norm_num [valuationWeight, floorSum, floorSquareSum, Finset.sum_range_succ]

end
end TenthDiscriminant
