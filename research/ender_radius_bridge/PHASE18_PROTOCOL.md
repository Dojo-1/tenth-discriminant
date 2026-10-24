# Phase 18 preregistration: check the lattice-cell area inequality

Date: 2026-10-24. Base: draft PR #28 head `be426b0`, pinned Lean CI
`40047725905` and CodeQL passed. This protocol precedes proof edits.

## Exact target

For every natural `D>0` and integer radius `rho` with
`(1+sqrt D)/2 <= rho`, prove in Lean for the existing `ellipsePairs`:

`pi * (rho - (1+sqrt D)/2)^2 <= card(ellipsePairs D rho) * sqrt D`.

Use the actual Euclidean disk volume and the width-one, height-`sqrt D`
lattice cells. The intended proof picks a cell center by integer floors,
shows each point of the smaller disk belongs to a cell whose center is
in `ellipsePairs`, then bounds disk volume by the sum of the cell areas.
Finite-union subadditivity suffices; disjointness of boundaries is not
needed. Compose the result with Phase 17 to remove its area premise.

This target does not include Ender's analytic determinant comparison,
Arb certificate interpretation, or final class-number classification.
Do not substitute a different lattice, radius, matrix, or numerical
experiment for the theorem.

## Adversarial controls and stop rule

Retain exact `D=1,rho=1` and `D=19,rho=5` counts. Check origin and
boundary-center inclusion, negative coordinates, and `rho=delta` equality.
Use no `sorry`/new axioms. If full formalization does not close, retain
only genuinely checked helper lemmas and record the precise remaining
measure/covering obligations. Update the claim map honestly; run targeted
Lean and the complete pinned checks on any proof head. Keep PR draft and
unmerged.

## Execution (2026-10-24)

`EllipseCellArea.lean` compiles the full target. It measures each closed
cell exactly, constructs a containing cell for every complex point with
integer floors, bounds the distance to its lattice center, proves the
smaller disk is covered by cells from the *actual* `ellipsePairs`, and
applies finite-union subadditivity plus Mathlib's exact complex disk
volume. The resulting `ellipsePairs_cell_area_bound` has no area or
point-count premise. `ellipsePairs_card_gt_of_ender_radius` composes it
with Phase 17; `ellipseTraceGram_det_bounds_of_ender_radius` transports
the strict count to the original Gram at an interval upper endpoint.

The registered `D=rho=1` endpoint and negative-boundary controls compile.
At `D=1,rho=0`, the unchecked strengthening without `rho>=delta` is
formally refuted (`pi>1` versus the one-point ellipse). Initial proof
errors were tactic/coercion issues: nesting the second floor case,
selecting the ENNReal top/coercion lemmas, and making square-root
nonnegativity explicit. They were repaired; no mathematical guard was
removed. Full build and pinned CI status are recorded separately.
Local targeted Lean and the complete 6708-step `lake build` pass.
`python verify_sources.py` passes its endpoint-only correspondence check;
task-state JSON and whitespace checks pass. No proof placeholders occur
in the new module. Pinned dependency audit and negative controls await CI.
