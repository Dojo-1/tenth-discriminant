# Phase320-B — matched index-two suborder controls for D187 and D203

Date: 14 November 2026. This is a supplemental preregistration to Phase320, committed before implementing or measuring the additional D187/D203 even-order arms. It does not revise Phase320-A's already frozen D163/D187/D203 full-maximal-order arms.

## Question

The full maximal-order experiment changes both the field and the finite support. D163 already has a source-matched control: the 109-point even-coordinate suborder versus the 225-point full maximal order. Repeat that comparison for D187 and D203, so the class-group and support variables are not conflated.

## Frozen coordinate square

For every (Din{187,203}), use
[
B_D=egin{pmatrix}2&1\1&(D+1)/2end{pmatrix},quad
T=egin{pmatrix}1&-1\0&2end{pmatrix},quad
(x,y)mapsto(a,b)=(x-y,2y).
]
Verify exactly
[
T^T B_D T=operatorname{diag}(2,2D),qquad
N(a+bomega)=x^2+Dy^2.
]
The determinant of T is 2, a 5-adic unit, but the finite norm-ball support of the suborder is only the even-b subset of the maximal-order norm ball. Do not identify the supports.

## Arms

For each D=187 and D=203, compare:
1. common diagnostic cutoff (ho=21), (R=40,J=1);
2. native row/jet dimensions and native (ho(D)): D187 ((23,46,1)), D203 ((24,50,2)).

Within each arm, compare the full maximal-order support with its exact even-b index-two suborder. Use the same original row labels and unchanged trace pairing on both sides. The local second-wild lift and radical-normal computations are repeated independently on each support.

## Exact checks

- Independently enumerate the original (mathbb Z[sqrt{-D}]) norm ball and map it by T; it must equal the even-b subset point-for-point.
- Check exact norm preservation and the Gram congruence under T for every arm.
- Keep all 5-divisible points separate.
- Repeat all five local norm-preserving lifts per signed 5-unit site, first-wild-digit preservation, differential linearity, full symmetric span and radical-normal image.
- Report support size, residue classes, primitive rank/radical, first radical Smith layer and local normal image for both suborder and maximal order.

## Evidence boundary

This is a finite source-support comparison in two nontrivial class groups. It does not identify local isomorphism with equality of samples, does not transfer D163 global prime characters, and does not prove a class-number-to-valuation theorem. Any unexpected equality or difference is reported as measured; no rank is assumed from D163.
