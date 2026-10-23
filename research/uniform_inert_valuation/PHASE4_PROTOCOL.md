# Phase 4 preregistration: ordinary-jet powers

Date: 2026-10-23. Base: draft PR #23 at `059741a` (unmerged).
This protocol is recorded before Phase 4 Lean proof edits. It does not
change the recorded candidate cutoff or the classification status.

## Exact bounded target

For a commutative ring `A`, a polynomial `H : A[X]`, evaluation point
`z : A`, and `q : A`, assume every **ordinary iterated derivative** of
`H` evaluates to a multiple of `q`. Prove in Lean that for every
`k,j : Nat` and every polynomial prefactor `B`, the `j`-th ordinary
derivative of `B*H^k` at `z` is a multiple of `q^k`.

Use Mathlib's iterated polynomial product rule, which includes the
integer binomial coefficient. Do not replace ordinary derivatives by
Hasse/divided derivatives. No primality or quadratic-order hypothesis
belongs in this universal algebra lemma. The theorem is a necessary
piece of the proposed rectangular basis proof, but is not itself an
identification with `integerDerivativeRow` or an integral matrix
factorization.

## Falsifiers and stop conditions

- Test `k=0` and derivative order greater than the degree.
- Avoid the false divided-derivative analogue: for `H=X^p` at zero,
  the `p`-th Hasse derivative is `1`, while the ordinary derivative is
  `p!`. This is why the derivative convention is essential.
- Keep the noninert `D=2,p=3` order-zero counterexample: the algebra
  lemma must not be advertised as making its premise true.
- If the product rule cannot be connected to the quadratic-order
  polynomial encoding this cycle, report that interface as open.

Verify targeted Lean, source correspondence, full `lake build`, pinned
dependency audit and inherited negative controls. Update reader text
only to the exact checked declaration. No automatic merge or Tao post.

## Execution record

The protocol-only commit `86f40e7` preceded all new Lean edits. The
first targeted proof attempt exposed a missing evaluation-scalar lemma
and an induction hypothesis fixed at one derivative order. Two later
attempts exposed a power-associativity normalization and a mistaken
`eval_zero` lemma name. These were proof-script failures, not negative
mathematical results; each was repaired before the passing check.

`JetPower.lean` proves the universal ordinary-jet product-power theorem,
specializes it to `Z^p-W` and the selected quadratic order, and derives
`p^k` divisibility in **both** integer coordinates of every proposed
transformed-row jet under the explicit order-zero congruence. A Lean
control confirms the analogous Hasse-derivative claim fails for
`X³`, order three, modulo three. Targeted Lean, source correspondence
and full 6693-step `lake build` passed. The unitriangular matrix-row
identification, derivation of the Frobenius premise from inertness,
and cutoff/classification remain open. Final-head pinned CI remains
to be recorded.
