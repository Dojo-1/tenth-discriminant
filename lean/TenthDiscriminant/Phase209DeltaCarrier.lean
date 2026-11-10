import Mathlib.Algebra.MvPolynomial.PDeriv

/-!
Phase209 — the ACTUAL integral three-variable derivation carrier.

This is the first concrete Mathlib bridge from the paper-level delta
operator to an audited integer polynomial. The important p²-iterate
divisibility statement is NOT proved here: the following only proves
that the operator exists with the specified source generator action.
The full ordinary-jet substitution and p² base-step are separate.
-/
namespace TenthDiscriminant.Phase209DeltaCarrier

inductive Variable
  | z | w | t
  deriving DecidableEq

abbrev Carrier := MvPolynomial Variable ℤ

noncomputable def delta (p : ℕ) : Derivation ℤ Carrier Carrier :=
  MvPolynomial.mkDerivation ℤ fun v =>
    match v with
    | .z => 1
    | .w => 0
    | .t => (MvPolynomial.X Variable.z : Carrier) ^ (p - 1)

/-- The integer coefficient derivation acts on Z as ordinary d/dZ. -/
theorem delta_z (p : ℕ) :
    delta p (MvPolynomial.X Variable.z) = (1 : Carrier) := by
  simp [delta]

/-- The W-source is fixed during every ordinary Z-derivative. -/
theorem delta_w (p : ℕ) :
    delta p (MvPolynomial.X Variable.w) = (0 : Carrier) := by
  simp [delta]

/-- The auxiliary divided Frobenius variable has its actual derivative. -/
theorem delta_t (p : ℕ) :
    delta p (MvPolynomial.X Variable.t) =
      (MvPolynomial.X Variable.z : Carrier) ^ (p - 1) := by
  simp [delta]

/-- Constants really are constant, as required for integer coefficients. -/
theorem delta_int_constant (p : ℕ) (c : ℤ) :
    delta p (MvPolynomial.C c) = (0 : Carrier) :=
  MvPolynomial.derivation_C (delta p) c

end TenthDiscriminant.Phase209DeltaCarrier

#print axioms TenthDiscriminant.Phase209DeltaCarrier.delta_z
#print axioms TenthDiscriminant.Phase209DeltaCarrier.delta_t
#print axioms TenthDiscriminant.Phase209DeltaCarrier.delta_int_constant
