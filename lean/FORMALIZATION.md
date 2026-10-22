# Claim-to-Lean map

**The main classification remains unformalized.** This table distinguishes proved components from unresolved links. A conditional helper does not discharge its hypotheses. Declaration names below are in namespace `TenthDiscriminant`; consult the corresponding source and the CI result for the exact revision. This is not a percentage-of-proof metric.

| Source obligation | Lean artifact | Boundary |
|---|---|---|
| Principal quadratic form and nonrational norm threshold | `principalNorm_four`, `principalNorm_lower`, `small_norm_impossible` | Integer algebra proved. Identification with the ring of integers and principal ideals is not yet formalized. |
| h(-D)=1 forces prime D=3 mod 8 and inert small primes | None | OPEN: genuine number fields, absolute fundamental discriminants, class groups, ideal norms, ramification and splitting. |
| Strict R<(D+1)/4 throughout intervals | `strict_cutoff`, `interval_strict_cutoff`, endpoint controls | Integer cutoff proved. Does not by itself prove inertness. |
| Optimized A(q)=sum_{r<R} floor(r/q) | `floorSum_scaled`, `floorSum_closed` | Universal arithmetic identity; matches `tools/ender.py:floor_sum` for its positive-q domain. Lean's total division extends to q=0; Python's domain does not. |
| F(p) and its finite sum-of-minima identity | `valuationWeight`, `sum_min_identity` | Exact arithmetic defined/proved. Connection to det G valuations is OPEN. |
| Legendre superfactorial identity and log form | None | OPEN in this project. No prime-mass inequality imported as an axiom. |
| Integral factorial lower bound, small-prime subtraction, higher-power tail | None | OPEN: the complete prime_mass inequality, including positivity and truncation. |
| Ellipse point counts and interpolation/nonvanishing | None | OPEN for the actual evaluation set. `rank_guard_impossible` proves only failure of the sufficient guard when n<=R+S. |
| Derivative trace Gram, integrality and positivity | None | OPEN for the actual construction. |
| v_p(det G)>=2F(p), Hadamard and aggregate upper_B | None | OPEN for the actual construction and parameters. |
| 250 saved intervals: endpoint stitching | `checkChain_sound`, `ender_chain_checked`, `ender_integer_coverage` | Kernel-checked coverage on [7e11,10^36). `verify_sources.py` matches all saved endpoint pairs and pins source bytes. No Arb margin is thereby certified. |
| 250 numerical contradictions | None | OPEN: reification into kernel-checkable rational/analytic certificates and their semantic link. |
| Floor-safe universal determinant envelopes | Partial | `ender_slope` proves the coefficient; determinant/envelope inequalities and geometry remain OPEN. |
| Decrease of actual C=80 error terms | `enderError_expansion`, `enderError_antitone` | Exact error expression and antitonicity on u>=1. Numeric endpoint margin remains OPEN. |
| All-u propagation | `positive_envelope`, `ender_positive_from_endpoint` | CONDITIONAL: endpoint positivity is an explicit hypothesis, not a theorem here. |
| CRT sieve on [92,7e11) and its soundness | None | OPEN: the saved survivor list is not a Lean proof. |
| Reduced-form enumeration below 92 and class-number correspondence | None | OPEN: not replaced by a finite list axiom or a disguised definition. |
| Exact derivative-row moment identities | None | OPEN, including derivative cutoffs, conjugation and the unmatched-column case. |
| Scalar radial correlation and two-row matrix determinant | `weighted_correlation_bound`, `weighted_block_bound`, `momentMatrix_bound` | Finite weighted moments with explicit multiplier range. Derivative rows are not silently identified with this matrix. |
| Annular derivative multiplier bound | `derivative_multiplier_bound` | Numeric r,J inequality proved; its application to actual derivative rows remains OPEN. |
| 9/25 constant and necessity of bounded multipliers | `radial_constant_attained`, `multiplier_range_is_essential` | Exact scalar-moment controls; not sharpness or a counterexample inside every derivative-row family. |
| Disjoint-block Fischer product and Smith filtration | None | OPEN in this project; finite Python campaigns are not renamed as Lean proofs. |
| Guaranteed normalized pair-saving ceiling | `normalized_pair_gain` | Algebraic inequality under R,S>0, c>=0 and 2m<=RS; no bound on all possible actual savings. |
| h(-D)=1 implies D in {3,4,7,8,11,19,43,67,163} | None | OPEN. No Lean theorem, surrogate predicate, assumed structure field or custom axiom asserts this conclusion. |

## Review and stop conditions

The first discriminator for each new module is an exact statement match, not whether automation finds a proof. Existing number-field and determinant dependencies must be attached to the actual objects before promoting the endpoint claim. The next bounded bridge is the derivative-row-to-moment identity, including the origin and derivative saturation boundary. A failed origin/cutoff case blocks that bridge; passing finite controls alone does not close it.

The universal arithmetic identities and scalar radial bound are the strongest current component results. The load-bearing obstruction to end-to-end certification is the missing determinant/arithmetic/analytic chain, not an alleged counterexample to the paper.

Proof construction, the coverage recurrence and test design were authored in the same review loop. Lean's kernel provides a distinct proof-checking mechanism, but not independent assurance that the formal statements capture every intended theorem. Human or independently authored semantic review remains absent.
