# Tao's challenge: current accounting and side discoveries

**The actual class-number-one bound remains 50 billion.** The new side
result is an integrated local Lean bound for ANY imaginary quadratic field with
at most two ideal classes: actual absolute discriminant<2^52, sharper<2^50
when odd. [Understand the transport](research/ender_radius_bridge/ALL_FIELD_BOUND_CURRENT.md).
This is a bound, not a full classification or an optimality claim.

These twelve rows are our working categories for
[Tao's challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/),
not an official numbered checklist. The [claim map](lean/FORMALIZATION.md)
keeps theorem checking, execution evidence and independent review separate. The [universal radial operator](research/ender_radius_bridge/RADIAL_OPERATOR_CURRENT.md) is now integrated unchanged with passing local checks; its quantitative gain and smaller cutoff remain paper candidates.

## How we are faring

| # | Tao's objective | Where we are, with the limit attached |
|---:|---|---|
| 1 | Effective bound without Heegner input | **Checked cutoff:** imaginary quadratic fields of class number one have absolute discriminant below 50 billion. [Proof and guards](research/ender_radius_bridge/FIFTY_BILLION_GUIDE.md). |
| 2 | Best efforts to optimize the constant | **Conservative improvement:** 700 to 50 billion; the latest step from 62.5 to 50 saves 20%. Other approaches report much smaller bounds. No optimality claim. |
| 3 | A finite computation can finish the range | **Certificates supplied** for the canonical field family. The separate [finite-endgame scope](research/ender_radius_bridge/CLASSIFICATION_GUIDE.md) matters; no full-classification announcement here. |
| 4 | High-quality, possibly upstreamable Lean | **Connected formal apparatus.** Independent human semantic/API review and Mathlib acceptance remain open. [Claim map](lean/FORMALIZATION.md). |
| 5 | Compare different writeups | **Partial:** frozen [same-route comparison](research/ender_radius_bridge/SAME_ROUTE_COMPARISON.md) and [current source comparison](METHOD_COMPARISON_CURRENT.md). External proofs were not independently replayed. |
| 6 | Stimulate new arguments or arrangements | **Reusable arrangements:** factorial prime mass, staircase weights and now [compatible polynomial/jet transport](research/ender_radius_bridge/PASSIVE_TRANSPORT_CURRENT.md) over commutative rings, retaining the SAME arithmetic Gram. No novelty claim or cutoff gain. |
| 7 | Preserve and report negative results | **Preserved:** failed proofs, resource stops, per-form counting failure and the checked translation counterexample (determinant24 becomes60). [Coordinate guide](research/ender_radius_bridge/COORDINATE_TRANSLATION_GUIDE.md). PR37 and [PR39 CI](research/ender_radius_bridge/PR39_CI_LIMIT_RECEIPT.md) timed out; neither is relabelled successful. |
| 8 | Help higher class-number problems | **Integrated and published:** EVERY imaginary quadratic number field with actual h<=2 has actual absolute discriminant<2^52; odd discriminants retain<2^50. Phase108 integrates arbitrary even-field transport unchanged. [Human proof](research/ender_radius_bridge/ALL_FIELD_BOUND_CURRENT.md). Independent human review remains open; [PR38 passed exact-head CI and merged](research/ender_radius_bridge/PR38_MERGE_RECEIPT.md). |
| 9 | Disclose AI use | **Disclosed** in the [README](README.md) and research/review records. Disclosure is not validation. |
| 10 | Post a repository link and human summary | **Public repo-linked comments located:** 26/27 October, attributed to jesusasit; authorship process not independently verified. [Source refresh](research/ender_radius_bridge/SOURCE_REFRESH_20261028.md). The current [AI-prepared brief](TAO_REPLY_BRIEF.md) remains unposted by this agent. |
| 11 | Independent due diligence | **Partial:** one bounded AI [review](research/ender_radius_bridge/PHASE58_VERIFICATION.md) at `63be64b`/50 billion. That reviewer did not rerun Lean/CI; later geometry is outside its scope. |
| 12 | Quality, collaboration and attribution | **Documented practice:** credited antecedents, versioned evidence and explicit limits. No endorsement, priority or external quality verdict is inferred. |

## Supplementary results

| Reusable insight | Checked scope and limit |
| --- | --- |
| One integer, real and modular views | The original derivative trace-Gram has exact integer/real correspondence, positivity from a strict point-count criterion and prime-power divisibility. [Mathematical spine](lean/MATHEMATICAL_SPINE.md). |
| Coordinate maps, active and passive shifts | Actual chart norms/index and affine laws are checked. With fixed observables an active shift changes24to60; moving the polynomial observables too now recovers24and the SAME original integer Gram. [Passive transport](research/ender_radius_bridge/PASSIVE_TRANSPORT_CURRENT.md) is integrated unchanged at111; external CI is versioned per head. |
| Symmetry and exact counting | Central negation separates total-degree parity rows; staircase weights count the same boxes in a different order. Neither supplies an extra divisibility exponent. [Symmetry](research/ender_radius_bridge/CENTRAL_SYMMETRY_GUIDE.md) · [Staircase](research/ender_radius_bridge/STAIRCASE_EXACT_GUIDE.md). |
| Actual ideal geometry | Basis construction, norm/discriminant identities, off-axis counts and principal-axis calibration for actual ideal classes. [Basis operator](research/ender_radius_bridge/BASIS_COMPLETION_GUIDE.md) · [Even lattice](research/ender_radius_bridge/EVEN_IDEAL_LATTICE_GUIDE.md). The class-number assumption must travel with controlled coefficients. |
| One coherent prime family | The SAME ideals provide counts and4*card(P) selected distinct labelled norm elements; class-slice double counting and weighted loss feed the SAME Gram. [Family](research/ender_radius_bridge/COMMON_FAMILY_GUIDE.md) · [Weighted bridge](research/ender_radius_bridge/EVEN_WEIGHTED_BRIDGE_GUIDE.md). |
| Geometric normalization | Actual Minkowski constants and closed weighted estimates connect field discriminant to the all-range contradiction. [Even normalization](research/ender_radius_bridge/EVEN_NORMALIZATION_GUIDE.md). Odd/even discriminant factors differ. |
| Field invariants, independent of coordinates | A generic actual ideal-class bijection preserves class number under field isomorphism without h1/PID. Phase107 combines both actual-discriminant charts; the caller supplies no generator. [Global bound](research/ender_radius_bridge/ALL_FIELD_TWO_CLASS_GUIDE.md). |
| Failure as mathematical information | Per-form zero-row counting fails although aggregate accounting works; resource-stopped attempts and negative scalar samples remain preserved. The [larger-block trial](research/ender_radius_bridge/RADIAL_BLOCK_CURRENT.md) stopped after11/12cases; partial gains supply no new cutoff. The distinct [integral radial operator](research/ender_radius_bridge/RADIAL_OPERATOR_CURRENT.md) is now integrated with passing local checks, while the 48-billion quantitative comparison remains paper. [Counterexample](research/ender_radius_bridge/SPLIT_COUNT_BOUNDARY_GUIDE.md) · [History](STATUS.md). |

## Exact verification boundaries

| Checkpoint | Authoritative status |
| --- | --- |
| Production through104 | [PR36 merged](research/ender_radius_bridge/PR36_MERGE_RECEIPT.md), exact sourcebe1c0e3; pinned CI40700006963 and security passed. Whole audit5307logical/4516theorems. Includes canonical even-chart cutoff. |
| Passive polynomial/jet transport110/111 | All20accepted types/proofs/four definitions/controls are integrated unchanged. All four first checks pass;5393logical/4593theorems,198reachable modules,70exclusions. [Integration evidence](research/ender_radius_bridge/PHASE111_VERIFICATION.md). [PR40 full CI passed and merged](research/ender_radius_bridge/PR40_MERGE_RECEIPT.md); source7913eba/merge4b2492f share the tested tree. PR39's older cancellation remains preserved. |
| Arbitrary-field transport107/108 | First standalone run PASS100.7739366s; exact library integration at108 passes all four first checks. Whole audit5361logical/4565theorems;197reachable modules. [Integration evidence](research/ender_radius_bridge/PHASE108_VERIFICATION.md). [PR38 merged after full pinned CI](research/ender_radius_bridge/PR38_MERGE_RECEIPT.md). |

The old bounded AI review at63be64b does not cover later geometry or107.
Independent human review, Mathlib acceptance and optimality remain open.
The [primary-source refresh](research/ender_radius_bridge/SOURCE_REFRESH_20261028.md)
records existing public comments and keeps q<480 unverified. No new posting
or reviewer was commissioned here.

Milestone details remain in [STATUS](STATUS.md) and the unchanged phase
records. The [historical accounting](TAO_OBJECTIVES_HISTORY.md) is the exact
70f9217snapshot; the [original audit](TAO_OBJECTIVE_AUDIT.md) stays frozen
at4c034f9. The current claims are the table above and the linked claim map.
