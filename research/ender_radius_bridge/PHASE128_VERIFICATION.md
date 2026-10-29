# Exact integration of the endpoint and structural interfaces

**All four registered first checks passed.** Production now contains
`EndpointCutoff`, `FieldClassification` and `RadialAction`, with three root
imports. [Short mathematical explanation](STRUCTURAL_BRIDGE_CURRENT.md).

Protocol commit `3e95187dbcafc6c4a6fe77cb1964268d35a99479` preceded production
edits. Nineteen public theorem types/proofs and two private helpers from
accepted Phase125/126/127 are unchanged after the registered namespace rename
and leading dependency imports. No mathematical repair or additional import
was needed. Old proof sources, controls, workflows, pins and certificates
remain unchanged. All earlier failed proof sources and outcomes are preserved.

| Check | Seconds | Registered cap | Native result |
|---|---:|---:|---|
| Three-module build | 42.3759818 | 600 | 0 |
| Full root build | 34.3232739 | 1200 | 0 |
| Nineteen types / eight fresh closures | 93.5216249 | 240 | 0 |
| Compiled whole-library audit | 44.1793535 | 180 | 0 |

All checks used default heartbeat/recursion limits and an 8192MB threshold
per owned process. Sampled per-process working-set peaks are saved in the
native records; they are neither aggregate nor exact peak measurements.
No resource stop, proof-body edit, second invocation or proof replay occurred.

The new namespaces have respectively 17, 2 and 16 logical declarations,
all theorems, including compiler-generated proof helpers. The whole audit is
5,619 logical declarations / 4,807 theorems / 17,029 runtime auxiliaries.
Exactly 35 logical declarations were added, none removed, matching the
registered prediction; 205 project modules are reachable from the root.

The endpoint retains three fresh closures and 77 excluded roots. The field
interface retains two closures, four required inputs and eight forbidden
newer cutoff roots. Radial composition retains three closures, the actual
matrix requirement and 70 exclusions. Every closure allows only `propext`,
`Classical.choice` and `Quot.sound`. The nonmultiplicativity control is intact.

One preflight bookkeeping error used character offsets where UTF-8 byte
offsets were needed. It was corrected before any Lean invocation. Mathematical
sources were unchanged; no trial was consumed or restarted.

[Correspondence](PHASE128_CORRESPONDENCE.json) · [Native results and inventory](PHASE128_RESULTS.json)
· [33 raw artifacts](PHASE128_RAW.zip) · [Saved-evidence verifier](verify_phase128_results.py).

The exact local commands, from the repository root, were:

```powershell
powershell -NoProfile -File research/ender_radius_bridge/run_phase128.ps1 -Mode build
powershell -NoProfile -File research/ender_radius_bridge/run_phase128.ps1 -Mode root
powershell -NoProfile -File research/ender_radius_bridge/run_phase128.ps1 -Mode input
powershell -NoProfile -File research/ender_radius_bridge/run_phase128.ps1 -Mode audit
python research/ender_radius_bridge/verify_phase128_results.py
```

These one-shot checks are already terminal; do not rerun them. The saved
verifier reads evidence rather than replaying a theorem or experiment.
Main retains the published 48-billion result. A frozen-head draft PR and its
unchanged pinned CI/security gates remain separate publication requirements.
This is project verification, not independent human semantic review, a new
classification method, Mathlib acceptance or an optimality claim.
