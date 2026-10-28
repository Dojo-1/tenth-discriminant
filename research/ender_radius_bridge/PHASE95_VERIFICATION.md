# Phase95: actual even kernels and one coherent controlled prime family

The FULL registered standalone theorem is proved:
`EvenPrimeFamily.controlled_family`. For positive squarefree d congruent
to 1 or 2 modulo4 and actual class number at most two, it constructs ONE
bounded class-indexed ideal family before ALL finite admissible prime sets.
That same family carries actual per-class calibrated form/count data and
supplies a selected set of exactly4*card(P) distinct tagged ideal elements.
Every selected point has actual norm magnitude p*N(J_C) for a p in P.
No family, maps, kernel distinction, four-lift or count premise is supplied.
[Human proof](EVEN_PRIME_FAMILY_GUIDE.md).

The actual even residue map is constructed through the maximal order.
Its generator maps to z, it is surjective, its actual kernel norm is p,
and the kernels for z,-z are distinct at odd primes not dividing d.
Generic kernel recovery, four-lift and aggregation operators are reused;
no odd-field actual residue map or odd controlled-family theorem is used.
ClassCountData records the SAME J_C's actual count and basis obligations.

[Protocol](PHASE95_PROTOCOL.md) and [runner](run_phase95.ps1) registered at
`4ad27da64dcf79f4e1e2ca344b612ceac19a0d1d` before source/execution.
Base `eb548173e7ce4834071ae94981694d2b6ecef4bd`.
Lean4.19.0; Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b`.

| Invocation | Result | Seconds | Observed peak process working set, bytes |
| --- | --- | --- | --- |
| Target1 | FAIL: coefficient cast under integer ring map | 36.1379252 | 3252224000 |
| Target2 | FAIL: simplification rewrote polynomial constant early | 36.1710641 | 3253620736 |
| Target3 | PASS: evaluation and cast normalization separated | 37.675812 | 3253415936 |

Total109.9848013s. All three target slots consumed: no target replay.
Time caps600s each,1200s cumulative; runner per-process guard8192MB.
No internal/outer resource stop. The only repairs are in the root-evaluation
proof argument of orderResidueMap. All13public theorem statements AND
proof bodies, three definition types, two later definitions, final family
assembly and five controls are unchanged. The mapping construction is
unchanged; its root proof is normalized explicitly. Failed definitions
had sorryAx dependencies and both namespace/input audits rejected those
attempts. Their complete sources/logs/results are preserved as failures.

Final source SHA256:
`f8b7476b57cc1e5482bdaa60a1c60324b2af8c137a954bc30dd1d8f606046e67`.
Namespace28logical/25theorems/0runtime auxiliaries; only `propext`,
`Classical.choice`, `Quot.sound`. Fresh final closure54,801 excludes the
same42old roots as94 plus five old odd-field map/family wrappers (47total).
Controls: Gaussian d1p5 actual kernel pair, characteristic-two root
collapse, actual ramified d5p5 zero-root map equality, zero-modulus guard
and empty finite-set aggregation. The selected cardinality is not a
claim that these are ALL representations of a prime.

## Verify the saved evidence

```sh
python research/ender_radius_bridge/verify_phase95_results.py
```

PASS: exact two proof-only repairs,13public types/proofs,3definition types,
fixed mapping construction, five controls, caps/snapshots/transcripts,
47 exclusions, [12rawfiles](PHASE95_RAW.zip), [manifest](PHASE95_RESULTS.json),
1,506frozen prior files and61README lines. It does not execute Lean.
Exact executed command from lean/:
`lake env lean -j 1 ../research/ender_radius_bridge/Phase95EvenPrimeFamily.lean`.
No other Lean invocation was made. Native cumulative time72.30898930000001
is retained verbatim; the budget verifier permits1e-10s rounding against
sum of serialized run durations. It does not alter the raw result JSON.

This is standalone, outside the productionroot. All prior production,
root, tools, pins, certificates, CI, reviews, ledgers, protocols, raw data,
verifiers and failed/stopped attempts remain frozen. The94whole-library
audit is historical, not a new95root audit. External exact-head CI and
independent human review are not claimed. Argon's report is still pending;
no report assessed or reviewer agent started. No publication or merge.

## Remaining comparison

Integration, the actual class-slice cardinality sum, complete weighted
split-prime loss, actual Minkowski normalization and contradiction on the
SAME original positive integer Gram remain open. Radicandd and actual
field discriminant4d need explicit matching. The unproved scalar-envelope
candidate is NOT a premise here. Existing field bounds are unchanged;
no even cutoff, full classification, novelty, optimality or upstream
acceptance is asserted.
