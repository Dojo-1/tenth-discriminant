# Current claim-to-Lean map

**The interpolation/Gram positivity chain is connected. The class-number
classification chain is not.** This map supersedes the PR #8-era coverage
summary previously stored here; Git history preserves that record. Stage notes
remain useful derivations, but their old frontier descriptions are historical.

**Phase 28 now closes the universal odd-discriminant cutoff.**
`FirstCertificate.odd_large_classNumber_ne_one` in `UniformUpperEnvelope`
requires only `D≥700000000000`, `Squarefree D` and `Fact ((D:Int)%4=3)`;
it concludes actual-field class number not one. `NormalizedComparison`
checks exact algebra and clipping, `UniformLowerEnvelope` bounds the lower
side, `UniformRadiusFamily` supplies the new fixed family's geometric and
arithmetic guards, and `UniformUpperEnvelope` proves the upper side and
composes the contradiction. No numerical premise remains. The older
campaign's other 249 certificates need not be checked for this theorem;
their records remain unchanged. Even cases and finite classification are
not asserted. [Short human proof](../research/ender_radius_bridge/ODD_CUTOFF_GUIDE.md).
The phase descriptions below retain their historical scope.

Phases 25–26 close the first saved interval's class-number exclusion.
`LogEnclosure` and
`IntegerLogCheck` bound logs; `DivisionWitness` checks supplied floor sums
and complete prime-power lists; `NumericalCertificate` aggregates a complete
checked table. `FirstIntervalGuards` proves the exact radius/padding guards,
and `FirstIntervalScalars`/`FirstIntervalConclusion` reduce exclusion to two
integer budgets on that table.
`FirstIntervalData` contains generated data; `FirstIntervalRows` now proves
every row valid. `FirstIntervalCoverage` proves complete prime coverage and
`FirstIntervalTotals` proves both budgets. `FirstIntervalChecked` composes
them into `first_interval_classNumber_ne_one` for squarefree `D≡3 (mod 4)`
in `[700000000000,875000000000]`, with no numerical premise. These modules
have built locally. Resource failures
are preserved, not silently converted into a proof.

Phase 27 adds bounds uniform in the rectangle dimensions, not another
class-number range. `UniformPrimeMass` proves the floor/geometric and
retained-prime estimates plus clipping on the same production masses.
`PrimeLogCertificate` and `PrimeLogConstants` certify four fixed prime-log
constants. `UniformPrimeMassCertified` gives arbitrary-R,S bounds and
`classNumber_ne_one_of_certified_budget_comparison`, retaining all geometric,
arithmetic and strict-comparison guards. The unchanged first interval's
budgets are recovered as a checked pilot. [Human guide](../research/ender_radius_bridge/UNIFORM_PRIME_MASS_GUIDE.md).

Read the [mathematical spine](MATHEMATICAL_SPINE.md) first, then the
[detailed human proof](HUMAN_GUIDE.md) and linked source statements.
"Proved" below means the encoded implication under its explicit hypotheses,
not that its intended application or all of its hypotheses have been proved.

Phase 14's [coordinate criterion](TenthDiscriminant/MaximalOrderCoordinates.lean)
is checked: squarefree `D≡3 (mod 4)` plus integral rational trace/norm
forces unique half-integral coordinates. Phase 15's
[field chart](TenthDiscriminant/QuadraticFieldChart.lean) transports
this into the actual quadratic number field and proves a ring
equivalence with its maximal integer ring. Phase 16's
[class-number bridge](TenthDiscriminant/ClassNumberInertBridge.lean)
now composes that equivalence with the residue quotient and the
principal-ideal theorem to prove the strict local Gram valuation.

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
explicit count hypothesis. Phase 18 now discharges that count for Ender's
chosen-radius guard.

