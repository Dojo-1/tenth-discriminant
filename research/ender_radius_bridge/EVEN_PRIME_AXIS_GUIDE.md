# The missing row costs two points, across all primes

The ellipse count excludes the coordinate row y=0. That exclusion was
necessary: counting the origin alone would break its zero-threshold
bound. To count prime-norm elements, we must account for that row using
arithmetic, rather than remove the guard from the geometric theorem.

Fix ONE actual ideal J and ONE positive normalized norm form

    norm(x*e0+y*e1)=N(J)*(a*x^2+b*x*y+c*y^2).

A prime-normalized element has norm magnitude p*N(J), with p prime.
On y=0, positivity and cancellation of N(J)>0 give a*x^2=p.

## Two possible points, not two for each prime

Since p is prime, x^2 must be1: otherwise the square would factor the
prime. Thus x = 1 or x = -1 and a=p. The only possible axis coordinates are
(1,0) and (-1,0). The coefficient a is fixed BEFORE the prime varies.
Consequently there are at most TWO axis elements across ALL primes in
any finite set in this fixed lattice. We do not pay two for each prime.
Distinct actual elements have distinct coordinates, so the coordinate
bound is also a bound on actual ideal elements.

## The principal class pays nothing

An identity-class ideal J is principal, even when the whole field has
class number two. Multiply the actual maximal-ring basis1,sqrt(-d) by
its generator. The generator's norm equals N(J); dividing the norm form
by N(J) cancels that factor. The normalized form is exactly

    x^2+d*y^2,             a=1, b=0, c=d.

Its discriminant magnitude is4d. No global unique-factorization or
class-number-one assumption is used. On the axis it would represent a
prime as x^2=p, which is impossible. Thus every prime-normalized element
in this calibrated principal-class basis is already off the axis.

## The complete per-class count

Under actual class number at most two in the positive squarefree even chart d congruent to 1 or 2 modulo 4,
choose a bounded J and controlled basis for a class C. For C=1 use the
calibrated basis above; for other classes retain the controlled basis.
The SAME J lifts every ideal in C and the SAME basis serves every finite
prime-normalized norm-bounded set U and natural-number threshold t. Splitting U into
its off-axis and axis parts gives

    cardU <= 2*pi*t/sqrt(4*d)+4*sqrt(M(K)*t/(4*d))
              +(if C=1 then0 else2).

The caller supplies no off-axis guard. The theorem derives the missing
axis contribution and combines it with the checked geometric count.
[Exact bounded attempt and controls](PHASE93_VERIFICATION.md).

The accepted proof and all controls are now integrated unchanged into
the main Lean library. [Exact integration record](PHASE94_VERIFICATION.md)
keeps those local checks separate from external CI and human review.

This is a count in each actual class, not yet the complete split-prime
weighted estimate. Distinct even residue maps, four labelled prime lifts,
a common class-indexed prime family, class summation, weighted loss and
the same-original-Gram comparison still need their own checked assembly.
No even cutoff or full classification follows from this statement alone.
