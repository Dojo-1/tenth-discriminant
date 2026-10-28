# The even-chart contradiction, in one page

For K=Q(sqrt(-d)), with d positive, squarefree and d=1 or 2 modulo 4,
Lean now proves

    class number(K)<=2  =>  d<2^50,
    absolute field discriminant(K)<4*2^50=2^52.

This is a checked standalone theorem about the actual even quadratic
field. [Exact statements and evidence](PHASE103_VERIFICATION.md).
The discriminant is 4*d, so the two bounds must not be interchanged.

## Where the contradiction comes from

Assume d>=2^50 and class number at most two. Put u=log(d). Choose the
already checked dimensions and radius

    R=floor(d/4), S=floor(R/25), rho=ceil((13/25)*d^(3/4)).

They satisfy the radius, positivity and counting guards throughout this
range. Normalize every term by the SAME positive scale N=R^2*S.

Let A be the total odd-prime weight and H the logarithmic product of
diagonal entries of the original ellipse Gram. Three checked estimates
then suffice:

    Arithmetic:   A/N >= (999997/1000000)*u - 5739/1000.
    Geometry:     H/N <= (4/5)*u - 813/1000.
    Lost factors: loss/N <= 3/5 + u/25.

The [weighted bridge](EVEN_WEIGHTED_BRIDGE_GUIDE.md) says A<=H+loss.
The [actual even normalization](EVEN_NORMALIZATION_GUIDE.md) supplies the
closed loss cost; its scalar domination permits the same all-range
numerical estimate. Primes dividing d are included in the u/25 term.
The arithmetic lower bound comes from the exact prime-mass/factorial
bridge, not from class number one or a sampled numerical experiment.

## Why these inequalities cannot coexist

For d>=2^50, the checked logarithmic bound gives u>=693/20. At that
endpoint, arithmetic exceeds geometry plus losses by

    (159997/1000000)*(693/20) - 4926/1000 - 3/5
      = 1789605/100000000 > 0.

The difference increases with u. Thus the lower bound exceeds the upper
bound for EVERY d in the range. The assumed class number<=2 is impossible.
No known list of small answers or old odd-field cutoff is used.

The separate class-number-one bound remains 50 billion. The new result
extends the class-number-at-most-two track in the even chart; no novelty
or optimality is claimed. The first full attempt checked the contradiction
but failed in an absolute-value wrapper; the repaired full run checks all
three statements, with both runs preserved.

Integration, transport to arbitrary field types, new external CI and
independent human review remain open. This supplies a cutoff, not a
full class-number classification.
