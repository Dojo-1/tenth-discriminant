# Phase82: a concrete weighted budget on the original determinant

The local Lean proof now carries the actual h<=2 prime-prefix count into
the weighted arithmetic loss for the original derivative trace-Gram.
It chooses every available nonsquare prime as good, proves exact coverage
of the remaining nondivisor primes, and pays parameter divisors separately.
There is no supplied counting function, good-prime coverage assumption,
class-number-one assumption or older cutoff in the new theorem.

This is a finite weighted inequality, not a new numerical cutoff. Its
explicit finite kernel cost still needs a useful closed estimate. The
Minkowski term, field-parameter transport and even chart remain obligations.
[Human explanation](WEIGHTED_SPLIT_GUIDE.md).

## Registered execution and one recorded discrepancy

Base: `5207326b5e941d52c14184a769ae409fd6003557`.
Registration: `9e3f5e59b9d0ed90ccfa753c64ce50f0fa71bb33`.
The accepted Phase81 source was transported with only its first import
changed; the new budget module and two root imports are the production diff.
No proof repair or second target invocation occurred.

| Check | Exact invocation from `lean/` | Result | Seconds |
|---|---|---|---:|
| Target | `lake build TenthDiscriminant.ClassAggregation TenthDiscriminant.SplitPrimeBudget` | PASS, first attempt | 102.4795045 |
| Root | `lake build` | PASS, once | 32.6526531 |
| Dependencies | `lake env lean -j 1 ../research/ender_radius_bridge/Phase82InputCheck.lean` | PASS, once | 43.1749583 |
| Whole-library audit | `lake env lean -j 1 Audit.lean` | PASS, once | 38.4201912 |

The registered runner mistakenly encoded a 182-second input/audit cap
instead of 180, from a broad phase-number replacement. The input run's
actual duration was below 180 seconds, but its enforcement limit was 182.
This is a protocol discrepancy, not an exactly conforming input run.
Its raw metadata remains unchanged. No check was rerun to conceal it.
Before the audit, commit `a36bde9617539b7521f1c352ef32e0b2c4cd3e66`
preserved the original runner and [addendum](PHASE82_RUNNER_ADDENDUM.md),
and reduced the future cap to 180. The audit used that corrected cap.
All four runs stayed below the 8,192 MB threshold; no resource stop occurred.

## What the checks establish

The new namespace audit checks 19 logical declarations / 16 theorems;
transported ClassAggregation checks 8 / 8. The full audit checks 5,058
logical declarations / 4,285 theorems, with 16,993 runtime auxiliaries
reported separately. Only `propext`, `Classical.choice`, `Quot.sound`
are admitted. Dependency closures of the count and weighted-budget roots
visit 54,831 and 57,545 declarations respectively and exclude the same
34 named class-number-one, older-cutoff and finite-answer inputs.

Controls cover an actual split prime (D=7,p=11), removal of divisors,
selection of every nonsquare prime, and the empty set. Transported controls
retain class labels and the h<=2 boundary. Structural checks cover 183
reachable project modules and absence of source escapes. All 250 endpoint
pairs match the existing Lean recurrence; this is endpoint identity, not
a rerun of Arb inequalities or the numerical regression campaign.

Pins remain Lean 4.19.0 and Mathlib
`c44e0c8ee63ca166450922a373c7409c5d26b00b`.
The [manifest](PHASE82_RESULTS.json) hashes all four source/root/input
snapshots, raw logs/results, the original runner/addendum, and frozen prior
sources, protocols, reports and evidence. The [archive](PHASE82_RAW.zip) contains
31 files. Verify saved integrity from the repository root with:

```sh
python research/ender_radius_bridge/verify_phase82_results.py
```

This command does not rerun Lean. Earlier stopped attempts, historical
verifiers and reviews remain unchanged. External CI for this exact source
and independent human review are not claimed. The class-number-one cutoff
remains 50 billion; no full-classification announcement follows.

Reader checks: all392 local links in the eight updated reader documents
resolve, and the README stays61lines. Whitespace checking reports one
inherited final blank line at ClassAggregation.lean:183. It is retained
because the registered transport permits only the first-import change;
no checked source was edited after its snapshots. Other changed files
pass the whitespace check.
