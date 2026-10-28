# Phase94: complete even prime-axis count integrated unchanged

`EvenPrimeAxis.controlled_class_prime_count` is now imported by the main
Lean root. One actual bounded ideal and basis per class under h<=2 give
the complete finite prime-normalized count, with no off-axis premise.
The calibrated principal class pays zero axis points; every other class
pays at most two across ALL primes in its fixed lattice. All 11 theorem
statements, proofs, five controls and reports are exact after imports.
There are no new definitions. [Human proof](EVEN_PRIME_AXIS_GUIDE.md).

Only dependency imports change, the standalone input command is relocated,
and one root import is appended. No mathematical repair or retry occurred.
One inherited blank EOF line is preserved at EvenPrimeAxis.lean:256 for
exact accepted-body transport; the verifier checks that precise exception
and all other new whitespace is checked. No standalone93 replay.

[Protocol](PHASE94_PROTOCOL.md) and [runner](run_phase94.ps1) registered at
`a943e4858575ec32b1405db4493b52ec38315c8f` before source/execution.
Base: `ceeaaf34932e71ab2d0c041e07fbf81671d4d590`.
Source SHA256:
`82b95f6809920d98cdbc5e64d2fd978dc71ee347ff533dbb385ea71f13a21423`.
Lean 4.19.0; Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b`.

| Invocation | Result | Seconds | Observed peak process working set, bytes |
| --- | --- | --- | --- |
| Module target | PASS, first | 70.1855337 | 3299962880 |
| Full root | PASS, first | 25.1691685 | 2799456256 |
| Fresh input check | PASS, first | 28.8799819 | 3147153408 |
| Whole-library audit | PASS, first | 31.0698475 | 3356360704 |

Time caps: target 600 s, root 1200 s, input/audit 180 s. Runner memory
guard: 8192 MB per owned process. No internal or outer resource stop.
Namespace: 13 logical declarations, 13 theorems, no runtime auxiliaries.
Whole library: 5,219 logical declarations, 4,434 theorems, 17,004 runtime
auxiliaries. Only `propext`, `Classical.choice`, `Quot.sound`.
Fresh target closure: 54,650 declarations, excluding the same 42 old roots
as93. All five inherited controls are unchanged and checked.
Structural coverage: 190 reachable modules; no proof escapes; all 250
saved interval endpoints match. This does not replay Arb inequalities,
old numerical campaigns or the earlier negative-control suite. No new
external CI is claimed.

## Verify the saved integration record

```sh
python research/ender_radius_bridge/verify_phase94_results.py
```

PASS: exact93 mathematical/control/report transfer, one root import,
42 exclusions, budgets/logs/snapshots, [25 raw files](PHASE94_RAW.zip),
[manifest](PHASE94_RESULTS.json) and 1,496 frozen prior files. It does not
execute Lean. The registered runner records each exact executed command.
Prior production proofs/tools/pins/CI/certificates/reviews/ledgers/protocols/
raw/verifiers and failed/stopped attempts remain unchanged. Historical
root-fixed verifiers stay at their accepted refs; none was weakened or
replayed on this changed root.

## Remaining arithmetic bridge

Construct actual even residue maps with distinct kernels and a coherent
class-indexed family, supply four labelled lifts per prime on THAT family,
then prove the class sum, weighted loss, actual Minkowski normalization
and contradiction on the SAME original positive integer Gram. Actual
field discriminant 4d and Gram parameter d need explicit matching.
No even cutoff, full classification, optimality, novelty or upstream
acceptance is claimed. Existing field bounds are unchanged. Independent
human review remains open; Argon's report has not appeared in the refreshed
review folder or been assessed. No reviewer agent started, publication
or merge performed.
