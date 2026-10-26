import TenthDiscriminant.QuadraticChartEquivalence
import Mathlib.NumberTheory.NumberField.Discriminant.Defs

/-! Compute the actual field discriminant from a maximal integral basis,
not merely the discriminant of a convenient suborder. -/
namespace TenthDiscriminant
open Polynomial Matrix
set_option autoImplicit false
noncomputable section

private theorem quadraticBasis_repr {A : Type*} [CommRing A]
    (b : Basis (Fin 2) Int A) (u : A) (h0 : b 0=1) (h1 : b 1=u)
    (x y : Int) (i : Fin 2) :
    b.repr ((x : A)+(y : A)*u) i=(if i=0 then x else y) := by
  have heq : (x : A)+(y : A)*u=x • b 0+y • b 1 := by
    simp [h0,h1,Algebra.smul_def]
  rw [heq, map_add, map_smul, map_smul]
  fin_cases i <;> simp

private theorem quadraticBasis_trace {A : Type*} [CommRing A]
    (b : Basis (Fin 2) Int A) (u : A) (s t : Int)
    (h0 : b 0=1) (h1 : b 1=u) (hu : u^2=(s : A)*u-(t : A)) (x y : Int) :
    Algebra.trace Int A ((x : A)+(y : A)*u)=2*x+s*y := by
  have hmul : ((x : A)+(y : A)*u)*u=
      ((-t*y : Int) : A)+((x+s*y : Int) : A)*u := by
    rw [add_mul, mul_assoc, ← pow_two, hu]
    push_cast
    ring
  have hmatrix : Algebra.leftMulMatrix b ((x : A)+(y : A)*u)=
      !![x,-t*y; y,x+s*y] := by
    ext i j
    have hj : j=0 ∨ j=1 := by fin_cases j <;> simp
    rcases hj with rfl | rfl
    · rw [Algebra.leftMulMatrix_eq_repr_mul, h0, mul_one]
      have hr := quadraticBasis_repr b u h0 h1 x y i
      fin_cases i <;> simpa using hr
    · rw [Algebra.leftMulMatrix_eq_repr_mul, h1, hmul]
      have hr := quadraticBasis_repr b u h0 h1 (-t*y) (x+s*y) i
      fin_cases i <;> simpa using hr
  rw [Algebra.trace_eq_matrix_trace b, hmatrix]
  simp [Matrix.trace_fin_two]
  ring

/-- The trace pairing in basis (1,u), u^2=s*u-t, has determinant s^2-4*t. -/
theorem quadraticBasis_discr {A : Type*} [CommRing A]
    (b : Basis (Fin 2) Int A) (u : A) (s t : Int)
    (h0 : b 0=1) (h1 : b 1=u) (hu : u^2=(s : A)*u-(t : A)) :
    Algebra.discr Int b=s^2-4*t := by
  have ht1 : Algebra.trace Int A 1=2 := by
    simpa using quadraticBasis_trace b u s t h0 h1 hu 1 0
  have htu : Algebra.trace Int A u=s := by
    simpa using quadraticBasis_trace b u s t h0 h1 hu 0 1
  have heq : u*u=((-t : Int) : A)+(s : A)*u := by
    rw [← pow_two, hu]
    push_cast
    ring
  have htuu : Algebra.trace Int A (u*u)=s*s-2*t := by
    rw [heq, quadraticBasis_trace b u s t h0 h1 hu]
    ring
  have hm : Algebra.traceMatrix Int b=!![2,s; s,s*s-2*t] := by
    ext i j
    fin_cases i <;> fin_cases j <;>
      simp [Algebra.traceMatrix_apply, Algebra.traceForm_apply, h0,h1,ht1,htu,htuu]
  rw [Algebra.discr_def, hm, Matrix.det_fin_two_of]
  ring

theorem evenOrder_root_sq (d : Nat) :
    (AdjoinRoot.root (evenOrderPoly d))^2 = -AdjoinRoot.of (evenOrderPoly d) (d : Int) := by
  have h := AdjoinRoot.eval₂_root (evenOrderPoly d)
  change (X^2+C (d : Int)).eval₂ (AdjoinRoot.of (evenOrderPoly d))
    (AdjoinRoot.root (evenOrderPoly d))=0 at h
  simp only [eval₂_add, eval₂_pow, eval₂_X, eval₂_C] at h
  linear_combination h

