import TenthDiscriminant.EllipseCellArea
import TenthDiscriminant.ClassNumberInertBridge

/-!
# Local prime powers assembled on the same positive integer Gram

Each inert prime supplies a divisor of the actual integer determinant.
Distinct prime powers are coprime, so their product is also a divisor.
The chosen-radius theorem makes that determinant positive, allowing an
ordinary size comparison with the real Hadamard diagonal product.
This is an exact finite bridge, not Ender's factorial estimate or cutoff.
-/

namespace TenthDiscriminant

/-- A finite family of distinct prime powers dividing one integer has a
product which divides that integer. An empty family has product one. -/
theorem primePowerProduct_dvd_int (P : Finset Nat) (e : Nat → Nat) (z : Int)
    (hprime : ∀ p ∈ P, p.Prime)
    (hlocal : ∀ p ∈ P, (p : Int) ^ e p ∣ z) :
    ((∏ p ∈ P, p ^ e p : Nat) : Int) ∣ z := by
  classical
  have hpair : (P : Set Nat).Pairwise
      (fun p q => IsCoprime ((p : Int) ^ e p) ((q : Int) ^ e q)) := by
    intro p hp q hq hpq
    have hc : Nat.Coprime (p ^ e p) (q ^ e q) :=
      Nat.coprime_pow_primes (e p) (e q) (hprime p hp) (hprime q hq) hpq
    simpa only [Nat.cast_pow] using (Nat.Coprime.isCoprime hc)
  have h := Finset.prod_dvd_of_coprime hpair hlocal
  simpa only [Nat.cast_prod, Nat.cast_pow] using h

/-- The finite product of local factors lies between one and the positive
integer determinant, with no logarithm or floating-point approximation. -/
theorem primePowerProduct_le_det (P : Finset Nat) (e : Nat → Nat) (z : Int)
    (hz : 0 < z) (hprime : ∀ p ∈ P, p.Prime)
    (hlocal : ∀ p ∈ P, (p : Int) ^ e p ∣ z) :
    (∏ p ∈ P, p ^ e p : Nat) ≤ z.natAbs := by
  have hdiv := primePowerProduct_dvd_int P e z hprime hlocal
  have hnonzero : z ≠ 0 := ne_of_gt hz
  simpa only [Int.natAbs_natCast] using Int.natAbs_le_of_dvd_ne_zero hdiv hnonzero

/-- Under class number one, every registered odd small prime contributes
its exact `2F(p)` factor to the *same* integer ellipse Gram determinant. -/
theorem ellipse_primeMass_product_dvd
    (P : Finset Nat) (D rho R S : Nat)
    [Fact ((D : Int) % 4 = 3)] (hDsq : Squarefree D)
    (hclass : NumberField.classNumber
      (QuadraticField (((D : Int) + 1) / 4)) = 1)
    (hprime : ∀ p ∈ P, p.Prime)
    (hodd : ∀ p ∈ P, p ≠ 2)
    (hsmall : ∀ p ∈ P, (p : Int) < ((D : Int) + 1) / 4) :
    ((∏ p ∈ P, p ^ (2 * valuationWeight R S p) : Nat) : Int) ∣
      (integerRectangularTraceGram (ellipsePairs D rho) D S R S).det := by
  classical
  apply primePowerProduct_dvd_int P (fun p => 2 * valuationWeight R S p) _ hprime
  intro p hp
  letI : Fact p.Prime := ⟨hprime p hp⟩
  exact rectangularTraceGram_valuation_of_classNumber_one
    (ellipsePairs D rho) D S R S p hDsq (hodd p hp) (hsmall p hp) hclass

