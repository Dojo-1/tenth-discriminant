# One symmetry respected by geometry and arithmetic

The earlier [central-symmetry theorem](CENTRAL_SYMMETRY_GUIDE.md) separates
even- and odd-total-degree rows of the original integer Gram. The new
compatibility theorem checks that the actual odd-p Frobenius basis matrix
respects precisely the same separation. This closes the operator link that
was only an elementary observation in the Phase49 guide.

## The shared operator

On the original R*S monomial rows define C to be diagonal: +1 on labels
(r,s) with r+s even, and -1 on labels with r+s odd. The two sectors consist
of coordinate vectors supported on the corresponding labels.

The Lean module proves two equations for the actual integer matrices:

    G*C = C*G       when the original samples are centrally symmetric;
    U_p*C = C*U_p   when p is positive and odd.

Here G is the original ordinary-derivative trace-Gram with factor two.
U_p is the already constructed integral, determinant-one binomial basis
matrix; it is not a newly selected equivalent matrix.

The first equation says that observation geometry does not couple the
sectors. The second says that the arithmetic basis change does not couple
them either. Grouping the original labels by parity therefore respects
both operators. No square-rectangle assumption or Z/W exchange is used.

## Why odd p is the exact guard

A guarded term of the Frobenius basis expansion has label

    (r-p*t, s+t),  with p*t<=r and s+t<S.

Its total degree is r+s-(p-1)*t. For odd p, the change in degree is even.
The existing active-index theorem supplies the bounds, so natural
subtraction never silently truncates an invalid exponent. Lean checks
zero matrix entries between opposite-parity labels before proving
commutation with C.

For p=2 the counterexample is the row Z^2-W in the3-by2 rectangle:
the coefficient from even label(2,0) to odd label(0,1) is -1.
The claimed support separation would be false without oddness.

## Why this is an integral decomposition

Over Q the sector projectors can be written (I+C)/2 and (I-C)/2. One
must not assume such division preserves an arbitrary integer lattice.
Here it does preserve the row lattice because C is explicitly diagonal
with entries+1 or-1: the projectors simply keep or erase coordinates.
This explanation is a direct consequence of the definition; the module
exports the support and commutation theorems, not a separate projector API.

The two commuting equations also imply that the transformed Gram
U_p*G*transpose(U_p) respects the same sectors. That is a linear-algebra
consequence, not an additional exported determinant-factorization theorem.

## The quantitative question is still open

Commutation makes the proof structure clearer, but it supplies no new
prime-power exponent. Applying Hadamard inside each sector still gives
the old product of diagonal entries. A better cutoff needs a proved gain
within a sector, with all derivative and integral-quotient factors retained.
The existing saturation control forbids adding a universal extra p^2.

[ParityCompatibility.lean](../../lean/TenthDiscriminant/ParityCompatibility.lean)
contains the checked support/commutation theorems and prime-two control.
The [protocol](PHASE50_PROTOCOL.md) preceded execution. This is a small
structural bridge, not a cutoff improvement, classification, novelty,
optimality, independent review, merge or Tao-submission result.
