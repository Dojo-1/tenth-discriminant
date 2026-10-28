# The odd-chart two-class exclusion is now a theorem

**Integrated and checked locally in Lean:** if D is squarefree, D=3 mod4,
and D>=2^50, the actual quadratic field in this chart has class number
greater than two. Equivalently, a field in this chart with class number
at most two must have D<1125899906842624.

The chart is K=Q(theta), where theta^2-theta+(D+1)/4=0. Its actual field discriminant
is -D. This statement concerns the actual class group and discriminant;
it assumes no earlier cutoff or known list of fields. The even chart
and an arbitrary-field formulation remain separate obligations.

The earlier numerical test only suggested an endpoint. The new proof
covers EVERY larger D without reading the test output.

## How the local and global arguments meet

Local arithmetic supplies points in fixed ideal lattices, four labelled
lifts per admissible prime, and a bound for every prime-prefix count.
A positive summation-by-parts operator turns those counts into a weighted
loss on the SAME original derivative Gram determinant. Prime divisors
of D have their own logarithmic payment.

The actual Minkowski term is 2sqrt(D)/pi. Substitution gives an explicit
cost. Divide the comparison by the positive scale R^2*S, with the existing
choices R=floor(D/4), S=floor(R/25) and rho=ceil(.52*D^.75).
All the original radius, count, derivative and finite-prime guards remain.

Write u=log(D). The checked lower estimate is

    lower >= .999997*u - 5.739.

The checked geometric upper estimate, divisor payment and split-prime
loss together give

    upper <= .8*u - .813 + u/25 + .6.

For every D>=2^50, u>=34.65. The gap is therefore at least

    .159997*34.65 - 4.926 - .6 = .01789605 > 0.

The same determinant would have to satisfy both inequalities. That is
the contradiction excluding actual class number<=2 in this range.

## Why checking one endpoint now suffices

The conservative loss contains q(u)=2+u*(1+u), divided by the square root
or fourth root of D. In logarithmic coordinates these are
q(u)*exp(-u/2) and q(u)*exp(-u/4).

For a>=9 and v>=0, the quadratic exponential estimate proves

    q(a+v) <= q(a)*exp(v/4).

Thus both weighted expressions decrease as u grows. This is an exact
all-range inequality, not interpolation between numerical samples.
At the endpoint, log(2^50)<=35 and fourthRoot(2^50)>=5000 suffice to bound
the loss by 3/5 using rational arithmetic. No high-precision experiment
is a proof premise.

## Scope that must stay visible

This is a new locally integrated odd-chart bound for class number<=2.
It does not classify all such fields or cover the even chart. The separate
class-number-one field-discriminant cutoff remains 50 billion. We claim
neither sharpness nor novelty. External CI and independent human review of this addition remain outstanding.

[Exact integration verification](PHASE87_VERIFICATION.md) records the full-root
checks and exact source transport. The standalone record below preserves
all three proof attempts, unchanged statements and dependency checks.

Integration update (Phase87): the mathematical source, controls and reports
were transported exactly into the main root. The full local build,
input check and whole-library audit passed on their first invocations.
The [standalone record](PHASE86_VERIFICATION.md) retains both failed attempts.

The [actual-field bridge](ODD_FIELD_TWO_CLASS_GUIDE.md) now transports this
bound to ANY imaginary quadratic field with odd actual discriminant.
The even-discriminant branch remains open. See [Phase88](PHASE88_VERIFICATION.md).
