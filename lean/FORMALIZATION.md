# Claim-to-Lean map

**The main classification remains unformalized.** This table distinguishes checked components from unresolved links. A conditional helper does not discharge its hypotheses. Declaration names are in namespace `TenthDiscriminant`; consult the source and CI result for the exact revision. This is not a percentage-of-proof metric.

The component snapshot `2048b9a5f14229d118cae7e70050db54cd006281` passed [build, source linkage, axiom audit and matched controls](https://github.com/Dojo-1/tenth-discriminant/actions/runs/39758347058). The proof statements, not a passing summary, delimit each result.

| Source obligation | Lean artifact | Boundary |
|---|---|---|
| Principal quadratic form and nonrational norm threshold | `principalNorm_four`, `principalNorm_lower`, `small_norm_impossible` | Integer algebra proved. Identification with the ring of integers and principal ideals remains OPEN. |
| h(-D)=1 forces prime D=3 mod 8 and inert small primes | None | OPEN: genuine number fields, absolute fundamental discriminants, class groups, ideal norms, ramification and splitting. |
| Strict R<(D+1)/4 throughout intervals | `strict_cutoff`, `interval_strict_cutoff`, endpoint controls | Integer cutoff proved. Does not by itself prove inertness. |
| Optimized A(q)=sum_{r<R} floor(r/q) | `floorSum_scaled`, `floorSum_closed` | Universal arithmetic identity; expression matches `tools/ender.py:floor_sum` for positive q. Lean's total division extends to q=0; Python's domain does not. No full Python-language semantics theorem is asserted. |
| F(p) and its finite sum-of-minima identity | `valuationWeight`, `sum_min_identity` | Exact arithmetic defined/proved. Connection to det G valuations is OPEN. |
| Legendre superfactorial identity and log form | None | OPEN in this project. No prime-mass inequality imported as an axiom. |
| Integral factorial lower bound, small-prime subtraction, higher-power tail | None | OPEN: complete prime_mass inequality, including positivity and truncation. |
| Ellipse point counts and interpolation/nonvanishing | None | OPEN for the actual evaluation set. `rank_guard_impossible` proves only failure of the sufficient guard when n<=R+S. |
| Derivative trace Gram construction | `derivativeRow`, `traceGramEntry` in `TraceGram.lean` | Actual finite complex row and trace-entry formulas defined. Full integer implementation equivalence, integrality, matrix positivity and nonsingularity remain OPEN. |
| Coordinate norm x^2+D*y^2 | `latticePoint_normSq` | Proved for the complex embedding using sqrt(D) with D>=0. This is not yet a number-field/discriminant definition. |
| v_p(det G)>=2F(p), Hadamard and aggregate upper_B | None | OPEN for the actual construction and parameters. |
| 250 saved intervals: endpoint stitching | `checkChain_sound`, `ender_chain_checked`, `ender_integer_coverage` | Kernel-checked coverage on [7e11,10^36). `verify_sources.py` matches all saved endpoint pairs and pins source bytes. No Arb margin is thereby certified. |
| 250 numerical contradictions | None | OPEN: reification into kernel-checkable rational/analytic certificates and their semantic link. |
| Floor-safe universal determinant envelopes | Partial | `ender_slope` proves the coefficient; determinant/envelope inequalities and geometry remain OPEN. |
| Decrease of actual C=80 error terms | `enderError_expansion`, `enderError_antitone` | Exact error expression and antitonicity on u>=1. Numerical endpoint margin remains OPEN. |
| All-u propagation | `positive_envelope`, `ender_positive_from_endpoint` | CONDITIONAL: endpoint positivity is an explicit hypothesis, not a theorem here. |
| CRT sieve on [92,7e11) and its soundness | None | OPEN: the saved survivor list is not a Lean proof. |
| Reduced-form enumeration below 92 and class-number correspondence | None | OPEN: not replaced by a finite-list axiom or a disguised definition. |
| Exact derivative-row moment identities | `row_diagonal`, `row_radial_cross`, `traceGram_diagonal`, `traceGram_radial_cross` | Proved for every finite complex point set, including the origin and nonsymmetric sets, with the actual derivative cutoff. The successor diagonal retains its unmatched derivative column. |
| Scalar radial correlation and two-row matrix determinant | `weighted_correlation_bound`, `weighted_block_bound`, `momentMatrix_bound` | Proved for finite weighted moments with explicit multiplier range. Instantiation of that bounded-multiplier representation for the derivative rows remains OPEN. |
| Annular derivative multiplier parameter bound | `derivative_multiplier_bound` | Numeric r,J inequality proved; the factorial-ratio/actual-row multiplier bridge remains OPEN. |
| 9/25 constant and necessity of bounded multipliers | `radial_constant_attained`, `multiplier_range_is_essential` | Exact moment-class controls; not sharpness or a counterexample inside every derivative-row family. |
| Origin and extra derivative column | `traceGram_origin_control`, `traceGram_unmatched_column_control`, `traceGram_cross_cutoff_control` | Exact entry controls: origin diagonal 2; successor diagonal at z=1 is 4; corresponding cross entry 2. |
| Disjoint-block Fischer product and Smith filtration | None | OPEN in this project; finite Python campaigns are not renamed as Lean proofs. |
| Guaranteed normalized pair-saving ceiling | `normalized_pair_gain` | Algebraic inequality under R,S>0, c>=0 and 2m<=RS; no bound on all possible actual savings. |
| h(-D)=1 implies D in {3,4,7,8,11,19,43,67,163} | None | OPEN. No theorem, surrogate predicate, assumed structure field or custom axiom asserts this conclusion. |

## Strongest surviving results and main obstruction

The universal floor-sum identity, principal-form bound, weighted-moment determinant inequality, exact derivative-row moment identities, actual error decay and endpoint coverage are checked component results. The load-bearing obstruction to end-to-end certification is the missing field/determinant/analytic/finite chain, not an identified counterexample to the mathematical argument.

The source-to-Lean comparison is explicit about natural-number subtraction, positive Python divisor domain, derivative truncation, and interval endpoints. Kernel checking does not silently certify the Python implementation or turn a saved decimal margin into a real inequality.

## Next bounded bridge

Construct the full finite real trace-Gram matrix from `derivativeRow` and prove its positive-semidefinite property from a sum of squares, then instantiate an appropriate determinant upper bound. Positive definiteness and positive determinant must require an actual independence argument, not a Boolean flag.

Controls must include a single nonzero row, duplicate rows, the origin and the unmatched-column example. A positive-determinant claim on duplicate rows kills the attempted bridge. Stop at the exact Gram/upper-bound theorem; do not promote global class-number closure until the remaining obligations are discharged.

## Independent-witness boundary

Proof construction, the coverage recurrence and test design were authored in the same review loop. Lean's kernel supplies a distinct proof-checking implementation, but not independent assurance that all formal statements capture the intended mathematics. No human or independently authored semantic review is recorded. Standard axioms are allowed; extra axioms, incomplete proofs and native-evaluation dependencies are rejected by the tested audit gate.
