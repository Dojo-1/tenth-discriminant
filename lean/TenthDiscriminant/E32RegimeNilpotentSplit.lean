import TenthDiscriminant.E31ConductorGramNegative

/-!
# E32 — Nonreduced conductor source versus split Gaussian target

Two local arithmetic regimes can share an ambient rational field while
being structurally inequivalent modulo a conductor prime.

At D=1,k=5:
  source A_25/5 = F5[t]/(t^2), nonreduced;
  target A_1/5 = F5[t]/(t^2+1), reduced and split.

We directly prove a nonzero square-zero SOURCE witness and that the
TARGET has no nonzero square-zero element, using the E28 exact
coefficient-pair multiplication law.

The induced conductor frame is multiplicative but not injective. No
zero-preserving, square-compatible injective map between these two
finite pair algebras can exist.

No field-discriminant theorem or p-adic valuation is inferred.
-/

namespace TenthDiscriminant.E32
set_option autoImplicit false
noncomputable section

/-- The source mod-5 imaginary generator is nonzero and square-zero. -/
theorem source_mod5_has_nonzero_squarezero :
    E28.residueMul 5 25 (0,1) (0,1) = (0,0) ∧
      ((0,1) : ZMod 5 × ZMod 5) ≠ (0,0) := by
  constructor <;> decide

/-- Target Gaussian multiplication mod 5 is reduced at square-zero
elements. This exact finite test does not invoke any abstract
number-field or prime-ideal API. -/
theorem target_mod5_squarezero_implies_zero
    (p : ZMod 5 × ZMod 5)
    (hp : E28.residueMul 5 1 p p = (0,0)) :
    p = (0,0) := by
  have hfull :
      ∀ q : ZMod 5 × ZMod 5,
        E28.residueMul 5 1 q q = (0,0) → q = (0,0) := by
    decide
  exact hfull p hp

/-- The source nilpotent maps to zero in the target. -/
theorem conductor_frame_kills_nilpotent :
    E28.residueFrame 5 5 (0,1) = (0,0) := by decide

/-- The E28 source multiplication transport is honest even though
the conductor frame itself is noninjective at the bad prime. -/
theorem conductor_frame_preserves_mul
    (a b : ZMod 5 × ZMod 5) :
    E28.residueFrame 5 5 (E28.residueMul 5 25 a b) =
      E28.residueMul 5 1
        (E28.residueFrame 5 5 a)
        (E28.residueFrame 5 5 b) := by
  simpa using E28.residueFrame_mul 5 1 5 a b

/-- A zero-preserving, square-compatible map cannot be injective
from a ring with a nonzero nilpotent into a reduced target. The
obstruction is an actual algebraic source witness, not a scalar loss
score or a Riemannian curvature claim. -/
theorem no_injective_zero_square_compatible_map
    (f : (ZMod 5 × ZMod 5) → (ZMod 5 × ZMod 5))
    (hzero : f (0,0) = (0,0))
    (hsquare : ∀ p, f (E28.residueMul 5 25 p p) =
      E28.residueMul 5 1 (f p) (f p)) :
    ¬ Function.Injective f := by
  intro hf
  have hsource := source_mod5_has_nonzero_squarezero
  have hsq := hsquare (0,1)
  rw [hsource.1, hzero] at hsq
  have htarget :
      f (0,1) = (0,0) :=
    target_mod5_squarezero_implies_zero (f (0,1)) hsq.symm
  have heq : ((0,1) : ZMod 5 × ZMod 5) = (0,0) := by
    apply hf
    rw [htarget, hzero]
  exact hsource.2 heq

/-- Instantiate the negative-control with the actual conductor
frame itself, which indeed satisfies the transport obligations. -/
theorem actual_conductor_map_not_injective :
    ¬ Function.Injective (E28.residueFrame 5 5) :=
  E31.mod5_conductor_five_not_injective

end
end TenthDiscriminant.E32

#print axioms TenthDiscriminant.E32.source_mod5_has_nonzero_squarezero
#print axioms TenthDiscriminant.E32.target_mod5_squarezero_implies_zero
#print axioms TenthDiscriminant.E32.conductor_frame_kills_nilpotent
#print axioms TenthDiscriminant.E32.conductor_frame_preserves_mul
#print axioms TenthDiscriminant.E32.no_injective_zero_square_compatible_map
