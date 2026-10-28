# Phase76: least actual norm and primitivity in every basis

Registration `82ff23d` precedes source/execution on `5614e71`. The new
Nat.find/ambient-norm construction is separate from stopped75. That
failed source/protocol/runner/raw remain byte-identical; no repair/rerun.

`LeastNorm.bounded_class_least_primitive` assumes squarefree D=3mod4
and actual classNumber of the constructed quadratic field<=2. For each
actual class it chooses a bounded nonzero integral ideal J, then an actual
nonzero z whose norm magnitude is minimal in J, at most N(J)^2 and whose
coordinates have gcd1 in EVERY integral basis. Neither minimality nor
primitivity is supplied. The minimum need not generate J squared.

Exactly three invocations from the repository root:

```powershell
& research/ender_radius_bridge/run_phase76.ps1 build
```

FAIL55.1707368seconds: two unit-control subtype coercions. FAIL99.0056703:
unit-control positivity simplification mismatch. PASS51.8930719: typed
norm positivity and an explicit unit-norm rewrite. All nine public types,
all source before unit_control, and all reporting commands are identical.
Total206.0694790seconds. No heartbeat, time or memory resource stop and
no limit increase. All three invocation slots consumed; no further run.

The final invocation prints all9public types, three root axiom lists and
the complete namespace audit:12logical/12theorem/0runtime. Only propext,
Classical.choice and Quot.sound occur. Four controls cover zero and -2
scaling, the nonprimitive pair(4,6), and actual D7 unit-element primitivity
in every basis. The full audit rejects the first two incomplete controls;
both failed sources/logs remain in the12-file PHASE76_RAW.zip.

Saved-evidence check, without a Lean rerun:

```powershell
python research/ender_radius_bridge/verify_phase76_results.py
```

It verifies registration/runner, all raw/source/result hashes, unchanged
statements and main proof, budgets, final audit/axioms, preserved stopped75
and earlier evidence, unchanged production and unchanged README. The new
runner explicitly detects internal Lean resource diagnostics as stop_reason;
none occurred. This check establishes saved integrity, not human semantic
review or production CI coverage.

The proof closes primitivity, not basis completion or a leading-coefficient
bound. Class-wide B, even chart, field transport and new numerical range
remain open. No publication, merge, reviewer, upstream or Tao post.
[Human proof](LEAST_NORM_GUIDE.md).
