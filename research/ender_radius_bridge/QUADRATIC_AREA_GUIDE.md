# A checked count for quadratic ellipses

**The geometric estimate is now in the production Lean library.**
Let Q(x,y)=ax²+bxy+cy², with a>0, D=4ac-b²>0 and t>=0. For any finite
collection U of integer pairs with Q<=t and y!=0, Lean proves

    #U <= 2*pi*t/sqrt(D) + 4*sqrt(a*t/D).

The first term is the ellipse area. The second pays for integer rounding
on its nonzero rows. This is a count of actual points, without a supplied
count or area premise.

## One proof, three transformations

**Slice.** Completing the square confines x on row y to an interval of
width w(y)=sqrt(4at-Dy²)/a. An interval contains at most its length plus
one integers. The positive row widths decrease, so their sum is bounded
by the integral up to Y=sqrt(4at/D); rounding costs at mostY.

**Reflect.** Simultaneous negation(x,y)->(-x,-y) preserves Q, including
the mixed term bxy. It carries negative rows to positive rows. This gives
#U<=2 integral_0^Y w+2Y and works for sheared ellipses too.

**Scale.** Write C=4at. Then D Y²=C and
w(Yu)=sqrt(C)/a * sqrt(1-u²). Mathlib's exact unit-semicircle integral
evaluates the full width integral; symmetry halves it. Consequently
2 integral_0^Y w=2pi*t/sqrt(D), while2Y=4sqrt(at/D). The scaling identity
also holds at Y=0, so the zero threshold belongs to the same proof.

The unit-circle, a sheared circle and zero-threshold controls compile.
The origin at t=0 still refutes dropping y!=0. For prime representations,
the [separate axis argument](TWO_CLASS_AXIS_GUIDE.md) charges at most two
zero-row points per form and none when its leading coefficient is1.

## Where the research now stands

The geometric count is closed. To obtain a usable split-prime bound B,
we still need the actual ideal-class/form dictionary, the representation
multiplicity and ramified-prime accounting. The [count-to-loss theorem](COUNT_TO_LOSS_GUIDE.md)
then transfers B to the original determinant argument. No new B, numerical
cutoff or class-number classification follows from the geometry alone.
The existing50-billion class-number-one cutoff is unchanged.

Public theorem: `TenthDiscriminant.QuadraticRows.off_axis_area_bound`.
[Production proof](../../lean/TenthDiscriminant/QuadraticAreaCount.lean) and
[exact verification scope](PHASE64_VERIFICATION.md). No new independent
semantic review or Mathlib acceptance is claimed.
