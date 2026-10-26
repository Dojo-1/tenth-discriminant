# Recover two terms that the uniform proxy discarded

The production determinant budget already counts every odd prime below its
cutoff. Its simpler certified uniform proxy kept only primes at least7
in the small-prime sum. The exact contributions from3 and5 can be restored
without changing the determinant or proving any stronger divisibility.

Write F(p)=sum_(r<R,t<S) min(floor(r/p),t), the original row-weight sum.
The new proxy is exactly

    recovered = certified + 2*F(3)*log(3) + 2*F(5)*log(5).

Lean proves, for R>=2 and S>=1,

    recovered <= the unchanged production lower-budget expression.

For R>=4 and S>=2 the recovered proxy is strictly larger than the old
certified proxy. This is a strict improvement in the estimate, not a new
valuation of the underlying integer determinant.

## Why adding the terms is legitimate

Knowing only that certified<=production would not justify adding anything.
The proof first identifies three disjoint pieces of the actual small-prime
sum: the3 term, the5 term and the retained>=7 terms. It bounds the certified
small-prime expression by that retained sum specifically. Because the
retained sum is nonnegative, clipping the certified expression at zero
still leaves room for the exact3 and5 contributions. The tail comparison
is unchanged. Thus neither a prime nor its valuation is counted twice.

This does not correct a false earlier theorem: discarding nonnegative terms
gave a valid but weaker proxy. The full production budget already included
them. The strict saturation example at D=19,p=3 is unaffected: no universal
extra p^2 is being claimed.

## The boundaries matter

At R=4,S=2, the gain is exactly2*log(3). At R=3,S=2 the gain is zero.
Both controls are checked. Strictness therefore has explicit dimension
guards, rather than being inferred merely from naming two primes.

The budget inequality is algebraic in its tail parameter I. To apply it
to the actual Gram, the existing certified tail, class-number/inert-prime,
radius and sampling guards still have to be supplied. This module does
not assert that arbitrary fields have every small prime inert.

## What remains before a smaller cutoff

The recovered F terms must receive useful uniform bounds after normalization
by R^2*S. Those estimates then need to be combined with the upper budget
and every geometric/floor/ceiling guard at a new endpoint. Strict gain alone
does not give a numerical endpoint, so the checked cutoff remains10^11.

[SmallPrimeRecovery.lean](../../lean/TenthDiscriminant/SmallPrimeRecovery.lean)
contains the no-double-counting and strictness proofs. The
[protocol](PHASE52_PROTOCOL.md) preceded execution; both elaboration failures
are preserved. No new numerical pilot, valuation exponent, cutoff,
classification, novelty, optimality or independent review is claimed.
