# Phase86: all-range actual odd-chart class-number exclusion

**PASS locally, standalone.** For all natural D>=2^50 with squarefree D
and D=3mod4, `UniformTwoClass.odd_classNumber_gt_two` proves
2<classNumber(QuadraticField((D+1)/4)). The threshold is1125899906842624.
This is no longer just the sampled scalar margin from85.
[Human proof](ODD_TWO_CLASS_BOUND_GUIDE.md).

Base60c2eef43e1c1428f14819e5a26a6f4a4956c058.
Registration32ca2e1f5bbb5aec3cdde2075ed1f587dd23a090 before source/execution.
The standalone source imports unchanged root84. No production Lean, root,
tool, certificate, dependency pin or CI gate changed.

| Invocation | Exit | Seconds | Result |
|---|---:|---:|---|
| First | 1 | 79.5313154 | Endpoint-number rewrites, implicit coercions and multiplication normalization failed; audit rejected dependent sorryAx. |
| Second | 1 | 46.5392337 | One remaining endpoint argument-inference failure; audit rejected dependent sorryAx. |
| Third | 0 | 48.5733911 | Full actual-class-number theorem, all-range helpers, controls, namespace and transitive dependency checks passed. |

Total174.6439402seconds. Each cap600seconds/8192MB; cumulative1200.
No internal or outer resource stop; measured peaks stayed below8192MB.
ALL3registered target slots are consumed. No target rerun after acceptance.

The21public theorem statement texts and2definitions are unchanged across
all attempts. The final actual-class-number proof body is also byte-identical.
Repairs only normalize constants/casts/inverses/multiplication and provide
explicit endpoint types/transitive inequalities in helpers. Controls and
reporting are unchanged. All twelve raw files remain in the archive.
The nonfatal unnecessarySeqFocus warning is preserved, not suppressed.

The complete invocation from `lean/` was:

```sh
lake env lean -j 1 ../research/ender_radius_bridge/Phase86UniformTwoClass.lean
```

It includes all21public checks, both new definitions, chartCost, the final
root axiom list, namespace audit and fresh transitive assumption check.
Namespace:42logical declarations/40theorems;3runtime auxiliaries excluded.
Root closure:59,721declarations, excluding the SAME34named h1, older-cutoff,
classification and finite-answer inputs as84. In particular the old
rawPrimeMassLower_uniform is not a dependency. Only propext,
Classical.choice, Quot.sound are admitted. No numerical85output is imported.
The generic scalar helpers are applied under their existing guards;
no class-number-one or earlier exclusion theorem is a premise.

Controls check the exact endpoint integer, zero shift, rejection of the
a=0 coefficient guard, and the exact positive rational separation margin.

Pins remain Lean4.19.0 and Mathlib c44e0c8ee63ca166450922a373c7409c5d26b00b.
[Source](Phase86UniformTwoClass.lean), [protocol](PHASE86_PROTOCOL.md),
[manifest](PHASE86_RESULTS.json), [raw archive](PHASE86_RAW.zip).
Verify saved evidence without running Lean:

```sh
python research/ender_radius_bridge/verify_phase86_results.py
```

The verifier checks hashes, exact statement/definition/main-proof preservation,
all repair deltas, results, budgets, axioms and exclusions, plus frozen prior
sources/evidence. Root84is unchanged; its full build/audit is historical,
not a new full-library verification of86. Numerical85remains its own sealed
experiment, with negative samples and missing memory observation preserved.
External exact-head CI, root integration and independent human review of86
remain outstanding. Even-chart/arbitrary-field transport and classification
are not supplied. The stronger h1field cutoff remains50billion.

Reader checks: all 420 local links in the eight updated reader documents
resolve; README remains 61 lines. Changed-file whitespace check passes.
