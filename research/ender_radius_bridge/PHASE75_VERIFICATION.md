# Phase75: stopped controlled-basis attempt

Registration `f589ca5` precedes source/execution on base `9996c82`.
Fixed target: an actual controlled ideal basis/form with 0<a<=N(J), then
one such bounded ideal and basis per actual class under h<=2 in the odd
squarefree maximal-order chart. No primitive/basis/coefficient premise.

One invocation from the repository root:

```powershell
& research/ender_radius_bridge/run_phase75.ps1 build
```

FAIL after39.4407757seconds, exit1. The outer runner's stop_reason is empty:
the600second/8192MB thresholds were not reached. The Lean log separately
records deterministic timeouts at the default200000heartbeat limit while
assembling the actual normalized-form witnesses. The protocol explicitly
includes internal heartbeat exhaustion in its resource-stop rule. Therefore
this campaign is stopped, with no repair, second/third invocation, raised
limit, imported fallback or later reinterpretation as success.

Other visible errors: primitive_basis leaves a reflexive equality goal;
incorrect Int.natCast_natAbs.symm projection syntax; unfinished Squarefree7
control. The final namespace audit rejects PROJECT_AXIOM at unit_ideal_control.
No AUDIT_OK exists for the namespace. Printed theorem types or a root saying
no axioms while its declaration failed are not evidence of an accepted proof.
No controlled-basis main root is accepted here.

All four raw files are preserved in PHASE75_RAW.zip. The source remains
unchanged after its sole attempt. Run only the saved-evidence check:

```powershell
python research/ender_radius_bridge/verify_phase75_results.py
```

It verifies registration, exact source/log/result/archive hashes, one run,
internal/outer resource distinction, audit rejection and unchanged prior
production/evidence. It does not invoke Lean. This is a formalization failure,
not a mathematical counterexample or an accepted partial coefficient bound.
The accepted controlled-vector theorem74 remains unchanged; the50-billion
h=1 cutoff remains unchanged. No publication/merge/reviewer/Tao post.
[Human explanation](CONTROLLED_BASIS_ATTEMPT.md).
