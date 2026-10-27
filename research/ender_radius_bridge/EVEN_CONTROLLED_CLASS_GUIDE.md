# One lattice per class, with a controlled first direction

The even ideal-count theorem still contained a geometric error depending
on a form coefficient a. Choosing a different basis can make a enormous.
The checked bridge chooses the basis rather than assuming a favorable one.
The statement concerns positive squarefree d=1or2mod4 and actual class
number at most two; the full field discriminant has magnitude4d.

## Why a useful first vector exists

Choose a bounded ideal J representing a given ideal class C. The existing
Minkowski theorem gives N(J)<=M(K), where M(K) is the actual field bound.
A group with at most two elements has every element equal to its inverse.
Consequently J*J is principal. A generator is an actual nonzero element
of J, with norm magnitude exactly N(J)^2.

Among nonzero elements of J choose one, z, of least norm magnitude. Its
norm is at most N(J)^2. This minimum is a natural number; no compactness
or unproved geometric shortest-vector assertion is needed.

## Why the vector is primitive in every basis

Suppose both integer coordinates of z had a common divisor g>1. Dividing
them by g produces another nonzero element w of THE SAME ideal lattice,
with z=g*w. Quadratic norm scales by g^2, so w has smaller norm than z.
That contradicts minimality. Thus the coordinates have gcd1 in every
basis. The conclusion belongs to z itself, rather than to a favored chart.

Bezout's identity completes those primitive coordinates to a matrix of
determinant1. This reversible integer operator gives a new basis with z
first. The [actual even norm form](EVEN_IDEAL_LATTICE_GUIDE.md) in that
basis satisfies

    N(z)=N(J)*a,       0<a,       4*a*c-b^2=4*d.

Since N(z)<=N(J)^2 and N(J)>0, division gives a<=N(J)<=M(K).
The previously uncontrolled geometric coefficient is now bounded.

## The choice stays fixed across the whole class

J and its basis are selected BEFORE the later ideal I, finite set U and
threshold t. Every I in C has I*J principal, so it has an actual NormLift
in the SAME J, with exact norm and recovery of I. Every norm-bounded
finite subset away from its zero coordinate row then satisfies

    cardU <= 2*pi*t/sqrt(4*d)+4*sqrt(M(K)*t/(4*d)).

This is the local-to-class bridge: different inputs share one controlled
lattice, so later sums can count them consistently. Changing J for each
prime would lose the common counting domain; this statement avoids that.

The controls retain zero scalar, negative scalar scaling, a nonprimitive
Gaussian vector and primitivity of the unit element in every basis of
the Gaussian unit ideal. [Exact attempt and checks](PHASE91_VERIFICATION.md).

The accepted proof, definitions and controls are now integrated unchanged
into the main Lean library. [Exact integration record](PHASE92_VERIFICATION.md)
keeps its local build/input/audit checks separate from external CI and
independent human review.

## What remains

This statement supplies controlled per-class OFF-AXIS counts. Full axis
counts, distinct prime lifts, the class sum and weighted prime loss on the
original Gram are still needed for an even cutoff. M(K) has not yet been
replaced by a new explicit scalar estimate. The odd-field2^50 bound and
class-number-one50billion bound are separate accepted results. No even
cutoff, classification, optimality or completed human review is asserted.
