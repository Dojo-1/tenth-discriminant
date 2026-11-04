# Phase206 — three preregistered lines, one matched source, two honest residuals

**4 November 2026.** Protocols were written *before tests* in [analytic #142](https://github.com/Dojo-1/tenth-discriminant/issues/142), [arithmetic #143](https://github.com/Dojo-1/tenth-discriminant/issues/143) and [adversarial/type audit #144](https://github.com/Dojo-1/tenth-discriminant/issues/144). Later dense-matching and second-stage Smith tests were separately preregistered **before their execution** in the same issues. This branch is stacked on [Phase205 #141](https://github.com/Dojo-1/tenth-discriminant/pull/141), which has passed all three of its Lean, exact-arithmetic and Markdown workflows. No new class-number-one conclusion, updated 322⁴ cutoff, novel generic theorem, or independent human verification is claimed.

## Fixed original source and type constraints

**Primary specimen (both lines):** squarefree \(D=283\equiv3\pmod4\), \(R=\lfloor D/4\rfloor=70\), \(S=J=\lfloor R/25\rfloor=2\), \(\rho=\lceil(11/25)D^{3/4}\rceil=31\), original **complete** ellipse \(Q=\{(x,y)\in\mathbb Z^2:x^2+283y^2\le31^2\}\), with \(|Q|=169\). Exactly 140 rectangular rows \((r,s)\), all ordinary \(\partial_Z^j Z^rW^s\), \(0\le j<2\), *holding W fixed in differentiation*, original real/imag integer channels \(m=2J|Q|=676\) and \(B=\operatorname{diag}(2,566,\ldots,2,566)\). Same \(G=EBE^{T}\) for arithmetic and analytic comparisons. **No class-number-one assumption**: both \(p=3,5\) are inert because \(-283\bmod 3=2\) and \(-283\bmod5=2\). Inertness suffices for the **pointwise modular factorization** but NOT the field theorem.

**Secondary analytic stress only:** \(D=403=13\cdot31\), \(R=100,S=J=4,\rho=40,|Q|=219\). This is a **different** integer Gram and therefore NOT a simultaneous arithmetic/analytic inequality about the \(D=283\) determinant.

## A — the actual multidimensional moving modes, not a scalar trace heuristic

For a fixed pair of radial fibres \(I_d=\{(r,s):r-s=d\}\) and \(I_{d+2}\), reconstruct the original principal block from integer-pair derivatives **and independently from Phase139 mixed moments**. Let \(A,B,C\) be its within/cross blocks. Exact \(d_A,d_B,d_{\mathrm{joint}}>0\) imply
\[
0\le\tau_{d,d+2}=\operatorname{tr}(A^{-1}CB^{-1}C^T)\le\min(|I_d|,|I_{d+2}|),\quad
L_{d,d+2}=\log\frac{d_A d_B}{d_{\mathrm{joint}}}\ge\tau.
\]
All reported logs derive only **after exact integer determinant positivity**, and no unknown whole-gram determinant is used in choosing a frame.

**Original three preregistered pairs** \(d\in\{\lfloor R/4\rfloor-1,\lfloor R/2\rfloor-1,R-S-7\}\):
- D283: d=16,34,61, pair sizes (2,2). Individual gains 0.745698, 0.852439, 0.894789, sum 2.492925, normalized by R²S=9800 gives **0.000254380**. Trace total 2.027493, normalized 0.000206887.
- D403: d=24,49,89, pair sizes (4,4). Individual gains 3.078830, 5.734471, 9.935762, sum 18.749063, normalized by R²S=40000 gives **0.000468727**. Trace total 6.420853, normalized 0.000160521.
Both direct and mixed-moment reconstructions agree for every tested block entry. Cross-parity blocks vanish; dropping j>0 changes the source, the deliberate negative control.

**FOLLOW-ON matching, separately preregistered first**: list every radial fibre \(d=1-S,\dots,R-1\), partition by parity, and pair consecutive fibres within each parity, leaving at most one singleton. Absolutely no data-driven re-pairing:
- D283: **35** disjoint pairs, 138/140 rows covered; log Fischer improvement **26.211688459**, normalized **0.002674662088**.
- D403: **51** disjoint pairs, 398/400 rows covered; log Fischer improvement **274.584187422**, normalized **0.006864604686**.
Every joint principal determinant is positive, and its gain nonnegative. The second finite normalized gain is above the historical **0.0043** research threshold; the first is below it. Therefore the finite results neither prove a production-uniform lower nor establish monotonicity, and **0.0043 belongs to an older cutoff proposal, not to the integrated 322⁴ theorem**. No class-number-one field was used.

**Non-negotiable analytic scaling barriers [P, paper]:**
- For disjoint pairs \(\sum\tau\le RS/2\) so \(\sum\tau/(R^2S)\le1/(2R)\); the uniform constant from *first trace alone* is **R, retired**.
- For canonical-correlation residuals \(\delta_i=1-\sigma_i^2\in(0,1]\), \(L=\sum-\log\delta_i\). If \(L\ge cR^2S\) among \(\le RS/2\) modes, some \(\delta_i\le e^{-2cR}\); this is **NECESSARY**, not sufficient. A real production advance requires source-estimable very small Schur eigenvalues (or a different rigorously costed architecture).
- A finite \(\rho^2-M_2\) boundary gap can collapse with D; Phase139 D95/rho10 gives \(\Delta=1\), invalidating an unguarded uniform boundary-concentration argument. Every j<S contributes.

## B — uncounted arithmetic index AFTER the actual Frobenius basis, not twice-counted p-mass

Use the **already proved** integral unitriangular \`RectangularBasisMatrix.lean\` at p3,p5. Since S=2, its row exponent is \(k_{r,s}=\min(\lfloor r/p\rfloor,1-s)\), so \(F_p=\sum k_{r,s}=R-p\) and the inherited, already counted divisor is \(p^{2F_p}\). The transformed row with (s=0,r>=p) is exactly \(Z^r-Z^{r-p}W\), all other rows unchanged. Divide **every original integer/ordinary jet coordinate** by p on those rows; verify divisibility at every Q point and j, not just a selected column.

Initial **same-E finite test** at D283:
| p | existing 2F_p | rank modp of first quotient C0 | uncounted evaluation index ≥ | extra determinant exponent ≥ |
|---|---:|---:|---:|---:|
| 3 | 134 | 36/140 | 104 | 208 |
| 5 | 130 | 60/140 | 80 | 160 |

For any integral n×m C0 with rank r modp, an invertible p-local row change can make \(n-r\) entire rows divisible by p, implying \(v_p(\det(C0BC0^T))\ge2(n-r)\). This is a classical source-independent **conditional rank lemma**, not a universal production lower, and avoids calling a nonprimitive C0 metric radical a genuine primitive residual.

**Second-stage, preregistered modular Smith with the ROW map recorded, at precision p⁶ only**:
- p3 secondary levels {0:36,1:9,2:9,4:36,5:9,6:41}. Level6 denotes **41 unresolved exponents ≥6**, not 41 exact sixes. The recorded minimum secondary index is 462. Therefore \(v_3(\det G)\ge 2F_3+2(462)=1058\). **Do not** compute/claim a primitive residual H1.
- p5 secondary levels {0:60,1:15,2:30,3:20,4:15}. No level6 truncation; secondary index is **exactly 195**. The normalized primitive C1 (constructed using ONLY the tracked p-local **row operations**, not the source-changing Smith column operations) has full F5 rank140. Its restricted original-metric \(H_1=C_1BC_1^T\) is also nondegenerate mod5. Therefore
\[
\boxed{v_5(\det G_{D=283,R=70,S=J=2,\rho=31})=2(65)+2(195)=520.}
\]
This is a **finite arithmetic identity** from modular local Smith and nondegenerate residual matrix, not a statement about class-number-one production or a new cutoff. It proves that all p5 uncounted mass in this specimen is an **extra evaluation-lattice index**, not a final primitive residual-pairing valuation.
- Counterworld D287,p3 split: the source \(Z^3-W\) fails divisibility at q=(1,1), with exact remainder \((0,2)\in\mathbb F_3^2\). No inertness → no extracted old factor.

The secondary p3 truncation was **deliberately not raised** after viewing results; further precision requires a new prospective protocol. p2 is separate: the trace metric degenerates mod2 and the old binary factor must not be added twice.

**Why this still does not solve the actual-field problem:** in the production chart \(R\sim D/4\), \(S\sim R/25\), the normalization is \(R^2S\), while the current finite \(S=2\) Smith depth is not uniform across these changing dimensions. To obtain a *constant* new \(p\)-mass one needs \(\sum u_i+\tfrac12\sum b_i=\Omega(R^2S)\), meaning extensive p-local depths, not just a large rank deficiency at one small D.

## Additional prospective checks — modal depth and independent primitive-unit witness

**Both tests were separately preregistered in #142/#143/#144 before being run** on the frozen two source worlds. They are **additional measurements**, not after-the-fact changes of radial pairs or arithmetic hypotheses.

### Exact rational generalized-eigenvalue counts

For each original three selected fibre pairs per D, form the actual Schur residual \(S_{d,e}=B-C^TA^{-1}C\) **over \(\mathbb Q\)**. For the preselected thresholds \(\theta\in\{1/2,1/4,1/8\}\), count the generalized eigenvalues of \((S_{d,e},B)\) below \(\theta\) via the **negative inertia of \(S_{d,e}-\theta B\)**, computed from exact rational leading principal minors and LDL-sign changes. Every residual matrix is SPD; its exact determinant ratio agrees with the joint Gram / product of within-fibre determinants. No floating eigenvalue fitting or numerical threshold changes.

| D | Three fixed pairs | Total modes | \(\delta<1/2\) | \(\delta<1/4\) | \(\delta<1/8\) |
|---:|---|---:|---:|---:|---:|
| 283 | (16,18),(34,36),(61,63) | 6 | **0** | **0** | **0** |
| 403 | (24,26),(49,51),(89,91) | 12 | **5** | **3** | **2** |

The individual D403 \(\delta<1/8\) counts are 0,1,1 across those pairs. This distinguishes a large block-log saving from a sufficiently **extensive family** of very small residual directions. A fixed numerical threshold \(\theta\) is NOT the production-uniform \(\theta_R=e^{-\alpha R}\); nothing here proves a common \(\alpha,\kappa>0\).

The [exact rational inference script](rational_schur_modes.py) is committed and added to scoped CI. Its status is bounded [M] until an exact-head GitHub Actions receipt is obtained.

### A second determinant algorithm confirms the finite p5 equality

The p5 secondary normalization yields a primitive \(C_1\) with original trace metric \(B\). An independently coded modular row-elimination determinant test computes

\[
\det_{\mathbb F_5}(C_1 B C_1^T)=3\ne0,
\]

and a simultaneous first/last row-column swap leaves the determinant unchanged. Together with the tracked source Frobenius row map, the complete secondary p-index \(\sum u_i=195\), and the old \(F_5=65\), this confirms the **finite source** \(v_5(\det G)=2(65+195)=520\) without a full 140×140 integer determinant calculation. It is a second algorithmic witness but **not independent human mathematical validation**. [Executable check](primitive_p5_det.py) is committed and in CI; p3's 41 unresolved \(\ge6\) factors remain open.

## C — evidence ledger, transport restrictions, and next kill test

**P-paper, classical:** Schur/Fischer, canonical-correlation rank cap, p-local Smith row normalization and determinant valuation, Frobenius rectangular polynomial expansion (already in repository). **M exact finite CPU:** complete original D283/D403 tests reported above, including the in-person standard-library computations; CI promotion is separate. **H:** uniform D-dependent near-unit canonical correlations; uniform uncounted evaluation index or residual depth at the actual class-number-one hypotheses. **R:** disjoint first-trace uniform constant; transplanting D19 split p5 residual to production inert p5; treating a truncated p3 Smith level6 as exact; treating a globally modified support as the same Gram.

**Controls:** source derivative j0-only is intentionally different and rejected; signed cross-parity moments vanish; arithmetic split p3 D287 fails; original p3/p5 Frobenius factors never added again; real and finite-place fibres NOT equated. The extra numerical p5 precision uses explicit p-unit row transformations, so source metric B is never silently transported by a Smith COLUMN operation. Independent source/review Issues [#50](https://github.com/Dojo-1/tenth-discriminant/issues/50) and [#51](https://github.com/Dojo-1/tenth-discriminant/issues/51) remain open.

**Next decisive tests (requiring new preregistration before running):** (i) certify a lower bound on the number of **deep** Schur modes at rational thresholds for the already frozen fibres, not merely the product of residuals; (ii) independently verify p5 det(H1) mod5 ≠0 with a different modular elimination, and (iii) test a parameter-uniform rank/valuation bound for the original production family instead of extrapolating this small S2 example. **No merge, no new field cutoff, no outside submission.**
