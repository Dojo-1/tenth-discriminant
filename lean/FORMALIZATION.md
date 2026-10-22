# Claim-to-Lean map

**The main classification remains unformalized.** A conditional helper does not discharge its hypotheses. Declaration names below are in `TenthDiscriminant`. Read each statement and the CI result for its exact revision; this is not a percentage-of-proof metric.

The matrix follow-up starts at merged PR #5 (`c1dbf68`). Its implementation snapshot is `c64a8655bed0aa0a9c12def30a47d89aaf12e827`, with [run 39774302749](https://github.com/Dojo-1/tenth-discriminant/actions/runs/39774302749). Historical component evidence remains at `2048b9a` / [run 39758347058](https://github.com/Dojo-1/tenth-discriminant/actions/runs/39758347058). All four gates passed for the matrix snapshot, including the expanded controls. A historical green run must not be applied to later source changes.

| Source obligation | Lean artifact | Boundary |
|---|---|---|
| Principal quadratic form and nonrational norm threshold | `principalNorm_four`, `principalNorm_lower`, `small_norm_impossible` | Integer algebra. Identification with the ring of integers and principal ideals remains OPEN. |
| h(-D)=1 forces prime D=3 mod 8 and inert small primes | None | OPEN: genuine fields, fundamental discriminants, class groups, ideal norms, ramification and splitting. |
| Strict R<(D+1)/4 throughout intervals | `strict_cutoff`, `interval_strict_cutoff`, endpoint controls | Integer cutoff only, not inertness. |
| Optimized A(q)=sum of floor(r/q), r<R | `floorSum_scaled`, `floorSum_closed` | Universal identity matching the expression in `tools/ender.py` for positive q. Lean division is total at q=0; Python division is not. No Python-language semantics theorem. |
| F(p) and sum-of-minima identity | `valuationWeight`, `sum_min_identity` | Exact arithmetic. Link to determinant valuations OPEN. |
| Legendre superfactorial identity and logarithmic form | None | OPEN in this project. |
| Factorial lower bound, small-prime subtraction, higher-power tail | None | OPEN: complete prime-mass inequality, positivity and truncation. |
| Ellipse counts and interpolation/nonvanishing | None | OPEN. `rank_guard_impossible` proves only failure of a sufficient guard when n<=R+S. |
| Actual derivative rows and trace entries | `derivativeRow`, `traceGramEntry` | Defined over finite complex point sets with the actual derivative cutoff. Python implementation equivalence and integrality OPEN. |
| Full real trace-Gram matrix | `traceGramMatrix`, `rectangularTraceGram` | Entries are existing trace entries. Arbitrary finite row-label families, including repeated labels; row-major rectangular specialization. |
| Real/imaginary Gram factorization | `traceGramMatrix_factorization` | Exact equality G=H+H with H=A A^T+B B^T. Factor two and all derivative columns retained. |
| Sum of squares and semidefiniteness | `real_gram_quadratic`, `traceGramMatrix_quadratic`, `traceGramMatrix_posSemidef`, `rectangularTraceGram_posSemidef` | Universal finite statements. No independence assumed. PSD is not PD. |
| Nonnegative determinant | `real_psd_det_nonneg`, `traceGramMatrix_det_nonneg` | Nonnegative, not necessarily positive. |
| Hadamard diagonal-product bound | `real_det_sq_le_column_sq`, `real_psd_det_le_diag`, `traceGramMatrix_det_le_diag` | Proved for real PSD matrices and instantiated for the actual trace matrix, including singular matrices. Uses Mathlib volume-form inequality and PSD factorization. |
| Exact moment upper bound | `traceGramMatrix_det_le_moments` | Product of the actual diagonal moments, with derivative truncation explicit. This is not the aggregate analytic `upper_B` bound. |
| Coordinate norm x^2+D*y^2 | `latticePoint_normSq` | Complex embedding with sqrt(D), D>=0; not a field/discriminant definition. |
| v_p(det G)>=2F(p) | None | OPEN: integer construction/integrality and inert-prime divisibility. |
| Aggregate upper_B estimate | None | OPEN: analytic estimate of the proved diagonal-product bound at the required parameters. |
| 250 saved intervals: stitching | `checkChain_sound`, `ender_chain_checked`, `ender_integer_coverage` | Exact integer coverage on [7e11,10^36). Source digests/endpoints match; no Arb margin certified by this check. |
| 250 numerical contradictions | None | OPEN: kernel-checkable numerical certificates and semantic linkage. |
| Floor-safe universal determinant envelopes | Partial | `ender_slope` proves the coefficient; determinant/envelope inequalities and geometry OPEN. |
| Actual C=80 error decay | `enderError_expansion`, `enderError_antitone` | Exact expression and antitonicity on u>=1. Starting margin OPEN. |
| All-u propagation | `positive_envelope`, `ender_positive_from_endpoint` | CONDITIONAL on endpoint positivity, explicitly a hypothesis. |
| CRT sieve on [92,7e11) | None | OPEN: saved survivors are not a Lean certificate. |
| Reduced forms below 92 and class-number correspondence | None | OPEN; not replaced by a finite-list axiom. |
| Derivative-row moment identities | `row_diagonal`, `row_radial_cross`, `traceGram_diagonal`, `traceGram_radial_cross` | All finite complex point sets, including origin and nonsymmetric sets. Successor diagonal retains unmatched derivative. |
| Scalar radial correlation / two-row determinant | `weighted_correlation_bound`, `weighted_block_bound`, `momentMatrix_bound` | Weighted moments with explicit multiplier range. Actual-row bounded-multiplier instantiation OPEN. |
| Annular multiplier parameter inequality | `derivative_multiplier_bound` | Numeric r,J inequality; actual-row factorial-ratio bridge OPEN. |
| 9/25 and necessity of bounded multipliers | `radial_constant_attained`, `multiplier_range_is_essential` | Exact moment-class controls, not sharpness in every derivative-row family. |
| Singular and nonzero actual matrix controls | `traceGramMatrix_duplicate_rows`, `traceGramMatrix_single_control`, `traceGramMatrix_duplicate_control`, `traceGramMatrix_unmatched_control`, `traceGramMatrix_zero_derivatives_control` | Duplicate labels force det=0. Exact examples give det=2,0,4,0 respectively; no sampled result is generalized into nonvanishing. |
| Disjoint-block Fischer product / Smith filtration | None | OPEN; ordinary Hadamard is not the sharper block product. |
| Normalized guaranteed pair-saving ceiling | `normalized_pair_gain` | R,S>0, c>=0, 2m<=RS; not a bound on every possible actual saving. |
| h(-D)=1 implies D in {3,4,7,8,11,19,43,67,163} | None | OPEN. No surrogate predicate, assumed structure field or custom axiom asserts classification. |

