# How many missing primes can the determinant afford?

**Lean now proves the conversion from a count of excluded primes to their
lost determinant contribution. The arithmetic count itself remains open.**
The theorem is in the production library. It improves the interface, not
the current50-billion cutoff.

## Keep the same object in view

Geometry puts a ceiling on our positive integer determinant. A prime p
for which -D is nonsquare supplies a divisor of that very same determinant.
Call those primes good. The other primes are excluded: their factors
cannot be demanded by this argument. We must account for the loss.

Let F(R,S,p) be the existing staircase weight. Each of its RS entries is
min(floor(r/p),t). Ignore the second restriction and multiply by p:

    2p F(R,S,p) <= 2S sum(r=0,...,R-1) r = R(R-1)S.

Thus an excluded prime costs at most C log(p)/p, where C=R(R-1)S.
This bound is deliberately simple; no sharpness is claimed.

## Counts become a loss budget

Write N(n) for the number of excluded primes at most n. Suppose arithmetic
proves N(n)<=B(n) for3<=n<=L. Put f(n)=log(n)/n. This function is positive
and decreasing for integer n>=3. Exact finite summation by parts gives

    sum(excluded p) f(p)
      = f(L)N(L) + sum(n=3,...,L-1) (f(n)-f(n+1))N(n)
      <= f(L)B(L) + sum(n=3,...,L-1) (f(n)-f(n+1))B(n).

All coefficients are nonnegative. Consequently the actual-Gram theorem is

    all prime mass <= geometric ceiling + C*(the displayed count budget).

This is the local-to-global bridge: each good prime supplies a local
congruence constraint; their coprime factors accumulate on one global
integer. A count of the remaining primes measures what that argument
loses. The geometry and arithmetic meet on the same determinant.

## What is still missing?

A valid B for the intended class-number family, strong enough to make the
final bounds conflict. The Phase60 zero-row example shows why an attractive
per-form count cannot simply be assumed. This theorem neither repairs that
count nor refutes its aggregate version. It proves no higher-class-number
cutoff and supplies no new classification claim.

Lean entry point: `TenthDiscriminant.ExcludedPrime.excluded_prime_budget_log_div`.
It retains the original prime, nonsquare and radius hypotheses. Callers no
longer supply a kernel, monotonicity proof or separate weight bound.
The proof reuses Mathlib summation by parts, the integer interval sum and
logarithm monotonicity. [Verification and preserved failure](PHASE61_VERIFICATION.md).
