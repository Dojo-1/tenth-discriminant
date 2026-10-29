import TenthDiscriminant.PassiveTransport

/-! Integer-linear radial frames: actual polynomials, all ordinary jets,
original integer Gram, real positivity and invertible prime reductions.
This file does not prove a quantitative gain or a smaller cutoff. -/
open Matrix Polynomial
open scoped BigOperators ComplexConjugate Classical
namespace TenthDiscriminant.RadialOperator
set_option autoImplicit false
noncomputable section

def target (S r s t : Nat) : Nat := (r-t)*S+(s-t)

def matrix (R S : Nat) (a : Int) : Matrix (Fin (R*S)) (Fin (R*S)) Int :=
  fun i j => ∑ t ∈ Finset.range (min (i.val/S) (i.val%S)+1),
    if j.val=target S (i.val/S) (i.val%S) t then
      (-a)^t*(min (i.val/S) (i.val%S)).choose t else 0

theorem term_bounds (R S : Nat) (i : Fin (R*S)) (t : Nat)
    (ht : t ≤ min (i.val/S) (i.val%S)) :
    t ≤ i.val/S ∧ t ≤ i.val%S ∧ i.val%S-t < S := by
  have hS : 0 < S := by
    by_contra h
    have hz : S=0 := by omega
    have hi := i.isLt
    simp [hz] at hi
  have hs := Nat.mod_lt i.val hS
  exact ⟨ht.trans (min_le_left _ _),ht.trans (min_le_right _ _),by omega⟩

private theorem target_lt (R S : Nat) (i : Fin (R*S)) (t : Nat)
    (ht : t ≤ min (i.val/S) (i.val%S)) (hpos : 0 < t) :
    target S (i.val/S) (i.val%S) t < i.val := by
  obtain ⟨hr,hs,_⟩ := term_bounds R S i t ht
  have hm : (i.val/S-t)*S ≤ (i.val/S)*S :=
    Nat.mul_le_mul_right S (Nat.sub_le _ _)
  have he : (i.val/S)*S+i.val%S=i.val := Nat.div_add_mod' _ _
  unfold target
  omega