## Strongest surviving result and obstruction

The full real trace matrix now has an exact factorization and sum-of-squares identity, a PSD proof, and a determinant bound by its actual diagonal moments. Hadamard is no longer merely a finite experimental check in this layer. This does not prove a positive determinant for the intended ellipse family or the analytic bound needed for Ender. The main obstruction remains the missing field/nonvanishing/divisibility/analytic/numerical/finite chain, not an identified counterexample to the candidate argument.

## Source alignment and controls

The new matrix is built from `traceGramEntry`, not defined as a convenient PSD surrogate. The factorization theorem proves the equivalence with real/imaginary coordinates. Singular cases remain in the domain. Six matched Lean pairs test correct and deliberately false assertions; four audit probes exercise standard proofs and rejected dependencies. Six known-answer and 64 fixed-seed exact Gaussian-integer cases exercise the trace formula, quadratic identity, determinant bounds, point reordering, row reordering and extra zero columns. Those finite tests use a different code path but share authorship; they do not prove Python implementation equivalence or general invariance beyond the formal statements.

## Next bounded obligation

Prove the actual row-independence/nonvanishing implication needed by the interpolation argument for the specified sampling set. Positive determinant must follow from genuine independence, not a Boolean flag or an assumption of the desired determinant conclusion. Retain duplicate/zero-row controls, specify the exact point-count/line-count hypotheses, and check their role on boundary cases.

Kill an attempted stronger interpretation if duplicate rows obtain a positive determinant, the witness is silently replaced, or the required independence is assumed rather than proved. Stop at the precisely stated nonvanishing theorem; do not promote class-number closure until the remaining dependencies are discharged.

## Verification and review boundary

The Lean kernel is a separately implemented checker. It is not independent assurance that the source interpretation and theorem selection capture every intended claim. Proofs, tests and interpretation share authorship; no independent semantic or human mathematical review is recorded. Standard axioms are allowed; extra axioms, incomplete proofs and native-evaluation dependencies are rejected by the audit gate.

The failed matrix draft and its sum-transport repairs remain in Git history. Only proof scripts changed; definitions, hypotheses and conclusions were preserved. Existing numerical evidence, Ender/Formic computations, discriminant cutoff and global classification status are unchanged.
