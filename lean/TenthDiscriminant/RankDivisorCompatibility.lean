import TenthDiscriminant.RectangularBasisMatrix

/-!
# One integer observation matrix: divisor primes and rank-witness primes

The only new content is a generic integral matrix obstruction: if an
integer left row change extracts factors p^k from the SAME rectangular
observation matrix, then every maximal minor has p^(sum k) as a divisor.
A nonzero maximal minor modulo p therefore cannot coexist with positive
extraction weight. No auxiliary-prime existence or improved discriminant
cutoff is asserted by this module.

All matrices and column selection maps below are actual integer objects;
no substitute Gram or change in ordinary-jet observations is introduced.
-/

namespace TenthDiscriminant

open scoped BigOperators

/-- Select n columns of an n-by-m integer matrix. The column map need not
be injective: a repeated column simply has a zero determinant. -/
def selectedColumns {n m : Nat} (E : Matrix (Fin n) (Fin m) Int)
    (cols : Fin n → Fin m) : Matrix (Fin n) (Fin n) Int :=
  fun i j => E i (cols j)

/-- Selecting columns commutes with multiplication on the left. -/
theorem selectedColumns_mul_left {n m : Nat}
    (U : Matrix (Fin n) (Fin n) Int)
    (E : Matrix (Fin n) (Fin m) Int)
    (cols : Fin n → Fin m) :
    selectedColumns (U * E) cols = U * selectedColumns E cols := by
  ext i j
  simp [selectedColumns, Matrix.mul_apply]

/-- If the extraction is integral and the row change is unimodular,
**every** maximal minor of this very same E contains the full factor
p^(sum k). This avoids a rank-over-a-different-matrix substitution. -/
theorem all_maximal_minors_pow_dvd {n m : Nat}
    (E C : Matrix (Fin n) (Fin m) Int)
    (U : Matrix (Fin n) (Fin n) Int)
    (p : Int) (k : Fin n → Nat)
    (hU : U.det = 1)
    (hfactor : U * E = Matrix.diagonal (fun i => p ^ k i) * C)
    (cols : Fin n → Fin m) :
    p ^ (∑ i, k i) ∣ (selectedColumns E cols).det := by
  have hminor :
      U * selectedColumns E cols =
        Matrix.diagonal (fun i => p ^ k i) * selectedColumns C cols := by
    calc
      U * selectedColumns E cols = selectedColumns (U * E) cols :=
        (selectedColumns_mul_left U E cols).symm
      _ = selectedColumns (Matrix.diagonal (fun i => p ^ k i) * C) cols :=
        congrArg (fun M => selectedColumns M cols) hfactor
      _ = Matrix.diagonal (fun i => p ^ k i) * selectedColumns C cols :=
        selectedColumns_mul_left _ C cols
  have hdet := congrArg Matrix.det hminor
  simp only [Matrix.det_mul, Matrix.det_diagonal, hU, one_mul] at hdet
  have hpow : (∏ i, p ^ k i) = p ^ (∑ i, k i) := by
    simpa using (Finset.prod_pow_eq_pow_sum Finset.univ k p)
  rw [hpow] at hdet
  exact ⟨(selectedColumns C cols).det, hdet.symm⟩

/-- With positive extracted weight, each maximal minor is divisible
by p itself. It cannot simultaneously be a unit modulo p. This is
a divisibility statement, not (yet) a claim about a particular residue
field or an independently selected auxiliary inert prime. -/
theorem all_maximal_minors_p_dvd_of_weight_pos {n m : Nat}
    (E C : Matrix (Fin n) (Fin m) Int)
    (U : Matrix (Fin n) (Fin n) Int)
    (p : Int) (k : Fin n → Nat)
    (hU : U.det = 1)
    (hfactor : U * E = Matrix.diagonal (fun i => p ^ k i) * C)
    (hF : 0 < ∑ i, k i)
    (cols : Fin n → Fin m) :
    p ∣ (selectedColumns E cols).det := by
  obtain ⟨w, hw⟩ :=
    all_maximal_minors_pow_dvd E C U p k hU hfactor cols
  cases hsum : (∑ i, k i) with
  | zero => omega
  | succ t =>
    rw [hsum, pow_succ] at hw
    refine ⟨p ^ t * w, ?_⟩
    calc
      (selectedColumns E cols).det = (p ^ t * p) * w := hw
      _ = p * (p ^ t * w) := by ring

