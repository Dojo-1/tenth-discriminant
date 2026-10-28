# Phase102: actual even normalization joins the main library

`EvenMinkowski.scalar_actual_gram_budget` is now imported by the main root.
It derives actual M(K)=4*sqrt(d)/pi, closes the finite count-kernel cost,
composes it into the full weighted budget on the original ellipse Gram,
and dominates the cost by the previously used scalar formula. Positive
squarefree d=1or2mod4, actual class number<=2 and the existing radius/
odd-prime guards remain explicit. Actual field discriminant4*d and Gram
radicandd remain distinct. [Human reconstruction](EVEN_NORMALIZATION_GUIDE.md).

## Exact accepted mathematics

Accepted101body is exact after three dependency imports: all16public
statements and proof bodies, two definitions, four controls and reports,
including the accepted final simp. The standalone input checker moves to
its own file; one root import is appended. No mathematical repair or
retry occurred. The original failed101source/result and sole proof
repair remain frozen; there was no standalone101replay. An inherited
blank EOFline at EvenMinkowski.lean:211 is retained for exact transport;
the verifier checks that precise whitespace exception.

[Protocol](PHASE102_PROTOCOL.md) and [runner](run_phase102.ps1) registered at
`c181e2d45a34b7bae9ba1e14702f8cf945e6cbdd` before source/execution.
Base: `0bc0b9156912e17fa7fdee2dd0f4b55aa62380f1`.
Source SHA256:
`c2d2c46e880856733fb3db23779c055eca756b015f4da0f4dd7508538732410c`.
Live pins rechecked: Lean4.19.0; Mathlib
`c44e0c8ee63ca166450922a373c7409c5d26b00b`.

## Executed checks

| Invocation | Result | Seconds | Peak observed process working set, bytes |
| --- | --- | --- | --- |
| Module | PASS, first | 84.6782799 | 3317235712 |
| Full library | PASS, first | 28.3455345 | 2793865216 |
| Fresh input check | PASS, first | 32.735253 | 3176296448 |
| Whole-library audit | PASS, first | 28.823217 | 3355803648 |

Caps: module600s,root1200s,input/audit180s,8192MB per owned process.
No internal/outer resource stop. Namespace23logical declarations,
21theorems including generated auxiliaries, no runtime auxiliaries.
Whole library5,287logical declarations,4,496theorems,17,004runtime
auxiliaries. Only propext,Classical.choice,Quot.sound. Fresh final
closure57,646declarations excludes the same58older inputs, including
odd-field normalization/count/budget and whole cutoff results. ActualM
and both full budgets have printed types/axiom lists. All four controls
are unchanged and checked. Structural194modules/no source escapes;
all250endpoint identities unchanged. No Arb inequalities, old numerical
campaign or inherited negative-control-suite replay occurred.

## Recheck the saved integration

```sh
python research/ender_radius_bridge/verify_phase102_results.py
```

The saved verifier checks exact101transport, definitions/types/controls/
reports, one root import, exclusions/axioms/caps/commands/snapshots,
[25raw records](PHASE102_RAW.zip), [manifest](PHASE102_RESULTS.json) and
1,558frozen prior files. It does not execute Lean. Actual commands from lean/:

```sh
lake build TenthDiscriminant.EvenMinkowski
lake build
lake env lean -j 1 ../research/ender_radius_bridge/Phase102InputCheck.lean
lake env lean -j 1 Audit.lean
```

Structural checking imports audit.py's coverage/source scanner without
calling its main routine, then runs `python lean/verify_sources.py`.
Historical root-fixed verifiers remain at accepted refs; none was weakened
or replayed on the changed root. Prior production/tools/pins/CI/
certificates/protocols/raw/verifiers/reviews/ledgers and failures are
unchanged except the one root import and authorized current reader updates.

## Next mathematical target

Combine the integrated scalar budget with the all-range estimates on the
same Gram, then transport the even result to arbitrary actual fields.
Neither step is claimed here. No new cutoff, full classification, novelty,
optimality, external exact-head CI or independent human review is claimed.
No numerical candidate becomes a premise. A fresh repository check found
no Argon report; its review remains pending until received/versionpinned.
