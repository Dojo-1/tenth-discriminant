# Current claim-to-Lean map

`ExcludedPrime.excluded_prime_budget_log_div` is now production-root reachable.
It bounds the original total prime mass by the actual Gram Hadamard ceiling
plus an explicit loss from a supplied excluded-prime prefix bound B. The
canonical log(n)/n kernel, its signs and monotonicity, and the domination
2pF<=R(R-1)S are proved internally. Phase59 core is transported with a
namespace change; all old production proofs/pins/tools stay unchanged.
Local target/root,34-input exclusions and4821/4071/16978 audit pass; controls
and exact-head CI have their own status in the [record](../research/ender_radius_bridge/PHASE61_VERIFICATION.md).
[Human proof](../research/ender_radius_bridge/COUNT_TO_LOSS_GUIDE.md).
API/audit controls pass; the local full negative suite is INCOMPLETE after
its existing120-second multiplicity limit, with no rerun. New CI is pending.
No arithmetic B, higher-class-number cutoff or new semantic review follows.


The [Phase60 boundary diagnostic](../research/ender_radius_bridge/SPLIT_COUNT_BOUNDARY_GUIDE.md)
finds a counterexample to a suggested per-form estimate in the unreviewed
higher-class-number count derivation. This is exact arithmetic and a paper
argument, not a new Lean result. The aggregate bound and h<=2 cutoff are
not refuted by this test; no production proof depends on this candidate.

A [standalone Phase59 prototype](../research/ender_radius_bridge/EXCLUDED_PRIME_PROTOTYPE_GUIDE.md)
now checks the actual-Gram excluded-prime budget and positive-kernel count
transfer. Its arithmetic count/weight inputs stay explicit. It is outside
the production root and existing CI, and outside Phase58 review coverage.
No new cutoff or higher-class-number result is supplied.

The [Phase58 bounded review](../research/ender_radius_bridge/PHASE58_VERIFICATION.md)
now covers the final50b and exact-staircase changes at frozen63be64b.
It established no concrete FATAL/GAP/SLOPPY finding in six obligations;
local calculations were re-derived and inherited machinery source-traced.
Lean/CI were NOT RERUN by the reviewer. This is not human review or
whole-library certification; the first native report remains unchanged.

`valuationWeight_exact_of_last_threshold` proves the exact real-cast
identity6F=S(S-1)(3R-p(S+1)) under p>0 and p(S-1)<=R.
`clippedFloorSum_succ` counts rows reaching the next column level;
`clippedFloorSum_closed` sums those increments. Guard counterexamples and
coexistence with the old false unguarded floor identity are checked.
Target/full build, signatures and4772/4028/16971 audit pass locally.
[Human count](../research/ender_radius_bridge/STAIRCASE_EXACT_GUIDE.md) and
[scope](../research/ender_radius_bridge/PHASE57_VERIFICATION.md). No change
to the50b cutoff or existing valuation exponents; no new semantic review.

`totallyComplex_degree_two_classNumber_one_discriminant_bound_50b`
proves actual absolute discriminant<50000000000 under the standard
totally-complex/degree-two/actual-class-number-one hypotheses.
`StrongSmallPrimeRecoveryGain` proves the81/1000 gain from the same
weights; `FiftyBillionCutoff` composes the450^4 geometry helpers, certified
tail and actual-Gram comparison. Old100b/62.5b conclusions remain.
Full local root, controls, fresh25-input exclusions and4755/4012/16968
audit pass. [Human proof](../research/ender_radius_bridge/FIFTY_BILLION_GUIDE.md)
and [verification](../research/ender_radius_bridge/PHASE56_VERIFICATION.md).
Earlier review55 is frozen at86abe21 and does not cover these edits.
New exact-head CI and independent human semantic review remain separate.

The [Phase55 review](../research/ender_radius_bridge/PHASE55_REVIEW_REPORT.md)
checked six joints of the new62.5-billion proof at frozen86abe21. It
established no FATAL/GAP finding, re-derived new local calculations and
source-traced inherited apparatus. It did not rerun Lean/CI or establish
human/model-family independence. No proof changed; [limits and provenance](../research/ender_radius_bridge/PHASE55_VERIFICATION.md).

