# Count the same prime lifts in two ways

The coherent-family theorem supplies four selected labelled points for
each eligible prime. The geometric theorem bounds the points lying in
each actual ideal-class lattice. This bridge counts the SAME selected
finite set in those two ways.

Ideal classes group nonzero ideals up to principal scaling; their number
is h(K).

Assume positive squarefree d congruent to 1 or 2 modulo 4, actual class
number h(K) at most two, and a finite set P of odd primes p<=t with
p not dividing d and -d a square modulo p. Here t is a natural number.

## Keep the class label until after slicing

Write a selected point as (C,z), with z in the actual ideal J_C. First
partition the selected set by C. Inside ONE slice, forgetting C loses
nothing: all labels are equal, so equality of z implies equality of pairs.
The formal slice is an actual finite subset of J_C, with exactly the
same cardinality and norm data as that labelled slice.

Forgetting labels before partitioning would be wrong. Two different
classes can carry the same underlying element. A control explicitly
checks that two labelled pairs may project to just one value.

Let A(t) be the common area term and B(t) the common boundary term:

    A(t)=2*pi*t/sqrt(4*d),
    B(t)=4*sqrt(M(K)*t/(4*d)).

M(K) remains the ACTUAL field's Minkowski bound, not a new chosen constant.
The count for class C is at most A+B plus zero for the identity class,
or two otherwise. Every selected point in its slice is prime-normalized;
its prime p<=t supplies exactly the norm bound required by that count.

## Sum the classes and divide by four

Class slices partition the selected set, whose size is 4*card(P). Thus

    4*card(P) <= h(K)*(A+B)+2*(h(K)-1).

The identity class is present and pays no axis error. For h=1 or 2,
2*(h-1)<=h. This gives the checked bounds

    card(P) <= h(K)/4*(A+B+1) <= (A+B+1)/2.

The second inequality uses h<=2 and nonnegativity of A+B+1. Its uniformity
is in the class number; M(K) still depends on the field. A negative control
shows why the same axis simplification fails at h=3: 4>3.

The caller supplies no chosen family, points, cardinality identity or
slice estimate. Those come from the actual coherent family and the
checked slice/count interfaces. [Original bounded attempt](PHASE97_VERIFICATION.md).
The accepted proof is now imported by the main library without mathematical
changes. [Integration and verification](PHASE98_VERIFICATION.md).

This actual prime-prefix count now feeds the integrated
[weighted determinant bridge](EVEN_WEIGHTED_BRIDGE_GUIDE.md). The actual
[Minkowski normalization and closed estimate](EVEN_NORMALIZATION_GUIDE.md)
are integrated unchanged at Phase102. The
[all-range even-chart contradiction](EVEN_TWO_CLASS_BOUND_GUIDE.md) is
integrated unchanged at Phase104; arbitrary-field transport remains open.
No full classification is asserted.
