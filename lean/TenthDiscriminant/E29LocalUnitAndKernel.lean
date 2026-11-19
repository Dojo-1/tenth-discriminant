import TenthDiscriminant.E28ConductorResidue

/-!
# E29 — Exact modular unit gate and graded reconstruction fibers

This continues the E24-E28 ORIGINAL quadratic integer-pair arithmetic carrier.
The index-k order inclusion is injective over Z (k > 0), but its local
coefficient-pair reductions have different reconstructibility at each modulus.

New universal theorem: residueFrame m k is bijective iff the residue of k
has a two-sided modular inverse (encoded as the explicit left-inverse
witness t*k=1). This includes m=0, where ZMod 0 is Z, and m=1, the
trivial quotient, without silently assuming primality.

An exact fiber characterization and finite power-of-two controls make
loss of information visible at different observation depths. These are
coefficient-pair statements, NOT prime-ideal valuations, a p-adic
classification theorem or a bound on the original integer trace-Gram.
-/

namespace TenthDiscriminant.E29

set_option autoImplicit false

/-- A scalar frame with explicitly provided modular coefficient.
Used for the inverse without pretending every integer k is invertible. -/
def coefficientFrame (m : Nat) (c : ZMod m)
    (p : ZMod m × ZMod m) : ZMod m × ZMod m :=
  (p.1, c * p.2)

/-- Mod-m scalar frames compose exactly, independent of the arithmetic
quadratic parameter D. -/
theorem coefficientFrame_compose (m : Nat) (c d : ZMod m)
    (p : ZMod m × ZMod m) :
    coefficientFrame m c (coefficientFrame m d p) =
      coefficientFrame m (c*d) p := by
  apply Prod.ext
  · rfl
  · simp only [coefficientFrame]
    ring

/-- A modular inverse witness reconstructs an original residue point
after a conductor frame change. -/
theorem unit_witness_left_reconstruct (m k : Nat) (u : ZMod m)
    (hu : u * (k : ZMod m) = 1) (p : ZMod m × ZMod m) :
    coefficientFrame m u (E28.residueFrame m k p) = p := by
  rcases p with ⟨a,b⟩
  apply Prod.ext
  · rfl
  · change u * ((k : ZMod m) * b) = b
    calc
      _ = (u * (k : ZMod m)) * b := by ring
      _ = b := by rw [hu]; ring

/-- The same modular witness also reconstructs the target from the
source. This is a true two-sided inverse, not a partial formal one. -/
theorem unit_witness_right_reconstruct (m k : Nat) (u : ZMod m)
    (hu : u * (k : ZMod m) = 1) (p : ZMod m × ZMod m) :
    E28.residueFrame m k (coefficientFrame m u p) = p := by
  rcases p with ⟨a,b⟩
  apply Prod.ext
  · rfl
  · change (k : ZMod m) * (u * b) = b
    calc
      _ = (u * (k : ZMod m)) * b := by ring
      _ = b := by rw [hu]; ring

theorem frame_bijective_of_unit_witness (m k : Nat) (u : ZMod m)
    (hu : u * (k : ZMod m) = 1) :
    Function.Bijective (E28.residueFrame m k) := by
  constructor
  · intro a b hab
    have h := congrArg (coefficientFrame m u) hab
    simpa only [unit_witness_left_reconstruct m k u hu] using h
  · intro p
    exact ⟨coefficientFrame m u p,
      unit_witness_right_reconstruct m k u hu p⟩

/-- Surjectivity must recover the source imaginary coordinate of (0,1);
therefore the scalar conductor is a unit at this modulus. -/
theorem unit_witness_of_frame_surjective (m k : Nat)
    (hs : Function.Surjective (E28.residueFrame m k)) :
    ∃ u : ZMod m, u * (k : ZMod m) = 1 := by
  obtain ⟨q,hq⟩ := hs (0,1)
  refine ⟨q.2, ?_⟩
  have hsecond := congrArg Prod.snd hq
  change (k : ZMod m) * q.2 = 1 at hsecond
  calc
    _ = (k : ZMod m) * q.2 := by ring
    _ = 1 := hsecond

/-- THE generic observer gate. No odd-prime-only assumption, no
unproved field/order equivalence, no source-jet substitution. -/
theorem frame_bijective_iff_unit_witness (m k : Nat) :
    Function.Bijective (E28.residueFrame m k) ↔
      ∃ u : ZMod m, u * (k : ZMod m) = 1 := by
  constructor
  · intro hb
    exact unit_witness_of_frame_surjective m k hb.2
  · rintro ⟨u,hu⟩
    exact frame_bijective_of_unit_witness m k u hu

/-- A typed kernel/fiber, not a claim that its cardinality is a
new arithmetic invariant. -/
def lostFiber (m k : Nat) : Set (ZMod m) :=
  {d | (k : ZMod m) * d = 0}

theorem lostFiber_zero (m k : Nat) : (0 : ZMod m) ∈ lostFiber m k := by
  simp [lostFiber]

theorem lostFiber_add (m k : Nat) (x y : ZMod m)
    (hx : x ∈ lostFiber m k)
    (hy : y ∈ lostFiber m k) :
    x + y ∈ lostFiber m k := by
  change (k : ZMod m) * x = 0 at hx
  change (k : ZMod m) * y = 0 at hy
  change (k : ZMod m) * (x+y) = 0
  rw [mul_add, hx, hy, add_zero]

theorem lostFiber_neg (m k : Nat) (x : ZMod m)
    (hx : x ∈ lostFiber m k) :
    -x ∈ lostFiber m k := by
  change (k : ZMod m) * x = 0 at hx
  change (k : ZMod m) * (-x) = 0
  rw [mul_neg, hx, neg_zero]

