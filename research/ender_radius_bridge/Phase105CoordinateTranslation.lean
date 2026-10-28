import TenthDiscriminant

/-! Actual two-dimensional charts and literal lattice shifts, with guarded invariants. -/
open scoped NumberField nonZeroDivisors BigOperators Classical ComplexConjugate
namespace TenthDiscriminant.CoordinateTranslation
open Matrix Polynomial
set_option autoImplicit false
noncomputable section

def shift (v : Int × Int) : (Int × Int) ≃ (Int × Int) where
  toFun p := p+v
  invFun p := p-v
  left_inv := by intro p; simp
  right_inv := by intro p; simp

def orderPoint (D : Nat) (p : Int × Int) : AdjoinRoot (evenOrderPoly D) :=
  AdjoinRoot.of (evenOrderPoly D) p.1+
    AdjoinRoot.of (evenOrderPoly D) p.2*AdjoinRoot.root (evenOrderPoly D)

def embedding (D : Nat) : EvenQuadraticField D →ₐ[Rat] Complex := by
  have hz : (pairEval D (0,1))^2+(D : Complex)=0 := by
    rw [pow_two,←pairEval_mul D (0,1) (0,1)]
    simp [pairMul,pairEval,latticePoint]
  exact AdjoinRoot.liftHom (evenFieldPoly D) (pairEval D (0,1))
    (by simpa [evenFieldPoly] using hz)

def integralPoint (D : Nat) [Fact (0<D)] (p : Int × Int) : 𝓞 (EvenQuadraticField D) :=
  evenOrderToRingOfIntegers D (orderPoint D p)

def oddCoordinates (p : Int × Int) : Int × Int := (p.1-p.2,2*p.2)

theorem shift_zero (p : Int × Int) : shift 0 p=p := by simp [shift]

theorem shift_comp (u v p : Int × Int) : shift u (shift v p)=shift (u+v) p := by
  simp [shift,add_assoc,add_comm,add_left_comm]

theorem shift_inverse (v p : Int × Int) : shift (-v) (shift v p)=p := by
  simp [shift,add_assoc]

theorem pairEval_shift (D : Nat) (p v : Int × Int) :
    pairEval D (shift v p)=pairEval D p+pairEval D v := by
  apply Complex.ext <;> simp [shift,pairEval,latticePoint,add_mul] <;> ring

theorem pairEval_sub (D : Nat) (p q : Int × Int) :
    pairEval D (p-q)=pairEval D p-pairEval D q := by
  apply Complex.ext <;> simp [pairEval,latticePoint,sub_mul] <;> ring

theorem metric_translation (D : Nat) (p q v : Int × Int) :
    Complex.normSq (pairEval D (shift v p)-pairEval D (shift v q))=
      Complex.normSq (pairEval D p-pairEval D q) := by
  rw [pairEval_shift,pairEval_shift]
  congr 1
  abel

theorem orderPoint_to_field (D : Nat) [Fact (0<D)] (p : Int × Int) :
    evenOrderToField D (orderPoint D p)=
      (p.1 : EvenQuadraticField D)+(p.2 : EvenQuadraticField D)*AdjoinRoot.root (evenFieldPoly D) := by
  simp [orderPoint,evenOrderToField]

theorem embedding_root (D : Nat) :
    embedding D (AdjoinRoot.root (evenFieldPoly D))=pairEval D (0,1) := by
  simp [embedding]

theorem integralPoint_eval (D : Nat) [Fact (0<D)] (p : Int × Int) :
    embedding D (integralPoint D p : EvenQuadraticField D)=pairEval D p := by
  change embedding D (evenOrderToField D (orderPoint D p))=pairEval D p
  rw [orderPoint_to_field,map_add,map_mul]
  simp only [map_intCast,embedding_root]
  simp [pairEval,latticePoint] <;> ring

theorem integralPoint_shift (D : Nat) [Fact (0<D)] (p v : Int × Int) :
    integralPoint D (shift v p)=integralPoint D p+integralPoint D v := by
  unfold integralPoint
  rw [←map_add]
  congr 1
  simp [shift,orderPoint,map_add,add_mul] <;> ring

