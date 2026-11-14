# Phase289 — exact observed quartet upper and next held-out field test

**Recorded AFTER the corrected focused exact-head run** [#43246486688](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43246486688) at `4068d5b`, 12 Nov 2026. The initial CI [#43246305235](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43246305235) failed on a duplicated index slice in the self-authored *moving-frame assertion*; it is retained in the PR. The correction did not modify original source, partition, thresholds or predictions. These are AI-authored finite computations, not independently reviewed results.

## The new same-source analytic inequality

Keep exactly original D283(R70,S=J2,Q169) and D403(R100,S=J4,Q219) entire ordinary-jet integer trace-Grams (full 140/400 row sets), original point sets and metric. All original radial-fiber labels are covered once. The already-known Phase206 adjacent-same-parity 2-fiber matching has 35 / 51 pairs and 1 leftover singleton in each source. Our fixed further grouping combines two consecutive old pairs into **17/25 nonoverlapping four-fiber blocks**; one unmatched pair and one singleton remain unchanged. Exact integer SPD/Fischer checks passed in *all* 17/25 blocks with strict improvement. No fourth-row selection or reordering was optimized after observing correlations.

For a 4-fiber principal Gram block \(G_{4}=\begin{psmallmatrix}A&C\\C^T&B\end{psmallmatrix}\), with A,B the *preexisting* adjacent 2-fiber block Grams, exact Schur gives
\[
\det G_4=\det A\cdot\det(B-C^T A^{-1} C).
\]
For any fixed original coordinate pair (i,j) with cross-entry c, original positive diagonals u,v, the Cauchy/Fischer canonical-correlation estimate gives the certificate
\[
\det G_4\, u v \le \det A\det B\,(uv-c^2).
\]
The verifier selects the first nonzero cross entry in deterministic original lexicographic order, checks it separately via Phase204's full ordinary jets and original 2,2D metric, then checks the exact integer inequality. This is an independently reproducible sufficient determinant bound, not an extrapolated asymptotic correlation rate. The cross entries of opposite monomial parity vanish as an explicit negative control.

**Measured finite exact lower on log saving over the OLD pair-product baseline:**
| D | all original rows | quartets | strict quartets | certified K: log(V_pair/V_four)>K ln 2 | approximate actual extra log saving | approximate normalized extra gain |
|---|---:|---:|---:|---:|---:|---:|
| 283 | 140 | 17 | 17 | **266** | 191.898451531 | 0.0195814746 |
| 403 | 400 | 25 | 25 | **1027** | 720.520285186 | 0.0180130071 |

The K numbers are *exact integer* comparisons of fraction-free determinants of the original quartet and its existing paired principal blocks. The approximate values are illustration, not a numerical proof. All original 140/400 rows are covered, though **the full 140x140/400x400 Gram determinants were not evaluated**.

**Do not double-count the old pair saving.** Phase207's already proven finite D403 layer-cake bound is `log(V_rad/V_pair)>=251 ln2`. The exact same pair partition is checked. The NEW bound is
\[
\boxed{\log\det G_{403} \le \log V_{\rm four}
< \log V_{\rm rad} - (251+1027)\log2
=\log V_{\rm rad}-1278\log2 .}
\]
This is a strictly better finite same-source Archimedean upper and is compatible with all original p-local lower certificates, which remain unchanged. It proves **no** field-discriminant cutoff improvement because D403 does not supply the growing-D field-theorem regime.

**Frame semantics:** the exact determinant-one real shear F_t between the old paired blocks and the conditioned pair is checked at t=0,1/2,1 on one frozen quartet per D. It is generally not in GL(Z) or GL(Z_p), so local Smith is not transported through F_t. This is a moving frame of a positive symmetric real Gram, **not** the separate Phase287 adiabatic Schr evolution or a new Berry curvature. The Phase288 integer transverse completion remains a distinct lattice-preserving construction.

## Why this is not yet the needed UNIFORM theorem

The exact 2-sample normalized gains \(\approx0.0196,0.0180\) are suggestive but make no asymptotic statement. For a growing family R,S(D), one must prove a lower bound on the accumulated Schur residual entropy
\[
L_4(D)=\sum_{\mathcal Q}\sum_{j=1}^{m_\mathcal Q}
   -\log(1-\sigma_{\mathcal Q,j}^2),
\]
where the \(\sigma_{\mathcal Q,j}\) are canonical correlations across the two paired fiber subspaces in the original source, not imported from a surrogate theta. A **sufficient** production-scale criterion is that \(\Omega(RS)\) modes obey \(1-\sigma^2\le e^{-cR}\), giving \(L_4(D)=\Omega(R^2S)\); it is not implied by the finite computations. A single first nonzero cross-entry per quartet, or any O(R) fixed-correlate witnesses, is too weak to certify that scaling without additional structure. The origin/dyadic-coset external channels from Phase288 cannot be used as extra arithmetic factors.

## Independently predeclared next discriminator: D=563

D563 is squarefree, \(\equiv3\pmod4\); original helper predicts \(\rho=51,R=140,S=J=5\) (n=700). This is a **different, larger source**, deliberately not selected for favorable measured gains. Its original ellipse Q must be recomputed and verified via an independent integer-norm enumerator before any source Gram computation; no predicted numerical K or gain threshold beyond positivity will be fitted.

For R140/S5, the deterministic same-parity partition should yield **72 old pairs, 36 new quartets, zero leftover**; all 700 original rows must appear once. Run precisely the same quartet/Fischer/second-original-jet/Schur logic. Freeze this test before implementation. Report the actual K and \(L_4/(R^2S)\) as a third-scale observation without promoting a uniform theorem; **D563 has different local-prime inertness status**, which is irrelevant to the source-matched real-place upper but prevents assuming identical p-adic factors.

Stop if the third sample fails source count, block positivity, original-jet agreement, no-overlap or any frozen analytic control. Treat a falling normalized gain as evidence against naïve constant extrapolation, not a failure to adjust the test.
