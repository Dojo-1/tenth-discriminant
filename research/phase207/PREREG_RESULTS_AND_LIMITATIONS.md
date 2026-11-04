# Phase207 · full moving Schur flag and high Frobenius-depth source audit

**Preregistration date:** 4 November 2026, before Phase207 calculations, with separate [analytic protocol #146](https://github.com/Dojo-1/tenth-discriminant/issues/146), [arithmetic protocol #147](https://github.com/Dojo-1/tenth-discriminant/issues/147) and [type/audit protocol #148](https://github.com/Dojo-1/tenth-discriminant/issues/148). This draft is stacked on [Phase206 PR #145](https://github.com/Dojo-1/tenth-discriminant/pull/145), pinned at base commit e9609ee4dff374a78a3451227e935810e9820d44. The complete source protocol predates all Phase207 code. Parent exact-source and Markdown passes are not automatically passes of this new branch.

**One scope per claim:** Original integer-pair ordinary-Z jets, W frozen DURING differentiation, original full ellipse, original row-major \((r,s)\), all \(j<J\), and integer-coordinate metric \(B=\operatorname{diag}(2,2D,\ldots)\). D283 and D403 remain *different* source worlds. D403 is newly tested at **both** the real Archimedean and p3/p5 local fibres, but there is NO isomorphism between those fibres. Neither D is assumed class-number-one, so the existing actual-field bound \(322^4\) is untouched.

## A: full matching and the shape of the deep spectrum

Frozen worlds and matching:
- D283, rho31, R70 S=J2, Q169; 35 disjoint same-parity fibre pairs.
- D403, rho40, R100 S=J4, Q219; 51 disjoint same-parity fibre pairs.
- d ranges through \(1-S,\dots,R-1\). Split by d parity and pair consecutive available d values within each parity. No chosen pairs after viewing results.

For any original positive block \(G_{d,e}=\begin{psmallmatrix}A&C\\ C^\top&B\end{psmallmatrix}\), let \(S_{d,e}=B-C^\top A^{-1}C\succ0\). The squared canonical-correlation **residual** eigenvalues \(\delta_i\in(0,1]\) of the generalized pair \((S_{d,e},B)\) have total log saving \(-\sum_i\log\delta_i\). This is independent of a simultaneous invertible row gauge on the second fibre, unlike individual coordinate entries. At a rational threshold \(\theta>0\), the exact number of \(\delta_i<\theta\) equals the negative inertia of \(S_{d,e}-\theta B\).

**Fixed thresholds:** \(1/2,1/8,1/64,1/1024,2^{-\lceil R/10\rceil},2^{-\lceil R/4\rceil}\). Coincident numerical thresholds retain both labels. Every threshold is exact rational. [Script](full_schur_spectrum.py) uses exact rational symmetric-congruence inertia including a 2×2 fallback for zero diagonal pivots; checks the exact Schur determinant ratio, SPD residual, monotone threshold counts, explicit one-step unimodular gauge on the second fibre, same-source Phase206 three-pair regression, original reflection parity zero cross block, and retained j=J−1 negative control. It reports counts AND fraction of all RS original rows, not a single determinant. A zero generalized eigenvalue at a preregistered θ is flagged as a boundary, never rounded away.

**Prior P:** disjoint first-trace \(\sum\tau/(R^2S)\le1/(2R)\) prohibits a uniform constant via \(\tau\) alone; three original pairs span only O(S) modes. **H:** an extensive set of \(\delta_i\lesssim2^{-cR}\) in the full matching, requiring a source-computable approximation map, not merely numerical samples. **Stop:** if stringent \(R\)-dependent thresholds have zero/low counts, say so; no uniform theorem follows even if finite counts are large.

## B: original Frobenius rows in the middle/high strata

Take the **unchanged D403** source with rho40, R100, S=J4, |Q|219, n=400, **m=1752 integer coordinate columns**. Its source can be evaluated at p3 and p5, both inert since \(-403\) is nonsquare modulo either p (and neither p divides D). The odd-prime source trace weights 2 and 806 remain p-units. The original row basis is already in [RectangularBasisMatrix.lean](../../lean/TenthDiscriminant/RectangularBasisMatrix.lean):
\[
k_{r,s}(p)=\min(\lfloor r/p\rfloor,S-1-s),\qquad
F_{r,s}=Z^{r-pk}W^s(Z^p-W)^k
=\sum_{t=0}^k(-1)^t\binom{k}{t}Z^{r-pt}W^{s+t}.
\]
Its determinant is one. The **old** certified divisor is \(p^{2F_p}\), \(F_p=\sum_{r,s} k_{r,s}\); it cannot be added again as an improvement.

The [exact source script](middle_frobenius.py) prospectively freezes two nested row subsets \(\mathcal I_2=\{k\ge2\}\), \(\mathcal I_3=\{k\ge3\}\). For every selected p,z,j,r,s it evaluates the original ordinary derivative by the exact expanded polynomial and falling-factorial coefficients in the integer-pair algebra modulo \(p^4\), with W frozen. On preselected first/middle/last rows of each stratum, an independent truncated-dual-number oracle evaluates \(j!\,[h^j]F_{r,s}(z+h,\bar z)\) at every original source point. Source divisibility by \(p^k\) is required *before* reduction modulo p. All 1752 quotient columns are retained. Independent deterministic first/middle/last original-row checks use **truncated dual-number polynomial multiplication** in \(h^4=0\), not just a second call to the monomial derivative formula.

Let \(d_t=|\mathcal I_t|-\operatorname{rank}_{\mathbb F_p} C_0[\mathcal I_t,:]\). The subsets are nested, so \(0\le d_3\le d_2\), and no one may add them. The full original source determinant obeys
\[
v_p(\det G_D)\ge2F_p+2d_2
\]
provided the full original matrix is nonsingular in characteristic zero and the existing row-source factorization is valid. This is a certified *lower* on additional **evaluation-lattice index**, NOT the exact full Smith profile and NOT a lower on a primitive restricted-pairing radical. To prove a uniform production improvement one still needs uncounted index/depth of order \(R^2S\) across admissible large D, with every high ordinary derivative intact.

**Countercontrols:** previously known split D287,p3 fails factorization of \(Z^3-W\) at (1,1); dropping high j changes the source. A zero high-strata defect is a valid negative result, not a mandate to change the strata or enlarge modulus. No full 400-row Smith decomposition or high-precision lift is claimed.

## C: adversarial/source-type closure

[Executable type-audit](audit_source_guards.py) checks the old Frobenius-depth census, original metric invertibility at odd p3,p5, non-substitutability of Hasse divided derivatives for ordinary j=p, and a two-row exact toy case showing that one p-local evaluation rank defect forces a Gram \(p^2\) factor. Its arithmetic scope includes neither p2 nor p|D, where ambient B can degenerate.

Analytic gauge invariance is an **internal exact same-source** change of basis inside the fibre; it is not a real-to-p transport. The middle-strata test distinguishes a source row change (unimodular over Z) from a non-unimodular p-local normalization by \(p^{-k}\). None of the current scripts equates the resulting matrices between different D, primes, supports or derivative conventions.

**Evidence ledger:**
- **P, classical paper:** Schur/Courant–Fischer inertia, invariant-factor rank-defect lower, unimodular row factors, combinatorial k-depth bounds. Earlier repository prior art is retained.
- **M, only after execution:** exact finite generalized-eigenvalue counts and local middle-strata nullities. No automatic promotion from passing scripts to original actual-field theorem.
- **H:** uniform \(\Theta(RS)\) exponentially close canonical-correlation modes and uncounted \(\Theta(R^2S)\) p-adic depth under class-number-one hypotheses.
- **R:** fixed positive constant via a disjoint first-trace lower, automatic addition of column j! and row p^k, treating finite D403 as a new class-one case.
- **Human review:** [#50](https://github.com/Dojo-1/tenth-discriminant/issues/50), external comparator [#51](https://github.com/Dojo-1/tenth-discriminant/issues/51) remain open.

**Stop/promotion:** exact-head scoped GitHub CI must pass; whole-root Lean/build and semantic/source review remain separate; keep draft PR, no merge, no new field cutoff, no outside communication without authorization.

## Exact-source execution receipt and bounded results (recorded AFTER the preregistration)

The original Phase207 source checks passed at [run 41835855791](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41835855791), after a purely operational Python import-path fix. A later separately preregistered **independent rank replay** and **post-result layer-cake mathematical deduction** passed at [run 41836160864](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41836160864) on source head bb350d8ca257364c066f088e066415ee258b52b6. These receipts precede this dossier update, so the latest-head CI still needs to be checked separately. Original test/source failure, if any, would remain a distinct issue from the earlier import defect.

**A, moving multi-mode flags.** The full original parity-matched Schur residual spectra contain:

| Original source | Pair count | Residual modes | Number <1/2 | <1/8 | <1/64 | <1/1024 | <2^-ceil(R/4) |
|---|---:|---:|---:|---:|---:|---:|---:|
| D283,R70,SJ2,Q169 | 35 | 69 | 0 | 0 | 0 | 0 | 0 |
| D403,R100,SJ4,Q219 | 51 | 200 | **65** | **33** | **24** | **12** | **0** |

At D403, θ_R=2^-ceil(R/10)=2^-10 coincides with 1/1024; **12** of the 200 canonical-correlation residuals are below θ_R. None is below 2^-ceil(R/4)=2^-25. These tests distinguish existence of a few deep modes from a proven extensive family of exponentially small residuals. The values are exact integer inertia counts from rational Schur forms, not fitted floating eigenvalues. The zero D283 counts and gauge/derivative/parity controls are preserved.

**A, POST-RESULT deduction, NOT another preregistered outcome.** The previously frozen four thresholds give the D403 cumulative eigenvalue counts (65,33,24,12). Since
\[
L=\sum_i-\log\delta_i=\int_0^\infty \#\{\delta_i<e^{-t}\}\,dt,
\]
the monotone counting function yields the **rigorous source-matched layer-cake lower**
\[
L\ge(65+2\cdot33+3\cdot24+4\cdot12)\log2
=251\log2>\frac{14056}{81}.
\]
The last inequality uses only \(\log2=2\sum_{m\ge0}[3^{-(2m+1)}/(2m+1)]>2(1/3+1/81)=56/81\). Thus at this ONE fixed D403, \(R^2S=40000\),
\[
\boxed{\frac{L}{R^2S}>\frac{1757}{405000}\approx0.00433827>\frac{43}{10000}.}
\]
The comparison with 0.0043 is to a **historical, conditional research target**, not the current threshold for improving the mainline 322⁴ theorem. The calculation is based only on exact small original moment/Schur blocks; the determinant of the full 400×400 Gram is NOT required to construct the lower certificate. [Executable post-result check](layer_cake_certificate.py) re-runs the frozen original-source inertia and performs the rational inequality without approximating \(\log2\) numerically.

**B, original middle/high Frobenius row strata.** At the SAME D403,R100,S=J4,Q219 source, the old row basis and its already-counted indices are \(F_3=570,\ F_5=550\). Independent original-source dual-jet and GFp rank controls passed:

| p | k≥2: rows/rank/defect | k≥3: rows/rank/defect | Uncounted first-level exponent ≥ | Combined valuation lower for this G |
|---:|---|---|---:|---:|
| 3 | 188 / 54 / **134** | 91 / 27 / 64 | 268 | \(v_3(\det G)\ge1408\) |
| 5 | 180 / 120 / **60** | 85 / 60 / 25 | 120 | \(v_5(\det G)\ge1220\) |

The inner k≥3 deficit is already contained within the k≥2 deficit; **never add it again**. Original full-row positive definiteness is supported by the repository's interpolation criterion \(|Q|>2(R-1)+(S-1)\), here \(219>201\); this semantic link still warrants independent human review. Therefore the same finite original determinant has the **mixed integer divisor**
\[
\boxed{3^{1408}5^{1220}\mid\det G_{D403,R100,S=J4,\rho40}}.
\]
This is a conservative lower-bound divisor; exact full p-adic Smith exponents at D403 have NOT been determined. It depends on original *inert* p3,p5 and the already-known old polynomial row map, and is separate from D283's exact \(v_5=520\). The independent column-pivot rank algorithm and deterministic reversal of paired point columns both reproduce k≥2 ranks; the different h-truncated polynomial oracle verifies selected rows at every original point and all j. These are correlated AI-authored code paths, not human mathematical certification.

**C, asymptotic stop rules (P, simple linear algebra):** A single first-stage local rank nullity \(d_p\le RS\) yields normalized additional prime mass at most \(2d_p\log p/(R^2S)\le 2\log p/R\). With only p3,p5 this is bounded by \(2\log15/R\to0\). Therefore the *observed* nonzero middle/high **FIRST-LAYER** defects cannot alone certify a uniform fixed positive new mass in the actual production limit; need deeper p-adic valuation layers, possibly extensive as \(R,S\) grow, with pre-existing \(F_p\) counted once. On the analytic side the exact D403 post-result certificate is finite, and D283 supplies a clear hostile case (zero below every chosen deep threshold); uniform \(\Theta(RS)\) modes of defect \(e^{-\alpha R}\) remain H, not P.

**Final claim ledger:** (P) classical Schur/inertia, source Frobenius determinant factorization conditional on the unchanged integer row map and original full rank, and layer-cake inequality; (M) two finite spectral distributions and two conservative extra local divisors; (H) uniform middle/high depth *beyond first layer* and production-scale deep subspace construction; (R) constant normalized gain from disjoint first trace, additive counting of nested defects, automatic promotion from historical 0.0043. Do not merge or modify the integrated \(322^4\) field theorem. External human mathematical review #50 and comparator interface #51 remain open.

### One finite, genuinely source-matched arithmetic–analytic sandwich

For the **same** \(D=403,\rho=40,R=100,S=J=4,Q219\) original integer trace Gram \(G\), no identification of arithmetic/Archimedean fibres is needed to combine their constraints on the same positive integer determinant. Let \(V_{\rm rad}=\prod_d\det G[I_d,I_d]\), a product of original principal radial blocks. Then, from the two valid inert-prime divisors and classical Hadamard–Fischer plus the exact threshold layer-cake:

\[
\boxed{
1408\log3+1220\log5
\ \le\ \log\det G
\ \le\ \log V_{\rm rad}-L
\ <\ \log V_{\rm rad}-\frac{14056}{81}.
}
\]

This is a **finite-source inequality** whose proof components have different evidential status: the general linear-algebra inequalities are classical [P paper], the prime ranks and Schur inertia are exact but AI-authored computational instances [M], and translation to class-number-one fields or a uniform cutoff remains [H]. The finite inequality does not claim a contradiction, does not use the selected complex minor of another investigator, does not multiply the nested Smith defects, and does not promote the historical 0.0043 normalized target into the present 322⁴ theorem.

**Smallest surviving new research target:** construct a uniform *source-computable* lower on the number of Schur defects \(\delta\le e^{-\alpha R}\) across \(\Omega(RS)\) matched modes **or** an uncounted deep p-adic Smith filtration of total mass \(\Omega(R^2S)\) after old \(\sum k_{r,s}\) extraction, with all derivative depths. The finite cross-world experimental contrast D283 vs D403 supplies a counterworld to naive monotonicity, not a proof of such a theorem.
