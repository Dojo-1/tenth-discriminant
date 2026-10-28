# Phase104: full actual even-chart cutoff joins the main library

For positive squarefree d=1or2mod4, actual even-field class number<=2
implies radicand<2^50 and actual absolute field discriminant<4*2^50=2^52.
Equivalently d>=2^50 forces actual h>2. The same original Gram supports
the arithmetic/geometric contradiction. [Human proof](EVEN_TWO_CLASS_BOUND_GUIDE.md).

## Exact accepted mathematics

All accepted103body is exact after dependency imports: seven public
theorem statements/proofs, four controls and reports, including the
Int.natAbs_mul wrapper repair. No new definitions or mathematical repair.
One root import and a relocated58-input checker with TWO fresh roots
integrate the result. No standalone103replay occurred; both original
attempts and their exact repair remain frozen. One inherited blank EOFline
at EvenTwoClass.lean:107 is preserved for exact body transfer; the saved
verifier checks that precise whitespace exception.

[Protocol](PHASE104_PROTOCOL.md) and [runner](run_phase104.ps1) registered at
`a16feb6b270c9bb82db7c00d0a04cd0925987aed` before source/run.
Base:`f42d2005f500c75332eff1d0a67b2d4d1044a7e0`.
Source SHA256:
`7956a2f1a51b1f5159d4d4810f3ffbbab146ef4e55bb0604d5cf88e1f28c5126`.
Live pins rechecked: Lean4.19.0; Mathlib
`c44e0c8ee63ca166450922a373c7409c5d26b00b`.

| Invocation | Result | Seconds | Peak observed process working set, bytes |
| --- | --- | --- | --- |
| Module | PASS, first | 84.820204 | 3347615744 |
| Full library | PASS, first | 20.2078022 | 2792529920 |
| Fresh two-root input check | PASS, first | 33.6182774 | 3242475520 |
| Whole-library audit | PASS, first | 24.6340176 | 3354210304 |

Caps: module600s/root1200s/input-audit180s,8192MB per owned process.
No resource stop or retry. Namespace20logical declarations/20theorems,
no runtime auxiliaries. Whole library5,307logical declarations/4,516theorems/
17,004runtime auxiliaries, with only propext,Classical.choice,Quot.sound.
Fresh closures59,697/59,701exclude the same58older inputs. Three main
statements/axiom lists are printed. All four controls are unchanged.
Structural195modules/no escapes;250endpoint identities unchanged. No
Arb inequality, old numerical campaign or negative-control-suite replay
is included in this local integration record.

```sh
python research/ender_radius_bridge/verify_phase104_results.py
```

The verifier checks exact103transfer, fixed statements/proofs/controls,
one root import, bothclosures/58exclusions/axioms/caps/commands/snapshots,
[25raw records](PHASE104_RAW.zip), [manifest](PHASE104_RESULTS.json) and
1,573frozen prior files. It does not execute Lean. Commands, from lean/:

```sh
lake build TenthDiscriminant.EvenTwoClass
lake build
lake env lean -j 1 ../research/ender_radius_bridge/Phase104InputCheck.lean
lake env lean -j 1 Audit.lean
```

Structural checking imports audit.py's coverage/source scanner without
calling its main routine, then runs `python lean/verify_sources.py`.
Historical root-fixed verifiers remain at accepted refs without weakening
or replay. Production/tools/pins/CI/certificates/prior proofs/protocols/
raw/verifiers/reviews/ledgers and failures are unchanged except one root
import and authorized current reader updates.

## Publication and remaining work

The user explicitly authorizes publication and merge after current-head
checks. [PR35's earlier merge](SOURCE_REFRESH_20261028.md) is verified, but
its CI does not validate this newer head. This local record precedes the
new publication. Its exact-head CI and merge receipt belong in that PR;
no new external success is asserted in advance. Existing pinned CI gates
remain unchanged, and any new failure must be preserved.

Arbitrary actual-field transport and requested BOTH coordinate/literal
2Dtranslation compatibility remain separate proof targets. The current
cutoff assumes no new shift law or blanket trace-Gram determinant
invariance. No full classification, optimality, novelty or independent
human review is claimed. Argon remains pending until received/versioned.
No Tao posting or new reviewer was requested or performed by this agent.
