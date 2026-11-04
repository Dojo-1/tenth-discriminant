# Phase208 · sparse analytic witnesses and second-depth Frobenius indices

**Prospective registration:** 4 November 2026, before Phase208 code, in [analytic #150](https://github.com/Dojo-1/tenth-discriminant/issues/150), [arithmetic #151](https://github.com/Dojo-1/tenth-discriminant/issues/151) and [source audit #152](https://github.com/Dojo-1/tenth-discriminant/issues/152). Stacked on [Phase207 draft #149](https://github.com/Dojo-1/tenth-discriminant/pull/149) at source head 5a254f889dc65b318ce509aa70a447f5d05c95d7. Original field cutoff \(322^4\) is unchanged. The common original source is an integral evaluation matrix \(E_D\) with all ordinary \(Z\)-derivatives, \(W\) frozen during differentiation, complete ellipse \(Q\), original row-major monomials, and trace weights \(2,2D\). D283 and D403 are different source worlds; neither is assumed class number one.

## A · an explicit source-computable analytic approximation map

Retain the original full parity-matched fibre pairs from Phase207: D283 has R70,S=J2,Q169 and 35 pairs; D403 has R100,S=J4,Q219 and 51 pairs. For a matched pair d,e=d+2, write its SAME original positive source Gram in blocks
\[
\begin{pmatrix}A&C\\C^T&B\end{pmatrix},\quad
S_{\mathrm{opt}}=B-C^TA^{-1}C.
\]

**Frozen simple hypothesis:** choose a sparse map \(L\) from target fibre row (r,s) to predecessor (r−2,s) when present in the first fibre; assign the single rational coefficient \(t=G_{(r-2,s),(r,s)}/G_{(r-2,s),(r-2,s)}\), with no other row mixing. This is a deterministic original-jet one-parent rule, computable from low-dimensional source moments. It is **row-frame dependent** and is NOT claimed invariant under arbitrary row shears.

For this map, \(S_{\mathrm{trial}}=B-C^TL-L^TC+L^TAL\). Classical exact algebra gives
\[
\boxed{S_{\mathrm{trial}}-S_{\mathrm{opt}}
=(L-A^{-1}C)^TA(L-A^{-1}C)\succeq0.}
\]
Consequently the number of generalized eigenvalues \(S_{\mathrm{trial}}w=\lambda Bw\) below any positive \(\theta\) can never exceed those of \(S_{\mathrm{opt}}\). This direction is critical. The preregistered rational thresholds are \(1/2,1/8,1/1024,2^{-\lceil R/10\rceil}\). The [exact test](sparse_schur_map.py) computes all original principal source blocks, both residuals and exact symmetric inertia; it reports sparse versus optimal deep-mode counts across all pairs, and a 1D counterexample with optimal residual 7/16 while zero sparse map residual is 1. The claim of uniform \(\alpha,\kappa>0\) remains **H**, not a property granted by the exact identity.

**Kill:** If no sparse trial mode survives below 1/1024 at D403 where Phase207 found 12 optimal deep modes, retire the one-parent mechanism at this frozen source. Do not retire the existence of optimal correlations or replace the sparse map with \(A^{-1}C\) to claim an explicit miracle.

## B · second \(p\)-adic layer on the SAME production-shaped D403 source

Here the source is specifically D403,rho40,R100,S=J4,Q219: 400 original rows × 1752 integer-coordinate columns, with all ordinary jet orders j=0,1,2,3. Both odd p=3 and5 are inert and the trace metric is p-adically nondegenerate. The **already certified** unimodular old Frobenius row is
\[
F_{r,s}=Z^{r-pk}W^s(Z^p-W)^k,\quad
k=\min(\lfloor r/p\rfloor,S-1-s).
\]
It extracts **already counted** \(F_3=570,F_5=550\) and factors \(p^{2F_p}\). We do not add them again.

The predeclared selected row subset is ONLY \(I_2=\{(r,s):k\ge2\}\), 188 rows at p3 and 180 at p5 (nested k≥3 is not an independent divisor). For every selected row and every original point/jet coordinate, evaluate its polynomial expansion modulo \(p^5\) (enough for the declared \(p^{k+2}\) precision since \(k\le3\)), verify divisibility by \(p^k\) BEFORE division, then form the normalized \(C_0[I_2,:]\) mod \(p^2\). The [exact test](truncated_middle_smith.py) finds all unit factors by unimodular pivots over \(\mathbb Z/p^2\), divides the residual block by p and computes its mod-p rank. This yields **truncated** Smith levels
\[
(0:r_0,\ 1:r_1,\ \ge2:r_2),\quad
r_0+r_1+r_2=|I_2|,
\]
and the certified minimal additional index \(I_{\min}=r_1+2r_2\), with the last level at least two rather than exactly two. It must reproduce the Phase207 first ranks r0=54/120.

**Why subset index implies full-source divisor [P classical].** Any full maximal minor of the normalized 400-row original E can be expanded along the selected \(I_2\) rows. Each term contains a full \(|I_2|\)-minor of \(C_0[I_2,:]\), divisible by \(p^{I_{\min}}\). Hence every full normalized maximal E minor is divisible by \(p^{I_{\min}}\). Using the original integral trace metric in Cauchy–Binet then gives
\[
\boxed{v_p(\det G_D)\ge 2F_p+2I_{\min}.}
\]
This is a **finite lower bound** and need not be exact; the primitive residual pairing and full source Smith factors are NOT evaluated here.

Controls: two independent modular rank algorithms must agree; toy diag(1,p,p²) and integer row/column shear must preserve \((0,1,\ge2)\) levels; a deterministic original dual-number jet oracle checks selected first/middle/last source rows at all Q points and all ordinary j. No precision increase, no new prime set, no scope migration, and no unlabeled additivity of nested ranks.

## C · semantic and adversarial gates

[Type/audit script](audit_three_lines.py) verifies the original trace metric \(2,2D\) versus incorrect Euclidean \(2,2\), ordinary \(j=3\) derivative \(3!=6\) versus Hasse coefficient 1, the original Frobenius exponent census, small integer subset-minor valuation controls and a restricted-pairing isotropy counterexample. It distinguishes source row (unimodular) from p-division (not unimodular), sparse coordinate-frame dependence from optimal Schur gauge invariance, and locally measured Smith levels from exact field valuation. Parent Phase207 high-level values remain the matched baseline.

**Evidence boundary:** classical Schur and Smith/Laplace identities = P under explicit types; bounded exact finite results = M only after exact-head CI; a uniform \(R\)-dependent analytic or local arithmetic gain = H; false disjoint first-trace constant and automatic factorial double counting = R. Independent human meaning review [#50](https://github.com/Dojo-1/tenth-discriminant/issues/50) and external cross-source check [#51](https://github.com/Dojo-1/tenth-discriminant/issues/51) remain open. Keep all PRs draft, do not claim class-number-one D403, no new bound beyond integrated \(322^4\).

## Exact-source outcomes, after prospectively registered Phase208 tests

[Original Phase208 scoped CI](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41839652464) passed. At D283 all 69 matched Schur residual modes remained above every selected deep threshold. At D403 (200 modes across 51 pairs), the explicit **sparse one-parent row map** certifies counts 47/32/7 at θ=1/2,1/8,1/1024, versus optimal Schur counts 65/33/12. The source map covers 196 target rows. Exact fractional PSD identity and minmax direction passed, with a toy negative showing sparse L=0 misses a genuine δ=7/16 optimal mode.

The selected \(k\ge2\) old-Frobenius rows (D403, same full Q and J) produced these **p²-truncated** Smith level profiles:
- p3: 188 rows, \((0:54,1:18,\ge2:116)\), subset extra index lower \(18+2\cdot116=250\), original Gram lower \(v_3\ge2(570+250)=1640\);
- p5: 180 rows, \((0:120,1:15,\ge2:45)\), subset extra index lower \(15+2\cdot45=105\), original Gram lower \(v_5\ge2(550+105)=1310\).

Both retain all 1752 integer-coordinate channels and ordinary derivatives through j3. The tests checked every original source row in the selected strata, alternative original dual-number evaluations on deterministic rows at all sample points, separate GFp pivots, a p² matrix toy and unit shears. **The \(\ge2\) levels are truncated, NOT exact valuation 2.** No primitive residual trace pairing was inferred.

## Follow-on registered BEFORE implementation: source class collapse and safe sparse log lower

Two further protocols were posted in #150/#151/#152 **after the first numerical results were visible**, and before the follow-on code. Therefore the following are *not* part of the original Phase208 prospective primary measurement. The [integral Frobenius quotient theorem dossier](FROBENIUS_QUOTIENT_JET_THEOREM.md) proves on paper that old-normalized ordinary source jets modulo odd inert p depend only on \(z\bmod p^2 O_D\), using the integer derivation \(\delta T=Z^{p-1}\) on the polynomial in \(T=(Z^p-W)/p\). A conjugate-stable original Q has at most \(J|Q\bmod p^2|\) independent normalized observation columns modulo p. The [exact source compression replay](frobenius_signature.py) checked the identity row-by-row and jet-by-jet, including conjugate and repeated classes, for D283/403 at p3/5.

At D403, the full normalized C0 has **rank 90 at p3 and rank 240 at p5** (out of 400), yielding \(\gamma_1=310,160\). The p² selected subset previously had \(\gamma_2\ge116,45\). A genuine **cokernel surjection** from the full normalized evaluation to its selected row subsystem implies \(\gamma_h(\mathrm{full})\ge\gamma_h(\mathrm{subset})\) at each p-depth h. Hence **different** filtration levels can be combined without double counting:

\[
\boxed{
v_3(\det G_{403})\ge2(570+310+116)=1992,\qquad
v_5(\det G_{403})\ge2(550+160+45)=1510.
}
\]

Consequently, the SAME original positive integer Gram has \(3^{1992}5^{1510}\mid\det G\). The measured ranks are finite M; the derivation of rank collapse and cokernel-grade monotonicity is classical P-paper with explicit hypotheses, neither end-to-end Lean nor human peer review. The uniform rank ceiling is only first-layer \(O(RS)\), still insufficient by itself for a constant \(R^2S\)-normalized improvement.

On the analytic side, an **important correction** was recorded in #150 *before* implementing the follow-on [safe layer-cake script](sparse_layer_cake.py): the sparse trial residual may have eigenvalues **greater than 1**, so its own negative-log sum is **not** automatically a positive lower. The *valid* order \(S_{\rm opt}\preceq S_{\rm trial}\) implies \(N_{\rm opt}(\theta)\ge N_{\rm trial}(\theta)\) and therefore for the actual optimal Fischer saving

\[
\boxed{
L_{\rm opt}\ge(47+2\cdot32+7\cdot7)\log2
=160\log2>\frac{8960}{81},\qquad
\frac{L_{\rm opt}}{R^2S}>\frac{28}{10125}
}
\]
at the frozen D403, using \(\log2>56/81\). This is a *post-result deduction* based on originally preregistered mode counts and an explicitly source-computable sparse map. It remains below the historical 0.0043 research target and is not a new field cutoff.

**Exact-head verification gate:** the expanded scoped CI must be rechecked on the final commit after these docs; the previous GitHub run at the code head succeeded, but documentation changes trigger new workflows. No claim of current-head Lean pass or external mathematical review is made until a matching receipt is inspected. No merges, no altered mainline \(322^4\) theorem, and no equating fibres at different places.
