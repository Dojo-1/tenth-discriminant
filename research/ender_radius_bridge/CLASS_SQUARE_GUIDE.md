# Squaring a class gives a controlled vector

**Checked locally in Lean under the actual hypothesis that the field has
class number at most two.** This supplies a vector in each ideal class;
it does not yet supply the controlled basis needed for a new cutoff.

The class group records which ideals differ by multiplication by a
single field element. Multiplying ideals multiplies their classes.
With at most two classes, every class is its own inverse: squaring any
class gives the identity. This elementary symmetry is the whole new step.

Choose a nonzero integral ideal J representing a class, with the existing
Minkowski bound N(J)<=M(K). The class of J squared is the identity, so

    J*J = (z)

for some nonzero algebraic integer z. Also z belongs to J: the product of
two integral ideals is contained in either factor. Ideal norms multiply,
and the norm of a principal ideal is the magnitude of its element norm:

    |Norm(z)| = N(J*J) = N(J)^2.

Our quadratic form measures element norm divided by N(J). Thus this vector
has normalized value N(J), bounded by M(K). The construction uses actual
ideals and actual algebraic norms, without assuming all ideals principal
or importing a table of fields of class number two. The theorem is valid
for every number field with class number at most two; the geometric
interpretation as a short vector uses the imaginary quadratic setting.

Why this matters: the geometric count has an error term depending on the
first basis vector's normalized norm. An arbitrary basis can make that
coefficient enormous. We now have a controlled candidate vector instead.

Why a gap remains: z might be an integer multiple of a smaller vector.
One must divide out the gcd of its two coordinates, prove the resulting
vector stays in the ideal and does not increase its norm, then extend it
to an integral basis using Bezout's identity. Only after those steps may
we claim a controlled leading coefficient. They have not been checked
in this campaign. A [later bounded attempt](CONTROLLED_BASIS_ATTEMPT.md)
hit its resource limit and is preserved as failure; it does not close this gap.

The order-three control checks 1!=-1 in ZMod3: self-inversion is special
to the at-most-two hypothesis. Other controls exclude the zero vector,
check the group identity and instantiate the result over the rationals.

[Exact statements](Phase74ClassSquare.lean) ·
[Saved verification](PHASE74_VERIFICATION.md) ·
[Principal-class calibration](PRINCIPAL_BASIS_GUIDE.md).

This standalone result is outside production CI. Class-wide counting,
the even chart, field transport and a usable excluded-prime bound remain
open. The checked class-number-one cutoff stays 50 billion.
