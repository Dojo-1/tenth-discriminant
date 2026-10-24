# Phase 21 preregistration: the upper ellipse count

Date: 2026-10-24. Base: draft PR #28 head `5f5614c`, pinned Lean CI
`40091741093` and CodeQL passed. This protocol precedes proof edits.

## Exact target

For every natural `D>0` and integer radius `rho>=0`, let
`Y=floor(rho/sqrt(D))` (natural floor). Prove for the existing full
`ellipsePairs`:

`card(ellipsePairs D rho) <= pi*rho^2/sqrt(D) + 2rho + (2Y+1)`.

Use the original lattice and radius. For each point with both coordinates
nonzero, attach the open unit cell lying inward toward the two axes. These
cells have physical area `sqrt(D)`, are pairwise disjoint, and lie in the
closed disk of radius `rho`. Thus disk area bounds the nonaxis count.
The nonzero horizontal axis contributes exactly `2rho` possible points;
the vertical axis contributes at most `2Y+1`. No square-root slice integral
or altered numerical bound is needed.

Transport this count from a lower discriminant endpoint `D1` to all
`D>=D1` using existing ellipse-set antitonicity. Compose it with Phase 20
to remove the abstract upper-count premise from the actual-Gram/`upper_B`
comparison. Expose any line-count padding as an explicit `floor<=Y` guard:
production floors an Arb **upper endpoint**, which is not automatically
equal to the exact real floor. Do not claim an Arb interpretation theorem.

## Controls and stop rule

Check `rho=0` (one point, equality), `D=rho=1`, and the existing
`D=19,rho=5` count. Retain the origin and both signs. Reject assigning
positive-area inward cells to axis points: that would overcount disk area
already at `D=rho=1`. Check adjacent cells are disjoint even on integer
boundaries, and include a negative-coordinate cell. The open boundaries
are harmless because only cell volumes, containment and disjointness are
needed, not a covering theorem.

No `sorry`, new axioms, new cutoff, changed production formula or numerical
campaign. If full formalization fails, retain only checked subclaims and
name the remaining counting/measure obligation. Run targeted Lean, full
build, endpoint-only source correspondence, compiled dependency audit and
inherited negative controls on the published proof head. Keep PR draft and
unmerged; factorial, certificate, universal-envelope and classification
links remain separate obligations.

## Execution (2026-10-24)

Protocol-only commit `157ba64` preceded proof edits. `EllipseUpperCount.lean`
checks the open inward intervals, unique coordinate assignment, exact cell
volume, containment in the original disk, pairwise disjointness, and finite
union area bound. It then proves the exact vertical-floor bound, removes
the origin from the horizontal axis box, and counts the two axis boxes.
The resulting `ellipsePairs_card_le_upper_count` is the unchanged target.

`ellipsePairs_card_le_padded_upper_count` transports the lower-endpoint
upper count throughout an interval, with any upward line-count padding
explicit. `ellipseVerticalBound_le_of_ratio_lt` supplies that padding from
the strict real bound `rho/sqrt(D)<Y+1`. The public composition
`ellipse_primeMass_log_le_counted_upperB` removes Phase 20's abstract upper
sample-count premise while retaining the exact radius, strict prime cutoff,
class-number and floor-padding guards. No equality between an Arb endpoint
floor and the exact floor is assumed.

Eight controls compile: zero-radius equality, the unit ellipse, the
`D=19,rho=5` count, adjacent disjoint cells, a negative cell, an excluded
integer boundary, the false all-points-as-cells area claim, and the false
upper count at `D=0`. Development failures concerned the explicit volume
measure, multiplication order, integer absolute-value casts, finset product
cardinality notation and the zero-radius singleton filter. All were repaired
without changing the mathematical statement or removing a guard.

Targeted Lean and the complete 6711-step local `lake build` pass. The
endpoint-only source correspondence, task JSON, whitespace and local
documentation-link checks also pass. The
factorial lower estimate, exact numerical interpretation, universal closure
and classification remain open. Final published-head CI is recorded
separately.
