# Phase 2 preregistration: the universal one-factor jet

Date: 2026-10-23. Base: merged PR #21, `origin/main` at `08c7260`.
This protocol is written before Phase 2 proof edits. Preserve the
Phase 1 paper proof, controls and negative record unchanged.

## Exact bounded target

For arbitrary `D : Nat`, `p : Nat`, a selected integer pair `a`, and
`j : Nat`, define the jet difference between the *existing*
`integerDerivativeRow D p 0 j a` (`Z^p`) and
`integerDerivativeRow D 0 1 j a` (`W`). Under the explicit pairwise
premise that both coordinates of `pairPow D a p - pairConj a` are
divisible by `p`, prove that both coordinates of this jet difference
are divisible by `p` for **every** ordinary derivative order `j`.

This is the local product-rule input for the uniform valuation proof,
not a claim that all primes satisfy the premise. It is stronger in `j`
than finite checking and should specialize to the fixed `D=19,p=3`
pilot without changing its theorem. Do not infer irreducibility or
inertness from this conditional result. The next phase would prove
the Frobenius premise and the rectangular `H^k` basis transform.

## Falsifiers and stop conditions

- Check `j=0`, `1<=j<=p`, and `j>p` separately; ordinary derivatives
  must retain a factor `p` in both integer coordinates.
- The noninert `D=2,p=3,a=(0,1)` does **not** meet the premise; do not
  accidentally make an unconditional theorem.
- Avoid a theorem about a replacement matrix or reduction of a set
  that drops colliding samples.
- If Lean only proves a coefficient lemma or a weaker conditional
  version, record it as partial, keep the failed target, and do not
  promote the paper valuation to a checked theorem.

Verification: targeted `lake env lean`, `python verify_sources.py`,
full `lake build`, the compiled axiom audit and negative controls in
pinned Linux CI. Update reader documentation only to the exact extent
of the checked declaration. No cutoff, class-number or merge claim.
