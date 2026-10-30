# Factual brief for a possible reply to Tao

## Current short human-review brief (30 October 2026; AI-prepared, NOT posted)

The strongest accepted result now on [main](README.md) is the **Lean-checked
strict bound |discr K|<47,100,000,000 for every totally complex quadratic
number field K with class number one**. The [precise theorem](lean/TenthDiscriminant/SharpRadialEndpoint.lean),
[human reconstruction](research/sharp_radial_v1/ENDPOINT_RECONSTRUCTION.md),
and [full exact-head proof CI](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41087748526)
are available. This improves the earlier 47.5-billion bound without
changing the original positive integer trace Gram, ordinary derivatives,
arithmetic prime-power lower bound, or class-number-one field premise.

The central arithmetic identity is an actual two-sided INTEGRAL factorization
U_p G U_p^T = Delta_p K_p Delta_p with K_p integral; this is why p^(2F(p))
divides det G. An integral radial change of basis preserves that SAME
determinant while tightening its Hadamard ceiling. At 47.1 billion the
explicit rational logarithm estimates give a positive contradiction.
The argument is not competitive with source-reported much smaller bounds
from other methods, and is not independently human-refereed.

I would ask an interested mathematician to try four reconstruction questions,
not to endorse the entire generated library:
[review issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50).
The [Phase133 PR #49](https://github.com/Dojo-1/tenth-discriminant/pull/49)
tests 47.0 billion, but that statement is a proposal until full Lean acceptance.

No comment or email to Tao was posted by this agent. The contributor should
decide whether and how this brief would help the discussion, preserving their
own wording and disclosing the extensive AI assistance.

---

### Historical brief, retained as a dated record

**AI-prepared through121; this brief is not posted.** Existing public
repo-linked comments are recorded separately. Tao asks for a human-generated
summary; the contributor should review and revise the text in their own words.

## Current verification boundary

Phase121 integrates the full actual-field48-billion proof unchanged in three production modules. All four first local checks pass;56written types/6data bodies exact, nine fresh closures, whole audit5,584logical/4,772theorems/17,029runtime and202reachable modules. The inventory adds134logical declarations and removes none; two generated equations explain the difference from the132source expectation. [Current human scope](research/ender_radius_bridge/RADIAL_CUTOFF_CURRENT.md) · [Exact evidence](research/ender_radius_bridge/PHASE121_VERIFICATION.md). Exact-head CI/security/merge status is versioned in the branch PR; no classification/optimality/new human-review claim or Tao posting.

Phase120 now proves the FULL actual-field48-billion cutoff standalone: every totally complex degree2 number field of class number1 has actual absolute discriminant<48000000000, with no supplied generator or earlier cutoff/classification premise. First invocation PASS174.6648317s; namespace28logical/28theorems; three fresh closures exclude73registered roots. [Human explanation](research/ender_radius_bridge/FORTY_EIGHT_BILLION_GUIDE.md) · [Exact evidence and input policy](research/ender_radius_bridge/PHASE120_VERIFICATION.md). Published integrated result stays50billion until unchanged integration and pinned CI; no new independent review or Tao posting.

Phase119 now checks the full SAME original integer determinant upper bound at the unchanged production radius: normalized log(detG)<=.8logD-.823 for everyD>=41006250000, with actual jet/trace equality, guarded positivity and exact penalty aggregation. [Human explanation](research/ender_radius_bridge/RADIAL_DETERMINANT_GUIDE.md) · [Exact evidence](research/ender_radius_bridge/PHASE119_VERIFICATION.md). This is standalone: arithmetic lower/endpoint/actual-field48bcomposition, integration and CI remain. Published cutoff stays50billion; no new review or Tao posting.

Phase118 now checks the full actual ordinary-jet radial estimate and sufficient.010rectangular scale saving standalone, with19unchanged public types/2definitions, namespace49logical/47theorems, three fresh dependency checks, and the failed first attempt preserved. [Human explanation](research/ender_radius_bridge/RADIAL_JET_GUIDE.md) · [Exact evidence](research/ender_radius_bridge/PHASE118_VERIFICATION.md). It does not yet prove the full original-Gram logarithmic saving or actual-field48btheorem. No new integration/CI, independent review or Tao posting; the published bound stays50billion.

Phase117 integrates the accepted universal radial operator unchanged. All four first local checks pass, with whole audit5,450logical/4,644theorems and199reachable modules. [Current scope](research/ender_radius_bridge/RADIAL_OPERATOR_CURRENT.md). PR41 is merged at e74028a after pinned proof CI40853123367 and same-head security passed; source/tested/actual trees agree. [Receipt](research/ender_radius_bridge/PR41_MERGE_RECEIPT.md). The .013gain and48bcutoff remain paper; the published theorem remains50billion.

Phase116 now proves the universal integral radial operator/all ordinary jets/original Gram determinant and divisor bridge standalone, with namespace and three fresh dependency checks. [Exact scope](research/ender_radius_bridge/PHASE116_VERIFICATION.md). The 0.013 gain, actual-field 48-billion theorem and integration/CI remain open; the published bound is 50 billion.

Phase115 gives a distinct **48-billion paper candidate**, using an integral monic radial basis and the same determinant/divisors. Its fixed finite checks pass; Phase116 now checks its universal operator bridge, while the quantitative estimate and cutoff remain unformalized. The published bound remains **50 billion**. [Candidate and limits](research/ender_radius_bridge/RADIAL_CENTERING_GUIDE.md). No Tao posting.

Phase114 full symbolic radial-block bridge also resource-stopped at the default Lean heartbeat limit after two failed invocations. No completed bridge/audit, production integration or lower cutoff. [Preserved failure and syntax-change disclosure](research/ender_radius_bridge/PHASE114_VERIFICATION.md).

Phase110 checks, and111integrates unchanged, passive polynomial/ordinary-jet transport recovering the SAME original integer Gram. [Human guide](research/ender_radius_bridge/PASSIVE_TRANSPORT_CURRENT.md). PR39's older cancellation is preserved; PR40's new-policy source7913eba passed full CI/security and merged at4b2492f with identical source/tested/actual trees. [Exact publication](research/ender_radius_bridge/PR40_MERGE_RECEIPT.md). The separate113larger-block experiment stopped at180s after11/12cases; positive focal samples are PARTIAL evidence, not a completed verdict, Lean theorem or cutoff gain. [Scope](research/ender_radius_bridge/RADIAL_BLOCK_CURRENT.md).

The h1 cutoff stays50b. Phase108 integrates the accepted107 proof unchanged: actual absdiscr<2^52 for
ANY imaginary quadratic field with actual h<=2, retaining odd<2^50;
no caller generator or isomorphism. [Human proof](research/ender_radius_bridge/ALL_FIELD_BOUND_CURRENT.md).
PR36 is merged with passing exact-head CI. PR37's CI is cancelled at25m,
not green, and its cancellation remains preserved. [Preserved receipt](research/ender_radius_bridge/PR37_CI_LIMIT_RECEIPT.md).
[PR38 passed full pinned CI and merged](research/ender_radius_bridge/PR38_MERGE_RECEIPT.md); no independent review is claimed for107/108. No cutoff gain,
full classification announcement, new posting or review commission here.
Older milestone descriptions below retain their separate evidence scopes.

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
actual discriminant<2^52. Arbitrary even-field transport is now checked standalone at107;
this is no full-classification announcement.

[Phase104 verification](research/ender_radius_bridge/PHASE104_VERIFICATION.md)
records the unchanged accepted proof, all four local checks passing,
195 reachable modules, the whole-library axiom audit and 58 excluded older
inputs. These checks are separate from the earlier published CI and
review. External CI is recorded per published head; no independent review is claimed. No new independent Argon report was received or assessed in this cycle.

## Limits that must travel with the result

Independent human semantic review, verified model-family independence, Mathlib acceptance and optimality are not established. The arbitrary-field even-discriminant h<=2 extension is integrated at108 and published with passing PR38 CI. The new odd-chart range is integrated and checked locally. A passing Lean build checks the encoded statement; it does not itself establish that the intended mathematical interpretation has received independent review.

The quoted 1933 Lehmer announcement reports a strict finite range `163 < D < 5 billion` in radicand notation. It cannot alone complete our 50-billion cutoff. Nor does deriving a later theorem from older foundations establish an earliest historical year. No such year is claimed.

The question about a zero-free region Re(s)>3/4 is a separate possible analytic input. It is not assumed by this determinant proof. The quoted zero-existence estimate only starts at `d >= 655`, so replacing 7/8 by 3/4 does not automatically yield a 164 cutoff. Do not confuse zeta(3/4) in the Chowla-Selberg evaluation at 7/8 with a 3/4 zero-free theorem.

Two public repo-linked comments are now located in the [28 October source refresh](research/ender_radius_bridge/SOURCE_REFRESH_20261028.md). Their authorship process is not independently verified. This AI-prepared brief and the newest results have not been posted by this agent. The contributor retains control over further wording and posting; earlier records remain in Git and [STATUS](STATUS.md).
