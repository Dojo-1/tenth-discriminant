# Phase44: current human entry points, unchanged mathematics

Protocol-only commit `6447409` preceded the edits. Baseline mathematical
head: `e2848c8fd767381cfcb73504f033af61a8a21ee0`. This is an internal
source/document correspondence correction, not independent semantic review.

The current source declarations inspected were:

- `ClassNumberClassification.lean`: positive squarefree d, actual class
  number, exact nine-radicand iff; the certificate premise is discharged.
- `QuotientFiberClassification.lean` and `QuotientFiberCertified.lean`:
  original cutoff, all eleven seed proofs and all nine positive cases
  supply that iff. The new 100-billion cutoff is not its proof input.
- `ClassNumberInertBridge.lean`: actual maximal-order norm lifting supplies
  nonsquareness and the original integer-Gram valuation, under the strict
  small odd-prime and squarefree odd-chart guards.
- `TunedAnalyticCutoff.lean`: both actual public 100-billion bounds have
  positive-squarefree d and actual class number one only.
- `QuadraticChartEquivalence.lean` and `EvenQuadraticField.lean`: the
  canonical field is the actual rational quotient by `X^2+d`.

The short spine no longer calls those supplied bridges open. Its formulas,
examples and section names are retained. The interpolation guide now gives
current navigation, rather than three incompatible historical frontiers.
README puts earlier checkpoints inside one historical disclosure; current
proof links, attribution and review limits remain visible outside it.

A one-off Python standard-library read-only check compared each document
with `git show e2848c8:<path>`, extracted heading lines and `$$` display blocks,
and checked equality. It resolved every relative Markdown link against the
document's directory. Results below are a transcription, not a raw log:

| Document | Existing local targets | Headings retained | Display blocks retained |
|---|---:|---:|---:|
| README | 80 | 13 | 4 |
| HUMAN_GUIDE | 65 | 32 | 32 |
| MATHEMATICAL_SPINE | 37 | 9 | 8 |

All checks PASS. The first check failed at the single-disclosure assertion:
an older nested disclosure remained in README. Its redundant opening/closing
tags were removed, retaining its full content; the same assertion then passed.
No acceptance rule was weakened. This checks source structure, not a rendered
browser/GitHub visual review or new mathematical correctness.

Re-run existing evidence and source-diff checks from repository root:

```powershell
python research/ender_radius_bridge/verify_phase43_results.py
git diff --exit-code e2848c8 -- lean/TenthDiscriminant lean/TenthDiscriminant.lean lean/lean-toolchain lean/lakefile.lean .github/workflows tools
git diff --check
```

PASS: Phase43's four records, three input closures, unchanged candidate body,
negative history, source/archive hashes and 507 reader targets. Mathematical,
dependency-pin, workflow and production-code diff is EMPTY. No extra Lean
run, parameter test, numerical pilot or altered frozen record.

Pinned CI40172177485 on the baseline finished SUCCESS on25 October2026
at07:36:56 UTC. Its full build, namespace audit and inherited rejection
gates pass; audit4602 logical/3868 theorem/16955 runtime-only. Security
40172174676 and separate CodeQL also pass. Synthetic mergeac9d4f11 has
the identical baseline tree. The [final mathematical-head record](PHASE43_PUBLICATION_FINAL.md)
was posted as [comment6394963969](https://github.com/Dojo-1/tenth-discriminant/pull/28#issuecomment-6394963969)
before the documentation-only push. The same CI run finished; no cancellation
or restart. New publication-head CI is distinct. Independent human review,
Mathlib acceptance and human-authored external reporting remain open.

The user clarified on25 October that Gemini Argor's peer review covers only
earlier work, not the100-billion proof at e2848c8. It must not be transferred
to that new mathematical head. PR28's latest-review list was also empty
when inspected; that observation alone is not a search of every review record.
