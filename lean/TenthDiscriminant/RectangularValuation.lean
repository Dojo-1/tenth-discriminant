import TenthDiscriminant.Arithmetic
import TenthDiscriminant.IntegerTraceGram
import TenthDiscriminant.GramDivisibility

/-!
# The exact exponent required by Ender's rectangular determinant

The mathematical construction of a unimodular polynomial basis is an
explicit hypothesis here. This module proves that its proposed row
weights sum to *the existing* `valuationWeight`, then applies the
generic two-sided determinant theorem to the actual integer Gram.
-/
namespace TenthDiscriminant

/-- The exponent assigned to one row `(r,s)` by the proposed basis
`Z^(r-pk) W^s (Z^p-W)^k`, in the original row-major indexing. -/
def rectangularBasisExponent (R S p : Nat) (i : Fin (R * S)) : Nat :=
  let rs := (finProdFinEquiv : Fin R × Fin S ≃ Fin (R * S)).symm i
  min (rs.1.val / p) (S - 1 - rs.2.val)

theorem rectangularBasisExponent_eq (R S p : Nat) (i : Fin (R * S)) :
    rectangularBasisExponent R S p i =
      min ((i.val / S) / p) (S - 1 - i.val % S) := by
  rfl

/-- Reflection of the `s` coordinate turns the basis exponent sum into
Ender's previously defined `F(p)`, even for empty rectangles. -/
theorem sum_rectangularBasisExponent (R S p : Nat) :
    (∑ i : Fin (R * S), rectangularBasisExponent R S p i) =
      valuationWeight R S p := by
  have he := Fintype.sum_equiv
    (finProdFinEquiv : Fin R × Fin S ≃ Fin (R * S))
    (fun rs => rectangularBasisExponent R S p (finProdFinEquiv rs))
    (rectangularBasisExponent R S p) (fun _ => rfl)
  rw [← he]
  simp only [rectangularBasisExponent, Equiv.symm_apply_apply,
    Fintype.sum_prod_type, valuationWeight, Finset.sum_fin_eq_sum_range]
  apply Finset.sum_congr rfl
  intro r hr
  have hrR : r < R := Finset.mem_range.mp hr
  have hremove :
      (∑ x ∈ Finset.range S,
        if h : x < S then min (r / p) (S - 1 - x) else 0) =
        ∑ x ∈ Finset.range S, min (r / p) (S - 1 - x) := by
    apply Finset.sum_congr rfl
    intro x hx
    simp [Finset.mem_range.mp hx]
  simpa only [dif_pos hrR, hremove] using
    (Finset.sum_range_reflect (fun t => min (r / p) t) S)

/-- In the `4 × 2`, `p=3` pilot, only row `(3,0)` receives one factor;
the top `s=1` row receives none. -/
theorem rectangularBasisExponent_pilot :
    rectangularBasisExponent 4 2 3 6 = 1 ∧
      rectangularBasisExponent 4 2 3 7 = 0 := by
  decide

/-- Exact Ender exponent for the *same* integer Gram matrix, once the
concrete integral polynomial basis and quotient-jet matrix have been
constructed. This hypothesis is not supplied by inertness here. -/
theorem rectangularTraceGram_valuation_of_basis_factor
    (Q : Finset (Int × Int)) (D J R S p : Nat)
    (U K : Matrix (Fin (R * S)) (Fin (R * S)) Int)
    (hU : U.det = 1)
    (hfactor : U * integerRectangularTraceGram Q D J R S * U.transpose =
      Matrix.diagonal (fun i => (p : Int) ^ rectangularBasisExponent R S p i) *
        K * Matrix.diagonal
          (fun i => (p : Int) ^ rectangularBasisExponent R S p i)) :
    (p : Int) ^ (2 * valuationWeight R S p) ∣
      (integerRectangularTraceGram Q D J R S).det := by
  simpa only [sum_rectangularBasisExponent] using
    pow_dvd_det_of_unimodular_gram_factor
      (integerRectangularTraceGram Q D J R S) U K (p : Int)
      (rectangularBasisExponent R S p) hU hfactor

end TenthDiscriminant
