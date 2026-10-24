# Factual brief for a possible human comment on Tao's challenge

**24 October 2026, through Phase 28. This is an AI-prepared evidence brief, not the
human-generated summary requested by [Tao's post](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/).**
The contributor should write the actual comment in their own words
after reviewing the linked work. No comment has been submitted by this
repository work.

## What can be stated now

- The repository studies an effective tenth-discriminant bound by a
  Green-style derivative trace-Gram determinant, an elementary
  factorial prime-mass input, and finite interval/CRT computations.
  Lean now checks the exclusion for every squarefree `D≡3 (mod 4)`
  with `D >= 7×10¹¹`, with no numerical premise. This is an odd-discriminant
  cutoff, not a theorem for even discriminants or a full classification.
  The [short proof](research/ender_radius_bridge/ODD_CUTOFF_GUIDE.md)
  explains the fixed auxiliary radius and normalized affine envelopes.
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
proved a full-discriminant cutoff, or obtained an upstream-ready Mathlib
formalization. The odd cutoff is checked; even cases and the finite
classification are not. The new auxiliary radius is not the frozen
campaign's radius. Green CI is evidence about the statements
encoded in Lean, not independent semantic review of their intended
number-theoretic application.

## Decision gate for an actual challenge entry

A comment claiming a **full effective bound or classification** must not
silently extrapolate the odd theorem to even cases or treat the recorded
CRT sieve as a Lean proof. Obtain independent semantic review as well.
Before posting even a progress note, the
human contributor should inspect the evidence, write their own short
summary, decide whether a non-bound progress report fits the thread,
and disclose the AI assistance. Large detail belongs in a repository
link, as Tao requests. This brief does not authorize posting.
