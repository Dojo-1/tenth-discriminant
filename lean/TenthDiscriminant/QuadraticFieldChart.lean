import TenthDiscriminant.MaximalOrderCoordinates
import Mathlib.Algebra.Polynomial.SpecificDegree

/-!
# The rational quadratic field chart

For `4c-1>0`, the polynomial `X²-X+c` has negative discriminant,
so its quotient over `ℚ` is a genuine quadratic field. This file
supplies the field and rational basis needed for the later maximal-
order identification; it does not claim that identification.
-/

namespace TenthDiscriminant
open Polynomial
noncomputable section

noncomputable def quadraticFieldPoly (c : ℤ) : Polynomial ℚ := X ^ 2 - X + C (c : ℚ)

private theorem fieldPoly_monic (c : ℤ) : (quadraticFieldPoly c).Monic := by
  have hle : ((-X + C (c : ℚ) : Polynomial ℚ).degree) ≤ 1 := by compute_degree!
  have hdeg : ((-X + C (c : ℚ) : Polynomial ℚ).degree) < 2 :=
    lt_of_le_of_lt hle (by norm_num)
  simpa only [quadraticFieldPoly, sub_eq_add_neg, add_assoc] using monic_X_pow_add hdeg

private theorem fieldPoly_degree (c : ℤ) : (quadraticFieldPoly c).natDegree = 2 := by
  unfold quadraticFieldPoly
  compute_degree!

theorem quadraticFieldPoly_irreducible (c : ℤ) (hc : 0 < 4 * c - 1) :
    Irreducible (quadraticFieldPoly c) := by
  apply Polynomial.irreducible_of_degree_le_three_of_not_isRoot
  · simp [fieldPoly_degree]
  · intro r hr
    have hr0 : r ^ 2 - r + (c : ℚ) = 0 := by
      simpa [Polynomial.IsRoot, quadraticFieldPoly] using hr
    have hcq : (0 : ℚ) < 4 * (c : ℚ) - 1 := by exact_mod_cast hc
    nlinarith [sq_nonneg (2 * r - 1)]

theorem fifteen_quadraticFieldPoly_irreducible :
    Irreducible (quadraticFieldPoly 4) :=
  quadraticFieldPoly_irreducible 4 (by norm_num)

theorem zero_quadraticFieldPoly_reducible :
    ¬ Irreducible (quadraticFieldPoly 0) := by
  intro hi
  have hroot : (quadraticFieldPoly 0).IsRoot 0 := by
    simp [quadraticFieldPoly, Polynomial.IsRoot]
  have hdeg := Polynomial.degree_eq_one_of_irreducible_of_root hi hroot
  have htwo : (quadraticFieldPoly 0).degree = 2 := by
    exact (Polynomial.degree_eq_iff_natDegree_eq_of_pos (by norm_num)).2
      (fieldPoly_degree 0)
  exact absurd hdeg (by rw [htwo]; norm_num)

abbrev QuadraticField (c : ℤ) := AdjoinRoot (quadraticFieldPoly c)

noncomputable instance (c : ℤ) [Fact (0 < 4 * c - 1)] : Field (QuadraticField c) := by
  letI : Fact (Irreducible (quadraticFieldPoly c)) :=
    ⟨quadraticFieldPoly_irreducible c Fact.out⟩
  infer_instance

