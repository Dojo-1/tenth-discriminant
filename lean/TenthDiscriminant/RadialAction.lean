import TenthDiscriminant.RadialOperator

/-! The actual radial matrices form an additive integer action on observations. -/
namespace TenthDiscriminant.RadialAction
open Polynomial Matrix
open scoped BigOperators Classical
set_option autoImplicit false
noncomputable section

private theorem polynomial_composition {A : Type*} [CommRing A]
    (R S : Nat) (a b : Int) (i : Fin (R*S)) (w : A) :
    ∑ h : Fin (R*S), RadialOperator.matrix R S a i h •
      RadialOperator.polynomial b w (h.val/S) (h.val%S) =
      RadialOperator.polynomial (a+b) w (i.val/S) (i.val%S) := by
  rw [RadialOperator.row_action]
  let r := i.val/S
  let s := i.val%S
  let m := min r s
  have hmr : m ≤ r := min_le_left _ _
  have hms : m ≤ s := min_le_right _ _
  have term (t : Nat) (ht : t ≤ m) :
      RadialOperator.polynomial b w
        ((RadialOperator.targetFin R S i t).val/S)
        ((RadialOperator.targetFin R S i t).val%S) =
      X^(r-m)*C w^(s-m)*(X*C w-C (b : A))^(m-t) := by
    obtain ⟨hr,hs⟩ := RadialOperator.targetFin_labels R S i t ht
    rw [hr,hs]
    change RadialOperator.polynomial b w (r-t) (s-t) = _
    have hm : min (r-t) (s-t)=m-t := by dsimp [m]; omega
    have hr' : r-t-(m-t)=r-m := by omega
    have hs' : s-t-(m-t)=s-m := by omega
    unfold RadialOperator.polynomial
    rw [hm,hr',hs']
  change (∑ t ∈ Finset.range (m+1),
    ((-a)^t*(m.choose t : Int)) •
      RadialOperator.polynomial b w
        ((RadialOperator.targetFin R S i t).val/S)
        ((RadialOperator.targetFin R S i t).val%S)) =
      RadialOperator.polynomial (a+b) w r s
  have hrad : (-C (a : A))+(X*C w-C (b : A)) =
      X*C w-C ((a+b : Int) : A) := by simp only [Int.cast_add,map_add]; ring
  calc
    _ = ∑ t ∈ Finset.range (m+1),
        ((-a)^t*(m.choose t : Int)) •
          (X^(r-m)*C w^(s-m)*(X*C w-C (b : A))^(m-t)) := by
      apply Finset.sum_congr rfl
      intro t ht
      rw [term t (by have := Finset.mem_range.mp ht; omega)]
    _ = X^(r-m)*C w^(s-m)*((-C (a : A))+(X*C w-C (b : A)))^m := by
      rw [add_pow,Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro t ht
      rw [zsmul_eq_mul]
      have hc : (((-a)^t*(m.choose t : Int) : Int) : A[X]) =
          (-C (a : A))^t*(m.choose t : A[X]) := by simp
      rw [hc]
      ring
    _ = _ := by rw [hrad]; rfl

private theorem row_coeff (R S : Nat) (v : Fin (R*S) → Int) (i : Fin (R*S)) :
    ((∑ h : Fin (R*S), v h •
      (X^(h.val/S)*C (X : Polynomial Int)^(h.val%S) : Polynomial (Polynomial Int))).coeff
        (i.val/S)).coeff (i.val%S) = v i := by
  have mono (h : Fin (R*S)) :
      ((X^(h.val/S)*C (X : Polynomial Int)^(h.val%S) :
        Polynomial (Polynomial Int)).coeff (i.val/S)).coeff (i.val%S) =
        if h=i then 1 else 0 := by
    rw [← map_pow,mul_comm,Polynomial.coeff_C_mul_X_pow]
    by_cases hr : i.val/S=h.val/S
    · rw [if_pos hr,Polynomial.coeff_X_pow]
      by_cases hs : i.val%S=h.val%S
      · have he : h=i := by
          apply Fin.ext
          calc
            h.val = (h.val/S)*S+h.val%S := (Nat.div_add_mod' _ _).symm
            _ = (i.val/S)*S+i.val%S := by rw [← hr,← hs]
            _ = i.val := Nat.div_add_mod' _ _
        simp [hs,he]
      · have he : h≠i := by intro he; subst h; exact hs rfl
        simp [hs,he]
    · have he : h≠i := by intro he; subst h; exact hr rfl
      simp [hr,he]
  simp only [Polynomial.finset_sum_coeff,Polynomial.coeff_smul]
  simp_rw [mono]
  simp

theorem matrix_zero (R S : Nat) : RadialOperator.matrix R S 0=1 := by
  ext i j
  unfold RadialOperator.matrix
  rw [Finset.sum_eq_single 0]
  · simp [RadialOperator.target,Nat.div_add_mod',Matrix.one_apply,Fin.ext_iff,eq_comm]
  · intro t ht ht0
    simp [ht0]
  · simp

theorem matrix_add (R S : Nat) (a b : Int) :
    RadialOperator.matrix R S a*RadialOperator.matrix R S b =
      RadialOperator.matrix R S (a+b) := by
  ext i j
  have hp :
      (∑ h : Fin (R*S), (RadialOperator.matrix R S a*RadialOperator.matrix R S b) i h •
        (X^(h.val/S)*C (X : Polynomial Int)^(h.val%S) : Polynomial (Polynomial Int))) =
      ∑ h : Fin (R*S), RadialOperator.matrix R S (a+b) i h •
        (X^(h.val/S)*C (X : Polynomial Int)^(h.val%S) : Polynomial (Polynomial Int)) := by
    simp only [Matrix.mul_apply,Finset.sum_smul,MulAction.mul_smul]
    rw [Finset.sum_comm]
    simp_rw [← Finset.smul_sum]
    simp_rw [RadialOperator.polynomial_action]
    rw [polynomial_composition]
  have hc := congrArg (fun P : Polynomial (Polynomial Int) =>
    (P.coeff (j.val/S)).coeff (j.val%S)) hp
  simpa only [row_coeff] using hc

theorem matrix_neg (R S : Nat) (a : Int) :
    RadialOperator.matrix R S a*RadialOperator.matrix R S (-a)=1 ∧
      RadialOperator.matrix R S (-a)*RadialOperator.matrix R S a=1 := by
  constructor
  · rw [matrix_add,add_neg_cancel,matrix_zero]
  · rw [matrix_add,neg_add_cancel,matrix_zero]

theorem matrix_commute (R S : Nat) (a b : Int) :
    RadialOperator.matrix R S a*RadialOperator.matrix R S b =
      RadialOperator.matrix R S b*RadialOperator.matrix R S a := by
  rw [matrix_add,matrix_add,Int.add_comm a b]

theorem transform_add (D R S : Nat) (a b : Int)
    (V : Fin (R*S) → Int × Int → Nat → Zsqrtd (-(D : Int))) :
    zsqrtdJetTransform (RadialOperator.matrix R S a)
      (zsqrtdJetTransform (RadialOperator.matrix R S b) V) =
      zsqrtdJetTransform (RadialOperator.matrix R S (a+b)) V := by
  funext i q j
  unfold zsqrtdJetTransform
  rw [← matrix_add]
  simp only [Matrix.mul_apply,Finset.sum_smul,MulAction.mul_smul,Finset.smul_sum]
  rw [Finset.sum_comm]

theorem gram_add (Q : Finset (Int × Int)) (D J R S : Nat) (a b : Int) :
    RadialOperator.matrix R S a*RadialOperator.gram Q D J R S b*
      (RadialOperator.matrix R S a).transpose =
      RadialOperator.gram Q D J R S (a+b) := by
  rw [RadialOperator.gram_congruence,RadialOperator.gram_congruence,← matrix_add]
  simp only [Matrix.transpose_mul,Matrix.mul_assoc]

theorem nonmultiplicative_control :
    ((RadialOperator.polynomial 3 (1 : Int) 1 0)*
      (RadialOperator.polynomial 3 (1 : Int) 0 1)).eval 0=0 ∧
      (RadialOperator.polynomial 3 (1 : Int) 1 1).eval 0 = -3 := by
  exact ⟨RadialOperator.origin_and_ring_controls.2.2,
    RadialOperator.origin_and_ring_controls.2.1⟩

end
end TenthDiscriminant.RadialAction
