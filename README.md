# The Tenth Discriminant

**Can geometry and arithmetic squeeze the same integer until it cannot exist?**

That is the idea behind this AI-assisted contribution to [Terence Tao's challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/).
The question concerns imaginary quadratic number systems: extensions of the rational numbers obtained by adjoining a square root of a negative number. Which have unique factorization in their ring of integers?

**[Current research state — start here](RESEARCH_NOW.md):** one canonical branch, checked results, finite instruments, hypotheses and open review.

## The result in one sentence

**The Lean-checked theorem on `main` proves that every totally complex quadratic number field of class number one has actual absolute field discriminant strictly below 47.0 billion.**

Here, class number one means unique factorization in that ring; the discriminant measures the arithmetic size of the field. The bound applies to the actual field and its actual discriminant. It assumes neither the known list of answers nor an earlier cutoff.

This is a bound from one approach. It is far larger than the strongest bounds discussed in the challenge, and we claim neither novelty nor optimality. Tao explicitly welcomes understanding what each approach can achieve, including weaker numerical bounds.

## One determinant, two pressures

We build a positive integer determinant from polynomial values and derivatives at lattice points inside an ellipse.

- **Geometry limits its size.** The ellipse and derivative estimates give an upper bound.
- **Arithmetic forces divisibility.** Class number one makes that same determinant divisible by many prime powers, giving a lower bound.
- **At 47.0 billion and above, the bounds conflict.** The lower bound exceeds the upper bound, so class number one is impossible there.

The hard part is making both estimates refer to exactly the same positive integer. The formal development connects the lattice count, polynomial independence, integer matrix, prime divisibility and final inequality.

**[Read the 47.0-billion argument and its verification boundary](research/tight_radial_v1/HUMAN_RECONSTRUCTION.md)** · [Original arithmetic spine](lean/MATHEMATICAL_SPINE.md) · [Precise Lean theorem](lean/TenthDiscriminant/TightRadialEndpoint.lean)

## What is checked, and what remains

The **47.0-billion actual-field theorem** is now integrated in `main` ([merged PR #49](https://github.com/Dojo-1/tenth-discriminant/pull/49)). Its [exact-head full Lean CI](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41098122516) passed the complete root build, the source digest and 250 interval comparisons, permitted-axiom audit (5,729 logical declarations; 4,914 theorems), known-false negative controls, and security checks; [focused Lean modules](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41098122564) passed too. The [Phase133 verification receipt](research/tight_radial_v1/PHASE133_VERIFICATION.md) records the two failed elaboration runs and their proof-only corrections. The older **47.1-billion theorem** ([PR #48](https://github.com/Dojo-1/tenth-discriminant/pull/48)) and **47.5-billion theorem** remain checked predecessors. Such checks establish the encoded statements, not independent human mathematical review.

Independent human semantic review remains open: [a bounded independent-reader review request](https://github.com/Dojo-1/tenth-discriminant/issues/50) names the four exact obligations, so reviewers need not read the entire research history. [Argon’s frozen review and project CI](research/ender_radius_bridge/VERIFICATION_LAYERS_CURRENT.md) concern different questions: no defect was confirmed, but its verdict remains insufficient evidence. That review does not cover the later radial improvement or new interfaces.

The [source-aware method comparison](METHOD_COMPARISON_CURRENT.md) now separates our rectangular full-trace Gram from external auxiliary-prime maximal-minor and exact-rank methods (including a working-draft 331 claim). A possible full-rank transport must first align the *same* original observations and their prime conditions; no competitor's constant is imported. The [arbitrary-field classification interface](research/ender_radius_bridge/CLASSIFICATION_INTERFACE_CURRENT.md) transports the existing canonical-family proof and its separate finite certificates; it is not a new classification method. A separate [all-field bound for class number at most two](research/ender_radius_bridge/ALL_FIELD_BOUND_CURRENT.md) is published. Independent review, Mathlib acceptance and optimal constants remain open.

## One main branch, visible experiments

The public record now lives in **[main](https://github.com/Dojo-1/tenth-discriminant/tree/main)**. The independent two-sided finite oracle ([#44](https://github.com/Dojo-1/tenth-discriminant/pull/44)), the 47.5-billion actual-field theorem ([#45](https://github.com/Dojo-1/tenth-discriminant/pull/45)), the exterior-volume account ([#46](https://github.com/Dojo-1/tenth-discriminant/pull/46)), and the finite Rust/Lean mixed-frame atlas ([#47](https://github.com/Dojo-1/tenth-discriminant/pull/47)) are merged. Their original review discussions and exact CI receipts remain available; the cancelled overall CI on #47 is **not** called green.

[PR #48](https://github.com/Dojo-1/tenth-discriminant/pull/48) has also merged: the same original integral Gram now admits a sharper rounded radial center `101/200`, ordinary-jet factor `63/100`, and normalized Hadamard saving `0.011`. The five-term rational logarithm certificate closes the **actual-field 47.1-billion bound**; [full Lean + audit + negative-control CI passed](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41087748526) on its published source head. This is a more effective **bound from this method**, not a claim of novelty, optimality or external referee endorsement. The [human reconstruction](research/sharp_radial_v1/ENDPOINT_RECONSTRUCTION.md) follows exactly the same object through arithmetic and geometry. [Phase133 PR #49](https://github.com/Dojo-1/tenth-discriminant/pull/49) is **merged** after exact-head root audit. Its only mathematical improvement is a tighter uniform rectangle estimate on the SAME original integer ordinary-jet Gram: for `t=R-25S`, `S≥100`, `25S≤R≤26S`, the identity `676S(R-9S)-17R²=(S-t)(191S+17t)≥0` gives normalized saving `0.0115` with a checked rational log certificate. The actual-field cutoff is strictly **47,000,000,000**. [Human reconstruction](research/tight_radial_v1/HUMAN_RECONSTRUCTION.md) · [registered protocol](research/tight_radial_v1/PROTOCOL.md) · [CI receipt and preserved failures](research/tight_radial_v1/PHASE133_VERIFICATION.md). This is a checked improvement *within our method*, not priority, optimality, an independent referee, or a proof about Siegel zeroes.

Mathematicians should be able to recover both the argument and the precise uncertainty without opening five competing branches. The short [current-state map](RESEARCH_NOW.md) records what has been proved, tested, proposed, corrected and left to independent review. Each experiment turn updates this README after an **@Rizz pass** for mathematical clarity and reconstructability; [the contributor contract](AGENTS.md) makes that obligation explicit.

## Explore or check it yourself

| Start here | What you get |
| --- | --- |
| [Tao's objectives](TAO_OBJECTIVES_CURRENT.md) | Achievements, limitations and side discoveries |
| [Human proof guide](lean/HUMAN_GUIDE.md) | Why the determinant is positive |
| [Exact staircase count](research/ender_radius_bridge/STAIRCASE_EXACT_GUIDE.md) | A double sum understood by counting the same boxes in another order |
| [Compatible transport](research/ender_radius_bridge/PASSIVE_TRANSPORT_CURRENT.md) · [All-field h<=2 bound](research/ender_radius_bridge/ALL_FIELD_BOUND_CURRENT.md) · [Same integer and radial composition](research/ender_radius_bridge/STRUCTURAL_BRIDGE_CURRENT.md) | Explicit invariants, preserved failures and numerical scope |
| [Research history](STATUS.md) | Earlier checkpoints, failed attempts and corrections |

With the pinned Lean toolchain and dependencies installed, the core checks are:

```sh
cd lean
lake build
python audit.py
python negative_controls.py
```

The [pinned CI workflow](.github/workflows/lean.yml) supplies the full setup. [Environment notes](ENVIRONMENT.md) and the [preserved campaign README](https://github.com/Dojo-1/tenth-discriminant/blob/63be64b4ba3ff9795f552dd34bc415f6ea3acb25/README.md#reproduce-the-record) document the separate numerical experiments. A passing run supports only the statement and version it checks.

## Credit and collaboration

Ben Green supplies the derivative determinant method. [Prior art](PRIOR_ART.md) records contributions including twinheterodox, Kyle Pratt and van Dijk; [BEAN](BEAN.md) records route attribution and Jesús Vilela's norm-ellipse experiment. AI assistance is extensive and disclosed in the research records. Workflow names such as Ender are labels, not independent authorities.

The aim is an argument people can reconstruct, question and improve. Corrections are welcome: point to the statement, the disputed step and a way to check it.
