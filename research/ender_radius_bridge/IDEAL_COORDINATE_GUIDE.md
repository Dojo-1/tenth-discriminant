# From an actual ideal to the geometric count

**The odd-chart coordinate/count bridge is Lean-checked locally in production.**
For squarefree D congruent to3 modulo4 and every nonzero ideal J in the
actual ring of integers, the theorem constructs one integral basis e0,e1
and integer coefficients a,b,c, chosen before any point set or threshold:

    Norm(x*e0+y*e1) = N(J)*(a*x^2+b*x*y+c*y^2),
    a>0,  4ac-b^2=D.

Here N(J) is the actual positive ideal norm. The left side is the existing
algebraic norm. The basis comes from Mathlib's ideal-basis constructor.

## Why the coefficients are integers

The ideal norm divides the norm of every element of J. In the existing
rank-two norm chart, expand at e0, e1 and e0+e1. With n=N(J), the coefficients
are the integer quotients

    a=Norm(e0)/n,  c=Norm(e1)/n,
    b=(Norm(e0+e1)-Norm(e0)-Norm(e1))/n.

The first basis vector is nonzero and its imaginary quadratic norm is
positive, so a>0. No coefficient divisibility is assumed by the caller.

## Why the discriminant is exactly D

Write the ideal basis in the ambient maximal-order basis. Its coordinate
matrix M has |det M|=N(J), by the actual ideal index/norm theorem. Quadratic
substitution multiplies4ac-b^2 by(det M)^2. Dividing each coefficient by
N(J) divides that discriminant by N(J)^2. Those two factors cancel.

This is also the proof-design improvement: calculate with an arbitrary
basis first, then choose the actual basis once. The determinant proof never
unfolds the large chosen Smith-basis expression. The stopped Phase69 attempt
remains preserved; the new helper and composition have separate registrations.

## How actual elements enter the count

Basis coordinates are injective and reconstruct each actual element.
For a natural threshold t, a finite set with norm magnitude<=N(J)*t has
Q(x,y)<=t. When
its second coordinate is nonzero, the checked geometric theorem gives

    card(U) <= 2*pi*t/sqrt D + 4*sqrt(a*t/D).

The same constructed basis and form serve every U and t. Cardinality is
preserved by the coordinate map, so this counts actual elements of J.

## The remaining choice is mathematically significant

The area term is controlled by D; the boundary term remembers the chosen
basis through a. An arbitrary basis can have a very large a. For example,
replacing1 by1+k*omega in the D=7 unit basis leaves determinant1 and gives
leading norm1+k+2k^2. A uniform cutoff needs a proved controlled basis choice.
The generic chosen-basis theorem does not promise a=1. The subsequent
[principal-class theorem](PRINCIPAL_BASIS_GUIDE.md) now supplies that calibrated
basis locally, using a generator of the particular identity-class ideal.

The [controlled h<=2 class choice](CONTROLLED_CLASS_GUIDE.md) now supplies
a<=N(J)<=M(K) and a common per-class off-axis count locally. The generic
result above still needs that extra class-number hypothesis for this bound.
Class-wide usable arithmetic B, even chart and field-parameter transport
remain open. No new cutoff or classification.
[Verification and exact scope](PHASE72_VERIFICATION.md).
