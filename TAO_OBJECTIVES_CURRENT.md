# Tao's challenge: current accounting and side discoveries

**Living update: 24 October 2026, through preregistered Phase 24;
original accounting began after externally merged PR #20
(`main` at `8ab2be0`).** This updates, but does not rewrite, the
[earlier frozen audit](TAO_OBJECTIVE_AUDIT.md) at `4c034f9`.

[Tao's 20 October post](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/)
poses a main challenge—an effective bound for a hypothetical tenth
discriminant without using Heegner's classification—and invites optimization,
comparison, new arrangements, negative results, formalization, and careful
AI-assisted reporting. **The twelve rows below are our operational
accounting, not twelve numbered objectives written by Tao.** His post uses
radicands such as `1,2,3`; this repository's `D` is the *absolute fundamental
discriminant*, whose nine known values are `3,4,7,8,11,19,43,67,163`.

## How we are faring

| # | Aspect of the challenge | Current verdict | Evidence and limit |
|---:|---|---|---|
| 1 | Effective bound, avoiding Heegner as proof input | **Candidate, not established** | [Ender](ledger/ender.txt) proposes exclusion for `D≥7×10¹¹`. The class-number/local-factor, geometric and finite analytic chains now connect unchanged mathematical `prime_mass≤upper_B` on one determinant, including the proven reciprocal-prime tail. The strict-comparison exclusion criterion is checked, but numerical enclosure/guard interpretation and universal closure remain open in Lean. |
| 2 | Best efforts to optimize the constant | **Effort documented; no improved cutoff** | The factorial arrangement removes Dusart from this route but gives a much larger threshold than the historical `1.5×10⁴` branch and the dated [prior-art](PRIOR_ART.md) report of `q<570` (not re-reviewed here). Preregistered [lift](ledger/determinant_lifts.txt) and [radial](ledger/radial_bounds.txt) investigations did not improve Ender's global cutoff. |
| 3 | Threshold low enough for direct computation | **Conditional computational endgame** | The saved [CRT sieve](ledger/sieve_ender.txt) leaves `163` in `[92,7×10¹¹)`, and the small range has a recorded [form check](ledger/formic.txt). They finish the finite part **if** the candidate exclusions hold. |
| 4 | High-quality Lean formalization, perhaps upstreamable | **Connected finite comparison, not the classification** | Lean checks interpolation, both ellipse counts, actual-Gram valuation from class number one, finite weight conversion, clipping and the analytic tail. The mathematical production lower/upper comparison has no remaining tail premise; the exclusion criterion retains strict numerical and radius/count guards. Numerical interpretation, universal closure and classification remain open. No Mathlib upstream review is recorded. See the [claim map](lean/FORMALIZATION.md). |
| 5 | Compare strengths of different writeups | **Qualitative only** | [Prior art](PRIOR_ART.md) records a dated comparison and attribution, not a controlled, current, like-for-like comparison of optimized manuscripts. |
| 6 | Spur new arguments or arrangements | **Modest local progress** | BEAN-to-Ender changes the prime input; the checked integer/residue Gram bridge gives a useful fixed example. The overarching Green/twinheterodox route is not claimed novel, and no new global exclusion follows. |
| 7 | Preserve failed attempts and negative results | **Documented internally** | The [review response](review/RESPONSE_Claude.md), [BEAN audit](review/BEAN_AUDIT.txt), fixed [radial protocol](flow/PREREG_RADIAL.txt), and [lift protocol](flow/PREREG_LIFTS.txt) retain counterexamples, failed guards and ceilings. Internal preservation does not equal external reporting. |
| 8 | Help higher class-number problems | **Not delivered** | The `h≤2` [review brief](REVIEW_BRIEF_2.md) remains unreviewed; nothing here advances a verified higher-class-number range. |
| 9 | Disclose AI involvement | **Repository practice present** | The [README](README.md) and review records identify AI assistance. This is disclosure, not validation or a submission. |
| 10 | Contribute a repository link and human summary in Tao's comments | **No documented submission** | The repository has no comment permalink or posting record. A page-text search found no `Dojo-1` string, but cannot exclude an unrecognized contribution under another name. |
| 11 | Independent due diligence before an AI-generated submission | **Partial** | Adversarial AI review, negative controls and pinned CI cover important errors. They are not independent human semantic review, and no submission is recorded. |
| 12 | Quality, collaboration and attribution over speed | **Visible practice, not an external verdict** | The [README](README.md) and [prior-art note](PRIOR_ART.md) credit antecedents and preserve scope limits. No Tao endorsement, human peer review or priority claim is inferred. |

**Bottom line.** We have not fulfilled the main bound challenge at the
standard of a connected, independently checked proof. The candidate
`7×10¹¹` cutoff and finite sieve are a research program with recorded
certificates, not a new classification. The strongest completed mathematical
work is a checked *piece* of the determinant machinery.
Tao explicitly welcomes informative larger bounds and clean human-verifiable
arguments: the central shortfall here is the unclosed proof chain, not simply
the size of the proposed constant.

## Supplementary accounting: useful results even if the main route stalls

| Result | Evidence class | Exact gain—and boundary |
|---|---|---|
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
| Positive potential drops bound the reciprocal-prime tail by a finite telescoping sum. | **Lean theorem and connected finite exclusion criterion** | No prime-distribution input or infinite-series exchange. The strict numerical comparison and its radius/count guards remain to be certified; no checked cutoff or novelty is claimed. [Proof](lean/TenthDiscriminant/PrimeTail.lean). |
| At `D=19,p=3`, `Z³−W` yields `9∣det G` for the canonical eight-row Gram for every finite sample set and derivative cutoff. A 21-point ellipse also gives `det G>0`. | **Fixed Lean theorem with positive control** | A concrete nonzero local–global bridge, not the uniform inert-prime estimate Ender needs. [Mechanism](lean/MATHEMATICAL_SPINE.md#a-complete-small-arithmetic-bridge). |
| The radial guarantee has an `O(1/R)` normalized ceiling; a finite `D=19` lift case rules out a universal extra `+2` in the proposed valuation exponent. | **Preregistered negative/finite results** | They eliminate tempting upgrades without changing the cutoff. Finite controls must not be generalized. [Radial](ledger/radial_bounds.txt) · [lifts](ledger/determinant_lifts.txt). |
| A short proof spine separates the hard contact lemma, fixed arithmetic pilot and open bridge. | **Expository/process artifact** | Makes the apparatus more inspectable; readability is not independent mathematical review. [Guide](lean/MATHEMATICAL_SPINE.md). |

The next decisive step is **not** another isolated zero determinant modulo a
prime. The uniform valuation now has a Lean proof for the *same
integer determinant* under a precise local nonsquare guard; checked
connections through the finite analytic inequalities are now checked,
including the tail. The next decisive work is numerical enclosure/guard
interpretation, universal closure and the finite classification, not a new
matrix or new algebra. No checked cutoff claim follows yet.
