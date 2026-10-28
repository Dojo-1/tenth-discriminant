import TenthDiscriminant.CoordinateTranslation

/-! Passive transport of actual bivariate polynomials, ordinary jets and the original Gram. -/
open scoped ComplexConjugate BigOperators Classical
namespace TenthDiscriminant.PassiveTransport
open Polynomial Matrix JetAssembly
set_option autoImplicit false
noncomputable section

section Rings
variable {A B : Type*} [CommRing A] [CommRing B]

def translate (a b : A) (F : Polynomial (Polynomial A)) : Polynomial (Polynomial A) :=
  Polynomial.taylor (Polynomial.C (-a))
    (F.map (Polynomial.taylorAlgHom (-b)).toRingHom)

private theorem map_taylor (phi : A →+* B) (f : Polynomial A) (a : A) :
    (Polynomial.taylor a f).map phi=Polynomial.taylor (phi a) (f.map phi) := by
  simp [Polynomial.taylor_apply,Polynomial.map_comp]

private theorem coefficient_comp (b d : A) :
    (Polynomial.taylorAlgHom (-b)).toRingHom.comp
      (Polynomial.taylorAlgHom (-d)).toRingHom=
    (Polynomial.taylorAlgHom (-(b+d))).toRingHom := by
  apply RingHom.ext
  intro f
  change Polynomial.taylor (-b) (Polynomial.taylor (-d) f)=Polynomial.taylor (-(b+d)) f
  rw [Polynomial.taylor_taylor]
  congr 1
  ring

private theorem derivative_taylor (f : Polynomial A) (a : A) :
    Polynomial.derivative (Polynomial.taylor a f)=
      Polynomial.taylor a (Polynomial.derivative f) := by
  simp [Polynomial.taylor_apply,Polynomial.derivative_comp]

theorem translate_zero (F : Polynomial (Polynomial A)) : translate 0 0 F=F := by
  have h : (Polynomial.taylorAlgHom (0 : A)).toRingHom=RingHom.id _ := by
    apply RingHom.ext
    intro f
    change Polynomial.taylor 0 f=f
    simp
  unfold translate
  simp only [neg_zero,Polynomial.C_0]
  rw [h]
  simp

theorem translate_add (a b c d : A) (F : Polynomial (Polynomial A)) :
    translate a b (translate c d F)=translate (a+c) (b+d) F := by
  unfold translate
  rw [map_taylor]
  have hc : (Polynomial.taylorAlgHom (-b)).toRingHom (Polynomial.C (-c))=Polynomial.C (-c) := by
    change Polynomial.taylor (-b) (Polynomial.C (-c))=Polynomial.C (-c)
    simp
  rw [hc]
  rw [Polynomial.taylor_taylor,Polynomial.map_map,coefficient_comp]
  have h : Polynomial.C (-a)+Polynomial.C (-c)=Polynomial.C (-(a+c)) := by
    simp [neg_add,add_comm]
  rw [h]

theorem translate_inverse (a b : A) (F : Polynomial (Polynomial A)) :
    translate (-a) (-b) (translate a b F)=F := by
  rw [translate_add]
  simpa using translate_zero F

theorem translate_map (phi : A →+* B) (a b : A) (F : Polynomial (Polynomial A)) :
    (translate a b F).map (Polynomial.mapRingHom phi)=
      translate (phi a) (phi b) (F.map (Polynomial.mapRingHom phi)) := by
  have hc : (Polynomial.mapRingHom phi).comp (Polynomial.taylorAlgHom (-b)).toRingHom=
      (Polynomial.taylorAlgHom (-(phi b))).toRingHom.comp (Polynomial.mapRingHom phi) := by
    apply RingHom.ext
    intro f
    change (Polynomial.taylor (-b) f).map phi=Polynomial.taylor (-(phi b)) (f.map phi)
    simpa using map_taylor phi f (-b)
  unfold translate
  rw [map_taylor]
  have ha : (Polynomial.mapRingHom phi) (Polynomial.C (-a))=Polynomial.C (-(phi a)) := by
    simp
  rw [ha,Polynomial.map_map,Polynomial.map_map,hc]

theorem derivative_translate (a b : A) (F : Polynomial (Polynomial A)) :
    Polynomial.derivative (translate a b F)=translate a b (Polynomial.derivative F) := by
  unfold translate
  rw [derivative_taylor,Polynomial.derivative_map]

