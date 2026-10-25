# A checked direct analytic bound below 100 billion

For positive squarefree d, actual class number one of the canonical field
`Q(sqrt(-d))` now implies both `d<100000000000` and an actual absolute field
discriminant below 100000000000. Local target, whole-library, signature,
fresh dependency and axiom checks pass. Exact publication-head pinned CI
is a separate required record. Independent human semantic review is open.

This halves the previous direct analytic cutoff and improves the original
700-billion threshold by a factor of seven. It does not recycle the finite
classification consequence d<=163. It is not an optimality or novelty claim;
the stronger external bounds in our frozen comparison remain stronger.

## The idea in one sentence

Make the monomial rectangle thinner and the sampling disk smaller, while
paying explicitly for the resulting prime-divisibility loss and proving
that the disk still contains enough observations.

## The proof, with the same integer throughout

Fix the original integral derivative trace-Gram determinant: ordinary
derivatives, factor-two normalization and rectangular labels unchanged.
For the odd chart choose exactly

    R = floor(D/4), S = J = floor(R/25), t = D^(1/4),
    rho = ceil((13/25)*t^3).

The [geometric bridge](TUNED_CUTOFF_GUIDE.md) checks t>=500, all integer
floor/ceiling and strict-prime guards, and the original chosen-radius
condition. In particular `3R+S<=.76D`, so pi>3.14 gives a square-root term
at most `.495*t^3`. Its boundary correction costs `10/t<=.02`; therefore
`1.001*.495+.02<.52`. The smaller disk still makes the SAME Gram positive.

The [aspect-ratio lemma](ASPECT_RATIO_GUIDE.md) bounds the quadratic prime
loss by `.0448K` when `R<=K*S`. Here K = 25.1 accounts for the integer
rounding in S. The guarded floor/log bound gives `log R>=log D-1.4`.
Using the same four checked prime constants and reciprocal tail yields

    L/(R^2*S) >= .999997*u-5.820,  u=log D.

The completed counted upper proof retains the original count-log,
derivative and endpoint corrections. Its accounting is

    U/(R^2*S)
      <= .75*u-.65 + (S/R)*(1.25*u-4.11) + .00125
      <= .8*u-.81315 <= .8*u-.813.

The prime arithmetic and positive integer determinant require `L<=U`.
But the two displayed affine envelopes separate for every `u>=25.3`;
the exact scalar gap at 25.3 is .0529241, and its slope is positive. The
candidate comparison fails at 25, a retained control. The endpoint
`D>=10^11` gives `log D>=25.3` using `10^11=2^11*5^11` and checked log2/log5
bounds. Thus every odd-chart D above the fixed threshold is excluded.

The existing maximal-order norm argument at prime two handles the other
parity chart. Explicit field equivalence and the actual discriminant
identity then give both public bounds—no field-identification or numerical
premise is left to assume.

## What was checked, and what was not

The public names in [TunedAnalyticCutoff.lean](../../lean/TenthDiscriminant/TunedAnalyticCutoff.lean)
end in `radicand_bound_100b` and `discriminant_bound_100b`. Fresh compiled
closures of the odd, radicand and discriminant proofs exclude 16 listed
old-cutoff/classification/finite-answer inputs. The finite classification,
nine positive cases and old 700-billion/200-billion bounds are not used.

The [Phase43 protocol](PHASE43_PROTOCOL.md) registered one separate fixed
completion before execution. Its mathematical body is identical to the
preserved Phase42 upper candidate; the first Phase43 build passed in
76.3502975 seconds within the same 600-second/8192-MB cap. No parameter tuning,
new pilot or repair was needed in Phase43. Phase42 still records its
66.9683539-second ceiling-control failure and 600.8587502-second resource stop.
Combined proof-build time across those attempts is 744.1774016 seconds.
The raw negative history is not relabelled PASS.

[Results](PHASE43_RESULTS.json) and [verification](PHASE43_VERIFICATION.md)
separate local proofs from exact-head CI. The earlier comparison, no-leak
check and provenance snapshots retain their dated scopes. No frozen
campaign, finite certificate, dependency pin or gate is changed. No
arbitrary-field-type representation, independent human review, general
Siegel-zero theorem, higher-class-number result, merge or Tao post is claimed.
