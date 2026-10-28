# Move the observables with the points

The transport question now has a checked translation instance. Over ANY
commutative ring, define T_(a,b)F by the actual polynomial F(Z-a,W-b).
Lean proves that these operators compose by adding(a,b), have inverses,
commute with coefficient ring maps and commute with every ordinary
Z derivative. W is held independent throughout differentiation.

The central identity is

    (∂_Z^j T_(a,b)F)(z+a,w+b) = (∂_Z^j F)(z,w).

For complex sampling, take b=conj(a) and w=conj(z). Translating both the
points and their polynomial observables leaves every sampled jet unchanged.
The proof derives this from actual polynomial differentiation and
specialization. It does not define a shifted derivative row and assume
that row is the derivative of a translated polynomial.

## The integer has not been replaced

At translated lattice points, each transported monomial jet equals the
complex image of the ORIGINAL integer-pair derivative row. Summing their
real trace products gives the same original integer Gram entry by entry,
including row order and factor two. Consequently the determinant, its
proved prime-power divisor and its guarded positivity all concern the
same positive integer. No replacement Hermitian determinant is used.

The final theorem assumes positive D, the original R,S,J and strict
point-count guards, and an odd prime with -D nonsquare modulo that prime.
It supplies no compatibility, jet-injectivity or divisibility premise.
[Source and explicit guards](Phase110PassiveTransport.lean).

## Why24and60 are both correct

Use the SAME three shifted points from our earlier vertical-translation
example. Fixed monomials1,z give determinant60. Transporting the
observables as1,z-i gives determinant24, equal to the original24.
Both conclusions are now checked together. The old active-shift
counterexample is preserved; the passive action answers a different,
fully specified question.

Other checked controls retain the real/complex rank distinction (real
determinant4 versus Hermitian determinant0), ordinary third derivative6
rather than divided derivative1, and W as an independent parameter.

## Equivalence and reduction are different transports

An invertible compatible transport preserves the sampled construction.
A ring map such as integral reduction preserves the proved polynomial
identities but need not preserve injectivity or rank. Kernel growth in a
residue fiber is arithmetic information; it supplies local divisibility.
The common integral model relates complex and residue views. We do not
assert a unital ring map from the complex numbers to a finite field.

A passive chart change alone therefore lowers no cutoff: it preserves the
obstruction. A better bound still needs a sharper estimate or a genuinely
new admissible family of observables, with its arithmetic bridge proved.
Computational hardness additionally needs bounded-cost, witness-preserving
transports; the new algebraic identities do not prove those cost bounds.

[Verification and preserved failures](PHASE110_VERIFICATION.md):20public
statements, four definitions, standard three axioms. Standalone only;
production integration and external CI for this addition remain open.
The class-number-one cutoff stays50billion. No classification or optimality
claim. [Broader invariant framework](TRANSPORT_INVARIANTS_GUIDE.md).
