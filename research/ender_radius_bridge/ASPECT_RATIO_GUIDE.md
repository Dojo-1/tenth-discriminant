# Why a thinner rectangle helps—and eventually hurts

The new result is a Lean-checked trade-off in the existing determinant
argument. A single new-radius pilot also passes. **The checked analytic
cutoff is still200 billion, not100 billion.**

## One object, two competing budgets

Our rows are monomials `z^r*conjugate(z)^s`, in a rectangle with widths
`R,S`. The same integral trace-Gram determinant has a lower budget from
prime divisibility and an upper budget from complex size. These are not
separate matrices that we may optimize independently.

Making `S` smaller reduces the monomials' size cost. But it also reduces
the available Frobenius factors. The quadratic prime-loss term, after
dividing by `R^2*S`, therefore grows like `R/S`. We must pay that cost
rather than keep only the favorable size saving.

## The checked bridge: expose the price instead of hiding it

The old lower-envelope lemma required `R<=21*S`. The new
`rawPrimeMassLower_aspect_ratio` accepts any nonnegative real `K` with
`R<=K*S`, provided `R>=100000000`, `S>=500000` and `log R>=2`. It proves

    raw lower budget / (R^2*S)
      >= 0.999997*log R - (3.294 + 0.0448*K).

All decimals here are exact rational constants. The proof uses the same
four certified prime-log constants, factorial predecessor, reciprocal tail
and original unclipped lower expression. Clipping can only increase that
budget. No finite classification or old cutoff is used.

The reason for `0.0448*K` is short: the quadratic mass is at most `R^3/3`,
its fixed coefficient is at most `0.1344`, and `R/S<=K`. Their normalized
product is at most `0.1344*K/3`. The remaining losses are bounded by3.294.
This is a bookkeeping refinement in the credited method, not a new
number-theoretic argument or a proof of an optimal rectangle.

At `K=21` it recovers the old rounded bound. At `K=25.1` it gives the
rounded loss4.419 before converting `log R` to `log D`. Floors matter:
`R=100000024` has `S=floor(R/25)=4000000`, so `R>25*S`. Replacing the
floor ratio by the exact real value25 would be false.

## What the one pilot says

The preregistered observational test used only

    D=100000000003, R=25000000000, S=J=1000000000,
    rho=ceil(0.52*D^(3/4))=92470530, P=10000,
    Arb256-bit arithmetic, no parameter search.

All17 checks passed, including the original chosen-radius, point-count,
derivative-count and strict inertness guards. The conservative normalized
lower budget is about19.53218, versus upper19.44437: the recorded interval
for their difference lies strictly above0.08781. Production prime mass is
larger still. These are measurements at that input, not universal bounds.

Candidate affine envelopes `.999997*u-5.820` and `.8*u-.813` separate
for `u>=25.3`; that scalar statement is checked in Lean. The comparison
fails at `u=25`, also checked. Proving their separation does not prove
that every admissible D satisfies those envelopes.

## What remains before a smaller cutoff

For this NEW radius family, we still need universal floor/dimension and
chosen-radius guards, the counted upper envelope with every correction
term, and the lower-envelope conversion at the proposed endpoint. Then
we must compose to the actual class-number theorem and independently
check its inputs. The old family, finite certificate and200-billion
theorems are unchanged. Another preregistered cycle is needed; this phase
does not claim that the new cutoff is established.

## Evidence and limits

[AspectRatioLowerEnvelope.lean](../../lean/TenthDiscriminant/AspectRatioLowerEnvelope.lean)
contains the theorem and exact controls. [Protocol](PHASE41_PROTOCOL.md),
[results](PHASE41_RESULTS.json) and [verification](PHASE41_VERIFICATION.md)
separate the one pilot, local proof acceptance, dependency checks and
publication-head CI. The compiled input closure excludes the listed
classification/finite-answer theorems and both older cutoff generations.
Independent human semantic review, Mathlib API review and optimality are
not supplied by these checks. No external submission was made.
