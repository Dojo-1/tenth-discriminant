# Tao's challenge: current accounting and side discoveries

**Living update: 25 October 2026, through preregistered Phase 40;
original accounting began after externally merged PR #20
(`main` at `8ab2be0`).** This updates, but does not rewrite, the
[earlier frozen audit](TAO_OBJECTIVE_AUDIT.md) at `4c034f9`.

Phase39 improves the DIRECT analytic cutoff from700 billion to200 billion
for both the actual radicand and absolute field discriminant. It sharpens
floor/log loss on the same auxiliary radius family and prime constants.
The new bound does not borrow the finite classification or old cutoff:
fresh compiled input checks and a full local axiom audit pass. Publication
requires exact-head pinned CI. This is a modest improvement within the
credited method, not an optimality or novelty claim.
[Short analytic proof](research/ender_radius_bridge/ANALYTIC_CUTOFF_OPTIMIZATION_GUIDE.md).
Earlier phase statements below retain their checkpoint scopes.

Phase37 joins the entire original finite interval to the existing cutoff
and all nine positive equalities. The actual canonical field-family iff
requires only positive-squarefree d; no range or certificate premise remains.
Phase36's aggregate pilot remains incomplete; Phase37's separately registered
unchanged last-seed check passed, followed by serialized library rechecking.
Exact-head build/audit/pinned CI records accompany publication. No arbitrary
field-type representation theorem, improved analytic constant, novelty or
independent human review is claimed.
[One-page human proof](research/ender_radius_bridge/CLASSIFICATION_GUIDE.md).

Phase38 supplies an internal compiled proof-input inventory, with source
inspection of the generic class-number/PID/Minkowski frontier and explicit
separation of cutoff, positive cases and finite certificate. No pre-existing
classification input was identified in that reviewed frontier. This
strengthens provenance evidence, not independent review or optimization.
[Input map and limitations](research/ender_radius_bridge/PROOF_INPUT_GUIDE.md).
Earlier finite-frontier statements below are historical checkpoints.

Phase 34 supplies a checked representation change for the remaining sieve:
bit-mask queries equal the original guarded root tests and preserve the
entire wheel list. This is supplementary formal infrastructure, not a new
classification, optimized bound or completed challenge objective. Literal
mask validation passed locally. All four fixed translate attempts hit the
registered memory threshold; no interval or challenge objective is newly
closed by this experiment. The failure is preserved, not recast as success.
[Human explanation](research/ender_radius_bridge/RESIDUE_MASK_GUIDE.md).

Phase 33 supplies all nine actual positive class-number equalities, via
prime-norm residue maps, small ideal principality and Minkowski. Together
with the checked finite sieve this proves BOTH directions below one million
for positive squarefree radicands. Actual field discriminant and cutoff
remain checked. The entire upper interval [1000000,700000000000) is still
unclosed, so full classification is not achieved. No improved constant,
novelty or independent human review is claimed.
[Human proof and range map](research/ender_radius_bridge/NINE_POSITIVE_GUIDE.md).
Older phase paragraphs below are historical where positive-case gaps are now closed.

Phase 31 advances the finite proof bridge: a universal no-loss wheel theorem
and exact complete check on [92,1000000) prove the necessary nine-element
list below one million for the actual field. The original effective cutoff
is unchanged. The upper middle interval [1000000,700000000000) and positive
class-number equalities remain open, so the full classification objective
is not achieved. Supplementary result: the wheel/interval coverage operators
are proved generically and may be reused for the full interval.
[Human explanation](research/ender_radius_bridge/WHEEL_COVERAGE_GUIDE.md).

Phase 30 advances formalization, not the optimization or classification
status: the actual class-number hypothesis now supplies the saved sieve's
modulo-eight entry condition and guarded prime tests. A kernel-checked
necessary list below 92 and explicit conditional middle-range reduction
are supplementary results. The saved CRT campaign is not thereby a checked
full-range certificate; positive class-number proofs remain separate.
[Human explanation](research/ender_radius_bridge/FINITE_SIEVE_GUIDE.md).

Phase 29 now gives an **effective bound for every positive squarefree
radicand d**: actual class number one of the constructed `Q(sqrt(-d))`
implies `d<700000000000`. The even maximal-order/prime-two argument and
an explicit field equivalence join both parity cases in one actual field
family. No mod-4, numerical or field-identification premise remains in this
public bound. The conventional absolute-discriminant parameter d or 4d
is also bounded; an identity with Mathlib's `NumberField.discr` is not claimed.
Finite classification, optimization, independent human review, systematic
comparison and submission remain separate. [Human proof](research/ender_radius_bridge/FULL_CUTOFF_GUIDE.md).

