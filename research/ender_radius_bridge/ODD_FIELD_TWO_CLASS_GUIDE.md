# The bound now belongs to the actual field

The new theorem removes the caller's choice of coordinates. For any
imaginary quadratic number field K with odd absolute field discriminant
and class number at most two, Lean now proves

    abs(discriminant K) < 2^50.

The formal inputs are: K is a number field, has rational degree two,
has no real places, has class number<=2, and its ACTUAL absolute field
discriminant is odd. No generator, isomorphism, chart, squarefree radicand
or numerical margin is supplied by the caller. Even discriminants remain
an open branch of this extension.

## The invariant that makes transport legitimate

A field isomorphism carries algebraic integers to algebraic integers.
It therefore gives an isomorphism of the full rings of integers.

That ring isomorphism carries nonzero ideals to nonzero ideals. It also
preserves the relation defining an ideal class: if x*I=y*J with x,y nonzero,
the same relation holds after mapping every object through the isomorphism.
Mapping back recovers the original ideal class.

Lean constructs this bijection of actual ideal classes and proves that
every representative gives the same class-map value. A chosen integral
representative cannot change the result. Taking finite cardinalities gives

    classNumber(K) = classNumber(L)

for ANY rational field isomorphism K≃L. This is the reusable local lemma.
It extends the earlier class-number-one convenience interface to equality
of class numbers themselves. Its proof uses no PID assumption or earlier
class-number-one bound. No novelty or Mathlib acceptance is claimed.

## How the actual discriminant selects the chart

The existing field-representation theorem internally produces a positive
squarefree d and a square root of -d in K. Degree two then identifies the
canonical quadratic field with K.

The already checked maximal integral bases compute the ACTUAL field
discriminant: -d in the odd chart, -4d in the even chart. If its absolute
value is odd, the -4d branch is impossible. The proof therefore derives
the odd chart rather than asking the caller to assume it.

Class-number equality now transfers the hypothesis<=2 to that chart.
The [all-range determinant comparison](ODD_TWO_CLASS_BOUND_GUIDE.md)
gives d<2^50, and actual discriminant preservation gives the stated bound
for K itself. Every overlap concerns the same field, integer ring and
class group.

## Remaining boundary

This closes arbitrary-field transport for ODD actual discriminants.
The even-discriminant h<=2 argument still needs proof. The separate
class-number-one field bound remains 50 billion. There is no full
classification, optimality claim or completed independent human review.
Argon's new review is still underway and has not been assessed yet.

[Exact verification](PHASE88_VERIFICATION.md) preserves the failed identity
controls, the passing repair and the integration/dependency checks.
