import TenthDiscriminant.RankDivisorCompatibility
import TenthDiscriminant.EllipseResidueTransport

/-!
# Phase136: exact selected-minor saturation and the full-ellipse residue criterion

Both results concern the SAME original integer objects used by the
Phase134/135 interfaces. No prime-existence claim, new determinant
bound, or transport of a real metric into finite characteristic is used.

The maximal-minor statement is conditional on one normalized unit minor.
This is not yet the full Smith cokernel isomorphism over Z_(p).
-/

namespace TenthDiscriminant

open scoped BigOperators

/-- A selected maximal minor of the ORIGINAL observation matrix
equals the explicit extracted row factor times the corresponding
minor of its integral normalized quotient. This is an equality in Z,
not merely a p-adic congruence. -/
theorem selectedColumns_det_exact_factor {n m : Nat}
    (E C : Matrix (Fin n) (Fin m) Int)
    (U : Matrix (Fin n) (Fin n) Int)
    (p : Int) (k : Fin n → Nat)
    (hU : U.det = 1)
    (hfactor : U * E = Matrix.diagonal (fun i => p ^ k i) * C)
    (cols : Fin n → Fin m) :
    (selectedColumns E cols).det =
      p ^ (∑ i, k i) * (selectedColumns C cols).det := by
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
  exact hdet

/-- If a selected minor of integral NORMALIZED C is not divisible by p, the matching minor of the
ORIGINAL E has exactly the extracted power, and not one more.

For prime |p| this is a residue-unit witness. For composite |p|,
nondivisibility by p alone does NOT imply invertibility modulo p;
this theorem deliberately claims only the integer divisibility fact.
The cancellation over Z requires p != 0. -/
theorem selectedColumns_exact_power_of_not_dvd {n m : Nat}
    (E C : Matrix (Fin n) (Fin m) Int)
    (U : Matrix (Fin n) (Fin n) Int)
    (p : Int) (k : Fin n → Nat)
    (hp : p ≠ 0)
    (hU : U.det = 1)
    (hfactor : U * E = Matrix.diagonal (fun i => p ^ k i) * C)
    (cols : Fin n → Fin m)
    (hnot_dvd : ¬ p ∣ (selectedColumns C cols).det) :
    p ^ (∑ i, k i) ∣ (selectedColumns E cols).det ∧
      ¬ p ^ ((∑ i, k i) + 1) ∣ (selectedColumns E cols).det := by
  have hdet := selectedColumns_det_exact_factor E C U p k hU hfactor cols
  constructor
  · exact ⟨(selectedColumns C cols).det, hdet⟩
  · intro hmore
    obtain ⟨w, hw⟩ := hmore
    have heq :
        p ^ (∑ i, k i) * (selectedColumns C cols).det =
          p ^ (∑ i, k i) * (p * w) := by
      calc
        _ = (selectedColumns E cols).det := hdet.symm
        _ = (p ^ ((∑ i, k i) + 1)) * w := hw
        _ = p ^ (∑ i, k i) * (p * w) := by rw [pow_succ]; ring
    have hc : (selectedColumns C cols).det = p * w :=
      mul_left_cancel₀ (pow_ne_zero _ hp) heq
    exact hnot_dvd ⟨w, hc⟩

/-- Elementary integer divisibility cannot wrap around a modulus
larger than the coordinate difference. -/
private theorem small_dvd_zero {p v : Int}
    (hp : 0 < p) (hlow : -p < v) (hhigh : v < p)
    (hdvd : p ∣ v) : v = 0 := by
  rcases hdvd with ⟨t, rfl⟩
  by_cases ht : t = 0
  · simp [ht]
  · by_cases htpos : 0 < t
    · have hm : 0 ≤ p * (t - 1) :=
        mul_nonneg (le_of_lt hp) (by omega)
      nlinarith
    · have hm : 0 ≤ p * (-t - 1) :=
        mul_nonneg (le_of_lt hp) (by omega)
      nlinarith

/-- For the FULL symmetric integer ellipse, pairwise distinct
coordinate residues modulo p are equivalent to p > 2*rho.
The reverse implication uses coordinate bounds of the ORIGINAL
finite set, not a reduced or separated node selection. -/
theorem full_ellipse_coordinate_residues_distinct_iff
    (D rho p : Nat) (hD : 0 < D) (hp : 0 < p) :
    (∀ a ∈ ellipsePairs D rho, ∀ b ∈ ellipsePairs D rho,
        (p : Int) ∣ b.1 - a.1 →
        (p : Int) ∣ b.2 - a.2 → a = b) ↔ 2 * rho < p := by
  constructor
  · intro hdistinct
    by_contra hnot
    have hle : p ≤ 2 * rho := by omega
    obtain ⟨a, b, ha, hb, hne, hx, hy⟩ :=
      full_ellipse_axis_residue_collision D rho p hD hp hle
    exact hne (hdistinct a ha b hb hx hy)
  · intro hlarge
    have hlargeInt : (2 * (rho : Int)) < (p : Int) := by
      exact_mod_cast hlarge
    have hpInt : (0 : Int) < (p : Int) := by
      exact_mod_cast hp
    have hbox (u : Int × Int) (hu : u ∈ ellipsePairs D rho) :
        -(rho : Int) ≤ u.1 ∧ u.1 ≤ (rho : Int) ∧
          -(rho : Int) ≤ u.2 ∧ u.2 ≤ (rho : Int) := by
      change u ∈
        ((Finset.Icc (-(rho : Int)) (rho : Int)).product
          (Finset.Icc (-(rho : Int)) (rho : Int))).filter
          (fun z => z.1 ^ 2 + (D : Int) * z.2 ^ 2 ≤ (rho : Int) ^ 2) at hu
      obtain ⟨hx, hy⟩ := Finset.mem_product.mp (Finset.mem_filter.mp hu).1
      obtain ⟨hxlo, hxhi⟩ := Finset.mem_Icc.mp hx
      obtain ⟨hylo, hyhi⟩ := Finset.mem_Icc.mp hy
      exact ⟨hxlo, hxhi, hylo, hyhi⟩
    intro a ha b hb hx hy
    obtain ⟨haxlo, haxhi, haylo, hayhi⟩ := hbox a ha
    obtain ⟨hbxlo, hbxhi, hbylo, hbyhi⟩ := hbox b hb
    have hxzero : b.1 - a.1 = 0 :=
      small_dvd_zero hpInt (by omega) (by omega) hx
    have hyzero : b.2 - a.2 = 0 :=
      small_dvd_zero hpInt (by omega) (by omega) hy
    exact Prod.ext (by omega) (by omega)

end TenthDiscriminant
