# A field is more than its name

The former generator-existence gap is now supplied by the
[conjugation-based normalization](CONJUGATION_BRIDGE_GUIDE.md) under standard
degree-two/total-complexity hypotheses. This page explains the reusable
conditional dictionary used after that normalization.

The cutoff was proved for an actual rational quotient called
`ImaginaryQuadraticField d`. A caller may construct the same field using
a different type and generator. The new bridge proves that identification
from mathematical data, rather than asking the caller to supply an isomorphism.

## What the caller supplies

Let K be a number field, d a positive natural number, and a an element of K.
Supply two facts:

    a^2 + d = 0,       dimension of K over Q = 2.

The constructor gives a rational algebra equivalence from the canonical
field to K, and proves that its distinguished square root goes to a.
For squarefree d and actual class number one of K, the existing analytic
argument then gives both d < 100000000000 and an actual absolute field
discriminant of K below 100000000000. The cutoff itself is unchanged.

## Why the identification takes only three ideas

1. Evaluation at a sends the quotient's polynomial root to a. This is the
   universal property of adjoining a root of X^2+d.
2. For d > 0 the rational polynomial is irreducible: a rational square
   cannot equal a negative number. Its quotient is a field, so the map
   into K is injective.
3. Both rational vector spaces have dimension two. An injective linear
   map between them is onto, hence an algebra equivalence.

The class-number transport uses the actual maximal integer rings and
principality. Discriminant transport uses the actual number-field
discriminant. There is no replacement class-number definition or
coordinate-dependent discriminant.

## Transformations, and the guard they expose

Changing a to -a gives the other choice of square root. The constructed
map records that choice; the negative-root control at d=19 checks it.
Another control uses the native half-integral chart, whose generator w
satisfies w^2-w+5=0, and supplies a=2w-1.

Scaling a by n changes the equation to (na)^2+n^2*d=0 while leaving K
unchanged. Thus the equation alone does not make d a normalized field
parameter. In K=Q(i), take a=1000000*i and D=1000000000000. The root
equation, degree two and actual class number one hold, but D is not
squarefree and exceeds the proposed radicand bound. This fixed control
rejects dropping squarefreeness from the radicand statement. It does not
refute the actual discriminant bound: this field still has discriminant -4.

These are ordinary algebraic coordinate changes. Composing sign changes
and integer rescalings preserves the field but need not preserve the
squarefree label. Removing square factors is a substantive normalization step.

## The exact remaining bridge

This theorem starts with a specified positive squarefree root witness
and degree two. The new operator normalizer produces that witness for an
abstract degree-two totally-complex number field, so the composed actual
cutoff no longer assumes a presentation. No full classification is claimed.

The public constructor and both transported bounds are in
[QuadraticGeneratorBridge.lean](../../lean/TenthDiscriminant/QuadraticGeneratorBridge.lean).
The [protocol](PHASE46_PROTOCOL.md) and fixed
[control addendum](PHASE46_CONTROL_ADDENDUM.md) precede their execution.
The prior AI review covered the underlying cutoff, not this new constructor.
Local formal checks, publication-head CI and independent human review
remain distinct evidence.
