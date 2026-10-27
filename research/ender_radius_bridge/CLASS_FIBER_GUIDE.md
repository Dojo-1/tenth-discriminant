# A fixed lattice for each ideal class

**Integrated into the production root; checked locally for actual number fields.** This closes the
ideal-to-element part of the representation bridge, without assuming
class number one. It does not yet produce a binary quadratic form.

An ideal records a divisibility condition inside the ring of integers.
Its class measures the obstruction to writing it as a single generated
ideal. Class number one removes that obstruction everywhere. For more
classes, we can instead cancel the obstruction one class at a time.

Fix a class C. Mathlib's existing Minkowski theorem supplies a nonzero
integral ideal J in the inverse class, with a bound on its ideal norm.
Choose this J once, before choosing a prime or an ideal to represent.

If I belongs to C, then the product IJ has trivial class. Thus some
nonzero integer z of the number field satisfies

    (z) = IJ.

Three useful facts now follow from the same equality:

1. **Location:** IJ is contained in J, so z belongs to the fixed lattice J.
2. **Size:** multiplicativity of ideal norm gives
   |N(z)| = N(I)*N(J).
3. **Recovery:** if another ideal I' has I'J=(z), cancellation of the
   nonzero ideal J gives I'=I.

The generator z need not be unique; units can change it. The recovered
ideal is unique. Negation preserves membership, the generated ideal and
norm magnitude; the Lean control checks that symmetry explicitly.

A residue map from the actual ring of integers onto ZMod p has kernel
ideal of norm p, by an existing proved quotient calculation. For p>0 its
kernel is nonzero, so the theorem supplies z in that class's fixed J with

    |N(z)| / N(J) = p.

The checked statement uses the equivalent product equality, with no division.
Its quantifiers matter: one J serves every residue map in the class.
This is what allows a future count of many primes in one lattice.

The later [actual coordinate/count bridge](IDEAL_COORDINATE_GUIDE.md) now
constructs an integral basis of J, proves the normalized norm's integer
coefficients and exact discriminant, and counts its off-axis element sets.
A small ideal norm alone still does not bound the leading coefficient of
an arbitrary basis. Quantitative basis control, principal-class calibration
and even-chart/field-parameter transport remain before a usable uniform B.

[Source](Phase66ClassFiber.lean) and [verification](PHASE66_VERIFICATION.md).
The original standalone source is frozen; its exact production transport has
a [combined local audit](PHASE67_VERIFICATION.md), with new-head CI still
required. No arithmetic count B,
new cutoff or classification is inferred.

The later standalone [odd-chart multiplicity theorem](RESIDUE_MULTIPLICITY_GUIDE.md)
constructs actual residue pairs and4*card(P) selected labelled elements locally.
The subsequent coordinate theorem fills the actual basis/form gap locally;
quantitative leading control and the even chart remain.