theorem integralPoint_norm (D : Nat) [Fact (0<D)] (p : Int × Int) :
    Algebra.norm Int (integralPoint D p)=p.1^2+(D : Int)*p.2^2 := by
  exact evenOrder_ringOfIntegers_norm D p.1 p.2

theorem coordinate_norm_commutes (D : Nat) [Fact (0<D)] (p : Int × Int) :
    (Algebra.norm Int (integralPoint D p) : Real)=Complex.normSq (pairEval D p) := by
  rw [integralPoint_norm]
  change ((p.1^2+(D : Int)*p.2^2 : Int) : Real)=
    Complex.normSq (latticePoint (D : Real) p.1 p.2)
  rw [latticePoint_normSq _ (Nat.cast_nonneg D)]
  push_cast <;> ring

theorem even_coordinates_bijective (D : Nat) [Fact (0<D)] (hsq : Squarefree D)
    (hm : (D : Int)%4=1 ∨ (D : Int)%4=2) : Function.Bijective (integralPoint D) := by
  constructor
  · intro p q hpq
    have he := congrArg (fun z : 𝓞 (EvenQuadraticField D) =>
      embedding D (z : EvenQuadraticField D)) hpq
    dsimp only at he
    rw [integralPoint_eval,integralPoint_eval] at he
    exact latticePoint_injective D Fact.out he
  · intro z
    obtain ⟨w,hw⟩ := evenOrderToRingOfIntegers_surjective D hsq hm z
    obtain ⟨x,y,hxy⟩ := evenOrder_coordinates D w
    refine ⟨(x,y),?_⟩
    rw [hxy] at hw
    exact hw

theorem actual_integer_norm_commutes (D : Nat) [Fact (0<D)] (hsq : Squarefree D)
    (hm : (D : Int)%4=1 ∨ (D : Int)%4=2) (z : 𝓞 (EvenQuadraticField D)) :
    (Algebra.norm Int z : Real)=Complex.normSq (embedding D (z : EvenQuadraticField D)) := by
  obtain ⟨p,rfl⟩ := (even_coordinates_bijective D hsq hm).2 z
  rw [integralPoint_eval]
  exact coordinate_norm_commutes D p

theorem odd_coordinate_matrix (p : Int × Int) :
    ( !![(1 : Int),-1;0,2] : Matrix (Fin 2) (Fin 2) Int).mulVec ![p.1,p.2]=
      ![(oddCoordinates p).1,(oddCoordinates p).2] ∧
    ( !![(1 : Int),-1;0,2] : Matrix (Fin 2) (Fin 2) Int).det=2 ∧
    (∀ q : Int × Int, (∃ a, oddCoordinates a=q) ↔ 2∣q.2) := by
  refine ⟨?_,?_,?_⟩
  · ext i
    fin_cases i <;> simp [Matrix.mulVec,dotProduct,Fin.sum_univ_two,oddCoordinates] <;> ring
  · norm_num [Matrix.det_fin_two]
  · intro q
    constructor
    · rintro ⟨a,rfl⟩
      exact ⟨a.2,rfl⟩
    · rintro ⟨y,hy⟩
      refine ⟨(q.1+y,y),?_⟩
      apply Prod.ext
      · simp [oddCoordinates]
      · simpa only [oddCoordinates] using hy.symm

theorem odd_coordinate_shift (p v : Int × Int) :
    oddCoordinates (shift v p)=oddCoordinates p+oddCoordinates v := by
  apply Prod.ext <;> simp [oddCoordinates,shift] <;> ring

theorem odd_coordinate_norm (D : Nat) [Fact ((D : Int)%4=3)] (p : Int × Int) :
    principalNorm (D : Int) (oddCoordinates p).1 (oddCoordinates p).2=
      p.1^2+(D : Int)*p.2^2 := by
  have hfour : 4*(((D : Int)+1)/4)=(D : Int)+1 := by
    have hm := (Fact.out : (D : Int)%4=3)
    omega
  dsimp [oddCoordinates,principalNorm]
  linear_combination p.2^2*hfour

