# The 48-billion contradiction

**Status: the full actual-field 48-billion theorem is integrated unchanged.**
The complete local build and audits pass. Exact-head CI/publication status
is versioned in the [current scope](RADIAL_CUTOFF_CURRENT.md). [Checked geometric estimate](RADIAL_DETERMINANT_GUIDE.md).

We want to squeeze one positive integer from two directions. It is the
determinant of the original integer matrix of polynomial observations and
ordinary derivatives at lattice points inside an ellipse.

**Arithmetic makes it large.** If the field has class number one, each
eligible prime forces a power of that prime to divide this determinant.
Different primes are coprime, so their powers multiply into one divisor.
Positivity then makes the divisor no larger than the determinant. Taking
logarithms turns that product into a sum; the factorial argument bounds
the sum from below. The primes 3 and 5 recover some deliberately unused
weight, without inventing new divisibility.

**The radial observations make its ceiling smaller.** We change the
polynomial rows by an integer matrix of determinant 1. This preserves the
original determinant and all its divisors. Centering the radial quantity
ZW improves its uniform geometric bound even after every derivative term
and the integer-rounding error are included. The completed geometric
estimate still refers to the same original determinant.

Normalize both estimates by the same positive scale R^2*S. The checked
comparison is

    0.999997 log D - 5.739 <= log(det G)/(R^2*S)
                           <= 0.8 log D - 0.823.

The lower expression grows faster. At the fixed endpoint 48,000,000,000,
exact rational logarithm certificates give log D>=24.5813. The
lower expression then exceeds the upper by at least0.0001862561. This
small positive margin is why none of the rounding or radius guards can
be discarded. The coarser input 24.58 is insufficient and remains a
negative control; there is no retrospective endpoint tuning.

The final step must concern a field's **actual discriminant**, not just
a convenient radicand. In the odd chart these agree in absolute value;
the even chart has a factor 4. The elementary even-case argument leaves
radicands 1 and 2, whose actual absolute discriminants are 4 and 8. A field
equivalence then carries the result to an arbitrary imaginary quadratic
number field, without requiring the caller to provide a generator.

The checked theorem is: every imaginary quadratic number field of class
number one has actual absolute discriminant below 48 billion. This is a
cutoff, not the full classification. It assumes no earlier cutoff or list
of nine fields. Existing valuation and field-equivalence lemmas are
explicit dependencies; old cutoff/classification conclusions are excluded.

Unchanged library integration and its complete local checks now pass.
Pinned CI/publication is versioned at the exact source head. Independent human
semantic review remains open. [Exact verification](PHASE120_VERIFICATION.md) · [Registered scope](PHASE120_PROTOCOL.md).