theorem target_in_range (R S : Nat) (i : Fin (R*S)) (t : Nat)
    (ht : t ≤ min (i.val/S) (i.val%S)) :
    target S (i.val/S) (i.val%S) t < R*S := by
  by_cases hz : t=0
  · subst t
    simpa [target,Nat.div_add_mod'] using i.isLt
  · exact (target_lt R S i t ht (by omega)).trans i.isLt

def targetFin (R S : Nat) (i : Fin (R*S)) (t : Nat) : Fin (R*S) :=
  ⟨target S (i.val/S) (i.val%S) (min t (min (i.val/S) (i.val%S))),
    target_in_range R S i _ (min_le_right _ _)⟩

theorem targetFin_labels (R S : Nat) (i : Fin (R*S)) (t : Nat)
    (ht : t ≤ min (i.val/S) (i.val%S)) :
    (targetFin R S i t).val/S=i.val/S-t ∧
      (targetFin R S i t).val%S=i.val%S-t := by
  have hs := (term_bounds R S i t ht).2.2
  have hS : 0 < S := by omega
  simp only [targetFin,min_eq_left ht,target]
  constructor
  · rw [Nat.mul_comm (i.val/S-t) S,Nat.mul_add_div hS]
    simp [Nat.div_eq_of_lt hs]
  · exact Nat.mul_add_mod_of_lt hs

theorem lower_triangular (R S : Nat) (a : Int) :
    (matrix R S a).BlockTriangular
      (OrderDual.toDual : Fin (R*S) → OrderDual (Fin (R*S))) := by
  intro i j hij
  have hij' : i.val < j.val := by simpa using hij
  unfold matrix
  apply Finset.sum_eq_zero
  intro t ht
  have ht' : t ≤ min (i.val/S) (i.val%S) := by
    have := Finset.mem_range.mp ht
    omega
  by_cases hz : t=0
  · subst t
    simp [target,Nat.div_add_mod',ne_of_gt hij']
  · have hl := target_lt R S i t ht' (by omega)
    simp [ne_of_gt (hl.trans hij')]

theorem diagonal_one (R S : Nat) (a : Int) (i : Fin (R*S)) :
    matrix R S a i i=1 := by
  unfold matrix
  rw [Finset.sum_eq_single 0]
  · simp [target,Nat.div_add_mod']
  · intro t ht ht0
    have ht' : t ≤ min (i.val/S) (i.val%S) := by
      have := Finset.mem_range.mp ht
      omega
    have hl := target_lt R S i t ht' (by omega)
    simp [ne_of_gt hl]
  · simp

theorem determinant_one (R S : Nat) (a : Int) : (matrix R S a).det=1 := by
  rw [Matrix.det_of_lowerTriangular _ (lower_triangular R S a)]
  simp [diagonal_one]

/-- Explicit integral inverse witness; no fraction-field inverse is substituted. -/
theorem integral_inverse (R S : Nat) (a : Int) :
    matrix R S a * (matrix R S a).adjugate=1 ∧
      (matrix R S a).adjugate * matrix R S a=1 := by
  constructor
  · rw [Matrix.mul_adjugate,determinant_one,one_smul]
  · rw [Matrix.adjugate_mul,determinant_one,one_smul]

/-- The direct polynomial formula, with W treated as the constant w. -/
def polynomial {A : Type*} [CommRing A] (a : Int) (w : A) (r s : Nat) : A[X] :=
  X^(r-min r s) * C w^(s-min r s) * (X*C w-C (a : A))^(min r s)

theorem polynomial_expansion {A : Type*} [CommRing A] (a : Int) (w : A)
    (r s : Nat) :
    polynomial a w r s = ∑ t ∈ Finset.range (min r s+1),
      ((-a)^t*((min r s).choose t : Int)) • (X^(r-t)*C w^(s-t) : A[X]) := by
  let m := min r s
  have hmr : m ≤ r := min_le_left _ _
  have hms : m ≤ s := min_le_right _ _
  have hb : (X*C w-C (a : A) : A[X]) = -C (a : A)+X*C w := by ring
  unfold polynomial
  change X^(r-m)*C w^(s-m)*(X*C w-C (a : A))^m = _
  rw [hb,add_pow,Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro t ht
  have htm : t ≤ m := by have := Finset.mem_range.mp ht; omega
  have hr : r-m+(m-t)=r-t := by omega
  have hs : s-m+(m-t)=s-t := by omega
  rw [zsmul_eq_mul]
  have hcoef : (((-a)^t*(m.choose t : Int) : Int) : A[X]) =
      (-C (a : A))^t*(m.choose t : A[X]) := by simp
  rw [hcoef]
  calc
    X^(r-m)*C w^(s-m)*((-C (a : A))^t*(X*C w)^(m-t)*(m.choose t : A[X])) =
      ((-C (a : A))^t*(m.choose t : A[X])) *
        (X^(r-m)*X^(m-t))*(C w^(s-m)*C w^(m-t)) := by
          rw [mul_pow]
          ring
    _ = _ := by rw [← pow_add,← pow_add,hr,hs]; ring

theorem row_action {A : Type*} [AddCommGroup A] (R S : Nat) (a : Int)
    (i : Fin (R*S)) (f : Fin (R*S) → A) :
    ∑ h : Fin (R*S), matrix R S a i h • f h =
      ∑ t ∈ Finset.range (min (i.val/S) (i.val%S)+1),
        ((-a)^t*((min (i.val/S) (i.val%S)).choose t : Int)) •
          f (targetFin R S i t) := by
  unfold matrix
  simp_rw [Finset.sum_smul]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro t ht
  have ht' : t ≤ min (i.val/S) (i.val%S) := by
    have := Finset.mem_range.mp ht
    omega
  let k : Fin (R*S) := ⟨target S (i.val/S) (i.val%S) t,target_in_range R S i t ht'⟩
  have he (h : Fin (R*S)) : h.val=target S (i.val/S) (i.val%S) t ↔ h=k := by
    constructor
    · intro h; exact Fin.ext h
    · intro h; exact congrArg Fin.val h
  have hk : targetFin R S i t=k := by
    apply Fin.ext
    simp [targetFin,k,min_eq_left ht']
  simp_rw [he]
  simp [hk,k]

theorem polynomial_action {A : Type*} [CommRing A] (R S : Nat) (a : Int)
    (i : Fin (R*S)) (w : A) :
    ∑ h : Fin (R*S), matrix R S a i h •
      (X^(h.val/S)*C w^(h.val%S) : A[X]) =
      polynomial a w (i.val/S) (i.val%S) := by
  rw [row_action,polynomial_expansion]
  apply Finset.sum_congr rfl
  intro t ht
  have ht' : t ≤ min (i.val/S) (i.val%S) := by
    have := Finset.mem_range.mp ht
    omega
  obtain ⟨hr,hs⟩ := targetFin_labels R S i t ht'
  rw [hr,hs]

theorem jet_action {A : Type*} [CommRing A] (R S : Nat) (a : Int)
    (i : Fin (R*S)) (w z : A) (j : Nat) :
    ∑ h : Fin (R*S), matrix R S a i h •
      ((derivative^[j]) (X^(h.val/S)*C w^(h.val%S))).eval z =
      ((derivative^[j]) (polynomial a w (i.val/S) (i.val%S))).eval z := by
  rw [← polynomial_action R S a i w,iterate_derivative_sum,eval_finset_sum]
  apply Finset.sum_congr rfl
  intro h _
  rw [iterate_derivative_smul,eval_smul]

private theorem complex_monomial_jet (r s j : Nat) (z : Complex) :
    ((derivative^[j]) (X^r*C (conj z)^s)).eval z = derivativeRow r s j z := by
  rw [← map_pow,mul_comm,iterate_derivative_C_mul,iterate_derivative_X_pow_eq_C_mul]
  simp only [eval_mul,eval_C,eval_pow,eval_X]
  by_cases hj : j ≤ r
  · simp [derivativeRow,hj]
    push_cast
    ring
  · have hz : (r.descFactorial j : Complex)=0 := by
      rw [Nat.descFactorial_of_lt (by omega)]
      norm_num
    simp [derivativeRow,hj,hz]

theorem complex_jet_action (R S : Nat) (a : Int) (i : Fin (R*S))
    (z : Complex) (j : Nat) :
    ∑ h : Fin (R*S), matrix R S a i h • derivativeRow (h.val/S) (h.val%S) j z =
      ((derivative^[j]) (polynomial a (conj z) (i.val/S) (i.val%S))).eval z := by
  simpa only [complex_monomial_jet] using jet_action R S a i (conj z) z j

def integerJet (D R S : Nat) (a : Int) (i : Fin (R*S)) (q : Int × Int)
    (j : Nat) : Zsqrtd (-(D : Int)) :=
  ((derivative^[j]) (polynomial a (star (pairZsqrtdEquiv D q))
    (i.val/S) (i.val%S))).eval (pairZsqrtdEquiv D q)

theorem integer_jet_action (D R S : Nat) (a : Int) (i : Fin (R*S))
    (q : Int × Int) (j : Nat) :
    zsqrtdJetTransform (matrix R S a) (rectangularCanonicalJet D R S) i q j =
      integerJet D R S a i q j := by
  simpa only [zsqrtdJetTransform,rectangularCanonicalJet,integerJet,
    integerDerivativeRow_zsqrtd_jet] using
      jet_action R S a i (star (pairZsqrtdEquiv D q)) (pairZsqrtdEquiv D q) j

def gram (Q : Finset (Int × Int)) (D J R S : Nat) (a : Int) :
    Matrix (Fin (R*S)) (Fin (R*S)) Int :=
  zsqrtdJetGram Q D J (integerJet D R S a)

theorem gram_congruence (Q : Finset (Int × Int)) (D J R S : Nat) (a : Int) :
    gram Q D J R S a = matrix R S a * integerRectangularTraceGram Q D J R S *
      (matrix R S a).transpose := by
  have he : integerJet D R S a =
      zsqrtdJetTransform (matrix R S a) (rectangularCanonicalJet D R S) := by
    funext i q j
    exact (integer_jet_action D R S a i q j).symm
  rw [gram,he,zsqrtdJetGram_transform]
  rfl

theorem gram_det (Q : Finset (Int × Int)) (D J R S : Nat) (a : Int) :
    (gram Q D J R S a).det=(integerRectangularTraceGram Q D J R S).det := by
  rw [gram_congruence,Matrix.det_mul,Matrix.det_mul,Matrix.det_transpose,determinant_one]
  ring

theorem gram_map {A : Type*} [CommRing A] (phi : Int →+* A)
    (Q : Finset (Int × Int)) (D J R S : Nat) (a : Int) :
    (gram Q D J R S a).map phi = (matrix R S a).map phi *
      (integerRectangularTraceGram Q D J R S).map phi * ((matrix R S a).map phi).transpose := by
  rw [gram_congruence,Matrix.map_mul,Matrix.map_mul,Matrix.transpose_map]

theorem real_cast (Q : Finset (Int × Int)) (D J R S : Nat) (a : Int) (hD : 0 < D) :
    (gram Q D J R S a).map (Int.castRingHom Real) =
      (matrix R S a).map (Int.castRingHom Real) *
      rectangularTraceGram (Q.image (pairEval D)) J R S *
      ((matrix R S a).map (Int.castRingHom Real)).transpose := by
  rw [gram_map,integerRectangularTraceGram_cast Q D J R S hD]

theorem mapped_det_one {A : Type*} [CommRing A] (phi : Int →+* A)
    (R S : Nat) (a : Int) : ((matrix R S a).map phi).det=1 := by
  calc
    ((matrix R S a).map phi).det = phi (matrix R S a).det := (phi.map_det _).symm
    _ = 1 := by rw [determinant_one,map_one]

theorem real_posSemidef (Q : Finset (Int × Int)) (D J R S : Nat) (a : Int)
    (hD : 0 < D) : ((gram Q D J R S a).map (Int.castRingHom Real)).PosSemidef := by
  rw [real_cast Q D J R S a hD]
  simpa only [Matrix.conjTranspose_eq_transpose_of_trivial] using
    (rectangularTraceGram_posSemidef (Q.image (pairEval D)) J R S).mul_mul_conjTranspose_same
      ((matrix R S a).map (Int.castRingHom Real))

theorem real_posDef (Q : Finset (Int × Int)) (D J R S : Nat) (a : Int)
    (hD : 0 < D) (hR : 1 ≤ R) (hS : 1 ≤ S) (hJ : S ≤ J)
    (hcard : 2*(R-1)+(S-1) < Q.card) :
    ((gram Q D J R S a).map (Int.castRingHom Real)).PosDef := by
  have hc : 2*(R-1)+(S-1) < (Q.image (pairEval D)).card := by
    rw [Finset.card_image_of_injective _ (show Function.Injective (pairEval D) from
      latticePoint_injective D hD)]
    exact hcard
  have hp := rectangularTraceGram_posDef_of_point_count (Q.image (pairEval D)) J R S hR hS hJ hc
  have hu : IsUnit ((matrix R S a).map (Int.castRingHom Real)) := by
    apply (Matrix.isUnit_iff_isUnit_det _).mpr
    rw [mapped_det_one]
    exact isUnit_one
  rw [real_cast Q D J R S a hD]
  simpa only [Matrix.conjTranspose_eq_transpose_of_trivial] using
    hp.mul_mul_conjTranspose_same (Matrix.vecMul_injective_iff_isUnit.mpr hu)

theorem reduced_rank (Q : Finset (Int × Int)) (D J R S p : Nat) (a : Int)
    [Fact p.Prime] :
    ((gram Q D J R S a).map (Int.castRingHom (ZMod p))).rank =
      ((integerRectangularTraceGram Q D J R S).map (Int.castRingHom (ZMod p))).rank := by
  rw [gram_map]
  have hu : IsUnit (((matrix R S a).map (Int.castRingHom (ZMod p))).det) := by
    rw [mapped_det_one]
    exact isUnit_one
  rw [Matrix.rank_mul_eq_left_of_isUnit_det _ _ (by simpa using hu),
    Matrix.rank_mul_eq_right_of_isUnit_det _ _ hu]

theorem integer_bridge (Q : Finset (Int × Int)) (D J R S p : Nat) (a : Int)
    (hD : 0 < D) [Fact p.Prime] (hp2 : p ≠ 2) (hns : ¬ IsSquare (-(D : ZMod p)))
    (hR : 1 ≤ R) (hS : 1 ≤ S) (hJ : S ≤ J) (hcard : 2*(R-1)+(S-1) < Q.card) :
    let G := integerRectangularTraceGram Q D J R S
    let H := gram Q D J R S a
    H.det=G.det ∧ (H.map (Int.castRingHom Real)).PosDef ∧ 0 < H.det ∧
      (p : Int)^(2*valuationWeight R S p) ∣ H.det := by
  dsimp only
  have old := PassiveTransport.passive_translation_bridge Q D (0,0) J R S p
    hD hp2 hns hR hS hJ hcard
  refine ⟨gram_det Q D J R S a,real_posDef Q D J R S a hD hR hS hJ hcard,?_,?_⟩
  · rw [gram_det]
    exact old.2.2.1
  · rw [gram_det]
    exact old.2.2.2

theorem empty_control (S : Nat) (a : Int) : Matrix.det (matrix 0 S a)=1 := by
  exact determinant_one _ _ _

theorem pilot_row_control (j : Fin 6) :
    matrix 3 2 3 5 j = if j=5 then 1 else if j=2 then -3 else 0 := by
  fin_cases j <;> decide

theorem ordinary_controls :
    ((derivative^[1]) (polynomial 3 (1 : Int) 1 1)).eval 1=1 ∧
    ((derivative^[2]) (polynomial 3 (1 : Int) 1 1)).eval 1=0 ∧
    ((derivative^[2]) (polynomial 3 (1 : Int) 2 1)).eval 1=2 := by
  norm_num [polynomial,Function.iterate_succ_apply,derivative_sub,derivative_mul,
    derivative_pow,eval_mul,eval_sub]

theorem origin_and_ring_controls :
    (X*C (1 : Int) : Int[X]).eval 0=0 ∧
      (polynomial 3 (1 : Int) 1 1).eval 0 = -3 ∧
      ((polynomial 3 (1 : Int) 1 0)*(polynomial 3 (1 : Int) 0 1)).eval 0=0 := by
  norm_num [polynomial]

theorem reduction_control :
    (matrix 2 2 3).map (Int.castRingHom (ZMod 3))=1 ∧ matrix 2 2 3 3 0 = -3 := by
  constructor
  · ext i j
    fin_cases i <;> fin_cases j <;> decide
  · decide

end
end TenthDiscriminant.RadialOperator

