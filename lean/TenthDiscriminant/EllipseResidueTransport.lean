import TenthDiscriminant.LatticeEllipse
import TenthDiscriminant.JetPower

/-!
# The unchanged ellipse and the ordinary-jet residue boundary

The full (symmetric) integer ellipse contains two distinct horizontal
axis nodes with equal coordinate residues modulo every 0 < p <= 2*rho.
This is a necessary-condition obstruction to applying a proof whose
node set must be pairwise distinct modulo p. It does NOT obstruct the
competitor's separated subset, nor prove anything about its normalized
matrix. The ordinary-vs-Hasse control records an independent column
normalization boundary. Neither lemma changes the determinant cutoff.
-/

namespace TenthDiscriminant

open Polynomial

/-- For any nonzero modulus at most twice the radius, the ORIGINAL
full ellipse contains two DISTINCT nodes congruent in both integer
coordinates. The explicit witnesses are (-rho,0) and (p-rho,0).

This strengthens the earlier p <= rho observation to the exact axis
threshold p <= 2*rho. No prime, field, or class-number assumption is
needed for this elementary geometric obstruction. -/
theorem full_ellipse_axis_residue_collision (D rho p : Nat)
    (hD : 0 < D) (hp : 0 < p) (hpr : p <= 2 * rho) :
    exists a b : Int × Int,
      a ∈ ellipsePairs D rho ∧ b ∈ ellipsePairs D rho ∧ a ≠ b ∧
      (p : Int) ∣ b.1 - a.1 ∧ (p : Int) ∣ b.2 - a.2 := by
  let a : Int × Int := (-(rho : Int), 0)
  let b : Int × Int := ((p : Int) - (rho : Int), 0)
  have hpInt : (0 : Int) < (p : Int) := by exact_mod_cast hp
  have hprInt : (p : Int) <= 2 * (rho : Int) := by exact_mod_cast hpr
  have hprod : (0 : Int) <= (p : Int) * (2 * (rho : Int) - (p : Int)) :=
    mul_nonneg (by omega) (by omega)
  have hinside : ((p : Int) - (rho : Int)) ^ 2 <= (rho : Int) ^ 2 := by
    nlinarith
  have ha : a ∈ ellipsePairs D rho := by
    apply (mem_ellipsePairs_iff D rho hD _ _).2
    simp [a]
  have hb : b ∈ ellipsePairs D rho := by
    apply (mem_ellipsePairs_iff D rho hD _ _).2
    simpa [b] using hinside
  refine ⟨a, b, ha, hb, ?_, ?_, ?_⟩
  · intro hab
    have heq := congrArg Prod.fst hab
    dsimp [a, b] at heq
    omega
  · change (p : Int) ∣ ((p : Int) - (rho : Int)) - (-(rho : Int))
    convert (dvd_refl (p : Int)) using 1 <;> ring
  · change (p : Int) ∣ (0 : Int) - (0 : Int)
    simp

/-- Exact small *inert-prime* scenario for the unchanged ellipse:
D=19 and p=3. This is a residue-node collision, not a claim that
the original polynomial-jet matrix is rank deficient. -/
theorem full_ellipse_19_5_mod_three_control :
    exists a b : Int × Int,
      a ∈ ellipsePairs 19 5 ∧ b ∈ ellipsePairs 19 5 ∧ a ≠ b ∧
      (3 : Int) ∣ b.1 - a.1 ∧ (3 : Int) ∣ b.2 - a.2 := by
  exact full_ellipse_axis_residue_collision 19 5 3
    (by decide) (by decide) (by decide)

/-- The order-three ordinary jet of X^3 is divisible by three,
whereas the Hasse/Taylor coefficient jet is NOT. Thus the factorial
column map is not invertible modulo three at j=3. -/
theorem cubic_ordinary_hasse_mod_three_control :
    (3 : Int) ∣
      ((Polynomial.derivative^[3] (Polynomial.X ^ 3 : Polynomial Int)).eval 0) ∧
    ¬ (3 : Int) ∣
      ((Polynomial.hasseDeriv 3 (Polynomial.X ^ 3 : Polynomial Int)).eval 0) := by
  constructor
  · exact dvd_iterate_derivative_pow Polynomial.X 3 0 (by decide)
  · exact hasse_derivative_negative_control

end TenthDiscriminant
