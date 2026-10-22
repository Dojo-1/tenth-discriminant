# Claim-to-Lean map

**The main classification remains unformalized.** A conditional helper does not discharge its hypotheses. Declaration names below are in `TenthDiscriminant`. Read each statement and the CI result for its exact revision; this is not a percentage-of-proof metric.

The current code/test snapshot `9c41b2482fc69d8e53f906c2d0dd4357dc4909ef` passed [run 39789129577](https://github.com/Dojo-1/tenth-discriminant/actions/runs/39789129577): source linkage, build, compiled transitive axiom audit and all controls. The PR synthetic merge `b83a39e17fe29cd826959e83bf385c5559631e09` has the same tree. Historical matrix evidence remains at `c64a865` / [39774302749](https://github.com/Dojo-1/tenth-discriminant/actions/runs/39774302749), jet evidence at `561b294` / [39781264061](https://github.com/Dojo-1/tenth-discriminant/actions/runs/39781264061), and foundation evidence at `2048b9a` / [39758347058](https://github.com/Dojo-1/tenth-discriminant/actions/runs/39758347058). A historical green run does not approve later source changes.

| Source obligation | Lean artifact | Boundary |
|---|---|---|
| Principal quadratic form and nonrational norm threshold | `principalNorm_four`, `principalNorm_lower`, `small_norm_impossible` | Integer algebra. Identification with the ring of integers and principal ideals remains OPEN. |
| h(-D)=1 and D>163 force prime D=3 mod 8 and inert small primes | None | OPEN: genuine fields, fundamental discriminants, class groups, ideal norms, ramification and splitting. D>163 is essential. |
| Strict R<(D+1)/4 throughout intervals | `strict_cutoff`, `interval_strict_cutoff`, endpoint controls | Integer cutoff only, not inertness. |
| A(q)=sum of floor(r/q), r<R | `floorSum_scaled`, `floorSum_closed` | Universal identity matching the expression in `tools/ender.py` for positive q. Lean division is total at q=0; Python division is not. No Python-language semantics theorem. |
| F(p) and sum-of-minima identity | `valuationWeight`, `sum_min_identity` | Exact arithmetic. Link to determinant valuations OPEN. |
| Legendre superfactorial identity and logarithmic form | None | OPEN in this project. |
| Factorial lower bound, small-prime subtraction, higher-power tail | None | OPEN: complete prime-mass inequality, positivity and truncation. |
| Ellipse counts and full interpolation/nonvanishing | None | OPEN. `rank_guard_impossible` proves only failure of a sufficient guard when n<=R+S. The jet-count candidate below is not yet a Lean theorem. |
| Actual derivative rows and trace entries | `derivativeRow`, `traceGramEntry` | Defined over finite complex point sets with the actual derivative cutoff. Python implementation equivalence and integrality OPEN. |
| Full real trace-Gram matrix | `traceGramMatrix`, `rectangularTraceGram` | Existing trace entries, arbitrary finite row-label families, repeated labels permitted, row-major rectangular specialization. |
| Real/imaginary factorization | `traceGramMatrix_factorization` | Exact G=H+H with H=A A^T+B B^T. Factor two and all derivative columns retained. |
| Sum of squares and PSD | `real_gram_quadratic`, `traceGramMatrix_quadratic`, `traceGramMatrix_posSemidef`, `rectangularTraceGram_posSemidef` | Universal finite statements. PSD is not PD. |
| Nonnegative determinant | `real_psd_det_nonneg`, `traceGramMatrix_det_nonneg` | Nonnegative, not necessarily positive. |
| Hadamard diagonal-product bound | `real_det_sq_le_column_sq`, `real_psd_det_le_diag`, `traceGramMatrix_det_le_diag` | Proved for real PSD matrices and the actual trace matrix, including singular cases. Uses Mathlib volume-form inequality and PSD factorization. |
| Exact moment upper bound | `traceGramMatrix_det_le_moments` | Actual diagonal moments with truncation. Not the aggregate analytic `upper_B` bound. |
| Coordinate norm x^2+D*y^2 | `latticePoint_normSq` | Complex embedding with sqrt(D), D>=0; not a field/discriminant definition. |
| v_p(det G)>=2F(p) | None | OPEN: integer construction/integrality and inert-prime divisibility. |
| Aggregate upper_B | None | OPEN: analytic estimate of the proved diagonal-product bound at required parameters. |
| 250 interval endpoints | `checkChain_sound`, `ender_chain_checked`, `ender_integer_coverage` | Exact integer coverage on [7e11,10^36). Source endpoints match; no Arb margin is certified by that linkage. |
| 250 numerical contradictions | None | OPEN: kernel-checkable numerical certificates and semantic linkage. |
| Floor-safe universal envelopes | Partial | `ender_slope` proves the coefficient; determinant/envelope inequalities and geometry OPEN. |
| Actual C=80 error decay | `enderError_expansion`, `enderError_antitone` | Exact expression and antitonicity on u>=1. Starting margin OPEN. |
| All-u propagation | `positive_envelope`, `ender_positive_from_endpoint` | CONDITIONAL on endpoint positivity, explicitly a hypothesis. |
| CRT sieve on [92,7e11) | None | OPEN: saved survivors are not a Lean certificate. |
| Reduced forms below 92 and class-number correspondence | None | OPEN; not replaced by a finite-list axiom. |
| Derivative-row moment identities | `row_diagonal`, `row_radial_cross`, `traceGram_diagonal`, `traceGram_radial_cross` | All finite complex point sets, including origin and nonsymmetric sets. Successor diagonal retains unmatched derivative. |
| Scalar radial correlation / two-row determinant | `weighted_correlation_bound`, `weighted_block_bound`, `momentMatrix_bound` | Weighted moments with explicit multiplier range. Actual-row bounded-multiplier instantiation OPEN. |
| Annular multiplier parameter inequality | `derivative_multiplier_bound` | Numeric r,J inequality; actual-row factorial-ratio bridge OPEN. |
| 9/25 and necessity of bounded multipliers | `radial_constant_attained`, `multiplier_range_is_essential` | Exact moment-class controls, not sharpness in every derivative-row family. |
| Actual matrix controls | `traceGramMatrix_duplicate_rows`, `traceGramMatrix_single_control`, `traceGramMatrix_duplicate_control`, `traceGramMatrix_unmatched_control`, `traceGramMatrix_zero_derivatives_control` | Duplicate labels force det=0. Exact examples give det=2,0,4,0; sampled results are not generalized to nonvanishing. |
| Fischer block product / Smith filtration | None | OPEN; ordinary Hadamard is not the sharper block product. |
| Guaranteed pair-saving ceiling | `normalized_pair_gain` | R,S>0, c>=0, 2m<=RS; not a bound on all actual savings. |
| Final class-number-one classification | None | OPEN. No surrogate predicate, assumed structure field or custom axiom supplies the conclusion. |

## Jet-kernel bridge

| Claim | Artifact | Exact boundary |
|---|---|---|
| Gram nullspace equals invisible real jets | `realJet`, `traceGramMatrix_jet_energy`, `traceGramMatrix_kernel_iff` | Universal finite equality/equivalence, without independence. |
| PD iff real jet uniqueness | `traceGramMatrix_posDef_iff`, `traceGramMatrix_det_pos_of_jet_unique` | Equivalence proved; determinant corollary conditional. Geometric uniqueness remains OPEN. |
| More observations preserve established PD | `traceGramMatrix_posDef_mono_jets`, `traceGramMatrix_posDef_mono_points` | Added derivative columns or points. |
| Actual rows are polynomial jets | `rowSection_iterate_eval`, `realJet_eq_polynomial_jet` | Mathlib iterated derivative with W fixed, not differentiation along the conjugate graph. |
| Circle obstruction if J>=S is dropped | `circle_power_jet_zero`, `circle_power_nonzero` | General specialized polynomial facts; four sampled rank controls also detect the defect. |
| Complex dependence differs from real singularity | `traceGramMatrix_real_complex_control`, `complex_row_relation_control` | Actual example: complex rank 1 and real determinant 4. |
| J>=S and n>2(R-1)+(S-1) imply independence | [JET_NONVANISHING.md](JET_NONVANISHING.md) | Conventional derivation, NOT yet a Lean theorem. Local order implication is now proved below; factorization, determinant nonzero/degree and global accounting remain OPEN. |
| Finite evidence for the candidate | `jet_uniqueness_controls.py` | 96 full-rank modular cases, four dropped-J and four fixed-size resultant cases. Not universal verification. |

## Local Sylvester multiplicity: newly discharged link

| Claim | Artifact | Exact boundary |
|---|---|---|
| Row divisor product divides determinant | `row_divisors_dvd_det` | Actual matrix over a commutative ring; no nonsingularity premise. |
| Vanishing selected rows give powers of W-w | `polynomial_rows_vanish_pow_dvd_det` | Exponent is row count. |
| Constant determinant-one transform preserves the divisor | `constant_row_transform_pow_dvd_det` | Hypothesis discharged by the explicit Taylor matrix. |
| Taylor coordinates and determinant one | `taylorCoefficientMatrix_det`, `taylorCoefficientMatrix_mul` | Exact coefficient matrix/action, not an assumed rank-normal-form operation. |
| Root multiplicity kills low Taylor coefficients | `taylor_coeff_zero_of_root_power` | Actual polynomial power divisibility. |
| Full columns specialize correctly | `finiteColumnPolynomial_eq_specialization`, `polynomial_columns_root_power_dvd_det` | Explicit degree bounds and W-specialization; fixed matrix size. |
| Fixed Sylvester local order bound | `fixedSylvester_root_power_dvd_det`, `fixedDerivativeSylvester_multiplicity` | Shared specialized root power implies determinant-root power; leading-degree loss allowed. Lower-level m<=a premise explicit. |
| Nonzero specialization supplies m<=a | `fixedDerivativeSylvester_multiplicity_at_nonzero` | Proved over any field. Nonzero specialization is NOT nonzero resultant. |
| Sharpness and repeated-factor controls | `quadratic_fixedSylvester_det`, `quadratic_fixedSylvester_linear_coefficient`, `repeated_fixedSylvester_det` | F=Z^2-W gives -4W; F=Z^2 gives zero. Universal exponent m and automatic determinant nonzero are excluded. |
| Fixed determinant nonzero and W-degree bound | None | OPEN for the intended primitive irreducible mixed factor in characteristic zero. |
| Distinct-root and irreducible-factor contact budget | None | OPEN, then connect to actual rectangular jets and Gram PD. |

Read [SYLVESTER_MULTIPLICITY.md](SYLVESTER_MULTIPLICITY.md). The required local order implication is now proved directly through Taylor coordinates. A generic arbitrary-corank normal-form theorem is not claimed or required by this implementation.

## Strongest surviving result and obstruction

The actual real Gram kernel equals invisible real jets. The local fixed-size Sylvester determinant now provably absorbs the required root multiplicity, including leading-degree loss. This does not yet eliminate every invisible polynomial. A zero determinant is divisible by every power; nonzero determinant and its degree bound are load-bearing remaining obligations, not cosmetic refinements. No counterexample to the candidate class-number argument is identified by these distinctions.

## Source alignment, controls and independent-witness boundary

The Gram matrix uses actual trace entries. The local polynomial matrix uses actual shifted F/F_Z coefficient columns and explicit specialization. No source witness, numerical radius, derivative cutoff or guard is replaced. The arithmetic row retains the corrected D>163 hypothesis; small discriminants are not silently included.

All 13 matched mathematical pairs and four proof-audit probes passed at the verified snapshot. All earlier exact Gram/jet controls remain. The new exact suite has three reference polynomials and 48 fixed-seed cases, with translated roots, reordered bases and held-out determinant evaluations. There are 24 degree drops, but only 22 positive-exponent cases and nine cases satisfying both properties. The other 26 are boundary controls. Same-author tests are not independent semantic review; a separate SymPy resultant calculation agrees on the three reference formulas only.

The compiled audit found only standard permitted axioms across 145 theorem entries, including generated/private auxiliaries. These counts are inventory, not proof-completion metrics. The Lean kernel is a separately implemented checker, not assurance that all intended mathematics has been encoded. No independent human or semantic review is recorded.

Failed drafts remain in history. The local multiplicity repairs changed syntax, typed maps/sums and concrete-proof unfolding, not mathematical statements, and did not disable controls. Two nonfatal tactic-style warnings remain. Source linkage of endpoint pairs does not certify numerical inequalities.

## Next bounded gate

For the actual fixed coefficient matrix of a primitive irreducible mixed factor H, prove nonzero determinant in characteristic zero and the W-degree bound `(2a-1)b`. Do not supply nonzero determinant as a renamed field of a structure. Repeated-factor and leading-degree-drop controls must remain active. Then the distinct-root multiplicity sum and factor budget can be assembled into the candidate uniqueness theorem.

Kill a proposed promotion if a necessary coprimality/characteristic premise is missing, if the matrix is resized at specialization, or if an exact qualifying counterexample appears. Stop at the nonzero/degree bridge before claiming global nonvanishing. Number-field, integrality/divisibility, analytic, numerical and finite-classification links remain open; all saved certificates and the cutoff are unchanged.

## Branch integration

PR #6 merged into main at `157650c4`. PR #7 subsequently merged into the stacked feature branch at `4af7c467`, not main. Main-targeted PR #8 preserves both histories and carries the jet work plus this local multiplicity layer. Opening a draft PR does not merge it.
