# Phase100: the actual even weighted bridge joins the main library

`EvenSplitPrimeBudget.actual_gram_budget` is now imported by the main root.
For positive squarefree d=1 or 2 modulo 4, actual even-field class number
at most two and the existing radius/odd-prime guards, it proves

    mass(P,R,S) <= log(product of original Gram diagonal entries)
      + lossScale(R,S)*kernelCost(L,primeKernel,countBound d)
      + R*S*(S-1)*log(d).

The count and local divisibility are derived. Actual field discriminant
4*d remains in the count; the original Gram retains radicand d, ordinary
derivatives and its normalization. [Human explanation](EVEN_WEIGHTED_BRIDGE_GUIDE.md).

## Exact accepted proof, new library checks

The Phase99 definition, all seven public theorem statements and proof
bodies, five controls and reports are exact after dependency imports.
The input checker moves to a separate file; one root import is appended.
There was no mathematical repair or retry, and no standalone99 replay.
One inherited blank EOF line at EvenSplitPrimeBudget.lean:81 is preserved
for exact transport; the saved verifier checks that precise exception.

[Protocol](PHASE100_PROTOCOL.md) and [runner](run_phase100.ps1) registered at
`0a5b22338ed9d9a37952bd41ec0945030ed1c1ea` before source/execution.
Base: `c25cec8ca067f8a97d704ed5a12f3f31ea1d0c25`.
Source SHA256: `aa2192a4c1a4bae12bca4c81f1966a4662218843fcebfa61b7c6de3bdbcbacae`.
Live pins rechecked: Lean 4.19.0; Mathlib
`c44e0c8ee63ca166450922a373c7409c5d26b00b`.

| Invocation | Result | Seconds | Peak observed process working set, bytes |
| --- | --- | --- | --- |
| Module | PASS, first | 47.9793447 | 3245162496 |
| Full library | PASS, first | 26.663038 | 2796179456 |
| Fresh input check | PASS, first | 66.3630844 | 3172495360 |
| Whole-library audit | PASS, first | 69.5947086 | 3357442048 |

Caps: module600s, root1200s, input/audit180s; 8192MB per owned process.
No internal or outer resource stop. Namespace:11 logical declarations,
10 theorems including generated definition proof auxiliaries, no runtime
auxiliaries. Whole library:5,264 logical declarations,4,475 theorems,
17,004 runtime auxiliaries. Only propext, Classical.choice, Quot.sound.
Fresh final closure:57,514 declarations, excluding the same52older inputs.
Both main statements and axiom sets were printed. All five inherited
controls remain checked. Structural coverage:193 modules, no source
escapes. All250endpoint identities unchanged; no Arb inequality replay,
old numerical campaign or inherited negative-control-suite rerun.

## Saved verification and commands

```sh
python research/ender_radius_bridge/verify_phase100_results.py
```

The verifier checks exact99transfer, definition/controls/reports, one root
import, exclusions/axioms/caps/snapshots, [25 raw records](PHASE100_RAW.zip),
[manifest](PHASE100_RESULTS.json) and1,544frozen prior files. It does not
execute Lean. The exact executed commands, from lean/, were:

```sh
lake build TenthDiscriminant.EvenSplitPrimeBudget
lake build
lake env lean -j 1 ../research/ender_radius_bridge/Phase100InputCheck.lean
lake env lean -j 1 Audit.lean
```

Structural checking imports audit.py's coverage/source scanner without
running its main routine, then executes `python lean/verify_sources.py`.
Historical root-fixed verifiers stay at their accepted refs, unchanged.
The first saved-verifier execution rejected its own mistyped8193MB
expectation; that was corrected to the registered/enforced8192MB. The
README assertion was also corrected during preparation to retain61lines.
No source, runner, result or raw transcript changed; no Lean run repeated.

## Remaining mathematics

Actual M(K) must be normalized and the positive weighted operator bounded
in closed form before the final original-Gram even-field contradiction.
These remain open. No candidate scalar envelope is a premise. No new
cutoff, full classification, novelty, optimality, external exact-head CI
or independent human review is claimed. All earlier failures/stopped
attempts remain frozen. A fresh repository check found no Argon report;
its review remains pending until received and pinned to a covered version.
