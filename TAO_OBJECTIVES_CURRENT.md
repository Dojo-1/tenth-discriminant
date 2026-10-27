# Tao's challenge: current accounting and side discoveries

**For imaginary quadratic fields of class number one, the checked absolute
field-discriminant bound is 50 billion.** Class number one means unique factorization in the ring of
integers. The geometric count is proved on the draft branch; the
higher-class-number numerical bound remains open. This page tracks
Tao's [challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/)
through proof source `70f9217` and integrated Phase82 and standalone83 and preserved75/69 failures, 27 October 2026. No full-classification
announcement, novelty, optimality or independent human review is claimed.

Lean checks encoded statements. A source claim, a checked theorem and a
human review have different evidential force. The [claim map](lean/FORMALIZATION.md)
spells out assumptions and the exact statements.

## How we are faring

| # | Tao's objective | Where we are, with the limit attached |
|---:|---|---|
| 1 | Effective bound without Heegner input | **Checked cutoff:** imaginary quadratic fields of class number one have absolute discriminant below 50 billion. [Proof and guards](research/ender_radius_bridge/FIFTY_BILLION_GUIDE.md). |
| 2 | Best efforts to optimize the constant | **Conservative improvement:** 700 to 50 billion; the latest step from 62.5 to 50 saves 20%. Other approaches report much smaller bounds. No optimality claim. |
| 3 | A finite computation can finish the range | **Certificates supplied** for the canonical field family. The separate [finite-endgame scope](research/ender_radius_bridge/CLASSIFICATION_GUIDE.md) matters; no full-classification announcement here. |
| 4 | High-quality, possibly upstreamable Lean | **Connected formal apparatus.** Independent human semantic/API review and Mathlib acceptance remain open. [Claim map](lean/FORMALIZATION.md). |
| 5 | Compare different writeups | **Partial:** frozen [same-route comparison](research/ender_radius_bridge/SAME_ROUTE_COMPARISON.md) and [current source comparison](METHOD_COMPARISON_CURRENT.md). External proofs were not independently replayed. |
| 6 | Stimulate new arguments or arrangements | **Reusable arrangements:** factorial prime mass, exact staircase weights and geometric operators, within the credited route. No novelty claim. |
| 7 | Preserve and report negative results | **Preserved:** failed attempts and a [per-form counting counterexample](research/ender_radius_bridge/SPLIT_COUNT_BOUNDARY_GUIDE.md). It does not refute the aggregate h<=2 claim. |
| 8 | Help higher class-number problems | **Finite weighted bridge checked locally; no new range.** Actual odd-chart h<=2 gives complete prime coverage, a derived prefix count and weighted loss on the original Gram. The closed kernel estimate is checked standalone at83; field/Minkowski transport, even chart and numerical contradiction remain. [Human proof and limits](research/ender_radius_bridge/WEIGHTED_SPLIT_GUIDE.md). |
| 9 | Disclose AI use | **Disclosed** in the [README](README.md) and research/review records. Disclosure is not validation. |
| 10 | Post a repository link and human summary | **Not posted.** The [AI-prepared brief](TAO_REPLY_BRIEF.md) awaits human revision and a posting decision. No submission permalink exists in our records. |
| 11 | Independent due diligence | **Partial:** one bounded AI [review](research/ender_radius_bridge/PHASE58_VERIFICATION.md) at `63be64b`/50 billion. That reviewer did not rerun Lean/CI; later geometry is outside its scope. |
| 12 | Quality, collaboration and attribution | **Documented practice:** credited antecedents, versioned evidence and explicit limits. No endorsement, priority or external quality verdict is inferred. |

## Supplementary accounting: useful results even if the main route stalls

