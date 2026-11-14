# Phase320 — cross-field maximal-order second-wild normal maps

> Three fields. Three class groups. One local residue algebra.
>
> The experiment separates the arithmetic of the field from the finite support and from the row/jet geometry.

Phase320 compares D163 (class number 1), D187 (class number 2), and D203 (class number 4). All three have 5 inert and (mathcal O_D/5congmathbb F_{25}).

## Source arms

| Arm | Norm radius | Original rows | Jet layers | Purpose |
|---|---:|---:|---:|---|
| D163 even legacy | 21 | 40 | 1 | Reproduce the old 109-point source |
| D163 full maximal | 21 | 40 | 1 | Reproduce Phase319's 225-point completion |
| D187 matched even / full | 21 | 40 | 1 | Compare index-two suborder with full support |
| D203 matched even / full | 21 | 40 | 1 | Compare index-two suborder with full support |
| D187 native even / full | 23 | 46 | 1 | Restore native row geometry and compare supports |
| D203 native even / full | 24 | 50 | 2 | Restore native high-jet geometry and compare supports |

The native D203 arm is a distinct source, not a scaled copy of the matched arm.

## What is measured

- Exact reduced-form class numbers and maximal-order norm-ball supports.
- The original-to-primitive Frobenius row transformation and its nonunimodular division.
- The complete conductor-125 local unit/log group in each field.
- Every norm-preserving second-wild lift at every signed 5-unit source site.
- Primitive Gram rank, radical, first radical-lift Smith layer, full differential span and radical-normal image.

Nonunits remain separate. No global split-prime character family is imported from D163 into the nonprincipal ideal classes of D187 or D203.

## Evidence boundary

[P] exact local ring, trace and norm identities; [M] bounded source/Smith/local-lift calculations after exact-head CI; [H] any uniform field-class-number-to-valuation implication; [R] transferring D163 principal-ideal characters to nontrivial class groups, or confusing changed determinant residues with new valuations.

The experiment cannot change the (322^4) publication endpoint or promote the (321^4) candidate.

The Phase318 parent workflow also runs this full Phase320 certificate and its adversarial tests on the integration PR head; the dedicated Phase320 workflow remains as the standalone branch gate.

Standalone branch gate refresh: Phase320 audit manifest and local-unit controls are aligned with the exact-head workflow.


**Source warning:** the D187/D203 native arms use the *native row/jet dimensions and norm radii* on the full maximal-order norm ball. They are not the same finite observation sets as the original integer-order source in the earlier D563/D587 programme. In particular, the D203 (R=50,J=2) maximal-order arm must not be identified with a prior integer-order D203 calculation. Phase320 measures the support change rather than importing a rank or radical from that different source.


## Phase320-B — index-two order controls

For D187 and D203, the experiment now repeats each matched and native geometry on both the full maximal-order norm ball and its even-ω-coordinate index-two suborder. The exact coordinate map
[
(x,y)mapsto(a,b)=(x-y,2y)
]
satisfies (T^TB_DT=operatorname{diag}(2,2D)) and identifies the old (mathbb Z[sqrt{-D}]) norm ball point-for-point with the even-b subset. The supports are still different: the odd-b maximal-order observations are genuinely new finite samples.

The additional arms are preregistered in `PRE_REGISTERED_PHASE320B_INDEX_TWO_ORDER_CONTROLS.md`. They measure whether the local radical-normal channel changes under support completion while keeping field and row/jet geometry fixed.
