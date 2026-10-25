# What would a substantially smaller cutoff require?

The conjugation bridge removes a field-presentation assumption. It does not
alter the determinant estimates. The current analytic comparison still has
two one-sided bounds, with u=log D:

    lower >= .999997*u - 5.820
    upper <= .8*u - .813.

Here lower and upper are the prime-divisibility and size budgets normalized
by R^2*S for the same positive integer determinant. Contradiction requires
the lower bound to exceed the upper bound.

Subtracting the displayed affine expressions gives exactly

    gap(u) = (199997/1000000)*u - 5007/1000.

Their unique crossing is u=5007000/199997, strictly between 25 and 25.3.
At 25 the gap is -283/40000; at 25.3 it is 529241/10000000.
The existing Lean proof uses the positive latter control and checks
log D>=25.3 for D>=100 billion, together with all geometric and rounding
guards. The [single preregistered rational diagnostic](PHASE48_RESULTS.json)
confirms those identities with exact fractions. It supplies no new cutoff.

This explains the next research choice. Better endpoint arithmetic might
reduce the gap between the crossing and 25.3, but cannot make these same
affine expressions separate at u<=5007000/199997. A larger improvement
requires stronger estimates somewhere in their derivation: a larger
prime-divisibility lower budget, a smaller determinant upper budget, or
both. It could still use the same original determinant. The overlapping
envelopes do not show that its actual budgets overlap, and do not refute
the underlying method.

The frozen external comparison identifies stronger Frobenius/factorial
valuation gains and a different auxiliary-prime nonvanishing route as
possible research directions. Neither is imported by this diagnostic.
The external constructions use a minor norm rather than our factor-two
trace-Gram determinant; transferring their constants requires proving
compatibility, not substituting numbers.

The next bounded proof-port attempt should therefore specify the exact
integer or module, the stronger inequality to be proved, its guards and a
failure control before execution. We have not preregistered or executed
that larger attempt here. No threshold, classification, novelty, optimality
or higher-class-number claim follows from this accounting.
