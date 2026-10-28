# Phase74: saved verification and limits

Registration `36ff708` precedes source and execution on base `cde93ff`.
The actual theorem `ClassSquare.bounded_class_vector` assumes
NumberField.classNumber K<=2, chooses an actual bounded ideal of EACH
class, and produces an actual nonzero element whose principal ideal is
J*J and whose norm magnitude is N(J)^2. NormLift additionally retains
membership and exact ideal recovery. No PID or classification premise.

Command from the repository root, run exactly twice:

```powershell
& research/ender_radius_bridge/run_phase74.ps1 build
```

Attempt1 FAIL26.6258372seconds: an implicit argument to pow_card_eq_one
was passed explicitly. Its failed source and sorryAx audit rejection are
preserved. Attempt2 PASS27.7909568seconds: only that inference line changed;
all eight public theorem types and four controls are identical. Total
54.4167940seconds. Neither run hit the600second/8192MB thresholds or a
Lean resource stop. No default limit or heartbeat increase; no third run.

The passing invocation prints all eight public types, complete NormLift
and normBound definitions, two root axiom lists and the full namespace
audit:9logical/9theorem/0runtime. Only propext, Classical.choice and
Quot.sound occur. Four controls cover identity, order-three failure,
zero exclusion and an actual rational-field instantiation. This audit
does not independently validate mathematical interpretation.

All eight raw files are retained losslessly in PHASE74_RAW.zip. Run:

```powershell
python research/ender_radius_bridge/verify_phase74_results.py
```

That saved-evidence verifier checks hashes, registration ancestry,
unchanged statements and exact one-line repair, budget, printed axioms,
audit and preserved prior sources/raw, production and README. It does
not execute Lean. Standalone source remains outside production Root/CI.
PR35 CI40426517803/job121933520286 is separately SUCCESS at exact head
`e77a446`, verified after this evidence was assembled. Its decoded full
controls marker is 2026-10-27T00:50:44.1424884Z; namespace audit is
4963/4196/16993. Only Lean is reported by the exact-head checks API.
That result covers production72, not this standalone74 or local73.

The result closes the controlled-vector step, not primitive reduction,
unimodular basis extension, leading coefficient control, class-wide
usable B, even chart, field transport or a new cutoff. No old campaign
was replayed, no failed result replaced, no merge/reviewer/Tao post.
[Human proof](CLASS_SQUARE_GUIDE.md).
