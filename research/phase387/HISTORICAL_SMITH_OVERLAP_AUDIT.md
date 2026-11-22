# Phase387.2 — Source-matched Smith overlap audit

**22 November 2026 · correction-preserving research audit · no new unconditional bound.**

## Verdict

The occupied-residue Smith estimate in Phase387 remains a conditional lower bound on an evaluation-module index. It cannot be added to a historical valuation of the **same Frobenius-normalized evaluation index**. Matched D283 and D403 source cases demonstrate the overlap. At D283/p3, a proposed additive lower bound is refuted by an exact older valuation.

## Frozen original source and historical provenance

The source is the original integer-pair trace Gram with ordinary Z derivatives, conjugate W held fixed, the same ellipsePairs source Q, row-major rectangular basis, and trace metric with weights 2 and 2D. The Frobenius basis uses k(r,s)=min(floor(r/p),S-1-s).

- [Phase278 pre-registration](../phase278/PRE_REGISTERED_P3_SOURCE_SATURATION.md): D283, rho31, R70, S=J2, Q169, old p3 Frobenius F3=67, exact normalized evaluation Smith index 527. Its Smith histogram is {0:36,1:9,2:9,4:36,5:9,6:9,8:31,9:1}.
- [Phase279 frozen primitive test](../phase279/PRE_REGISTERED_PRIMITIVE_RESIDUAL_SMITH.md) and [actual program](../phase279/primitive_residual_depth.py): same D283/p3 source, primitive pairing valuation 29, giving exact original determinant valuation v3(det G)=2(67+527)+29=1217. The prior D283/p5 normalized evaluation index is 195.
- [Phase280 observed D403 results](../phase280/OBSERVED_RESULTS_AND_LIMITS.md) and [Phase281 third-depth results](../phase281/OBSERVED_K3_RESULTS_AND_LIMITS.md): D403, rho40, R100, S=J4, Q219; p3 K3 capped Smith profile (0:90,1:36,2:18,>=3:256), additional index lower >=840; p5 profile (0:240,1:15,2:15,>=3:130), additional lower >=435. These are lower bounds, NOT exact complete indices or determinant valuations.
- [Phase284 Frobenius overlap](../phase284/PRE_REGISTERED_FROBENIUS_OVERLAP.md) already warns that raw first-lift witnesses may be carried by old Frobenius factors and must not be double credited.

## Exact matched comparisons

For each matched source let n=R*S, J=S, and C_m count occupied (x,y) residue classes on the SAME Q modulo p^(m+1). The new Phase387 lower estimate is

\[
I_{\mathrm{occ}}=\sum_{m\ge1}\max(0,n-2JC_m).
\]

| Original source | Source points | C1 modulo p^2 | Phase387 index floor | Older same-source evaluation index |
|---|---:|---:|---:|---:|
| D283/p3, rho31, n140, J2 | 169 | 27 | **32** | **527 exact** |
| D283/p5, same Q | 169 | 75 | **0** | **195 exact** |
| D403/p3, rho40, n400, J4 | 219 | 27 | **184** | **>=840 K3** |
| D403/p5, same Q | 219 | 75 | **0** | **>=435 K3** |

All deeper occupied-class estimates vanish on these four small sources. The new [historical_overlap.py](historical_overlap.py) performs two independent integer geometry calculations: direct enumeration of the actual Q and slice-based modular residue counting; it compares the result against fixed historical Smith profiles and checks the local tails. It does NOT rerun the old Smith eliminations, so the corroboration is an **overlap/provenance audit**, not an independent reproduction of the older Smith algorithms.

The first-layer **occupied-column cap** is also much weaker than actual structure:

- D283/p3: cap 2J*C1=108, actual normalized source rank mod3=36, a gap of 72.
- D403/p3: cap 216, actual normalized rank mod3=90, a gap of 126.

A productive future theorem must capture polynomial/ordinary-jet relations among distinct occupied residue classes, not merely count them.

## Exact falsification of adding the bounds

For D283/p3, the already saturated original source gives

\[
v_3(\det G)=2(F_3+I_3)+v_3(H_{\mathrm{primitive}})
=2(67+527)+29=\boxed{1217}.
\]

Incorrectly adding the Phase387 32 index units to that **same index** would demand

\[
v_3(\det G)\ge2(67+527+32)+29=\boxed{1281},
\]

contradicting the exact result 1217. This is a **refutation of the additive reading**, not of the Phase387 occupied-class lower bound itself.