Earlier checkpoint: Phase 28 closes the **universal odd-discriminant cutoff**: squarefree
`D≡3 (mod 4)` and `D≥700000000000` imply actual-field class number not one,
with no numerical premise. A new fixed auxiliary radius family and two
normalized affine envelopes replace the remaining interval comparisons for
this statement; the frozen campaign is not altered or retrospectively
certified. The even-chart gap recorded at that checkpoint is closed by
Phase29; finite classification and independent/upstream review remain open.
[Short human proof](research/ender_radius_bridge/ODD_CUTOFF_GUIDE.md).

Earlier checkpoints: Phase 26 closes one bounded exclusion end to end: squarefree `D≡3 (mod 4)`
in `[700000000000,875000000000]` gives actual-field class number not one.
All rows, complete prime coverage, both budgets and exact guards are supplied.
The strict comparison has no numerical premise. That bounded theorem was
not a global cutoff or classification; Phase 28 now extends its odd range.
As a supplementary reusable result, the staircase polynomial is proved a
global **lower bound**, even where the guarded exact identity fails. No
novelty claim is made. [Human numerical guide](research/ender_radius_bridge/NUMERICAL_BRIDGE_GUIDE.md).

Phase 27 now proves the arithmetic estimates uniformly in R,S, with four
certified prime-log constants reused from fixed prime information. It recovers
the same first-interval budgets; it does not extend the excluded D range.
[Uniform arithmetic guide](research/ender_radius_bridge/UNIFORM_PRIME_MASS_GUIDE.md).

