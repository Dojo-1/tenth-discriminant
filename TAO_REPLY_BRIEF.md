# Factual brief for a possible reply to Tao

**AI-prepared, through Phase 73. Not posted.** Tao asks for a human-generated summary; the contributor should review the evidence and write or revise the actual comment in their own words. This document authorizes no posting.

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

The odd-chart extension now supplies actual class-labelled prime multiplicity and an actual ideal-to-norm-form/geometric-count bridge. One constructed basis/form serves every finite norm-bounded set; integer coefficients, positive leading coefficient and exact discriminant are proved. [Human coordinate proof](research/ender_radius_bridge/IDEAL_COORDINATE_GUIDE.md) and [multiplicity](research/ender_radius_bridge/RESIDUE_MULTIPLICITY_GUIDE.md). The [principal-class calibration](research/ender_radius_bridge/PRINCIPAL_BASIS_GUIDE.md) is separately checked locally: a=1 and normalized prime-norm elements avoid the zero row. For actual class number at most two, [class squaring](research/ender_radius_bridge/CLASS_SQUARE_GUIDE.md) now also gives a controlled vector in every bounded class representative. A [least-norm construction](research/ender_radius_bridge/LEAST_NORM_GUIDE.md) now gives a bounded nonzero vector primitive in every actual basis, also checked locally. The [basis/coefficient interface](research/ender_radius_bridge/BASIS_COMPLETION_GUIDE.md) is also checked locally: a primitive vector of norm magnitude<=N(J)^2 becomes the first actual basis vector, with0<a<=N(J). Their chosen class-family composition, class-wide aggregation and even-chart transport still block a usable arithmetic B and new cutoff. These additional sources are currently outside production CI. The attempted controlled-basis composition hit its registered resource stop; its [failure is preserved](research/ender_radius_bridge/PHASE75_VERIFICATION.md), with no coefficient-bound claim.

Verification remains versioned: the50-billion proof has its completed CI/review scope above. Subsequent published arithmetic has separate exact-head records. The new coordinate production tree passes local full build/audit(4,963 logical declarations/4,196 theorems) and needs its own pinned CI. The [combined record](research/ender_radius_bridge/PHASE72_VERIFICATION.md) preserves source/attempt/axiom boundaries. The original [stopped coordinate attempt](research/ender_radius_bridge/PHASE69_VERIFICATION.md) remains a failure; the new result uses separately registered helper/composition proofs with unchanged resource limits. Earlier reviews and CI are not transferred.

## Limits that must travel with the result

Independent human semantic review, verified model-family independence, Mathlib acceptance, optimality and a new higher-class-number numerical range are not established. A passing Lean build checks the encoded statement; it does not itself establish that the intended mathematical interpretation has received independent review.

The quoted 1933 Lehmer announcement reports a strict finite range `163 < D < 5 billion` in radicand notation. It cannot alone complete our 50-billion cutoff. Nor does deriving a later theorem from older foundations establish an earliest historical year. No such year is claimed.

The question about a zero-free region Re(s)>3/4 is a separate possible analytic input. It is not assumed by this determinant proof. The quoted zero-existence estimate only starts at `d >= 655`, so replacing 7/8 by 3/4 does not automatically yield a 164 cutoff. Do not confuse zeta(3/4) in the Chowla-Selberg evaluation at 7/8 with a 3/4 zero-free theorem.

No Tao comment or submission permalink is recorded. The contributor retains the decision to post, the wording of a human summary and responsibility for the linked claims. The older briefing and failed attempts remain in Git and [STATUS](STATUS.md).