theorem odd_order_norm_commutes (D : Nat) [Fact ((D : Int)%4=3)] (p : Int × Int) :
    Algebra.norm Int (AdjoinRoot.of (halfOrderPolynomial D) (oddCoordinates p).1+
      AdjoinRoot.of (halfOrderPolynomial D) (oddCoordinates p).2*
        AdjoinRoot.root (halfOrderPolynomial D))=p.1^2+(D : Int)*p.2^2 := by
  rw [halfOrder_norm_eq_principalNorm]
  exact odd_coordinate_norm D p

theorem shifted_points (D : Nat) (Q : Finset (Int × Int)) (v : Int × Int) :
    (Q.image (shift v)).image (pairEval D)=
      (Q.image (pairEval D)).image (fun z => z+pairEval D v) := by
  rw [Finset.image_image,Finset.image_image]
  congr 1
  funext p
  exact pairEval_shift D p v

theorem shifted_card (Q : Finset (Int × Int)) (v : Int × Int) :
    (Q.image (shift v)).card=Q.card := by
  exact Finset.card_image_of_injective Q (shift v).injective

theorem shifted_ellipse_membership (D rho : Nat) [Fact (0<D)] (c p : Int × Int) :
    p ∈ (ellipsePairs D rho).image (shift c) ↔
      (p-c).1^2+(D : Int)*(p-c).2^2≤(rho : Int)^2 := by
  constructor
  · intro h
    obtain ⟨q,hq,rfl⟩ := Finset.mem_image.mp h
    simpa [shift] using (mem_ellipsePairs_iff D rho Fact.out q.1 q.2).mp hq
  · intro h
    refine Finset.mem_image.mpr ⟨p-c,?_,?_⟩
    · exact (mem_ellipsePairs_iff D rho Fact.out (p-c).1 (p-c).2).mpr h
    · simp [shift]

theorem shifted_gram_cast (D : Nat) [Fact (0<D)] (Q : Finset (Int × Int))
    (v : Int × Int) (J R S : Nat) :
    (integerRectangularTraceGram (Q.image (shift v)) D J R S).map (Int.castRingHom Real)=
      rectangularTraceGram ((Q.image (pairEval D)).image (fun z => z+pairEval D v)) J R S := by
  have he := integerRectangularTraceGram_cast (Q.image (shift v)) D J R S Fact.out
  rw [shifted_points] at he
  exact he

theorem shifted_valuation (D : Nat) (Q : Finset (Int × Int)) (v : Int × Int)
    (J R S p : Nat) [Fact p.Prime] (hp2 : p≠2) (hns : ¬ IsSquare (-(D : ZMod p))) :
    (p : Int)^(2*valuationWeight R S p) ∣
      (integerRectangularTraceGram (Q.image (shift v)) D J R S).det := by
  exact rectangularTraceGram_valuation_of_nonsquare (Q.image (shift v)) D J R S p hp2 hns

theorem shifted_posDef (D : Nat) [Fact (0<D)] (Q : Finset (Int × Int))
    (v : Int × Int) (J R S : Nat) (hR : 1≤R) (hS : 1≤S) (hJ : S≤J)
    (hcard : 2*(R-1)+(S-1)<Q.card) :
    (rectangularTraceGram ((Q.image (pairEval D)).image (fun z => z+pairEval D v)) J R S).PosDef := by
  rw [←shifted_points]
  apply rectangularTraceGram_posDef_of_point_count _ J R S hR hS hJ
  rw [Finset.card_image_of_injective _ (show Function.Injective (pairEval D) from
    latticePoint_injective D Fact.out),shifted_card]
  exact hcard