If the same evaluation index I admits two lower bounds A and B, the combined lower is at least max(A,B), not A+B. A separately and fully saturated primitive restricted-pairing factor may be counted once, but an unsaturated Gram radical cannot be added by itself.

## What survives and what is retired

**P (conditional paper):** the source-matched Phase387 occupied-column/Smith/Cauchy-Binet lower bound, with actual normalized jet congruence and full-rank premises. The production D322^4+15 twelve-depth count remains a self-contained p3 lower certificate for its particular source Q, not a direct computation of the production Gram or an automatically new increment over historical source valuations.

**M:** four independent geometry comparisons and exact negative integer arithmetic. Historical Smith indices are sourced repository data, not fresh external mathematical review.

**R:** treating Phase387 occupancy factors as additive to historical D283/D403 normalized evaluation Smith factors; replacing 81 occupied evaluation classes with 59 Gram-active weighted classes; presenting the invalid 1281 inequality as a new theorem.

**H:** a Lean source-typed Smith filtration, a stronger polynomial-jet rank theorem, a competitive uniform bound after dividing by the actual R^2*S scale, and independent source-to-field scrutiny in [issue #50](https://github.com/Dojo-1/Tenth-Discriminant/issues/50).

**State correction:** old PR #157 on the 321^4 research candidate is now **closed as a superseded duplicate and was not merged**. The consolidated research remains in branch research/phase309-original-source-picard-minors; the accepted mainline 322^4 theorem is unchanged.

## Next bounded falsification

Freeze **D403/p3** original source, n400, Q219, J4, both signed integer coordinates and all four ordinary derivatives. Compute the full class-compressed modulo-3 normalized evaluation matrix (at most 216 columns) and compare its rank to the historical actual 90. Require an independent direct ordinary-jet oracle and two rank implementations. Reject if source rows, W, Q, metric or rank90 differ. Do not extrapolate to production-scale valuation until the cross-class relations have a uniform source-typed proof and survive the normalization. This is a small falsifiable next experiment, not an invitation to spin another research ontology.

The separately scoped Masullo, conductor and Selberg-Ihara results are not changed by this overlap audit. No merge was performed.


## Source-compressed 400-by-216 rank regression (new measured control)

The bounded next experiment above was executed **without constructing the full 1,752-column original normalized matrix**. The original D403/p3 source ellipse has y=-1,0,1 with enough consecutive x values for every x mod9 residue. Hence all 27 coordinate classes modulo 9 are realized.

Construct the original Frobenius-normalized ordinary-Z derivative columns at each class representative using the factored source polynomial, retaining j=0,1,2,3 and both integer-coordinate trace channels. The resulting finite class-compressed matrix is **400 rows x (27*4*2)=216 columns**. By the Phase386 p^(m+1) precision lemma, its column span modulo3 is the same as the original 400x1752 normalized evaluation matrix modulo3.

Two **different elimination directions** (row Gauss-Jordan and incremental column-basis reduction) both give EXACT rank **90**, matching the historical Phase280/281 source measurement. The derivative-channel rank profile is:

| Source ordinary derivative channels included | Rank |
|---|---:|
| j=0 | 27 |
| j=0,1 | 54 |
| j=0,1,2 | 81 |
| j=0,1,2,3 | **90** |

Removing the final ordinary derivative j=3 incorrectly lowers rank to 81: this hostile control matches the already documented Phase280 drop-last-jet failure. A deterministic permutation of the residue-class columns preserves rank90. Selected entries at six genuine Q points and eight original r labels were independently checked against the older *direct integer-pair ordinary derivative* implementation, rather than trusting only the factored modular evaluation code.

Executable artifact: [d403_compressed_rank.py](d403_compressed_rank.py); CI pins the same source helper files and checks both independent ranks.

**Interpretation boundary:** the nine extra ranks contributed by j=3 are numerical dimensions, NOT a proof that they coincide as identified subspaces with Phase284's nine first-Bockstein/Frobenius-overlap witnesses. This equality-of-subspaces would require an explicit source-preserving linear map and an algebraic test; similar dimension alone is insufficient. Neither 126-dimensional class-cap slack nor j=3's nine new ranks imply new p-adic determinant exponents without a complete Smith-index theorem. The full original signed trace Gram and its higher Smith layers remain separately controlled.

**Next theorem target (not claimed here):** derive the source-normalized residue-jet column space for D mod9=7, p3, R100, S=J4 as a finite algebraic module, and prove its rank90 and exact j3 quotient rank9 without sampling-dependent elimination. Pair a proposed generator relation with a direct-original-jet falsification and then formalize it in pinned Lean. Do not promote this bounded result into a new large-D cutoff.