theorem iterate_derivative_translate (a b : A) (F : Polynomial (Polynomial A)) (j : Nat) :
    (Polynomial.derivative^[j]) (translate a b F)=
      translate a b ((Polynomial.derivative^[j]) F) := by
  induction j generalizing F with
  | zero => rfl
  | succ j ih =>
    simp only [Function.iterate_succ_apply,derivative_translate]
    exact ih (Polynomial.derivative F)

theorem specialize_translate (a b w : A) (F : Polynomial (Polynomial A)) :
    (translate a b F).map (Polynomial.evalRingHom (w+b))=
      Polynomial.taylor (-a) (F.map (Polynomial.evalRingHom w)) := by
  have hc : (Polynomial.evalRingHom (w+b)).comp
      (Polynomial.taylorAlgHom (-b)).toRingHom=Polynomial.evalRingHom w := by
    apply RingHom.ext
    intro f
    change (Polynomial.taylor (-b) f).eval (w+b)=f.eval w
    rw [Polynomial.taylor_eval]
    simp
  unfold translate
  rw [map_taylor]
  simp only [Polynomial.coe_evalRingHom,Polynomial.eval_C,Polynomial.map_map,hc]

theorem jet_covariance (a b w z : A) (F : Polynomial (Polynomial A)) (j : Nat) :
    ((Polynomial.derivative^[j])
      ((translate a b F).map (Polynomial.evalRingHom (w+b)))).eval (z+a)=
    ((Polynomial.derivative^[j]) (F.map (Polynomial.evalRingHom w))).eval z := by
  rw [Polynomial.iterate_derivative_map,iterate_derivative_translate,
    specialize_translate,Polynomial.taylor_eval,Polynomial.iterate_derivative_map]
  simp
end Rings

def polynomialJet (F : Polynomial (Polynomial Complex)) (j : Nat) (z : Complex) : Complex :=
  ((Polynomial.derivative^[j]) (specialize F (conj z))).eval z

def monomialRow (r s : Nat) : Polynomial (Polynomial Complex) :=
  Polynomial.C (Polynomial.X^s)*Polynomial.X^r

def polynomialGram {n : Nat} (P : Finset Complex) (J : Nat)
    (F : Fin n → Polynomial (Polynomial Complex)) : Matrix (Fin n) (Fin n) Real :=
  fun i k => 2*(Finset.range J).sum (fun j =>
    P.sum (fun z => (polynomialJet (F i) j z*conj (polynomialJet (F k) j z)).re))

theorem conjugate_jet_covariance (F : Polynomial (Polynomial Complex)) (c z : Complex) (j : Nat) :
    polynomialJet (translate c (conj c) F) j (z+c)=polynomialJet F j z := by
  simpa [polynomialJet,specialize] using jet_covariance c (conj c) (conj z) z F j

theorem monomial_jet_eq (r s j : Nat) (z : Complex) :
    polynomialJet (monomialRow r s) j z=derivativeRow r s j z := by
  simpa [polynomialJet,monomialRow,specialize,rowSection] using
    rowSection_iterate_eval (fun _ : Fin 1 => (r,s)) (fun _ => 1) z j

theorem transported_lattice_jet (D r s j : Nat) (p v : Int × Int) :
    polynomialJet (translate (pairEval D v) (conj (pairEval D v)) (monomialRow r s))
      j (pairEval D (CoordinateTranslation.shift v p))=
    pairEval D (integerDerivativeRow D r s j p) := by
  rw [CoordinateTranslation.pairEval_shift,conjugate_jet_covariance,monomial_jet_eq]
  exact (integerDerivativeRow_eval D r s j p).symm

theorem polynomialGram_translation {n : Nat} (P : Finset Complex) (J : Nat)
    (F : Fin n → Polynomial (Polynomial Complex)) (c : Complex) :
    polynomialGram (P.image (fun z => z+c)) J (fun i => translate c (conj c) (F i))=
      polynomialGram P J F := by
  ext i k
  unfold polynomialGram
  congr 1
  apply Finset.sum_congr rfl
  intro j hj
  rw [Finset.sum_image]
  · apply Finset.sum_congr rfl
    intro z hz
    rw [conjugate_jet_covariance,conjugate_jet_covariance]
  · intro a ha b hb h
    exact add_right_cancel h

theorem monomial_gram_eq {n : Nat} (P : Finset Complex) (J : Nat) (rows : Fin n → Nat × Nat) :
    polynomialGram P J (fun i => monomialRow (rows i).1 (rows i).2)=traceGramMatrix P J rows := by
  ext i k
  simp only [polynomialGram,traceGramMatrix,traceGramEntry,monomial_jet_eq]

