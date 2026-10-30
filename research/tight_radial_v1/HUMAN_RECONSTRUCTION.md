# A tenth-discriminant bound through one original integer

This is a **reader-facing reconstruction of a proposed Phase133 improvement**.
It is not a claim that the new Lean proof has passed. The established theorem
on main prior to this cycle is a 47.1-billion actual-field bound, which has
a successful exact-head root audit. Its mathematical premises are inherited.

The crucial distinction is that the actual absolute discriminant D of an
imaginary quadratic field is **not** the determinant constructed below.

## Build the object only once

Use the original quadratic-order integer lattice and evaluate the monomials
Z^r W^s and their ORDINARY Z-derivatives at each of the originally selected
integer lattice pairs q and qbar. W is held constant during differentiation.
Put all integer coordinate observations into E. With the original positive
trace metric B containing a factor 2 in each original coordinate block,

                     G = E B E^T.

The independent strict interpolation/point-count theorem makes det(G)>0.
Neither the characteristic polynomial nor the Gram itself is the field
discriminant. At odd discriminants the chosen pair order can have index two
in the maximal order; the full proof carries that distinction separately.

## Arithmetic: the lower pressure

For each eligible odd inert p, ordinary derivatives of Z^p-W, evaluated
at the original pairs, vanish modulo p; the *class-number-one* premise
is transported through the genuine maximal-order norm criterion. There is
an INTEGRAL upper-unitriangular row change U_p and a diagonal matrix
Delta_p=diag(p^k_i) such that

            U_p E = Delta_p Ehat      with Ehat integral,

hence (the same metric on both sides)

            U_p G U_p^T = Delta_p (Ehat B Ehat^T) Delta_p.

This two-sided integer factorization is the reason the determinant contains
p^(2F(p)), rather than merely p^F(p). Summing the guarded prime powers
and the inherited explicit tail estimates gives

  (999997/1000000)*log(D) - 5739/1000
    <= log(det G)/(R^2*S).

The integral middle matrix matters. Row-divisibility slogans alone would
not establish this exponent. The full independent arithmetic discussion is
in research/ender_radius_bridge/TWO_SIDED_ARITHMETIC_BRIDGE.md.

## Geometry: the upper pressure, same G

An integer unimodular frame T_a with a=floor(rho^2/2) preserves det(G)
under congruence while changing the row lengths entering Hadamard.

With rho>=10, the maximal rounding loss over the ORIGINAL complex disc is
|z*conj(z)-a| <= (101/200)*rho^2. The inherited coefficient lemma for
ORDINARY derivatives adds at most 1/8 on eligible r>=9S rows; their factor
is (63/100)^s. The other rows retain the old no-loss estimate.

The new proposal tightens only a uniform ratio. For 25S<=R<=26S, put
t=R-25S, hence 0<=t<=S. Direct multiplication gives

  676*S*(R-9*S) - 17*R^2 = (S-t)*(191*S+17*t) >= 0.

Therefore (R-9S)/R^2 >= 17/(676*S), and S>=100 also gives
(S-1)/S>=99/100. From the exact rational logarithm bound

  log(100/63) >= 231/500

the row saving is at least

  (17/676)*(99/100)*(231/500)
      = 388773/33800000
      > 23/2000 = 0.0115.

The prior normalized upper baseline is unchanged, so the proposed
tighter *upper bound on the SAME det G* is

  log(det G)/(R^2*S) <= (4/5)*log(D) - 1649/2000.

## Where the number 47,000,000,000 enters

The existing *sound* rational binary logarithm enclosure, with k=35,N=5
terms, is expected to certify log(47,000,000,000)>=24573/1000.

At that rational lower threshold, arithmetic minus geometry is

  (999997/1000000 - 4/5)*(24573/1000)
        - (5739/1000 - 1649/2000)
    = 26281/1000000000 > 0.

Thus if a class-number-one odd field had D>=47 billion the two bounds
would contradict one another. The prior separate even-field argument and
field equivalence then transport the result to every totally complex
degree-two number field; the final statement must concern its ACTUAL
absolute discriminant, with no caller-chosen quadratic generator.

This proposed endpoint is in
lean/TenthDiscriminant/TightRadialEndpoint.lean; the original-Gram
normalization is in TightRadialSaving.lean.

## For an independent mathematical reader

Can you check, without opening Lean, which maximal order the class-number
premise uses and why the prime is inert? Can you derive Ehat with ordinary
derivatives and construct the integral middle matrix? Can you confirm the
trace pairing, the positivity threshold and every original sample survive
radial re-framing? Can you reproduce the factorization and rational bracket
with exact arithmetic? Finally, does the odd/even chart return the actual
field discriminant rather than an observation determinant?

A passing kernel check validates the encoded theorem under its dependencies.
It does **not** supply an independent mathematician's semantic review, a
claim of originality or a proof of the Riemann hypothesis.

Professor Tao's challenge also values accessible exposition, method
comparison and negative results. This document is written so a skeptical
reader can isolate and test a particular obligation, rather than review an
unbounded AI research log.
