import TenthDiscriminant.TunedAnalyticCutoff

/-! A field dictionary from a specified root and degree two.
This does not produce squarefree generators for arbitrary field types.
The actual discriminant is transported through a constructed equivalence. -/
namespace TenthDiscriminant
open Polynomial
set_option autoImplicit false
noncomputable section

theorem imaginaryQuadratic_finrank (d : Nat) [Fact (0 < d)] :
    Module.finrank Rat (ImaginaryQuadraticField d) = 2 := by
  simpa using Module.finrank_eq_card_basis (evenFieldBasis d)

/-- The quotient's root is sent to the root supplied by the caller. -/
def imaginaryQuadraticLiftOfRoot (d : Nat) (K : Type*) [Field K] [NumberField K]
    (a : K) (ha : a^2 + (d : K) = 0) :
    ImaginaryQuadraticField d →ₐ[Rat] K :=
  AdjoinRoot.liftHom (evenFieldPoly d) a (by simpa [evenFieldPoly] using ha)

theorem imaginaryQuadraticLiftOfRoot_root (d : Nat) (K : Type*) [Field K] [NumberField K]
    (a : K) (ha : a^2 + (d : K) = 0) :
    imaginaryQuadraticLiftOfRoot d K a ha (AdjoinRoot.root (evenFieldPoly d)) = a :=
  AdjoinRoot.liftHom_root _ _

/-- A nonzero field homomorphism between two-dimensional rational spaces is onto. -/
def imaginaryQuadraticEquivOfRoot (d : Nat) [Fact (0 < d)]
    (K : Type*) [Field K] [NumberField K] (a : K)
    (ha : a^2 + (d : K) = 0) (hdegree : Module.finrank Rat K = 2) :
    ImaginaryQuadraticField d ≃ₐ[Rat] K := by
  let f := imaginaryQuadraticLiftOfRoot d K a ha
  have hdim : Module.finrank Rat (ImaginaryQuadraticField d) = Module.finrank Rat K :=
    (imaginaryQuadratic_finrank d).trans hdegree.symm
  have hsurj : Function.Surjective f :=
    (LinearMap.injective_iff_surjective_of_finrank_eq_finrank hdim
      (f := f.toLinearMap)).mp f.injective
  exact AlgEquiv.ofBijective f ⟨f.injective, hsurj⟩

theorem imaginaryQuadraticEquivOfRoot_root (d : Nat) [Fact (0 < d)]
    (K : Type*) [Field K] [NumberField K] (a : K)
    (ha : a^2 + (d : K) = 0) (hdegree : Module.finrank Rat K = 2) :
    imaginaryQuadraticEquivOfRoot d K a ha hdegree
      (AdjoinRoot.root (evenFieldPoly d)) = a :=
  imaginaryQuadraticLiftOfRoot_root d K a ha

/-- The degree guard is also necessary for any such field identification. -/
theorem imaginaryQuadratic_degree_of_equiv (d : Nat) [Fact (0 < d)]
    (K : Type*) [Field K] [NumberField K]
    (e : ImaginaryQuadraticField d ≃ₐ[Rat] K) : Module.finrank Rat K = 2 :=
  e.toLinearEquiv.finrank_eq.symm.trans (imaginaryQuadratic_finrank d)

theorem classNumber_one_radicand_bound_of_quadratic_root
    (d : Nat) [Fact (0 < d)] (hsq : Squarefree d)
    (K : Type*) [Field K] [NumberField K] (a : K)
    (ha : a^2 + (d : K) = 0) (hdegree : Module.finrank Rat K = 2)
    (hclass : NumberField.classNumber K = 1) : d < 100000000000 := by
  let e := imaginaryQuadraticEquivOfRoot d K a ha hdegree
  have hc := classNumber_one_of_field_equiv K (ImaginaryQuadraticField d) e.symm hclass
  exact imaginaryQuadratic_classNumber_one_radicand_bound_100b d hsq hc

theorem classNumber_one_discriminant_bound_of_quadratic_root
    (d : Nat) [Fact (0 < d)] (hsq : Squarefree d)
    (K : Type*) [Field K] [NumberField K] (a : K)
    (ha : a^2 + (d : K) = 0) (hdegree : Module.finrank Rat K = 2)
    (hclass : NumberField.classNumber K = 1) :
    (NumberField.discr K).natAbs < 100000000000 := by
  let e := imaginaryQuadraticEquivOfRoot d K a ha hdegree
  have hc := classNumber_one_of_field_equiv K (ImaginaryQuadraticField d) e.symm hclass
  rw [NumberField.discr_eq_discr_of_algEquiv K e.symm]
  exact imaginaryQuadratic_classNumber_one_discriminant_bound_100b d hsq hc

end
end TenthDiscriminant