theorem evenOrder_basis_discr (d : Nat) :
    Algebra.discr Int (evenOrderBasis d)= -4*(d : Int) := by
  have hu : (AdjoinRoot.root (evenOrderPoly d))^2=
      ((0 : Int) : AdjoinRoot (evenOrderPoly d))*AdjoinRoot.root (evenOrderPoly d)-
      ((d : Int) : AdjoinRoot (evenOrderPoly d)) := by
    simpa using evenOrder_root_sq d
  simpa using quadraticBasis_discr (evenOrderBasis d) _ 0 (d : Int)
    (evenOrderBasis_zero d) (evenOrderBasis_one d) hu

theorem even_actual_discr (d : Nat) [Fact (0 < d)] (hsq : Squarefree d)
    (hmod : (d : Int)%4=1 ∨ (d : Int)%4=2) :
    NumberField.discr (EvenQuadraticField d)= -4*(d : Int) := by
  let e := evenOrderEquivRingOfIntegers d hsq hmod
  let b := (evenOrderBasis d).map e.toAddEquiv.toIntLinearEquiv
  have h0 : b 0=1 := by simp [b, evenOrderBasis_zero]
  have h1 : b 1=e (AdjoinRoot.root (evenOrderPoly d)) := by simp [b, evenOrderBasis_one]
  have hu : (e (AdjoinRoot.root (evenOrderPoly d)))^2=
      ((0 : Int) : NumberField.RingOfIntegers (EvenQuadraticField d))*
        e (AdjoinRoot.root (evenOrderPoly d))-
      ((d : Int) : NumberField.RingOfIntegers (EvenQuadraticField d)) := by
    rw [← map_pow, evenOrder_root_sq, map_neg]
    simp
  rw [← NumberField.discr_eq_discr _ b]
  simpa using quadraticBasis_discr b _ 0 (d : Int) h0 h1 hu

theorem half_actual_discr (d : Nat) [Fact ((d : Int)%4=3)] (hsq : Squarefree d) :
    NumberField.discr (QuadraticField (((d : Int)+1)/4))= -(d : Int) := by
  let e := halfOrderEquivRingOfIntegers d hsq
  let b := (halfOrderBasis d).map e.toAddEquiv.toIntLinearEquiv
  have h0 : b 0=1 := by simp [b, halfOrderBasis_zero]
  have h1 : b 1=e (AdjoinRoot.root (halfOrderPolynomial d)) := by simp [b, halfOrderBasis_one]
  have hu : (e (AdjoinRoot.root (halfOrderPolynomial d)))^2=
      ((1 : Int) : NumberField.RingOfIntegers (QuadraticField (((d : Int)+1)/4)))*
        e (AdjoinRoot.root (halfOrderPolynomial d))-
      ((((d : Int)+1)/4 : Int) : NumberField.RingOfIntegers (QuadraticField (((d : Int)+1)/4))) := by
    rw [← map_pow, halfOrder_root_sq, map_sub]
    simp
  have hm := Fact.out (p := (d : Int)%4=3)
  have hc : 4*(((d : Int)+1)/4)=(d : Int)+1 := by omega
  rw [← NumberField.discr_eq_discr _ b, quadraticBasis_discr b _ 1 _ h0 h1 hu]
  norm_num
  omega

theorem imaginaryQuadratic_discr (d : Nat) [Fact (0 < d)] (hsq : Squarefree d) :
    NumberField.discr (ImaginaryQuadraticField d)=
      if (d : Int)%4=3 then -(d : Int) else -4*(d : Int) := by
  by_cases hodd : (d : Int)%4=3
  · letI : Fact ((d : Int)%4=3) := ⟨hodd⟩
    rw [if_pos hodd]
    exact (NumberField.discr_eq_discr_of_algEquiv _ (quadraticChartEquiv d)).trans
      (half_actual_discr d hsq)
  · rw [if_neg hodd]
    rcases squarefree_mod_four_cases d hsq with h | h
    · exact False.elim (hodd h)
    · exact even_actual_discr d hsq h

theorem imaginaryQuadratic_discr_natAbs (d : Nat) [Fact (0 < d)] (hsq : Squarefree d) :
    (NumberField.discr (ImaginaryQuadraticField d)).natAbs=absoluteDiscriminantParameter d := by
  rw [imaginaryQuadratic_discr d hsq]
  by_cases h : (d : Int)%4=3 <;> simp [absoluteDiscriminantParameter,h,Int.natAbs_mul]

theorem imaginaryQuadratic_classNumber_one_discriminant_bound (d : Nat) [Fact (0 < d)]
    (hsq : Squarefree d) (hc : NumberField.classNumber (ImaginaryQuadraticField d)=1) :
    (NumberField.discr (ImaginaryQuadraticField d)).natAbs<700000000000 := by
  rw [imaginaryQuadratic_discr_natAbs d hsq]
  exact imaginaryQuadratic_classNumber_one_parameter_bound d hsq hc

end
end TenthDiscriminant
