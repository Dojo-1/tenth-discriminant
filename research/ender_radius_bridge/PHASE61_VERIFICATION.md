# Phase61 verification: canonical excluded-prime loss

Protocol `fad0eac` preceded proof source and execution; base `c6cbb1f`.
The actual-Gram theorem, all geometry/prime guards and all fixed controls
compile in the production library. No arithmetic prefix bound or improved
cutoff is asserted. [Human argument](COUNT_TO_LOSS_GUIDE.md).

## Local results

- Target1 FAIL98.8740729s: the real-cast proof needed `lossScale` unfolded.
  Its full source, core snapshot and logs are retained. The namespace gate
  rejected the incomplete dependency (`sorryAx`); this was never accepted.
- Target2 PASS39.3685823s after that one proof-body repair. All nine new
  theorem type prefixes, definitions and guards are unchanged.
- Target3 PASS44.6006691s after removing an inherited trailing blank line.
  No theorem, proof token or guard changed. This build was already dispatched
  before the control-suite timeout was observed.
- Target total182.8433243s; all three allowed attempts consumed, no target
  resource stop. No further local proof or control run was started.
- Full root PASS23.0083248s (6822 build tasks).
- Compiled input checks PASS32.5598265s. The final theorem reaches48263
  declarations, none of the34 listed class-number-one/old-cutoff/
  classification/finite-answer roots. This checks the listed exclusions,
  not every possible formulation of an undesired premise.
- Whole-project compiled audit PASS30.2626588s:4821 logical declarations,
  4071 theorems,16978 runtime auxiliaries. Only `propext`, `Classical.choice`
  and `Quot.sound` are permitted.
- Structural coverage:168 reachable acyclic project modules, no source
  escapes; source correspondence: all250 endpoint pairs. The latter is
  identity checking, not Arb inequality certification.

Existing apparatus/API/audit controls PASS (exit0). The negative-control
wrapper exits1 when its existing120-second multiplicity sub-suite limit
is reached. **The local full regression suite is INCOMPLETE, not passed.**
Its partial output and traceback are preserved, without increasing the
limit or rerunning it. No matching surviving child was found on inspection.
Root/input/global-audit records above precede the final EOF-only cleanup;
target3 checks the final formatted modules. No proof token changed.

Exact-head Linux CI at `b4cff273f620ead13fc60097222fac01cce4ab67` now
PASSES: run40403267176/job121854391609. Decoded logs give250 source pairs
at21:19:24.7819216Z, audit4821/4071/16978 at21:35:06.0529577Z, and the
entire final control suite at21:40:28.3892260Z on26October2026. Same-head
CodeQL121854700666/actions121854377421/python121854377037 all pass.
[Final public record](https://github.com/Dojo-1/tenth-discriminant/pull/30#issuecomment-6428022437)
was posted before any later publication. This covers the integrated
production theorem. It does not rewrite the local Windows timeout as a
local pass or execute the separate Phase62 research file.

## Preservation and scope

`ExcludedPrimeAssembly.lean` transports the Phase59 core by changing only
imports, namespace, an explanatory header and final blank-line cleanup. Its proof bodies and eleven
public theorem statements are unchanged under that namespace transport.
`PrimeWeightKernel.lean` contains the new universal bound and canonical
kernel. The root gains two imports. Old production proofs, tools, pins,
certificates and CI gates are unchanged. The61-line README is unchanged.

The Phase59/60 source, raw archives, results and native Phase58 report stay
byte-for-byte frozen. Their earlier current-tree verifiers are historical
after production integration; the new verifier preserves the committed
prior bytes without claiming their old scope still describes this root.
No new reviewer was dispatched. No new cutoff/classification, optimality,
Mathlib acceptance, human review or historical-year claim is made.

## Commands

From repository root, with pinned elan binaries on PATH:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File research/ender_radius_bridge/run_phase61.ps1 build
powershell -NoProfile -ExecutionPolicy Bypass -File research/ender_radius_bridge/run_phase61.ps1 root
powershell -NoProfile -ExecutionPolicy Bypass -File research/ender_radius_bridge/run_phase61.ps1 input
powershell -NoProfile -ExecutionPolicy Bypass -File research/ender_radius_bridge/run_phase61.ps1 audit
python lean/verify_sources.py
python lean/apparatus_controls.py
python lean/negative_controls.py
python research/ender_radius_bridge/verify_phase61_results.py
```

The runner preserves each source and raw result and enforces the registered
build budget. Do not restart the frozen original Phase59/60 campaigns.
The evidence verifier reads saved bytes; it does not rerun Lean or prove B.
Its first invocation used the wrong log encoding and failed while reading;
UTF-8 was then established from the actual bytes and the reader corrected.
No raw byte was changed. The saved-evidence check now passes, including
the preserved timeout; that integrity PASS is not a regression-suite PASS.
