# How a prime count controls the determinant's lost factors

We now have a checked weighted bridge for the actual even quadratic field.
Its class number may be one or two. The proof uses the original ellipse
Gram matrix throughout. [Exact statement and checks](PHASE99_VERIFICATION.md).

## One integer, three sets of primes

Write d for the positive squarefree radicand, with d=1 or 2 modulo 4.
The field is Q(sqrt(-d)); its absolute field discriminant is 4*d.
Choose any finite set P of odd primes, all at most L, with L>=3.
The original Ender radius condition and positive row dimensions remain.

A prime has a determinant weight

    w(p) = 2*F(p)*log(p),
    F(p) = sum over 0<=r<R, 0<=t<S of min(floor(r/p),t).

Partition P without dropping any prime:

- If -d is not a square modulo p, the checked local congruence gives
  an actual prime-power divisor of the same positive integer determinant.
- If p divides d, the product of these distinct primes divides d.
  Their total weight is at most R*S*(S-1)*log(d).
- The remaining primes have a square root of -d modulo p and do not
  divide d. The actual even-field class count bounds how many occur.

This last count is B(n), the Phase98 bound with actual field constant M(K):

    B(n) = (2*pi*n/sqrt(4*d) + 4*sqrt(M(K)*n/(4*d)) + 1)/2.

## The operator that turns counting into weight

Set f(n)=log(n)/n. For n>=3, f is nonnegative and decreasing. The exact
finite summation-by-parts identity replaces a sum of prime weights by
prefix counts. Replacing each count by B(n) is legitimate because every
coefficient in the following expression is nonnegative:

    K_L(B) = f(L)*B(L) + sum from n=3 to L-1 of (f(n)-f(n+1))*B(n).

This is the local-to-global step: a bound on every prefix controls the
whole weighted sum. It is the same previously checked positive operator;
only the field-specific counting input changes.

If H is the logarithm of the product of diagonal entries of the original
Gram matrix, the resulting checked inequality is

    sum over p in P of w(p)
      <= H + R*(R-1)*S*K_L(B) + R*S*(S-1)*log(d).

The theorem derives the prefix estimate and the local divisibility;
neither is supplied as an extra assumption. Empty sets work. A Gaussian
split prime and a parameter divisor exercise different parts of the
partition. A root modulo two does not bypass the odd-prime guard. With
one column, all valuation weights vanish, as they should.

## What still prevents a cutoff

The [actual constant and closed error estimate](EVEN_NORMALIZATION_GUIDE.md)
are now integrated unchanged into the main library: M(K)=4*sqrt(d)/pi, with a closed
weighted cost no larger than the previously used scalar envelope.
The original weighted bridge is integrated unchanged at Phase100. The
normalization is integrated unchanged at Phase102. The
[all-range even-chart contradiction](EVEN_TWO_CLASS_BOUND_GUIDE.md) now
passes standalone. Integration of that cutoff, arbitrary-field transport,
new external CI and human review remain open. No numerical candidate is
a premise, and no full classification is claimed.
