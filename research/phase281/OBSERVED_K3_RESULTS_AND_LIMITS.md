# Phase281 — observed third Smith layer, exact finite D403 (after preregistration)

**Recorded 12 November 2026, after** [preregistration at `2d049a2`](PRE_REGISTERED_D403_K3.md) and the source-plus-workflow implementation head `209778bb9f0167e02c7eca03b45cbc2df85c65fe`. The focused source-faithful exact integer regression [run 43184659965](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43184659965) **PASSED** at that code head; its 3 per-prime prints are the primary numerical receipt. This file is **post-result analysis**, not part of the original frozen prediction.

## Frozen source and negative controls

Unchanged `D=403, rho=40, R=100, S=J=4, |Q|=219`, 400 original monomial rows, 1752 real/imaginary coordinates, all four **ordinary** `d/dZ` jets, conjugate W held fixed, and the original positive diagonal trace metric `B=(2,806,2,806,...)`. No Hasse jets, source-row subset substitution, changed support or flat Euclidean metric.

Three matched primes: 3 and 5 inert, 11 split. The integral unimodular old Frobenius row exponents `F3=570,F5=550` were divided once at the source before the capped Smith computation; split `F11=0`. Source numerator precision was raised to `p^(K+max_k)` *only because the preregistered quotient precision is K=3*; numerical **Smith depth remained frozen at K=3**.

Every source git-blob assertion, exact integer/dual-number jet oracle, Phase280 full-K2 replay, Phase208 selected-row K2 subset replay, two independent ranks, all high jets, original signed Gram, row shears, column reversals, and toy Smith test passed. The root Lean check is an independent CI gate; a successful arithmetic run does not automatically certify it.

## Exact computed capped Smith grades

The four buckets `r0,r1,r2,r>=3` sum to n=400. The last bucket is **CENSORED**: all its factors have valuation at least 3, with unknown exact depths.

| p | splitting | old F once | capped (r0, r1, r2, r>=3) | extra evaluation index I3 >= | conditional original v_p(det G) >= | unsaturated image radical (NOT additive) |
|--:|---|--:|---|--:|--:|--:|
| 3 | inert | 570 | (90, 36, 18, 256) | 840 | 2,820 | 36 |
| 5 | inert | 550 | (240, 15, 15, 130) | 435 | 1,970 | 0 |
| 11 | split | 0 | (132, 66, 44, 158) | 628 | 1,256 | 0 |

The inequality is the elementary-divisor and Cauchy–Binet conditional result for the original rational full-rank evaluation lattice and integral signed trace metric:

`I3 = r1 + 2*r2 + 3*r_ge3`, and `v_p(det(E B E^T)) >= 2*(F_p+I3)`.

The **difference from the previous K2 lower certificate** is:

| p | K2 additional index >= | K3 additional index >= | improvement in original Gram lower bound |
|--:|--:|--:|--:|
| 3 | 584 | 840 | +512 |
| 5 | 305 | 435 | +260 |
| 11 | 470 | 628 | +316 |

These differences are precisely twice the K3 unresolved bucket counts (256, 130, 158) because changing a censored floor from 2 to 3 raises the lower certificate by one for every still-unresolved factor.

### Interpretation

1. **Positive finite depth, not a primitive residual.** No `Cprim` or `H=Cprim B Cprim^T` has been recovered on D403. The K3 method does not determine complete evaluation indices or primitive pairings. **Prior work does:** draft [Phase277 PR #167](https://github.com/Dojo-1/tenth-discriminant/pull/167) (its exact-head focused/Lean/Markdown workflows passed) already fully saturated the **same original D403 source at split p11**, obtaining evaluation Smith levels (0:132,1:66,2:44,3:44,4:44,5:44,6:26), exact evaluation index **838**, primitive pairing levels (0:394,1:6), and exact **v11(det G)=2*838+6=1682**. Phase281's p11 capped histogram (132,66,44,>=3:158) is an exact **prefix replay of this older result**, not a new exact determinant discovery. Neither Phase281 nor Phase277 resolves the complete p3/p5 saturation at D403. The first two K2 grades agree with merged Phase280 exactly.
2. **Specificity negative control.** The split p11 still exhibits a large capped index and valuation bound, so mere large Smith depth is **not unique to inert primes**. This D403 specimen is intentionally not a class-number-one field candidate (p11 splits).
3. **Prior exact split control, not a new claim.** Full p11 saturation and its six-unit primitive residue were already reported in draft PR #167 before this Phase281 run. The Phase281 p11 *lower* certificate 1256 is weaker than that previously measured exact 1682 (difference 420 from deeper evaluation exponents plus 6 primitive pairing). This new experiment independently corroborates only the K3 prefix and source controls; PR #167 still requires its own integration/review decision.
4. **No asymptotic growth proof.** For fixed K and fixed finite prime set P, `I_K<=KRS` yields normalized additional mass `(2/(R^2 S))sum_p I_K log p <= (2K/R)sum_p log p -> 0` as R increases. It does not bound uncensored depths or primitive valuations.
5. **No repeated credit.** Old Frobenius F is counted once, K2 selected-index bounds are subsets of full K3, and the unsaturated pairing radical is not an independent determinant exponent. The source-to-existing-analytic-proof overlap audit remains unresolved.
6. **Distinct source worlds.** D283 has an exact primitive p3 residual valuation 29 and p5 primitive unit, but those cannot be transported into D403 without a new same-source saturation argument.
7. **No human semantic review.** This is exact finite machine arithmetic [M] and classical conditional linear algebra [P]; it is not independently peer-reviewed proof of the original analytic or field formulation.

## Decision and next smallest discriminating step

**STOP at K=3 under the registered experiment.** All three *K3 profiles* are censored, but p11 was already fully resolved by a DIFFERENT earlier method (PR #167). Do not retroactively increase the Phase281 precision, suggest that p11 is globally unknown, or call the K3 valuation an exact determinant valuation. A *new*, separately preregistered research action could seek a structural explanation of the modular observation-class collision strata shared by inert p3/p5 and split p11, with a theorem that separates evaluation-lattice index from the primitive restricted-pairing remainder.

The downstream questions are still open:
- Can the D403 p3/p5 local lattices be saturated completely with a new separately frozen precision/algorithm while retaining signed B? PR #167 already handles D403 p7/p11, so repeating p11 would be redundant.
- Is a positive primitive remainder specific to any broad family of inert-prime source geometries rather than occasional finite examples?
- Can **new, non-overlapping** mass be established uniformly on the original production family and compared to the same analytic inequality, without confusing determinant valuation with field discriminant or exceptional-zero exclusion?

**Merge policy:** Keep PR #172 draft until the final exact-head arithmetic, Markdown and Lean/axiom/source checks are green and the original-source semantics pass review. PR #157 remains behind independent human mathematical review #50. No class-number-one threshold improvement or Siegel-zero exclusion follows.
