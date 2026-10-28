# A controlled vector is still not a checked controlled basis

**The latest bounded proof attempt failed and is stopped.** The preceding
[controlled-vector theorem](CLASS_SQUARE_GUIDE.md) remains accepted locally.
This attempt adds no checked leading-coefficient bound or numerical range.

The intended mathematical step is concrete. Start with the actual
coordinates (m,n) of the nonzero controlled vector z in an ideal J.
Write (m,n)=d(u,v), where d is a positive integer and gcd(u,v)=1.
Then w=u*e0+v*e1 is an actual element of J, with z=d*w.

Bezout gives integers A,B with u*A+v*B=1. The two matrices

    [ u  -B ]       [ A   B ]
    [ v   A ]  and  [-v   u ]

are inverse over the integers. They should make w the first vector of
an integral basis of J. This is a reversible change of coordinates on
the same ideal, preserving the lattice rather than replacing it.

The old normalized norm form Q is homogeneous of degree two:

    N(J) = Q(m,n) = d^2*Q(u,v).

Here the first equality uses the checked controlled-vector norm identity
and cancellation of the positive ideal norm. If the new actual basis
construction is checked, its leading coefficient is Q(u,v)>0. Since
d>=1, this gives the desired a<=N(J). This paragraph describes the
intended proof; the current Lean attempt did not establish that theorem.

What failed: basis equality simplification left a reflexive goal; an
absolute-value theorem was referenced with incorrect projection syntax;
the unit-ideal control's squarefreeness proof was unfinished. More
decisively, assembling the actual normalized-form witnesses reached
Lean's default 200000-heartbeat limit. The final namespace audit rejected
an unavailable project theorem. Printed signatures are not accepted proofs.

The registration says to stop after any resource limit. There was one
invocation, no repair or rerun, and no raised limit. Full source and logs
remain in [the verification record](PHASE75_VERIFICATION.md). This is a
formalization failure, not a mathematical counterexample. A future design
needs smaller independently checked interfaces; renaming and replaying
this stopped attempt would not satisfy its protocol.