theorem coordinate_translation_bridge (D : Nat) [Fact (0<D)] (hsq : Squarefree D)
    (hm : (D : Int)%4=1 ∨ (D : Int)%4=2) (Q : Finset (Int × Int)) (v : Int × Int)
    (J R S p : Nat) [Fact p.Prime] (hR : 1≤R) (hS : 1≤S) (hJ : S≤J)
    (hcard : 2*(R-1)+(S-1)<Q.card) (hp2 : p≠2) (hns : ¬ IsSquare (-(D : ZMod p))) :
    Function.Bijective (integralPoint D) ∧
    (∀ u w a, shift u (shift w a)=shift (u+w) a) ∧
    (∀ a, integralPoint D (shift v a)=integralPoint D a+integralPoint D v) ∧
    (∀ a, embedding D (integralPoint D (shift v a) : EvenQuadraticField D)=
      embedding D (integralPoint D a : EvenQuadraticField D)+pairEval D v) ∧
    (∀ z : 𝓞 (EvenQuadraticField D), (Algebra.norm Int z : Real)=
      Complex.normSq (embedding D (z : EvenQuadraticField D))) ∧
    (Q.image (shift v)).card=Q.card ∧
    (integerRectangularTraceGram (Q.image (shift v)) D J R S).map (Int.castRingHom Real)=
      rectangularTraceGram ((Q.image (pairEval D)).image (fun z => z+pairEval D v)) J R S ∧
    (rectangularTraceGram ((Q.image (pairEval D)).image (fun z => z+pairEval D v)) J R S).PosDef ∧
    (p : Int)^(2*valuationWeight R S p) ∣
      (integerRectangularTraceGram (Q.image (shift v)) D J R S).det := by
  refine ⟨even_coordinates_bijective D hsq hm,shift_comp,(fun a => integralPoint_shift D a v),
    ?_,actual_integer_norm_commutes D hsq hm,shifted_card Q v,
    shifted_gram_cast D Q v J R S,shifted_posDef D Q v J R S hR hS hJ hcard,
    shifted_valuation D Q v J R S p hp2 hns⟩
  intro a
  rw [integralPoint_eval,pairEval_shift,integralPoint_eval]

theorem shifted_gram_counterexample :
    let Q : Finset (Int × Int) := {(-1,0),(0,0),(1,0)}
    (integerRectangularTraceGram Q 1 1 2 1).det=24 ∧
      (integerRectangularTraceGram (Q.image (shift (0,1))) 1 1 2 1).det=60 ∧
      2*(2-1)+(1-1)<Q.card := by
  dsimp only
  refine ⟨?_,?_,by decide⟩
  · rw [Matrix.det_fin_two]
    norm_num [integerRectangularTraceGram,integerTraceGramMatrix,integerTraceGramEntry,
      integerPairTrace,integerDerivativeRow,pairScale,pairMul,pairPow,pairConj,
      Finset.sum_range_succ,Nat.descFactorial]
    have hc : ({0,(1,0)} : Finset (Int × Int)).card=2 := by decide
    norm_num [hc]
  · rw [Matrix.det_fin_two]
    norm_num [integerRectangularTraceGram,integerTraceGramMatrix,integerTraceGramEntry,
      integerPairTrace,integerDerivativeRow,pairScale,pairMul,pairPow,pairConj,
      shift,Finset.sum_range_succ,Nat.descFactorial]

theorem zero_discriminant_control : pairEval 0 (0,0)=pairEval 0 (0,1) ∧
    (0,0)≠((0,1) : Int × Int) := by
  constructor
  · simp [pairEval,latticePoint]
  · decide

theorem odd_index_control :
    ( !![(1 : Int),-1;0,2] : Matrix (Fin 2) (Fin 2) Int).det=2 ∧
      ( !![(1 : Int),-1;0,2] : Matrix (Fin 2) (Fin 2) Int).det≠1 := by
  norm_num [Matrix.det_fin_two]

theorem additive_axes_control : shift (2,3) (shift (-1,4) (5,-2))=(6,5) := by
  norm_num [shift]
end
end TenthDiscriminant.CoordinateTranslation