The [cell-covering proof](../research/ender_radius_bridge/PROOF.md) explains
that count mathematically for the chosen radius. Phase 17 checks the exact
radius-to-strict-count step (`ellipsePairs_card_gt_of_ender_radius_and_area`)
and its upper-endpoint composition with the actual Gram
(`ellipseTraceGram_det_bounds_of_ender_radius_and_area`). Phase 18's
[`EllipseCellArea.lean`](TenthDiscriminant/EllipseCellArea.lean) proves the
missing area inequality by an exact closed-cell covering and measure bound,
then exposes unconditional `ellipsePairs_card_gt_of_ender_radius` and
`ellipseTraceGram_det_bounds_of_ender_radius`. Existing
`ellipsePairs_antitone_D` carries the upper-endpoint count to each D≤D2.

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
| Generic two-sided determinant factor | [GramDivisibility](TenthDiscriminant/GramDivisibility.lean): `sq_dvd_det_of_gramShear_factor`, `pow_dvd_det_of_unimodular_gram_factor` | Construction of the rectangular unitriangular basis and its integral jet quotients. |
| Universal one-factor jet under an explicit congruence | [FrobeniusJet](TenthDiscriminant/FrobeniusJet.lean): `frobeniusJet_zero`, `frobeniusJet_dvd_of_zero_congruence`, noninert negative control | Proof of the order-zero congruence from inertness; product-power and rectangular-basis instantiation. |
| Exact exponent of the proposed rectangular basis | [RectangularValuation](TenthDiscriminant/RectangularValuation.lean): `sum_rectangularBasisExponent`, `rectangularTraceGram_valuation_of_basis_factor` | The theorem assumes an integral unimodular basis factorization; it does not construct the polynomial rows, quotient jets, or inertness premise. |
| Explicit sample-independent rectangular basis matrix | [RectangularBasisMatrix](TenthDiscriminant/RectangularBasisMatrix.lean): `rectangularBasis_term_bounds`, `rectangularBasisMatrix_lowerTriangular`, `rectangularBasisMatrix_det`, full-row pilot | This module establishes the matrix and determinant one; the later row-action theorem below identifies its action on actual jets. |
| Actual rectangular row action | [RectangularRowAction](TenthDiscriminant/RectangularRowAction.lean): `rectangularBasisMatrix_integerDerivativeRow_action`, `rectangularBasisMatrix_actualRow_dvd` | Exact action and jet divisibility use ordinary derivatives; the latter assumes the coordinatewise Frobenius congruence. |
| Integral Gram factor and exact determinant power | [RectangularGramFactor](TenthDiscriminant/RectangularGramFactor.lean): `rectangularTraceGram_basis_factor_of_frobenius`, `rectangularTraceGram_valuation_of_frobenius` | Constructs the previously assumed middle integer matrix on the original samples. The universal Frobenius premise remains explicit; no inertness or classification theorem is inferred. |
| Inert quadratic residue to universal Frobenius | [QuadraticResidueRing](TenthDiscriminant/QuadraticResidueRing.lean) and [InertFrobenius](TenthDiscriminant/InertFrobenius.lean): `residuePair_pow_conj_of_nonsquare`, `integerPair_frobenius_of_nonsquare`, `rectangularTraceGram_valuation_of_nonsquare` | For odd prime `p`, nonsquareness of `-D : ZMod p` suffices for the exact exponent on the original integer Gram. Phase 16 now derives that guard from class number one in the specified strict small-prime range. |
| Small-prime norm gate | [SmallPrimeBridge](TenthDiscriminant/SmallPrimeBridge.lean): `small_prime_no_root_of_norm_lifting`, `quadratic_irreducible_iff_nonsquare`, `rectangularTraceGram_valuation_of_small_prime_norm_lifting` | This module alone assumes root-to-principal-norm lifting; Phase 16 now derives it from class number one for squarefree `D≡3 (mod 4)`. Strict `p<(D+1)/4`; `D=15,p=3` falsifier. |
| Abstract class-number-one quotient norm | [PrincipalIdealBridge](TenthDiscriminant/PrincipalIdealBridge.lean): `residueKernel_absNorm`, `exists_integer_of_absNorm_of_classNumber_one` | For any number field, a map from its integer ring to `ZMod n` and class number one give an algebraic integer of norm magnitude `n`. Phase 16 composes this with the specific quadratic root quotient and the norm sign. |
| Quadratic root to explicit half-order quotient | [HalfOrderResidue](TenthDiscriminant/HalfOrderResidue.lean): `halfOrder_root_of_quadratic_root`, `halfOrderResidueMap`, `halfOrderResidueMap_surjective` | For `D ≡ 3 (mod 4)` and odd prime `p`, a root of `X²+D` gives a surjective map from `ℤ[T]/(T²-T+(D+1)/4)` to `ZMod p`. Phase 16 composes this with the maximal-ring equivalence. |
| Explicit order multiplication chart | [HalfOrderNorm](TenthDiscriminant/HalfOrderNorm.lean): `halfOrder_root_sq`, `halfOrder_mul_root`, `halfOrderMultiplicationMatrix_det` | The quotient relation, second multiplication column, and determinant `x²+xy+cy²` are checked. |
| Explicit order algebraic norm | [HalfOrderAlgebraicNorm](TenthDiscriminant/HalfOrderAlgebraicNorm.lean): `quadraticOrder_norm`, `halfOrder_norm_eq_principalNorm` | A reindexed power basis and the actual left-multiplication matrix identify Mathlib's `Algebra.norm ℤ (x+yT)` with `x²+xy+cy²`, and with the existing `principalNorm`. This is an order theorem, not a maximal-order identification. |
| Maximal-order field chart | [QuadraticFieldChart](TenthDiscriminant/QuadraticFieldChart.lean): `quadraticFieldPoly_irreducible`, `quadraticField_integral_coordinates`, `halfOrderEquivRingOfIntegers`, `halfOrder_ringOfIntegers_norm` | For squarefree `D ≡ 3 (mod 4)`, the explicit order is exactly the maximal integer ring of the genuine quadratic field and its norm is `principalNorm`. |
| Class-number-one to local determinant valuation | [ClassNumberInertBridge](TenthDiscriminant/ClassNumberInertBridge.lean): `smallPrimeNormLifting_of_classNumber_one`, `rectangularTraceGram_valuation_of_classNumber_one`, `fifteen_classNumber_ne_one` | For squarefree `D≡3 (mod 4)` and odd prime `p<(D+1)/4`, class number one gives Ender's exact exponent for the actual integer Gram. The area/analytic/classification chain is separate. |
| Finite prime-mass assembly on the chosen-radius Gram | [PrimeMassAssembly](TenthDiscriminant/PrimeMassAssembly.lean): `ellipse_allOddPrimeMass_hadamard_sandwich`, `ellipse_allOddPrimeMass_log_le_hadamard` | The product of all distinct odd-prime factors below `R` divides the same positive integer determinant, and `∑ 2F(p) log p ≤ log(∏ Gᵢᵢ)`. Requires squarefree `D≡3 (mod 4)`, class number one, strict `R<(D+1)/4`, and the exact radius guard. It does not supply Ender's factorial estimate or certify Arb margins. |
| Production Hadamard upper expression at integer radii | [EnderUpperB](TenthDiscriminant/EnderUpperB.lean): `enderUpperB_eq_production_coefficients`, `ellipseTraceGram_log_diag_le_upperB`, `ellipse_primeMass_log_le_upperB` | For positive integer `rho<R`, the exact production expression bounds the actual diagonal product and the finite odd-prime mass. Its sample-count premise is supplied by Phase 21; Arb evaluation remains separate. |
| Upper ellipse count and counted upper formula | [EllipseUpperCount](TenthDiscriminant/EllipseUpperCount.lean): `ellipsePairs_card_le_upper_count`, `ellipsePairs_card_le_padded_upper_count`, `ellipse_primeMass_log_le_counted_upperB` | Disjoint inward cells and exact axis bounds prove the unchanged upper count, transport it from the lower endpoint, and compose with the chosen-radius class-number theorem. Padding the exact vertical floor upward is allowed under an explicit guard. No Arb-floor equality is assumed. |
| Ordinary-jet powers in the selected quadratic order | [JetPower](TenthDiscriminant/JetPower.lean): `jet_power_dvd`, `rectangular_frobenius_row_jet_coordinates`, Hasse negative control | The order-zero congruence is assumed. The later row-action theorem identifies these jets with the actual integer Gram rows. |
| Conjugation operator on local samples | [LocalOperators](TenthDiscriminant/LocalOperators.lean): `pairConj_involutive`, `frobenius_congruence_conj`, `frobeniusJet_conj_dvd`, non-real pilot | Closes the explicit Frobenius premise under one symmetry; does not derive the premise from inertness or change the global class-number hypothesis. |
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
| Fundamental discriminants, actual quadratic rings, ideals/class groups and small-prime inertness under the class-number-one hypothesis | PROVED in Lean for squarefree `D≡3 (mod 4)` and strict small odd primes: the explicit order is the maximal integer ring; a residue root gives a quotient, class number one gives a principal element of absolute norm `p`, norm nonnegativity gives exact norm `p`, and the actual integer Gram has the required valuation. Even-discriminant variants, numerical certificates, universal closure and classification remain open. |
| Concrete integer-radius norm ellipse and required lower bound on its cardinality | Finite construction, exact membership, injectivity, cell-area inequality, chosen-radius strict count and upper-endpoint Gram transfer PROVED in Lean for `D>0` under the exact radius guard. The area proof uses closed cells; boundary overlap is harmless because only finite-union subadditivity is needed. |
| Equality between the formal real Gram matrix and the integer-pair matrix with the same derivative rows and supplied point set | PROVED in Lean for D>0, including row-major rectangular and integer-radius ellipse specializations and determinant cast. This does not equate distinct point-set generators or duplicate-containing Python lists. |
| Reduction of that integer matrix, with the same original sample indexing, and equivalence between local determinant vanishing and global divisibility by m>0 | PROVED in Lean; this is a detector, not a lower bound. |
| Inert-prime divisibility and prime-adic valuation lower bound for that same integer determinant | [Uniform proof](../research/uniform_inert_valuation/PROOF.md) gives the full exponent. Lean identifies the actual derivative-row action, constructs the integral Gram factor, derives universal Frobenius from **odd-prime nonsquareness of `-D : ZMod p`**, and proves the exact determinant power. Phase 16 derives that local condition from class number one for squarefree `D≡3 (mod 4)` and strict small odd primes. Phases 18–24 close the area and finite mathematical comparison; numerical interpretation, universal closure and classification remain open. |
| Ender's upper ellipse point-count estimate used as `n_up` | PROVED for `D>0` and natural radius. The exact natural floor gives the mathematical bound; any upward padding is allowed under `floor≤Y` (also derivable from `rho/sqrt(D)<Y+1`). Interpreting the program's Arb endpoint still requires a numerical certificate theorem. |
| Exact factorial/Legendre identity and scalar lower estimate | PROVED in [FactorialPrimeMass](TenthDiscriminant/FactorialPrimeMass.lean): `factorialMass_eq_prime_power_sum`, `factorialLower_le_mass`, `factorialLower_le_prime_power_sum`. The finite factorial sum includes prime `2`; the unchanged scalar expression requires `R≥2`. This is not yet the determinant's odd-prime valuation mass. |
| Finite `prime_mass` weight conversion and clipping | PROVED in [PrimeMassLower](TenthDiscriminant/PrimeMassLower.lean): exact staircase identity, small-prime split, finite geometric and floor-square losses, production integer coefficients/padding/branch, and `enderPrimeMassLower_le_exact_of_tail`. The actual-Gram composition `ellipse_enderPrimeMassLower_le_upperB` is CONDITIONAL on the displayed finite reciprocal-prime sum being at most the supplied `I`. |
| Analytic tail estimate supplying production `I(P)` | PROVED in [PrimeTail](TenthDiscriminant/PrimeTail.lean): `largeReciprocalTail_le_enderTailIntegral`. A positive potential and finite telescoping dominate all integer summands, hence their prime subset, for `P≥2`. No prime-distribution input or infinite sum. |
| Connected finite mathematical lower/upper comparison | PROVED: `ellipse_enderPrimeMassLower_le_counted_upperB` in [PrimeTail](TenthDiscriminant/PrimeTail.lean) has no tail premise. Arithmetic, class-number, strict range, radius and floor-padding guards remain. `classNumber_ne_one_of_ender_comparison` excludes class number one only when the strict real numerical comparison is supplied. No saved Arb inequality is assumed true. |
| Kernel-checkable numerical contradictions, with their exact analytic interpretation | PROVED for the first saved interval, squarefree `D≡3 (mod 4)`: `first_interval_numeric_bounds`, `first_interval_strict_comparison`, `first_interval_classNumber_ne_one` in [FirstIntervalChecked](TenthDiscriminant/FirstIntervalChecked.lean). No numerical premise remains there. Other 249 intervals remain open; no global cutoff. |
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

The geometric count, local factors and their exact finite-product/logarithmic
comparison on one determinant are now checked. Production `upper_B` is also
connected at integer radii, with its count input now proved by inward cells
and axis accounting. The exact factorial identity and scalar lower bound are
now checked. Finite weight conversion, geometric losses and clipping reach
the same Gram. The reciprocal-prime tail is now proved by finite potential
drops. Phase 26 also closes the first bounded numerical exclusion with
its exact guards. The other intervals, universal closure, even cases and
classification remain open. Earlier stages identified
`H^k` polynomial jets with a concrete unitriangular change on the actual
integer Gram, then establish the inertness interface of
the [paper valuation proof](../research/uniform_inert_valuation/PROOF.md).
Residue naturality detects divisibility once established; it does not force
it. No classification conclusion follows yet.
