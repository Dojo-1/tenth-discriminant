# Phase105: both translations, explicit invariants

Preregistered at `45b7e70dbe0bbc40097a566d74ef3d3d6f8f82b0`, against
`be1c0e36b9eea47a846277383253318063e717e0`. Full standalone target passed.
[Human guide](COORDINATE_TRANSLATION_GUIDE.md) · [Protocol](PHASE105_PROTOCOL.md).

| Attempt | Exit | Seconds | Result |
| --- | --- | --- | --- |
| 1 | 1 | 32.3643311 | Injection rewrite, binder order and control simplifications failed |
| 2 | 1 | 34.5409098 | Main bridge checked; one finite-cardinality control simplification remained |
| 3 | 0 | 40.3833118 | Entire target and all controls passed |

Total recorded decimal time: 107.2885527 seconds. Each run stayed within
600 seconds and 8192 MB; cumulative cap 1200 seconds. No resource stop.
All three slots are consumed: do not replay this registered target.

All 29 complete public mathematical statements, including let-bound
control data and expected determinants 24/60, are identical across runs.
All five complete definitions are byte-identical. The two permitted
proof-only repairs fix lambda reduction and argument order, unfold the
finite matrix controls, split the zero-discriminant control, and supply
one decidable cardinality fact. Control proof scripts changed; their
statements and expectations did not. No weakened target was substituted.

Namespace audit: 43 logical declarations, 38 theorems, 11 runtime-only
auxiliaries excluded. Only propext, Classical.choice and Quot.sound.
Fresh dependency closures: bridge 37,660; odd-order norm 17,619;
counterexample 12,095. All exclude the registered 68 forbidden roots,
including the cutoff and later counting/budget results.

The [saved manifest](PHASE105_RESULTS.json) and [archive](PHASE105_RAW.zip)
preserve all 12 source/stdout/stderr/result artifacts, including failures.
`python research/ender_radius_bridge/verify_phase105_results.py` checks
hashes, full statements/definitions, exact proof repairs, exclusions,
axioms, budgets and frozen prior evidence without running Lean.
Actual proof command (from lean):
`lake env lean -j 1 ../research/ender_radius_bridge/Phase105CoordinateTranslation.lean`.
It has already been executed three times; this is an execution receipt,
not an invitation to consume extra attempts.

The production root, tools, pins, CI and historical evidence are unchanged.
Standalone status: no Phase105 library integration, full-library audit or
external CI is claimed. [PR36's own successful merge](PR36_MERGE_RECEIPT.md)
covers its earlier head only. No cutoff reduction, full classification or
independent human semantic review is claimed.
