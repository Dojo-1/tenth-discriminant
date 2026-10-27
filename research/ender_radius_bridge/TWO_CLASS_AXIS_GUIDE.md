# Why the two-class constant may survive the zero-row failure

**Lean checks two small parts:** prime factorization controls
the zero row; finite accounting explains the constant for at most two forms.
The nonzero-row geometry and the class-to-form representation count are
not Lean-checked by this attempt. No new class-number bound follows yet.

## The missing pair, and the pair that is absent

For Q(x,y)=ax²+bxy+cy², the row y=0 gives a*x². If this is prime p,
a=p and x=+1 or-1: a square factor of a prime must be a unit. The symmetry
x↦-x pairs the two possible points. Thus each form contributes at most two
prime points on its zero row. The principal form has a=1, so contributes
none: a square cannot be prime.

This explains the frozen Phase60 example a=3,b=1,c=1001. Both x=+-1
represent3, so a uniform per-form allowance of one point fails.

But a family of h forms containing the principal form needs at most
2(h-1) zero-row points. If h<=2, then2(h-1)<=h. After dividing by four
representations per split prime, the allowance is at most h/4. That is
the old two-class constant, obtained by different accounting. We do not
need to assert the false per-form estimate to recover this constant.

## The remaining paper route

Let D=4ac-b²>0, a>0 and t>=0. Completing the square gives

    4aQ(x,y)=(2ax+by)²+D y².

At Q<=t, |y|<=Y=2sqrt(at/D). At fixed y, the allowed x interval has width
ell(y)=sqrt(4at-Dy²)/a. An interval contains at most its length plus one
integers. On [0,Y], ell decreases, so the sum of widths on positive integer
rows is at most its integral from0 toY. Reflecting the rows gives

    number of points with y!=0
      <= 2 integral_0^Y ell(s) ds + 2 floor(Y)
      <= 2pi*t/sqrt(D) + 4sqrt(at/D).

This bounds all nonzero-row lattice points, hence also prime representations.
Add at most two zero-row prime points for each nonprincipal form and none
for the principal form. If the h forms are reduced, a<=sqrt(D/3). If four
total representations per unramified odd split prime have been justified,
the proposed aggregate result is

    N_split(t) <= h*pi*t/(2sqrt(D))
                 + h*(3D)^(-1/4)*sqrt(t) + (h-1)/2.

For h<=2 this implies the old constant h/4. For a larger h it does not;
the old generic-H claim still needs its own proof. The representation
multiplicity, reductions, finite row/integral estimate and exact interface
to the excluded-prime count B remain obligations. Ramified primes also
need a separate budget. No old numerical campaign is newly certified.

Lean targets: `PrimeAxisRepair.axis_prime_iff`, `primeAxis_card_le_two`,
`principal_axis_empty`, and conditional `two_class_accounting`.
[Verification](PHASE62_VERIFICATION.md) and [registration](PHASE62_PROTOCOL.md).
This research file is outside production CI.

Update: [Phase63](NONZERO_ROWS_GUIDE.md) checks the row-width count and
[Phase64](QUADRATIC_AREA_GUIDE.md) closes its area evaluation in production.
Arithmetic/class inputs remain open. This does not change the frozen
Phase62 source or its original verification scope.