`totallyComplex_degree_two_classNumber_one_discriminant_bound_recovered`
proves actual absolute discriminant<62500000000 from standard degree-two,
totally-complex and actual class-number-one hypotheses. It composes
the recovered prime weights with geometry checked at500^4, then transports
through the conjugation-based squarefree generator. The canonical and
odd-chart versions are in `RecoveredAnalyticCutoff.lean`.
Target/full root build, fresh21-input closure checks and4710/3967/16968
axiom audit pass. [Verification](../research/ender_radius_bridge/PHASE54_VERIFICATION.md)
and [human argument](../research/ender_radius_bridge/RECOVERED_CUTOFF_GUIDE.md).
The checked dependency closures exclude the listed finite-answer and
earlier-cutoff roots; publication CI remains separate.

`FirstCertificate.recovered_normalized_gap` proves a gain of at least3/50
over the certified proxy for S>=100 and25*S<=R<=26*S.
`raw_normalized_add_gain_le_recovered` transfers it to the raw expression.
The generic positive-p saturated-row count and p=0/S=1 controls are in
`SmallPrimeRecoveryGain.lean`. [Human proof](../research/ender_radius_bridge/NORMALIZED_RECOVERY_GUIDE.md).
This supplies a quantitative bridge, not a new discriminant endpoint.
Phase51 semantic review and Phase52 CI predate this module.
Local root/signature/controls/audit checks pass, with4687 logical declarations
and3944 theorems; [verification scope](../research/ender_radius_bridge/PHASE53_VERIFICATION.md).

`FirstCertificate.recoveredPrimeMassLower_le_production` restores the
exact3/5 contributions omitted by the uniform proxy, with no double-counting.
`certified_lt_recoveredPrimeMassLower` proves strict proxy improvement for
R>=4,S>=2. The production expression and determinant weights are unchanged;
that theorem alone does not export a new scaled affine envelope or cutoff.
Local root/signature/axiom checks pass. [Guide](../research/ender_radius_bridge/SMALL_PRIME_RECOVERY_GUIDE.md)
and [evidence scope](../research/ender_radius_bridge/PHASE52_VERIFICATION.md).
The Phase51 reviewer predates this addition; new-head CI remains separate.

The [Phase51 source review](../research/ender_radius_bridge/PHASE51_REVIEW_REPORT.md)
covers five bounded obligations in the new representation and symmetry
modules. It established no FATAL/GAP finding and identified one guide
dependency error, corrected after preservation; no Lean source changed.
It did not re-prove the inherited analytic chain or rerun compiled checks.
Exact-head CI, this bounded AI review and independent human semantic/API
review are distinct evidence. [Correction and provenance](../research/ender_radius_bridge/PHASE51_VERIFICATION.md).

`rectangularBasisMatrix_commutes_sign` and
`integerRectangularTraceGram_commutes_sign` prove compatibility of the
actual arithmetic and geometric matrices with the same integer diagonal
sign operator. The former requires positive odd p; the latter requires
central sample symmetry. The mixed-parity support theorem and prime-two
control are checked. [Typed operator guide](../research/ender_radius_bridge/PARITY_COMPATIBILITY_GUIDE.md).
Local root/signature/axiom checks pass; no quantitative gain is inferred.

`TenthDiscriminant.integerTraceGramEntry_eq_zero_of_central_symmetry`
proves mixed-parity zero entries of the original integer Gram under
sample negation stability; the ellipse instance and nonsymmetric entry2
control are checked. Local root/signature/audit checks pass. No stronger
valuation or smaller cutoff follows solely from this structure.
[Human sign-sector guide](../research/ender_radius_bridge/CENTRAL_SYMMETRY_GUIDE.md).