/-- At Ender's chosen upper-endpoint radius, local arithmetic and real
geometry meet in a single exact determinant sandwich. -/
theorem ellipse_primeMass_hadamard_sandwich
    (P : Finset Nat) (D D₂ rho R S : Nat)
    (hD : 0 < D) (hD₂ : D ≤ D₂) (hR : 1 ≤ R) (hS : 1 ≤ S)
    [Fact ((D : Int) % 4 = 3)] (hDsq : Squarefree D)
    (hclass : NumberField.classNumber
      (QuadraticField (((D : Int) + 1) / 4)) = 1)
    (hprime : ∀ p ∈ P, p.Prime) (hodd : ∀ p ∈ P, p ≠ 2)
    (hsmall : ∀ p ∈ P, (p : Int) < ((D : Int) + 1) / 4)
    (hradius : (1001 / 1000 : Real) *
        Real.sqrt (((3 * R + S : Nat) : Real) * Real.sqrt D₂ / Real.pi) +
        10 * Real.sqrt D₂ ≤ (rho : Real)) :
    ((∏ p ∈ P, p ^ (2 * valuationWeight R S p) : Nat) : Real) ≤
        (rectangularTraceGram (ellipsePoints D rho) S R S).det ∧
      (rectangularTraceGram (ellipsePoints D rho) S R S).det ≤
        Finset.univ.prod (fun i =>
          rectangularTraceGram (ellipsePoints D rho) S R S i i) := by
  have hb := ellipseTraceGram_det_bounds_of_ender_radius
    D D₂ rho R S hD hD₂ hR hS hradius
  have hpos : 0 < (integerRectangularTraceGram
      (ellipsePairs D rho) D S R S).det := by
    have hreal : (0 : Real) <
        ((integerRectangularTraceGram (ellipsePairs D rho) D S R S).det : Real) := by
      rw [ellipseIntegerTraceGram_det_cast D rho S R S hD]
      exact hb.1
    exact_mod_cast hreal
  have hdvd := ellipse_primeMass_product_dvd P D rho R S
    hDsq hclass hprime hodd hsmall
  have hle : (∏ p ∈ P, p ^ (2 * valuationWeight R S p) : Nat) ≤
      (integerRectangularTraceGram (ellipsePairs D rho) D S R S).det.natAbs := by
    have hnonzero : (integerRectangularTraceGram
        (ellipsePairs D rho) D S R S).det ≠ 0 := ne_of_gt hpos
    simpa only [Int.natAbs_natCast] using
      Int.natAbs_le_of_dvd_ne_zero hdvd hnonzero
  constructor
  · have hleInt : ((∏ p ∈ P, p ^ (2 * valuationWeight R S p) : Nat) : Int) ≤
        (integerRectangularTraceGram (ellipsePairs D rho) D S R S).det := by
      have hcast : ((∏ p ∈ P, p ^ (2 * valuationWeight R S p) : Nat) : Int) ≤
          ((integerRectangularTraceGram (ellipsePairs D rho) D S R S).det.natAbs : Int) := by
        exact_mod_cast hle
      simpa only [Int.natCast_natAbs, abs_of_pos hpos] using hcast
    have hcast : ((∏ p ∈ P, p ^ (2 * valuationWeight R S p) : Nat) : Real) ≤
        ((integerRectangularTraceGram (ellipsePairs D rho) D S R S).det : Real) := by
      exact_mod_cast hleInt
    rwa [ellipseIntegerTraceGram_det_cast D rho S R S hD] at hcast
  · exact hb.2

/-- Exactly Ender's local-prime range: all odd primes below the row count.
The prime filter is finite and its members are distinct by construction. -/
def oddPrimesBelow (R : Nat) : Finset Nat :=
  (Finset.range R).filter (fun p => p.Prime ∧ p ≠ 2)

/-- The actual full odd-prime product, not a caller-selected subfamily. -/
theorem ellipse_allOddPrimeMass_hadamard_sandwich
    (D D₂ rho R S : Nat)
    (hD : 0 < D) (hD₂ : D ≤ D₂) (hR : 1 ≤ R) (hS : 1 ≤ S)
    [Fact ((D : Int) % 4 = 3)] (hDsq : Squarefree D)
    (hclass : NumberField.classNumber
      (QuadraticField (((D : Int) + 1) / 4)) = 1)
    (hRcut : (R : Int) < ((D : Int) + 1) / 4)
    (hradius : (1001 / 1000 : Real) *
        Real.sqrt (((3 * R + S : Nat) : Real) * Real.sqrt D₂ / Real.pi) +
        10 * Real.sqrt D₂ ≤ (rho : Real)) :
    ((∏ p ∈ oddPrimesBelow R,
        p ^ (2 * valuationWeight R S p) : Nat) : Real) ≤
        (rectangularTraceGram (ellipsePoints D rho) S R S).det ∧
      (rectangularTraceGram (ellipsePoints D rho) S R S).det ≤
        Finset.univ.prod (fun i =>
          rectangularTraceGram (ellipsePoints D rho) S R S i i) := by
  apply ellipse_primeMass_hadamard_sandwich
    (oddPrimesBelow R) D D₂ rho R S hD hD₂ hR hS hDsq hclass
  · intro p hp
    exact (Finset.mem_filter.mp hp).2.1
  · intro p hp
    exact (Finset.mem_filter.mp hp).2.2
  · intro p hp
    have hpR : p < R := Finset.mem_range.mp (Finset.mem_filter.mp hp).1
    have hpRi : (p : Int) < R := by exact_mod_cast hpR
    exact lt_trans hpRi hRcut
  · exact hradius

