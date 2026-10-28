# One lattice, compatible arithmetic and geometry

The bridge is the map Φ(x,y)=x+i√D y. Its arithmetic interpretation is
x+y√(-D) in the quadratic field. The new Lean proof checks that these are
coordinates for the same object, and that its arithmetic norm is exactly
the squared complex length x²+Dy². This is the local-to-global joint:
prime divisibility and real geometry act on the same integer matrix.

For positive squarefree D congruent to 1 or 2 modulo 4, these coordinates
describe every element of the actual ring of integers, uniquely. In the
odd chart, (x,y) maps to (x-y,2y) in the half-integral basis. That matrix
has determinant 2: its image is precisely the pairs with even second
coordinate. The norm identity holds there; this selected sublattice is
not the entire integer ring. The distinction matters.

## Moving the samples

The second operator is T_v(p)=p+v. Its inverse is T_{-v}, and
T_u∘T_v=T_{u+v}. It commutes with both arithmetic addition and Φ.
Distances and the number of samples stay fixed. An ellipse moves with its
centre: membership is tested by (x-c₁)²+D(y-c₂)²≤ρ². A point's norm from
the original origin need not stay fixed.

The shifted integer trace-Gram matrix casts exactly to the real matrix
built from the shifted complex samples. The row order, ordinary Z
derivatives with W fixed, and factor-of-two normalization are unchanged.
For an odd prime p with -D nonsquare modulo p, its determinant still has
the proved prime-power divisor. With J≥S, positive R,S and more than
2(R-1)+(S-1) distinct samples, it is still positive definite.

## The invariant we must not assume

Take D=1 and samples {(-1,0),(0,0),(1,0)}, with J=1,R=2,S=1.
The determinant is 24. Move every point by (0,1): it becomes 60.
Both sets exceed the strict sample-count threshold. Lean proves these
exact values. Thus even an ample sample set does not make this real
trace-Gram determinant invariant under translation. Translation is an
affine action; it is not a multiplicative ring homomorphism.

This negative result guides optimization: a shifted construction needs
its own upper estimate. We cannot carry over the old diagonal estimate
merely because distances and divisibility survive. No lower cutoff has
been obtained here; the class-number-one bound remains 50 billion.

## Where to inspect the proof

The small lemmas in [the source](Phase105CoordinateTranslation.lean)
lead to `coordinate_translation_bridge`; the counterexample is
`shifted_gram_counterexample`. All 29 public statements and five complete
definitions stayed fixed across three bounded attempts. Two proof-script
repairs were needed; all failures are retained in the
[verification record](PHASE105_VERIFICATION.md).

This is a checked standalone bridge, awaiting library integration and its
own pinned CI. [PR #36's merged result](PR36_MERGE_RECEIPT.md) is a separate
verified checkpoint. Arbitrary even-field transport and independent human
semantic review remain open. Neither checkpoint announces a full
class-number classification.
