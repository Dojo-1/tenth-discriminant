# Factual brief for a possible human comment on Tao's challenge

**24 October 2026, through Phase 30. This is an AI-prepared evidence brief, not the
human-generated summary requested by [Tao's post](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/).**
The contributor should write the actual comment in their own words
after reviewing the linked work. No comment has been submitted by this
repository work.

## What can be stated now

- Phase 30 proves the finite sieve's entry conditions from actual class
  number one, including d=3 mod 8 above 7 and strict guarded prime tests.
  The necessary list below 92 is kernel checked. The complete middle-range
  certificate is still missing: the conditional nine-candidate theorem is
  not a classification. [Human bridge guide](research/ender_radius_bridge/FINITE_SIEVE_GUIDE.md).

- The repository studies an effective tenth-discriminant bound by a
  Green-style derivative trace-Gram determinant, an elementary
  factorial prime-mass input, and finite interval/CRT computations.
  Lean now proves: for every positive squarefree radicand d, actual class
  number one of the constructed `Q(sqrt(-d))` implies `d<7×10¹¹`. Both
  parity cases and an explicit field equivalence are supplied; there is no
  numerical premise. This is an effective bound, not the finite classification.
  The [short proof](research/ender_radius_bridge/FULL_CUTOFF_GUIDE.md)
  explains the even prime-two obstruction and its connection to the odd cutoff.
- The real determinant's positivity for sufficiently many samples,
  its exact integer-coordinate realization, and its reduction modulo
  `m` have Lean proofs. A fixed `D=19,p=3` example is both positive
  and divisible by `9`.
- A [human-readable paper proof](research/uniform_inert_valuation/PROOF.md)
  reconstructs the inherited general `p^(2F(p))` divisibility using
  `Z^p-W` and a unitriangular rectangular basis. Lean now supplies its
  actual-row action, integral factorization, maximal-order and class-number
  bridge in the stated odd, squarefree, strict-small-prime range. Geometry,
  finite prime mass, factorial conversion, tail and universal comparison
  are also connected. This is more than the earlier conditional helper.
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
or obtained an upstream-ready Mathlib formalization. The effective radicand
bound is checked in both parity cases; the finite classification is not.
Do not confuse the proved conventional parameter formula with an as-yet
unsupplied identity about Mathlib's `NumberField.discr`.
The new auxiliary radius is not the frozen
campaign's radius. Green CI is evidence about the statements
encoded in Lean, not independent semantic review of their intended
number-theoretic application.

## Decision gate for an actual challenge entry

A comment may describe the precise checked effective radicand bound, but
must not turn the recorded CRT sieve into a Lean classification or assert
human semantic review. Obtain independent semantic review before submission.
Before posting even a progress note, the
human contributor should inspect the evidence, write their own short
summary, decide whether a non-bound progress report fits the thread,
and disclose the AI assistance. Large detail belongs in a repository
link, as Tao requests. This brief does not authorize posting.
