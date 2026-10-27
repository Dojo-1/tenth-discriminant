# Put the primitive element first

**Checked locally in Lean:** a primitive element of an actual rank-two
integer lattice can be the first vector of an actual integral basis.
For the actual ideal norm form, the controlled norm bound then gives
the leading-coefficient bound 0<a<=N(J).

Write the element's coordinates as (u,v), with gcd(u,v)=1. Bezout gives
integers A,B satisfying u*A+v*B=1. The matrix

    [ u  -B ]
    [ v   A ]

has determinant one. Its inverse has integer entries. Therefore this
operator maps the lattice bijectively to itself: no lattice points are
lost, added or replaced. Its first column is the chosen element.

The proof uses Mathlib's matrix-to-linear-equivalence construction and
maps the existing basis through it. This constructs a basis of the
actual module, rather than stopping at a formal determinant identity.
The same construction works on the actual ideal as an integer module.

For that new ideal basis, the already checked arithmetic theorem supplies
integer coefficients a,b,c, a>0, exact discriminant D and

    Norm(x*e0+y*e1) = N(J)*(a*x^2+b*x*y+c*y^2).

At (1,0), the first vector is z, so Norm(z)=N(J)*a. If its norm magnitude
is at most N(J)^2, cancellation of the positive N(J) gives a<=N(J).
No coefficient bound or norm form is supplied as an extra premise.

The [least-norm theorem](LEAST_NORM_GUIDE.md) provides a vector with
exactly the needed primitivity and norm bound, in each bounded actual
class representative under h<=2. Its composition with this interface
still needs a separate check and production integration. We do not
claim an end-to-end class-family coefficient theorem from two standalone
files merely because their mathematical interfaces match.

Four controls check an actual basis beginning with (2,3), the failure
of the zero and (4,6) primitive guards, and an existing first basis vector.
The failed first proof assembly and passing second run are preserved.
[Exact verification](PHASE77_VERIFICATION.md).

The [stopped earlier attempt](CONTROLLED_BASIS_ATTEMPT.md) is unchanged.
This new proof uses the existing Mathlib lattice operator and the
separately checked primitivity interface. Class-wide counting, the even
chart, field transport and a new cutoff remain open. Outside production CI.
