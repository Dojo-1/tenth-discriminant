import TenthDiscriminant.QuadraticGeneratorBridge

/-! Intrinsic normalization through conjugation and its anti-invariant projector.
Coordinates enter only when choosing a squarefree representative of the
negative rational square class. No class-number input constructs the generator. -/
namespace TenthDiscriminant
open NumberField
set_option autoImplicit false
noncomputable section

theorem quadratic_nonidentity_aut_eq (K : Type*) [Field K] [NumberField K]
    (hdegree : Module.finrank Rat K = 2) {sigma tau : K ≃ₐ[Rat] K}
    (hsigma : sigma ≠ 1) (htau : tau ≠ 1) : sigma = tau := by
  classical
  letI : Algebra.IsQuadraticExtension Rat K where
    toFree := inferInstance
    finrank_eq_two' := hdegree
  have hc : Nat.card (K ≃ₐ[Rat] K) = 2 := by
    rw [Nat.card_eq_fintype_card, IsGalois.card_aut_eq_finrank Rat K, hdegree]
  obtain ⟨rho, _, huniq⟩ := (Nat.card_eq_two_iff' (1 : K ≃ₐ[Rat] K)).mp hc
  exact (huniq sigma hsigma).trans (huniq tau htau).symm

theorem exists_conjugation_operator (K : Type*) [Field K] [NumberField K]
    [NumberField.IsTotallyComplex K] (hdegree : Module.finrank Rat K = 2) :
    ∃ (phi : K →+* Complex) (sigma : K ≃ₐ[Rat] K),
      ComplexEmbedding.IsConj phi sigma ∧ sigma ≠ 1 ∧ Function.Involutive sigma := by
  classical
  letI : Algebra.IsQuadraticExtension Rat K where
    toFree := inferInstance
    finrank_eq_two' := hdegree
  let phi : K →+* Complex := Classical.choice inferInstance
  have hbase : phi.comp (algebraMap Rat K) =
      (ComplexEmbedding.conjugate phi).comp (algebraMap Rat K) := by
    ext r
    simp only [RingHom.comp_apply, ComplexEmbedding.conjugate_coe_eq]
    change phi (r : K) = star (phi (r : K))
    simp
  obtain ⟨tau, htau⟩ := ComplexEmbedding.exists_comp_symm_eq_of_comp_eq
    (k := Rat) phi (ComplexEmbedding.conjugate phi) hbase
  let sigma := tau.symm
  have hconj : ComplexEmbedding.IsConj phi sigma := htau.symm
  have hne : sigma ≠ 1 := by
    intro heq
    have hr : ComplexEmbedding.IsReal phi :=
      ComplexEmbedding.isConj_one_iff.mp (by simpa [heq] using hconj)
    have hw : InfinitePlace.IsReal (InfinitePlace.mk phi) := ⟨phi, hr, rfl⟩
    exact (InfinitePlace.not_isReal_iff_isComplex.mpr
      (NumberField.IsTotallyComplex.isComplex (InfinitePlace.mk phi))) hw
  refine ⟨phi, sigma, hconj, hne, ?_⟩
  intro x
  apply phi.injective
  calc
    phi (sigma (sigma x)) = star (phi (sigma x)) := hconj.eq _
    _ = star (star (phi x)) := congrArg star (hconj.eq x)
    _ = phi x := star_star _

def antiInvariantProjection (K : Type*) [Field K] [NumberField K]
    (sigma : K ≃ₐ[Rat] K) (x : K) : K := (x-sigma x)/2

theorem antiInvariantProjection_anti (K : Type*) [Field K] [NumberField K]
    (sigma : K ≃ₐ[Rat] K) (hinv : Function.Involutive sigma) (x : K) :
    sigma (antiInvariantProjection K sigma x) = -antiInvariantProjection K sigma x := by
  simp only [antiInvariantProjection, map_div, map_sub, map_ofNat, hinv]
  ring

theorem antiInvariantProjection_idempotent (K : Type*) [Field K] [NumberField K]
    (sigma : K ≃ₐ[Rat] K) (hinv : Function.Involutive sigma) (x : K) :
    antiInvariantProjection K sigma (antiInvariantProjection K sigma x) =
      antiInvariantProjection K sigma x := by
  change (antiInvariantProjection K sigma x-sigma (antiInvariantProjection K sigma x))/2 = _
  rw [antiInvariantProjection_anti K sigma hinv x]
  ring

private theorem exists_negative_rational_square (K : Type*) [Field K] [NumberField K]
    [NumberField.IsTotallyComplex K] (hdegree : Module.finrank Rat K = 2) :
    ∃ q : Rat, 0 < q ∧ ∃ u : K, u^2+algebraMap Rat K q=0 := by
  classical
  letI : Algebra.IsQuadraticExtension Rat K where
    toFree := inferInstance
    finrank_eq_two' := hdegree
  obtain ⟨phi, sigma, hconj, hne, hinv⟩ := exists_conjugation_operator K hdegree
  have hex : ∃ x : K, sigma x ≠ x := by
    by_contra! h
    apply hne
    ext x
    exact h x
  obtain ⟨x, hx⟩ := hex
  let u := antiInvariantProjection K sigma x
  have hu : u ≠ 0 := by
    dsimp [u, antiInvariantProjection]
    exact div_ne_zero (sub_ne_zero.mpr hx.symm) (by norm_num)
  have hanti : sigma u = -u := antiInvariantProjection_anti K sigma hinv x
  have hall (tau : K ≃ₐ[Rat] K) : tau=1 ∨ tau=sigma := by
    by_cases ht : tau=1
    · exact Or.inl ht
    · exact Or.inr (quadratic_nonidentity_aut_eq K hdegree ht hne)
  have hfixed : u^2 ∈ IntermediateField.fixedField (⊤ : Subgroup (K ≃ₐ[Rat] K)) := by
    rw [IntermediateField.mem_fixedField_iff]
    intro tau _
    rcases hall tau with ht | ht
    · rw [ht]
      rfl
    · rw [ht, map_pow, hanti, neg_sq]
  have hbot : IntermediateField.fixedField (⊤ : Subgroup (K ≃ₐ[Rat] K)) = ⊥ :=
    ((IsGalois.tfae Rat K).out 0 1).mp (inferInstance : IsGalois Rat K)
  have hmem : u^2 ∈ (⊥ : IntermediateField Rat K) := by
    rw [← hbot]
    exact hfixed
  obtain ⟨r, hr⟩ := IntermediateField.mem_bot.mp hmem
  have hp : phi u ≠ 0 := by
    intro h
    apply hu
    apply phi.injective
    simpa using h
  have hstar : star (phi u) = -phi u := by
    rw [← hconj.eq u, hanti, map_neg]
  have hre : (phi u).re = 0 := by
    have h := congrArg Complex.re hstar
    simp at h
    linarith
  have him : (phi u).im ≠ 0 := by
    intro h
    apply hp
    exact Complex.ext (by simpa using hre) (by simpa using h)
  have hrC : (r : Complex) = (phi u)^2 := by
    calc
      (r : Complex) = phi (algebraMap Rat K r) := (phi.toRatAlgHom.commutes r).symm
      _ = phi (u^2) := congrArg phi hr
      _ = (phi u)^2 := map_pow phi u 2
  have hrR : (r : Real) = -(phi u).im^2 := by
    simpa [pow_two, Complex.mul_re, hre] using congrArg Complex.re hrC
  have hrneg : r < 0 := by
    have h : (r : Real) < 0 := by
      rw [hrR]
      nlinarith [sq_pos_of_ne_zero him]
    exact_mod_cast h
  refine ⟨-r, by linarith, u, ?_⟩
  rw [map_neg, hr]
  ring

private theorem squarefree_root_of_positive_rational (K : Type*) [Field K] [NumberField K]
    (q : Rat) (hq : 0 < q) (u : K) (hu : u^2+algebraMap Rat K q=0) :
    ∃ d : Nat, 0 < d ∧ Squarefree d ∧ ∃ a : K, a^2+(d : K)=0 := by
  let A : Nat := q.num.natAbs
  let B : Nat := q.den
  let N := A*B
  have hnum : 0 < q.num := Rat.num_pos.mpr hq
  have hAint : (A : Int) = q.num := Int.natAbs_of_nonneg hnum.le
  have hA : 0 < A := by
    have h : (0 : Int) < A := by rw [hAint]; exact hnum
    exact_mod_cast h
  have hB : 0 < B := q.den_pos
  have hBq : (B : Rat) ≠ 0 := by exact_mod_cast hB.ne'
  have hAk : (A : Rat) = (q.num : Rat) := by exact_mod_cast hAint
  have hfrac : q=(A : Rat)/(B : Rat) := by
    rw [hAk]
    exact (Rat.num_div_den q).symm
  have hclear : (B : Rat)^2*q=(N : Rat) := by
    calc
      (B : Rat)^2*q = (B : Rat)^2*((A : Rat)/(B : Rat)) :=
        congrArg (fun z : Rat => (B : Rat)^2*z) hfrac
      _ = (N : Rat) := by
        dsimp [N]
        push_cast
        field_simp
        ring
  have hclearK : (B : K)^2*algebraMap Rat K q=(N : K) := by
    simpa only [map_mul, map_pow, map_natCast] using congrArg (algebraMap Rat K) hclear
  let z := (B : K)*u
  have hz : z^2+(N : K)=0 := by
    dsimp [z]
    rw [mul_pow]
    linear_combination (B : K)^2*hu-hclearK
  obtain ⟨d, b, hd, hb, hfactor, hsq⟩ := Nat.sq_mul_squarefree_of_pos (Nat.mul_pos hA hB)
  have hbK : (b : K) ≠ 0 := by exact_mod_cast hb.ne'
  have hfactorK : (b : K)^2*(d : K)=(N : K) := by exact_mod_cast hfactor
  refine ⟨d, hd, hsq, z/(b : K), ?_⟩
  field_simp
  linear_combination hz+hfactorK

theorem exists_squarefree_root_of_totallyComplex_degree_two
    (K : Type*) [Field K] [NumberField K] [NumberField.IsTotallyComplex K]
    (hdegree : Module.finrank Rat K = 2) :
    ∃ d : Nat, 0 < d ∧ Squarefree d ∧ ∃ a : K, a^2+(d : K)=0 := by
  obtain ⟨q, hq, u, hu⟩ := exists_negative_rational_square K hdegree
  exact squarefree_root_of_positive_rational K q hq u hu

private theorem totallyComplex_of_no_realAlgHom (K : Type*) [Field K] [NumberField K]
    (h : ¬ Nonempty (K →ₐ[Rat] Real)) : NumberField.IsTotallyComplex K := by
  constructor
  intro w
  apply InfinitePlace.not_isReal_iff_isComplex.mp
  intro hw
  exact h ⟨(InfinitePlace.isReal_iff.mp hw).embedding.toRatAlgHom⟩

theorem imaginaryQuadratic_isTotallyComplex (d : Nat) [Fact (0 < d)] :
    NumberField.IsTotallyComplex (ImaginaryQuadraticField d) := by
  apply totallyComplex_of_no_realAlgHom
  rintro ⟨f⟩
  have hr : (AdjoinRoot.root (evenFieldPoly d))^2+(d : ImaginaryQuadraticField d)=0 := by
    simpa using (eq_neg_iff_add_eq_zero.mp (evenField_root_sq d))
  have h : (f (AdjoinRoot.root (evenFieldPoly d)))^2+(d : Real)=0 := by
    simpa using congrArg f hr
  have hd : (0 : Real) < d := by exact_mod_cast (Fact.out : 0 < d)
  nlinarith [sq_nonneg (f (AdjoinRoot.root (evenFieldPoly d)))]

theorem totallyComplex_degree_two_classNumber_one_discriminant_bound
    (K : Type*) [Field K] [NumberField K] [NumberField.IsTotallyComplex K]
    (hdegree : Module.finrank Rat K = 2) (hclass : NumberField.classNumber K=1) :
    (NumberField.discr K).natAbs < 100000000000 := by
  obtain ⟨d, hd, hsq, a, ha⟩ := exists_squarefree_root_of_totallyComplex_degree_two K hdegree
  letI : Fact (0 < d) := ⟨hd⟩
  exact classNumber_one_discriminant_bound_of_quadratic_root d hsq K a ha hdegree hclass

end
end TenthDiscriminant
