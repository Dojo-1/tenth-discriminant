import TenthDiscriminant.EvenOrderCoordinates
import TenthDiscriminant.QuadraticFieldChart

/-! The genuine trace-zero quadratic field. Rational and integer bases
are explicit; the maximal-order identification is a separate theorem. -/
namespace TenthDiscriminant
open Polynomial
set_option autoImplicit false
noncomputable section

def evenFieldPoly (d : Nat) : Polynomial Rat := X^2+C (d : Rat)
def evenOrderPoly (d : Nat) : Polynomial Int := X^2+C (d : Int)
abbrev EvenQuadraticField (d : Nat) := AdjoinRoot (evenFieldPoly d)

theorem evenField_monic (d : Nat) : (evenFieldPoly d).Monic := by
  simpa [evenFieldPoly] using (monic_X_pow_add_C (d : Rat) (by decide : 2 ≠ 0))

theorem evenField_degree (d : Nat) : (evenFieldPoly d).natDegree=2 := by
  unfold evenFieldPoly
  compute_degree!

theorem evenOrder_monic (d : Nat) : (evenOrderPoly d).Monic := by
  simpa [evenOrderPoly] using (monic_X_pow_add_C (d : Int) (by decide : 2 ≠ 0))

theorem evenOrder_degree (d : Nat) : (evenOrderPoly d).natDegree=2 := by
  unfold evenOrderPoly
  compute_degree!

theorem evenField_irreducible (d : Nat) (hd : 0 < d) : Irreducible (evenFieldPoly d) := by
  apply Polynomial.irreducible_of_degree_le_three_of_not_isRoot
  · simp [evenField_degree]
  · intro r hr
    have h : r^2+(d : Rat)=0 := by simpa [Polynomial.IsRoot, evenFieldPoly] using hr
    have hdp : (0 : Rat) < d := by exact_mod_cast hd
    nlinarith [sq_nonneg r]

instance evenFieldInstance (d : Nat) [Fact (0 < d)] : Field (EvenQuadraticField d) := by
  letI : Fact (Irreducible (evenFieldPoly d)) := ⟨evenField_irreducible d Fact.out⟩
  infer_instance

instance evenPositiveFact (d : Nat) [Fact ((d : Int)%4=1 ∨ (d : Int)%4=2)] : Fact (0 < d) := by
  have h := Fact.out (p := (d : Int)%4=1 ∨ (d : Int)%4=2)
  exact ⟨by omega⟩

