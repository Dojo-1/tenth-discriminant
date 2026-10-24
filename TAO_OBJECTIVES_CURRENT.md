# Tao's challenge: current accounting and side discoveries

**Living update: 25 October 2026, through preregistered Phase 34;
original accounting began after externally merged PR #20
(`main` at `8ab2be0`).** This updates, but does not rewrite, the
[earlier frozen audit](TAO_OBJECTIVE_AUDIT.md) at `4c034f9`.

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

The original post was re-read on 24 October for this update. Its request for
an effective optimized bound, useful comparisons/negative results, readable
arguments, disclosed AI assistance and a human-generated submission summary
does not turn an effective bound into a full classification. No comment
was posted in this cycle.

## How we are faring

| # | Aspect of the challenge | Current verdict | Evidence and limit |
|---:|---|---|---|
| 1 | Effective bound, avoiding Heegner as proof input | **Actual absolute field-discriminant bound checked; semantic review pending** | [Phase 32](lean/TenthDiscriminant/QuadraticDiscriminant.lean) proves the actual discriminant identity, so class number one bounds both d and the actual absolute field discriminant below `7×10¹¹`. Both parity charts are supplied; no numerical premise or Heegner classification input. This is a bound, not full classification or independent human review. |
| 2 | Best efforts to optimize the constant | **Effort documented; no improved cutoff** | The factorial arrangement removes Dusart from this route but gives a much larger threshold than the historical `1.5×10⁴` branch and the dated [prior-art](PRIOR_ART.md) report of `q<570` (not re-reviewed here). Preregistered [lift](ledger/determinant_lifts.txt) and [radial](ledger/radial_bounds.txt) investigations did not improve Ender's global cutoff. |
| 3 | Threshold low enough for direct computation | **Checked cutoff; finite certification partial** | The saved [CRT sieve](ledger/sieve_ender.txt) leaves `163` in `[92,7×10¹¹)`. The complete initial interval and all nine positive fields are now supplied, giving a bounded iff below one million. The entire upper interval remains unclosed in Lean. |
| 4 | High-quality Lean formalization, perhaps upstreamable | **Actual discriminant bound, all nine positives, bounded iff; global classification partial** | The actual field discriminant, cutoff, all nine positive equalities and both classification directions below one million are checked. Complete upper-middle certification, independent human semantic review and Mathlib upstream review remain open. See the [claim map](lean/FORMALIZATION.md). |
| 5 | Compare strengths of different writeups | **Qualitative only** | [Prior art](PRIOR_ART.md) records a dated comparison and attribution, not a controlled, current, like-for-like comparison of optimized manuscripts. |
| 6 | Spur new arguments or arrangements | **Reusable arrangement, no novelty claim** | BEAN-to-Ender changes the prime input. Four fixed prime-log constants and normalized affine envelopes now yield a checked universal odd cutoff without replaying 249 more interval comparisons. This is an arrangement within the credited Green/twinheterodox route, not a claim of a new mathematical method. |
| 7 | Preserve failed attempts and negative results | **Documented internally** | The [review response](review/RESPONSE_Claude.md), [BEAN audit](review/BEAN_AUDIT.txt), fixed [radial protocol](flow/PREREG_RADIAL.txt), and [lift protocol](flow/PREREG_LIFTS.txt) retain counterexamples, failed guards and ceilings. Internal preservation does not equal external reporting. |
| 8 | Help higher class-number problems | **Not delivered** | The `h≤2` [review brief](REVIEW_BRIEF_2.md) remains unreviewed; nothing here advances a verified higher-class-number range. |
| 9 | Disclose AI involvement | **Repository practice present** | The [README](README.md) and review records identify AI assistance. This is disclosure, not validation or a submission. |
| 10 | Contribute a repository link and human summary in Tao's comments | **No documented submission** | The repository has no submission permalink or posting record. This cycle posted nothing to Tao. The article was re-read, but a new sitewide/comment-pagination submission search was not performed. |
| 11 | Independent due diligence before an AI-generated submission | **Partial** | Adversarial AI review, negative controls and pinned CI cover important errors. They are not independent human semantic review, and no submission is recorded. |
| 12 | Quality, collaboration and attribution over speed | **Visible practice, not an external verdict** | The [README](README.md) and [prior-art note](PRIOR_ART.md) credit antecedents and preserve scope limits. No Tao endorsement, human peer review or priority claim is inferred. |

**Bottom line.** There is now a connected kernel-checked effective bound
on both d and the actual absolute field discriminant below `7×10¹¹`, for the
actual imaginary quadratic field family with both parity cases supplied.
All nine positive cases and the bounded iff below one million are proved.
The full finite classification remains incomplete, and independent
human semantic review is not supplied by kernel checking.
The frozen finite sieve remains computational evidence, not a new Lean
classification. No submission or optimized threshold is claimed.
Tao explicitly welcomes informative larger bounds and clean human-verifiable
arguments. The remaining shortfalls are finite classification, review,
optimization and systematic comparison, not an unsupplied cutoff premise.

## Supplementary accounting: useful results even if the main route stalls

| Result | Evidence class | Exact gain—and boundary |
|---|---|---|
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

The next decisive step is **not** another isolated zero determinant modulo a
prime. The uniform valuation now has a Lean proof for the *same
integer determinant* under a precise local nonsquare guard; checked
connections through the finite analytic inequalities are now checked,
including the tail. The first bounded numerical exclusion is now checked.
Phase28 closes universal odd exclusion, and Phase29 supplies the even chart
and actual field equivalence. The next decisive work is the finite odd
classification and independent semantic review, not another isolated
determinant identity. The effective bound is checked; classification is not.
