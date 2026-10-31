# Phase140 — nested ellipsoids, smaller interpolation radius, and proof-margin sensitivity

**31 October 2026 · evidence [M] on small instances; [P] source-established general integer-jet divisibility and point-count interpolation; [H] new production-radius and determinant-upper interfaces pending exact-head Lean CI.** The current strict 47-billion actual-field theorem remains unchanged. Independent semantic reconstruction [#50](https://github.com/Dojo-1/tenth-discriminant/issues/50) and compatible arithmetic/real interface [#51](https://github.com/Dojo-1/tenth-discriminant/issues/51) remain open.

This experiment addresses an actual mathematical choice, not visual novelty. The existing observation domain is already a norm ellipse in integer coordinates, and a disk after the field embedding. Other ellipsoids might help only if they improve the *same-integer determinant sandwich*, including the original inert-prime factors and strict rank guard.

## Existing formal facts that make shape selection legitimate

1. [IntegerTraceGram.lean](../../lean/TenthDiscriminant/IntegerTraceGram.lean) defines the same 2Re ordinary-jet Gram for **any finite integer-pair set Q**, not only the full ellipse. The [samplewise ordinary-jet action](../../lean/TenthDiscriminant/RectangularRowAction.lean) and [class-number-one Frobenius valuation bridge](../../lean/TenthDiscriminant/PrimeMassAssembly.lean) also have arbitrary-Q inputs. Under the *original inertness, degree, integrality and class-number assumptions*, the local divisor p^(2F(p)) applies to that choice of Q. No automatic new prime valuation is obtained.
2. [Interpolation.lean](../../lean/TenthDiscriminant/Interpolation.lean) makes the **same** integer Gram positive whenever 1<=R,S, J>=S, and 2*(R-1)+(S-1)<|Q|. This is a sufficient condition, not a claimed necessary one.
3. [EllipseCellArea.lean](../../lean/TenthDiscriminant/EllipseCellArea.lean) proves the cell-covering lower count. [TunedRadiusFamily.lean](../../lean/TenthDiscriminant/TunedRadiusFamily.lean) chose radius approximately 0.52 D^(3/4) by requiring the **stronger** 3R+S count. Thus the older production radius has *genuine, checkable geometric slack* relative to the current interpolation theorem; the [earlier proof narrative](../ender_radius_bridge/PROOF.md) explicitly notes this difference.
4. For Q' subset Q, the original real positive trace matrices obey G_Q=G_Q'+G_(Q\Q'), and G_(Q\Q') is positive semidefinite. If G_Q' is positive definite, Loewner monotonicity gives 0<det G_Q'<=det G_Q (strict under a nonzero removed observation). This is classical linear algebra; no novel claim for determinants of PSD sums. Any arithmetic lower must be proved separately for G_Q' (here by the arbitrary-Q Frobenius theorem), NOT transported by det monotonicity alone.

## Exact bounded experiment: a genuine nested ellipse

Freeze D=19, rho=5, R=8, S=J=4. The original full ellipse has 21 nodes; the sufficient rank guard is 17. Consider a **different ellipse**, nested in the original,

    Q' = {(x,y) in Z² : 6*x²+95*y² <= 125}
       = {(x,y) : (6/5)*x²+19*y² <= 25}.

Since (6/5)x²+19y² >= x²+19y², Q' is globally inside the original Q; it retains **exactly 19 nodes**, removing only (5,0) and (-5,0). Rank guard 17<19 survives. This is a changed node support and therefore a new Gram integer, **not** an integer row-frame change. The original prime factor must be reapplied to Q', and it is.

The fully reproducible [arbitrary-precision integer pilot](phase140_exact_trim.py), [CI run 41190304576](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41190304576), checked every one of the 32 original monomial rows, all four ordinary derivative orders and the unchanged factor-two trace metric. It recomputed the full determinant by exact fraction-free elimination and verifies that 3^38 divides both determinant integers (p=3 is inert for D=19; F(3)=19). Presentation-only natural logs:

| Measure | Original 21 nodes | Nested ellipsoid, 19 nodes |
|:--|--:|--:|
| log of exact full Gram determinant | 530.285191201861 | 512.666684183565 |
| log of raw monomial diagonal Hadamard product | 626.255217764800 | 615.964084500076 |

Log determinant decrease **17.618507018296**; raw monomial diagonal-product decrease **10.291133264724**. These logs are not exact claims—only the determinants and their divisibility checks are exact integers. Raw monomial Hadamard is **not** the repo's best production upper; one must not add the displayed finite gain to the existing certified normalized constant.

**Matched controls:** the script removes each of the ten possible antipodal pairs in turn, retaining 19 nodes for every control; (±5,0) maximizes the *actual determinant decrease* in this **exhaustive ten-case matched class**. The same 3^38 divisor survives each control. A rotated quadratic-form condition x²+19y²+5xy<=25 can include (3,-1), whose original norm² is 28>25: reusing the old radius bound for such a **non-nested** ellipse would be false. Removing four nodes leaves 17 and invalidates the **sufficient** rank guard, but does not prove singularity.

The measured original form is two-dimensional; the determinant and rank guards act on a 32-dimensional polynomial observation space. The difference matters: higher-dimensional feature-space ellipsoids are potentially useful, but the finite benchmark above tests only the node-selection geometry and its exact full Gram consequence.

## A stronger production theorem target: 0.44 instead of 0.52

The candidate [ThinEllipseCount.lean](../../lean/TenthDiscriminant/ThinEllipseCount.lean) is a **new Lean compilation target** for the same tuned R(D), S(D) and D>=41,006,250,000. Define

    h = fourthRoot(D) = D^(1/4) >= 450,
    rho_thin(D) = ceil((11/25)*h^3).

The desired **geometric-only theorem** is

    2*(R(D)-1)+(S(D)-1)
       < card(ellipsePairs D rho_thin(D)).

The existing tuned dimension lemma gives R<=D/4 and S<=R/25, hence q:=2R+S <=51D/100. Because pi>3 and 3*(413/1000)^2>51/100, one obtains

    sqrt(q*sqrt(D)/pi) <=(413/1000)*h^3.

For h>=450,
    (1001/1000)*(413/1000) + 10/h < 11/25.

Consequently the smaller radius meets the already proved **chosen-radius counting lemma with q=2R+S**, so q<#Q_thin and therefore the desired weaker interpolation guard follows. The coefficient margin is explicit. This mathematical argument is proposed for formal compilation; **do not label it a compiled Lean theorem until the exact-head build passes**. It establishes geometry only, no field cutoff.

This reduces the radius coefficient from 13/25=0.52 to 11/25=0.44—a factor **11/13** in the leading radius. The maximum norm of observations and their number can both decrease, and the *same* original odd-inert-prime valuation theorem applies for that chosen finite ellipse. The quantitative production upper is a separate obligation: the old [SharpRadialDetBound.lean](../../lean/TenthDiscriminant/SharpRadialDetBound.lean) takes arbitrary Q, rho and a cardinality upper estimate, but its specialized affine envelope still uses the OLD radius and count. One must rebuild that envelope, show its uniform improvement over the **previous certified upper**, and redo the logarithm/actual-field threshold before promoting a cutoff. A margin of 43/10000 for a conditional 46-billion endpoint remains an [H] target, not a consequence of count alone.

## Distinct further questions, falsifiers and prior art

**H1 (primary): Shape-versus-dimension majorant.** Can the thinner certified radius combined with the original high-order ordinary-jet row estimates and a newly certified padded node-count upper yield at least 43/10000 extra normalized geometric saving for all D>=46 billion? A changed Q is allowed only because both the rank and inert-prime valuations are rebuilt on that SAME Q. Counterworld: the increased relative derivative costs, integer rounding and cardinality estimate consume all the saving when expressed against the best existing upper, not the raw Hadamard pilot.

**H2 (higher-order ellipsoids):** For fixed original Q, consider the complete SPD Gram G on n=R*S polynomial rows, its determinant-one real frame orbit, and multiscale radial blocks. Can a *determinant-independent*, analytically specified positive quadratic norm / ellipsoid on this full feature space expose a uniform block-volume saving beyond H1? Compare to the ordinary radius control at matched analytic effort; a real optimized frame computed from the unknown full G is circular. Classical ellipsoid approximation and John's theorem do not themselves supply a field bound ([John's theorem](https://mathworld.wolfram.com/JohnsTheorem.html), [geometry-of-numbers notes](https://n.ethz.ch/~pkoymans/DA/dio2.pdf)).

**H3 (apparent irregularity versus hardness):** With frozen integer radius rho=5 and R=8,S=4, the sample count jumps from 21 at D=21 to 17 at D=22, crossing the sufficient guard abruptly. This is a **finite lattice threshold**, not evidence for NP-hardness. To test a real phenomenon as the cutoff is lowered, pre-register a family of *simultaneously scaled* production-like (D,R,S,J,rho) settings, record the signed analytic comparison margin, the count surplus, prime-valuation discontinuities and the normalized Gram spectrum, and compare with a smooth-volume baseline. A one-parameter jagged plot is neither chaos in the dynamical-systems sense (no proved sensitive trajectories) nor a complexity lower bound. Kill the interpretation if irregularity disappears after controlling floors/count thresholds or has no predictive relationship to proof-margin failure.

**Novelty and priority:** Green's determinant, Frobenius divisibility, the count/rank asymmetry, John ellipsoids, Loewner determinant monotonicity, and numerical D-optimal support selection have known mathematical antecedents. The live question is whether these together yield a *new uniform inequality in this exact proof architecture*. Tao's [experimental tenth-discriminant forum](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/) discusses alternative split-prime and auxiliary-prime improvements with much smaller **reported** numerical cutoffs, so do not present ours as a record bound. Our distinguishing objective remains a direct, reconstructible **one-integer, no-auxiliary-prime** argument.

**Promotion rule:** exact-source finite CI for the 19-node pilot [M]; exact root Lean/source/axiom/negative-controls for the thin-radius count [P for geometry only]; separately checked full-ordinary-jet normalized upper [P] and actual field transport to claim any smaller discriminant endpoint. No changed proof code to the 47-billion theorem; issues #50 and #51 remain open until their distinct semantic and cross-method requirements are met.
