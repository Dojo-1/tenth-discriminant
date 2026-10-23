# Current claim-to-Lean map

**The interpolation/Gram positivity chain is connected. The class-number
classification chain is not.** This map supersedes the PR #8-era coverage
summary previously stored here; Git history preserves that record. Stage notes
remain useful derivations, but their old frontier descriptions are historical.

Read the [human proof](HUMAN_GUIDE.md), then inspect the linked source statement.
"Proved" below means the encoded implication under its explicit hypotheses,
not that its intended application or all of its hypotheses have been proved.

## 1. One public entry point

[`Interpolation.lean`](TenthDiscriminant/Interpolation.lean) exposes the original
`rectangularTraceGram P J R S` without requiring the caller to reconstruct the
row labels or prove their injectivity.

```text
P: finite set of distinct complex points
R >= 1, S >= 1, J >= S
card P > 2*(R-1)+(S-1)
-------------------------------------
G is positive definite
0 < det G <= product of its diagonal entries
```

Declarations: `rectangularRowLabels_injective`,
`rectangularTraceGram_posDef_of_point_count`, `rectangularTraceGram_det_bounds`.
No independence, positive determinant, nonzero resultant or irreducibility
premise occurs in these public statements. They are direct specializations of
the existing all-factor proof, not a replacement matrix or a stronger cutoff.

[`LatticeEllipse.lean`](TenthDiscriminant/LatticeEllipse.lean) now provides a
concrete input. `ellipsePairs` is the full integer-radius norm ellipse for
natural D>0; `ellipsePoints` is its complex image. `mem_ellipsePairs_iff`
proves the finite box does not truncate the ellipse, `latticePoint_injective`
and `ellipsePoints_card` prove distinctness and preserve its count, and
`ellipseTraceGram_det_bounds` applies the same matrix theorem under the
explicit count hypothesis. The count itself is **not** established in Lean for
Ender's chosen D and radius.

The [cell-covering proof](../research/ender_radius_bridge/PROOF.md) establishes
that count mathematically for the chosen radius. The area argument is not in
Lean. Lean does check `ellipsePairs_antitone_D`, its card consequence, and
`ellipseTraceGram_det_bounds_of_ender_guard`: a `3R+S` count at finite-interval
upper endpoint D2 propagates to each D≤D2 and then to the original matrix.

[`IntegerTraceGram.lean`](TenthDiscriminant/IntegerTraceGram.lean) identifies
that matrix with exact integer coordinates. For any finite pair set and D>0,
`integerTraceGramEntry_cast` proves the original real trace entry equals the
cast integer pairing sum; `integerRectangularTraceGram_cast` and
`integerRectangularTraceGram_det_cast` carry this to the canonical matrix and
determinant. `ellipseIntegerTraceGram_cast` specializes it to `ellipsePairs`.
The proof uses multiplication/conjugation transport, not finite-case
comparison or an assumed matrix equality. The selected pair lattice is not
asserted to be the full ring of integers.

## 2. The connected interpolation proof

Names in this section are in `TenthDiscriminant`, with the `JetAssembly` prefix
where shown.

