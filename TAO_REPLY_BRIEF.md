# Factual brief for a possible reply to Tao

**AI-prepared, through Phase 104. Not posted.** Existing public repo-linked comments are recorded in the source refresh below. Tao asks for a human-generated summary; the contributor should review the evidence and write or revise the actual comment in their own words. This document authorizes no posting.

## Short draft for human revision

Following Ben Green's derivative-determinant method and the credited preceding work, we used AI assistance to connect local prime divisibility and global geometry on the same positive integer determinant. The Lean development proves that every imaginary quadratic number field of class number one has absolute field discriminant below 50 billion, without assuming the known list or an older cutoff. We want the joints of the argument to remain visible: this is a large bound, other approaches report much smaller bounds, failures are preserved, and we claim neither novelty nor optimality nor completed independent human review.

## Facts behind those sentences

| Question | Supported answer |
| --- | --- |
| Exact result? | Every actual number field K of rational degree two, with no real places and actual class number one, satisfies `(NumberField.discr K).natAbs < 50000000000`. No supplied generator or isomorphism is needed. |
| Why does it work? | Geometry bounds one positive integer determinant above. Class number one forces prime-power divisibility of that same determinant, bounding it below. Above the cutoff the two bounds conflict. |
| What was optimized? | Sharper accounting of the existing prime 3/5 terms lowers the direct cutoff from 62.5 to 50 billion. The determinant, ordinary derivatives and valuation exponents stay the same. This is best-effort progress, not an optimality result. |
| What is verified? | Mathematical source `63be64b` passed pinned CI 40367229446: full build,4,772 logical declarations / 4,028 theorems dependency audit, source correspondence and rejection controls. Same-head security/CodeQL passed. [Exact completed record](https://github.com/Dojo-1/tenth-discriminant/pull/28#issuecomment-6423129650). Later geometric additions have separate verification; they do not enter this cutoff proof. |
| What did the review do? | One registered fresh-context AI reviewer checked six obligations at `63be64b`. No concrete FATAL/GAP/SLOPPY finding; local calculations re-derived, inherited machinery source-traced. Lean/CI NOT RERUN by the reviewer. Its first report is preserved, with no reroll. [Scope and limits](research/ender_radius_bridge/PHASE58_VERIFICATION.md). |

Read the [short mathematical spine](lean/MATHEMATICAL_SPINE.md), [50-billion proof](research/ender_radius_bridge/FIFTY_BILLION_GUIDE.md) and [current objective accounting](TAO_OBJECTIVES_CURRENT.md). The separate finite certificate and canonical-family iff have their own [guide](research/ender_radius_bridge/CLASSIFICATION_GUIDE.md); this proposed reply makes no full-classification announcement.

## What the entry would contribute

A connected formal development of the credited derivative-determinant route, a direct50-billion cutoff, and human explanations of its arithmetic/geometric joints. The [exact staircase identity](research/ender_radius_bridge/STAIRCASE_EXACT_GUIDE.md) is a supplementary simplification; it adds no valuation exponent. Credit and comparisons remain in [prior art](PRIOR_ART.md), the [same-route comparison](research/ender_radius_bridge/SAME_ROUTE_COMPARISON.md) and the [current pinned-source comparison](METHOD_COMPARISON_CURRENT.md). External results are source claims, not locally replayed proofs.

## Supplementary work beyond the class-number-one cutoff

The [actual odd-field extension](research/ender_radius_bridge/ODD_FIELD_TWO_CLASS_GUIDE.md)
proves absolute discriminant <2^50 for any imaginary quadratic field with
odd discriminant and class number at most two. This is a local checked
result; it does not use the sealed numerical feasibility test as a premise.
The preserved test and its negative samples are a separate evidence class.

For even discriminants, the [integrated weighted bridge](research/ender_radius_bridge/EVEN_WEIGHTED_BRIDGE_GUIDE.md)
now derives the prime count from actual ideal classes and uses it to pay
for lost factors of the same original determinant. It includes parameter
divisors and assumes no counting function or local divisibility result.
The distinction between radicand d and actual field discriminant 4*d
remains explicit. The [actual normalization and closed estimate](research/ender_radius_bridge/EVEN_NORMALIZATION_GUIDE.md)
are now integrated unchanged: M(K)=4*sqrt(d)/pi, and the full original-Gram
budget is dominated by the previously used scalar envelope. The
[all-range even-chart contradiction](research/ender_radius_bridge/EVEN_TWO_CLASS_BOUND_GUIDE.md)
is integrated unchanged: actual class number<=2 implies radicand<2^50 and
actual discriminant<2^52. Arbitrary even-field transport remains open;
this is no full-classification announcement.

[Phase104 verification](research/ender_radius_bridge/PHASE104_VERIFICATION.md)
records the unchanged accepted proof, all four local checks passing,
195 reachable modules, the whole-library axiom audit and 58 excluded older
inputs. These checks are separate from the earlier published CI and
review. External CI is recorded per published head; no independent review is claimed. Argon's
review is still underway and has not been received or assessed.

## Limits that must travel with the result

Independent human semantic review, verified model-family independence, Mathlib acceptance, optimality and the arbitrary-field even-discriminant higher-class-number extension are not established. The new odd-chart range is integrated and checked locally. A passing Lean build checks the encoded statement; it does not itself establish that the intended mathematical interpretation has received independent review.

The quoted 1933 Lehmer announcement reports a strict finite range `163 < D < 5 billion` in radicand notation. It cannot alone complete our 50-billion cutoff. Nor does deriving a later theorem from older foundations establish an earliest historical year. No such year is claimed.

The question about a zero-free region Re(s)>3/4 is a separate possible analytic input. It is not assumed by this determinant proof. The quoted zero-existence estimate only starts at `d >= 655`, so replacing 7/8 by 3/4 does not automatically yield a 164 cutoff. Do not confuse zeta(3/4) in the Chowla-Selberg evaluation at 7/8 with a 3/4 zero-free theorem.

Two public repo-linked comments are now located in the [28 October source refresh](research/ender_radius_bridge/SOURCE_REFRESH_20261028.md). Their authorship process is not independently verified. This AI-prepared brief and the newest results have not been posted by this agent. The contributor retains control over further wording and posting; earlier records remain in Git and [STATUS](STATUS.md).
