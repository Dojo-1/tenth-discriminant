# Factual brief for a possible human comment on Tao's challenge

**25 October 2026, through Phase46. This is an AI-prepared evidence brief, not the
human-generated summary requested by [Tao's post](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/).**
The contributor should write the actual comment in their own words
after reviewing the linked work. No comment has been submitted by this
repository work.

## Short AI-assisted draft for human revision

This draft follows the contributor's emphasis on making the local and
global views meet at one object. It remains AI-written; it is not a
human-generated submission or a claim that review has finished.

Building on Ben Green's derivative-determinant method and the credited
prior route, we used AI assistance to bring geometry and arithmetic back
to one integer: under class number one in the odd-discriminant case,
the same Gram determinant is
positive, highly divisible, and too small to satisfy both demands once
the radicand reaches `10^11`. With a prime-two argument for the even case,
the Lean result concerns the canonical
`Q(sqrt(-d))` family for positive squarefree d and bounds both d and the
actual absolute field discriminant, without borrowing the finite answer
or an older cutoff. Our aim is a proof whose joints remain human-readable;
this is still a large bound, we claim neither novelty nor optimality,
and independent human semantic review remains open.

Attach the [short proof](research/ender_radius_bridge/HUNDRED_BILLION_GUIDE.md)
and exact verification record after reviewing the current publication
status. The mathematical head e2848c8 passed pinned CI40172177485; the
[final record](research/ender_radius_bridge/PHASE43_PUBLICATION_FINAL.md)
states its full scope. A [separate AI review](research/ender_radius_bridge/PHASE45_REVIEW_REPORT.md)
found no semantic contradiction in five bounded checks. It rederived the
scalar/floor/field arguments, but traced rather than reproved the inherited
determinant apparatus. The exact model identifier was unavailable; no
independence between model families or human peer review is inferred.

## What can be stated now

- A [field dictionary](research/ender_radius_bridge/GENERATOR_BRIDGE_GUIDE.md)
  now constructs the caller's field identification from a specified root
  of X^2+d and degree two. Positive squarefree d and actual class number one
  then give the same actual100-billion bounds. Universal squarefree-generator
  existence remains open; the prior AI review does not cover this new API.

- The direct analytic radicand and actual absolute field-discriminant
  bounds are reduced to `10¹¹`, without using the finite classification
  or old cutoff. A fixed thinner rectangle `S=floor(R/25)` and auxiliary
  radius `ceil(0.52 D^(3/4))` retain the same prime constants and actual
  factor-two trace-Gram determinant. Local full build, fresh input
  and axiom checks pass; cite exact-head publication CI separately. This
  is a modest optimization, not an optimality or novelty claim.
  [Human analytic proof](research/ender_radius_bridge/HUNDRED_BILLION_GUIDE.md).

- Phase42's failed control and600-second cutoff attempt remain preserved
  as incomplete. Phase43's separately preregistered, unchanged completion
  passed in76.3502975s; combined proof-build cost is744.1774016s. No new
  pilot, parameter search or larger cap supplied the completion.

- A frozen internal proof-input audit inventories five compiled roots and
  checks their separation. The inspected class-number inputs are generic
  finiteness/PID/Minkowski facts, not an identified borrowed classification.
  This is not independent human review or a new permanent CI gate. The
  finite d≤163 conclusion must not be confused with an analytic estimate.
  Phases39/43 separately improve the latter to2e11/1e11, each with fresh
  input checks. [Frozen input map](research/ender_radius_bridge/PROOF_INPUT_GUIDE.md).

- Phase37 supplies a complete quotient-fiber certificate for the original
  remaining interval. The public actual-field iff has only positive-squarefree
  d hypotheses; the nine positive cases and original `7×10¹¹` cutoff are
  supplied. This is the canonical field family, not an arbitrary-field-type
  representation theorem. Cite the exact published commit and pinned CI
  result, not an earlier partial pilot. Independent human semantic/upstream
  review and further constant optimization remain open. No novelty, generalized
  Siegel-zero result, higher-class-number progress or Tao endorsement is claimed.
  [Human proof and failure accounting](research/ender_radius_bridge/CLASSIFICATION_GUIDE.md).

The following phase descriptions preserve earlier checkpoint scopes.

- Phase 31 proves the necessary nine-candidate list below one million.
  Universal wheel and interval-coverage proofs connect the actual class-number
  hypothesis to a kernel-checked complete finite computation on [92,1000000).
  The positive equalities are now supplied by Phase33; the upper middle
  interval remains open. This is not the full classification.
  [Human wheel proof](research/ender_radius_bridge/WHEEL_COVERAGE_GUIDE.md).

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

Do **not** make an unqualified full class-number classification claim,
claim an arbitrary imaginary-quadratic field-type representation theorem,
or call this upstream-ready Mathlib work. The canonical constructed family
has a connected checked iff with nine radicands; this needs independent
semantic review of the intended mathematical application. The100-billion
analytic estimate is distinct from the finite d<=163 conclusion. Phase32
supplies Mathlib's actual discriminant identity, Phase33 the nine positives,
and Phase37 the entire finite certificate. The new auxiliary radius is not the frozen
campaign's radius. Green CI is evidence about the statements
encoded in Lean, not independent semantic review of their intended
number-theoretic application.

## Decision gate for an actual challenge entry

A comment may describe the precise checked effective radicand bound, but
must distinguish the historical CRT run from the complete Lean certificate
and must not assert human semantic review. Obtain independent semantic review before submission.
Before posting even a progress note, the
human contributor should inspect the evidence, write their own short
summary, decide whether a non-bound progress report fits the thread,
and disclose the AI assistance. Large detail belongs in a repository
link, as Tao requests. This brief does not authorize posting.
