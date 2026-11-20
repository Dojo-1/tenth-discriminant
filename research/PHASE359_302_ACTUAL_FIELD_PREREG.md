# Phase359 — exact 302^4 actual-field theorem target, conditional until all sources verify

**20 November 2026. Pre-registered before creation of candidate Lean theorem. Research-only.**

## Mathematical target

For every type K with Field K, NumberField K, NumberField.IsTotallyComplex K, degree over Q=2, and NumberField.classNumber K=1, prove

  (NumberField.discr K).natAbs < 302^4 = 8,318,169,616.

This is the **actual field discriminant**, not the auxiliary integer Gram det. The proof must not invoke the known nine-field classification as a substitute for the desired source-to-field comparison, and must not introduce any unreviewed axiom.

## Critical same-source conjunction

For integer D>=302^4 in the odd class-number-one chart with D squarefree, construct the SAME source Q=ellipsePairs D (Tuned.thinRadius D), J=S, R=floor(D/4), S=floor(R/25), original ordinary Z-jets with W held fixed, original trace pairing (2,2D), and one integer Gram G_D.

In the proof body, obtain all three statements at exactly this D:

1. Original G_D positive: Phase354 14^4 source count / Phase358 source positivity.
2. Analytic upper on *this G_D*: Phase358 thin_production_normalized_upper_stronger_302.
3. Binary-plus-odd-prime source lower on *the same G_D*: Phase357 original_source_joint_normalized_lower_302, with explicit squarefree, odd chart and class-number-one hypotheses, no repeated prime power.
4. Contradiction of the two scalar bounds: Phase355 no_scalar_overlap_302_without_mixed.

Then transport odd/even maximal-order charts back to NumberField.discr K using the pre-existing field-transport lemmas. The even branch remains its existing theorem; do not misread the odd D parameter as a field discriminant in all cases.

## Falsifiers and promotion

- If ANY of #265 analytic upper or the new root fails to compile, label H and do not merge into main.
- Any hidden 307-only theorem in the dependency closure fails this 302 target.
- Any use of a different sampling set, trace metric, Gram, derivative convention or normalization fails the source test.
- Any unapproved prime factor, incorrect odd/even maximal order chart or unreviewed change to actual field discrimination fails semantic review.
- Even with green full-root Lean and source checks, human independent reconstruction in issue #50 remains mandatory before public promotion. Do not close #50.

## Evidence status

The input geometry, scalar, radius, and joint-lower components each have prior exact-head full-root Lean checks, but the NEW combined root and analytic upper are H until checked. A full field theorem at 302^4 remains H and unmerged by default.
