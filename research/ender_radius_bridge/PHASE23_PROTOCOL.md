# Phase 23 preregistration: factorial weights to the determinant's prime mass

Date: 2026-10-24. Base `c8a42a5`, pinned CI `40096404959` and CodeQL
`40096403109` passed. Register before new proof edits.

## Target

Use the unchanged `floorSum`, `valuationWeight`, factorial identity and
scalar lower bound. Split primes at a natural `P≥2`. For the large primes
`p>P`, require `R≤P*S`, as in production. Prove the exact identity

`F(p)=(S-1/2) A(p) - (1/2) sum_{r<R} floor(r/p)^2`.

Define the finite small-prime factorial contribution, exact small odd-prime
determinant contribution, remaining higher-power contribution and quadratic
floor loss. Prove their exact decomposition and that the production-shaped
clipped lower expression lies below the determinant's exact odd-prime mass
whenever the explicit finite higher-power and quadratic losses have the two
stated tail bounds. Compose that theorem with the already checked counted
`upper_B` comparison on the actual Gram, if the interface permits a small diff.

The two tail bounds must remain explicit hypotheses unless independently
proved: higher-power loss ≤ `V*I`, quadratic floor loss ≤ `W*I`, where
`V=R(R-1)/2`, `W=R(R-1)(2R-1)/6`, and production
`I=log(P+1)/P+log(1+1/P)`. Try the elementary floor bounds needed for these
estimates. Do not describe a conditional interface as a verified computable
cutoff. The analytic tail domination and Arb interpretation are separate.

## Controls and scope

Check a concrete large-prime weight identity with nonzero quadratic loss,
the equality endpoint `R=P*S`, primes on the split boundary, empty large
prime sets, and both branches of clipping. Reject dropping the quadratic
loss and reject the quotient guard: a quotient larger than `S` invalidates
the polynomial identity. Preserve failures/repairs, no new axiom or `sorry`.

Keep production code, formulas, radii, cutoff, certificates and frozen audit
unchanged. Update the short human guide, README/STATUS/FORMALIZATION and
living objective ledger. Run pinned full build, dependency audit and
negative controls on the exact published head; keep PR #28 draft/unmerged.
Even cases, numerical certificates, universal closure and classification
remain open. No novelty claim or automatic public comment.

## Execution record

Protocol-only `e4736fdf6b947968c17df5a69683d498da83381e` preceded proof
edits. `PrimeMassLower.lean` proves the finite conversion, exact split,
production integer coefficients, zero-weight padded enumeration and clipping.
Both requested finite losses are independently bounded using natural-floor
comparison, polynomial row sums and a finite geometric series. They share
one reciprocal-prime sum, so the public actual-Gram composition exposes
only its upper bound `J≤I`. Production's `I(P)` is defined but its analytic
domination theorem remains open. No numerical/cutoff conclusion is inferred.

Eight controls compile. The omitted-quadratic and missing-quotient-guard
claims are proved false, not discarded. Development repairs normalized
sum association/distribution, an unsimplified `True` in the prime partition,
cast rewriting order, and explicit positive denominator guards. No domain
guard was weakened. All proof code has automatic implicit variables disabled.

From `lean/`, `lake env lean TenthDiscriminant/PrimeMassLower.lean` and
the full `lake build` pass locally (6713 steps). The final published head
must also pass `python verify_sources.py`, `python audit.py` and
`python negative_controls.py` in pinned Linux CI. The correspondence check
only matches interval endpoints; it does not certify Arb inequalities.
The generated untracked manifest is excluded. No production code, formula,
cutoff, certificate or frozen objective audit was changed.
Local `python verify_sources.py`, root `git diff --check`,
`python -m json.tool .agent/state.json` and Markdown file-link checks pass.
