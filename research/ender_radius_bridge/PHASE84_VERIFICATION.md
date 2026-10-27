# Phase84: actual odd-field Minkowski term and integrated closed budget

The target proves `OddMinkowski.actual_minkowski`: for squarefree D=3mod4,
actual ClassFiber.normBound K=(2/pi)*sqrt(D). It proves no real embedding,
one complex place, then uses the EXISTING maximal-integral-basis discriminant
identity. It transports the closed kernel and original-Gram budget to an
explicit function of D and L. [Human proof](ODD_MINKOWSKI_GUIDE.md).

Base: `2ee03a6f63998b5eb4e97387c62053da448e4cd1`.
Registration: `0bc6f9a1a46f384afea1504d057538b29924264e` before source/execution.
Accepted83 mathematics/reporting is preserved exactly, except its first
import and relocation of the final standalone dependency-check command.
It is now integrated as ClosedKernel; OddMinkowski and two root imports
are the only other production changes. The original83source stays unchanged.

## Target and repairs

| Target invocation | Exit | Seconds | Scope |
|---|---:|---:|---|
| First | 1 | 86.666025 | Root-polynomial rewrite failed; D3 field instance missing; small squarefree decision reductions stuck; namespace audit rejected dependent sorryAx. |
| Second | 0 | 48.909904 | All target statements, four controls, root axiom lists and namespace audits passed. |

Total135.575929seconds. Both600s/8192MB caps were respected; no internal or
outer resource stop. Repairs only expand the existing root evaluation
explicitly, open Polynomial notation, provide a local numeric Field Fact,
prove Squarefree3/7 via primality and reject Squarefree9 via3*3dividing9.
The ten intended public statement texts and chartCost definition are
unchanged; the D3 control did NOT elaborate on the first invocation, so
there was no checked first D3 signature. No theorem guard was weakened.
The accepted83math/control/report source was not repaired. No target rerun
after acceptance. Both raw attempts are preserved.

The new namespace checks17logical declarations/16theorems/0runtime-only;
transported ClosedKernel checks28/26/0. Allowed axioms are exactly
propext, Classical.choice, Quot.sound. Controls cover actual D3 and D7,
non-squarefree D9 and the zero mod4 guard.

## Integration checks

- `lake build`: first invocation PASS27.0026287seconds,1200s/8192MB cap.
- `lake env lean -j 1 ../research/ender_radius_bridge/Phase84InputCheck.lean`:
  first invocation PASS38.1729728seconds,180s/8192MB cap. Closures47,300
  (actualM) and57,669(normalizedGram) exclude the SAME34named olderh1,
  cutoff/classification/finite-answer roots. Both report standard3axioms.
- `lake env lean -j 1 Audit.lean`: first invocation PASS35.6841639seconds,
  180s/8192MB cap;5103logical declarations/4327theorems,16993runtime
  auxiliaries reported separately. Only the standard3axioms are admitted.
- Structural coverage:185project modules reachable; no source escapes.
  All250endpoint pairs match the existing Lean recurrence. This checks
  source identity, not new Arb inequalities or a numerical campaign.

Pins remain Lean4.19.0 and Mathlib c44e0c8ee63ca166450922a373c7409c5d26b00b.
[Manifest](PHASE84_RESULTS.json), [36-file raw archive](PHASE84_RAW.zip),
[protocol](PHASE84_PROTOCOL.md). From the root, saved-integrity verification:

```sh
python research/ender_radius_bridge/verify_phase84_results.py
```

This verifier does not execute Lean. Older82/83root-fixed verifiers remain
unchanged and historical at their accepted refs; they are not weakened or
rerun on the new root. Their sources, archived failures and manifests stay
frozen. The earlier82input-cap discrepancy remains explicitly preserved.

The odd-chart field-size substitution is closed. General field/even-chart
transport and a strict numerical cutoff are not supplied. External
exact-head CI and independent human review remain outstanding. The
class-number-one cutoff stays50billion; no classification/optimality claim.

Reader check: all408local links in the nine updated reader documents
resolve; README stays61lines. Changed-file whitespace check passes.
