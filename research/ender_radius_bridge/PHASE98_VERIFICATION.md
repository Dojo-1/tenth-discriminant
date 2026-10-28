# Phase98: the actual even prime count joins the main library

The proof counts the same selected points in two ways: four per eligible
prime, and then class by class inside norm ellipses. This yields

    card(P) <= h(K)/4*(A+B+1) <= (A+B+1)/2,
    A = 2*pi*t/sqrt(4*d),
    B = 4*sqrt(actual M(K)*t/(4*d)).

Here d is positive and squarefree, d=1 or 2 modulo 4, K is the actual even
quadratic field, and h(K)<=2. Its actual field discriminant is 4*d.
P is any finite set of admissible primes bounded by t. The caller supplies
no family, cardinality identity or slice estimate. [Human proof](EVEN_CLASS_SUM_GUIDE.md).

## What changed

The six accepted theorem statements and proof bodies, four controls and
reports from Phase97 are exact after dependency imports. The standalone
input-checking command moves into its own file; one root import is added.
No mathematical repair or retry occurred. A single inherited blank EOF
line at EvenClassAggregation.lean:114 is retained for exact transfer;
the saved verifier checks this precise whitespace exception.

[Protocol](PHASE98_PROTOCOL.md) and [runner](run_phase98.ps1) were registered
at `80565f28159266a4e43e099051f1969ee471517d` before source or execution.
Base: `507c6d8f91c78c682b6869550003d95c5c24cc6d`.
Source SHA256: `6a151e12cd261caef8f5cc2a59de9ef16617a1c13c0cc1dd9e8df461bb9f636f`.
Live pins rechecked: Lean 4.19.0 and Mathlib
`c44e0c8ee63ca166450922a373c7409c5d26b00b`.

## Executed verification

| Invocation | Result | Seconds | Peak observed process working set, bytes |
| --- | --- | --- | --- |
| Module | PASS, first | 91.3810459 | 3246366720 |
| Full library | PASS, first | 29.1131802 | 2798051328 |
| Input check | PASS, first | 35.1269046 | 3147747328 |
| Whole-library audit | PASS, first | 33.234779 | 3358449664 |

Caps were 600 seconds for the module, 1,200 for the full library and
180 each for input and audit, with an 8,192 MB guard per owned process.
No resource stop occurred. The interrupted module result was recovered
from its terminal record; the build was not restarted.

Namespace: six logical declarations, six theorems, no runtime auxiliaries.
Whole library: 5,253 logical declarations, 4,465 theorems and 17,004 runtime
auxiliaries. Only `propext`, `Classical.choice`, `Quot.sound` are admitted.
The fresh 54,805-declaration closure excludes the same 49 older inputs,
including both odd-field prefix bounds. Both public bound statements and
axiom sets were printed. All four inherited controls remain checked.
Structural coverage reaches 192 modules with no source escapes; all 250
endpoint identities are unchanged. This does not replay Arb inequalities
or the inherited numerical/negative-control campaigns.

## Recheck the saved record

```sh
python research/ender_radius_bridge/verify_phase98_results.py
```

This verifies exact transport, imports, exclusions, invocation caps and
snapshots, [25 archived raw files](PHASE98_RAW.zip), the
[manifest](PHASE98_RESULTS.json) and 1,528 frozen prior files. It does not
execute Lean. The registered runner records the exact executed commands:
`lake build TenthDiscriminant.EvenClassAggregation`, `lake build`,
`lake env lean -j 1 ../research/ender_radius_bridge/Phase98InputCheck.lean`
and `lake env lean -j 1 Audit.lean`, all from `lean/`.
Structural verification imports the coverage/source scanner from `audit.py`
without invoking its main routine, then runs `python lean/verify_sources.py`.
No standalone Phase97 replay or historical verifier weakening occurred.

## The next bridge

The count must now be fed through the positive weighted summation used
for the original determinant. The actual M(K) must be normalized, with
radicand d kept distinct from actual discriminant 4*d. Only then can the
same positive integer Gram receive the final opposing estimates.

No even cutoff, improved constant, full classification, exact-head
external CI or independent human review is claimed. Argon's review is
pending until received and tied to a version. Prior failures and stopped
attempts remain preserved; no numerical candidate becomes a premise.