| Result | What is checked, and where it stops |
|---|---|
| Exact staircase weight | A guarded double-sum identity from counting columns. No extra divisibility exponent. [Guide](research/ender_radius_bridge/STAIRCASE_EXACT_GUIDE.md). |
| Symmetry of the original Gram | Central negation separates opposite total-degree parity rows. No new cutoff. [Guide](research/ender_radius_bridge/CENTRAL_SYMMETRY_GUIDE.md). |
| Excluded-prime loss | Production [count-to-loss theorem](research/ender_radius_bridge/COUNT_TO_LOSS_GUIDE.md) uses log(p)/p. An integrated local [prime-divisor budget](research/ender_radius_bridge/PRIME_DIVISOR_LOSS_GUIDE.md) pays for parameter divisors separately; B remains an input for the others. |
| Off-axis quadratic point count | Production-root draft bound: cardU<=2pi*t/sqrt(D)+4sqrt(at/D), for finite U with Q<=t,y!=0,a>0,D=4ac-b²>0,t>=0. [Human proof](research/ender_radius_bridge/QUADRATIC_AREA_GUIDE.md). |
| Fixed ideal-class norm lattice | Integrated local [class-fiber lifting](research/ender_radius_bridge/CLASS_FIBER_GUIDE.md) proves (z)=IJ, norm multiplication and exact recovery, with one bounded J per class. The generic basis/count bridge is checked; the controlled h<=2 choice is now integrated locally below. |
| Odd-chart finite multiplicity | Integrated local [four-representation construction](research/ender_radius_bridge/RESIDUE_MULTIPLICITY_GUIDE.md) gives a selected set of4*card(P) distinct class-labelled actual norm elements. Actual coordinates/count and an h<=2 controlled coefficient choice are checked locally; their class-wide aggregation remains. |
| Actual ideal coordinates and count | [Constructed basis/form](research/ender_radius_bridge/IDEAL_COORDINATE_GUIDE.md) has integer coefficients, a>0, exact discriminant D and actual norm identity; finite element sets satisfy the off-axis geometric bound. The generic theorem alone gives no upper bound on a; the h<=2 controlled choice below supplies one. No new cutoff. |
| Controlled vector in every class | For actual class number at most two, [class squaring](research/ender_radius_bridge/CLASS_SQUARE_GUIDE.md) gives a bounded ideal J and actual z with normalized norm N(J). Checked locally, outside production CI; the chosen class-family composition is now integrated locally at78. The [attempted composition](research/ender_radius_bridge/CONTROLLED_BASIS_ATTEMPT.md) hit a registered resource stop and is preserved as failure. |
| Primitive vector independent of coordinates | [Least actual norm](research/ender_radius_bridge/LEAST_NORM_GUIDE.md) gives one nonzero element of norm magnitude<=N(J)^2, primitive in EVERY actual basis of each bounded class representative under h<=2. Checked locally outside production CI; basis completion and class-family composition are integrated locally; no new cutoff. |
| Actual basis and leading-coefficient interface | [A determinant-one lattice operator](research/ender_radius_bridge/BASIS_COMPLETION_GUIDE.md) completes the supplied actual primitive vector and proves0<a<=N(J) from its norm bound. Composed with76 and integrated locally at78; external CI, Minkowski/even-field transport and a new range remain. |
| Controlled per-class actual count | [One bounded ideal and basis per actual class](research/ender_radius_bridge/CONTROLLED_CLASS_GUIDE.md) lift all ideals of that class and give a common off-axis error bound using M(K). Local full-library/input/axiom checks pass; external exact-head CI and Minkowski/even-field/new range remain. |
| Full actual per-class prime count | The [actual axis theorem](research/ender_radius_bridge/ACTUAL_PRIME_AXIS_GUIDE.md) proves at most2 across all primes and0 in the calibrated principal class. A chosen actual class-family full prime count now needs no caller off-axis guard. Integrated locally at80 with four selected lifts on the SAME ideals; class-slice sum and finite weighted budget now close at82; Minkowski/even-field/new range remain. |
| Same-family multiplicity compatibility | [A fixed-family lifting interface](research/ender_radius_bridge/COMMON_FAMILY_GUIDE.md) now gives one controlled family with both full per-class prime counts and selected4*cardP labelled points. Local full-library/input/audit checks pass; class-slice sum and weighted loss are integrated locally at82; kernel estimate is checked standalone83; external CI remains. |
| Actual admissible-prime prefix count | [Actual class-slice aggregation](research/ender_radius_bridge/PRIME_PREFIX_GUIDE.md) now proves cardP<=h/4*(2pi*t/sqrtD+4sqrt(Mt/D)+1), uniformh<=2coefficient1/2, with all actual family/count/multiplicity premises supplied. Integrated locally at82 with complete weighted coverage; Minkowski/even-field/newcutoff remain. |
| Finite weighted arithmetic budget | [Count pays weighted loss](research/ender_radius_bridge/WEIGHTED_SPLIT_GUIDE.md): exact complete prime coverage, finite summation by parts and parameter-divisor payment on the original Gram. Local checks pass, with an explicitly recorded input-cap discrepancy; its closed estimate is supplied separately at83; no new cutoff. |
| Closed weighted-kernel estimate | [Positive affine operator and harmonic bound](research/ender_radius_bridge/CLOSED_KERNEL_GUIDE.md) now give an explicit formula in actual M(K), composed with the same Gram. Checked standalone locally; field/even transport and a new numerical range remain open. |
| Limits that prevented overclaiming | A radial O(1/R) ceiling, the per-form zero-row failure and the [stopped coordinate attempt](research/ender_radius_bridge/PHASE69_VERIFICATION.md) remain preserved. [History and controls](STATUS.md). |

## Verification and the next decisive step

The cutoff's [bounded review](research/ender_radius_bridge/PHASE58_VERIFICATION.md)
and its versioned CI records remain distinct from later additions.
Geometry source `70f9217` passes the full
[pinned Lean CI](https://github.com/Dojo-1/tenth-discriminant/actions/runs/40412438935),
including final regression controls: 4,869 logical declarations, 4,114
theorems, 170 reachable modules. The [exact record](research/ender_radius_bridge/PHASE64_VERIFICATION.md)
keeps source versions, checks and review distinct. Passing code does not
establish human review. Published arithmetic at `e77a446` has its own completed pinned CI40426517803,
verified separately from the new [local Phase82 checks](research/ender_radius_bridge/PHASE82_VERIFICATION.md):
183modules,5058logical/4285theorem declarations, with the input-cap discrepancy recorded. Standalone83 adds the closed estimate with its own28/26 namespace audit and dependency check, without a new root build. New exact-head CI is pending.

The next decisive bridge is field/Minkowski and even-chart transport
for the now-closed weighted-kernel estimate, then a strict numerical contradiction. The local parameter-divisor bound
still needs field-discriminant transport.
[PR30](https://github.com/Dojo-1/tenth-discriminant/pull/30) has completed
pinned CI/security checks; merging still requires explicit authorization.

The [detailed research history](TAO_OBJECTIVES_HISTORY.md) is the exact
`70f9217` snapshot, including superseded status language and all earlier
side results. The [original audit](TAO_OBJECTIVE_AUDIT.md) remains frozen
at `4c034f9`. Current claims are the table above and the linked claim map.
