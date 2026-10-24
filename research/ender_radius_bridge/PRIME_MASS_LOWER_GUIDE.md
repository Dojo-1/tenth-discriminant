# The lower bridge: count a staircase, then control its tail

Phase 23 checks the finite conversion from factorial weights to the
determinant's odd-prime weights. It reaches the actual counted `upper_B`
**conditional on one explicit reciprocal-prime tail bound**. That analytic
bound and numerical certificate interpretation are not proved by this phase.

## Why the quadratic correction is there

For one row index `r`, put `k=floor(r/p)`. The determinant weight counts
the staircase `min(k,0), min(k,1), …, min(k,S−1)`. When `k≤S`, its sum is
a rectangle of area `S*k` minus the triangular corner `k(k+1)/2`.
Consequently, with

$$A(p)=\sum_{r<R}\lfloor r/p\rfloor,\qquad
Q(p)=\sum_{r<R}\lfloor r/p\rfloor^2,$$

the exact identity is

$$\boxed{F(p)=(S-\tfrac12)A(p)-\tfrac12Q(p).}$$

The program's guard `R≤P*S` ensures `k<S` for every `r<R` and `p>P`.
The proof permits the harmless equality `k=S` too. Dropping `Q` is false:
at `R=5,S=2,p=3`, `F=2`, `A=2`, `Q=2`, so the omitted-loss formula gives
`3` instead of `2`. Without the quotient guard, the polynomial formula
also fails; the staircase has already saturated. Both falsifiers compile.

## Where factorials enter

Let `H` be the [factorial mass](FACTORIAL_LOWER_GUIDE.md). Split its exact
Legendre identity at `P≥2`:

$$H=B_{\rm small}+T+E,$$

where `Bsmall` counts **all powers** of small primes (including `2`),
`T=∑_{p>P} A(p) log p`, and `E` counts their remaining powers `p²,p³,…`.
All these sums are finite, with prime indices below `R`.

Write `V=R(R−1)/2`, `W=R(R−1)(2R−1)/6`, and

$$J=\sum_{\substack{P<p<R\\p\text{ prime}}}
\frac{\log p}{p(p-1)}.$$

Lean checks `A(q)≤V/q` and `Q(p)≤W/p²`. A finite geometric sum bounds
`∑_{j≥2}p^(−j)` by `1/(p(p−1))`; also `1/p²≤1/(p(p−1))`. Therefore
`E≤V*J` and `∑_{p>P} Q(p)log p≤W*J`. No prime-distribution result is used.

For any supplied `I≥J`, the checked scalar `Hlow≤H` gives

$$\sum_{p>P}F(p)\log p\ge
(S-\tfrac12)(H_{\rm low}-B_{\rm small}-VI)-WI/2=:b.$$

The actual sum on the left is nonnegative, so it also exceeds `max(b,0)`.
Add the exact small **odd** prime contributions and multiply by two. This
is precisely the mathematical clipping and integer coefficients used by
production `prime_mass`. The production enumeration through `P` agrees
with the restricted finite sums: primes at or above `R` have zero weight.
Lean checks these coefficient, padding and branch identities too.

## The remaining analytic inequality is explicit

To use production's unchanged `I`, the next proof must establish

$$J\le I(P)=\frac{\log(P+1)}P+\log(1+1/P).$$

The paper compares the summands with the integral of `log(t+1)/t²`.
That comparison is **still open in Lean here**. The public theorem
`ellipse_enderPrimeMassLower_le_upperB` exposes `J≤I` as a hypothesis;
it does not hide it inside a numerical premise or a new axiom. Once
supplied, the same original Gram gives the full mathematical lower/upper
comparison. Interpreting Arb enclosures, universal closure, even cases and
finite classification remain separate. No new cutoff or novelty is claimed.

[Lean source](../../lean/TenthDiscriminant/PrimeMassLower.lean) ·
[Preregistration and execution](PHASE23_PROTOCOL.md). Eight controls cover
the split boundary, empty large-prime set, guard endpoint, both clipping
branches and the two false strengthenings. From `lean/`: `lake build`,
`python verify_sources.py`, `python audit.py`, `python negative_controls.py`.
