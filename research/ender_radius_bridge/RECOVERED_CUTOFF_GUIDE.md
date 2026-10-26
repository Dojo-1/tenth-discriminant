# Why recovering two small primes can lower the cutoff

This is the mathematical explanation of the fixed Phase54 proof attempt.
Its acceptance and verification status is recorded separately. Do not
read an unverified candidate calculation as a checked field theorem.

The determinant is constrained in two ways. Geometry bounds its size
from above. Arithmetic makes it divisible by a large product of prime
powers. A positive integer cannot be smaller than a positive divisor.
Thus a contradiction follows once the arithmetic lower bound exceeds
the geometric upper bound. Both sides refer to the same determinant.

Write u=log D and divide both budgets by R²S. The existing estimates are

    geometric upper <= .8u - .813,
    raw arithmetic lower >= .999997u - 5.820.

The raw estimate had dropped the exact prime3 and prime5 terms when
replacing a finite sum by a simpler uniform formula. Restoring them
does not assert new divisibility: it keeps more of the divisibility
already proved. Counting saturated rows gives a normalized recovery
of at least.06 in this rectangle. The new arithmetic estimate is

    recovered arithmetic lower >= .999997u - 5.760.

At u=24.8 this exceeds the upper estimate by exactly.0129256. At u=24.7
the same coarse comparison fails, by.0070741. These are rational checks
of these particular estimates, not an optimality claim.

## Why500^4 is the fixed endpoint

The existing radius proof works once D^(1/4)>=500. Choosing
D0=500^4=62500000000 retains that condition exactly. Moreover,
D0=2^8*5^12, so the existing rational log2 and log5 certificates prove
log D>=24.8 for every D>=D0. No floating-point logarithm is an input.

The rectangle remains R=floor(D/4), S=floor(R/25), J=S. The radius
remains ceil(.52D^.75). Integer division proves S>=100 and
25S<=R<=26S. The cell-area count, radius rounding, strict inertness
endpoint, positive scale, certified prime tail and upper error estimates
must all hold at D0. Checking these is what turns the short affine
calculation into a cutoff proof.

## From the determinant back to an actual field

For odd squarefree D congruent to3 modulo4, class number one supplies
the inert primes needed by the original arithmetic determinant proof.
The recovered budget stays below the production budget, and tail
antitonicity gives the correct direction when replacing the actual tail
by its certified upper bound. The strict budget inequality then rules
out class number one at and above D0.

The existing separate even-case argument handles the other squarefree
radicands. Conjugation and its anti-invariant projector construct a
positive squarefree generator for any actual totally complex degree-two
number field. A rational algebra equivalence transports its actual
class number and discriminant. This needs neither a supplied generator
nor the previously computed list of nine answers.

The dependency check must confirm that the new bound uses none of the
older large cutoffs or finite-answer classification. Importing a file
that contains those results is different from using those results in a
proof; the compiled constant closure is checked for that distinction.

This is a conservative improvement within the existing construction.
It does not prove the best possible constant, announce a full
classification, extend to higher class numbers, establish novelty, or
replace independent human mathematical review.
