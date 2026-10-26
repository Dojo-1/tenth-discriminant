# One complete numerical bridge, not a global cutoff

The conceptual argument is short. If the quadratic field has class number
one, the **same positive integer determinant** must satisfy two incompatible
bounds. Arithmetic forces it to be large; geometry bounds it from above.
We need a strict numerical gap, not a large matrix computation.

## One fixed interval, not a global cutoff

Phases 25–26 concern only `700000000000 ≤ D ≤ 875000000000`, with `D` squarefree
and `D ≡ 3 (mod 4)`. The fixed choices are
`R=175000000000`, `S=8750000000`, `P=10000`, radius `408406701`, and vertical
padding `488`. These are the first saved Ender interval's choices, not the
outcome of a new parameter search.

The checked numerical certificate is deliberately coarse:

    arithmetic lower bound ≥ 581 × 10^31
    geometric upper bound ≤ 572 × 10^31.

Class number one would force the arithmetic lower bound to be at most the
geometric upper bound, for the **same** positive integer Gram determinant.
The displayed inequalities would then imply `581≤572`. This is the whole
contradiction. No matrix of size `R*S` is computed.

`FirstIntervalGuards.lean` supplies the radius, padding and arithmetic guards;
`FirstIntervalScalars.lean` reduces the gap to two finite prime-table budgets;
`FirstIntervalConclusion.lean` composes them with the class-number argument.
`FirstIntervalRows.lean` proves all 1,229 row certificates;
`FirstIntervalCoverage.lean` accounts for every prime through 10000, without
omissions or duplicates; `FirstIntervalTotals.lean` proves both budgets.

The short final theorem is in
[FirstIntervalChecked.lean](../../lean/TenthDiscriminant/FirstIntervalChecked.lean):
`TenthDiscriminant.FirstCertificate.first_interval_classNumber_ne_one`.
It excludes class number one for the actual constructed quadratic field
under precisely the squarefree, congruence and interval hypotheses above.
**There is no remaining numerical premise. There is no global cutoff or
full class-number classification here.**

## Why the certificate is understandable

There are only three kinds of arithmetic to inspect.

1. **Logarithms.** Write `x=2^k t` with `1≤t<2`, and set
   `z=(t−1)/(t+1)`. Then
   `log t = 2(z+z^3/3+z^5/5+…)`.
   Eight terms give a lower bound. A geometric-series remainder gives an
   upper bound. Thus every log lies between two rational numbers. The
   integer `45045` merely clears the odd denominators `1,3,…,15`.

2. **Floor sums.** For each contributing prime power `q`, supply integers
   `k,m,A`. Check `R=qk+m`, `0≤m<q`, and
   `2A+qk=qk²+2km`. These equations prove that `A=Σ_{r<R} floor(r/q)`.
   A prime-power list may stop only once `q≥R`, when every later sum is zero.
   The producer's division algorithm need not be trusted.

3. **Finite sums.** Include every prime at most `10000`, exactly once.
   Sum the certified contributions and compare the resulting integers with
   the two declared budgets. Omitting an inconvenient prime is not allowed.

For coverage, each integer is first proved prime or nonprime using ordinary
proof-producing arithmetic. Those proofs evaluate lists of at most 16
consecutive integers. Exact range identities join the windows, then join the
39 row chunks to the complete range `0,…,10000`. Both totals are proved on
the same 32-row chunks and then added symbolically. The generator supplies
claims, not truth: every emitted proof must be accepted by Lean.

The determinant never changes between its arithmetic and geometric views.
That is the local-to-global bridge: many separately checked prime factors
constrain one global integer, whose real size is independently controlled.
No extra hypercomplex structure is required for this step.

## A useful inequality, and a necessary distinction

The staircase identity for `Σ_{t<S} min(k,t)` needs a range guard. Its
polynomial expression remains a **lower bound** even beyond that range.
Phase 25 checks this weaker global inequality, which permits a simpler
conservative certificate without falsely extending the identity.
For `k≥S`, the difference between the saturated staircase and that polynomial
is `(k−S)(k−S+1)/2≥0`. This explains why a conservative bound survives even
where the original exact identity no longer applies. No novelty is claimed.

## What the failures tell us

Earlier table proofs exhausted stack or memory. Their source layouts and
terminal records are preserved beside the protocol. These are failed
verification attempts, not mathematical counterexamples and not evidence
that a table passed. The repairs keep all inputs, bounds and obligations;
they change only how exact arithmetic is presented to the kernel.

The accepted row-only proof takes about 26 seconds in the recorded local
run. That is not the runtime of a complete interval proof. Earlier large
folds and coverage proofs hit resource limits; their failed layouts are kept
outside the audited library. Phase 26's complete coverage proof passed in
95.0764805 seconds under the recorded 8-GB cap. Its successful repair changes
proof representation, not numerical parameters or the required conclusion.

To check the accepted core, run from `lean/`:

```text
lake build
python verify_sources.py
python audit.py
python negative_controls.py
```

`verify_sources.py` checks the recorded source digest and interval endpoints,
not the truth of Arb inequalities. The audit visits every logical project
constant, sharing only the already-inspected dependency graph between roots.
Its cumulative axiom log is not a per-theorem dependency attribution.

There are still 249 other saved intervals, the unbounded range,
even-discriminant cases and the finite classification to connect. The saved
Arb campaign is not automatically certified by proving this one interval.
One closed interval is real progress, not a full class-number proof.
