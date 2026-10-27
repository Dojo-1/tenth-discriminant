# Tao's challenge: current accounting and side discoveries

**For imaginary quadratic fields of class number one, the checked absolute
field-discriminant bound is 50 billion.** Class number one means unique factorization in the ring of
integers. The geometric count is proved on the draft branch; the
higher-class-number arithmetic bridge remains open. This page tracks
Tao's [challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/)
through proof source `70f9217` and Phase70/69 outcomes, 27 October 2026. No full-classification
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
| 8 | Help higher class-number problems | **No new verified range.** Geometry has pinned CI; parameter-prime-divisor accounting and fixed actual ideal-class norm lattices are integrated and checked locally; odd-chart multiplicity is integrated and checked locally; controlled coordinates/coefficient bounds, the even chart and field-discriminant transport still block an arithmetic count B. |
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
| Fixed ideal-class norm lattice | Integrated local [class-fiber lifting](research/ender_radius_bridge/CLASS_FIBER_GUIDE.md) proves (z)=IJ, norm multiplication and exact recovery, with one bounded J per class. No binary-form basis; odd-chart multiplicity has a separate local proof. |
| Odd-chart finite multiplicity | Integrated local [four-representation construction](research/ender_radius_bridge/RESIDUE_MULTIPLICITY_GUIDE.md) gives a selected set of4*card(P) distinct class-labelled actual norm elements. Coordinates and coefficient bounds are still missing. |
| Prime-axis accounting | Standalone Lean gives at most two prime points, none when a=1; two-class aggregation remains conditional on representation inputs. [Guide](research/ender_radius_bridge/TWO_CLASS_AXIS_GUIDE.md). |
| Limits that prevented overclaiming | A radial O(1/R) ceiling, the per-form zero-row failure and the [stopped coordinate attempt](research/ender_radius_bridge/PHASE69_VERIFICATION.md) remain preserved. [History and controls](STATUS.md). |

## Verification and the next decisive step

The cutoff's [bounded review](research/ender_radius_bridge/PHASE58_VERIFICATION.md)
and its versioned CI records remain distinct from later additions.
Geometry source `70f9217` passes the full
[pinned Lean CI](https://github.com/Dojo-1/tenth-discriminant/actions/runs/40412438935),
including final regression controls: 4,869 logical declarations, 4,114
theorems, 170 reachable modules. The [exact record](research/ender_radius_bridge/PHASE64_VERIFICATION.md)
keeps source versions, checks and review distinct. Passing code does not
establish human review. The later arithmetic production roots pass local
full build/audit at `82bfea6`; their [new-head CI remains separate](research/ender_radius_bridge/PHASE70_VERIFICATION.md).

The next arithmetic bridge must choose controlled binary-form coordinates
for the fixed ideal lattices and complete even-chart transport. The local
parameter-divisor bound still needs field-discriminant transport.
[PR30](https://github.com/Dojo-1/tenth-discriminant/pull/30) has completed
pinned CI/security checks; merging still requires explicit authorization.

The [detailed research history](TAO_OBJECTIVES_HISTORY.md) is the exact
`70f9217` snapshot, including superseded status language and all earlier
side results. The [original audit](TAO_OBJECTIVE_AUDIT.md) remains frozen
at `4c034f9`. Current claims are the table above and the linked claim map.
