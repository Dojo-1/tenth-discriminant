import TenthDiscriminant.SylvesterNonzero

/-!
# Irreducibility discharges the fixed determinant's nonzero hypothesis

Field-of-fractions transport keeps the original coefficient matrix and its
exact global degree. It does not claim nonzero determinant at every fiber.
-/
namespace TenthDiscriminant
open Polynomial Matrix
noncomputable section

variable {K L : Type*} [Field K] [Field L]

/-- Exact correspondence, not an assumed identification with a resultant. -/
theorem fixedSylvesterMatrix_map_to_field
    (F G : Polynomial (Polynomial K)) (a b : Nat) (phi : Polynomial K →+* L) :
    (fixedSylvesterMatrix F G a b).map phi =
      (NonzeroBridge.coeffMatrix (F.map phi) (G.map phi) b a).submatrix
        (finCongr (Nat.add_comm a b)) (finCongr (Nat.add_comm a b)) := by
  apply Matrix.ext
  intro i j
  by_cases hj : j.val < b
  all_goals simp [fixedSylvesterMatrix, polynomialCoefficientMatrix,
    fixedSylvesterColumns, NonzeroBridge.coeffMatrix, NonzeroBridge.columns,
    Matrix.map_apply, Matrix.submatrix, hj, Polynomial.coeff_X_pow_mul',
    Polynomial.coeff_map, apply_ite]
  all_goals split_ifs <;> simp_all

/-- The original fixed determinant is nonzero when its field images are coprime. -/
theorem fixedSylvester_det_ne_zero_of_coprime_map
    (F G : Polynomial (Polynomial K)) (a b : Nat) (ha : 1 <= a)
    (hF : F.natDegree = a) (hG : G.natDegree <= b)
    (phi : Polynomial K →+* L) (hphi : Function.Injective phi)
    (hcop : IsCoprime (F.map phi) (G.map phi)) :
    (fixedSylvesterMatrix F G a b).det ≠ 0 := by
  have hd : (F.map phi).natDegree = a :=
    (Polynomial.natDegree_map_eq_of_injective hphi F).trans hF
  have hf0 : F.map phi ≠ 0 := by
    intro hf
    rw [hf, Polynomial.natDegree_zero] at hd
    omega
  have hg : (G.map phi).natDegree <= b := Polynomial.natDegree_map_le.trans hG
  have hn := NonzeroBridge.coeffMatrix_det_ne_zero (F.map phi) (G.map phi)
    b a hf0 hd hg hcop
  have he : phi ((fixedSylvesterMatrix F G a b).det) =
      (NonzeroBridge.coeffMatrix (F.map phi) (G.map phi) b a).det := by
    calc
      phi ((fixedSylvesterMatrix F G a b).det) =
          ((fixedSylvesterMatrix F G a b).map phi).det := RingHom.map_det phi _
      _ = _ := by rw [fixedSylvesterMatrix_map_to_field, Matrix.det_submatrix_equiv_self]
  intro hz
  apply hn
  rw [hz, map_zero] at he
  exact he.symm

/-- Derivative coprimality over the fraction field suffices; no nonzero resultant assumed. -/
theorem fixedDerivativeSylvester_ne_zero_of_coprime_map
    (F : Polynomial (Polynomial K)) (a : Nat) (ha : 1 <= a)
    (hF : F.natDegree = a)
    (phi : Polynomial K →+* L) (hphi : Function.Injective phi)
    (hcop : IsCoprime (F.map phi) (F.map phi).derivative) :
    (fixedSylvesterMatrix F F.derivative a (a-1)).det ≠ 0 := by
  apply fixedSylvester_det_ne_zero_of_coprime_map F F.derivative a (a-1) ha hF
    ((Polynomial.natDegree_derivative_le F).trans (by omega)) phi hphi
  simpa only [Polynomial.derivative_map] using hcop

