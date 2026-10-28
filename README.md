# The Tenth Discriminant

**Can geometry and arithmetic squeeze the same integer until it cannot exist?**

That is the idea behind this AI-assisted contribution to [Terence Tao's challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/).
The question concerns imaginary quadratic number systems: extensions of the rational numbers obtained by adjoining a square root of a negative number. Which have unique factorization in their ring of integers?

## The result in one sentence

**Our Lean development proves that any imaginary quadratic number field with class number one has absolute field discriminant below 50 billion.**

Here, class number one means unique factorization in that ring; the discriminant measures the arithmetic size of the field. The bound applies to the actual field and its actual discriminant. It assumes neither the known list of answers nor an earlier cutoff.

This is a bound from one approach. It is far larger than the strongest bounds discussed in the challenge, and we claim neither novelty nor optimality. Tao explicitly welcomes understanding what each approach can achieve, including weaker numerical bounds.

## One determinant, two pressures

We build a positive integer determinant from polynomial values and derivatives at lattice points inside an ellipse.

- **Geometry limits its size.** The ellipse and derivative estimates give an upper bound.
- **Arithmetic forces divisibility.** Class number one makes that same determinant divisible by many prime powers, giving a lower bound.
- **Above 50 billion, the bounds conflict.** The lower bound exceeds the upper bound, so class number one is impossible there.

The hard part is making both estimates refer to exactly the same positive integer. The formal development connects the lattice count, polynomial independence, integer matrix, prime divisibility and final inequality.

**[Read the mathematical spine](lean/MATHEMATICAL_SPINE.md)** · [See the short cutoff proof](research/ender_radius_bridge/FIFTY_BILLION_GUIDE.md)

## What is checked, and what remains

Lean checks the encoded theorem and its dependencies; the audit checks for incomplete or nonstandard proof dependencies. [Exact statements and scope](lean/FORMALIZATION.md) distinguish these checks from human mathematical review.

Independent human semantic review remains open. One bounded AI review covers the final **50-billion** proof and exact staircase lemma at `63be64b`. It re-derived new local calculations and source-traced inherited machinery; **Lean/CI were not rerun by that reviewer**. [Review and limitations](research/ender_radius_bridge/PHASE58_VERIFICATION.md).

The repository also contains a separate canonical-family classification theorem and finite certificates. Their scope is explained in the [classification guide](research/ender_radius_bridge/CLASSIFICATION_GUIDE.md); this README makes no full-classification announcement. A new [local field bound](research/ender_radius_bridge/ODD_FIELD_TWO_CLASS_GUIDE.md) proves absolute discriminant `< 2^50` for any imaginary quadratic field with odd discriminant and class number at most two; external CI and the even-discriminant extension remain open. Mathlib acceptance and optimal constants remain open.

## Explore or check it yourself

| Start here | What you get |
| --- | --- |
| [Tao's objectives](TAO_OBJECTIVES_CURRENT.md) | Achievements, limitations and side discoveries |
| [Human proof guide](lean/HUMAN_GUIDE.md) | Why the determinant is positive |
| [Exact staircase count](research/ender_radius_bridge/STAIRCASE_EXACT_GUIDE.md) | A double sum understood by counting the same boxes in another order |
| [Latest local bridge](research/ender_radius_bridge/PHASE97_VERIFICATION.md) · [Field bound](research/ender_radius_bridge/PHASE88_VERIFICATION.md) · [Bounded test](research/ender_radius_bridge/PHASE85_VERIFICATION.md) | Checked statements and numerical feasibility kept separate |
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
