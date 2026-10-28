# The field constant becomes an explicit geometric scale

The even-field weighted bridge now has a closed, checked error estimate.
The remaining task is the all-range contradiction, not an assumed field
constant. [Exact proof and verification](PHASE101_VERIFICATION.md).

## Why the constant is 4*sqrt(d)/pi

Let K=Q(sqrt(-d)), with d positive and squarefree, d=1 or 2 modulo 4.
Its actual field discriminant is -4*d. These are different quantities:
d still parametrizes the original Gram matrix.

The checked basis has rational dimension two. A real embedding would send
the square root to a real number z with z^2+d=0, impossible for d>0.
Thus K has one complex place. Substitution into the existing Minkowski
bound gives

    M(K) = (4/pi)^1 * (2!/2^2) * sqrt(4*d)
         = 4*sqrt(d)/pi.

This is a theorem about the actual field. It assumes neither a numerical
estimate for M(K) nor a class-number-one condition.

## From a finite sum to a closed formula

The prime count still carries its half-unit constant. The positive
summation operator carries that constant to log(3)/6; it is not dropped.
For L>=3, define

    C(x,M,L) = (pi/sqrt(x) + 2*sqrt(M/(3*x)))
                 * (log(3) + log(L)*(1+log(L))) + log(3)/6.

The checked error cost for the even count is at most

    C(4*d, (4/pi)*sqrt(d), L).

This uses the generic square-root majorant, exact finite summation by
parts and a harmonic-sum bound. No odd-field counting theorem is used.
Multiplying by the original nonnegative loss scale and adding the
parameter-divisor budget gives the full closed bound on the SAME Gram.

## Why the old scalar envelope is still sufficient

A second checked inequality gives

    C(4*d, (4/pi)*sqrt(d), L)
      <= C(d, (2/pi)*sqrt(d), L).

Although M(K) doubles relative to the odd scalar expression, the count's
discriminant denominator also changes to 4*d. The area contribution
shrinks, and so does the square-root contribution. Nonnegative weights
preserve the comparison. This compares two real formulas; it does not
replace the even field by an odd one.

Consequently the full original-Gram weighted budget is now bounded by
an explicit scalar formula already used elsewhere in the development.
The accepted proof and controls are now integrated unchanged into the main
library. [Integration checks](PHASE102_VERIFICATION.md) pass locally. The
final all-range even cutoff, arbitrary-field transport, new external CI
and human review remain open. No new cutoff is claimed here.
