# Registered proof check: Ender's chosen ellipse radius

Registered on 23 October 2026 before changing the proof guide or Lean source.
Base: draft PR #18, head `2b69c2a`. This is a continuation of the frozen
`flow/PREREG_ENDER.txt`, not a change to its numerical parameters or outcomes.

## Claim to test

For integer `D >= 1`, natural `R,S` with `q = 3R+S > 0`, and natural radius
`rho` satisfying

    rho >= 1.001 * sqrt(q*sqrt(D)/pi) + 10*sqrt(D),

prove that the full integer ellipse `x²+D*y² <= rho²` has more than `q`
points. Apply this at Ender's finite-interval upper endpoint `D2`, then use
exact set inclusion for every `D <= D2`; apply it directly to the universal
ceiling radius. Independently verify the inherited lower count
`n >= pi*rho²/sqrt(D) - 2*rho/sqrt(D) - 6*rho` for all integer radii,
including zero and axis endpoints.

Permitted proof tools: elementary lattice-cell geometry or the already
recorded horizontal-slice comparison in `review/PHASE2_GPT-6.1-Sol.md`.
Falsifiers: a missing origin/boundary point, a cell whose center is outside
the ellipse despite intersecting the inner disk, an unjustified area
comparison, or a hidden assumption that `rho` is real rather than the
integer returned by Ender's code.

## Stop and reporting rule

Try to mechanize a small exact-set monotonicity lemma in Lean, but do not
claim the area estimate is kernel-checked unless it actually compiles.
Run the pinned Lean build/audit/negative controls for any source change and
one bounded exact finite falsification check. Preserve failed checks and
any discrepancy with the original Ender protocol. Do not modify Ender's
certificates or claim arithmetic divisibility or classification from this
count alone.

## Result recorded on 23 October 2026

`PROOF.md` gives a complete elementary cell-area proof of the all-radius
lower estimate and the stronger direct chosen-radius guard. Its area theorem
is **not** kernel-checked. Lean 4.19.0 accepted the new endpoint-inclusion,
cardinality and conditional determinant lemmas, as well as the exact
`D=19,rho=5` 21-point control. `lake build` and `python verify_sources.py`
passed locally; the latter checks source identity, not Arb inequalities.
Pinned CI on the continuation commit is still required. No historical
interval certificate or cutoff was changed.

After this protocol was registered, PR #18 merged externally at `6431e78`.
The proof continuation was moved unchanged onto `codex/ender-radius-count`
based on that merge; the registration target and test rules above were not
rewritten.
