# Phase337 verification ledger

## Initial 313-domain analytic upper attempt — 17 November 2026

At [run 44031218936](https://github.com/Dojo-1/tenth-discriminant/actions/runs/44031218936), `Phase337Dimensions313` compiled, but `Phase337UpperScalars313` failed before the original-Gram upper could be certified.

The errors were narrowly identified at the exact head:

- Line 248: `log_floor_from_313_fourth_power` was referenced unqualified. The proven floor lives in `TenthDiscriminant.Phase332`; source file must use the explicit namespace.
- Line 286: a literal `(315 : Real)^3` remained after changing the theorem hypothesis to `D >= 313^4`, preventing the proof of `thin_radius_guards_313`. It must be replaced by `(313 : Real)^3`.
- The dependent `normalized_upper_313` and `thin_radius_guards_313` temporarily printed `sorryAx` because their proofs failed. Neither counts as established at that head.

**Repair scope:** update only the two source references. The radius, point-count criterion, arithmetic mass, normalized constants, and original Qthin Gram must not change. Re-run exact-head Lean build, source test, and allowed-axiom inspection. This failure remains recorded regardless of subsequent success.

## Second attempt — original-Gram upper signature mismatch

[CI run 44032183393](https://github.com/Dojo-1/tenth-discriminant/actions/runs/44032183393) confirmed that the corrected `Phase337UpperScalars313` compiled successfully. The final `Phase337ThinUpper313` declaration still carried the **old assumption** `hD : 315^4 ≤ D`, while all its supporting lemmas now require `313^4 ≤ D`. Lean rejected seven calls with `315^4 ≤ D` supplied where `313^4 ≤ D` was expected. The failed declaration temporarily reported `sorryAx` and is **not verified** at that source head.

**Controlled repair:** change the *single* hypothesis in `thin_production_normalized_upper_stronger_313` from `315^4 ≤ D` to `313^4 ≤ D`, without touching its conclusion, determinant, source Q, radii, constants, row structure or bounding lemmas. This is the intended theorem-strengthening obligation, so the CI rerun must verify it rather than accepting the old domain.
