import Mathlib

/-!
# Exact derivative-row moment identities
The rows and real trace product are the complex formulation of
`tools/verify_exact.py:gram`, with an explicit derivative cutoff.
No symmetry, angular averaging, nonzero-point assumption or rank assertion
is used. Identification of the entire integer implementation, divisibility
and interpolation/nonvanishing remain separate obligations.
-/
namespace TenthDiscriminant
open scoped ComplexConjugate

noncomputable def derivativeRow (r s j : Nat) (z : Complex) : Complex :=
  if j <= r then ((r.descFactorial j : Real) : Complex) * z^(r-j) * (conj z)^s
  else 0

noncomputable def normMoment (P : Finset Complex) (k : Nat) : Real :=
  P.sum (fun z => Complex.normSq z ^ k)

noncomputable def traceGramEntry (P : Finset Complex) (J r s t u : Nat) : Real :=
  2 * (Finset.range J).sum (fun j =>
    P.sum (fun z => (derivativeRow r s j z * conj (derivativeRow t u j z)).re))

theorem monomial_normSq (c : Real) (z : Complex) (a b : Nat) :
    Complex.normSq ((c : Complex)*z^a*(conj z)^b) =
      c^2 * Complex.normSq z^(a+b) := by
  simp only [map_mul, map_pow, Complex.normSq_ofReal, Complex.normSq_conj, pow_add]
  ring

theorem paired_monomial_product (c d : Real) (z : Complex) (a b : Nat) :
    ((c : Complex)*z^a*(conj z)^b) *
      conj ((d : Complex)*z^(a+1)*(conj z)^(b+1)) =
      ((c*d*Complex.normSq z^(a+b+1) : Real) : Complex) := by
  calc
    _ = (c : Complex)*(d : Complex)*(z*conj z)^(a+b+1) := by
      simp [map_mul, map_pow, pow_add, pow_succ, mul_pow] <;> ring
    _ = _ := by
      rw [Complex.mul_conj]
      push_cast
      ring

theorem row_diagonal (r s j : Nat) (z : Complex) :
    (derivativeRow r s j z * conj (derivativeRow r s j z)).re =
      if j <= r then (r.descFactorial j : Real)^2 * Complex.normSq z^(r+s-j)
      else 0 := by
  by_cases hj : j <= r
  · simp only [derivativeRow, if_pos hj]
    rw [Complex.mul_conj, Complex.ofReal_re, monomial_normSq]
    have he : r-j+s = r+s-j := by omega
    rw [he]
  · simp [derivativeRow, hj]

theorem row_radial_cross (r s j : Nat) (z : Complex) :
    (derivativeRow r s j z * conj (derivativeRow (r+1) (s+1) j z)).re =
      if j <= r then (r.descFactorial j : Real)*((r+1).descFactorial j : Real)*
        Complex.normSq z^(r+s+1-j)
      else 0 := by
  by_cases hj : j <= r
  · have hj1 : j <= r+1 := by omega
    have he : r+1-j = (r-j)+1 := by omega
    simp only [derivativeRow, if_pos hj, if_pos hj1]
    rw [he, paired_monomial_product, Complex.ofReal_re]
    have hexp : r-j+s+1 = r+s+1-j := by omega
    rw [hexp]
  · simp [derivativeRow, hj]

/-- Full diagonal, including the successor row's extra derivative column. -/
theorem traceGram_diagonal (P : Finset Complex) (J r s : Nat) :
    traceGramEntry P J r s r s =
      2 * (Finset.range J).sum (fun j =>
        if j <= r then (r.descFactorial j : Real)^2 * normMoment P (r+s-j) else 0) := by
  unfold traceGramEntry
  congr 1
  apply Finset.sum_congr rfl
  intro j hj
  simp_rw [row_diagonal]
  by_cases h : j <= r
  · simp [h, normMoment, Finset.mul_sum]
  · simp [h]

/-- Exact cross entry; its cutoff is r, not r+1. -/
theorem traceGram_radial_cross (P : Finset Complex) (J r s : Nat) :
    traceGramEntry P J r s (r+1) (s+1) =
      2 * (Finset.range J).sum (fun j =>
        if j <= r then (r.descFactorial j : Real)*((r+1).descFactorial j : Real)*
          normMoment P (r+s+1-j) else 0) := by
  unfold traceGramEntry
  congr 1
  apply Finset.sum_congr rfl
  intro j hj
  simp_rw [row_radial_cross]
  by_cases h : j <= r
  · simp [h, normMoment, Finset.mul_sum]
  · simp [h]

noncomputable def latticePoint (D : Real) (x y : Int) : Complex :=
  ((x : Real) : Complex) + (((y : Real)*Real.sqrt D : Real) : Complex)*Complex.I

theorem latticePoint_normSq (D : Real) (hD : 0 <= D) (x y : Int) :
    Complex.normSq (latticePoint D x y) = (x : Real)^2 + D*(y : Real)^2 := by
  rw [latticePoint, Complex.normSq_add_mul_I, mul_pow, Real.sq_sqrt hD]
  ring

/-- The origin is retained and zeroth powers are not accidentally discarded. -/
theorem traceGram_origin_control :
    traceGramEntry {0} 2 0 0 0 0 = 2 := by
  norm_num [traceGramEntry, derivativeRow, Finset.sum_range_succ, Nat.descFactorial]

/-- The j=1 contribution in the successor diagonal is nonzero at z=1. -/
theorem traceGram_unmatched_column_control :
    traceGramEntry {1} 2 1 1 1 1 = 4 := by
  norm_num [traceGramEntry, derivativeRow, Finset.sum_range_succ, Nat.descFactorial]

/-- The corresponding cross term has no j=1 contribution. -/
theorem traceGram_cross_cutoff_control :
    traceGramEntry {1} 2 0 0 1 1 = 2 := by
  norm_num [traceGramEntry, derivativeRow, Finset.sum_range_succ, Nat.descFactorial]

end TenthDiscriminant
