import TenthDiscriminant

/-! Full principal-block upper bound on the original ordinary-jet determinant.
Orthogonal bases are real proof auxiliaries, never arithmetic lattice changes. -/
open Matrix
open scoped BigOperators ComplexConjugate Classical
namespace TenthDiscriminant.RadialBlocks
noncomputable section

private theorem finite_hadamard {n : Type*} [Fintype n] [DecidableEq n]
    (A : Matrix n n Real) (hA : A.PosSemidef) :
    A.det ≤ ∏ i, A i i := by
  let e := Fintype.equivFin n
  have h := real_psd_det_le_diag (Fintype.card n) (A.submatrix e.symm e.symm)
    (hA.submatrix e.symm)
  rw [Matrix.det_submatrix_equiv_self] at h
  convert h using 1
  exact (Fintype.prod_equiv e (fun i => A i i)
    (fun i => A (e.symm i) (e.symm i)) (by intro i; simp))

/-- General Fischer inequality, including empty and singular principal blocks. -/
theorem fischer_sigma {k : Type*} [Fintype k] [DecidableEq k]
    {n : k → Type*} [∀ b, Fintype (n b)] [∀ b, DecidableEq (n b)]
    (A : Matrix (Sigma n) (Sigma n) Real) (hA : A.PosSemidef) :
    A.det ≤ ∏ b, (A.submatrix (Sigma.mk b) (Sigma.mk b)).det := by
  classical
  let B (b : k) := A.submatrix (Sigma.mk b) (Sigma.mk b)
  have hb (b : k) : (B b).IsHermitian := (hA.submatrix (Sigma.mk b)).1
  let V (b : k) : Matrix (n b) (n b) Real := (hb b).eigenvectorUnitary
  let U := Matrix.blockDiagonal' V
  have hu : Uᴴ * U = 1 := by
    dsimp [U]
    rw [Matrix.blockDiagonal'_conjTranspose, ← Matrix.blockDiagonal'_mul]
    have hv (b : k) : (V b)ᴴ * V b = 1 := by
      exact unitary.coe_star_mul_self ((hb b).eigenvectorUnitary)
    simp_rw [hv]
    exact Matrix.blockDiagonal'_one
  have hd : (Uᴴ * A * U).det = A.det := by
    have hdet := congrArg Matrix.det hu
    simp only [Matrix.det_mul, Matrix.det_one] at hdet
    rw [Matrix.det_mul, Matrix.det_mul]
    calc
      Uᴴ.det * A.det * U.det = (Uᴴ.det * U.det) * A.det := by ring
      _ = A.det := by rw [hdet, one_mul]
  have hc (b : k) : (Uᴴ * A * U).submatrix (Sigma.mk b) (Sigma.mk b) =
      (V b)ᴴ * B b * V b := by
    ext i j
    simp [U, B, Matrix.mul_apply, ← Finset.univ_sigma_univ,
      Finset.sum_sigma, Matrix.blockDiagonal'_apply, Matrix.conjTranspose_apply]
  have he (b : k) (i : n b) :
      (Uᴴ * A * U) ⟨b,i⟩ ⟨b,i⟩ = (hb b).eigenvalues i := by
    have h := congrFun (congrFun (hc b) i) i
    rw [show (V b)ᴴ * B b * V b =
        Matrix.diagonal (RCLike.ofReal ∘ (hb b).eigenvalues) from
      (hb b).star_mul_self_mul_eq_diagonal] at h
    simpa using h
  have h := finite_hadamard (Uᴴ * A * U) (hA.conjTranspose_mul_mul_same U)
  rw [hd] at h
  calc
    A.det ≤ ∏ i : Sigma n, (Uᴴ * A * U) i i := h
    _ = ∏ b, ∏ i : n b, (hb b).eigenvalues i := by
      rw [← Finset.univ_sigma_univ, Finset.prod_sigma]
      simp_rw [he]
    _ = ∏ b, (B b).det := by
      apply Finset.prod_congr rfl
      intro b _
      exact ((hb b).det_eq_prod_eigenvalues).symm

/-- Product of actual principal blocks for a finite partition. -/
def blockProduct {n k : Type*} [Fintype n] [Fintype k] [DecidableEq n]
    (A : Matrix n n Real) (f : n → k) : Real :=
  ∏ b, (A.submatrix (fun i : {i // f i = b} => i.val)
    (fun i : {i // f i = b} => i.val)).det

/-- Regrouping rows changes neither determinant nor the principal blocks. -/
theorem fischer_partition {n k : Type*} [Fintype n] [Fintype k]
    [DecidableEq n] [DecidableEq k] (A : Matrix n n Real)
    (hA : A.PosSemidef) (f : n → k) : A.det ≤ blockProduct A f := by
  classical
  let e := Equiv.sigmaFiberEquiv f
  have h := fischer_sigma (A.submatrix e e) (hA.submatrix e)
  rw [Matrix.det_submatrix_equiv_self] at h
  simpa [blockProduct,e,Equiv.sigmaFiberEquiv,Matrix.submatrix] using h

private theorem equal_weight_monomials (c d : Real) (z : Complex)
    (a b t u m : Nat) (h1 : a+u=m) (h2 : b+t=m) :
    ((c : Complex)*z^a*(conj z)^b) * conj ((d : Complex)*z^t*(conj z)^u) =
      ((c*d*Complex.normSq z^m : Real) : Complex) := by
  calc
    _ = (c : Complex)*(d : Complex)*(z^(a+u)*(conj z)^(b+t)) := by
      simp [map_mul, map_pow, pow_add]; ring
    _ = _ := by
      rw [h1,h2, ← mul_pow, Complex.mul_conj]
      push_cast
      ring

/-- Full equal-weight identity: arbitrary separation, all ordinary derivatives. -/
theorem equal_weight_entry (P : Finset Complex) (J r s t u : Nat)
    (hw : r+u=t+s) :
    traceGramEntry P J r s t u =
      2 * ∑ j ∈ Finset.range J, if j≤r ∧ j≤t then
        (r.descFactorial j : Real)*(t.descFactorial j : Real)*
          normMoment P (r+u-j) else 0 := by
  classical
  unfold traceGramEntry
  congr 1
  apply Finset.sum_congr rfl
  intro j _
  by_cases hr : j≤r
  · by_cases ht : j≤t
    · simp only [hr,ht,and_self,if_true]
      have h (z : Complex) :
          (derivativeRow r s j z * conj (derivativeRow t u j z)).re =
          (r.descFactorial j : Real)*(t.descFactorial j : Real)*
            Complex.normSq z^(r+u-j) := by
        simp only [derivativeRow,if_pos hr,if_pos ht]
        rw [equal_weight_monomials _ _ _ _ _ _ _ (r+u-j) (by omega) (by omega)]
        rfl
      simp_rw [h]
      simp [normMoment,Finset.mul_sum]
    · simp [derivativeRow,hr,ht]
  · simp [derivativeRow,hr]

def rowWeight (R S : Nat) (i : Fin (R*S)) : Int :=
  (i.val/S : Nat) - (i.val%S : Int)

def weightLabels (R S : Nat) : Finset Int := Finset.univ.image (rowWeight R S)

def weightLabel (R S : Nat) (i : Fin (R*S)) : ↥(weightLabels R S) :=
  ⟨rowWeight R S i,Finset.mem_image.mpr ⟨i,Finset.mem_univ _,rfl⟩⟩

/-- Each entry uses the actual moment and ordinary falling-factorial coefficients. -/
def momentBlock (P : Finset Complex) (J R S : Nat) (b : ↥(weightLabels R S)) :
    Matrix {i // weightLabel R S i=b} {i // weightLabel R S i=b} Real :=
  fun i t => 2 * ∑ j ∈ Finset.range J,
    if j ≤ i.val.val/S ∧ j ≤ t.val.val/S then
      ((i.val.val/S).descFactorial j : Real)*((t.val.val/S).descFactorial j : Real)*
        normMoment P (i.val.val/S+t.val.val%S-j) else 0

def momentProduct (P : Finset Complex) (J R S : Nat) : Real :=
  ∏ b : ↥(weightLabels R S), (momentBlock P J R S b).det

/-- Exact block equality, without symmetry of the sample set. -/
theorem principal_eq_moment (P : Finset Complex) (J R S : Nat)
    (b : ↥(weightLabels R S)) :
    (rectangularTraceGram P J R S).submatrix
      (fun i : {i // weightLabel R S i=b} => i.val)
      (fun i : {i // weightLabel R S i=b} => i.val) = momentBlock P J R S b := by
  ext i t
  change traceGramEntry P J (i.val.val/S) (i.val.val%S)
    (t.val.val/S) (t.val.val%S) = _
  apply equal_weight_entry
  have hi := congrArg Subtype.val i.property
  have ht := congrArg Subtype.val t.property
  dsimp [weightLabel,rowWeight] at hi ht
  omega

theorem rectangular_det_le_moments (P : Finset Complex) (J R S : Nat) :
    (rectangularTraceGram P J R S).det ≤ momentProduct P J R S := by
  classical
  have h := fischer_partition _ (rectangularTraceGram_posSemidef P J R S)
    (weightLabel R S)
  simpa only [blockProduct,principal_eq_moment,momentProduct] using h

/-- Same integer determinant between its arithmetic divisor and moment blocks. -/
theorem integer_prime_block_bridge (Q : Finset (Int × Int)) (D J R S p : Nat)
    (hD : 0<D) [Fact p.Prime] (hp2 : p≠2) (hns : ¬ IsSquare (-(D : ZMod p)))
    (hR : 1≤R) (hS : 1≤S) (hJ : S≤J) (hcard : 2*(R-1)+(S-1)<Q.card) :
    let G := integerRectangularTraceGram Q D J R S
    0<G.det ∧ (p:Int)^(2*valuationWeight R S p)∣G.det ∧
      (p:Real)^(2*valuationWeight R S p) ≤ (G.det:Real) ∧
      (G.det:Real) ≤ momentProduct (Q.image (pairEval D)) J R S := by
  dsimp only
  have h := PassiveTransport.passive_translation_bridge Q D (0,0) J R S p
    hD hp2 hns hR hS hJ hcard
  have hlo : (p:Int)^(2*valuationWeight R S p) ≤
      (integerRectangularTraceGram Q D J R S).det := Int.le_of_dvd h.2.2.1 h.2.2.2
  refine ⟨h.2.2.1,h.2.2.2,?_,?_⟩
  · exact_mod_cast hlo
  · rw [integerRectangularTraceGram_det_cast Q D J R S hD]
    exact rectangular_det_le_moments _ _ _ _

theorem empty_control : (rectangularTraceGram ∅ 0 0 0).det=1 := by
  simp

theorem singular_control :
    ((fun _ _ : Fin 2 => (1:Real)) : Matrix (Fin 2) (Fin 2) Real).det=0 ∧
      (∏ _i : Fin 2, (1:Real))=1 := by
  norm_num [Matrix.det_fin_two]

theorem cross_weight_control : traceGramEntry {1} 1 0 0 1 0=2 := by
  norm_num [traceGramEntry,derivativeRow,Finset.sum_range_succ,Nat.descFactorial]

theorem negative_nonadjacent_control :
    traceGramEntry {1} 3 0 2 2 4=2 ∧ traceGramEntry {1} 3 2 4 2 4=18 := by
  norm_num [traceGramEntry,derivativeRow,Finset.sum_range_succ,Nat.descFactorial]

theorem origin_control :
    traceGramEntry {0} 3 0 0 2 2=0 ∧ traceGramEntry {0} 3 0 0 0 0=2 := by
  norm_num [traceGramEntry,derivativeRow,Finset.sum_range_succ,Nat.descFactorial]

theorem real_hermitian_control :
    (traceGramMatrix {Complex.I} 1 (fun i : Fin 2 => (i.val,0))).det=4 ∧
      ((fun a b : Fin 2 => derivativeRow a.val 0 0 Complex.I *
        conj (derivativeRow b.val 0 0 Complex.I)) : Matrix (Fin 2) (Fin 2) Complex).det=0 := by
  refine ⟨PassiveTransport.real_complex_control.1,?_⟩
  norm_num [Matrix.det_fin_two,derivativeRow,Nat.descFactorial,Complex.I_mul_I]

end
end TenthDiscriminant.RadialBlocks
#audit_namespace TenthDiscriminant.RadialBlocks
#print TenthDiscriminant.RadialBlocks.fischer_sigma
#print TenthDiscriminant.RadialBlocks.fischer_partition
#print TenthDiscriminant.RadialBlocks.equal_weight_entry
#print TenthDiscriminant.RadialBlocks.principal_eq_moment
#print TenthDiscriminant.RadialBlocks.rectangular_det_le_moments
#print TenthDiscriminant.RadialBlocks.integer_prime_block_bridge

open Lean Elab Command

elab "#phase114_inputs " root:ident : command => do
  let env ← getEnv
  let target := root.getId
  unless env.checked.get.find? target |>.isSome do
    throwError "PHASE114_ROOT_MISSING {target}"
  let (_, state) := ((Lean.CollectAxioms.collect target).run env).run {}
  let forbidden : Array Name := #[
    ``TenthDiscriminant.ellipse_primeMass_product_dvd,
    ``TenthDiscriminant.ellipse_primeMass_hadamard_sandwich,
    ``TenthDiscriminant.ellipse_allOddPrimeMass_hadamard_sandwich,
    ``TenthDiscriminant.ellipse_allOddPrimeMass_log_le_hadamard,
    ``TenthDiscriminant.smallPrimeNormLifting_of_classNumber_one,
    ``TenthDiscriminant.smallPrime_nonsquare_of_classNumber_one,
    ``TenthDiscriminant.rectangularTraceGram_valuation_of_classNumber_one,
    ``TenthDiscriminant.FirstCertificate.Tuned.odd_large_classNumber_ne_one_50b,
    ``TenthDiscriminant.totallyComplex_degree_two_classNumber_one_discriminant_bound_50b,
    ``TenthDiscriminant.FirstCertificate.Tuned.odd_large_classNumber_ne_one_recovered,
    ``TenthDiscriminant.imaginaryQuadratic_large_classNumber_ne_one_recovered,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound_recovered,
    ``TenthDiscriminant.totallyComplex_degree_two_classNumber_one_discriminant_bound_recovered,
    ``TenthDiscriminant.FirstCertificate.Tuned.odd_large_classNumber_ne_one,
    ``TenthDiscriminant.imaginaryQuadratic_large_classNumber_ne_one_100b,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_radicand_bound_100b,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound_100b,
    ``TenthDiscriminant.totallyComplex_degree_two_classNumber_one_discriminant_bound,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_iff,
    ``TenthDiscriminant.known_nine_classNumber_one,
    ``TenthDiscriminant.phase36_all_fibers,
    ``TenthDiscriminant.classNumber_one_candidates_below_million,
    ``TenthDiscriminant.classNumber_one_iff_below_million,
    ``TenthDiscriminant.phase35_q0_translate,
    ``TenthDiscriminant.FirstCertificate.odd_large_classNumber_ne_one,
    ``TenthDiscriminant.imaginaryQuadratic_large_classNumber_ne_one,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_radicand_bound,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_parameter_bound,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound,
    ``TenthDiscriminant.FirstCertificate.odd_large_classNumber_ne_one_200b,
    ``TenthDiscriminant.imaginaryQuadratic_large_classNumber_ne_one_200b,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_radicand_bound_200b,
    ``TenthDiscriminant.imaginaryQuadratic_classNumber_one_discriminant_bound_200b,
    ``TenthDiscriminant.FirstCertificate.rawPrimeMassLower_uniform,
    ``TenthDiscriminant.classNumber_one_of_field_equiv,
    ``TenthDiscriminant.UniformTwoClass.odd_classNumber_gt_two,
    ``TenthDiscriminant.OddFieldTwoClass.arbitrary_odd_discriminant_bound,
    ``TenthDiscriminant.ControlledClassCount.controlled_class_form_and_count,
    ``TenthDiscriminant.PrincipalBasis.principal_form_of_class,
    ``TenthDiscriminant.PrincipalBasis.principal_class_form_and_prime_count,
    ``TenthDiscriminant.ActualPrimeAxis.actual_axis_card_le_two,
    ``TenthDiscriminant.ActualPrimeAxis.controlled_class_prime_count,
    ``TenthDiscriminant.ControlledPrimeFamily.controlled_family,
    ``TenthDiscriminant.ControlledPrimeFamily.fixed_family_odd_four,
    ``TenthDiscriminant.ControlledPrimeFamily.fixed_family_finite,
    ``TenthDiscriminant.ResidueMultiplicity.actualResidueMap,
    ``TenthDiscriminant.ResidueMultiplicity.actual_residue_pair_ne,
    ``TenthDiscriminant.ClassAggregation.prime_prefix_bound,
    ``TenthDiscriminant.ClassAggregation.uniform_two_class_bound,
    ``TenthDiscriminant.SplitPrimeBudget.countBound,
    ``TenthDiscriminant.SplitPrimeBudget.remainder_prefix_bound,
    ``TenthDiscriminant.SplitPrimeBudget.actual_gram_budget,
    ``TenthDiscriminant.ClosedKernel.actual_majorant,
    ``TenthDiscriminant.ClosedKernel.closed_count_kernel,
    ``TenthDiscriminant.ClosedKernel.closed_actual_gram_budget,
    ``TenthDiscriminant.OddMinkowski.actual_minkowski,
    ``TenthDiscriminant.OddMinkowski.normalized_count_kernel,
    ``TenthDiscriminant.OddMinkowski.normalized_actual_gram_budget,
    ``TenthDiscriminant.EvenTwoClass.even_classNumber_gt_two,
    ``TenthDiscriminant.EvenTwoClass.even_radicand_bound,
    ``TenthDiscriminant.EvenTwoClass.even_discriminant_bound,
    ``TenthDiscriminant.EvenFieldTwoClass.arbitrary_even_discriminant_bound,
    ``TenthDiscriminant.EvenFieldTwoClass.arbitrary_discriminant_bound,
    ``TenthDiscriminant.EvenFieldTwoClass.parity_refined_discriminant_bound,
    ``TenthDiscriminant.EvenFieldTwoClass.classNumber_gt_two_of_large_discriminant,
    ``TenthDiscriminant.CoordinateTranslation.coordinate_translation_bridge,
    ``TenthDiscriminant.CoordinateTranslation.shifted_gram_cast,
    ``TenthDiscriminant.CoordinateTranslation.shifted_posDef,
    ``TenthDiscriminant.CoordinateTranslation.shifted_valuation,
    ``TenthDiscriminant.CoordinateTranslation.shifted_gram_counterexample]
  for name in forbidden do
    if state.visited.contains name then
      throwError "PHASE114_FORBIDDEN_INPUT {target}: {name}"
  let mut count := 0
  for name in state.visited do
    count := count+1
    match env.checked.get.find? name with
    | none => throwError "PHASE114_UNRESOLVED {name}"
    | some info => if info.isUnsafe then throwError "PHASE114_UNSAFE_INPUT {name}"
  for name in state.axioms do
    unless name==``propext || name==``Classical.choice || name==``Quot.sound do
      throwError "PHASE114_NONSTANDARD_AXIOM {name}"
  logInfo m!"PHASE114_INPUTS_OK {target}: {count} reached;70forbidden roots excluded;axioms {state.axioms}"


#phase114_inputs TenthDiscriminant.RadialBlocks.integer_prime_block_bridge
