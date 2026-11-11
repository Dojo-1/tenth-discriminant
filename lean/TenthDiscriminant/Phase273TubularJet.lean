import TenthDiscriminant.Phase272JetDescent

/-!
# Phase273 — first-order p-adic tubular jet recovery, source-exact tests

The *paper* theorem has scope all integer polynomials and all primes:
at modulus p², translation by p is determined by the first J ordinary
derivatives for arbitrary polynomial degrees iff J >= p. This module
checks a bounded original-source instance at (p,J)=(3,3) and the hostile
J=2 boundary; it does NOT formalize the universal paper theorem.

W is HELD FIXED in ordinary Z differentiation, and the point lies
on the original integer-pair real axis. Changing a real-axis observation
also changes W; the existing Phase204 two-sided tube handles that
additional row-direction term.
-/
namespace TenthDiscriminant.Phase273
set_option autoImplicit false

/-- A truncated ordinary derivative vector for the source monomial
Z^r W^0 at a real-axis integer pair (a,0), reduced modulo nine. -/
def ordinary3 (a : Int) (r : Nat) : Fin 3 → ZMod 9 :=
  fun j => ((integerDerivativeRow 19 r 0 j.val (a, 0)).1 : ZMod 9)

/-- The p=3, mod p² local translation: Id + 3 * depth-shift.
Missing high jets can vanish at this precision only at adequate depth. -/
def nearStep3 (v : Fin 3 → ZMod 9) : Fin 3 → ZMod 9 :=
  ![v 0 + 3 * v 1, v 1 + 3 * v 2, v 2]

/-- Exact original-source calculation for monomials through degree nine,
including degrees far greater than the retained derivative count. -/
theorem local_source_transport_monomials :
    ∀ r : Fin 10,
      nearStep3 (ordinary3 0 r.val) = ordinary3 3 r.val := by
  intro r
  funext j
  fin_cases r <;> fin_cases j <;> decide

/-- Two depth-one jets cannot reconstruct the moved quadratic.
The source polynomial Z² has zero first two ordinary jets at zero,
but its first derivative after a shift by three equals six mod nine. -/
def ordinary2 (a : Int) (r : Nat) : Fin 2 → ZMod 9 :=
  fun j => ((integerDerivativeRow 19 r 0 j.val (a, 0)).1 : ZMod 9)

theorem insufficient_depth2_zero :
    ordinary2 0 2 = (fun _ => 0) := by
  funext j
  fin_cases j <;> decide

theorem insufficient_depth2_witness :
    ordinary2 3 2 (1 : Fin 2) = 6 := by decide

theorem no_mod_nine_two_jet_transport
    (F : (Fin 2 → ZMod 9) → (Fin 2 → ZMod 9))
    (hzero : F (fun _ => 0) = (fun _ => 0))
    (hquadratic : F (ordinary2 0 2) = ordinary2 3 2) :
    False := by
  rw [insufficient_depth2_zero, hzero] at hquadratic
  have hbad : (fun _ : Fin 2 => (0 : ZMod 9)) ≠ ordinary2 3 2 := by
    intro h
    have hh := congrArg (fun f : Fin 2 → ZMod 9 => f 1) h
    have ht : (0 : ZMod 9) ≠ ordinary2 3 2 1 := by
      rw [insufficient_depth2_witness]
      decide
    exact ht hh
  exact hbad hquadratic

#print axioms TenthDiscriminant.Phase273.local_source_transport_monomials
#print axioms TenthDiscriminant.Phase273.no_mod_nine_two_jet_transport
end TenthDiscriminant.Phase273
