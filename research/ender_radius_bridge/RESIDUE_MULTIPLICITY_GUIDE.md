# Why each eligible prime gives at least four representatives

**Production-root reachable; checked locally for the odd maximal-order chart.** For squarefree
D congruent to3 modulo4, take any finite set P of odd primes not dividing
D for which -D is a square modulo p. The theorem constructs a selected
set of exactly4*card(P) distinct class-labelled norm representatives.
It does not say these are all the representations.

Two operations account for the factor four:

- Replace a nonzero residue root r by -r. At an odd prime these roots
  differ. The two genuine maximal-order residue maps have distinct kernels.
- For each resulting ideal I, choose its generator in the fixed inverse-class
  lattice J_C. Both z and -z give the same ideal product (z)=I*J_C.

Why are the first two ideals different? The order generator recovers the
residue root by2*f(generator)-1=r. Different roots give different values.
If two residue maps differ on w, subtract the integer representative of
f(w): the result lies in ker(f) and does not lie in ker(g). Thus the
kernels differ; this is proved using the actual maps, not assumed.

Why do the sign pairs stay distinct? The integer ring has characteristic
zero and z is nonzero, so z cannot equal -z. Within the same class, any
coincidence between the two ideal pairs would contradict exact ideal
recovery. Across different classes, the class labels distinguish the points.

The family J_C is chosen once for all primes. A point records (C,z), with

    z != 0,  z belongs to J_C,  |Norm(z)| = p*Norm(J_C).

If the same labelled point represented two primes p and q, their norm
equalities would give p*Norm(J_C)=q*Norm(J_C). The ideal is nonzero, so its
norm is positive and cancellation gives p=q. The selected sets for distinct
primes are disjoint; their union therefore has4*card(P) elements.

**The labels matter.** These points belong to several ideal lattices.
The later [coordinate theorem](IDEAL_COORDINATE_GUIDE.md) constructs a basis
and actual form/count for each such lattice. A quantitative leading bound
and calibrated principal-class basis are still needed for uniform class-wide
bounds. The labelled points have not become one common Gram-lattice set.

The boundary controls explain the guards: at the ramified example D=15,
p=3, root0 equals its negative, so this pair of maps coincides. In
characteristic2, root1 equals its negative as well. These controls show
collapse of this construction, not that every ramified case has no other
representations. D=7,p=11 supplies the positive four-element control.

[Source](Phase68ResidueMultiplicity.lean) and [verification](PHASE68_VERIFICATION.md).
The original standalone source is frozen. Its exact production transport has
a [full local audit](PHASE70_VERIFICATION.md); new-head CI remains required.
The even chart, arbitrary-field
parameter transport and a usable arithmetic count B remain open.
No new cutoff or classification is claimed.

The later [actual ideal-coordinate theorem](IDEAL_COORDINATE_GUIDE.md) now
constructs the odd-chart basis/form and composes the geometric count locally.
A quantitative leading bound and calibrated principal-class basis remain.
