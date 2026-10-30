# What each verification layer establishes

These records concern different source versions and different questions.
Successful compilation, semantic reconstruction and independent review are
separate evidence; a result is never transferred just because code is related.

| Evidence | Exact scope | What remains outside it |
|---|---|---|
| [Argon referee report](https://github.com/Dojo-1/tenth-discriminant/blob/06d3986e3e12830dca3ecda0a73bc0573a6b6405/audit/REFEREE_REPORT.md) | Frozen39e9ce3/173modules;positive semantic/source assessment of canonical classification and arbitrary-field50btheorem;no defect confirmed | Verdict remains insufficient evidence. Its own build timed out and axiom audit was not completed. No later radial48bcoverage. |
| [Existing EXACT-frozen project CI40476544973](https://github.com/Dojo-1/tenth-discriminant/actions/runs/40476544973) | Push at39e9ce34d09ed9f990fab4b9ed5e3980cee64119,attempt1;full build,audit4917logical/4155theorems/16985runtime,250pairs and complete control driverPASS | This is projectCI evidence at the exact reviewed source, not Argon's independent environment replay or a human derivation. |
| [PR43 proofCI40902563385](https://github.com/Dojo-1/tenth-discriminant/actions/runs/40902563385) | Source182ea00/tested62d241f,identical tree;202modules,5584logical/4772theorems/17029runtime;full controls/securityPASS | Later local documentation and Phase125/structural proof work are not covered by that run. |
| [Arithmetic reconstruction](TWO_SIDED_ARITHMETIC_GUIDE.md) and Phase123 | Actual quotient observations and two-sided integer middle matrix;one sealed80-case exact check | Same-assistant derivation, not independent peer review. Finite cases alone do not prove the universal statement. |
| [Geometric reconstruction](GEOMETRIC_COMPARISON_GUIDE.md) and Phase124 | Radius,cell counts,ordinary jets and normalized upper inequality;ten fixed rational checks | Arithmetic prime-mass/tail lower estimate is identified as inherited. Rational checks do not prove analytic premises. Reader route for that lower estimate M: [HUMAN_RECONSTRUCTION, arithmetic](../tight_radial_v1/HUMAN_RECONSTRUCTION.md#arithmetic-the-lower-pressure); P: `RadialCutoff.recovered_mass_le_actual_log` (`M <= log det G`) and `RadialCutoff.recovered_normalized_lower` (`0.999997 log D - 5.739 <= M/(R^2 S)`). |
| [Phase125 successor](PHASE125_VERIFICATION.md) | Complete actual-field47.5btheorem,namespace and three fresh closuresPASS on first call | Integrated unchanged by Phase128 with all local checks; exact-head newCI/publication separate. Phase122failure stays preserved. |
| [Phase132 47.1b endpoint](../sharp_radial_v1/ENDPOINT_RECONSTRUCTION.md) / [PR #48](https://github.com/Dojo-1/tenth-discriminant/pull/48) | Exact source `b16e835` compiled both sharper same-Gram inequality and full actual-field endpoint; [run 41087748526](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41087748526) completed root source match, 208 project modules, standard-three-axiom audit, and known-false controls; focused Lean/CodeQL PASS; merged into main as `6fe9e67` | Formal proof of exact encoded statement, not independent semantic reconstruction, mathematical novelty or optimality. Future 47b tightening remained H then; now P (Phase133 row). |
| [Phase133 47.0b endpoint](../tight_radial_v1/HUMAN_RECONSTRUCTION.md) / [PR #49](https://github.com/Dojo-1/tenth-discriminant/pull/49) | Source `761f4f1`, merged by ordinary merge as `dddeae5`. `TightRadialEndpoint.totallyComplex_degree_two_classNumber_one_discriminant_bound_47b` proves `(NumberField.discr K).natAbs < 47000000000` for every totally complex degree-two number field K with class number one. [Run 41098122516](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41098122516) (PR merge ref `a44c9d7`, which differs from `761f4f1` only in Markdown) passed: source digest and all 250 interval pairs; lake build (6,864 jobs); audit of 5,729 logical/4,914 theorem declarations (17,029 runtime-only excluded) with standard axioms only; negative controls. Failed runs [41095139730](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41095139730) (`534f742`) and [41096816617](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41096816617) (`6163cd7`) are preserved in the [receipt](../tight_radial_v1/PHASE133_VERIFICATION.md). 210 modules. | Independent human semantic review ([#50](https://github.com/Dojo-1/tenth-discriminant/issues/50), R). |
| Phase126/127 structural proofs and Phase128 integration | Arbitrary-field iff and actual radial action; 19 public types/2 private helpers integrated exactly, all four first checks PASS; 205 modules, 5619 logical/4807 theorems/17029 runtime | These are project checks and same-assistant reconstructions. Exact-head publication and independent semantic review are separate. |
| Main at `841852d` (before #52) | From `761f4f1` to `841852d` only 11 Markdown files change; nothing under `lean/` or `.github/`. [Main run 41105564205](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41105564205) passed source correspondence, lake build and audit. | Its negative-controls step was cancelled by the 25-minute job timeout, so this run is **NOT** a full pass. The formal content is covered by run 41098122516: its tested tree differs from `841852d` only in Markdown, so `lean/` and `.github/` are identical. |
| Main at `10e5db6` (after #52) | [#52](https://github.com/Dojo-1/tenth-discriminant/pull/52) merged as `648cba2`; it adds `lean/TenthDiscriminant/RankDivisorCompatibility.lean` (+1 root import; 211 modules) and `.github/workflows/phase134-minors-lean.yml`. [Run 41126571097](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41126571097) (push on `10e5db6`) passed: source digest and all 250 interval pairs; lake build (6,865 jobs); audit of 5,742 logical/4,926 theorem declarations (17,032 runtime-only excluded) with standard axioms only; negative controls. | Phase134 adds no step of the 47.0b chain and no cutoff; its semantics stay with [#51](https://github.com/Dojo-1/tenth-discriminant/issues/51)/[#52](https://github.com/Dojo-1/tenth-discriminant/pull/52). [#50](https://github.com/Dojo-1/tenth-discriminant/issues/50) remains R. |

Issue [#50](https://github.com/Dojo-1/tenth-discriminant/issues/50) obligations: each encoded statement below is P; each obligation stays R until independent semantic review closes #50.

| #50 obligation | Checked declarations (P) | Reader route | Status |
|---|---|---|---|
| 1. Freeze the objects | definition `integerRectangularTraceGram`; `imaginaryQuadratic_discr_natAbs` | [Build the object](../tight_radial_v1/HUMAN_RECONSTRUCTION.md#build-the-object-only-once) | R |
| 2. Arithmetic divisor | `rectangularTraceGram_valuation_of_classNumber_one`; `RadialCutoff.recovered_mass_le_actual_log`; `RadialCutoff.recovered_normalized_lower` | [Two-sided guide](TWO_SIDED_ARITHMETIC_GUIDE.md); [arithmetic](../tight_radial_v1/HUMAN_RECONSTRUCTION.md#arithmetic-the-lower-pressure) | R |
| 3. Geometric comparison | `RadialCutoff.integer_det_positive`; `TightRadialSaving.production_normalized_upper_tight` | [Geometric guide](GEOMETRIC_COMPARISON_GUIDE.md); [geometry](../tight_radial_v1/HUMAN_RECONSTRUCTION.md#geometry-the-upper-pressure-same-g) | R |
| 4. Contradiction and field return | `TightRadialEndpoint.endpoint_certificate`, `endpoint_separation`, `odd_large_classNumber_ne_one_47b`, `imaginaryQuadratic_large_classNumber_ne_one_47b`, `totallyComplex_degree_two_classNumber_one_discriminant_bound_47b` | [Where 47000000000 enters](../tight_radial_v1/HUMAN_RECONSTRUCTION.md#where-the-number-47000000000-enters) | R |

All173Argon-reviewed module blobs and pinned toolchain/lakefile are unchanged
in the inherited202-module base;29modules were added later. Phase128 adds
three more modules, giving205. Thus its
source findings remain relevant to the inherited core, without reviewing the
new modules or independently establishing the full proof. Phase132 has 208
modules; Phase133 and main at `841852d` have 210; #52 adds one, giving 211
at `10e5db6`. All 173 Argon-reviewed module blobs, the pinned toolchain and
the lakefile are byte-identical to `39e9ce3` at `10e5db6`.

The historical exact-source run finished27October2026at09:16:36UTC. Its full
3,165,168-character log was inspected and archived with the run/job metadata
and exact frozen audit/control drivers. [Receipt](ARGON_EXACT_FROZEN_CI_RECEIPT.json)
· [Six raw artifacts](ARGON_EXACT_FROZEN_CI_RAW.zip). Source checkout SHA,
job success,compiled audit and final controlsPASS all match the frozen object.
No new build or retry was dispatched. The first observer incorrectly expected
newer per-family markers;inspection of the older driver confirmed eight
`check=True` calls followed by its finalPASS. The corrected observation is
recorded;the test standard and historical result were not changed.

The integration, full-root audit and publication gates described above are
now closed at [03cb58c](https://github.com/Dojo-1/tenth-discriminant/commit/03cb58c25975ed638bebfa3bcc5b2a3152e9f452):
[proof CI41021656669](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41021656669)
and [security41021651935](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41021651935)
passed on that head. Its tree is identical to mathematical source58b9371.
The full build,250certificate pairs,5619logical/4807theorems/17029runtime,
eight synthetic tests and all eight control families passed. The actual
runner checkout3d44376 has that same tree. **Publication update (30 October 2026):** PR45 was merged into `main` as [merge commit 3352f9d](https://github.com/Dojo-1/tenth-discriminant/commit/3352f9d38b6a2540f331b38e2faad3fa558ce234). The original verification describes the tested source/tree and is not retroactively a different CI result; independent human semantic review remains open.

Independent human semantic review remains open. The new
[exterior-volume reconstruction](EXTERIOR_VOLUME_GUIDE.md) is another
mathematical representation by the same assistant; its finite comparator
does not turn project verification into independent peer review.