/-- There is necessarily a positive rectangular weight when the prime
is below the monomial width R and S contains at least two conjugate
powers. This is an exact all-range result, not a numerical sample. -/
theorem valuationWeight_pos_of_lt_R (R S p : Nat)
    (hp : 0 < p) (hpR : p < R) (hS : 2 ≤ S) :
    0 < valuationWeight R S p := by
  have hself : p / p = 1 := Nat.div_self hp
  have hSone : (1 : Nat) ∈ Finset.range S := Finset.mem_range.mpr (by omega)
  have hs : 1 ≤ (∑ t ∈ Finset.range S, min (p / p) t) := by
    have hterm : min (p / p) 1 = 1 := by simp [hself]
    have hle : min (p / p) 1 ≤
        (∑ t ∈ Finset.range S, min (p / p) t) :=
      Finset.single_le_sum (fun _ _ => Nat.zero_le _) hSone
    omega
  have hr : (∑ t ∈ Finset.range S, min (p / p) t) ≤
      (∑ r ∈ Finset.range R, ∑ t ∈ Finset.range S, min (r / p) t) :=
    Finset.single_le_sum (fun _ _ => Nat.zero_le _)
      (Finset.mem_range.mpr hpR)
  change 0 < (∑ r ∈ Finset.range R, ∑ t ∈ Finset.range S, min (r / p) t)
  omega

/-- The repository's explicit rectangular basis has determinant one.
Whenever its pointwise integral row factor exists on an observation
matrix E, every maximal minor contains p^F(R,S,p). -/
theorem rectangular_all_maximal_minors_pow_dvd
    (R S m p : Nat) (hp : 0 < p)
    (E C : Matrix (Fin (R * S)) (Fin m) Int)
    (hfactor : rectangularBasisMatrix R S p * E =
      Matrix.diagonal (fun i => (p : Int) ^
        rectangularBasisExponent R S p i) * C)
    (cols : Fin (R * S) → Fin m) :
    (p : Int) ^ valuationWeight R S p ∣
      (selectedColumns E cols).det := by
  simpa only [sum_rectangularBasisExponent] using
    all_maximal_minors_pow_dvd E C (rectangularBasisMatrix R S p)
      (p : Int) (rectangularBasisExponent R S p)
      (rectangularBasisMatrix_det R S p hp) hfactor cols

/-- Small-prime incompatibility for the same rectangular observations:
if 0<p<R and S>=2, a positive row weight forces EVERY maximal minor
of E to be divisible by p. Thus the same prime cannot witness
a nonzero maximal minor modulo p. -/
theorem rectangular_all_maximal_minors_p_dvd
    (R S m p : Nat) (hp : 0 < p) (hpR : p < R)
    (hS : 2 ≤ S)
    (E C : Matrix (Fin (R * S)) (Fin m) Int)
    (hfactor : rectangularBasisMatrix R S p * E =
      Matrix.diagonal (fun i => (p : Int) ^
        rectangularBasisExponent R S p i) * C)
    (cols : Fin (R * S) → Fin m) :
    (p : Int) ∣ (selectedColumns E cols).det := by
  have hweight :
      0 < ∑ i, rectangularBasisExponent R S p i := by
    simpa only [sum_rectangularBasisExponent] using
      valuationWeight_pos_of_lt_R R S p hp hpR hS
  exact all_maximal_minors_p_dvd_of_weight_pos E C
    (rectangularBasisMatrix R S p) (p : Int)
    (rectangularBasisExponent R S p)
    (rectangularBasisMatrix_det R S p hp) hfactor hweight cols

/-- Historical 4-by-2 negative-control boundary: p=3 contributes
one weight if R=4, and none if R=3. -/
theorem rectangular_rank_weight_pilot :
    valuationWeight 4 2 3 = 1 ∧ valuationWeight 3 2 3 = 0 := by
  decide

end TenthDiscriminant
