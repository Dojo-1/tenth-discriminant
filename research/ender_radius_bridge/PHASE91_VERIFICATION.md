# Phase91: one controlled actual even lattice per ideal class

The FULL registered standalone target is proved:
`EvenControlledClass.controlled_class_form_and_count`.
For every positive squarefree d=1or2mod4, actual class number<=2 and actual
class C, it produces ONE J in C with N(J)<=actual M(K), exact NormLift
for EVERY I in C, and ONE actual basis/integral norm form with
0<a<=N(J),4ac-b²=4d and exact norm=N(J)*form for ALL coordinates.
That SAME basis supplies the common off-axis count for EVERY finite
norm-bounded U and threshold t, with coefficient replaced by actual M(K).
No representative, small vector, primitive basis, form, lift or count is
supplied by the caller. [Human proof](EVEN_CONTROLLED_CLASS_GUIDE.md).

[Protocol](PHASE91_PROTOCOL.md) and [runner](run_phase91.ps1) registered at
`48c309f61ca67e200066f15e16b318b8be32b8cd` before source/execution.
Base `e95f8389229bde7e656e8fb253ce73cbfc29957b`.
Lean4.19.0, Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b`.

| Invocation | Result | Seconds | Observed peak bytes |
| --- | --- | --- | --- |
| Target1 | FAIL: local equality shadowed modulo hypothesis | 83.4366943 | 3302285312 |
| Target2 | PASS | 106.49821 | 3298709504 |

Total189.9349043s. Caps600s/8192MB each,1200s cumulative,max3invocations.
No internal/outer resource stop, third target invocation or old campaign
replay. The sole repair renames a local coordinate equality hm to hmul
in primitive_of_minimal (its binder and two uses). This restores access
to the unchanged modulo-four hypothesis hm. All11public theorem statement
texts, the FormData definition, main theorem and four controls remain
byte-identical. The failed proof depended on sorryAx and both namespace
and input audits rejected it; that attempt is not accepted evidence.

Final source SHA256:
`9ba9359fa9fa1a2038d537379859b441920c91ccaf7fd99ec995d493d0fb8cc5`.
Namespace17logical/16theorem/0runtime auxiliaries; only `propext`,
`Classical.choice`, `Quot.sound`. Fresh target closure54590excludes
same37older roots as90 PLUS the odd controlled-class form/count theorem
(38total). The generic finitegroup self_inverse and determinant-one
primitive_completion are reused directly; no odd/even field isomorphism.
The four controls check zero/negative scalar norms, nonprimitive(4,6)
and primitivity of1 in EVERY actual Gaussian unit-ideal basis.

## Check the saved evidence

```sh
python research/ender_radius_bridge/verify_phase91_results.py
```

PASS. Exact local-variable rename,11types/FormData/mainproof/controls,
caps/logs/snapshots,38exclusions, [8rawfiles](PHASE91_RAW.zip),
[manifest](PHASE91_RESULTS.json),1474frozen prior files and README61lines
are checked. It does not execute Lean. Exact executed command:
`lake env lean -j 1 ../research/ender_radius_bridge/Phase91EvenControlledClass.lean`
from lean/. No additional Lean invocation outside the bounded attempts.

This is standalone research, outside the productionroot. All production
source/root, numerical tools, pins, certificates, CI gates, prior stopped
attempts/reviews/ledgers/protocols/raw/verifiers remain unchanged. The
whole-library audit at90is historical evidence, not a new91root audit.
No external exact-head CI or completed independent human review is claimed.
Argon's review is still underway; no report is received/assessed.
No reviewer agent started, publication or merge performed.

## Remaining mathematical work

The next assembly needs full axis counts and principal calibration,
distinct prime lifts on a common class-indexed family, the class sum,
weighted loss, actualM normalization and comparison on the SAME original
positive integer Gram. The actual field discriminant4d and Gram radicand
d must be matched explicitly. This statement alone supplies no full prime
count, weighted-Gram estimate, even cutoff or classification. The odd
actual-field h<=2bound2^50 and h1field50billion bound are unchanged.
No optimality, novelty or Mathlib acceptance is claimed.