`ImaginaryQuadraticRepresentation` proves the missing generator existence
from standard field hypotheses, organized through conjugation and the
anti-invariant projector. The public
`totallyComplex_degree_two_classNumber_one_discriminant_bound` takes an
actual number field K, total complexity, rational degree two and actual
class number one only. No root, isomorphism, radicand or numerical premise
remains. [Operator guide](../research/ender_radius_bridge/CONJUGATION_BRIDGE_GUIDE.md).
Normalization excludes class-number/cutoff inputs in its fresh compiled
closure. Local root/input/audit checks pass. Pinned CI40208552511 passed at
proof head `2f519884`; its [final record](https://github.com/Dojo-1/tenth-discriminant/pull/28#issuecomment-6399919070)
does not substitute for later-head CI or human semantic review.
No general full-classification theorem is asserted by this addition.

The Phase48 [envelope diagnostic](../research/ender_radius_bridge/ENVELOPE_LIMIT_GUIDE.md)
is exact rational arithmetic outside Lean. It changes no declaration or
constant and does not establish failure of the determinant method.

`QuadraticGeneratorBridge` now constructs `imaginaryQuadraticEquivOfRoot`
from a supplied root a^2+d=0 and rational degree two of an actual number
field K. Root preservation and necessary degree are proved. The new
`classNumber_one_radicand_bound_of_quadratic_root` and
`classNumber_one_discriminant_bound_of_quadratic_root` transport the100b
bound with positive squarefree d and actual class number one; no field
isomorphism is assumed. [Scope and guard explanation](../research/ender_radius_bridge/GENERATOR_BRIDGE_GUIDE.md).
Phase47 now supplies its former squarefree-generator existence obligation
under the standard degree-two/total-complexity hypotheses.
Local root/input/audit checks pass; exact publication-head CI is separate.
The Phase45 review predates and covers neither new representation module.

Phase45 adds a [bounded fresh-context AI review](../research/ender_radius_bridge/PHASE45_REVIEW_REPORT.md)
of the new cutoff, with three arguments rederived and two inherited paths
source-traced. It changes no Lean declaration or proof. No contradiction
was established; fresh kernel acceptance and exhaustive dependency checking
were not repeated by that reviewer. Separate AI process does not establish
model-family independence or independent human semantic review.

Phase43's `TunedAnalyticCutoff` completes the preserved upper/actual-field
candidate with the unchanged mathematical body. Public actual radicand and
Mathlib absolute-discriminant bounds below100000000000 require only
positive-squarefree d and actual class number one. Full local root/input/
axiom checks pass; closures55436/55569/55772 exclude16 listed old cutoff,
classification and finite-answer inputs. Library156 modules, audit4602
logical/3868 theorem declarations. Publication-head CI is separate.
Phase42's incomplete attempt and its snapshot-specific no-leak check remain
historical; they are not rewritten to PASS on the new root. The Phase43
completion has its own evidence and preserves all original controls.
[Human proof](../research/ender_radius_bridge/HUNDRED_BILLION_GUIDE.md).

Phase42's TunedRadiusFamily compiled: universal dimensions, log/floor
bounds, normalized lower budget, integer radius rounding and chosen-radius
geometry on the fixed100-billion-scale family. Its upper/cutoff target
stopped at the registered time limit, so the unaccepted candidate is kept
outside the library. The root imports only the accepted geometry module;
no new100-billion cutoff declaration is supplied. Partial root/input/audit
verification passes locally:6809 steps,155 modules; geometry/lower input
closures13721/23486 exclude16 listed old inputs, and the no100b-declaration
check passes. Namespace audit4573 logical/3839 theorem declarations passes,
only permitted axioms. These checks do not compile the parked upper/cutoff
candidate; publication-head CI is separate. The checked actual cutoff
remains200 billion. [Human guide](../research/ender_radius_bridge/TUNED_CUTOFF_GUIDE.md).

Phase41 adds `AspectRatioLowerEnvelope`: the same actual raw prime-mass
lower expression now has an explicit linear aspect-ratio cost. Its guarded
statement, K=21/K=25.1 specializations, scalar separation/rejection and
floor counterexample compile. Fresh input closure and namespace audit pass;
no old cutoff/finite classification is used. This is not an all-D radius
or upper-envelope theorem. The separate one-input Arb pilot is not Lean
evidence. The actual checked cutoff stays200 billion; new-family universal
geometry, upper/lower conversion and composition remain open.
[Human guide](../research/ender_radius_bridge/ASPECT_RATIO_GUIDE.md).

Phase40 adds a [frozen same-route source comparison](../research/ender_radius_bridge/SAME_ROUTE_COMPARISON.md),
not a Lean theorem or an external-proof audit. Its key interface warning:
our factor-two trace-Gram determinant and the external minor-norm integers
are different objects. Shared ordinary derivatives/Frobenius relations do
not permit transferring constants or rank arguments without a new bridge.
No mathematical library or CI-gate source changes in this phase.

Phase39 adds `OptimizedAnalyticCutoff` and public actual radicand/absolute
field-discriminant bounds below200000000000, requiring only positive
squarefree d and actual class number one. `UniformRadiusFamily` supplies
the sharper guarded floor/log inequality and stronger normalized lower
bound; radius/dimension/error helper domains extend to the new endpoint.
The actual radius family and prime constants are unchanged. Old public
700-billion cutoff and classification STATEMENTS are retained.

The local whole library153-module build, public signatures, retained old/new
controls and compiled axiom audit pass. `Phase39InputCheck.lean` separately
checks that the new proofs do not depend on classification, finite
certificates, nine positives or the old cutoff. The frozen Phase38 input
inventory is not silently transferred to this changed proof tree. Exact-head
pinned CI40153287923 passed on mathematical headf163801, with security
40153286062 and all inherited rejection suites;
[final exact-head record](https://github.com/Dojo-1/tenth-discriminant/pull/28#issuecomment-6392486504).
New documentation heads require their own CI. [Human proof](../research/ender_radius_bridge/ANALYTIC_CUTOFF_OPTIMIZATION_GUIDE.md).

Phase38 adds an internally performed **local provenance snapshot**, outside
the mathematical library and existing CI gates. `Phase38Provenance.lean`
reuses Lean's compiled traversal, inventories types and opaque/private
bodies, and passes three matched traversal controls. Five fixed roots and
their reached source modules are recorded, with exact generic input
signatures checked separately. No mathematical source or theorem changes.
The class-number frontier inspected uses generic finiteness/PID/Minkowski
facts; no pre-existing classification input was identified. This does not
certify all methods by name matching or replace independent semantic review.
[Human proof-input map](../research/ender_radius_bridge/PROOF_INPUT_GUIDE.md).

Phase37 supplies the complete original finite interval and the public
`imaginaryQuadratic_classNumber_one_iff`: for positive squarefree d, actual
class number one iff d belongs to the nine-element list, with no range,
certificate or numerical premise. `ClassNumberClassification` composes
`QuotientFiberClassification` with `QuotientFiberCertified` and the existing
cutoff/positive cases. Its signed-discriminant corollary uses the actual
maximal-order discriminant. This is the canonical constructed field family;
a representation theorem for arbitrary field types is not asserted.

`QuotientFiberCore/Bridge` prove exact initial bits, periodic affine prime
transport, bit retention and absence of phantom bits. Data and thirteen
check groups supply all200 literal inverses/patterns. Eleven serialized
`QuotientFiberSeed..` modules cover every wheel seed and all785 quotient
positions. `QuotientFiberField` connects this certificate to the actual
class-number hypothesis. `QuotientFiberTransport` derives the unchanged old
first-translate statements from the stronger result; imports are acyclic.
The incomplete Phase36 pilot and separately registered Phase37 completion
are distinct evidence. Full build, compiled dependency audit and exact-head
pinned CI are required in the publication record. Independent human semantic
and upstream review remain open. [Human proof](../research/ender_radius_bridge/CLASSIFICATION_GUIDE.md).
All earlier finite-frontier descriptions below are historical.

Phase35 proves `classNumber_one_iff_below_first_period`, with only positivity,
squarefreeness and d<892371480 as hypotheses. `FusedWheelCore/Bridge` prove
universal all-predicate traversal equivalence and complete seed coverage;
`FusedWheelMasks/Primes` supply all literal checks. Eleven generated,
serialized `Fused35Q0S..` modules and `FusedWheelPilot` certify translate0.
`FusedWheelFieldBridge/Conclusion` connect it to the actual class number.
The cost pilot's five extra passing blocks are not a complete translate,
and its time stop/skips are preserved. Full classification above this finite
endpoint is not claimed. [Human proof](../research/ender_radius_bridge/FUSED_WHEEL_GUIDE.md).
All earlier finite-frontier descriptions below are historical.

Phase 34 adds `ResidueMaskCore` (thin Lean/Std-only computation) and
`ResidueMaskBridge`: `maskRootTest_eq`, `maskGuardedTest_eq`, `maskTests_eq`
and `maskWheelResidues_eq` prove exact correspondence with the old checker.
`ResidueMaskPilotData` contains generated literals, not an interval theorem.
Its 208 masks were checked locally in a separate experimental file. Four
fixed translate computations all exceeded the registered memory threshold;
none yielded a certificate. They do not supply the missing full-range
certificate. [Human explanation](../research/ender_radius_bridge/RESIDUE_MASK_GUIDE.md).

**Phase 33 closes all nine positive equalities and both directions below one million.**
`SmallIdealClassNumber` proves prime-norm residue maps, scalar ideal norms,
small-ideal principality and two Minkowski criteria without assuming class
number one. `RemainingPositiveClassNumber` supplies all five remaining
concrete applications, `known_nine_classNumber_one`, and
`classNumber_one_iff_below_million`. The iff requires only positive squarefree
d<1000000; the prime tests and finite certificate are supplied.
The actual field-discriminant identity/bound remains checked in
`QuadraticDiscriminant`. The whole upper interval is still unclosed, so
full classification is not asserted. [Human proof](../research/ender_radius_bridge/NINE_POSITIVE_GUIDE.md).
Older phase descriptions are historical where positive-case gaps are now closed.

**Phase 31 closes the necessary candidate list below one million.**
`SieveWheel` proves universal residue-lift and interval-coverage invariants.
`MillionSieve` checks the entire fixed interval [92,1000000) and proves that
actual class number one there forces d=163. With the checked small end,
`classNumber_one_candidates_below_million` gives the necessary nine-element
list below one million. Its upper-middle certificate theorem explicitly
leaves [1000000,700000000000) unclosed. Positive class-number equalities
and the full classification are not asserted.
[Human wheel proof](../research/ender_radius_bridge/WHEEL_COVERAGE_GUIDE.md).

**Phase 30 adds the finite-sieve entry bridge.** `OddPrimeTwo` proves
actual class number one implies d=3 mod 8 above 7. `FiniteSieveBridge`
proves necessity of guarded checked-odd-prime tests and the necessary
eight-candidate list below 92. Its nine-candidate theorem has an explicit,
unsupplied middle-range survivor-certificate premise. All-nine acceptance
is only a test control, not a positive class-number theorem.
[Short proof and remaining obligation](../research/ender_radius_bridge/FINITE_SIEVE_GUIDE.md).

**Historical checkpoint: the interpolation/Gram positivity chain was connected,
but the class-number classification chain was not yet connected.** This map supersedes the PR #8-era coverage
summary previously stored here; Git history preserves that record. Stage notes
remain useful derivations, but their old frontier descriptions are historical.

**Phase 29: the effective bound now covers every positive squarefree radicand.**
`imaginaryQuadratic_classNumber_one_radicand_bound` concludes d<700000000000
from positivity, squarefreeness and Mathlib class number one of the actual
`AdjoinRoot (X^2+C(d:Rat))`. `EvenOrderCoordinates`, `EvenQuadraticField`,
`EvenMaximalOrder` and `EvenClassNumber` prove the trace-zero chart's
maximality and prime-two norm obstruction. `QuadraticChartEquivalence`
constructs both field maps/inverses, transports class number one through
the actual integer rings, and joins the two parity cases. The cutoff has
no mod-4, numerical or field-identification premise. Finite classification
is not asserted. The conventional absolute-discriminant parameter bound is
separate from any as-yet-unsupplied identity with `NumberField.discr`.
[Short human proof](../research/ender_radius_bridge/FULL_CUTOFF_GUIDE.md).
The following phase descriptions retain their historical frontier scope.

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