/-- Gauss plus characteristic-zero separability supply the coprimality premise. -/
theorem fixedDerivativeSylvester_ne_zero_of_primitive_irreducible
    [CharZero K] (F : Polynomial (Polynomial K)) (a : Nat) (ha : 1 <= a)
    (hF : F.natDegree = a) (hp : F.IsPrimitive) (hi : Irreducible F) :
    (fixedSylvesterMatrix F F.derivative a (a-1)).det ≠ 0 := by
  classical
  letI : NormalizedGCDMonoid (Polynomial K) := Classical.choice inferInstance
  let phi : Polynomial K →+* FractionRing (Polynomial K) :=
    algebraMap (Polynomial K) (FractionRing (Polynomial K))
  have hi' : Irreducible (F.map phi) :=
    (hp.irreducible_iff_irreducible_map_fraction_map
      (K := FractionRing (Polynomial K))).mp hi
  exact fixedDerivativeSylvester_ne_zero_of_coprime_map F a ha hF phi
    (IsFractionRing.injective _ _) hi'.separable

/-- Positive Z-degree irreducibility excludes every nonunit common coefficient factor. -/
theorem irreducible_positive_isPrimitive
    (F : Polynomial (Polynomial K)) (a : Nat) (ha : 1 <= a)
    (hF : F.natDegree = a) (hi : Irreducible F) : F.IsPrimitive := by
  apply Polynomial.isPrimitive_iff_isUnit_of_C_dvd.mpr
  intro q hq
  obtain ⟨r, hr⟩ := hq
  rcases hi.isUnit_or_isUnit hr with hc | hu
  · exact Polynomial.isUnit_C.mp hc
  · have hd : F.natDegree <= 0 := by
      rw [hr]
      exact Polynomial.natDegree_mul_le.trans (by
        simp [Polynomial.natDegree_eq_zero_of_isUnit hu])
    omega

/-- Public nonvanishing bridge with no assumed primitive or determinant premise. -/
theorem fixedDerivativeSylvester_ne_zero_of_irreducible
    [CharZero K] (F : Polynomial (Polynomial K)) (a : Nat) (ha : 1 <= a)
    (hF : F.natDegree = a) (hi : Irreducible F) :
    (fixedSylvesterMatrix F F.derivative a (a-1)).det ≠ 0 :=
  fixedDerivativeSylvester_ne_zero_of_primitive_irreducible F a ha hF
    (irreducible_positive_isPrimitive F a ha hF hi) hi

/-- A primitive coefficient family has no identically zero parameter fiber. -/
theorem primitive_specialization_ne_zero
    (F : Polynomial (Polynomial K)) (hp : F.IsPrimitive) (w : K) :
    F.map (Polynomial.evalRingHom w) ≠ 0 := by
  intro hz
  have hc (i : Nat) : (Polynomial.X - Polynomial.C w) ∣ F.coeff i := by
    apply Polynomial.dvd_iff_isRoot.mpr
    have hi := congrArg (fun p : Polynomial K => p.coeff i) hz
    simpa only [Polynomial.coeff_map,
      Polynomial.coeff_zero, Polynomial.IsRoot] using hi
  have hd : Polynomial.C (Polynomial.X - Polynomial.C w) ∣ F :=
    (Polynomial.C_dvd_iff_dvd_coeff _ _).mpr hc
  have hu : IsUnit (Polynomial.X - Polynomial.C w) :=
    (Polynomial.isPrimitive_iff_isUnit_of_C_dvd.mp hp) _ hd
  have hdeg := Polynomial.natDegree_eq_zero_of_isUnit hu
  simpa using hdeg

/-- The specialization premise in the contact budget follows from positive-degree irreducibility. -/
theorem irreducible_positive_specialization_ne_zero
    (F : Polynomial (Polynomial K)) (a : Nat) (ha : 1 <= a)
    (hF : F.natDegree = a) (hi : Irreducible F) (w : K) :
    F.map (Polynomial.evalRingHom w) ≠ 0 :=
  primitive_specialization_ne_zero F (irreducible_positive_isPrimitive F a ha hF hi) w

end
end TenthDiscriminant
