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