| Mathematical obligation | Source / principal declaration | Boundary retained |
|---|---|---|
| Actual ordinary derivative rows and trace entries | [TraceGram](TenthDiscriminant/TraceGram.lean): `derivativeRow`, `traceGramEntry`, `traceGram_diagonal` | W fixed during differentiation; factor two; origin and truncated derivatives retained. |
| Full real matrix, energy and PSD | [GramMatrix](TenthDiscriminant/GramMatrix.lean): `traceGramMatrix_factorization`, `traceGramMatrix_quadratic`, `traceGramMatrix_posSemidef` | PSD includes duplicate labels and singular cases. |
| Ordinary Hadamard upper bound | [GramHadamard](TenthDiscriminant/GramHadamard.lean), [GramMatrix](TenthDiscriminant/GramMatrix.lean): `traceGramMatrix_det_le_diag`, `traceGramMatrix_det_le_moments` | Not the aggregate analytic `upper_B` estimate or Fischer block product. |
| Kernel equals invisible real coefficient jets | [JetKernel](TenthDiscriminant/JetKernel.lean): `traceGramMatrix_kernel_iff`, `traceGramMatrix_posDef_iff`, `realJet_eq_polynomial_jet` | Complex row independence is sufficient, not equivalent to real Gram PD. |
| Fixed-size local determinant multiplicity | [DeterminantMultiplicity](TenthDiscriminant/DeterminantMultiplicity.lean), [SylvesterLocal](TenthDiscriminant/SylvesterLocal.lean): `fixedDerivativeSylvester_multiplicity_at_nonzero` | Explicit degree windows; no resizing at degree loss; zero determinant allowed at this layer. |
| Nonzero determinant from a bounded syzygy kernel | [SylvesterNonzero](TenthDiscriminant/SylvesterNonzero.lean): `NonzeroBridge.coeffMatrix_det_ne_zero` | Exact degree and derivative coprimality; field-level helper has a proved matrix correspondence. |
| Irreducibility supplies nonzero determinant and fibers | [SylvesterIrreducible](TenthDiscriminant/SylvesterIrreducible.lean): `fixedDerivativeSylvester_ne_zero_of_irreducible`, `irreducible_positive_specialization_ne_zero` | Exact positive Z-degree; characteristic zero for derivative nonvanishing; irreducible over the stated ring. |
| Global W-degree bound | [SylvesterDegree](TenthDiscriminant/SylvesterDegree.lean): `fixedDerivativeSylvester_natDegree_le_positive` | Includes zero determinants; a degree bound alone is not nonvanishing. |
| Distinct-contact budget | [ContactBudget](TenthDiscriminant/ContactBudget.lean), [IrreducibleContact](TenthDiscriminant/IrreducibleContact.lean): `irreducible_fixedDerivativeSylvester_excessive_contact_card` | b>0 for cardinality cancellation; distinct parameters and actual root-power divisibility. Nonzero premises are derived in the irreducible theorem. |
| Actual bidegree and its product rule | [BivariateDegree](TenthDiscriminant/BivariateDegree.lean): `JetAssembly.swap_involutive`, `JetAssembly.wDegree_mul` | Exact coordinate exchange, not a sampled degree estimate. Additivity assumes nonzero factors. |
| All-factor exceptional-set budget | [FactorJetBudget](TenthDiscriminant/FactorJetBudget.lean): `JetAssembly.bad_mul_subset`, `JetAssembly.badParameters_card_le` | Pure-variable factors, zero fibers, repeated factors and injective coordinates retained. |
| Ordinary jets force the polynomial to vanish | [FactorJetBudget](TenthDiscriminant/FactorJetBudget.lean): `JetAssembly.polynomial_eq_zero_of_jet_count` | Characteristic zero, derivative depth above actual W-degree, sufficient strict sample count. |
| Actual conjugate sampling and Gram PD | [JetCountGram](TenthDiscriminant/JetCountGram.lean): `JetAssembly.polynomial_eq_zero_of_conjugate_jets`, `JetAssembly.traceGramMatrix_posDef_of_point_count` | P is a finite set; row labels injective; no assumption of independence or positivity. |

The field coefficient matrix and nested-polynomial matrix are different typed
presentations linked by `fixedSylvesterMatrix_map_to_field`. They are not
unrelated substitutes. In particular, a general field-valued map cannot be
replaced by a coefficient-ring endomorphism merely to shorten the proof.

## 3. Other proved components, without promoting their interpretation