noncomputable def quadraticFieldBasis (c : ℤ) :
    Basis (Fin 2) ℚ (QuadraticField c) :=
  (AdjoinRoot.powerBasis' (fieldPoly_monic c)).basis.reindex
    (finCongr (fieldPoly_degree c))

theorem quadraticFieldBasis_zero (c : ℤ) : quadraticFieldBasis c 0 = 1 := by
  rw [quadraticFieldBasis, Basis.reindex_apply]
  rw [PowerBasis.basis_eq_pow]
  simp

theorem quadraticFieldBasis_one (c : ℤ) :
    quadraticFieldBasis c 1 = AdjoinRoot.root (quadraticFieldPoly c) := by
  rw [quadraticFieldBasis, Basis.reindex_apply]
  rw [PowerBasis.basis_eq_pow]
  simp

theorem quadraticFieldBasis_repr (c : ℤ) (a b : ℚ) (i : Fin 2) :
    ((quadraticFieldBasis c).repr
      (AdjoinRoot.of (quadraticFieldPoly c) a +
        AdjoinRoot.of (quadraticFieldPoly c) b *
          AdjoinRoot.root (quadraticFieldPoly c))) i =
      (if i = 0 then a else b) := by
  have hs : AdjoinRoot.of (quadraticFieldPoly c) a +
      AdjoinRoot.of (quadraticFieldPoly c) b *
        AdjoinRoot.root (quadraticFieldPoly c) =
        a • quadraticFieldBasis c 0 + b • quadraticFieldBasis c 1 := by
    simp [quadraticFieldBasis_zero, quadraticFieldBasis_one, Algebra.smul_def]
  rw [hs, map_add, map_smul, map_smul]
  fin_cases i <;> simp

private theorem halfOrderPolynomial_monic (D : ℕ) :
    (halfOrderPolynomial D).Monic := by
  have hle : ((-X + C (((D : ℤ) + 1) / 4) : Polynomial ℤ).degree) ≤ 1 := by
    compute_degree!
  have hdeg : ((-X + C (((D : ℤ) + 1) / 4) : Polynomial ℤ).degree) < 2 :=
    lt_of_le_of_lt hle (by norm_num)
  simpa only [halfOrderPolynomial, sub_eq_add_neg, add_assoc] using
    monic_X_pow_add hdeg

private theorem halfOrderPolynomial_degree (D : ℕ) :
    (halfOrderPolynomial D).natDegree = 2 := by
  unfold halfOrderPolynomial
  compute_degree!

noncomputable def halfOrderBasis (D : ℕ) :
    Basis (Fin 2) ℤ (AdjoinRoot (halfOrderPolynomial D)) :=
  (AdjoinRoot.powerBasis' (halfOrderPolynomial_monic D)).basis.reindex
    (finCongr (halfOrderPolynomial_degree D))

theorem halfOrderBasis_zero (D : ℕ) : halfOrderBasis D 0 = 1 := by
  rw [halfOrderBasis, Basis.reindex_apply]
  rw [PowerBasis.basis_eq_pow]
  simp

theorem halfOrderBasis_one (D : ℕ) :
    halfOrderBasis D 1 = AdjoinRoot.root (halfOrderPolynomial D) := by
  rw [halfOrderBasis, Basis.reindex_apply]
  rw [PowerBasis.basis_eq_pow]
  simp

theorem halfOrder_coordinates (D : ℕ)
    (z : AdjoinRoot (halfOrderPolynomial D)) :
    ∃ x y : ℤ,
      z = AdjoinRoot.of (halfOrderPolynomial D) x +
        AdjoinRoot.of (halfOrderPolynomial D) y *
          AdjoinRoot.root (halfOrderPolynomial D) := by
  let b := halfOrderBasis D
  refine ⟨b.repr z 0, b.repr z 1, ?_⟩
  have h := (b.sum_repr z).symm
  rw [Fin.sum_univ_two] at h
  simpa [b, halfOrderBasis_zero, halfOrderBasis_one, Algebra.smul_def] using h

theorem quadraticField_basis_dimension (c : ℤ) :
    Module.finrank ℚ (QuadraticField c) = 2 := by
  let b := quadraticFieldBasis c
  simpa using Module.finrank_eq_card_basis b

theorem quadraticField_coordinates (c : ℤ) (z : QuadraticField c) :
    ∃ a b : ℚ,
      z = AdjoinRoot.of (quadraticFieldPoly c) a +
        AdjoinRoot.of (quadraticFieldPoly c) b *
          AdjoinRoot.root (quadraticFieldPoly c) := by
  let v := quadraticFieldBasis c
  refine ⟨v.repr z 0, v.repr z 1, ?_⟩
  have h := (v.sum_repr z).symm
  rw [Fin.sum_univ_two] at h
  simpa [v, quadraticFieldBasis_zero, quadraticFieldBasis_one, Algebra.smul_def] using h

private theorem quadraticField_root_sq (c : ℤ) :
    (AdjoinRoot.root (quadraticFieldPoly c)) ^ 2 =
      AdjoinRoot.root (quadraticFieldPoly c) -
        AdjoinRoot.of (quadraticFieldPoly c) (c : ℚ) := by
  have h := AdjoinRoot.eval₂_root (quadraticFieldPoly c)
  change (X ^ 2 - X + C (c : ℚ)).eval₂
    (AdjoinRoot.of (quadraticFieldPoly c))
    (AdjoinRoot.root (quadraticFieldPoly c)) = 0 at h
  simp only [eval₂_add, eval₂_sub, eval₂_pow, eval₂_X, eval₂_C] at h
  linear_combination h

private theorem quadraticField_mul_root (c : ℤ) (a b : ℚ) :
    (AdjoinRoot.of (quadraticFieldPoly c) a +
      AdjoinRoot.of (quadraticFieldPoly c) b *
        AdjoinRoot.root (quadraticFieldPoly c)) *
      AdjoinRoot.root (quadraticFieldPoly c) =
      AdjoinRoot.of (quadraticFieldPoly c) (-(c : ℚ) * b) +
        AdjoinRoot.of (quadraticFieldPoly c) (a + b) *
          AdjoinRoot.root (quadraticFieldPoly c) := by
  have ht := quadraticField_root_sq c
  rw [add_mul, mul_assoc, ← pow_two, ht]
  simp only [map_mul, map_neg, map_add]
  ring

private theorem quadraticField_leftMulMatrix (c : ℤ) (a b : ℚ) :
    (Algebra.leftMulMatrix (quadraticFieldBasis c))
      (AdjoinRoot.of (quadraticFieldPoly c) a +
        AdjoinRoot.of (quadraticFieldPoly c) b *
          AdjoinRoot.root (quadraticFieldPoly c)) =
      !![a, -(c : ℚ) * b; b, a + b] := by
  ext i j
  have hj : j = 0 ∨ j = 1 := by fin_cases j <;> simp
  rcases hj with rfl | rfl
  · rw [Algebra.leftMulMatrix_eq_repr_mul, quadraticFieldBasis_zero, mul_one]
    have h := quadraticFieldBasis_repr c a b i
    fin_cases i <;> simpa using h
  · rw [Algebra.leftMulMatrix_eq_repr_mul, quadraticFieldBasis_one,
      quadraticField_mul_root]
    have h := quadraticFieldBasis_repr c (-(c : ℚ) * b) (a + b) i
    fin_cases i <;> simpa using h

theorem quadraticField_trace_coordinates (c : ℤ) (a b : ℚ) :
    Algebra.trace ℚ (QuadraticField c)
      (AdjoinRoot.of (quadraticFieldPoly c) a +
        AdjoinRoot.of (quadraticFieldPoly c) b *
          AdjoinRoot.root (quadraticFieldPoly c)) = 2 * a + b := by
  rw [Algebra.trace_eq_matrix_trace (quadraticFieldBasis c),
    quadraticField_leftMulMatrix]
  simp [Matrix.trace_fin_two]
  ring

theorem quadraticField_norm_coordinates (c : ℤ) (a b : ℚ) :
    Algebra.norm ℚ
      (AdjoinRoot.of (quadraticFieldPoly c) a +
        AdjoinRoot.of (quadraticFieldPoly c) b *
          AdjoinRoot.root (quadraticFieldPoly c)) =
      a ^ 2 + a * b + (c : ℚ) * b ^ 2 := by
  rw [Algebra.norm_eq_matrix_det (quadraticFieldBasis c),
    quadraticField_leftMulMatrix]
  simp only [Matrix.det_fin_two_of]
  ring

theorem quadraticField_integral_coordinates_of_trace_norm (D : ℕ)
    (hDsq : Squarefree D) (hD : (D : ℤ) % 4 = 3)
    (z : QuadraticField (((D : ℤ) + 1) / 4))
    (htrace : ∃ m : ℤ,
      Algebra.trace ℚ (QuadraticField (((D : ℤ) + 1) / 4)) z = (m : ℚ))
    (hnorm : ∃ k : ℤ, Algebra.norm ℚ z = (k : ℚ)) :
    ∃ x y : ℤ,
      z = AdjoinRoot.of (quadraticFieldPoly (((D : ℤ) + 1) / 4)) (x : ℚ) +
        AdjoinRoot.of (quadraticFieldPoly (((D : ℤ) + 1) / 4)) (y : ℚ) *
          AdjoinRoot.root (quadraticFieldPoly (((D : ℤ) + 1) / 4)) := by
  let c : ℤ := ((D : ℤ) + 1) / 4
  obtain ⟨a, b, hab⟩ := quadraticField_coordinates c z
  have hDq : (D : ℚ) + 1 = 4 * (c : ℚ) := by
    dsimp [c]
    exact_mod_cast (halfOrder_coefficient_identity D hD).symm
  obtain ⟨m, hm⟩ := htrace
  obtain ⟨k, hk⟩ := hnorm
  rw [hab, quadraticField_trace_coordinates] at hm
  rw [hab, quadraticField_norm_coordinates] at hk
  have hm' : 2 * (a + b / 2) = (m : ℚ) := by linarith
  have hk' : (a + b / 2) ^ 2 + (D : ℚ) * (b / 2) ^ 2 = (k : ℚ) := by
    nlinarith [sq_nonneg b, hDq]
  obtain ⟨x, y, hx, hy⟩ :=
    rational_quadratic_integral_coordinates D hDsq hD
      (a + b / 2) (b / 2) ⟨m, hm'⟩ ⟨k, hk'⟩
  have hby : b = (y : ℚ) := by linarith
  have hax : a = (x : ℚ) := by linarith
  refine ⟨x, y, ?_⟩
  simpa [c, hax, hby] using hab

theorem quadraticField_integral_coordinates (D : ℕ)
    (hDsq : Squarefree D) (hD : (D : ℤ) % 4 = 3)
    (z : QuadraticField (((D : ℤ) + 1) / 4))
    (hz : IsIntegral ℤ z) :
    ∃ x y : ℤ,
      z = AdjoinRoot.of (quadraticFieldPoly (((D : ℤ) + 1) / 4)) (x : ℚ) +
        AdjoinRoot.of (quadraticFieldPoly (((D : ℤ) + 1) / 4)) (y : ℚ) *
          AdjoinRoot.root (quadraticFieldPoly (((D : ℤ) + 1) / 4)) := by
  letI : Fact (0 < 4 * (((D : ℤ) + 1) / 4) - 1) :=
    ⟨by have hc := halfOrder_coefficient_identity D hD; omega⟩
  have ht : IsIntegral ℤ
      (Algebra.trace ℚ (QuadraticField (((D : ℤ) + 1) / 4)) z) :=
    Algebra.isIntegral_trace hz
  have hn : IsIntegral ℤ (Algebra.norm ℚ z) :=
    Algebra.isIntegral_norm ℚ hz
  obtain ⟨m, hm⟩ := (IsIntegrallyClosed.isIntegral_iff).mp ht
  obtain ⟨k, hk⟩ := (IsIntegrallyClosed.isIntegral_iff).mp hn
  exact quadraticField_integral_coordinates_of_trace_norm D hDsq hD z
    ⟨m, hm.symm⟩ ⟨k, hk.symm⟩

theorem quadraticField_condition_of_discriminant (D : ℕ)
    (hD : (D : ℤ) % 4 = 3) :
    0 < 4 * (((D : ℤ) + 1) / 4) - 1 := by
  have hc := halfOrder_coefficient_identity D hD
  omega

instance quadraticFieldConditionFact (D : ℕ)
    [Fact ((D : ℤ) % 4 = 3)] :
    Fact (0 < 4 * (((D : ℤ) + 1) / 4) - 1) :=
  ⟨quadraticField_condition_of_discriminant D Fact.out⟩

theorem quadraticFieldPoly_irreducible_of_discriminant (D : ℕ)
    (hD : (D : ℤ) % 4 = 3) :
    Irreducible (quadraticFieldPoly (((D : ℤ) + 1) / 4)) :=
  quadraticFieldPoly_irreducible _
    (quadraticField_condition_of_discriminant D hD)

/-- The old integral quotient maps into the genuine rational field by
sending its generator to the same root. Injectivity and maximality
are separate obligations. -/
def halfOrderToQuadraticField (D : ℕ) (hD : (D : ℤ) % 4 = 3) :
    AdjoinRoot (halfOrderPolynomial D) →+*
      QuadraticField (((D : ℤ) + 1) / 4) := by
  let c : ℤ := ((D : ℤ) + 1) / 4
  letI : Fact (0 < 4 * c - 1) :=
    ⟨quadraticField_condition_of_discriminant D hD⟩
  let t : QuadraticField c := AdjoinRoot.root (quadraticFieldPoly c)
  have ht : t ^ 2 - t + (c : QuadraticField c) = 0 := by
    have h := AdjoinRoot.eval₂_root (quadraticFieldPoly c)
    change (X ^ 2 - X + C (c : ℚ)).eval₂
      (AdjoinRoot.of (quadraticFieldPoly c)) t = 0 at h
    simpa only [eval₂_add, eval₂_sub, eval₂_pow, eval₂_X, eval₂_C]
      using h
  apply AdjoinRoot.lift (Int.castRingHom _) t
  change (X ^ 2 - X + C c).eval₂ (Int.castRingHom _) t = 0
  simpa only [eval₂_add, eval₂_sub, eval₂_pow, eval₂_X, eval₂_C]
    using ht

theorem halfOrderToQuadraticField_root (D : ℕ)
    (hD : (D : ℤ) % 4 = 3) :
    halfOrderToQuadraticField D hD
      (AdjoinRoot.root (halfOrderPolynomial D)) =
      AdjoinRoot.root (quadraticFieldPoly (((D : ℤ) + 1) / 4)) := by
  simp [halfOrderToQuadraticField]

theorem halfOrderToQuadraticField_injective (D : ℕ)
    (hD : (D : ℤ) % 4 = 3) :
    Function.Injective (halfOrderToQuadraticField D hD) := by
  let c : ℤ := ((D : ℤ) + 1) / 4
  let f := halfOrderToQuadraticField D hD
  apply (injective_iff_map_eq_zero f).2
  intro z hz
  obtain ⟨x, y, hxy⟩ := halfOrder_coordinates D z
  have hfield :
      AdjoinRoot.of (quadraticFieldPoly c) (x : ℚ) +
        AdjoinRoot.of (quadraticFieldPoly c) (y : ℚ) *
          AdjoinRoot.root (quadraticFieldPoly c) = 0 := by
    rw [hxy] at hz
    simpa [f, c, halfOrderToQuadraticField] using hz
  have hxq : (x : ℚ) = 0 := by
    have h := congrArg (fun w : QuadraticField c =>
      ((quadraticFieldBasis c).repr w) 0) hfield
    dsimp only at h
    rw [quadraticFieldBasis_repr] at h
    simpa using h
  have hyq : (y : ℚ) = 0 := by
    have h := congrArg (fun w : QuadraticField c =>
      ((quadraticFieldBasis c).repr w) 1) hfield
    dsimp only at h
    rw [quadraticFieldBasis_repr] at h
    simpa using h
  have hx : x = 0 := by exact_mod_cast hxq
  have hy : y = 0 := by exact_mod_cast hyq
  simp [hxy, hx, hy]

theorem halfOrder_image_integral (D : ℕ)
    (hD : (D : ℤ) % 4 = 3)
    (z : AdjoinRoot (halfOrderPolynomial D)) :
    IsIntegral ℤ (halfOrderToQuadraticField D hD z) := by
  obtain ⟨x, y, hxy⟩ := halfOrder_coordinates D z
  have hroot : IsIntegral ℤ (AdjoinRoot.root (halfOrderPolynomial D)) :=
    AdjoinRoot.isIntegral_root' (halfOrderPolynomial_monic D)
  have hz : IsIntegral ℤ z := by
    rw [hxy]
    have hx : IsIntegral ℤ (AdjoinRoot.of (halfOrderPolynomial D) x) :=
      isIntegral_algebraMap
    have hy : IsIntegral ℤ (AdjoinRoot.of (halfOrderPolynomial D) y) :=
      isIntegral_algebraMap
    exact hx.add (hy.mul hroot)
  exact map_isIntegral_int (halfOrderToQuadraticField D hD) hz

/-- An injective map of the explicit order into the *actual* ring of
integers. Surjectivity is the remaining maximality theorem. -/
def halfOrderToRingOfIntegers (D : ℕ)
    [Fact ((D : ℤ) % 4 = 3)] :
    AdjoinRoot (halfOrderPolynomial D) →+*
      NumberField.RingOfIntegers
        (QuadraticField (((D : ℤ) + 1) / 4)) := by
  let f := halfOrderToQuadraticField D Fact.out
  refine {
    toFun := fun z => ⟨f z, halfOrder_image_integral D Fact.out z⟩
    map_one' := ?_
    map_mul' := ?_
    map_zero' := ?_
    map_add' := ?_
  }
  · apply Subtype.ext
    exact f.map_one
  · intro x y
    apply Subtype.ext
    exact f.map_mul x y
  · apply Subtype.ext
    exact f.map_zero
  · intro x y
    apply Subtype.ext
    exact f.map_add x y

theorem halfOrderToRingOfIntegers_injective (D : ℕ)
    [Fact ((D : ℤ) % 4 = 3)] :
    Function.Injective (halfOrderToRingOfIntegers D) := by
  intro x y hxy
  apply halfOrderToQuadraticField_injective D Fact.out
  exact congrArg Subtype.val hxy

theorem halfOrderToRingOfIntegers_surjective (D : ℕ)
    (hDsq : Squarefree D) [Fact ((D : ℤ) % 4 = 3)] :
    Function.Surjective (halfOrderToRingOfIntegers D) := by
  intro w
  obtain ⟨x, y, hxy⟩ :=
    quadraticField_integral_coordinates D hDsq Fact.out w.1 w.2
  refine ⟨AdjoinRoot.of (halfOrderPolynomial D) x +
    AdjoinRoot.of (halfOrderPolynomial D) y *
      AdjoinRoot.root (halfOrderPolynomial D), ?_⟩
  apply Subtype.ext
  simpa [halfOrderToRingOfIntegers, halfOrderToQuadraticField] using hxy.symm

noncomputable def halfOrderEquivRingOfIntegers (D : ℕ)
    (hDsq : Squarefree D) [Fact ((D : ℤ) % 4 = 3)] :
    AdjoinRoot (halfOrderPolynomial D) ≃+*
      NumberField.RingOfIntegers
        (QuadraticField (((D : ℤ) + 1) / 4)) :=
  RingEquiv.ofBijective (halfOrderToRingOfIntegers D)
    ⟨halfOrderToRingOfIntegers_injective D,
      halfOrderToRingOfIntegers_surjective D hDsq⟩

theorem halfOrder_ringOfIntegers_norm (D : ℕ)
    [Fact ((D : ℤ) % 4 = 3)] (x y : ℤ) :
    Algebra.norm ℤ (halfOrderToRingOfIntegers D
      (AdjoinRoot.of (halfOrderPolynomial D) x +
        AdjoinRoot.of (halfOrderPolynomial D) y *
          AdjoinRoot.root (halfOrderPolynomial D))) =
      principalNorm (D : ℤ) x y := by
  let c : ℤ := ((D : ℤ) + 1) / 4
  have hn := Algebra.coe_norm_int (halfOrderToRingOfIntegers D
    (AdjoinRoot.of (halfOrderPolynomial D) x +
      AdjoinRoot.of (halfOrderPolynomial D) y *
        AdjoinRoot.root (halfOrderPolynomial D)))
  have hn' : ((Algebra.norm ℤ (halfOrderToRingOfIntegers D
      (AdjoinRoot.of (halfOrderPolynomial D) x +
        AdjoinRoot.of (halfOrderPolynomial D) y *
          AdjoinRoot.root (halfOrderPolynomial D))) : ℤ) : ℚ) =
      (x : ℚ) ^ 2 + (x : ℚ) * (y : ℚ) + (c : ℚ) * (y : ℚ) ^ 2 := by
    rw [hn]
    simpa [halfOrderToRingOfIntegers, halfOrderToQuadraticField, c] using
      quadraticField_norm_coordinates c (x : ℚ) (y : ℚ)
  have hform : ((principalNorm (D : ℤ) x y : ℤ) : ℚ) =
      (x : ℚ) ^ 2 + (x : ℚ) * (y : ℚ) + (c : ℚ) * (y : ℚ) ^ 2 := by
    simp only [principalNorm, c]
    push_cast
    ring
  exact_mod_cast hn'.trans hform.symm

example : Field (QuadraticField 4) := by
  letI : Fact (0 < 4 * (4 : ℤ) - 1) := ⟨by norm_num⟩
  infer_instance

example (c : ℤ) [Fact (0 < 4 * c - 1)] : NumberField (QuadraticField c) := by
  infer_instance

end
end TenthDiscriminant
