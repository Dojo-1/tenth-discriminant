# Why the arithmetic factor is squared

**The determinant is a squared volume in the observation space.** The field
lattice has rank two, but the observations live in a larger integer lattice:
one pair of coordinates for every original point and ordinary derivative.
This gives a second proof of the doubled exponent and explains what a better
geometric frame can change. It is exposition, not a new bound or theorem.

Let D>0 and let E have n=RS rows and m=2|Q|J columns. Its rows e_1,...,e_n are the
actual integer observations. The metric B repeats diag(2,2D), so the original
Gram is G=E B E^t. Keep the factor two and every observation slot.

## The whole frame as one object

The exterior product w=e_1 wedge ... wedge e_n records the oriented
n-dimensional volume. Its coordinates are all n-by-n minors of E. For
diagonal B with entries b_j, Cauchy--Binet says exactly

    det G = sum over |I|=n of (product of b_j for j in I) * det(E_I)^2.

Thus det G is the squared norm of w in the induced exterior metric. This
identity is integral: no square roots of B and no factorial denominators
are introduced. If m<n the sum and w vanish; if the rows are dependent the
same conclusion holds. For positive B, det G>0 precisely when w is nonzero.
The interpolation argument supplies that nonvanishing in the application.

## The prime factor before taking the norm

The [arithmetic derivation](TWO_SIDED_ARITHMETIC_GUIDE.md) constructs

    U_p E = Delta Ehat,   det U_p=1,   Delta=diag(p^k_i),   Ehat integral.

The difficult input is the integral quotient Ehat, obtained from ordinary
jets and the inert-prime congruence. An exterior argument does not eliminate
that obligation or the actual maximal-order class-number premise.

Taking the exterior product gives w(E)=w(U_p E)=p^F w(Ehat), where
F=sum k_i. Equivalently, EVERY maximal minor satisfies

    det(E_I) = p^F det(Ehat_I).

Substitute into Cauchy--Binet: every term contains p^(2F), and the remaining
weighted sum is an integer. This proves divisibility of the SAME det G,
without using the determinant of Delta K Delta as a shortcut. Applying
Cauchy--Binet to Ehat identifies that integer with det K, where
K=Ehat B Ehat^t is the original integral middle witness.

When the rows are independent, this has a lattice interpretation. The rows
of Ehat form a basis of their own lattice Lhat; the rows of U_p E span a
sublattice of index p^F. Gram determinants change by the SQUARE of that
index. Lhat need not be saturated in the ambient lattice. In dependent
cases that index argument is unavailable; the exterior identity still works.

## What a frame change actually improves

An integer row change T with det T=1 preserves w and its squared norm.
It can nevertheless change individual row lengths and their product.
Hadamard bounds the volume by that product: a better frame tightens the
ceiling around the same object. It does not shrink the determinant itself.

For the actual radial family, fix r-s and put u=ZW. Its rows are unpaired
monomials times powers of u. Centering translates u to u-a. This explains
T_a T_b=T_(a+b), its inverse, and zero-sum return of every jet and the Gram.
It is a linear action on observations, not multiplication of polynomials.
It supplies no new prime power. [Actual laws and controls](RADIAL_ACTION_CURRENT.md).

Changing ambient coordinates is different. If E'=E A, transport the metric
as B'=A^(-1) B A^(-t) to recover the whole original Gram. Changing coordinates
while silently fixing B changes the form being measured. Unimodularity also
matters for the integer lattice; an index-two order inclusion is not merely
an integer basis change.

Finally, reduction can kill the exterior vector: a nonzero real volume can
vanish modulo p. Unimodular frames preserve rank WITHIN that residue field,
not between the real and residue-field views. These are different transports.

## Evidence boundary

This is another derivation and representation by the same assistant, not
independent human peer review. [Phase131](PHASE131_PROTOCOL.md) preregisters
one exact comparator against eight sealed Gram cases and all 220 maximal
minors. It reconstructs zero-order observations through integer multiplication
matrices; it does not rerun the old all-order jet campaign. Finite checks
support the implementation, not the universal proof or a new cutoff.

The [sole invocation passed](PHASE131_VERIFICATION.md): eight fixed cases,
220 maximal minors, of which 24 are nonzero, in 0.265 seconds. These are
implementation checks; the universal argument is the exterior identity above.