#check TenthDiscriminant.CoordinateTranslation.shift_zero
#check TenthDiscriminant.CoordinateTranslation.shift_comp
#check TenthDiscriminant.CoordinateTranslation.shift_inverse
#check TenthDiscriminant.CoordinateTranslation.pairEval_shift
#check TenthDiscriminant.CoordinateTranslation.pairEval_sub
#check TenthDiscriminant.CoordinateTranslation.metric_translation
#check TenthDiscriminant.CoordinateTranslation.orderPoint_to_field
#check TenthDiscriminant.CoordinateTranslation.embedding_root
#check TenthDiscriminant.CoordinateTranslation.integralPoint_eval
#check TenthDiscriminant.CoordinateTranslation.integralPoint_shift
#check TenthDiscriminant.CoordinateTranslation.integralPoint_norm
#check TenthDiscriminant.CoordinateTranslation.coordinate_norm_commutes
#check TenthDiscriminant.CoordinateTranslation.even_coordinates_bijective
#check TenthDiscriminant.CoordinateTranslation.actual_integer_norm_commutes
#check TenthDiscriminant.CoordinateTranslation.odd_coordinate_matrix
#check TenthDiscriminant.CoordinateTranslation.odd_coordinate_shift
#check TenthDiscriminant.CoordinateTranslation.odd_coordinate_norm
#check TenthDiscriminant.CoordinateTranslation.odd_order_norm_commutes
#check TenthDiscriminant.CoordinateTranslation.shifted_points
#check TenthDiscriminant.CoordinateTranslation.shifted_card
#check TenthDiscriminant.CoordinateTranslation.shifted_ellipse_membership
#check TenthDiscriminant.CoordinateTranslation.shifted_gram_cast
#check TenthDiscriminant.CoordinateTranslation.shifted_valuation
#check TenthDiscriminant.CoordinateTranslation.shifted_posDef
#check TenthDiscriminant.CoordinateTranslation.coordinate_translation_bridge
#check TenthDiscriminant.CoordinateTranslation.shifted_gram_counterexample
#check TenthDiscriminant.CoordinateTranslation.zero_discriminant_control
#check TenthDiscriminant.CoordinateTranslation.odd_index_control
#check TenthDiscriminant.CoordinateTranslation.additive_axes_control
#print TenthDiscriminant.CoordinateTranslation.shift
#print TenthDiscriminant.CoordinateTranslation.orderPoint
#print TenthDiscriminant.CoordinateTranslation.embedding
#print TenthDiscriminant.CoordinateTranslation.integralPoint
#print TenthDiscriminant.CoordinateTranslation.oddCoordinates
#print axioms TenthDiscriminant.CoordinateTranslation.coordinate_translation_bridge
#print axioms TenthDiscriminant.CoordinateTranslation.odd_order_norm_commutes
#print axioms TenthDiscriminant.CoordinateTranslation.shifted_gram_counterexample
#audit_namespace TenthDiscriminant.CoordinateTranslation

open Lean Elab Command

elab "#phase105_inputs " root:ident : command => do
  let env ← getEnv
  let target := root.getId
  unless env.checked.get.find? target |>.isSome do
    throwError "PHASE105_ROOT_MISSING {target}"
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
    ``TenthDiscriminant.EvenMinkowski.actual_minkowski,
    ``TenthDiscriminant.EvenMinkowski.normalized_actual_gram_budget,
    ``TenthDiscriminant.EvenMinkowski.scalar_actual_gram_budget,
    ``TenthDiscriminant.EvenSplitPrimeBudget.actual_gram_budget,
    ``TenthDiscriminant.EvenClassAggregation.prime_prefix_bound,
    ``TenthDiscriminant.EvenClassAggregation.uniform_two_class_bound,
    ``TenthDiscriminant.EvenPrimeFamily.controlled_family]
  for name in forbidden do
    if state.visited.contains name then
      throwError "PHASE105_FORBIDDEN_INPUT {target}: {name}"
  let mut count := 0
  for name in state.visited do
    count := count+1
    match env.checked.get.find? name with
    | none => throwError "PHASE105_UNRESOLVED {name}"
    | some info => if info.isUnsafe then throwError "PHASE105_UNSAFE_INPUT {name}"
  for name in state.axioms do
    unless name==``propext || name==``Classical.choice || name==``Quot.sound do
      throwError "PHASE105_NONSTANDARD_AXIOM {name}"
  logInfo m!"PHASE105_INPUTS_OK {target}: {count} reached; none of listed h1/old-cutoff/classification/finite-answer inputs; axioms {state.axioms}"






#phase105_inputs TenthDiscriminant.CoordinateTranslation.coordinate_translation_bridge
#phase105_inputs TenthDiscriminant.CoordinateTranslation.odd_order_norm_commutes
#phase105_inputs TenthDiscriminant.CoordinateTranslation.shifted_gram_counterexample
