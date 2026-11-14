# Phase320 — cross-field maximal-order second-wild normal maps

Date: 14 November 2026. Preregistered before Phase320 implementation or new measurements. Branch: `research/phase277-320-unified`. Research-only; do not alter `main`, the accepted (322^4) theorem, or PR #157.

## Question

Does the Phase319 disappearance of the radical-normal channel belong to the D163 maximal-order support alone, to the class-number-one field, or to the particular row/jet geometry? Phase303 already supplied two important but differently scoped observations: D187 has class number two and a matched (R=40,J=1) maximal-order primitive Gram of rank 40; native D203 has (R=50,J=2), primitive rank 63 and a 37-dimensional radical. Phase320 repeats the complete local second-wild lift experiment on D187 and D203, and makes the source/geometry comparison explicit.

No global split-prime character family is transported from D163 to D187 or D203. Their nontrivial class groups mean element division does not enumerate all prime ideals. Phase320 is a local-ring and finite-source experiment only.

## Frozen fields and local arithmetic

Use the fundamental negative discriminants
[
Delta=-D,qquad Din{163,187,203}.
]
The exact reduced positive-definite primitive binary quadratic forms of discriminant (-D) are enumerated in the executable, with the preregistered class-number controls (h(-163)=1), (h(-187)=2), and (h(-203)=4). Do not import these class numbers as unexplained constants.

All three fields satisfy (Dequiv3pmod4), and 5 is inert because (-Dmod5in{2,3}). Put
[
m=(D+1)/4,quad omega=(1+sqrt{-D})/2,quad
omega^2=omega-m,
]
[
N(a+bomega)=a^2+ab+mb^2,quad
overline{(a,b)}=(a+b,-b),
]
and preserve the original trace pairing
[
B_D=egin{pmatrix}2&1\1&2mend{pmatrix},qquad det B_D=D.
]
All source and local calculations use exact integer pairs, with arithmetic reduced only at explicitly stated moduli.

## Source arms

### I. Common (R=40,J=1), common norm cutoff 441

For each of D163, D187 and D203, enumerate the full maximal-order support
[
Q_D(21)={(a,b)inmathbb Z^2:N(a+bomega)le441}.
]
Keep the same 40 original monomial labels (1,Z,ldots,Z^{39}), one ordinary layer, and the same norm cutoff. The three supports are allowed to differ; record exact point counts, b-layer counts, residue support in (mathcal O_D/5), unit/nonunit split and signed 5-unit sites. This is the matched geometry arm, not a claim that (R=40) is the native source row count for D187 or D203.

### II. D163 legacy suborder control

Use the 109-point even-b subsource inside (Q_{163}(21)), with the same maximal-order trace metric. Verify its exact identification with the original (mathbb Z[sqrt{-163}]) source through
[
(x,y)mapsto(a=x-y,b=2y),quad
T=egin{pmatrix}1&-1\0&2end{pmatrix},quad
T^TB_{163}T=operatorname{diag}(2,326).
]
The finite support is different from the full 225-point maximal-order source even though (det T=2) is a 5-adic unit. This is the required source-completion control.

### III. Native source-geometry arms

Derive (ho,R,J) from the exact original integer source parameter rule
[
25^4ho^4ge11^4D^3,quad
R=lfloor D/4floor,quad J=lfloor R/25floor.
]
The exact frozen parameters are:
- D163: (ho=21,R=40,J=1);
- D187: (ho=23,R=46,J=1);
- D203: (ho=24,R=50,J=2).

Use the full maximal-order norm ball (N(z)leho^2), the same original row labels (Z^rW^s), (0le r<R,0le s<J), with (W=ar Z), and the unchanged (B_D) trace metric. These native arms are separate from the matched (R=40,J=1) diagnostics.

## Original-to-primitive Frobenius frame

For a (J=1) arm, apply the unitriangular original-row change
[
Z^rlongmapsto Z^r-Z^{r-24}quad(rge25).
]
For a (J=2) arm, apply
[
Z^rlongmapsto Z^r-Z^{r-5}Wquad(rge5, s=0),
]
leaving the (s=1) rows unchanged. In each case the difference is divisible by 5 on every source point because (5) is inert and (mathcal O_D/5congmathbb F_{25}). Divide only the designated rows by 5 to form the primitive evaluation superlattice. Keep the unimodular row frame and the nonunimodular division matrix separate. Verify the original Gram congruence and exact trace-metric preservation; do not call the divided frame unimodular.

For every arm reconstruct the primitive Gram modulo 25 from the actual source, not from copied residue multiplicities. The 5-divisible source observations remain a separate nonunit stratum.

## Complete local second-wild experiment

For each signed 5-unit site (z), enumerate the entire line
[
{hinmathbb F_{25}:operatorname{Tr}_{mathbb F_{25}/mathbb F_5}(har z)=0},
]
which must contain exactly five elements. For each (h), check the lift (z'=z+25hpmod{125}), its signed partner, exact preservation of norm modulo 125, and preservation of the first wild digit of the Phase315 logarithm. Nonunits are never assigned a unit ray tag or lifted by this rule.

Recompute the source-native primitive Gram for each signed-site lift. Its difference from the baseline must be divisible by 5 modulo 25 and symmetric; the quotient differential must be linear in the (mathbb F_5) lift parameter. Independently compute:
1. the mod-5 primitive Gram radical (K);
2. the first radical-lift form (K^TGK/5mod5) and its rank (the first (5)-Smith layer);
3. the span rank of all differentials in the full symmetric matrix space;
4. the span rank of their restrictions (K^TH_iK), the radical-normal image.

Report ([e_0,e_1,e_{ge2}]) modulo 25 separately from any determinant valuation. A changed Gram entry or determinant residue is not a new 5-adic valuation. Do not assume the normal image is zero or nonzero.

The complete Phase315 signed conductor-125 local unit/log table is independently replayed for each field: all 15,000 units, 7,500 signed ray classes, exact residue/log lookup, conjugation and product identities. No class-number-one conductor-250 global ideal convolution is attempted for D187/D203.

## Independent controls and stop rules

- Count the class number by exact reduced-form enumeration; do not use a table lookup as executable evidence.
- Verify 5 inert in each field and the full 25-element residue algebra.
- Independently verify all exact norm-ball points and signed symmetry.
- Check the old D163 even-order Gram against the full-order even-b projection entry-by-entry.
- Check every Frobenius row divisibility and the original-to-primitive Gram identity.
- Exhaust every local five-lift line at every signed unit site.
- Recompute all local Smith layers and differential ranks independently of Phase318's D163 hard-coded functions.
- Reject any nonunit tagged as a unit, any lost support point, any unverified row transformation, any lift violating norm/first-digit constraints, or any unexplained rank/profile change.

If a native or matched source has insufficient rank or a censored modulus, report the obstruction as such. Do not increase precision, change the norm cutoff, alter row labels, or silently replace native geometry.

## Evidence boundary

- **P:** exact quadratic-order, trace, Frobenius-row and local norm-differential identities under the stated inertness hypotheses; exact reduced-form class-number calculation.
- **M:** finite source support, primitive Gram, Smith layers and local normal maps after exact-head CI.
- **H:** any uniform implication from class number to primitive rank/normal image, any uniform large-discriminant valuation, or any new tenth-discriminant cutoff.
- **R:** treating the D163 principal split-prime family as exhaustive for nontrivial class groups; identifying local order isomorphism with equality of finite supports; promoting determinant residues or local normal ranks to field-uniform valuation.

The objective is to distinguish field class group, finite source support, and row/jet geometry. It is not to add their valuations together.