/-- Taking logarithms turns the exact product into Ender's finite
prime-weight sum. No factorial or numerical lower estimate is used. -/
theorem ellipse_allOddPrimeMass_log_le_hadamard
    (D D₂ rho R S : Nat)
    (hD : 0 < D) (hD₂ : D ≤ D₂) (hR : 1 ≤ R) (hS : 1 ≤ S)
    [Fact ((D : Int) % 4 = 3)] (hDsq : Squarefree D)
    (hclass : NumberField.classNumber
      (QuadraticField (((D : Int) + 1) / 4)) = 1)
    (hRcut : (R : Int) < ((D : Int) + 1) / 4)
    (hradius : (1001 / 1000 : Real) *
        Real.sqrt (((3 * R + S : Nat) : Real) * Real.sqrt D₂ / Real.pi) +
        10 * Real.sqrt D₂ ≤ (rho : Real)) :
    (∑ p ∈ oddPrimesBelow R,
        (2 * valuationWeight R S p : Nat) * Real.log (p : Real)) ≤
      Real.log (Finset.univ.prod (fun i =>
        rectangularTraceGram (ellipsePoints D rho) S R S i i)) := by
  let P := oddPrimesBelow R
  have hb := ellipse_allOddPrimeMass_hadamard_sandwich
    D D₂ rho R S hD hD₂ hR hS hDsq hclass hRcut hradius
  have hp_pos : ∀ p ∈ P, 0 < (p : Real) := by
    intro p hp
    exact_mod_cast (Finset.mem_filter.mp hp).2.1.pos
  have hprod_pos : (0 : Real) <
      ((∏ p ∈ P, p ^ (2 * valuationWeight R S p) : Nat) : Real) := by
    exact_mod_cast Finset.prod_pos (fun p hp => pow_pos
      (by exact_mod_cast hp_pos p hp : 0 < p) _)
  have hlog := Real.log_le_log hprod_pos (hb.1.trans hb.2)
  have hmass :
      Real.log ((∏ p ∈ P, p ^ (2 * valuationWeight R S p) : Nat) : Real) =
        ∑ p ∈ P, (2 * valuationWeight R S p : Nat) * Real.log (p : Real) := by
    simp only [Nat.cast_prod, Nat.cast_pow]
    rw [Real.log_prod]
    · simp_rw [Real.log_pow]
    · intro p hp
      exact ne_of_gt (pow_pos (hp_pos p hp) _)
  rw [hmass] at hlog
  exact hlog

/-- Empty local data contribute the unit, not a spurious prime factor. -/
theorem primePowerProduct_empty_control (z : Int) :
    ((∏ p ∈ (∅ : Finset Nat), p ^ (2 : Nat) : Nat) : Int) ∣ z := by
  simp

/-- A single registered factor is retained with its full exponent. -/
theorem primePowerProduct_singleton_control :
    ((∏ p ∈ ({3} : Finset Nat), p ^ (2 : Nat) : Nat) : Int) ∣ (9 : Int) := by
  norm_num

/-- Distinctness matters: two copies of the same prime cannot be multiplied
merely because each copy divides the target. -/
theorem duplicate_prime_product_false :
    ¬ (3 : Nat) ^ (2 : Nat) ∣ (3 : Nat) := by
  norm_num

end TenthDiscriminant