def evenFieldBasis (d : Nat) : Basis (Fin 2) Rat (EvenQuadraticField d) :=
  (AdjoinRoot.powerBasis' (evenField_monic d)).basis.reindex (finCongr (evenField_degree d))

def evenOrderBasis (d : Nat) : Basis (Fin 2) Int (AdjoinRoot (evenOrderPoly d)) :=
  (AdjoinRoot.powerBasis' (evenOrder_monic d)).basis.reindex (finCongr (evenOrder_degree d))

theorem evenFieldBasis_zero (d : Nat) : evenFieldBasis d 0=1 := by
  rw [evenFieldBasis, Basis.reindex_apply, PowerBasis.basis_eq_pow]
  simp

theorem evenFieldBasis_one (d : Nat) : evenFieldBasis d 1=AdjoinRoot.root (evenFieldPoly d) := by
  rw [evenFieldBasis, Basis.reindex_apply, PowerBasis.basis_eq_pow]
  simp

theorem evenOrderBasis_zero (d : Nat) : evenOrderBasis d 0=1 := by
  rw [evenOrderBasis, Basis.reindex_apply, PowerBasis.basis_eq_pow]
  simp

theorem evenOrderBasis_one (d : Nat) : evenOrderBasis d 1=AdjoinRoot.root (evenOrderPoly d) := by
  rw [evenOrderBasis, Basis.reindex_apply, PowerBasis.basis_eq_pow]
  simp

theorem evenField_coordinates (d : Nat) (z : EvenQuadraticField d) :
    ∃ a b : Rat, z=AdjoinRoot.of (evenFieldPoly d) a+
      AdjoinRoot.of (evenFieldPoly d) b*AdjoinRoot.root (evenFieldPoly d) := by
  let v := evenFieldBasis d
  refine ⟨v.repr z 0, v.repr z 1, ?_⟩
  have h := (v.sum_repr z).symm
  rw [Fin.sum_univ_two] at h
  simpa [v, evenFieldBasis_zero, evenFieldBasis_one, Algebra.smul_def] using h

theorem evenOrder_coordinates (d : Nat) (z : AdjoinRoot (evenOrderPoly d)) :
    ∃ x y : Int, z=AdjoinRoot.of (evenOrderPoly d) x+
      AdjoinRoot.of (evenOrderPoly d) y*AdjoinRoot.root (evenOrderPoly d) := by
  let v := evenOrderBasis d
  refine ⟨v.repr z 0, v.repr z 1, ?_⟩
  have h := (v.sum_repr z).symm
  rw [Fin.sum_univ_two] at h
  simpa [v, evenOrderBasis_zero, evenOrderBasis_one, Algebra.smul_def] using h

theorem evenFieldBasis_repr (d : Nat) (a b : Rat) (i : Fin 2) :
    (evenFieldBasis d).repr (AdjoinRoot.of (evenFieldPoly d) a+
      AdjoinRoot.of (evenFieldPoly d) b*AdjoinRoot.root (evenFieldPoly d)) i =
      (if i=0 then a else b) := by
  have hs : AdjoinRoot.of (evenFieldPoly d) a+
      AdjoinRoot.of (evenFieldPoly d) b*AdjoinRoot.root (evenFieldPoly d) =
      a • evenFieldBasis d 0+b • evenFieldBasis d 1 := by
    simp [evenFieldBasis_zero, evenFieldBasis_one, Algebra.smul_def]
  rw [hs, map_add, map_smul, map_smul]
  fin_cases i <;> simp

theorem evenField_root_sq (d : Nat) : (AdjoinRoot.root (evenFieldPoly d))^2 =
    -AdjoinRoot.of (evenFieldPoly d) (d : Rat) := by
  have h := AdjoinRoot.eval₂_root (evenFieldPoly d)
  change (X^2+C (d : Rat)).eval₂ (AdjoinRoot.of (evenFieldPoly d))
    (AdjoinRoot.root (evenFieldPoly d))=0 at h
  simp only [eval₂_add, eval₂_pow, eval₂_X, eval₂_C] at h
  linear_combination h

theorem evenField_leftMulMatrix (d : Nat) (a b : Rat) :
    (Algebra.leftMulMatrix (evenFieldBasis d)) (AdjoinRoot.of (evenFieldPoly d) a+
      AdjoinRoot.of (evenFieldPoly d) b*AdjoinRoot.root (evenFieldPoly d)) =
      !![a, -(d : Rat)*b; b, a] := by
  have hmul : (AdjoinRoot.of (evenFieldPoly d) a+
      AdjoinRoot.of (evenFieldPoly d) b*AdjoinRoot.root (evenFieldPoly d))*
      AdjoinRoot.root (evenFieldPoly d) =
      AdjoinRoot.of (evenFieldPoly d) (-(d : Rat)*b)+
        AdjoinRoot.of (evenFieldPoly d) a*AdjoinRoot.root (evenFieldPoly d) := by
    rw [add_mul, mul_assoc, ← pow_two, evenField_root_sq]
    simp only [map_mul, map_neg]
    ring
  ext i j
  have hj : j=0 ∨ j=1 := by fin_cases j <;> simp
  rcases hj with rfl | rfl
  · rw [Algebra.leftMulMatrix_eq_repr_mul, evenFieldBasis_zero, mul_one]
    have h := evenFieldBasis_repr d a b i
    fin_cases i <;> simpa using h
  · rw [Algebra.leftMulMatrix_eq_repr_mul, evenFieldBasis_one, hmul]
    have h := evenFieldBasis_repr d (-(d : Rat)*b) a i
    fin_cases i <;> simpa using h

theorem evenField_trace (d : Nat) (a b : Rat) :
    Algebra.trace Rat (EvenQuadraticField d) (AdjoinRoot.of (evenFieldPoly d) a+
      AdjoinRoot.of (evenFieldPoly d) b*AdjoinRoot.root (evenFieldPoly d))=2*a := by
  rw [Algebra.trace_eq_matrix_trace (evenFieldBasis d), evenField_leftMulMatrix]
  simp [Matrix.trace_fin_two]
  ring

theorem evenField_norm (d : Nat) (a b : Rat) :
    Algebra.norm Rat (AdjoinRoot.of (evenFieldPoly d) a+
      AdjoinRoot.of (evenFieldPoly d) b*AdjoinRoot.root (evenFieldPoly d))=
      a^2+(d : Rat)*b^2 := by
  rw [Algebra.norm_eq_matrix_det (evenFieldBasis d), evenField_leftMulMatrix]
  simp only [Matrix.det_fin_two_of]
  ring

theorem evenField_integral_coordinates (d : Nat) [Fact (0 < d)]
    (hsq : Squarefree d) (hmod : (d : Int)%4=1 ∨ (d : Int)%4=2)
    (z : EvenQuadraticField d) (hz : IsIntegral Int z) :
    ∃ x y : Int, z=AdjoinRoot.of (evenFieldPoly d) (x : Rat)+
      AdjoinRoot.of (evenFieldPoly d) (y : Rat)*AdjoinRoot.root (evenFieldPoly d) := by
  obtain ⟨a, b, hab⟩ := evenField_coordinates d z
  have ht : IsIntegral Int (Algebra.trace Rat (EvenQuadraticField d) z) := Algebra.isIntegral_trace hz
  have hn : IsIntegral Int (Algebra.norm Rat z) := Algebra.isIntegral_norm Rat hz
  obtain ⟨m, hm⟩ := (IsIntegrallyClosed.isIntegral_iff).mp ht
  obtain ⟨k, hk⟩ := (IsIntegrallyClosed.isIntegral_iff).mp hn
  rw [hab, evenField_trace] at hm
  rw [hab, evenField_norm] at hk
  obtain ⟨x, y, hx, hy⟩ := evenChart_integral_coordinates d hsq hmod a b ⟨m, hm.symm⟩ ⟨k, hk.symm⟩
  exact ⟨x, y, by simpa [hx, hy] using hab⟩

end
end TenthDiscriminant
