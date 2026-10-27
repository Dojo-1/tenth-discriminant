# Tao's challenge: current accounting and side discoveries

**For imaginary quadratic fields of class number one, the checked absolute
field-discriminant bound is 50 billion.** Class number one means unique factorization in the ring of
integers. The geometric count is proved on the draft branch; the
higher-class-number arithmetic bridge remains open. This page tracks
Tao's [challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/)
through proof source `70f9217`, 26 October 2026. No full-classification
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
| 8 | Help higher class-number problems | **No new verified range.** Geometry is checked locally; class/form transport, prime multiplicity and ramified accounting still block an arithmetic count B. |
| 9 | Disclose AI use | **Disclosed** in the [README](README.md) and research/review records. Disclosure is not validation. |
| 10 | Post a repository link and human summary | **Not posted.** The [AI-prepared brief](TAO_REPLY_BRIEF.md) awaits human revision and a posting decision. No submission permalink exists in our records. |
| 11 | Independent due diligence | **Partial:** one bounded AI [review](research/ender_radius_bridge/PHASE58_VERIFICATION.md) at `63be64b`/50 billion. That reviewer did not rerun Lean/CI; later geometry is outside its scope. |
| 12 | Quality, collaboration and attribution | **Documented practice:** credited antecedents, versioned evidence and explicit limits. No endorsement, priority or external quality verdict is inferred. |

## Supplementary accounting: useful results even if the main route stalls

| Result | What is checked, and where it stops |
|---|---|
| Exact staircase weight | A guarded double-sum identity from counting columns. No extra divisibility exponent. [Guide](research/ender_radius_bridge/STAIRCASE_EXACT_GUIDE.md). |
| Symmetry of the original Gram | Central negation separates opposite total-degree parity rows. No new cutoff. [Guide](research/ender_radius_bridge/CENTRAL_SYMMETRY_GUIDE.md). |
| Excluded-prime count→determinant loss | Production theorem uses log(p)/p; the arithmetic count B remains an input. [Guide](research/ender_radius_bridge/COUNT_TO_LOSS_GUIDE.md). |
| Off-axis quadratic point count | Production-root draft bound: cardU<=2pi*t/sqrt(D)+4sqrt(at/D), for finite U with Q<=t,y!=0,a>0,D=4ac-b²>0,t>=0. [Human proof](research/ender_radius_bridge/QUADRATIC_AREA_GUIDE.md). |
| Prime-axis accounting | Standalone Lean gives at most two prime points, none when a=1; two-class aggregation remains conditional on representation inputs. [Guide](research/ender_radius_bridge/TWO_CLASS_AXIS_GUIDE.md). |
| Limits that prevented overclaiming | A radial O(1/R) saving ceiling and the per-form zero-row failure remain preserved. [History and controls](STATUS.md). |

## Verification and the next decisive step

The cutoff's [bounded review](research/ender_radius_bridge/PHASE58_VERIFICATION.md)
and its versioned CI records remain distinct from later additions.
Geometry source `70f9217` passes the full
[pinned Lean CI](https://github.com/Dojo-1/tenth-discriminant/actions/runs/40412438935),
including final regression controls: 4,869 logical declarations, 4,114
theorems, 170 reachable modules. The [exact record](research/ender_radius_bridge/PHASE64_VERIFICATION.md)
keeps source versions, checks and review distinct. Passing code does not
establish human review.

The next arithmetic bridge must place split-prime representations in the
actual ideal-class norm forms and justify their multiplicity. It must also
account for ramified primes. The geometric bound alone supplies neither.
[PR30](https://github.com/Dojo-1/tenth-discriminant/pull/30) has completed
pinned CI/security checks; merging still requires explicit authorization.

The [detailed research history](TAO_OBJECTIVES_HISTORY.md) is the exact
`70f9217` snapshot, including superseded status language and all earlier
side results. The [original audit](TAO_OBJECTIVE_AUDIT.md) remains frozen
at `4c034f9`. Current claims are the table above and the linked claim map.
