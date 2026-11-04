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

The [exact source script](middle_frobenius.py) prospectively freezes two nested row subsets \(\mathcal I_2=\{k\ge2\}\), \(\mathcal I_3=\{k\ge3\}\). For each p, z, j, r,s in either subset, it evaluates the actual original derivative \(j!\,[h^j]F_{r,s}(z+h,\bar z)\) in the integer-pair algebra modulo \(p^4\), with W frozen. Source divisibility by \(p^k\) is required *before* reduction modulo p. All 1752 quotient columns are retained. Independent deterministic first/middle/last original-row checks use **truncated dual-number polynomial multiplication** in \(h^4=0\), not just a second call to the monomial derivative formula.

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
