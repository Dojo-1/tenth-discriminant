# Phase79: full actual per-class prime count, including the axis

Registered70a06a4 before source/execution on19fb5f1. The scalar
axis_prime_iff proof is byte-for-byte transported from accepted62 into a
new namespace, without executing its old campaign. Production78 and
stopped69/75 source/raw/results/verifiers remain unchanged.

`ActualPrimeAxis.actual_axis_card_le_two` bounds actual elements of J
with prime normalized norm and second coordinate0 by2, across ALL primes.
It derives a*x^2=p from actual norm positivity and positive ideal-norm
cancellation; integer prime factorization gives x=+-1,a=p; injective
actual coordinates turn this into a finite cardinal bound.

`controlled_class_prime_count` chooses one bounded actual ideal J and
controlled actual basis per class under h<=2 in the squarefree odd chart.
It retains lifting of every ideal of the class into that sameJ. For the
principal class it recalibrates thatJ's basis to a=1, removing all prime
axis points. For all finite U:J of prime-normalized norm<=N(J)*t, the
count is2*pi*t/sqrtD+4*sqrt(M(K)*t/D)+(if C=1 then0else2). There is NO
caller off-axis condition, supplied class family/basis/form/count bound.

Exactly two invocations from the repository root:

```powershell
& research/ender_radius_bridge/run_phase79.ps1 build
```

FAIL28.7491471seconds: extra closing delimiter in a declaration, and
missing classical decidability for C=1. PASS31.175862seconds: only the
delimiter and open scoped Classical context repaired. All intended
mathematical statements and all proof bodies/controls/reporting unchanged;
the first axis-card declaration had not parsed, so no claim that its
first printed signature was a checked theorem. Total59.9250091seconds.
No resource stop, limit increase, probe, production change or third run.

The final invocation prints8public types, complete FormData/PrimeNormalized,
two root axiom lists and namespace audit10logical/10theorem/0runtime,
standard three axioms only. Four controls cover a=3 at+-1, no a=1 prime
axis, actual zero not prime-normalized, and coordinate negation. The first
source/stdout/stderr/result and its sorryAx audit rejection are preserved
with the passing run in the8-file PHASE79_RAW.zip.

Saved-evidence verification, without executing Lean:

```powershell
python research/ender_radius_bridge/verify_phase79_results.py
```

It checks registration/runner, all source/result/raw hashes, exact62scalar
proof transport, the exact two textual repairs, final printed audits,
resource budgets and preserved78/69/75 records/production/README.
This establishes saved integrity, not independent human review or CI.

The result supplies actual per-class full prime counts, not the remaining
aggregation of four prime representatives across THIS chosen ideal family.
The earlier scalar2(h-1)<=h bookkeeping is separate from that actual bridge.
Aggregate B, even/field transport and a new range remain open. Standalone
source outside production CI. No publication/merge/reviewer/upstream/Tao post.
[Human proof](ACTUAL_PRIME_AXIS_GUIDE.md).
