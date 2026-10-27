# Phase87: integrated odd-chart class-number bound

The accepted86theorem is now in `TenthDiscriminant.UniformTwoClass` and
reachable from the main Lean root. Every squarefree D=3mod4 with D>=2^50
has actual class number>2 in the field chart. [Human proof](ODD_TWO_CLASS_BOUND_GUIDE.md).
The separate class-number-one field cutoff stays50billion.

Basebcdeb97cdb6b09bfebf5438e21b60de77afcc7f5.
Registration05b89a331e28015272439f26efd48f8419862676 before source/execution.
The complete accepted86mathematical/control/reporting prefix is exact,
except replacement of its root import by OddMinkowski+FiftyBillionCutoff.
The final standalone dependency command is relocated to fresh87input.
One module and one root import are the only production mathematical diff.
No theorem statement, proof body, definition, bound, control or report changed.
No standalone86invocation was replayed; its three slots remain consumed.

| Check from lean/ | Result | Seconds |
|---|---|---:|
| `lake build TenthDiscriminant.UniformTwoClass` | PASS, first invocation |43.0412347|
| `lake build` | PASS, once |23.9453069|
| `lake env lean -j 1 ../research/ender_radius_bridge/Phase87InputCheck.lean` | PASS, once |30.1005506|
| `lake env lean -j 1 Audit.lean` | PASS, once |32.420875|

Target/root caps600/1200seconds; input/audit180seconds; all8192MB.
No resource stop or import/interface repair occurred in any check.
The integrated namespace checks42logical declarations/40theorems, with3runtime
auxiliaries excluded. The whole-library audit checks5145logical declarations/
4367theorems;16996runtime auxiliaries are reported separately. Fresh root closure59,721excludes the SAME34named oldh1,
cutoff/classification/finite-answer inputs. Root axioms exactly propext,
Classical.choice, Quot.sound; the numerical85output is not a premise.

Structural coverage186project modules, no source escapes. All250endpoint
pairs match the existing recurrence. Endpoint identity is not a rerun of
Arb inequalities or the earlier numerical/regression campaigns.

Pinned Lean4.19.0 / Mathlib c44e0c8ee63ca166450922a373c7409c5d26b00b unchanged.
[Production source](../../lean/TenthDiscriminant/UniformTwoClass.lean),
[protocol](PHASE87_PROTOCOL.md), [manifest](PHASE87_RESULTS.json),
[25-file archive](PHASE87_RAW.zip). Saved verification from the root:

```sh
python research/ender_radius_bridge/verify_phase87_results.py
```

This does not rerun Lean. Prior stopped/failed attempts, source snapshots,
protocols and verifiers are frozen, including the86FAIL/FAIL/PASS campaign,
85negative samples/missing memory sample and82cap discrepancy. Historical
root-fixed verifiers remain unchanged at their accepted refs; they were
not weakened or replayed on the new root.

External exact-head CI and independent human review are not established
for this addition. Even-chart/arbitrary-field transport, full classification,
optimality and novelty are not claimed. No publication or merge occurred.

Reader checks: all 423 local links in the seven updated reader documents
resolve; README remains 61 lines. Changed-file whitespace checks pass.
The manifest freezes 1439 prior files, including review/, ledger/, the
original objective audit/history and attribution snapshot.
