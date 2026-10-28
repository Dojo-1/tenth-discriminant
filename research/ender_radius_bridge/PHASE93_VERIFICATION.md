# Phase93: actual even principal calibration and complete prime-axis count

The FULL registered standalone theorem is proved:
`EvenPrimeAxis.controlled_class_prime_count`.
For positive squarefree d=1or2mod4, actual h(K)<=2 and EVERY actual class C,
it chooses ONE bounded J in C, all class-ideal NormLifts and ONE basis/form
with0<a<=N(J),4ac-b²=4d and C=1=>a=1. The SAME choice serves ALL finite
prime-normalized norm-bounded U and thresholds, with NO off-axis premise:

    cardU<=2pi*t/sqrt(4d)+4sqrt(actualM(K)*t/(4d))+(ifC=1then0else2).

The axis charge is at most2across ALL primes in a fixed lattice, not2per
prime. Principal-class calibration to(1,0,d) needs only that particular
ideal's class=1, not global h1. [Human proof](EVEN_PRIME_AXIS_GUIDE.md).
No residue-map/multiplicity/class-sum/weighted-Gram/cutoff claim follows yet.

[Protocol](PHASE93_PROTOCOL.md) and [runner](run_phase93.ps1) registered at
`1931b42b851b36fc32d08a0498e805b1c8b605e8` before source/execution.
Base `11b475f5469adc9f83aeb8bc4a7127be771ec382`.
Lean4.19.0, Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b`.

| Invocation | Result | Seconds | Observed peak bytes |
| --- | --- | --- | --- |
| Target1 | FAIL: odd/even norm theorem name ambiguous | 121.6047918 | 3289759744 |
| Target2 | PASS | 77.3449178 | 3298643968 |

Total198.9497096s. Caps600s/8192MB each,1200s cumulative,max3targets.
No internal/outer resource stop or third invocation. Sole repair: qualify
`norm_in_integer_basis` as `EvenIdealCount.norm_in_integer_basis` in the
principal calibration proof. All11public theorem statement texts, main
class-count proof and5controls are byte-identical. No new definitions;
existing actual even FormData and generic PrimeNormalized are reused.
The failed proof depended on sorryAx; namespace/input audits rejected it.
That attempt is not accepted evidence, and its complete source/log remain.

Final source SHA256:
`c6add285b74a4101812acfd1f1f32a2843fd7ace8550ce999ea7f5e57c8397bc`.
Namespace13logical/13theorems/0runtime auxiliaries; only `propext`,
`Classical.choice`, `Quot.sound`. Fresh target closure54650excludes
same38old roots as92 PLUS four odd-field principal/axis/class-count roots
(42total). The generic NUMERIC ActualPrimeAxis.axis_prime_iff is reused;
no odd/even field isomorphism or odd-field class count is assumed.
Controls: Gaussian unit-ideal form(1,0,1), uncalibrateda3axis+-1,
a1cannot representprime onaxis, zero notPrimeNormalized, coordinate negation.

## Check the saved evidence

```sh
python research/ender_radius_bridge/verify_phase93_results.py
```

PASS. Exact qualification repair,11types/mainproof/5controls,no newdefs,
caps/logs/snapshots,42exclusions, [8rawfiles](PHASE93_RAW.zip),
[manifest](PHASE93_RESULTS.json),1490frozen prior files and README61lines.
It does not execute Lean. Exact executed command from lean/:
`lake env lean -j 1 ../research/ender_radius_bridge/Phase93EvenPrimeAxis.lean`.
No additional Lean invocation outside the bounded attempts.

Standalone research only. All production/root/tools/pins/certificates/CI
and prior failures/reviews/ledgers/protocols/raw/verifiers remain unchanged.
The92whole-library audit is historical, not a new93root build/audit.
No external exact-head CI or independent human review is claimed. A remote
refresh finds main still39e9ce34d09ed9f990fab4b9ed5e3980cee64119 and no new
review-folder changes; Argon's announced report is not received/assessed.
No reviewer agent started, publication or merge performed.

## Remaining assembly

Choose a coherent class-indexed family, construct actual even residue maps
with distinct kernels, supply four labelled prime lifts on THAT family,
then class summation/weighted loss/actualM normalization/same-original-Gram
comparison. Field discriminant4d and Gram parameterd need explicit matching.
No even cutoff, full classification, optimality, novelty or upstream
acceptance is asserted. Existing h1field50billion and odd actual-field
h<=2bound2^50 are unchanged. Integration of this standalone source remains.
