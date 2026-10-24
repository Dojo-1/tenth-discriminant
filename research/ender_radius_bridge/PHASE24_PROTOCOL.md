# Phase 24 preregistration: discharge the reciprocal-prime tail

Date: 2026-10-24. Base `035454e`, pinned CI `40098513168` and CodeQL
`40098510944` passed. Register before new proof edits.

## Target

Prove, for natural `P≥2` and every natural `R`,

`largeReciprocalTail R P ≤ enderTailIntegral P`,

with the exact finite prime sum and unchanged production expression
`I(P)=log(P+1)/P+log(1+1/P)`. The intended argument compares each integer
summand `log(m)/(m(m−1))`, `m≥2`, with the drop of the positive potential
`K(x)=log(x+1)/x+log(x+1)−log(x)`. Its derivative is
`−log(x+1)/x²`. A finite telescoping sum and positivity of the discarded
endpoint should suffice. An integral comparison is an acceptable alternate
route. Do not import any prime-distribution estimate or assume the tail.

Compose with Phase 23 to remove the final analytic hypothesis from the
mathematical lower/upper comparison on the actual chosen-radius Gram.
Retain all squarefree, class-number, strict prime-range, radius and floor
padding guards. The final theorem must use the unchanged mathematical
production lower/upper expressions, not a replacement bound.

## Controls and scope

Check the integer step at `m=2`, `R≤P` (empty prime tail), `P=2`, the
prime exactly at `P` remaining excluded, a nonempty tail and nonnegativity
of `I(P)`. Reject lowering the bound to zero for a nonempty tail and
reject extending the positive-potential assertion to `x=0` (Lean's total
logarithm makes the displayed extension unsuitable). Preserve failures.

No `sorry`, new axiom, changed production tool, radius, cutoff or saved
certificate. Update current README/STATUS/FORMALIZATION and the short
staircase guide. Verify the exact published head with pinned full build,
dependency audit and inherited negative controls. Keep PR #28 draft and
unmerged. Arb enclosure interpretation, numerical contradictions, universal
closure, even cases and full classification remain open; no novelty claim.

## Execution record

Protocol-only `e1fa9be822e91f3210bd9161f6fd8e05498ad7cc` preceded proof
edits. `PrimeTail.lean` proves the positive potential, its derivative,
unit-step comparison, finite telescoping, integer-subset domination and
equality with production `I(P)`. It composes Phase 23 without a remaining
analytic tail premise and exposes the strict real inequality needed for
class-number exclusion. That inequality and the numerical radius/count
guards have not been certified by the saved Arb output in Lean.

Eight controls compile, including the positive `m=2` endpoint, empty and
nonempty prime tails, the prime-split boundary, positive production constant,
and false zero-tail/zero-input strengthenings. Development repairs removed
redundant function-equality goals from derivative conversion and normalized
the real numeral `2−1` in the endpoint control. No mathematical guard was
weakened or new numerical premise assumed. Automatic implicit variables
are disabled; no new axiom or proof escape is introduced.

From `lean/`, targeted `lake env lean TenthDiscriminant/PrimeTail.lean`
and full `lake build` pass (6714 steps). Pinned published-head CI must
also run `python verify_sources.py`, `python audit.py` and
`python negative_controls.py`. Endpoint correspondence is not an Arb
inequality verifier. The generated untracked manifest is excluded.
No production tool, formula, cutoff, saved certificate or frozen objective
audit changed. Numerical interpretation, universal closure, even cases and
classification remain open. This is classical mathematics, not a novelty claim.
Local `python verify_sources.py`, root `git diff --check`,
`python -m json.tool .agent/state.json` and local Markdown file-link checks pass.
