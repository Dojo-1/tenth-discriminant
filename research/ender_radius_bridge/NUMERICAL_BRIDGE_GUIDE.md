# The last numerical bridge: what must actually be checked

The conceptual argument is short. If the quadratic field has class number
one, the **same positive integer determinant** must satisfy two incompatible
bounds. Arithmetic forces it to be large; geometry bounds it from above.
We need a strict numerical gap, not a large matrix computation.

## One fixed interval, not a global cutoff

Phase 25 concerns only `700000000000 ≤ D ≤ 875000000000`, with `D` squarefree
and `D ≡ 3 (mod 4)`. The fixed choices are
`R=175000000000`, `S=8750000000`, `P=10000`, radius `408406701`, and vertical
padding `488`. These are the first saved Ender interval's choices, not the
outcome of a new parameter search.

The desired numerical certificate is deliberately coarse:

    arithmetic lower bound ≥ 581 × 10^31
    geometric upper bound ≤ 572 × 10^31.

Since `581>572`, those inequalities would contradict class number one.
`FirstIntervalGuards.lean` supplies the radius, padding and arithmetic guards;
`FirstIntervalScalars.lean` reduces the gap to two finite prime-table budgets;
`FirstIntervalConclusion.lean` composes them with the class-number argument.
The generated table is not a proof until every row, completeness and both
budgets are checked by Lean. Every one of its 1,229 rows now passes in
`FirstIntervalRows.lean`. Completeness and the total budgets remain pending:
**no interval exclusion or global cutoff is claimed here.**

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

The determinant never changes between its arithmetic and geometric views.
That is the local-to-global bridge: many separately checked prime factors
constrain one global integer, whose real size is independently controlled.
No extra hypercomplex structure is required for this step.

## A useful inequality, and a necessary distinction

The staircase identity for `Σ_{t<S} min(k,t)` needs a range guard. Its
polynomial expression remains a **lower bound** even beyond that range.
Phase 25 checks this weaker global inequality, which permits a simpler
conservative certificate without falsely extending the identity.

## What the failures tell us

Earlier table proofs exhausted stack or memory. Their source layouts and
terminal records are preserved beside the protocol. These are failed
verification attempts, not mathematical counterexamples and not evidence
that a table passed. The repairs keep all inputs, bounds and obligations;
they change only how exact arithmetic is presented to the kernel.

The accepted row-only proof takes about 26 seconds in the recorded local
run. That is not the runtime of a complete interval proof. Large folds and
prime-coverage proofs still hit resource limits, including a normalized
coverage pilot; those failed attempts are kept outside the audited library.

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

Even success here would leave 249 other saved intervals, the unbounded
range, even-discriminant cases and the finite classification to connect.
One closed interval is real progress, not a full class-number proof.
