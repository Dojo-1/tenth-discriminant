# Factual brief for a possible reply to Tao

**AI-prepared, through Phase 85. Not posted.** Tao asks for a human-generated summary; the contributor should review the evidence and write or revise the actual comment in their own words. This document authorizes no posting.

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

The odd-chart extension now chooses one actual bounded ideal and controlled basis per class under h<=2, proves0<a<=N(J)<=M(K), lifts every ideal of the class into that same J, and counts all finite off-axis norm-bounded sets with a common coefficient bound. [Human proof](research/ender_radius_bridge/CONTROLLED_CLASS_GUIDE.md). The principal-class calibration also supplies a=1 and excludes prime-normalized axis elements. Local full-library, input and axiom checks pass; external exact-head CI for these additions remains pending.

The local [weighted split-prime bridge](research/ender_radius_bridge/WEIGHTED_SPLIT_GUIDE.md) now joins actual ideal-class counts, four labelled lifts per prime, complete remainder coverage and the log(p)/p weighted loss on the SAME original determinant under odd-chart h<=2. The caller supplies no counting function or coverage assertion. A [standalone closed-kernel theorem](research/ender_radius_bridge/CLOSED_KERNEL_GUIDE.md) now supplies an explicit bound in actual M(K) and composes it with that same inequality. The [integrated odd-field normalization](research/ender_radius_bridge/ODD_MINKOWSKI_GUIDE.md) now proves actual M(K)=2sqrt(D)/pi and removes that field-dependent input. Arbitrary-field/even-chart transport and a strict numerical contradiction remain. No new numerical range or classification follows.

Verification remains versioned: [local Phase82](research/ender_radius_bridge/PHASE82_VERIFICATION.md) records5058logical/4285theorem declarations and fresh dependency checks. Its input run had a nominal182s cap rather than registered180s (actual43.17s); the discrepancy is preserved, and the audit cap was corrected before execution. At84, exact83mathematics is integrated with actualM normalization. Full local root/input/audit checks pass:5103logical/4327theorems and fresh closures excluding the same34old roots. The first normalization/control setup failure is preserved; the final control is checked. [Exact84record](research/ender_radius_bridge/PHASE84_VERIFICATION.md). Earlier reviews and external CI are not transferred. Original stopped attempts remain failures.

A [sealed scalar test](research/ender_radius_bridge/TWO_CLASS_FEASIBILITY_GUIDE.md) now finds a positive conservative margin at2^50 and preserves seven earlier negative samples. Its100/200digit enclosures and controls agree. This is a proof target, not a new cutoff: all-D control and full formal composition remain open. Production84proofs are unchanged.

## Limits that must travel with the result

Independent human semantic review, verified model-family independence, Mathlib acceptance, optimality and a new higher-class-number numerical range are not established. A passing Lean build checks the encoded statement; it does not itself establish that the intended mathematical interpretation has received independent review.

The quoted 1933 Lehmer announcement reports a strict finite range `163 < D < 5 billion` in radicand notation. It cannot alone complete our 50-billion cutoff. Nor does deriving a later theorem from older foundations establish an earliest historical year. No such year is claimed.

The question about a zero-free region Re(s)>3/4 is a separate possible analytic input. It is not assumed by this determinant proof. The quoted zero-existence estimate only starts at `d >= 655`, so replacing 7/8 by 3/4 does not automatically yield a 164 cutoff. Do not confuse zeta(3/4) in the Chowla-Selberg evaluation at 7/8 with a 3/4 zero-free theorem.

No Tao comment or submission permalink is recorded. The contributor retains the decision to post, the wording of a human summary and responsibility for the linked claims. The older briefing and failed attempts remain in Git and [STATUS](STATUS.md).
