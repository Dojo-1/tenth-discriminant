# R2 - Reorient the calculation, retain the evidence

**Implemented and locally tested methodology experiment. No new Lean theorem,
no new discriminant bound, no demonstrated geometric-policy advantage.**

Frozen main: `791ebf4815d8eb4be5da3b01527ca7f0877b6d0e`. This is additive and
independent of open PRs #9 and #10. Earlier negative granule results remain intact.
The matched primary comparison has four records per cache, not unlimited memory.

## What changed in the method

The unit of reuse is an exact transformation orbit, not a fuzzy resemblance or a
repeated byte string. A polynomial, its specialization, its fixed-size Sylvester
matrix and a checked scalar witness are views of the same object. Frame changes
carry their exact coefficient identity and a conventional determinant law.

The affine operator is an associative, noncommutative rational matrix action.
It is NOT a quaternion/octonion engine. The geometric ablation uses a fixed
three-dimensional Poincare-ball chart and the Euclidean metric on identical
coordinates. It does not train a hyperbolic embedding or establish that research
has a hyperbolic ontology. Slow context is a heuristic two-rate update, not a
physical or quantum adiabatic theorem. These distinctions prevent relabeling
ordinary certificate reuse as an unmeasured hypercomplex advantage.

## Exact transport law and scope

Let F lie in Q[W][Z], with exact Z-degree a >= 1. Define E_F(W) as the determinant
of the original derivative Sylvester coefficient matrix of size 2a-1. For

    T(F)(Z,W) = lambda F(u Z+h, v W+b),    lambda,u,v != 0,

we use the conventional identity

    E_T(F)(W) = lambda^(2a-1) u^(a*a) E_F(v W+b).

Thus a checked E_F(t)=d transports to the point (t-b)/v, with value
lambda^(2a-1) u^(a*a) d. This applies to zero values as well as nonzero values.
Seven zero observations remain seven zero observations, not a zero-polynomial
proof. An exact-zero leading coefficient and a tiny nonzero coefficient are
never identified. A degree-losing specialization does not shrink the matrix.

Derivation: work over Q(W). Translation/dilation on polynomials of degree <n
has upper-triangular coefficient matrix with diagonal 1,u,...,u^(n-1), hence
 determinant u^(n(n-1)/2). For N=2a-1 the output transformation contributes this
factor; the two input blocks contribute its inverses for n=a-1 and n=a.
Scaling F contributes lambda^N, and the chain rule contributes u^a in the second
block. The remaining exponent is

    N(N-1)/2 - (a-1)(a-2)/2 - a(a-1)/2 + a = a*a.

Parameter substitution W -> vW+b is a ring automorphism and commutes with the
fixed determinant. No additional v factor occurs because differentiation is in
Z. The identity over Q(W) descends to Q[W]. No claim of novelty is made.
**This derivation is not yet a new kernel-checked Lean transport theorem.**

`Frame.then` explicitly represents applying its left frame and then its argument.
Its affine offsets compose as h1+u1*h2 and b1+v1*b2. Scale and translation do not
commute. Tests exercise composition, inverses and noncommutation rather than
attaching hypercomplex terminology to an ordinary tuple.

## Exact recognition before reuse

For a polynomial of bidegree (a,b) with nonzero corner coefficient c_ab, the
canonicalizer divides by c_ab and translates by

    h = -c_(a-1,b)/(a*c_ab),
    k = -c_(a,b-1)/(b*c_ab)     (k=0 when b=0).

This gives the same representative under nonzero scalar multiplication and the
two translations. The source-to-input frame is retained and reconstructed
exactly at every reuse. Full affine dilation transport is implemented and tested,
but automatic recognition of arbitrary u/v dilations is NOT implemented.
Corner-unsupported objects keep their original identity; no approximate match
can be promoted to exact equivalence.

The admission gate recomputes each new source record using SymPy symbolic
differentiation, independently assembled coefficient columns and an exact matrix
determinant. Subsequent transport checks target identity, global degree, field
and derivative convention. `transport` is a CONDITIONAL low-level function:
its root record must first pass `admit`, as enforced in `Runner.run`. It is not a
standalone verifier for arbitrary unadmitted serialized claims. No signature,
security boundary against arbitrary Python execution, or Lean trust kernel is
claimed. Reference calculations and code paths differ, authorship does not.

## Fixed comparison and result

Protocol SHA256: `9f5f3c519fa13e1549393ea66cf43bff83d826ef9c96587f643461b88c355631`.
Two seeds, twelve base polynomials/seed, six transformed instances/base, and three
orders (blocked, shuffled, round-robin) produce 432 tasks per policy. Each seed
has 72 distinct raw inputs. Related tasks are intentionally reused; this is not
a held-out-family generalization experiment. No orbit IDs or generator frame
metadata are passed to a strategy. There is no learned distribution or training
budget hidden in this round.