/-- Two original residue states have the same transported observation
exactly when their real coefficients agree and their imaginary
coefficient difference belongs to this typed kernel. -/
theorem same_observation_iff_fiber (m k : Nat)
    (p q : ZMod m × ZMod m) :
    E28.residueFrame m k p = E28.residueFrame m k q ↔
      p.1 = q.1 ∧ (p.2 - q.2) ∈ lostFiber m k := by
  constructor
  · intro h
    constructor
    · have hp := congrArg Prod.fst h
      exact hp
    · have hp := congrArg Prod.snd h
      change (k : ZMod m) * p.2 = (k : ZMod m) * q.2 at hp
      change (k : ZMod m) * (p.2 - q.2) = 0
      calc
        _ = (k : ZMod m) * p.2 - (k : ZMod m) * q.2 := by ring
        _ = 0 := sub_eq_zero.mpr hp
  · rintro ⟨hre,him⟩
    apply Prod.ext
    · exact hre
    · change (k : ZMod m) * (p.2 - q.2) = 0 at him
      have hp : (k : ZMod m) * p.2 -
          (k : ZMod m) * q.2 = 0 := by
        calc
          _ = (k : ZMod m) * (p.2 - q.2) := by ring
          _ = 0 := him
      change (k : ZMod m) * p.2 = (k : ZMod m) * q.2
      exact sub_eq_zero.mp hp

/-- The generic no-decoder obstruction is relative to a specified
future query; unlike the geometric slogan, its hypothesis is testable. -/
theorem no_future_decoder_of_collision
    {m k : Nat} {β : Type}
    (future : (ZMod m × ZMod m) → β)
    (p q : ZMod m × ZMod m)
    (hobs : E28.residueFrame m k p = E28.residueFrame m k q)
    (hfut : future p ≠ future q) :
    ¬ ∃ decoder : (ZMod m × ZMod m) → β,
      ∀ x, decoder (E28.residueFrame m k x) = future x := by
  rintro ⟨decoder,hdec⟩
  have hp := hdec p
  have hq := hdec q
  apply hfut
  calc
    future p = decoder (E28.residueFrame m k p) := hp.symm
    _ = decoder (E28.residueFrame m k q) :=
      congrArg decoder hobs
    _ = future q := hq

/-- First stage: mod 2 forgets the entire second coefficient. -/
theorem mod2_loses_one : (1 : ZMod 2) ∈ lostFiber 2 2 := by
  change (2 : ZMod 2) * 1 = 0
  decide

/-- At depth two, the coefficient 2 is lost, but 1 survives. -/
theorem mod4_loses_two : (2 : ZMod 4) ∈ lostFiber 4 2 := by
  change (2 : ZMod 4) * 2 = 0
  decide

theorem mod4_preserves_one : (1 : ZMod 4) ∉ lostFiber 4 2 := by
  change (2 : ZMod 4) * 1 ≠ 0
  decide

/-- At depth three, 4 is lost but 2 survives. -/
theorem mod8_loses_four : (4 : ZMod 8) ∈ lostFiber 8 2 := by
  change (2 : ZMod 8) * 4 = 0
  decide

theorem mod8_preserves_two : (2 : ZMod 8) ∉ lostFiber 8 2 := by
  change (2 : ZMod 8) * 2 ≠ 0
  decide

/-- At depth four, 8 is lost but 4 survives. -/
theorem mod16_loses_eight : (8 : ZMod 16) ∈ lostFiber 16 2 := by
  change (2 : ZMod 16) * 8 = 0
  decide

theorem mod16_preserves_four : (4 : ZMod 16) ∉ lostFiber 16 2 := by
  change (2 : ZMod 16) * 4 ≠ 0
  decide

/-- Source-exact bad-prime no-decoder instance. -/
theorem mod2_second_coordinate_nondecode :
    ¬ ∃ decoder : (ZMod 2 × ZMod 2) → ZMod 2,
      ∀ p, decoder (E28.residueFrame 2 2 p) = p.2 := by
  apply no_future_decoder_of_collision
    (fun p : ZMod 2 × ZMod 2 => p.2) (0,0) (0,1)
  · exact E28.mod2_collision.1
  · decide

/-- The index-two frame is locally invertible at 5 and has an
explicit inverse witness 3 mod 5. -/
theorem mod5_unit_witness :
    ∃ u : ZMod 5, u * (2 : ZMod 5) = 1 :=
  ⟨3, by decide⟩

theorem mod5_bijective_via_general_gate :
    Function.Bijective (E28.residueFrame 5 2) :=
  (frame_bijective_iff_unit_witness 5 2).2 mod5_unit_witness

/-- At the conductor prime 2 there is no local inverse witness. -/
theorem mod2_no_unit_witness :
    ¬ ∃ u : ZMod 2, u * (2 : ZMod 2) = 1 := by
  decide

theorem mod2_not_bijective_via_general_gate :
    ¬ Function.Bijective (E28.residueFrame 2 2) := by
  intro hb
  exact mod2_no_unit_witness
    ((frame_bijective_iff_unit_witness 2 2).1 hb)

end TenthDiscriminant.E29

#print axioms TenthDiscriminant.E29.frame_bijective_iff_unit_witness
#print axioms TenthDiscriminant.E29.same_observation_iff_fiber
#print axioms TenthDiscriminant.E29.no_future_decoder_of_collision
#print axioms TenthDiscriminant.E29.mod2_second_coordinate_nondecode
#print axioms TenthDiscriminant.E29.mod5_bijective_via_general_gate
#print axioms TenthDiscriminant.E29.mod2_not_bijective_via_general_gate
