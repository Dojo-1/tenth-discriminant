# From a prime count to a closed error bound

The remaining weighted sum now has an explicit Lean-checked upper bound.
The result is local and standalone; it has not received external CI or
independent human review. It does not give a new discriminant cutoff.

The count from the ideal lattices has three terms:

    B_D(n) = pi*n/sqrt(D) + 2*sqrt(M(K)*n/D) + 1/2.

Here M(K) is the actual field's Minkowski norm bound. The first two
terms measure lattice size and boundary error. The last term comes from
counting the exceptional axis points across ideal classes.

The weights f(n)=log(n)/n decrease for n>=3. Summation by parts turns a
prefix count B into the positive linear operator

    K_L(B) = f(L)*B(L) + sum(n=3,...,L-1)(f(n)-f(n+1))*B(n).

Every coefficient is nonnegative. Thus a larger prefix bound gives a
larger cost, and we can estimate each part separately.

For n>=3, the square-root term obeys

    sqrt(M*n/D) <= n*sqrt(M/(3*D)).

So B_D(n) <= alpha*n+1/2, where

    alpha = pi/sqrt(D) + 2*sqrt(M(K)/(3*D)).

The useful identity is exact, before any estimate:

    K_L(alpha*n+beta)
      = alpha*(log(3)+sum(k=4,...,L)log(k)/k) + beta*log(3)/3.

A constant count is paid ONCE, at the first weight. Replacing that constant
by a linear allowance would create a growing error and discard useful
information. This is why the axis contribution stays separate.

Bounding the remaining sum by log(L) times the harmonic sum gives

    K_L(B_D) <= alpha*(log(3)+log(L)*(1+log(L))) + log(3)/6.

Lean also composes this bound with the original determinant inequality.
All its squarefree odd-chart, actual class-number<=2, finite odd-prime,
R,S,L and Ender-radius guards remain. No counting function, coverage
assertion or older cutoff is assumed. The original derivative Gram and
its normalization are unchanged.

What remains is concrete: express M(K) effectively in D for this actual
field chart, complete field/even-chart transport, choose parameters and
prove a strict numerical contradiction. The estimate above is conservative;
it is not claimed sharp. The class-number-one cutoff remains50billion.

[Exact source and verification](PHASE83_VERIFICATION.md) preserve the failed
first normalization, passing repair, controls and dependency exclusions.

Phase84 update: the accepted closed-kernel mathematics is now integrated.
The actual odd-field Minkowski term is proved equal to2sqrt(D)/pi and
substituted into the original-Gram budget. [Current human guide](ODD_MINKOWSKI_GUIDE.md).
Earlier open-M(K) language records the preceding checkpoint; arbitrary-
field/even transport and a new numerical cutoff remain open.
