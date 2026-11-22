# Phase386.1 — Rank-credit scaling is too small to settle Tao's constant

22 November 2026. This is a bound on the PARTICULAR first-layer
residue-rank method's certified contribution, not an upper bound on
the unknown total Smith valuation.

For n=RS and J=S, the Phase386 precision lemma guarantees, for each odd
inert p, an additional source-matched exponent at least

  a_p = max(0, S*(R-2*p^4))

beyond the original Frobenius 2F(p) factors. Actual source histograms
can sharpen this via nonzero count weights modulo p.

The universal class-count term is positive only if 2*p^4<R. Put
X=(R/2)^(1/4). If one credits EXACTLY the guaranteed a_p for eligible
primes p<=X (not the possibly larger true residual valuation), the
NORMALIZED CREDIT is bounded above:

  sum_{p<=X} a_p*log(p)/(R^2*S)
  <= sum_{p<=X} log(p)/R
  <= X*log(X)/R
  = O(R^(-3/4)*log R).

The elementary inequalities use only the count of integers <=X and
log monotonicity. This is emphatically NOT an upper bound on the
underlying actual residual Smith valuations or any general impossibility
theorem for improving the original tenth-discriminant cutoff.

At D=322^4+15, R=2,687,592,967, the basic p=3 normalized credit is
(R-162)*log(3)/R^2, about 4.0877e-10. With the actual 59 active source
classes it is (R-118)*log(3)/R^2. Even if every odd prime up to 191
were eligible, the sum of these rank-only credits is about 5.04e-8,
compared with the mainline 322^4 scalar margin 5.706e-6. This
all-primes comparison is deliberately overgenerous: many such primes
are split, and the chosen D is not assumed class-number-one.

Status P-paper: elementary rank/scale inequality relative to the
exact repository comparisonScale(R,S)=R^2*S. Status M: exact source
histograms and finite tests; decimal log displays are not proof
acceptance gates. Status H: stronger and potentially overlapping
Smith layers, complete original field-to-Gram review, and any
numeric improvement of Tao's bound.
