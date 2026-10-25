# Conjugation organizes the proof

The new cutoff theorem applies to an arbitrary number field K with rational
degree two, no real places, and actual class number one. Its actual absolute
field discriminant is below100000000000. The caller supplies neither a
square root nor an identification with a named quotient field.

The proof begins with operators. The existing large jet module and integer
Gram determinant remain intact; their dimension is R*S, not two. Degree
two is used at one specific field-theoretic step: identifying the fixed
field with Q.

## The harmonic decomposition

Complex conjugation transports through an embedding into an automorphism
sigma of K. It is nonidentity and squares to the identity. A quadratic
Galois group has only two elements, so the nonidentity operator is unique:
choosing a different complex embedding cannot choose a different sigma.

Its anti-invariant projection is

    Pminus(x) = (x-sigma(x))/2.

This is sign-character averaging for the group with two elements. It
requires no Euclidean metric. Lean proves that sigma(Pminus(x))=-Pminus(x)
and that applying Pminus twice gives the same result as applying it once.
Those two operator laws have no degree-two hypothesis: they hold for any
involution on any number field. They are not a new analytic estimate.

Because sigma is nonidentity, some nonzero u lies in this anti-invariant
part. Multiplication sends u*u back to the invariant part: (-u)*(-u)=u*u.
Uniqueness of the nonidentity automorphism makes this square fixed by the
whole quadratic Galois group. Its fixed field is Q.

## From an invariant to a normalized label

The embedding commutes with the two conjugations:

    phi(sigma(x)) = conjugate(phi(x)).

Thus phi(u) has zero real part. It is nonzero, so its square is strictly
negative. We have obtained a negative rational square class from the
operator structure, not from an arbitrarily chosen quadratic equation.

Write u^2=-q with q positive. Choose a positive squarefree representative
of q modulo rational squares; its negative represents the original class.
Clearing the rational denominator produces an integer D and a root z with z^2+D=0. Write
D=b^2*d, with d positive and squarefree, and replace z by z/b. The
[previous field dictionary](GENERATOR_BRIDGE_GUIDE.md) constructs the
canonical-field equivalence from this root and degree two. Actual maximal
integer rings, class number and field discriminant transport through it.
The existing100-billion analytic bound then applies.

The field normalization itself uses no class-number or cutoff input.
Fresh compiled input checks verify that separation. It proves existence
of a suitable representative, not a new computational uniqueness API.

## Keep the operators' types visible

| Operator | Acts on | Preserved information |
|---|---|---|
| sigma and Pminus | The number field K | Conjugation structure and its invariant/anti-invariant parts |
| Rational rescaling of a generator | A presentation of the same field | The rational square class; the raw radicand label can change |
| Integer unitriangular basis change U_p | The R*S polynomial-row module | Integer determinant under G -> U_p*G*transpose(U_p) |
| Reduction modulo an odd inert prime | The original integer observations | Frobenius relations and prime-power divisibility; samples are not deduplicated |
| Complex embedding and trace pairing | The same observed jets | The real positive Gram and its exact integer determinant |

These operators do not all act on the same space. Compose them only through
the appropriate evaluation or base-change maps. In particular, exchanging
the formal variables Z and W need not preserve a thin R-by-S rectangle;
the ordinary Z-derivative convention still keeps W fixed.

The inherited local relation z^p=bar(z) and the new global conjugation
picture express related involutions. The checked result composes the
field normalization with the existing cutoff. It does not export a new
theorem identifying every actual-field residue Frobenius with sigma.

At the end, log(det G) is a measurement of the preserved positive integer
determinant. It turns prime powers into an additive lower budget and
Hadamard into an upper budget. The scalar comparison measures the operator
construction; it does not replace the large module or its arithmetic.

## Checked scope

[ImaginaryQuadraticRepresentation.lean](../../lean/TenthDiscriminant/ImaginaryQuadraticRepresentation.lean)
proves the operator laws, squarefree-generator existence and the new actual
field-discriminant bound. Standard hypotheses are NumberField K,
NumberField.IsTotallyComplex K, rational degree two and actual class number
one; no supplied-root or isomorphism premise remains on that bound.

The original coordinate-centered plan was unexecuted. The
[user-directed operator route](PHASE47_OPERATOR_ROUTE.md) was registered
before any Phase47 source or attempt. Both later elaboration failures are
preserved; the statements and resource caps were unchanged.

Local full build/input/axiom checks and exact publication-head CI are
separate records. The prior bounded AI review predates this new proof;
independent human semantic review remains open. The analytic constant is
unchanged. No full-classification, novelty, optimality, higher-class-number,
merge or Tao-submission claim follows from this addition.
