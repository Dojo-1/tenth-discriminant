# Two sign sectors in the same determinant

There is a useful symmetry that preserves a thin monomial rectangle:
simultaneous negation of both coordinates. It acts on every observation
z as z -> -z, and on a monomial Z^r W^s by the sign (-1)^(r+s).
It neither exchanges Z with W nor requires equal side lengths.

The original ellipse is invariant under (x,y) -> (-x,-y). The new Lean
theorem proves that its actual integer trace-Gram entry vanishes whenever
the two row labels have opposite total-degree parity. The generic theorem
requires only that the original finite sample set be stable under this
negation; it retains all derivative orders, samples and the factor two.

## Why derivatives preserve the separation

An ordinary Z-derivative of order j changes a monomial's sign exponent
from r+s to r+s-j. In a Gram entry, both rows use the same order j.
The product therefore has sign

    (-1)^(r+s+t+u-2j) = (-1)^(r+s+t+u).

If a derivative is zero because j exceeds its Z-degree, that summand is
already zero. Otherwise the displayed sign follows from homogeneity.
For opposite parity the paired contributions at a and -a cancel. The
origin causes no exception: any contribution that changes sign there is
its own negative, hence zero in the integers.

Thus rows of even and odd total degree are orthogonal. Grouping the rows
by parity gives a block diagonal matrix. This is an immediate mathematical
consequence of the checked entry theorem; a separate determinant-product
API is not exported by this module.

## Compatibility with the local arithmetic

For an odd prime p, the existing integral Frobenius basis change replaces
Z^r W^s by a combination of Z^(r-p*t) W^(s+t). On its guarded active range,
the new total degree is r+s-(p-1)*t, of the same parity as r+s.
So this arithmetic transformation also respects the two sectors. This
paragraph is the elementary parity calculation on the already proved
row-action formula, not a newly exported Lean compatibility theorem.
The prime-two case is not included in this observation.

## What this does and does not buy

This decomposition makes the same large Gram matrix easier to understand
and supplies exact zeros for future bounds or implementations. It does
not by itself improve Hadamard: applying a diagonal bound separately to
the two blocks gives the same product of diagonal entries. A quantitative
improvement must exploit information inside a block. Nor may a prime-power
gain be added merely because there are two sectors.

The symmetry assumption matters. Lean checks that on the nonsymmetric
singleton sample (1,0), the entry between rows (0,0) and (1,0), at D=J=1,
equals2. Omitting sample symmetry would make the proposed theorem false.

[CentralSymmetry.lean](../../lean/TenthDiscriminant/CentralSymmetry.lean)
contains the generic entry theorem, ellipse instance and negative control.
The [protocol](PHASE49_PROTOCOL.md) preceded source execution. Both failed
attempts are preserved. This is a structural result, not a new cutoff,
classification, valuation improvement, novelty or independent review claim.
