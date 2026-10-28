# Phase103: full all-range actual even-chart two-class cutoff

The standalone theorem proves, for positive squarefree d=1or2mod4,

    d>=2^50 -> 2<classNumber(EvenQuadraticField d).

The two consequences are canonical radicand<2^50 and actual absolute
field discriminant<4*2^50=2^52 under actual class number<=2. No generator,
isomorphism, counting/M(K)/scalar bound or finite certificate is supplied.
The same actual original Gram carries both inequalities. The new result
is for the canonical actual even chart; arbitrary-field transport is not
claimed. [Human contradiction](EVEN_TWO_CLASS_BOUND_GUIDE.md).

## Registration and both sources

[Protocol](PHASE103_PROTOCOL.md) and [runner](run_phase103.ps1) registered at
`3bf1c54702579162639a90ee8cfda3d370894a9f` before source/run.
Base:`0239e1314e16a5c467cc7f202ea104db01f5aaf8`.
First failed source SHA256:
`6d59489516a853a944471e56c630755155db3e0a46f1c7dd8515d7e462966f3e`.
Final source SHA256:
`476ef6f7784ae5ca838d7e6f162c842a605b2880222f697a7ab48ce3447fcfa7`.

| Attempt | Result | Seconds | Peak observed process working set, bytes |
| --- | --- | --- | --- |
| 1 | FAIL, discriminant wrapper | 86.8947538 | 3345928192 |
| 2 | PASS, full target | 83.9126192 | 3353485312 |

Exact decimal sum170.807373s; native floating arithmetic/transcripts are
retained unchanged. Each invocation capped at600s/8192MB per owned process,
within1200s cumulative. No resource stop, extra probe, weaker target or
limit increase. The exact command, from lean/, was:

```sh
lake env lean -j 1 ../research/ender_radius_bridge/Phase103EvenTwoClass.lean
```

The first run checked the main contradiction and radicand bound, including
standard axioms and fresh main closure. Its discriminant wrapper left
`(4 * (D : Int)).natAbs = 4 * D` unsolved. The namespace/second closure
audits correctly rejected sorryAx from that incomplete wrapper. The sole
repair adds Int.natAbs_mul to its simp call. The full contradiction proof,
all seven public theorem types, four controls and every other proof are
unchanged. The second full invocation passes; neither partial first-run
success nor failed wrapper is relabelled as full acceptance.

## The actual proof and checks

The integrated even scalar budget supplies the original-Gram upper/loss
side. Existing field-independent radius/dimension/padded-count/diagonal
and exact prime-mass lower theorems, plus the all-range scalar estimates,
produce a positive contradiction for EVERY d>=2^50. The whole old
odd-field cutoff, h1cutoffs, old odd-field counting/normalization and
finite-answer roots are excluded (same58as102). No Phase85numerical test
or candidate envelope supplies a premise. Pure real scalarCost and
OddMinkowski.chartCost are definitionally the same formula; using its
numerical estimate is not replacing the actual even field by an odd field.

Final namespace20logical declarations/20theorems including generated
auxiliaries; no new definitions or runtime auxiliaries. Only propext,
Classical.choice,Quot.sound. All seven public types and three main axiom
lists are printed. Fresh closures:59,697for even_classNumber_gt_two and
59,701for even_discriminant_bound; both exclude58older roots. Controls
check exact2^50/4*2^50 endpoints, reject omission of factor4 and the wrong
mod4chart, and prove exact positive margin1789605/100000000.

```sh
python research/ender_radius_bridge/verify_phase103_results.py
```

The saved verifier checks both attempts, fixed seven types/no definitions/
four controls, unchanged main proof, exact wrapper-only repair, caps/
commands/axioms/bothclosures/58exclusions, [eight raw files](PHASE103_RAW.zip),
[manifest](PHASE103_RESULTS.json) and1,567frozen prior files. It does not
execute Lean. Production/root/tools/pins/CI/certificates/prior protocols/
raw/verifiers/reviews/ledgers and failed/stopped attempts are unchanged.
No new root build, whole-library audit or numerical campaign was run;
Phase102 remains the separate current production-check record. Historical
root-fixed verifiers remain at accepted refs without weakening or replay.

Integration, arbitrary-field transport, new external exact-head CI and
independent human review remain open. The separate class-number-one
field cutoff stays50billion. No full classification, novelty or optimality
is claimed. Argon review remains pending until received/versionpinned.
