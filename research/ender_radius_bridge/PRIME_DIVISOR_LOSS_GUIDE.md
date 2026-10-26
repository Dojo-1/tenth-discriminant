# The exceptional prime divisors pay for themselves

**Checked locally in Lean, as a standalone research theorem.** This removes
one part of the missing arithmetic budget. It gives no new cutoff.

The determinant argument earns a contribution from each good prime.
Excluded primes represent lost contributions. We now separate those that
divide the positive integer parameter D from the other excluded primes.

For any finite set T of distinct prime divisors of D,

    product of primes in T <= D,
    sum of their logarithms <= log D.

This is the local-to-global step: each prime divides D, distinct primes
are coprime, and therefore their whole product divides D. Taking logarithms
turns that product into the sum needed by the determinant argument.

The original valuation weight is

    F(R,S,p) = sum over 0<=r<R, 0<=t<S of min(floor(r/p), t).

Every minimum is at most t. Summing the resulting arithmetic progression gives

    2F(R,S,p) <= R*S*(S-1).

Consequently the total lost weight from T is at most

    R*S*(S-1) * log D.

No estimate of how many prime divisors D has is required.

For the full statement, let E=P\G be the excluded primes, T the members of
E dividing D, and U=E\T. The same original ellipse Gram determinant satisfies

    mass(P) <= log(Hadamard diagonal product)
               + lossScale * kernelCost(B)
               + R*S*(S-1)*log D.

The existing prime, oddness, nonsquare-good-prime and Ender-radius guards
remain. The prefix count B is required only for U. No prime is discarded:
P is the disjoint union of G, T and U, and the proof pays for each part.

**What remains:** for arbitrary G, U means non-divisor excluded primes;
it is not automatically the full split-prime set. Relating the parameter
to the actual field discriminant, constructing ideal-class norm forms and
proving representation multiplicity remain open here. This theorem does
not turn a geometric estimate into an arithmetic B by assumption.

The [verification record](PHASE65_VERIFICATION.md) preserves the first
failed attempt, its fixed repair, all controls and the successful axiom audit.
The source is outside the production root and its CI coverage.
