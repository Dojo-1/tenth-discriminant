# Tao's challenge: current accounting and side discoveries

**The actual class-number-one bound remains 50 billion.** The new side
result is an integrated local Lean bound for ANY imaginary quadratic field with
at most two ideal classes: actual absolute discriminant<2^52, sharper<2^50
when odd. [Understand the transport](research/ender_radius_bridge/ALL_FIELD_BOUND_CURRENT.md).
This is a bound, not a full classification or an optimality claim.

These twelve rows are our working categories for
[Tao's challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/),
not an official numbered checklist. The [claim map](lean/FORMALIZATION.md)
keeps theorem checking, execution evidence and independent review separate.

## How we are faring

| # | Tao's objective | Where we are, with the limit attached |
|---:|---|---|
| 1 | Effective bound without Heegner input | **Checked cutoff:** imaginary quadratic fields of class number one have absolute discriminant below 50 billion. [Proof and guards](research/ender_radius_bridge/FIFTY_BILLION_GUIDE.md). |
| 2 | Best efforts to optimize the constant | **Conservative improvement:** 700 to 50 billion; the latest step from 62.5 to 50 saves 20%. Other approaches report much smaller bounds. No optimality claim. |
| 3 | A finite computation can finish the range | **Certificates supplied** for the canonical field family. The separate [finite-endgame scope](research/ender_radius_bridge/CLASSIFICATION_GUIDE.md) matters; no full-classification announcement here. |
| 4 | High-quality, possibly upstreamable Lean | **Connected formal apparatus.** Independent human semantic/API review and Mathlib acceptance remain open. [Claim map](lean/FORMALIZATION.md). |
| 5 | Compare different writeups | **Partial:** frozen [same-route comparison](research/ender_radius_bridge/SAME_ROUTE_COMPARISON.md) and [current source comparison](METHOD_COMPARISON_CURRENT.md). External proofs were not independently replayed. |
| 6 | Stimulate new arguments or arrangements | **Reusable arrangements:** factorial prime mass, exact staircase weights and geometric operators, within the credited route. No novelty claim. |
| 7 | Preserve and report negative results | **Preserved:** failed proofs, resource stops, per-form counting failure and the checked translation counterexample (determinant24 becomes60). [Coordinate guide](research/ender_radius_bridge/COORDINATE_TRANSLATION_GUIDE.md). PR37 CI timed out; it is not relabelled successful. |
| 8 | Help higher class-number problems | **Integrated locally:** EVERY imaginary quadratic number field with actual h<=2 has actual absolute discriminant<2^52; odd discriminants retain<2^50. Phase108 integrates arbitrary even-field transport unchanged. [Human proof](research/ender_radius_bridge/ALL_FIELD_BOUND_CURRENT.md). Independent human review remains open; [external CI is versioned per head](research/ender_radius_bridge/VERIFICATION_CURRENT.md). |
| 9 | Disclose AI use | **Disclosed** in the [README](README.md) and research/review records. Disclosure is not validation. |
| 10 | Post a repository link and human summary | **Public repo-linked comments located:** 26/27 October, attributed to jesusasit; authorship process not independently verified. [Source refresh](research/ender_radius_bridge/SOURCE_REFRESH_20261028.md). The current [AI-prepared brief](TAO_REPLY_BRIEF.md) remains unposted by this agent. |
| 11 | Independent due diligence | **Partial:** one bounded AI [review](research/ender_radius_bridge/PHASE58_VERIFICATION.md) at `63be64b`/50 billion. That reviewer did not rerun Lean/CI; later geometry is outside its scope. |
| 12 | Quality, collaboration and attribution | **Documented practice:** credited antecedents, versioned evidence and explicit limits. No endorsement, priority or external quality verdict is inferred. |

## Supplementary results

| Reusable insight | Checked scope and limit |
| --- | --- |
| One integer, real and modular views | The original derivative trace-Gram has exact integer/real correspondence, positivity from a strict point-count criterion and prime-power divisibility. [Mathematical spine](lean/MATHEMATICAL_SPINE.md). |
| Coordinate maps and literal shifts | Norm-compatible actual charts; explicit odd index-two image; affine laws preserve distances/counts/divisor/guarded positivity. Original determinant is NOT shift invariant. [Guide](research/ender_radius_bridge/COORDINATE_TRANSLATION_GUIDE.md). Integrated locally at106; its CI stop remains open. |
| Symmetry and exact counting | Central negation separates total-degree parity rows; staircase weights count the same boxes in a different order. Neither supplies an extra divisibility exponent. [Symmetry](research/ender_radius_bridge/CENTRAL_SYMMETRY_GUIDE.md) · [Staircase](research/ender_radius_bridge/STAIRCASE_EXACT_GUIDE.md). |
| Actual ideal geometry | Basis construction, norm/discriminant identities, off-axis counts and principal-axis calibration for actual ideal classes. [Basis operator](research/ender_radius_bridge/BASIS_COMPLETION_GUIDE.md) · [Even lattice](research/ender_radius_bridge/EVEN_IDEAL_LATTICE_GUIDE.md). The class-number assumption must travel with controlled coefficients. |
| One coherent prime family | The SAME ideals provide counts and4*card(P) selected distinct labelled norm elements; class-slice double counting and weighted loss feed the SAME Gram. [Family](research/ender_radius_bridge/COMMON_FAMILY_GUIDE.md) · [Weighted bridge](research/ender_radius_bridge/EVEN_WEIGHTED_BRIDGE_GUIDE.md). |
| Geometric normalization | Actual Minkowski constants and closed weighted estimates connect field discriminant to the all-range contradiction. [Even normalization](research/ender_radius_bridge/EVEN_NORMALIZATION_GUIDE.md). Odd/even discriminant factors differ. |
| Field invariants, independent of coordinates | A generic actual ideal-class bijection preserves class number under field isomorphism without h1/PID. Phase107 combines both actual-discriminant charts; the caller supplies no generator. [Global bound](research/ender_radius_bridge/ALL_FIELD_TWO_CLASS_GUIDE.md). |
| Failure as mathematical information | Per-form zero-row counting fails although aggregate accounting works; resource-stopped attempts and negative scalar samples remain preserved. [Counterexample](research/ender_radius_bridge/SPLIT_COUNT_BOUNDARY_GUIDE.md) · [History](STATUS.md). |

## Exact verification boundaries

| Checkpoint | Authoritative status |
| --- | --- |
| Production through104 | [PR36 merged](research/ender_radius_bridge/PR36_MERGE_RECEIPT.md), exact sourcebe1c0e3; pinned CI40700006963 and security passed. Whole audit5307logical/4516theorems. Includes canonical even-chart cutoff. |
| Coordinate/shift integration106 | Source38d799e: all four local checks pass, whole audit5350logical/4554theorems. [PR37](https://github.com/Dojo-1/tenth-discriminant/pull/37) records an earlier stop: CI40707296487 cancelled at25m after build/audit success. Final controls PASS log is NOT job success. [Receipt](research/ender_radius_bridge/PR37_CI_LIMIT_RECEIPT.md). |
| Arbitrary-field transport107/108 | First standalone run PASS100.7739366s; exact library integration at108 passes all four first checks. Whole audit5361logical/4565theorems;197reachable modules. [Integration evidence](research/ender_radius_bridge/PHASE108_VERIFICATION.md). [Publication status is versioned](research/ender_radius_bridge/VERIFICATION_CURRENT.md). |

The old bounded AI review at63be64b does not cover later geometry or107.
Independent human review, Mathlib acceptance and optimality remain open.
The [primary-source refresh](research/ender_radius_bridge/SOURCE_REFRESH_20261028.md)
records existing public comments and keeps q<480 unverified. No new posting
or reviewer was commissioned here.

Milestone details remain in [STATUS](STATUS.md) and the unchanged phase
records. The [historical accounting](TAO_OBJECTIVES_HISTORY.md) is the exact
70f9217snapshot; the [original audit](TAO_OBJECTIVE_AUDIT.md) stays frozen
at4c034f9. The current claims are the table above and the linked claim map.
