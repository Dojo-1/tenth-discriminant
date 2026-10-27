# Phase67: the actual arithmetic bridges enter production

**All registered local checks PASS. New-head pinned CI is still required.**
Protocola4f9a0c precedes source7406e4d. Both arithmetic modules are the exact
accepted Phase65/66 sources with only the registered acyclic imports changed.
Their definitions, statements, guards, proofs, controls and prints are unchanged.
The production root imports both; no old proof/tool/pin/gate was modified.

| Once-registered check | Result | Seconds |
|---|---|---:|
| Both production modules | PASS, first attempt | 37.853676 |
| Complete root build | PASS | 19.7922849 |
| Types and3 dependency closures | PASS | 29.283270899999998 |
| Whole-library compiled audit | PASS | 24.978388799999998 |

The literal elapsed values above are preserved from the process records.
No repair, extra target invocation, resource stop or prior-campaign rerun.
Structural checks cover172 reachable modules, reject proof escapes and
confirm the original250 source endpoint pairs. Endpoint correspondence
is not certification of the Arb inequalities.

The complete audit checks4,897 logical declarations,4,139 theorems and
16,985 runtime-only auxiliaries, using only the standard3 axioms.
The two new namespaces separately report13/13/0 and15/12/3.

The full printed types and NormLift predicate retain the same matrix and
radius guards, nonzero ideals, norm magnitude and fixed-class quantifier
order. Three dependency closures reach13,764 (prime-divisor mass),48,266
(full Gram budget),53,052 (residue-class lifting) declarations. All exclude
the same34 listed old h1/cutoff/classification/finite-answer roots, resolve
all visited inputs, reject unsafe declarations and allow only propext,
Classical.choice and Quot.sound. This finite forbidden list is not a claim
about every possible semantic dependence or independent human review.

## Reproduce the saved record

The runner was invoked once per mode from the repository root:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File research/ender_radius_bridge/run_phase67.ps1 -Mode build
powershell -NoProfile -ExecutionPolicy Bypass -File research/ender_radius_bridge/run_phase67.ps1 -Mode root
powershell -NoProfile -ExecutionPolicy Bypass -File research/ender_radius_bridge/run_phase67.ps1 -Mode input
powershell -NoProfile -ExecutionPolicy Bypass -File research/ender_radius_bridge/run_phase67.ps1 -Mode audit
```

The first line builds both modules; no separate probe bypasses its budget.
Exact lake arguments, source hashes and resource observations are recorded
in PHASE67_RESULTS.json. PHASE67_RAW.zip preserves21 raw files, including
both source snapshots per invocation and the structural/source-check log.

```powershell
python research/ender_radius_bridge/verify_phase67_results.py
```

This checks saved integrity, transport, ancestry and frozen prior artifacts;
it does not rerun Lean. Phase65/66 original source/results/raw and verifiers
remain unchanged. Their fixed-current-production checks are historical at
their frozen refs after these new imports; this cycle preserves their bytes
without weakening old manifests or relabeling their execution scope.

## Human meaning and remaining work

[Prime-divisor loss](PRIME_DIVISOR_LOSS_GUIDE.md) removes parameter divisors
from the missing prefix-count input. [Class-fiber lifting](CLASS_FIBER_GUIDE.md)
places actual residue ideals in fixed ideal norm lattices and recovers them.
The bound on an ideal's norm is not a leading-coefficient bound in any basis.
Controlled form coordinates/discriminants, prime-pair/multiplicity and field
ramification transport remain open. No arithmetic B, new cutoff or full
classification is inferred. The prior Windows regression timeout remains
incomplete; the unchanged full suite is reserved for new-head pinned Linux CI.
No earlier review or CI success is transferred to these production additions.

## Completed publication baseline

Before this follow-up was published, exact PR32 head9705cac completed pinned
Lean CI40416976865/job121901646441. Decoded UTC logs on26October2026 confirm
250 pairs23:04:20.5954630Z, audit4869/4114/16982 at23:20:31.1098448Z and full
final controls23:25:43.0069365Z. [Terminal public record](https://github.com/Dojo-1/tenth-discriminant/pull/32#issuecomment-6429752867)
precedes this publication. Only Lean is reported; absent security checks
are not passes. This older tree does not contain the new arithmetic modules.
The new exact head requires its own build/audit/full regression result.

## Completed arithmetic-head CI

Exact published head564321005e8c9a34e5541dce8205e0e29b21caf7 completed pinned
Lean CI40419910108/job121911466303 SUCCESS. Decoded UTC logs on26October2026
record250 pairs23:28:40.0874486Z, ClassFiber15/12/3 at23:32:20.0661184Z,
PrimeDivisorLoss13/13/0 at23:33:57.5091293Z, global4897/4139/16985 at
23:45:12.2416271Z and full final regression23:50:27.5010638Z.
[Terminal public record](https://github.com/Dojo-1/tenth-discriminant/pull/33#issuecomment-6430115337)
preceded later publication. Only Lean is reported; absent security checks
are not passes. This run covers the two production arithmetic modules,
not subsequent standalone Phase68 multiplicity or failed Phase69 coordinates.
