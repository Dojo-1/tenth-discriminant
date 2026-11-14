# Phase319 — the maximal-order completion test

> Same local order, different global support.
>
> The wild-ray experiment on the old integer order is not automatically the experiment on the full maximal order.

Phase318 found a one-dimensional second-wild radical-normal image on the original (Q_{109}) integer-order source. Phase303 had already shown that the genuine maximal-order norm ball adds 116 odd-coordinate observations and changes the primitive Gram's mod-5 rank. Phase319 puts those two lines in the same finite experiment without identifying their sources.

## Frozen carrier

- (K=mathbb Q(sqrt{-163})), (omega^2-omega+41=0).
- Radius 21, norm cutoff 441.
- Full maximal-order source: 225 points.
- Old integer-order subsource: 109 points, exactly the even-(omega)-coordinate points.
- Same 40 original monomial rows and one ordinary-jet layer.
- 5-divisible points remain nonunits, never assigned a unit ray tag.

## What is tested

1. **Exact global realization.** For every changed norm shell of each of the 34 split-prime characters, enumerate every solution of
   [
   a^2+ab+41b^2=n.
   ]
   Compare synthetic signed ray classes with every actual maximal-order generator at that exact norm.

2. **Full conductor-250 arithmetic.** For each character, replay all 177 prime-to-10 norm-shell totals and all 270 eligible coprime products.

3. **Maximal-order local normal map.** Enumerate all five norm-preserving second-depth lifts at each signed 5-unit site. Measure both the span of the full symmetric Gram differentials and their restriction to the actual mod-5 Gram radical.

4. **Synthetic Gram Smith check.** Reconstruct the full maximal-order primitive Gram modulo 25 for each character. Compare the first two Smith layers, and report determinant residues separately from determinant valuations.

## How to read the result

The exact maximal-order source is not a coordinate relabeling of the old (Q_{109}) source: it adds 116 points. A local order isomorphism at 5 does not identify those finite supports.

A changed Gram entry, a changed determinant residue modulo 25, an exact multiplicative ideal character, and a new determinant valuation are four different claims. The experiment keeps them separate. Phase303's source-specific (v_5(det G)=30) remains a prior finite result, not a uniform field theorem.

## Evidence boundary

- **P:** elementary norm identity, exact principal-ideal valuation algebra, and local trace differential under explicit hypotheses.
- **M:** bounded D163 source and ray calculations after exact-head CI.
- **H:** any uniform class-number-one theorem for hypothetical large discriminants, any extra field-uniform valuation, and any improved tenth-discriminant cutoff.
- **R:** treating the (Q_{109}) radical as the maximal-order radical, or treating synthetic ray tags as actual generators.

No changes to main or the reported (322^4) endpoint. No promotion of the separate (321^4) candidate.


The exact-head workflow is `.github/workflows/phase319-maximal-order-realization.yml`; no claim is promoted until that run and its hostile controls complete.

The parent Phase318 workflow also runs the Phase319 certificate on this draft PR, so the new code is checked before it is consolidated.


## First exact-head result — 14 November 2026

The first complete Phase319 arithmetic run passed (GitHub Actions run 43607889835). The source distinction is now measured directly:

| Quantity | Old even suborder | Full maximal order |
|---|---:|---:|
| Observations | 109 | 225 |
| Signed 5-unit sites | 50 | 108 |
| Primitive Gram rank mod 5 | 23 | 40 |
| Primitive Gram radical dimension | 17 | 0 |
| Radical-normal image of local second-wild lifts | 1-dimensional | 0-dimensional |

On the full support, all **540** local norm-preserving lifts pass. Their full symmetric 40-by-40 differential span has rank **10**, so local Gram changes remain; what disappears is the radical-normal channel. Every synthetic full-support primitive Gram has Smith layers ([40,0,0]) modulo 25.

The split-prime replay covers all **34** characters: 16 active on the old support, all 34 active on the maximal-order support. Eighteen become active only because of the 116 new odd-coordinate observations. The run verifies **53,312** exact valuation-product checks, **6,018** conductor-250 norm-shell replays, and **9,180** coprime products.

The exact generator test finds **44 changed norm shells** across 33 characters. In every changed shell, both synthetic signed ray classes are absent from the exact maximal-order norm fibre: **88 unrealized signed classes** in total. The remaining character, (p=197), changes tags on individual points but leaves every per-norm ray distribution unchanged. The mandatory norm-164, norm-212 and norm-227 controls remain disjoint from their synthetic assignments even in the full maximal order.

A final distinction: **21 of the 34 synthetic characters change the determinant residue modulo 25**, while every resulting primitive Gram still has all 40 Smith factors units modulo 5. The actual determinant residue is 7; synthetic residues vary. This is a concrete instance of changed determinant residue without any additional 5-adic valuation.

These are exact finite results for one D163 source. They do not prove a class-number-one constraint uniform in (D), do not add to the existing valuationWeight, and do not change the (322^4) endpoint. The Phase318 full-stack workflow and whole-root Lean check are tracked separately from the Phase319 arithmetic run.
