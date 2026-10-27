# The prime count now pays the arithmetic loss

**Checked locally in Lean:** under actual h<=2 in the squarefree odd
chart, the prefix count now supplies a concrete weighted loss bound on
the original derivative trace-Gram. The radius and finite-prime guards
remain explicit. No new discriminant cutoff follows yet.

Start with any finite set P of odd primes, all at most L. Choose EVERY
nonsquare prime in P as good. Among the remaining primes, remove those
dividing D. Exact finite-set membership then says the remainder consists
of primes with -D square modulo p and p not dividing D. These are exactly
the guarded primes covered by the checked prefix count:

    B_D(n)=(2*pi*n/sqrt(D)+4*sqrt(M(K)*n/D)+1)/2.

The theorem supplies this B_D; the caller does not assume an excluded
count or supply an arbitrary incomplete good-prime set.

Why a count pays for a weighted sum: f(n)=log(n)/n decreases for n>=3.
Finite summation by parts bounds the remainder's sum of f(p) by

    K_L(B)=f(L)*B(L)+sum(n=3,...,L-1)(f(n)-f(n+1))*B(n).

Every coefficient of B is nonnegative, so an upper bound for every prefix
count gives an upper bound for this weighted sum. The earlier checked
contact-weight inequality converts it into the missing determinant budget.

Prime divisors of D have their own payment. Their distinct product divides
D, so their total logarithmic contribution is bounded by log(D), with
the already proved contact factor R*S*(S-1).

Combining the good primes, the counted remainder and the divisor payment
on the SAME original Gram yields

    sum(p in P) 2*F(p)*log(p)
       <= log(product of the original Gram's diagonal entries)
          + R*(R-1)*S*K_L(B_D) + R*S*(S-1)*log(D).

F(p) is the existing derivative-contact weight. The original matrix,
ordinary derivatives and factor-of-two normalization are unchanged.
The theorem assumes the existing Ender radius guard, R,S>=1 and L>=3.
It supplies the actual count, coverage and weighted arithmetic input.

The remaining analytic task is to bound K_L(B_D) in a useful closed form,
identify the field-dependent Minkowski term with the chart parameter,
and prove a strict numerical contradiction for a chosen radius family.
Even-chart/field transport and a new cutoff also remain open.

Controls retain an actual split witness D=7,p=11, removal of parameter
divisors, exclusion of good primes from the remainder, and the empty set.
[Exact verification](PHASE82_VERIFICATION.md) separates local proof/audit
from external exact-head CI and human review. No classification is announced.

Phase83 update: a separately registered standalone proof now supplies the
closed kernel estimate and composes it with this same inequality. The
paragraph above records the82 checkpoint. [Closed-bound explanation](CLOSED_KERNEL_GUIDE.md).
Minkowski/field/even transport and a new numerical cutoff remain open.

Phase84 update: the accepted closed-kernel mathematics is now integrated.
The actual odd-field Minkowski term is proved equal to2sqrt(D)/pi and
substituted into the original-Gram budget. [Current human guide](ODD_MINKOWSKI_GUIDE.md).
Earlier open-M(K) language records the preceding checkpoint; arbitrary-
field/even transport and a new numerical cutoff remain open.
