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