[Tao's 20 October post](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/)
poses a main challenge—an effective bound for a hypothetical tenth
discriminant without Heegner's methods—and invites optimization,
comparison, new arrangements, negative results, formalization, and careful
AI-assisted reporting. **The twelve rows below are our operational
accounting, not twelve numbered objectives written by Tao.** His post uses
radicands such as `1,2,3`, as does the new Phase29 public theorem's d.
Earlier repository `D` is the *absolute fundamental
discriminant*, whose nine known values are `3,4,7,8,11,19,43,67,163`.

The original post was re-read on 25 October for this update. Its request for
an effective optimized bound, useful comparisons/negative results, readable
arguments, disclosed AI assistance and a human-generated submission summary
does not turn an effective bound into a full classification. No comment
was posted in this cycle.

## How we are faring

| # | Aspect of the challenge | Current verdict | Evidence and limit |
|---:|---|---|---|
| 1 | Effective bound, avoiding Heegner as proof input | **Stronger actual field-discriminant bound supplied; semantic review pending** | [Phase39](lean/TenthDiscriminant/OptimizedAnalyticCutoff.lean) gives actual radicand and absolute field-discriminant bounds below `2×10¹¹`. Both parity charts and actual discriminant identity are supplied. No numerical or classification premise; fresh compiled input checks exclude the old cutoff and finite answer. Independent semantic review remains open. |
| 2 | Best efforts to optimize the constant | **Modest direct analytic improvement; no optimality claim** | A sharper guarded floor/log bound reduces the pre-computation cutoff from `7×10¹¹` to `2×10¹¹` on the same family, a factor3.5. The finite d≤163 consequence is separate. This remains much larger than historical/differently reviewed bounds in the dated [prior-art](PRIOR_ART.md) note; no controlled like-for-like superiority claim. Earlier [lift](ledger/determinant_lifts.txt)/[radial](ledger/radial_bounds.txt) negative results remain preserved. |
| 3 | Threshold low enough for direct computation | **Complete finite certificate supplied for the canonical field family** | The original remaining interval is covered by quotient/remainder, eleven complete seed proofs and all785 quotient positions. With the cutoff and nine positive cases, `imaginaryQuadratic_classNumber_one_iff` has no range or certificate premise. Exact-head CI and semantic-review status must accompany this claim. |
| 4 | High-quality Lean formalization, perhaps upstreamable | **Connected actual-field-family iff; external quality judgment open** | Actual class number/discriminant, cutoff, full finite exclusion and all nine positives are supplied. This is not an arbitrary-field-type representation theorem. Independent human semantic review, API/style review and Mathlib upstream acceptance remain open. See the [claim map](lean/FORMALIZATION.md). |
| 5 | Compare strengths of different writeups | **Bounded controlled comparison supplied; broad objective partial** | [Phase40](research/ender_radius_bridge/SAME_ROUTE_COMPARISON.md) compares two frozen complete same-route manuscripts with our proof head across parameter, analytic threshold, finite finish, rank, normalization, inputs and review. Original-byte source hashes and recency controls are recorded. External results are source claims, not newly audited or replayed; this is not an all-writeup optimized survey. [Prior art](PRIOR_ART.md) remains a frozen historical note. |
| 6 | Spur new arguments or arrangements | **Reusable arrangement, no novelty claim** | BEAN-to-Ender changes the prime input. Four fixed prime-log constants and normalized affine envelopes now yield a checked universal odd cutoff without replaying 249 more interval comparisons. This is an arrangement within the credited Green/twinheterodox route, not a claim of a new mathematical method. |
| 7 | Preserve failed attempts and negative results | **Documented internally** | The [review response](review/RESPONSE_Claude.md), [BEAN audit](review/BEAN_AUDIT.txt), fixed [radial protocol](flow/PREREG_RADIAL.txt), and [lift protocol](flow/PREREG_LIFTS.txt) retain counterexamples, failed guards and ceilings. Internal preservation does not equal external reporting. |
| 8 | Help higher class-number problems | **Not delivered** | The `h≤2` [review brief](REVIEW_BRIEF_2.md) remains unreviewed; nothing here advances a verified higher-class-number range. |
| 9 | Disclose AI involvement | **Repository practice present** | The [README](README.md) and review records identify AI assistance. This is disclosure, not validation or a submission. |
| 10 | Contribute a repository link and human summary in Tao's comments | **No documented submission** | The repository has no submission permalink or posting record. This cycle posted nothing to Tao. The article was re-read, but a new sitewide/comment-pagination submission search was not performed. |
| 11 | Independent due diligence before an AI-generated submission | **Partial** | Historical adversarial AI review, negative controls, pinned CI and the new [internal input audit](research/ender_radius_bridge/PROOF_INPUT_GUIDE.md) cover distinct risks. The last is not independent review; no new independent human semantic review or submission is recorded. |
| 12 | Quality, collaboration and attribution over speed | **Visible practice, not an external verdict** | The [README](README.md) and [prior-art note](PRIOR_ART.md) credit antecedents and preserve scope limits. No Tao endorsement, human peer review or priority claim is inferred. |

**Bottom line.** There is now a connected kernel-checked effective bound
on both d and the actual absolute field discriminant below `2×10¹¹`, for the
actual imaginary quadratic field family with both parity cases supplied.
All nine positive cases and the complete finite certificate now supply the
canonical-field-family iff without a range premise. Independent human
semantic review is not supplied by kernel checking. The frozen external
CRT run remains computational evidence; the new Lean certificate has its
own provenance. The analytic threshold is improved, not claimed optimal;
no submission is claimed.
Tao explicitly welcomes informative larger bounds and clean human-verifiable
arguments. Remaining shortfalls include independent review, upstream quality,
optimization, broader comparison and human-authored external reporting.

## Supplementary accounting: useful results even if the main route stalls

The entries below describe each component's own scope. Earlier finite
frontiers are historical; the Phase37 composition above is the current result.

Phase36–37 adds a reusable exact representation: pull periodic prime tests
back along r+Mk using checked modular inverses, then prove survivor-bit
retention and exact interval coverage. This is a formal/computational
arrangement, not a new number-theoretic method or a measured universal speedup.
The incomplete aggregate pilot remains negative evidence; its later
completion is separately registered and separately costed.

| Result | Evidence class | Exact gain—and boundary |
|---|---|---|
| Frozen same-route comparison with explicit object/parameter alignment. | **Internal primary-source analysis, not a theorem or independent review** | [Phase40](research/ender_radius_bridge/SAME_ROUTE_COMPARISON.md) separates rank mechanisms, trace-Gram versus minor-norm integers, strict prime endpoints and analytic versus finite bounds. Seven source hashes and two historical blob controls are reproducible. It suggests a future auxiliary-prime proof bridge, but imports no external constants and proves no stronger cutoff. |
| Complete-seed fused traversal preserves every leaf predicate. | **Lean theorem plus one complete concrete translate** | Checks below 892371480 now compose to an actual-field bounded iff. Translation does not preserve extra-prime tests (checked p=29 control). The fixed pilot had 16 passing blocks, one aggregate-time stop and 27 skipped blocks; no full-range runtime or isolated fusion speedup is established. [Human proof](research/ender_radius_bridge/FUSED_WHEEL_GUIDE.md). |
| Actual field discriminant and all nine positive class numbers. | **Lean theorems using maximal integral bases, small ideal norms and pinned Minkowski** | The actual absolute-discriminant cutoff and all nine positive equalities are supplied. Prime-norm quotients give root obstructions; the legitimate norm-four ideal (2) is retained. d=23 refutes omitting local hypotheses. No novelty or full classification claim. [Human proof](research/ender_radius_bridge/NINE_POSITIVE_GUIDE.md). |
| Prime 2 forces d=1 or 2 in the even fundamental chart under class number one. | **Lean theorem on the actual maximal order** | Squarefree denominator and mod-4 parity give integer coordinates; an F2 quotient ideal becomes principal and forces norm two. d=1,2 controls are retained; d=3 refutes dropping the chart guard. No claim of a new argument or a full classification. [Human proof](research/ender_radius_bridge/FULL_CUTOFF_GUIDE.md). |
| The explicit generator change theta=2*omega-1 joins both parity charts in one actual `Q[X]/(X²+d)` family. | **Lean field equivalence and effective-bound theorem** | Both inverse maps, actual integer-ring/PID transport and the universal radicand bound are supplied, not a piecewise class-number proxy. Finite classification and independent review remain open. [Theorem](lean/TenthDiscriminant/QuadraticChartEquivalence.lean). |
| A fixed radius family and normalized affine envelopes exclude all large odd fundamental discriminants in the encoded chart. | **Lean-checked universal odd-cutoff theorem** | No numerical premise: lower slope `0.999997` beats upper slope `13/16` with a checked finite margin at `log D≥27`. Avoids further interval tables, not even cases or finite classification. The auxiliary radius is new and explicitly distinct from the frozen campaign. [Human proof](research/ender_radius_bridge/ODD_CUTOFF_GUIDE.md). |
| Four fixed prime-log constants give bounds for arbitrary admissible rectangle dimensions. | **Lean theorem and checked finite constants** | Floor error, geometric prime powers, quadratic loss and both clipping terms are retained. The actual-Gram comparison keeps all radius/range/class-number guards. The same first interval is recovered; no new interval or optimized/global cutoff is claimed. [Human proof](research/ender_radius_bridge/UNIFORM_PRIME_MASS_GUIDE.md). |
| The first saved interval is excluded for squarefree `D≡3 (mod 4)`, with no numerical premise. | **Lean-checked bounded class-number theorem** | Every local factor, geometric guard, log enclosure, row, prime label and aggregate budget is supplied; `581×10^31>572×10^31` closes the contradiction. No global cutoff, new optimized constant or novelty claim. [Human proof](research/ender_radius_bridge/NUMERICAL_BRIDGE_GUIDE.md) · [Theorem](lean/TenthDiscriminant/FirstIntervalChecked.lean). |
| A contact budget of `2 deg_Z F + deg_W F` turns enough ordinary jets into a positive determinant for the **actual** trace-Gram matrix. | **Lean theorem** | General finite complex samples and rectangular monomial grids, not merely Ender's ellipse. It proves nonvanishing, not inertness or valuation. [Human proof](lean/HUMAN_GUIDE.md) · [short spine](lean/MATHEMATICAL_SPINE.md). |
| Unit-by-`√D` cells yield an elementary lower count at Ender's chosen radius. | **Lean-checked geometric theorem** | Lean checks the actual disk covering, cell volumes, strict chosen-radius count, and interval transfer to actual-Gram positivity. This is not the analytic cutoff. [Proof](lean/TenthDiscriminant/EllipseCellArea.lean) · [human explanation](lean/HUMAN_GUIDE.md#9-the-concrete-ellipse-bridge). |
| The Ender campaign records 250 contiguous Arb interval enclosures from `7×10¹¹` to `10³⁶`, an all-`D` envelope above that, and a finite CRT sieve below the cutoff. | **Recorded computation and conditional derivation** | Reproducible numerical evidence for the candidate route; source correspondence does not itself certify every Arb inequality or the missing determinant/class-group implications. [Coverage](ledger/coverage_ender.txt) · [derivation](ledger/ender.txt). |
| One integral Gram matrix has an exact real view and a residue view retaining samples that collide modulo `m`. | **Lean theorem** | For `m>0`, the residue determinant vanishes exactly when `m` divides the integer determinant. This detects divisibility, but gives no valuation exponent. [Claim map](lean/FORMALIZATION.md). |
| A unitriangular rectangular basis using `Z^p-W` yields Ender's full `2F(p)` valuation exponent under odd-prime nonsquareness of `-D` modulo `p`. | **Lean theorem with class-number bridge in the strict range** | Lean checks the actual Gram-row identity, integral factorization and universal Frobenius implication; Phase 16 derives the local guard from class number one for squarefree `D≡3 (mod 4)` and strict small odd primes. This is not a new analytic cutoff. [Proof](research/uniform_inert_valuation/PROOF.md). |
| The explicit half-integral order is the actual maximal integer ring, and class number one supplies the local determinant factor. | **Lean theorem with adversarial control** | Trace, norm, squarefree denominators and parity prove the order equivalence; the principal-ideal quotient and nonnegative norm give exact norm lifting. `D=15,p=3` forces class number not one. This closes a local arithmetic bridge, not the area/analytic/classification chain. [Human guide](lean/HUMAN_GUIDE.md#21-the-global-hypothesis-reaches-the-local-determinant). |
| Distinct odd-prime factors assemble on the same positive chosen-radius Gram. | **Lean theorem** | The product divides the integer determinant; its exact finite logarithmic mass is bounded by the real Hadamard diagonal product. This is the local-to-global-to-real junction, not the factorial estimate, numerical cutoff or classification. [Proof](lean/TenthDiscriminant/PrimeMassAssembly.lean) · [human explanation](lean/HUMAN_GUIDE.md#22-the-finite-prime-mass-sandwich). |
| Production `upper_B` and its geometric count bound apply to the same diagonal product at integer radii. | **Lean theorem** | Falling factorials, row sums and a logarithmic integral give the unchanged formula. Disjoint inward cells and exact axis counts supply `n_up`; the integral has spare endpoint slack. Floor padding remains explicit. No new numerical cutoff or novelty claim. [Human proof](research/ender_radius_bridge/UPPER_BOUND_GUIDE.md). |
| Exact Legendre factorization and an increasing integral envelope yield production `factorial_lower`. | **Lean theorem** | Includes prime `2`, all finite endpoints and the `R≥2` guard. The remaining weight conversion and tail estimate are not inferred. Classical mathematics, no novelty or new cutoff claim. [Short proof](research/ender_radius_bridge/FACTORIAL_LOWER_GUIDE.md). |
| A staircase identity converts factorial floor weights into determinant weights, with both losses controlled by one finite reciprocal-prime sum. | **Lean theorem** | Small-prime subtraction, geometric series, floor squares, integer coefficients, padded enumeration and clipping are checked. Phase 24 also proves the production tail bound. Classical mathematics, no new cutoff claim. [Short proof](research/ender_radius_bridge/PRIME_MASS_LOWER_GUIDE.md). |
| Positive potential drops bound the reciprocal-prime tail by a finite telescoping sum. | **Lean theorem and connected exclusion criterion** | No prime-distribution input or infinite-series exchange. Phase26 supplies the first interval, Phase28 universal odd closure, and Phase29 the combined field-family bound. Frozen campaign records are not retrospectively certified. No novelty claim. [Proof](lean/TenthDiscriminant/PrimeTail.lean). |
| At `D=19,p=3`, `Z³−W` yields `9∣det G` for the canonical eight-row Gram for every finite sample set and derivative cutoff. A 21-point ellipse also gives `det G>0`. | **Fixed Lean theorem with positive control** | A concrete nonzero local–global bridge, not the uniform inert-prime estimate Ender needs. [Mechanism](lean/MATHEMATICAL_SPINE.md#a-complete-small-arithmetic-bridge). |
| The radial guarantee has an `O(1/R)` normalized ceiling; a finite `D=19` lift case rules out a universal extra `+2` in the proposed valuation exponent. | **Preregistered negative/finite results** | They eliminate tempting upgrades without changing the cutoff. Finite controls must not be generalized. [Radial](ledger/radial_bounds.txt) · [lifts](ledger/determinant_lifts.txt). |
| A short proof spine separates the hard contact lemma, fixed arithmetic pilot and open bridge. | **Expository/process artifact** | Makes the apparatus more inspectable; readability is not independent mathematical review. [Guide](lean/MATHEMATICAL_SPINE.md). |

The next decisive work is independent semantic review of the connected
field-family theorem, followed by API/style refinement, comparison and
constant optimization. The finite interval is no longer an unsupplied
premise in the new iff. Neither a complete kernel proof nor this accounting
establishes novelty, upstream acceptance or a human-authored submission.