| Component | Source / declarations | What is not supplied |
|---|---|---|
| Principal-form integer algebra and strict cutoff | [Arithmetic](TenthDiscriminant/Arithmetic.lean): `principalNorm_four`, `principalNorm_lower`, `small_norm_impossible`, `strict_cutoff`, `interval_strict_cutoff` | Identification with actual ideals/class groups; small-prime inertness. |
| Floor sums and valuation-weight arithmetic | [FloorSum](TenthDiscriminant/FloorSum.lean), [Arithmetic](TenthDiscriminant/Arithmetic.lean): `floorSum_closed`, `floorSum_scaled`, `sum_min_identity` | Legendre/prime-mass estimates and a link to determinant valuations. Lean's total division at zero is not Python division semantics. |
| Weighted two-row correlation and 9/25 | [Radial](TenthDiscriminant/Radial.lean), [MomentMatrix](TenthDiscriminant/MomentMatrix.lean): `weighted_correlation_bound`, `momentMatrix_bound`, `normalized_pair_gain` | Actual-row bounded-multiplier instantiation and the full Fischer product. Attainment in the moment class is not derivative-family sharpness. |
| Actual radial cross entries and lattice norm | [TraceGram](TenthDiscriminant/TraceGram.lean): `traceGram_radial_cross`, `latticePoint_normSq` | Arithmetic field/class-group construction. |
| Integer-pair trace matrix, real cast and determinant | [IntegerTraceGram](TenthDiscriminant/IntegerTraceGram.lean): `integerTraceGramEntry_cast`, `integerRectangularTraceGram_det_cast`, `ellipseIntegerTraceGram_det_cast` | Prime-power divisibility; equivalence of the verifier's separate half-integer-radius point generator. |
| Selected quadratic-order coordinates | [QuadraticCoordinates](TenthDiscriminant/QuadraticCoordinates.lean): `pairZsqrtdEquiv`, `pairZsqrtd_mul`, `integerPairTrace_eq_zsqrtd_re` | Equality with the full ring of integers for every D; any class-group theorem. |
| Residue trace-Gram and determinant detector | [ResidueTraceGram](TenthDiscriminant/ResidueTraceGram.lean): `residueTraceGramMatrix_eq_map`, `residueRectangularTraceGram_det_zero_iff_dvd`, collision and asymmetric controls | A valuation lower bound; an image-set replacement that discards colliding samples. |
| Generic two-sided determinant factor | [GramDivisibility](TenthDiscriminant/GramDivisibility.lean): `sq_dvd_det_of_gramShear_factor` | The required integral factorization for an arbitrary Gram matrix. |
| Fixed inert-prime Gram pilot | [InertPilot](TenthDiscriminant/InertPilot.lean): `inertPilotJet_dvd_three`, `inertPilotGram_factor`, `inertPilot_nine_dvd_det`, positive and noninert controls | General inert-prime theorem for arbitrary D, p and row grid. |
| Affine coefficient/determinant transport | [AffineCoefficients](TenthDiscriminant/AffineCoefficients.lean), [AffineTransport](TenthDiscriminant/AffineTransport.lean): `fixedDerivativeDeterminant_affine`, `affineTransport_witness_nonzero` | Invariance of the determinant value or prime valuations without tracking the explicit scale factor. |
| Exact interval coverage | [Coverage](TenthDiscriminant/Coverage.lean), [RecordedCoverage](TenthDiscriminant/RecordedCoverage.lean): `checkChain_sound`, `ender_integer_coverage` | The 250 Arb inequalities. Coverage is half-open at the final endpoint in this theorem. |
| Error decay and endpoint propagation | [Envelope](TenthDiscriminant/Envelope.lean), [EnvelopeDecay](TenthDiscriminant/EnvelopeDecay.lean): `ender_slope`, `enderError_antitone`, `ender_positive_from_endpoint` | Endpoint positivity and connection from the actual determinant to these envelopes. |
| Conditional blend inequalities | [GranuleCertificates](TenthDiscriminant/GranuleCertificates.lean) | Truth of externally supplied bounds, a probability of theorem truth, or methodological superiority. |
| Boundary examples | [ComparatorR1](TenthDiscriminant/ComparatorR1.lean), [ComparatorM2](TenthDiscriminant/ComparatorM2.lean), [AffineControls](TenthDiscriminant/AffineControls.lean), controls inside other modules | Universal Python-Lean equivalence, global classification or a performance claim. |

