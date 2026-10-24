# Phase 17 preregistration: isolate the area-to-radius bridge

Date: 2026-10-24. Base: draft PR #28 head `bdbfef7`; pinned CI
`40045869458` and CodeQL passed. This protocol precedes proof edits.

## Exact bounded target

For `D > 0`, positive `q = 3R+S`, and Ender's unchanged radius
`rho >= 1.001 sqrt(q sqrt(D)/pi) + 10 sqrt(D)`, prove in Lean that
the *explicit* cell-area estimate

`pi (rho - (1+sqrt(D))/2)^2 <= |ellipsePairs D rho| sqrt(D)`

implies `3R+S < |ellipsePairs D rho|`. Compose with the existing
upper-endpoint transport to the actual trace-Gram determinant. Do not
assume the desired cardinality or alter the radius/certificate.

The cell-covering area estimate itself is the next separate theorem;
this bounded phase must not label it Lean-checked. If the algebraic
bridge fails, preserve the failure and report the exact obstruction.

## Controls and validation

Retain `D=1,rho=1` and `D=19,rho=5` exact count controls. Keep the
strict `>` conclusion (not `>=`) and require `D>0`, `q>0`, and the
radius guard. Run targeted Lean, full pinned build, source
correspondence, compiled dependency audit and inherited controls via
pinned CI. Update human-facing status and preserve draft/unmerged PR.

## Execution (2026-10-24)

`LatticeEllipse.lean` now checks the exact real radius algebra with a
strict count conclusion and composes it with upper-endpoint monotonicity
and the original trace-Gram determinant theorem. The area inequality
remains a named premise. Targeted Lean passed; inherited exact-count
controls remained in the compiled module. The disk-cell coverage proof,
analytic determinant comparison, and classification remain open.
Local `lake build` completed all 6707 steps; `python verify_sources.py`
passed its endpoint-only check. Whitespace and task-state JSON checks
passed. The compiled dependency audit and negative controls await pinned CI.
