import TenthDiscriminant.Phase223Horizontal
import TenthDiscriminant.EllipseUpperCount

/-!
# Phase225: inert horizontal band vanishing on the ORIGINAL full ellipse

The residue value below is the evaluation of the integer monic band
polynomial H(W) = (W^p-W) * product_{1<=b<=Y}
  ((W^p-W)^2 + 4*D*b^2)
in the actual quadratic-residue ring from ResidueTraceGram.

This proves the complete modular pointwise vanishing on the same
unduplicated original ellipse support. The lifting to integer Zsqrtd
divisibility, ordinary-Z-jet action, combined unimodular source basis,
and determinant factor are SEPARATE obligations, not assumed here.
-/

namespace TenthDiscriminant.Phase225

open TenthDiscriminant

/-- Residue evaluation of the finite horizontal annihilator. It
retains the distinct y=0 and |y|=b factors instead of a scalar
substitution for the source's quadratic residue arithmetic. -/
def residueBandValue (D p Y : Nat) (a : QuadraticResidue D p) :
    QuadraticResidue D p :=
  (a ^ p - a) *
    (Finset.Icc (1 : Nat) Y).prod (fun b : Nat =>
      (a ^ p - a) ^ 2 +
        QuadraticResidue.scalar D p
          (4 * (D : ZMod p) * (b : ZMod p) ^ 2))

/-- The horizontal factor vanishes whenever the imaginary coordinate
lies in the squared residue orbit of a level b between 0 and Y. -/
theorem residueBandValue_zero_of_im_sq
    (D p Y b : Nat) [Fact p.Prime]
    (hp2 : p ≠ 2) (hnonsquare : ¬ IsSquare (-(D : ZMod p)))
    (a : QuadraticResidue D p) (hb : b ≤ Y)
    (hsq : a.im ^ 2 = (b : ZMod p) ^ 2) :
    residueBandValue D p Y a = 0 := by
  by_cases hb0 : b = 0
  · subst b
    have hsq0 : a.im ^ 2 = 0 := by simpa using hsq
    have him0 : a.im = 0 := by
      simpa only [sq_eq_zero_iff] using hsq0
    have hfixed : a ^ p = a := by
      rw [Phase223.residue_frobenius_conj D p hp2 hnonsquare a]
      apply QuadraticResidue.ext
      · rfl
      · simp [him0]
    simp [residueBandValue, hfixed]
  · have hbpos : 1 ≤ b := by omega
    have hfactor :
        (a ^ p - a) ^ 2 +
            QuadraticResidue.scalar D p
              (4 * (D : ZMod p) * (b : ZMod p) ^ 2) = 0 := by
      have h := Phase223.residue_horizontal_quadratic_factor D p
        hp2 hnonsquare a
      rwa [hsq] at h
    have hprod :
        (Finset.Icc (1 : Nat) Y).prod (fun c : Nat =>
          (a ^ p - a) ^ 2 +
            QuadraticResidue.scalar D p
              (4 * (D : ZMod p) * (c : ZMod p) ^ 2)) = 0 := by
      apply Finset.prod_eq_zero (Finset.mem_Icc.mpr ⟨hbpos, hb⟩)
      exact hfactor
    unfold residueBandValue
    rw [hprod]
    simp

/-- Interpret the sample as the actual conjugate coordinate (x,-y).
The sign choice is explicit; no absolute-value division or Hasse jet. -/
theorem residueBandValue_zero_signed_integer_pair
    (D p Y b : Nat) [Fact p.Prime]
    (hp2 : p ≠ 2) (hnonsquare : ¬ IsSquare (-(D : ZMod p)))
    (x y : Int) (hb : b ≤ Y)
    (hy : y = (b : Int) ∨ y = -(b : Int)) :
    residueBandValue D p Y
      (QuadraticResidue.ofPair D p
        ((x : ZMod p), -(y : ZMod p))) = 0 := by
  apply residueBandValue_zero_of_im_sq D p Y b hp2 hnonsquare
    (QuadraticResidue.ofPair D p ((x : ZMod p), -(y : ZMod p))) hb
  rcases hy with hy | hy
  · simp [QuadraticResidue.ofPair, hy]
  · simp [QuadraticResidue.ofPair, hy]

/-- All ORIGINAL integer ellipse points are annihilated at their
conjugate residue coordinates. The vertical bound is the repository's
exact floor(rho / sqrt(D)), not an invented geometric sample set. -/
theorem residueBandValue_zero_original_ellipse
    (D p rho : Nat) [Fact p.Prime]
    (hD : 0 < D) (hp2 : p ≠ 2)
    (hnonsquare : ¬ IsSquare (-(D : ZMod p)))
    (q : Int × Int) (hq : q ∈ ellipsePairs D rho) :
    residueBandValue D p (ellipseVerticalBound D rho)
      (QuadraticResidue.ofPair D p
        ((q.1 : ZMod p), -(q.2 : ZMod p))) = 0 := by
  obtain ⟨hlo, hhi⟩ := ellipse_pair_y_bounds D rho hD q hq
  by_cases hy : 0 ≤ q.2
  · exact residueBandValue_zero_signed_integer_pair D p
      (ellipseVerticalBound D rho) q.2.toNat hp2 hnonsquare
      q.1 q.2 (by omega) (Or.inl (by omega))
  · exact residueBandValue_zero_signed_integer_pair D p
      (ellipseVerticalBound D rho) (-q.2).toNat hp2 hnonsquare
      q.1 q.2 (by omega) (Or.inr (by omega))

/-- Same original full-ellipse regression as Phase223's 49-residue
support count; the nonsquare condition is itself checked in ZMod 13. -/
theorem original_19_13_9_band_control
    (q : Int × Int) (hq : q ∈ ellipsePairs 19 9) :
    residueBandValue 19 13 (ellipseVerticalBound 19 9)
      (QuadraticResidue.ofPair 19 13
        ((q.1 : ZMod 13), -(q.2 : ZMod 13))) = 0 := by
  letI : Fact (Nat.Prime 13) := ⟨by decide⟩
  have hns : ¬ IsSquare (-(19 : ZMod 13)) := by decide
  exact residueBandValue_zero_original_ellipse 19 13 9
    (by decide) (by decide) hns q hq

/-- A real negative control: split p=3, D=2 does not satisfy the
inert Frobenius-conjugation identity on the quadratic generator. -/
theorem split_frobenius_negative_control :
    residuePairPow 2 3 (0, 1) 3 ≠
      residuePairConj ((0, 1) : ZMod 3 × ZMod 3) := by
  decide

end TenthDiscriminant.Phase225

#print axioms TenthDiscriminant.Phase225.residueBandValue_zero_of_im_sq
#print axioms TenthDiscriminant.Phase225.residueBandValue_zero_signed_integer_pair
#print axioms TenthDiscriminant.Phase225.residueBandValue_zero_original_ellipse
#print axioms TenthDiscriminant.Phase225.original_19_13_9_band_control
#print axioms TenthDiscriminant.Phase225.split_frobenius_negative_control
