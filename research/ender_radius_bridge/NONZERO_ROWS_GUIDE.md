# Count the strips, then pair them

**Lean now bounds the actual number of off-axis integer points by an
explicit row-width integral. The integral's closed area formula remains
a separate formal step.** No class-number cutoff changes.

Take a positive-definite real form Q(x,y)=ax²+bxy+cy², with a>0,
D=4ac-b²>0 and t>=0. Let U be any finite set of integer pairs satisfying
Q<=t and y!=0. Define

    Y = sqrt(4at/D),       w(s) = sqrt(4at-Ds²)/a.

The checked conclusion is

    #U <= 2 integral_0^Y w(s) ds + 2Y.

## Why this is the count we need

Completing the square gives4aQ=(2ax+by)²+D y². It limits the height to
Y. At a fixed integer height y, it places x in an interval of length w(y).
A real interval contains at most its length plus one integers: the first
and last integer already leave at least one unit of space per intervening
step. This argument handles a shifted interval, so the shear from b
causes no uncharged rounding error.

Group the positive-height points by their integer row. There are at most
floor(Y) rows. The width decreases as the height rises, so its right-end
sum lies below its integral from0 tofloor(Y). Nonnegative remaining width
extends that integral toY; the rounding cost is at mostY.

Now apply the actual reflection sigma(x,y)=(-x,-y). It is injective,
sigma²=id, and preserves Q. It pairs the negative half-plane with another
positive-height count. Adding the two bounds proves the displayed result.
The zero row is deliberately absent. At t=0, the origin alone would make
the right side zero but the count one; Lean checks that guard falsifier.
The two unit-circle points(0,+-1) and empty-input controls also compile.

## What remains

The usual semicircle calculation gives integral_0^Y w=pi*t/sqrt(D),
leading to area2pi*t/sqrt(D) plus4sqrt(at/D). That evaluation is described
here mathematically, but **not proved by this Lean file**. The class/form
dictionary, four representations per split prime and ramified-prime
budget are also still needed before supplying the arithmetic B to the
[determinant loss theorem](COUNT_TO_LOSS_GUIDE.md).

The [zero-row repair](TWO_CLASS_AXIS_GUIDE.md) then accounts for the missing
axis. These are complementary estimates of the same norm forms; no Gram
matrix, derivative or normalization was replaced.

Lean entry point: `TenthDiscriminant.NonzeroRows.off_axis_count`.
[Verification and preserved first attempt](PHASE63_VERIFICATION.md).
The research file is outside production CI.
