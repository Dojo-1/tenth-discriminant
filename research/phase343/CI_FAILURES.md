# Phase343 — exact-head Lean failure ledger

## 17 November 2026 — first 307 logarithm/scalar run

[Run 44043652544](https://github.com/Dojo-1/tenth-discriminant/actions/runs/44043652544), source head `c3be72844f984f082f19ab755843ee17da0eab79`:

- Exact Phase341 endpoint and negative-control tests: **PASS**.
- Lean logarithm module: **FAIL** at `Phase343Log307.lean:30`.
- The rational predicate `checkPositiveLogBounds 5 307 8 (5726/1000) (5728/1000) = true` was proved by `norm_num`. However `norm_num at h` reduced the upper bound `5728/1000` to the equivalent fraction `716/125`; `exact hhi` could not close the syntactically different but mathematically identical target.
- The dependent `log_floor_from_307_fourth_power` temporarily printed `sorryAx`. The 307 log floor and scalar theorem are **not verified** at that head. The field theorem at 307 has not been attempted.

**Controlled correction:** change only the upper enclosure proof's final `exact hhi` into `linarith`. Keep both rational endpoints, the sound finite-series checker, the 307-domain hypothesis, scalar constants and all original-source objects unchanged. Rebuild and recheck exact theorem types and axioms before promoting either statement.

Record this failure even if the corrected run passes.
