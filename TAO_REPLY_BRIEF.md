# Factual brief for a possible human comment on Tao's challenge

**26 October 2026, through Phase56. This is an AI-prepared evidence brief, not the
human-generated summary requested by [Tao's post](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/).**
The contributor should write the actual comment in their own words
after reviewing the linked work. No comment has been submitted by this
repository work.

## Short AI-assisted draft for human revision

This draft follows the contributor's emphasis on making the local and
global views meet at one object. It remains AI-written; it is not a
human-generated submission or a claim that review has finished.

Following Ben Green's determinant method and the credited preceding work,
we used AI assistance to keep local prime divisibility and global geometry
attached to the same positive integer Gram determinant. The Lean development
locally proves `|disc K|<50000000000` for totally complex quadratic number
fields of class number one, with no supplied generator or isomorphism.
We want the joints of the argument to remain visible: this is a large bound,
stronger compared writeups exist, failures are preserved, and we claim neither
novelty nor optimality or completed independent human semantic review.

Attach the [short proof](research/ender_radius_bridge/FIFTY_BILLION_GUIDE.md)
and exact verification record after reviewing the current publication
status. Mathematical head `86abe21` passed pinned CI40355317865 for the
older62.5b endpoint, including the build,4710/3967/16968 dependency audit and
inherited rejection controls; security/CodeQL passed. Its [final record](https://github.com/Dojo-1/tenth-discriminant/pull/28#issuecomment-6421231717)
was posted before the next review/documentation push. Later publication
heads require separate CI; [local evidence](research/ender_radius_bridge/PHASE54_VERIFICATION.md).
The new50b target/full build, fresh25-input exclusions and4755/4012/16968
audit pass locally; its exact-head CI and human semantic review remain
separate. Review55 predates these changes. [Current evidence](research/ender_radius_bridge/PHASE56_VERIFICATION.md).
The earlier
[cutoff review](research/ender_radius_bridge/PHASE45_REVIEW_REPORT.md) and new
[bridge review](research/ender_radius_bridge/PHASE51_REVIEW_REPORT.md) cover
different sources. The new first report found no FATAL/GAP issue in its five
bounded checks and identified one documentation dependency error, corrected
after preservation. Neither review re-proves every inherited argument or
establishes model-family independence or independent human review.

The [Phase55 first report](research/ender_radius_bridge/PHASE55_REVIEW_REPORT.md)
then checks six joints of the new62.5-billion proof at86abe21. It
established no FATAL/GAP finding, re-derived new recovery/endpoint
calculations and source-traced inherited machinery. It did not rerun
Lean or CI. This adds bounded AI due diligence, not independent human
certification; [provenance](research/ender_radius_bridge/PHASE55_VERIFICATION.md).

## What can be stated now

- The [operator normalizer](research/ender_radius_bridge/CONJUGATION_BRIDGE_GUIDE.md)
  now supplies a positive squarefree root witness for an abstract degree-two
  totally-complex number field. Its actual-discriminant bound has only those
  standard field hypotheses and actual class number one. No presentation
  premise remains; no new constant or full classification is claimed.

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

Historical partial-frontier descriptions remain in Git and
[STATUS](STATUS.md). For present limitations and the exact frozen comparisons,
use [the current objective ledger](TAO_OBJECTIVES_CURRENT.md). Credit Ben
Green, the repository's named contributors and the compared prior sources;
disclose AI assistance plainly. The original post's Lean/upstream and
higher-class-number directions are possible research benefits, not reasons
to claim those results have been achieved.

## What must not be said

Do **not** make an unqualified full class-number classification claim,
claim a representation theorem beyond the stated degree-two/no-real-place
hypotheses, or call this upstream-ready Mathlib work. The canonical constructed family
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
and must not assert human semantic review. The bounded source reviews do
not provide exhaustive semantic verification of the inherited apparatus.
Before posting even a progress note, the
human contributor should inspect the evidence, write their own short
summary, decide whether a non-bound progress report fits the thread,
and disclose the AI assistance. Large detail belongs in a repository
link, as Tao requests. This brief does not authorize posting.
