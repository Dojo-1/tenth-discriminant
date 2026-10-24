# The field's discriminant, and four positive class-number proofs

Phase33 now supplies all nine positive proofs and both classification
directions below one million. See the [all-nine guide](NINE_POSITIVE_GUIDE.md).
This guide retains the discriminant calculation and initial four-case argument.

There are now two kinds of checked class-number result. The sieve gives a
necessary nine-element list below one million. This phase proves actual
class number one for four of those fields: d=1,2,3,7. It also identifies the
actual field discriminant for every positive squarefree radicand.

## A basis calculation with a geometric warning

In an integral basis (1,u), suppose u^2=s*u-t. Multiplication has trace
2*x+s*y on x+y*u. Consequently the trace pairing has matrix

    [ 2      s       ]
    [ s    s^2-2*t   ]

and determinant s^2-4*t. This elementary two-dimensional identity is
`quadraticBasis_discr`; it does not need a special field presentation.

To call that determinant the **field discriminant**, the basis must span
the entire ring of algebraic integers. The maximal-order equivalences
already proved in the repository supply precisely that condition:

- If d=3 modulo 4, use u=(1+sqrt(-d))/2, s=1, t=(d+1)/4. The determinant is -d.
- Otherwise, for positive squarefree d, use u=sqrt(-d), s=0, t=d. It is -4*d.

These are statements about the actual `NumberField.discr`, not a parameter
defined to have the desired value. Its absolute value is now proved equal
to `absoluteDiscriminantParameter d`. The previously checked cutoff therefore
gives an actual absolute field-discriminant bound below 700000000000 under
class number one. The constant itself has not improved.

The warning is visible at d=3. The order with basis (1,sqrt(-3)) has
discriminant -12; the field's full integer ring has discriminant -3. Their
bases differ by a determinant-two change, and the trace determinants differ
by four. Lean checks both discriminant values. A convenient order must not
silently stand in for the maximal order.

Do not confuse this 2-by-2 integral-basis discriminant with the large positive
jet-Gram determinant used in the cutoff argument. This phase identifies the
field parameter; it does not replace the original Gram matrix.

## Why the first four fields really have class number one

The pinned library proves Minkowski's small-ideal representative theorem:
every ideal class has an integral ideal whose norm is bounded in terms of
the degree, signature and absolute field discriminant. If that bound is
strictly below two, its positive integer norm must be one. The ideal is
the whole ring, so every ideal class is trivial.

For an imaginary quadratic field the bound is 2*sqrt(|Delta|)/pi.
When |Delta|<=8, sqrt(|Delta|)<3<pi, so this is below two. Our formal helper
handles both possible degree-two signatures using the existing signature
identity and pi>3; it does not assume an unchecked embedding computation.

| Radicand d | Actual signed field discriminant |
| --- | --- |
| 1 | -4 |
| 2 | -8 |
| 3 | -3 |
| 7 | -7 |

Thus the actual fields in these four rows have class number one. These are
positive proofs, not the weaker assertion that they pass a necessary sieve.

The sufficient criterion stops here: d=11 has absolute discriminant 11,
outside the <=8 hypothesis. This is not evidence against its class number
being one. Phase33 now supplies the other five positive proofs. The complete
upper interval [1000000,700000000000) and full classification remain open.

## Proof and verification map

- [QuadraticDiscriminant](../../lean/TenthDiscriminant/QuadraticDiscriminant.lean):
  the general trace calculation, actual maximal-order transport and actual cutoff.
- [SmallPositiveClassNumber](../../lean/TenthDiscriminant/SmallPositiveClassNumber.lean):
  Minkowski criterion, four positive equalities and order/field controls.
- [Protocol](PHASE32_PROTOCOL.md), committed before proof edits;
  [results](PHASE32_RESULTS.json), including preserved development failures.

From `lean/`: `lake build`, `python verify_sources.py`, `python audit.py`,
`python negative_controls.py`, and
`lake env lean ../research/ender_radius_bridge/Phase32SignatureCheck.lean`.
Full-library and exact-head pinned CI status must accompany publication.
