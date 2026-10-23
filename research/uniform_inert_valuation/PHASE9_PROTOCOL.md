# Phase 9 preregistration: residue-fiber transport and index-2 norm bridge

Date: 2026-10-23. Base: merged PR #27, `2c9f05b`. This protocol is
committed before any new Lean proof edits.

## Exact target

This phase closes two complementary local-to-arithmetic obligations left
explicitly open across Phase 6 (`research/uniform_inert_valuation/PHASE6_PROTOCOL.md`,
`lean/HUMAN_GUIDE.md` §12) and Phase 8 (`research/uniform_inert_valuation/PHASE8_PROTOCOL.md`,
`lean/TenthDiscriminant/Arithmetic.lean`):

1. **Residue-fiber transport operator `T` (`LocalOperators.lean`):**
   Phase 6 listed `T`—replacing `D` and/or `a` by congruent integer
   representatives modulo `p`—as *"a paper deduction to test later, not
   a Lean claim in this phase"*, and `lean/HUMAN_GUIDE.md` §12 notes
   that changing `D` or `a` within their residues modulo `p` is *"only a
   proposed next lemma, not a checked result here."*
   Prove in `lean/TenthDiscriminant/LocalOperators.lean`:
   - `pairMul_congruence` and `pairPow_congruence`: coordinatewise and
     discriminant congruences modulo `p` (`(p : Int) ∣ (D₁ : Int) - (D₂ : Int)`,
     `(p : Int) ∣ a.1 - b.1`, `(p : Int) ∣ a.2 - b.2`) are preserved by
     `pairMul` and all natural powers `pairPow`.
   - `frobenius_congruence_of_mod_eq`: the order-zero Frobenius premise
     `F(D,p,a)` is invariant under `T`.
   - `frobeniusJet_of_mod_eq_dvd` and
     `rectangular_frobenius_row_jet_of_mod_eq`: composition of `T` with
     both the all-orders one-factor jet theorem and the `H^k` power-jet
     theorem in `Zsqrtd`.
   - `frobenius_congruence_residue_transport_pilot`: non-real pilot
     transporting `(D₁=1, a=(0,1))` to `(D₂=19, b=(3,-2))` modulo `p=3`.

2. **Index-2 order norm identity and nonsquareness transfer (`InertFrobenius.lean`):**
   Phase 8 proved `rectangularTraceGram_valuation_of_nonsquare` under the
   selected-order hypothesis `¬ IsSquare (-(D : ZMod p))`. Meanwhile,
   `Arithmetic.lean` works with the maximal-order principal norm
   `principalNorm D x y = x² + x y + ((D+1)/4) y²` for `D ≡ 3 (mod 4)`.
   To connect the selected order `ℤ[√(-D)]` (index 2 in the maximal order)
   to `principalNorm` without claiming unproved class-group theorems:
   - Prove that for `D₁ ≡ D₂ (mod p)`, `IsSquare (-(D₁ : ZMod p)) ↔ IsSquare (-(D₂ : ZMod p))`,
     so `rectangularTraceGram_valuation_of_nonsquare` is invariant across
     the discriminant residue fiber `D₁ ≡ D₂ (mod p)`.
   - Prove the exact index-2 norm identity linking `pairMul D a (pairConj a)`
     to `principalNorm`: for `D % 4 = 3`,
     `principalNorm D (x - y) (2 * y) = x^2 + D * y^2 = (pairMul D (x, y) (pairConj (x, y))).1`,
     and at the modulo-`p` level, if `(2 * x + y)^2 + D * y^2 ≡ 0 (mod p)`
     with `p ∤ y`, then `-(D : ZMod p)` is a square in `ZMod p` (contrapositively,
     if `¬ IsSquare (-(D : ZMod p))`, then `p` cannot divide `4 * principalNorm D x y`
     unless `p ∣ y` and `p ∣ 2 * x + y`, and for odd prime `p < (D + 1) / 4`
     no integer pair `(x, y)` has `principalNorm D x y = p`).

## Falsifiers and scope boundary

- Retain the `D=19, p=3` inert pilot and `D=2, p=3` split counterexample.
- Keep the boundary explicit: proving residue-fiber transport `T` and the
  norm/nonsquareness bridge between `principalNorm` and `IsSquare (-(D : ZMod p))`
  does **not** formalize Dedekind domains, ideal class groups, genus theory,
  or the global implication `h(-D) = 1 ⇒ ¬ IsSquare (-(D : ZMod p))`
  (which requires unique factorization of principal ideals in the maximal
  order), nor does it formalize the geometric cell-area lower bound or
  analytic cutoff.
- Run source correspondence, full pinned `lake build`, compiled axiom audit,
  and all inherited negative controls on pinned Linux CI. Keep the PR draft.

## Execution record

Protocol-only commit `2989c26` preceded the Lean proof edits.

1. `lean/TenthDiscriminant/LocalOperators.lean`:
   - `pairMul_congruence` and `pairPow_congruence` prove by induction that
     coordinatewise and discriminant congruences modulo `p` are preserved
     by `pairMul` and `pairPow`.
   - `frobenius_congruence_of_mod_eq` proves that the residue-fiber
     transport operator `T` preserves the explicit order-zero Frobenius
     congruence across congruent `(D, a)` pairs modulo `p`.
   - `frobeniusJet_of_mod_eq_dvd` and
     `rectangular_frobenius_row_jet_of_mod_eq` compose `T` with both the
     all-order single-factor jet theorem and the `H^k` power-jet theorem
     in `Zsqrtd`.
   - `frobenius_congruence_residue_transport_pilot` checks the non-real
     pilot transporting `(D₁=1, a=(0,1))` to `(D₂=19, b=(3,-2))` modulo `3`.
2. `lean/TenthDiscriminant/InertFrobenius.lean`:
   - `nonsquare_of_mod_eq` and `rectangularTraceGram_valuation_of_mod_eq_nonsquare`
     prove that the Phase 8 nonsquareness guard and exact `p^(2F(p))`
     Gram determinant valuation transfer across any `D₁ ≡ D₂ (mod p)`.
   - `selectedOrderNorm_eq_principalNorm` proves the exact index-2 norm
     identity `(pairMul D (x, y) (pairConj (x, y))).1 = principalNorm D (x - y) (2 * y)`
     for `D ≡ 3 (mod 4)`.
   - `norm_eq_zero_iff_of_nonsquare` and
     `dvd_four_mul_principalNorm_of_nonsquare` prove that when `-D` is
     nonsquare in `ZMod p`, `u^2 + D * v^2 = 0` in `ZMod p` forces
     `u = 0 ∧ v = 0`, so `p ∣ 4 * principalNorm D x y` forces
     `p ∣ 2 * x + y` and `p ∣ y`.

First CI build (`40026960495`) caught two proof-script issues: `omega`
treating `(p : Int) * k` as nonlinear in `frobenius_congruence_of_mod_eq`
(repaired via explicit `rw` + `ring`) and `push_cast` expanding
`((2 * x + y : Int) : ZMod p)` in `dvd_four_mul_principalNorm_of_nonsquare`
(repaired via `simpa only [Int.cast_add, Int.cast_mul, Int.cast_pow, Int.cast_natCast]`).
