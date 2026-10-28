# The bound belongs to the field, not its coordinates

Let K be any imaginary quadratic number field and let δ be the absolute
value of its actual field discriminant. The new standalone Lean theorem
proves:

**If K has at most two ideal classes, then δ < 2^52.**
For odd δ, the sharper bound δ < 2^50 remains available.
Equivalently, δ ≥ 2^52 forces at least three ideal classes.
An ideal class groups nonzero ideals that differ by multiplication by a
nonzero field element; class number counts these groups. Class number one
means every ideal is principal; at most two allows one additional class. Neither statement lists all such fields.

## Why the chart is not an extra assumption

Start with the field K, not a selected formula for it. Existing checked
algebra constructs a positive squarefree integer d and an element whose
square is -d. That element constructs an isomorphism Q(√(-d)) ≅ K.
The actual class number and actual discriminant survive this change of
presentation. The caller supplies neither the root nor the isomorphism.

There are two integral coordinate charts. If d is 3 modulo 4, the absolute
field discriminant is d. Otherwise squarefreeness leaves d equal to 1 or 2
modulo 4, and the absolute field discriminant is 4d. Thus an even δ selects
the even chart. Its already-proved class-number-at-most-two bound applies
to d, and transporting back gives δ < 4·2^50 = 2^52.

The factor four is structural: an index-two sublattice has four times the
discriminant of its containing lattice. This explains the square of two
in the checked chart formulas. The factor cannot be dropped when moving
from the even radicand bound to the field-discriminant bound.

For the all-parity theorem, split according to whether δ is even or odd.
The even branch uses the new transport; the odd branch explicitly uses
the existing arbitrary-field odd-discriminant theorem. This is composition
of two checked branches, not a new proof of the old odd cutoff.

## A short proof with visible joints

The [source](Phase107EvenFieldTwoClass.lean) has five main statements and
four arithmetic controls, with no new definitions. The main even transport
is a short construction of a root and field equivalence, followed by two
invariant identities and the existing canonical bound. The all-parity
conclusion is then a parity split. [Verification](PHASE107_VERIFICATION.md)
records the first full run, namespace audit and separate dependency checks.

This closes the arbitrary even-field transport gap at standalone proof
level. Integration and external CI for this new source remain to be done.
The older [coordinate/shift bridge](COORDINATE_BRIDGE_CURRENT.md) is a
separate result; its [CI timeout](PR37_CI_LIMIT_RECEIPT.md) remains preserved.

The class-number-one bound stays 50 billion. The new 2^52 bound concerns
the broader class-number-at-most-two problem; it is not an optimization of
that smaller bound. No novelty, optimality, completed independent human
review or full class-number classification is claimed.