theorem passive_integer_cast (Q : Finset (Int × Int)) (D : Nat) (v : Int × Int)
    (J R S : Nat) (hD : 0<D) :
    polynomialGram ((Q.image (CoordinateTranslation.shift v)).image (pairEval D)) J
      (fun i : Fin (R*S) => translate (pairEval D v) (conj (pairEval D v))
        (monomialRow (i.val/S) (i.val%S)))=
    (integerRectangularTraceGram Q D J R S).map (Int.castRingHom Real) := by
  rw [CoordinateTranslation.shifted_points,polynomialGram_translation,
    monomial_gram_eq _ _ (fun i : Fin (R*S) => (i.val/S,i.val%S))]
  exact (integerRectangularTraceGram_cast Q D J R S hD).symm

theorem passive_det_cast (Q : Finset (Int × Int)) (D : Nat) (v : Int × Int)
    (J R S : Nat) (hD : 0<D) :
    (polynomialGram ((Q.image (CoordinateTranslation.shift v)).image (pairEval D)) J
      (fun i : Fin (R*S) => translate (pairEval D v) (conj (pairEval D v))
        (monomialRow (i.val/S) (i.val%S)))).det=
    ((integerRectangularTraceGram Q D J R S).det : Real) := by
  rw [passive_integer_cast Q D v J R S hD]
  exact (Int.cast_det (R := Real) _).symm

theorem passive_translation_bridge (Q : Finset (Int × Int)) (D : Nat) (v : Int × Int)
    (J R S p : Nat) (hD : 0<D) [Fact p.Prime] (hp2 : p≠2)
    (hns : ¬ IsSquare (-(D : ZMod p))) (hR : 1≤R) (hS : 1≤S) (hJ : S≤J)
    (hcard : 2*(R-1)+(S-1)<Q.card) :
    let G := integerRectangularTraceGram Q D J R S
    let H := polynomialGram ((Q.image (CoordinateTranslation.shift v)).image (pairEval D)) J
      (fun i : Fin (R*S) => translate (pairEval D v) (conj (pairEval D v))
        (monomialRow (i.val/S) (i.val%S)))
    H=G.map (Int.castRingHom Real) ∧ H.PosDef ∧ 0<G.det ∧
      (p : Int)^(2*valuationWeight R S p)∣G.det := by
  dsimp only
  have he : polynomialGram ((Q.image (CoordinateTranslation.shift v)).image (pairEval D)) J
      (fun i : Fin (R*S) => translate (pairEval D v) (conj (pairEval D v))
        (monomialRow (i.val/S) (i.val%S)))=
      rectangularTraceGram (Q.image (pairEval D)) J R S := by
    rw [CoordinateTranslation.shifted_points,polynomialGram_translation]
    exact monomial_gram_eq _ _ (fun i : Fin (R*S) => (i.val/S,i.val%S))
  have hp : (polynomialGram ((Q.image (CoordinateTranslation.shift v)).image (pairEval D)) J
      (fun i : Fin (R*S) => translate (pairEval D v) (conj (pairEval D v))
        (monomialRow (i.val/S) (i.val%S)))).PosDef := by
    rw [he]
    apply rectangularTraceGram_posDef_of_point_count _ J R S hR hS hJ
    rw [Finset.card_image_of_injective _ (show Function.Injective (pairEval D) from
      latticePoint_injective D hD)]
    exact hcard
  have hi : 0<(integerRectangularTraceGram Q D J R S).det := by
    have hr : 0<((integerRectangularTraceGram Q D J R S).det : Real) := by
      rw [←passive_det_cast Q D v J R S hD]
      exact hp.det_pos
    exact_mod_cast hr
  exact ⟨passive_integer_cast Q D v J R S hD,hp,hi,
    rectangularTraceGram_valuation_of_nonsquare Q D J R S p hp2 hns⟩