| Policy | Production determinant calls | Admission determinant calls | Cache hits | Maximum records |
|---|---:|---:|---:|---:|
| No reuse | 1008 | 1008 | 0 | 0 |
| Raw-object LRU | 1008 | 1008 | 0 | 4 |
| Exact canonical LRU | 664 | 664 | 135 | 4 |
| Euclidean eviction | 658 | 658 | 144 | 4 |
| Hyperbolic eviction | 664 | 664 | 144 | 4 |
| Euclidean, slow context | 658 | 658 | 144 | 4 |
| Hyperbolic, slow context | 664 | 664 | 144 | 4 |
| Canonical, unbounded reference | 228 | 228 | 300 | 22 |

All policies produce 360 nonzero task answers and 72 unresolved answers. Every
returned evaluation is rechecked against the original symbolic resultant computed
BEFORE specialization; zero mismatches occurred. Root admission counts are shown
rather than hidden behind the reduction in production calls. At four records,
canonical reuse reduces both types of determinant call by 34.13% against raw LRU.
It is not a 34.13% measured wall-clock speedup.

None of the geometry/slow variants passes the registered >=10% call-reduction
and no-worse-stream gate against canonical LRU. Hyperbolic routing ties its total
but loses on both shuffled streams. Euclidean routing saves only six calls
(0.90%) in aggregate. More cache hits need not mean fewer determinant calls:
retaining a seven-zero record saves more probes than retaining a first-hit witness.
Slow updates change no outcomes in this corpus; frequent exact-degree resets and
constant features within an orbit make this a weak discriminator of richer
multi-clock designs. We do not retune the chart or eta after seeing the result.
The unbounded reference is explicitly NOT memory matched.

The common chart is v/(1+norm(v)), with
v=(a/4,b/3,tanh(c_00/4)) on the canonical representative. Context updates at eta=1
or eta=1/4; an exact bidegree change immediately resets context. Euclidean and
Poincare metrics see the same coordinates and cache capacity. The latter uses
acosh(1+2*norm(x-y)^2/((1-norm(x)^2)*(1-norm(y)^2))). Floating routing decisions
cannot authorize polynomial equality or a nonzero determinant.

## Executed verification and limitations

Python 3.13.5 / SymPy 1.14.0. The production helper is loaded only after verifying
Git blob `0c4ccb8f2dab99a5317f80345eae7920390fcbc0`. 20 test methods pass normally
and under python -O, including 60 affine composition/inverse cases, 80 orbit
recognition cases and 36 general affine determinant-law cases. Malformed inputs,
zero scale, wrong degree, wrong field/derivative, forged source value, stale source,
wrong target, empty/duplicate probes, repeated factors and leading-degree loss
are covered. The sparse rational implementation uses no tolerance for zero.

Normal and optimized benchmark semantic outputs match. Raw corpus and answer
traces match byte-for-byte. A final input-validation hardening rerun preserves
all outcomes. Stage timings are recorded but exploratory, not statistically
replicated speed evidence. Serialized active-record bytes are measured, not peak
process RSS; dictionary/geometry overhead and measurement code are not counted
as payload bytes. Independent global-resultant setup and postchecking are timed
separately and are not silently included in a per-policy speed comparison.

The primary finding is finite, same-author evidence for exact frame reuse.
It does not establish general Python/Lean equivalence, adversarial security,
optimal cache policy, geometric-learning superiority, or the class-number theorem.
No existing Lean source, numerical tool, guard or saved certificate is changed.

## Reproduce

From the repository root with SymPy 1.14.0 installed:

```sh
python -m unittest discover -s research/transport_r2 -p 'test_*.py' -v
python research/transport_r2/benchmark.py --source lean/multiplicity_exact_controls.py --output /tmp/transport-r2.json
python -O research/transport_r2/benchmark.py --source lean/multiplicity_exact_controls.py --output /tmp/transport-r2-optimized.json
```

This research experiment is manually executed; existing Lean CI does not execute
it. The next bounded proof target is the general affine transport identity for
the SAME fixed Sylvester matrix. No additional geometry should be enabled by
default without beating the exact-canonical comparator on a fresh declared task.

Primary references: the pinned repository's `DeterminantMultiplicity.lean`;
SymPy polynomial/resultant documentation (https://docs.sympy.org/latest/modules/polys/reference.html);
Nickel and Kiela, Poincare Embeddings (NeurIPS 2017,
https://proceedings.neurips.cc/paper/2017/hash/59dfa2df42d9e3d41f5b02bfc32229dd-Abstract.html).
The latter supplies background for a hyperbolic metric, not evidence of an
advantage in this experiment. The architecture interpretation is our proposal.
