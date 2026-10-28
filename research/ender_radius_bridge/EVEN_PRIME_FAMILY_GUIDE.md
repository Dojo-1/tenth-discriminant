# Four prime lifts, counted in one fixed family of lattices

The earlier theorem counts elements in each controlled ideal lattice.
The next question is whether actual split primes supply distinct elements
in those SAME lattices. A family chosen afresh for each prime would not
justify adding the counts.

## The two roots give two actual ideals

For an odd prime p not dividing d, a root z of z^2=-d modulo p gives a
ring map from the full even integer ring Z[sqrt(-d)] to Z/pZ: send the
generator sqrt(-d) to z. The checked maximal-order equivalence ensures
this is the actual ring of integers, not a convenient suborder.
The map is onto and its actual kernel ideal has norm p.

The other root is -z. Since p is odd and does not divide d, z is nonzero
and z differs from -z. The resulting kernel ideals are distinct. A
concrete witness is the generator minus an integer lift of z: one map
kills it and the other does not. Merely saying the two maps differ would
not be enough without this kernel argument.

## Two ideals become four points

Choose one bounded representative J_C and controlled basis for every
actual ideal class, BEFORE any finite set of primes is supplied. Actual
class number at most two makes each class its own inverse. Multiplying a
prime ideal I in class C by J_C therefore gives a principal ideal.
Its generator lies in J_C and has norm magnitude p*N(J_C).

Each of the two distinct prime ideals yields a generator and its negative.
Those four class-labelled points are distinct. Their classes may coincide;
we do not assume distinct ideals have distinct ideal classes. Instead,
the exact recovery identity (z)=I*J_C shows that equal generators, even
up to sign, would recover the same prime ideal, a contradiction.

Different primes cannot collide either: a labelled point's norm divided
by the positive N(J_C) recovers its prime. Thus a finite admissible set P
gives exactly4*card(P) selected distinct points in the fixed family.
This is a selected set of representatives, not an assertion that there
are exactly four representations in total.

## The overlap with the geometric count

The family carries the calibrated per-class norm form and full finite
prime-normalized count proved earlier. Every selected point belongs to
that family's actual J_C and has the required norm. Arithmetic lifts and
geometric counts therefore refer to the same lattices. The remaining
class-slice sum and weighted loss must still be proved explicitly.

Controls retain the successful Gaussian pair (d=1,p=5), collapse of the
two roots in characteristic two, collapse at a ramified zero root,
the zero-modulus guard and the empty finite prime set.
[Exact attempt and verification](PHASE95_VERIFICATION.md).

This is the coherent prime-family bridge. It is not yet a weighted
inequality for the original Gram, an even cutoff or a full classification.
Actual Minkowski normalization and the parameter/discriminant factor of
four must also be matched before claiming a final contradiction.