theorem passive_active_control :
    let Q : Finset (Int × Int) := {(-1,0),(0,0),(1,0)}
    (polynomialGram ((Q.image (CoordinateTranslation.shift (0,1))).image (pairEval 1)) 1
      (fun i : Fin (2*1) => translate Complex.I (-Complex.I)
        (monomialRow (i.val/1) (i.val%1)))).det=24 ∧
    (integerRectangularTraceGram (Q.image (CoordinateTranslation.shift (0,1))) 1 1 2 1).det=60 := by
  dsimp only
  have hc : pairEval 1 (0,1)=Complex.I := by norm_num [pairEval,latticePoint]
  have h := passive_det_cast {(-1,0),(0,0),(1,0)} 1 (0,1) 1 2 1 (by decide)
  have old := CoordinateTranslation.shifted_gram_counterexample
  dsimp only at old
  constructor
  · calc
      _ = ((integerRectangularTraceGram {(-1,0),(0,0),(1,0)} 1 1 2 1).det : Real) := by
        simpa [hc] using h
      _ = 24 := by exact_mod_cast old.1
  · exact old.2.1

theorem real_complex_control :
    (traceGramMatrix {Complex.I} 1 (fun i : Fin 2 => (i.val,0))).det=4 ∧
    ( !![(1 : Complex),-Complex.I;Complex.I,1] : Matrix (Fin 2) (Fin 2) Complex).det=0 := by
  refine ⟨traceGramMatrix_real_complex_control,?_⟩
  norm_num [Matrix.det_fin_two,Complex.I_mul_I]

theorem ordinary_derivative_control :
    polynomialJet (translate Complex.I (-Complex.I) (monomialRow 3 0)) 3 Complex.I=6 ∧
    polynomialJet (translate Complex.I (-Complex.I) (monomialRow 3 0)) 3 Complex.I≠1 := by
  have h : polynomialJet (translate Complex.I (-Complex.I) (monomialRow 3 0)) 3 Complex.I=6 := by
    simpa [monomial_jet_eq,derivativeRow,Nat.descFactorial] using
      conjugate_jet_covariance (monomialRow 3 0) Complex.I 0 3
  exact ⟨h,by rw [h]; norm_num⟩

theorem W_parameter_control :
    polynomialJet (translate Complex.I (-Complex.I) (monomialRow 0 1)) 1 (1+Complex.I)=0 ∧
    polynomialJet (translate Complex.I (-Complex.I) (monomialRow 0 1)) 0 (1+Complex.I)=1 := by
  constructor
  · simpa [monomial_jet_eq,derivativeRow] using
      conjugate_jet_covariance (monomialRow 0 1) Complex.I 1 1
  · simpa [monomial_jet_eq,derivativeRow] using
      conjugate_jet_covariance (monomialRow 0 1) Complex.I 1 0
end
end TenthDiscriminant.PassiveTransport

#check TenthDiscriminant.PassiveTransport.translate_zero
#check TenthDiscriminant.PassiveTransport.translate_add
#check TenthDiscriminant.PassiveTransport.translate_inverse
#check TenthDiscriminant.PassiveTransport.translate_map
#check TenthDiscriminant.PassiveTransport.derivative_translate
#check TenthDiscriminant.PassiveTransport.iterate_derivative_translate
#check TenthDiscriminant.PassiveTransport.specialize_translate
#check TenthDiscriminant.PassiveTransport.jet_covariance
#check TenthDiscriminant.PassiveTransport.conjugate_jet_covariance
#check TenthDiscriminant.PassiveTransport.monomial_jet_eq
#check TenthDiscriminant.PassiveTransport.transported_lattice_jet
#check TenthDiscriminant.PassiveTransport.polynomialGram_translation
#check TenthDiscriminant.PassiveTransport.monomial_gram_eq
#check TenthDiscriminant.PassiveTransport.passive_integer_cast
#check TenthDiscriminant.PassiveTransport.passive_det_cast
#check TenthDiscriminant.PassiveTransport.passive_translation_bridge
#check TenthDiscriminant.PassiveTransport.passive_active_control
#check TenthDiscriminant.PassiveTransport.real_complex_control
#check TenthDiscriminant.PassiveTransport.ordinary_derivative_control
#check TenthDiscriminant.PassiveTransport.W_parameter_control
#print TenthDiscriminant.PassiveTransport.translate
#print TenthDiscriminant.PassiveTransport.polynomialJet
#print TenthDiscriminant.PassiveTransport.monomialRow
#print TenthDiscriminant.PassiveTransport.polynomialGram
#print axioms TenthDiscriminant.PassiveTransport.jet_covariance
#print axioms TenthDiscriminant.PassiveTransport.passive_integer_cast
#print axioms TenthDiscriminant.PassiveTransport.passive_translation_bridge
#audit_namespace TenthDiscriminant.PassiveTransport