The numerical/experimental layers are not smuggled into the interpolation
proof as axioms. Likewise, endpoint correspondence does not turn a floating or
ball-arithmetic calculation into a kernel-checked inequality.

## 4. Open links in the classification argument

| Required link | Current status |
|---|---|
| Fundamental discriminants, actual quadratic rings, ideals/class groups and small-prime inertness under the class-number-one hypothesis | OPEN; integer norm lemmas are components, not these identifications. |
| Concrete integer-radius norm ellipse and required lower bound on its cardinality | Finite construction, exact membership, injectivity and upper-endpoint card transfer PROVED in Lean; the chosen-radius lower count has a complete geometric proof in `research/ender_radius_bridge/PROOF.md`, but its area step and radius instantiation are NOT Lean-checked. |
| Equality between the formal real Gram matrix and the integer-pair matrix with the same derivative rows and supplied point set | PROVED in Lean for D>0, including row-major rectangular and integer-radius ellipse specializations and determinant cast. This does not equate distinct point-set generators or duplicate-containing Python lists. |
| Reduction of that integer matrix, with the same original sample indexing, and equivalence between local determinant vanishing and global divisibility by m>0 | PROVED in Lean; this is a detector, not a lower bound. |
| Inert-prime divisibility and prime-adic valuation lower bound for that same integer determinant | OPEN in general; Lean proves the fixed D=19, p=3, R=4, S=2 canonical-matrix case `9 | det G` for all finite samples and derivative cutoffs, with a positive ellipse instance. |
| Full factorial/Legendre prime-mass inequality, remainder control and analytic upper bound | OPEN; selected floor-sum and moment identities are proved. |
| Kernel-checkable numerical contradictions, with their exact analytic interpretation | OPEN. |
| Universal envelope starting margin and its determinant bounds | OPEN; propagation is conditional. |
| CRT survivor certificate, reduced-form enumeration and class-number correspondence | OPEN. |
| End-to-end class-number-one classification | OPEN. |

Ender's stronger numerical guard `3*R+S < P.card` at J=S implies the abstract
interpolation guard; a regression instantiates this fact. That does not prove
the concrete ellipse satisfies the guard. The discriminant cutoff is unchanged.

## 5. Verification and human-review boundary

The baseline interpolation revision `d6c4876a316814aa0ac4ef1a719a13ea2822e620`
passed workflow `39863039414`. As checked against frozen current history on
23 October, PR #15 is merged at `47ec647` and PR #16 is merged at `4c034f9`.
The PR #16 source head `8aca367` passed pinned workflow `39897529309`, job
`120231301146`. That is the status of the checked source head; it must not be
silently extended to later edits or to the end-to-end classification claim.

For the human-facing objective audit and a record of the bounded preregistered
radial-control replay, see [`../TAO_OBJECTIVE_AUDIT.md`](../TAO_OBJECTIVE_AUDIT.md).
It does not add a formal premise or mathematical conclusion to this map.

The strengthened apparatus checks are:

- every project module is reachable from the root import graph;
- every logical constant under `TenthDiscriminant`, including private and
  unreferenced safe definitions/opaque values, has only the three permitted
  transitive axiom dependencies;
- unsafe runtime implementations are separately reported using Lean's own
  metadata, not a filename or name-suffix exemption;
- matched controls test the gate itself and the public rectangular API;
- all inherited mathematical controls remain active.

The import/source checks are structural checks, not a full Lean parser. The
compiled checker establishes formal validity, not external semantic correctness.
CI running the tests is not a second mathematical author. No human readability
study, blind independent semantic review, proof-completion percentage or
optimality claim is made.

The next formal geometric bridge is the cell-area lower bound and its radius
instantiation. The next arithmetic bridge is a genuine inert-prime valuation
bound for the now-identified integer determinant. Residue naturality detects
divisibility once established; it does not force it. No classification
conclusion follows yet.
