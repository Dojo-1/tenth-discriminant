# Factorials count prime powers—not yet the determinant's prime mass

Phase 22 proves the exact factorial identity and the scalar expression used
by `tools/ender.py:factorial_lower`. It does not yet prove `prime_mass`.
The distinction matters: two different sums occur in Ender's argument.

## One product, two descriptions

Write

$$H(R)=\sum_{r=0}^{R-1}\log(r!)
=\log\!\left(\prod_{r=0}^{R-1}r!\right),\qquad
A_R(q)=\sum_{r=0}^{R-1}\left\lfloor\frac r q\right\rfloor.$$

Legendre's formula counts the copies of a prime in each factorial.
Interchanging the two finite sums gives the checked identity

$$H(R)=\sum_{\substack{p<R\\p\text{ prime}}}\log p
\sum_{\substack{1\le j<R\\p^j<R}}A_R(p^j).$$

There is no prime-distribution estimate here. A power at or above `R`
contributes zero, so the strict endpoint is harmless once proved. Prime
`2` is essential: at `R=3`, the product is `2`, not `1`. At `R=5`,
the product is `288=2^5 3^2`; the two prime-power sums are exactly `5`
and `2`. These are checked controls, not evidence extrapolated to all `R`.

## A lower bound without evaluating the product

For `x≥1` put `f(x)=x log x−x+1`. The elementary inequality
`log(1+1/n)≤1/n` proves, by induction,

$$f(n)\le\log(n!).$$

Also `f'(x)=log x≥0`. An increasing function lies below the right-endpoint
rectangles used to integrate it. With `N=R−1≥1`, this yields

$$H(R)\ge\int_1^N f(x)\,dx
=\frac{N^2}{2}\log N-\frac{3N^2}{4}+N-\frac14.$$

Since `N≥1`, this implies the unchanged production bound

$$\boxed{H(R)\ge
\frac{N^2}{2}\log N-\frac{3N^2}{4}+\frac N2+\frac14,
\qquad R\ge2.}$$

The proof actually has spare slack `(N−1)/2`. We keep the production
formula rather than silently substituting an improved one. Equality holds
at `R=2`. The guard is real: at `R=1` the displayed formula would be `1/4`
while `H(1)=0` under Lean's totalized logarithm.

## The remaining bridge: change the weights, not the determinant

The already checked determinant comparison has a different left side:

$$L(R,S)=2\sum_{\substack{p<R\\p\text{ odd prime}}}F_{R,S}(p)\log p
\ \le\ \texttt{upper\_B}.$$

Here `F` is the rectangular valuation weight, not the factorial
prime-power weight above. Thus `factorial_lower≤H` does **not** imply
`prime_mass≤L`. [Phase 23's staircase proof](PRIME_MASS_LOWER_GUIDE.md)
now checks the small-prime split, weight conversion, finite geometric
loss bounds and clipping. One analytic reciprocal-prime tail inequality
remains explicit. Only after that and the numerical interpretation can
the saved comparisons yield contradictions under class number one.

This is a classical counting identity and elementary integral estimate;
no novelty, improved cutoff or class-number classification is claimed.

## Where to inspect and reproduce

[FactorialPrimeMass.lean](../../lean/TenthDiscriminant/FactorialPrimeMass.lean):
`factorialMass_eq_prime_power_sum`, `factorialLower_le_mass`, and
`factorialLower_le_prime_power_sum`. The final name refers to the factorial
prime-power sum, not `L`. Automatic implicit variables are disabled.
Ten controls include the small radii, prime `2`, composite indices and the
strict power endpoint. [Preregistration and execution record](PHASE22_PROTOCOL.md).

From `lean/`: `lake build`, `python verify_sources.py`, `python audit.py`,
and `python negative_controls.py`. Pinned Linux CI runs all four; the
source check compares recorded interval endpoints, not their Arb inequalities.
