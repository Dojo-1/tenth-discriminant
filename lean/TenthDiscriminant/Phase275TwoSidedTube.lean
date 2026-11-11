import TenthDiscriminant.Phase273TubularJet

/-!
# Phase275 — two-sided integer-pair tube transport on original ordinary Z jets

This is a finite original-source Lean regression of the existing Phase204
paper/Python two-sided tube, not a new universal or class-number theorem.
The j-th original Z derivative is taken with W held fixed. When moving
a real-axis observation by u=3, BOTH Z and W change by +3.

Prime 3 is inert in Q(sqrt(-7)) and split in Q(sqrt(-11)).
Both controls are deliberately included: the near-identity transport
does NOT rely on inertness and must not be counted as a Frobenius divisor.

The transformed observation is not asserted to preserve the entire
production ellipse, its weights, or the determinant of the Gram.
-/

namespace TenthDiscriminant.Phase275
set_option autoImplicit false
set_option maxRecDepth 4500
set_option maxHeartbeats 0

/-- Reduce both original integer-pair channels modulo p² = 9. -/
def row9 (D r s j : Nat) (z : Int × Int) : ZMod 9 × ZMod 9 :=
  let v := integerDerivativeRow D r s j z
  ((v.1 : ZMod 9), (v.2 : ZMod 9))

def add9 (x y : ZMod 9 × ZMod 9) : ZMod 9 × ZMod 9 :=
  (x.1+y.1,x.2+y.2)

def scale9 (k : ZMod 9) (x : ZMod 9 × ZMod 9) :
    ZMod 9 × ZMod 9 := (k*x.1,k*x.2)

/-- First-order simultaneous translation of Z and W at modulus nine.
The unavailable third ordinary Z jet is deliberately omitted when j=2;
3*partial_Z^3 is zero mod 9 by the factorial theorem. -/
def tube9 (D r s j : Nat) (z : Int × Int) : ZMod 9 × ZMod 9 :=
  let nextZ : ZMod 9 × ZMod 9 :=
    if j + 1 < 3 then row9 D r s (j+1) z else (0,0)
  let lowerW : ZMod 9 × ZMod 9 :=
    if s = 0 then (0,0) else row9 D r (s-1) j z
  add9 (row9 D r s j z)
    (scale9 3 (add9 nextZ (scale9 (s : ZMod 9) lowerW)))

/-- Inert-prime control: -7 is a nonsquare modulo three. The real and
imaginary integer-pair channels are compared, not merely the real part. -/
theorem inert_7_two_sided_source
    (r : Fin 4) (s : Fin 3) (j : Fin 3) :
    row9 7 r.val s.val j.val (4,1) =
      tube9 7 r.val s.val j.val (1,1) := by
  fin_cases r <;> fin_cases s <;> fin_cases j <;> decide

/-- Split-prime control: -11 is a square modulo three.
The same transport must work even though inertness is absent. -/
theorem split_11_two_sided_source
    (r : Fin 4) (s : Fin 3) (j : Fin 3) :
    row9 11 r.val s.val j.val (4,1) =
      tube9 11 r.val s.val j.val (1,1) := by
  fin_cases r <;> fin_cases s <;> fin_cases j <;> decide

/-- A nontrivial W-containing polynomial from ORIGINAL source rows:
F(Z,W) = Z^2 W - 2 Z W + W = (Z-1)^2 W. -/
def quadraticWRealJet (j : Nat) (z : Int × Int) : ZMod 9 :=
  (row9 7 2 1 j z).1 - 2*(row9 7 1 1 j z).1 +
     (row9 7 0 1 j z).1

theorem quadraticW_two_jet_at_origin :
    quadraticWRealJet 0 (1,0) = 0 ∧
    quadraticWRealJet 1 (1,0) = 0 := by decide

theorem quadraticW_two_jet_after_movement :
    quadraticWRealJet 1 (4,0) = 6 := by decide

/-- Even allowing an arbitrary nonlinear function on reduced two-jets,
movement cannot reconstruct all source polynomials at depth J=2.
The zero polynomial and F=(Z-1)^2 W have equal first two jets at
z=(1,0), but different derivatives at the translated z=(4,0). -/
theorem no_two_jet_two_sided_descent
    (T : (Fin 2 → ZMod 9) → (Fin 2 → ZMod 9))
    (hzero : T (fun _ => 0) = (fun _ => 0))
    (hpoly : T (fun i => quadraticWRealJet i.val (1,0)) =
         (fun i => quadraticWRealJet i.val (4,0))) :
    False := by
  have hbefore : (fun i : Fin 2 => quadraticWRealJet i.val (1,0))
       = (fun _ => (0 : ZMod 9)) := by
    funext i
    fin_cases i
    · exact quadraticW_two_jet_at_origin.1
    · exact quadraticW_two_jet_at_origin.2
  rw [hbefore, hzero] at hpoly
  have hcomponent := congrArg
    (fun f : Fin 2 → ZMod 9 => f 1) hpoly
  have htarget : (0 : ZMod 9) ≠ quadraticWRealJet 1 (4,0) := by
    rw [quadraticW_two_jet_after_movement]
    decide
  exact htarget hcomponent

#print axioms TenthDiscriminant.Phase275.inert_7_two_sided_source
#print axioms TenthDiscriminant.Phase275.split_11_two_sided_source
#print axioms TenthDiscriminant.Phase275.no_two_jet_two_sided_descent
end TenthDiscriminant.Phase275
