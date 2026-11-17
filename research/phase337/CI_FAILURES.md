# Phase337 verification ledger

## Initial 313-domain analytic upper attempt — 17 November 2026

At [run 44031218936](https://github.com/Dojo-1/tenth-discriminant/actions/runs/44031218936), `Phase337Dimensions313` compiled, but `Phase337UpperScalars313` failed before the original-Gram upper could be certified.

The errors were narrowly identified at the exact head:

- Line 248: `log_floor_from_313_fourth_power` was referenced unqualified. The proven floor lives in `TenthDiscriminant.Phase332`; source file must use the explicit namespace.
- Line 286: a literal `(315 : Real)^3` remained after changing the theorem hypothesis to `D >= 313^4`, preventing the proof of `thin_radius_guards_313`. It must be replaced by `(313 : Real)^3`.
- The dependent `normalized_upper_313` and `thin_radius_guards_313` temporarily printed `sorryAx` because their proofs failed. Neither counts as established at that head.

**Repair scope:** update only the two source references. The radius, point-count criterion, arithmetic mass, normalized constants, and original Qthin Gram must not change. Re-run exact-head Lean build, source test, and allowed-axiom inspection. This failure remains recorded regardless of subsequent success.
