# The even lattice: where the factor of four belongs

The odd and even cases describe the same kind of mathematical object,
but their full rings of integers use different coordinates. For positive
squarefree d congruent to1 or2 modulo4, the full ring is Z[sqrt(-d)].
Its ordinary norm is x^2+d*y^2 and its field discriminant is -4d.
A radius or counting formula using d where the field discriminant is
required would describe the wrong scale.

## One ideal, one form, every finite set

Take ANY actual nonzero integral ideal J. Its lattice has an integer
basis e0,e1. The new statement constructs integers a,b,c such that

    norm(x*e0+y*e1) = N(J)*(a*x^2+b*x*y+c*y^2),
    a>0,                 4*a*c-b^2=4*d.

Why are a,b,c integers? Every element of J has norm divisible by the
ideal norm N(J). Apply this to e0,e1 and e0+e1; the third value determines
the mixed coefficient. Why is the discriminant exactly4d? The determinant
of the basis-coordinate matrix has absolute value N(J). Changing basis
multiplies the norm-form discriminant by its square; division of the
three coefficients by N(J) cancels that same square.

This is the bridge between ideal arithmetic and the ellipse's geometry.
It uses the actual maximal ring of integers and an actual ideal basis.
It assumes no class-number bound or principal-ideal property.

## Counting the same points

If a finite set U in J has norm magnitude at most N(J)*t, its coordinates
lie in the ellipse a*x^2+b*x*y+c*y^2<=t. Distinct elements have distinct
coordinates. Away from y=0, the previously proved row-count theorem gives

    card(U) <= 2*pi*t/sqrt(4*d) + 4*sqrt(a*t/(4*d)).

The basis and coefficients are chosen BEFORE U and t: one lattice chart
serves all finite sets and thresholds. The first term is the ellipse's
area; the second pays for counting integer rows. The y!=0 condition is
essential: the origin alone disproves the zero-threshold bound without it.
The separate axis count must be supplied when counting all prime lifts.

The controls check x^2+y^2 in the Gaussian case and the sheared form
x^2+2xy+3y^2 for d=2. Its discriminant magnitude is8, not2. The shear changes
the formula and keeps its discriminant: it is a reversible coordinate
operator, not a change of arithmetic object.

The accepted statement, proofs and controls are now integrated unchanged
into the main Lean library. Full local build/input/whole-audit checks pass.
[Exact integration record](PHASE90_VERIFICATION.md). This is separate from
external CI or human review.

## What this does and does not close

This is the even-case local lattice bridge. To obtain an even-discriminant
h<=2 cutoff, we still need controlled bases across ideal classes, the
prime lifts and full weighted budget, and a comparison on the SAME
original positive integer determinant. No new even cutoff follows just
from this lattice theorem.

The [odd actual-field bound](ODD_FIELD_TWO_CLASS_GUIDE.md) remains a separate
accepted local result. The class-number-one field bound remains50billion.
[Exact verification](PHASE89_VERIFICATION.md) records the bounded attempt,
including its failure and repair. External CI and independent human review
for this extension remain open; Argon's report has not arrived.
