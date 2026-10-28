# Phase88 verification: the odd bound belongs to the actual field

For any number field K of rational degree two, totally complex, with
actual class number at most two and ODD actual absolute discriminant:

    (NumberField.discr K).natAbs < 2^50.

The theorem is `OddFieldTwoClass.arbitrary_odd_discriminant_bound`.
No generator, coordinate chart, field isomorphism, squarefree parameter,
count estimate or numerical margin is supplied. The new generic theorem
`field_classNumber_eq` proves equality of class numbers under rational
field isomorphisms. It uses a representative-independent bijection of
actual ideal classes, with an inverse. This is a bijection of class sets;
a checked multiplication-preservation theorem is not claimed.

[Human explanation](ODD_FIELD_TWO_CLASS_GUIDE.md) explains each invariant.
[Protocol](PHASE88_PROTOCOL.md) was committed at
`bb1fbf319a56fbe09a4e9d4e9218461d72b039f1` before source/execution.
Base: `571b62eca4b4652b9c69eb06ecc78d341ec9e1bb`.
Final source SHA256:
`6bffb5cdd19ae7b0257eb3e0ff4e55b053e36b45e8fdf16f81a0abf414001c75`.
Lean4.19.0; Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b`.

## Complete execution record

| Invocation | Result | Seconds | Observed peak bytes |
| --- | --- | --- | --- |
| Target1 | FAIL: identity-control elaboration | 35.8059275 | 3347083264 |
| Target2 | FAIL: same control, explicit ideal still missing | 100.5685172 | 3347939328 |
| Target3 | PASS | 42.3856978 | 3349114880 |
| Full root | PASS, first invocation | 25.7633655 | 2797801472 |
| Fresh input check | PASS, first invocation | 82.378348 | 3248005120 |
| Whole-library audit | PASS, first invocation | 33.3595419 | 3349336064 |

Total target178.7601425s. All3 target slots consumed; no target replay.
Each target cap600s, cumulative1200s; root1200s, input/audit180s;
all memory caps8192MB. No internal or outer resource stop occurred.
The input observation handle expired after completion; its saved terminal
result was read, without rerunning the check.

Both failures were caused by the identity control's omitted explicit ideal
argument to `Ideal.map_id`. The final repair uses `(I : Ideal R).map_id`.
All11 public theorem statement texts,3definitions and main field proof
blocks are identical across attempts. Exact repair scope is checked by the
saved verifier. Failed controls depended on `sorryAx` and were rejected by
the namespace audit; those attempts are not accepted proofs.

Namespace20logical/17theorems/3runtime auxiliaries. Whole library:
5165logical/4384theorems/16999runtime auxiliaries. Every logical dependency
uses only `propext`, `Classical.choice`, `Quot.sound`.
Fresh closures: generic equality29583; final arbitrary-field bound60577.
They exclude the same34old h1/cutoff/classification/finite-answer roots,
PLUS `classNumber_one_of_field_equiv` (35total). This rules out using the
old PID-based convenience helper in the new generic equality.
Structural coverage:187project modules reachable, no source escapes;
all250interval endpoint identities unchanged. This is an endpoint identity
check, not a replay of the Arb campaign or old negative-control suite.

## Reproduce the saved-evidence verification

```sh
python research/ender_radius_bridge/verify_phase88_results.py
```

This command checks hashes, snapshots, exact repairs, caps, transcripts,
35exclusions,1447frozen prior files and61README lines. It does not rerun Lean.
[Manifest](PHASE88_RESULTS.json) and [37raw files](PHASE88_RAW.zip) preserve
all six invocations and the structural check. The registered runner gives
the exact executed Lean commands. Its target budget is exhausted: do not
invoke another Phase88 target under this registration.

Production diff: one148-line module and one root import. Prior production
proofs, tools, pins, certificates, CI gates, review records, ledgers,
preregistrations and negative results remain frozen. Current reader
pointers are updated separately from those historical records.

## Boundaries

The even-discriminant h<=2 branch remains open. The class-number-one field
cutoff remains50billion. No full classification, optimality, novelty or
Mathlib acceptance is asserted. These are pinned LOCAL checks, not new
external exact-head CI. Independent human semantic review remains open.
Argon's announced review is still underway; no report has been assessed.
Nothing was published or merged by this session, and no reviewer agent was
started. A remote refresh found main at39e9ce3, containing merges of
PR30-34; no review-folder changes since21c7b78. No Argon report was found.
These older merges do not validate the current Phase88 head.
