# Factual brief for a possible human comment on Tao's challenge

**23 October 2026. This is an AI-prepared evidence brief, not the
human-generated summary requested by [Tao's post](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/).**
The contributor should write the actual comment in their own words
after reviewing the linked work. No comment has been submitted by this
repository work.

## What can be stated now

- The repository studies an effective tenth-discriminant bound by a
  Green-style derivative trace-Gram determinant, an elementary
  factorial prime-mass input, and finite interval/CRT computations.
  The proposed `D >= 7×10¹¹` exclusion is **candidate mathematics**,
  not an established theorem or an independently checked
  class-number-one classification.
- The real determinant's positivity for sufficiently many samples,
  its exact integer-coordinate realization, and its reduction modulo
  `m` have Lean proofs. A fixed `D=19,p=3` example is both positive
  and divisible by `9`.
- A [human-readable paper proof](research/uniform_inert_valuation/PROOF.md)
  reconstructs the inherited general `p^(2F(p))` divisibility using
  `Z^p-W` and a unitriangular rectangular basis, under explicit
  residue irreducibility. Lean checks all ordinary transformed-row
  jets have the expected `p^k` factor under an explicit order-zero
  congruence, the exact proposed exponent sum, and the determinant
  implication **conditional on** the integral basis factorization.
- [Preregistered negative results](TAO_OBJECTIVES_CURRENT.md) include
  the radial `O(1/R)` ceiling, a finite lift counterexample to a
  universal extra valuation, and a noninert prime at which the local
  Frobenius premise fails. The numerical cutoff was not improved.
- Prior work must be credited: [Ben Green and the dated
  comparisons](PRIOR_ART.md), as well as the repository's named
  contributors and adversarial reviewers. AI involvement must be
  disclosed plainly.

## What must not be said

Do **not** say the project proved `D<=163`, solved class number one,
proved the cutoff `7×10¹¹`, or obtained an upstream-ready Mathlib
formalization. The class-number-to-inertness interface, general
polynomial basis factor, chosen-radius area inequality in Lean,
analytic-to-certificate chain and finite classification correspondence
are not checked end to end. Green CI is evidence about the statements
encoded in Lean, not independent semantic review of their intended
number-theoretic application.

## Decision gate for an actual challenge entry

A comment claiming an **effective bound** should wait for a complete,
independently reviewed proof connecting the determinant, arithmetic,
analytic estimates and computation, or clearly cite a different
already established route. Before posting even a progress note, the
human contributor should inspect the evidence, write their own short
summary, decide whether a non-bound progress report fits the thread,
and disclose the AI assistance. Large detail belongs in a repository
link, as Tao requests. This brief does not authorize posting.
