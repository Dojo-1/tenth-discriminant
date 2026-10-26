# Factual brief for a possible reply to Tao

**AI-prepared, through Phase 64. Not posted.** Tao asks for a human-generated summary; the contributor should review the evidence and write or revise the actual comment in their own words. This document authorizes no posting.

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

The current geometric bonus is a production Lean bound on any finite set of off-axis integer points in Q=ax²+bxy+cy²<=t: cardU<=2pi*t/sqrt(D)+4sqrt(at/D), for a>0,D=4ac-b²>0,t>=0. Row intervals, reflection and a scaling proof give the closed area formula, including t=0. [Human proof](research/ender_radius_bridge/QUADRATIC_AREA_GUIDE.md). This does not supply the ideal-class dictionary, prime multiplicity or ramified budget needed for a higher-class-number cutoff.

Publication scope matters: b4cff27 passed full production CI40403267176;74d02d3 passed CI40407136985 on the unchanged production library. Phase62's research proof has separate local evidence. Phase64's new integrated geometric count passes local target/root/type/input/audit checks; its newly published head still needs pinned remote CI. [Exact records](research/ender_radius_bridge/PHASE64_VERIFICATION.md). Earlier reviews are not transferred to it.

A connected formal development of this credited determinant route, a direct effective cutoff and human explanations of its geometric/arithmetic bridges. The [exact staircase count](research/ender_radius_bridge/STAIRCASE_EXACT_GUIDE.md) is a supplementary simplification, not an extra divisibility exponent or smaller cutoff. Credit and frozen external comparisons belong in [prior art](PRIOR_ART.md), the [same-route comparison](research/ender_radius_bridge/SAME_ROUTE_COMPARISON.md), and the [current pinned-source comparison](METHOD_COMPARISON_CURRENT.md). External bounds are source claims, not computations replayed here.

## Limits that must travel with the result

Independent human semantic review, verified model-family independence, Mathlib acceptance, optimality and higher-class-number progress are not established. A passing Lean build checks the encoded statement; it does not itself establish that the intended mathematical interpretation has received independent review.

The quoted 1933 Lehmer announcement reports a strict finite range `163 < D < 5 billion` in radicand notation. It cannot alone complete our 50-billion cutoff. Nor does deriving a later theorem from older foundations establish an earliest historical year. No such year is claimed.

The question about a zero-free region Re(s)>3/4 is a separate possible analytic input. It is not assumed by this determinant proof. The quoted zero-existence estimate only starts at `d >= 655`, so replacing 7/8 by 3/4 does not automatically yield a 164 cutoff. Do not confuse zeta(3/4) in the Chowla-Selberg evaluation at 7/8 with a 3/4 zero-free theorem.

No Tao comment or submission permalink is recorded. The contributor retains the decision to post, the wording of a human summary and responsibility for the linked claims. The older briefing and failed attempts remain in Git and [STATUS](STATUS.md).
