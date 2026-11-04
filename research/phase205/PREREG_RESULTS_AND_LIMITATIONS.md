# Phase205 — matched-source arithmetic/analytic spectral sandwich

**4 November 2026.** Both finite tests were preregistered in [#139](https://github.com/Dojo-1/tenth-discriminant/issues/139) and [#140](https://github.com/Dojo-1/tenth-discriminant/issues/140) **before** calculations. Further exact residual-layer and block-attribution tests were separately preregistered in comments on those issues before executing them. This is a research instrument, **not** a new tenth-discriminant cutoff, external mathematician's construction, or novel generic Smith/Fischer theorem. Keep human semantic audit #50 open.

## One source, two independently reconstructed realizations

Freeze \(D=19,\rho=5,R=8,S=J=4\), **all 21** original lattice points \(Q=\{(x,y)\in\mathbb Z^2:x^2+19y^2\le25\}\), all 32 row-major monomials \(Z^r W^s\), and *ordinary* \(\partial_Z^j\) with \(W\) held fixed. The integer source \(E\) is \(32\times168\): each pair \((j,z)\) yields its real and imaginary integer coordinates. The original channel metric is \(B=\operatorname{diag}(2,38,\dots,2,38)\), and \(G=E B E^T\), **one fixed positive integer Gram**.

[The executable stdlib source](source_spectral_pilot.py) constructs G in two independent ways: (1) original integer-pair multiplication and ordinary jets; (2) Phase139 mixed moments \(M_{a,b}=\sum_{z\in Q}\operatorname{Re}(z^a\bar z^b)\), using its exact coefficient formula. All 1024 Gram entries match. Independent source controls: \((\mu_0,\mu_1,\mu_2,\mu_3)=(21,320,6396,135416)\) and \(G_{\{1,Z^2\}}=\bigl[\begin{smallmatrix}42&-120\\-120&15520\end{smallmatrix}\bigr]\), as previously recorded in [Phase139](../graded_moments/PHASE139_ORIGINAL_JET_MOMENTS.md). Exact determinant is positive, with \(\log\det G\approx530.285191201861\). Earlier source priority is retained, not relabelled as new.

## Track A — local Smith of E and *residual* trace pairing

At each prime p, a p-local Smith normalization, involving explicit invertible row/column operations over \(\mathbb Z/p^{22}\), yields \(U_p E=\Delta_p C_p\) in the p-adic sense, with diagonal valuations \(a_{p,i}\) and \(C_p\bmod p\) **full row rank 32**. The code independently selects a 32×32 minor of the original E and checks its **integer determinant valuation equals** \(\sum_i a_{p,i}\). Thus the evaluation-lattice Smith contribution is certified by an original-source minor, not guessed from Gram rank.

The same original metric gives
\[
\det G=p^{2\sum_i a_{p,i}}\cdot(\det U_p)^{-2}
        \det(C_pBC_p^T),
\quad
v_p(\det G)=2\sum_i a_{p,i}+v_p(\det(C_pBC_p^T)).
\]
The p-adic unit factor \(\det U_p\) may be ignored ONLY for valuations, not silently treated as 1 for equality of integers.

| p | Smith levels of E (level:count) | \(2\sum a_i\) | \(v_p(\det G)\) | Residual valuation | Residual rank mod p / radical dimension |
|--:|---|--:|--:|--:|---|
| 3 | 0:17, 1:11, 2:4 | 38 | 39 | **1** | 31 / 1 |
| 5 | 0:32 | 0 | 4 | **4** | 29 / 3 |
| 7 | 0:32 | 0 | 0 | **0** | 32 / 0 |
| 2 | 0:8, 1:8, 2:4, 3:8, 4:4 | 112 | 172 | 60 | 0 / 32 |
| 19 | 0:32 | 0 | 0 | 0 | 32 / 0 |

**Important arithmetic types:** at p=2 and 19 the ambient trace B is **degenerate modulo p** (both weights divisible at 2; 38 divisible at 19). Their residual ranks should not be interpreted using the nondegenerate ambient-isotropic terminology of p3, p5, p7. For p19 the restricted pairing remains nondegenerate despite ambient degeneracy, demonstrating another distinction.

The subsequently preregistered local lift of \(C_p\) through p^8 and an independently written residual-matrix elimination (executed locally) gives additional **vector-valued** residual Smith valuations:
- p3: 0 repeated31, 1 repeated1;
- p5: 0 repeated29, 1 repeated2, 2 repeated1;
- p7: 0 repeated32.

The p5 one-level-2 residual factor is a genuine deeper p-adic layer of THIS frozen matrix, not just a modp radical count. The independently written modular residual [certificate script](residual_gram_layers.py) is now committed and included in Phase205's scoped CI. It reproduces the p3/p5/p7 full residual Smith multisets with a separately normalized (C_p) modulo (p^8), subject to an exact-head GitHub Actions receipt. In the **different Phase135 8-row source**, p3 has one E-level1 factor and a mod3 **unit** residual Gram, a predeclared negative control against the false rule “normalized full rank always gives additional prime mass.”

**Do not add these numbers blindly to an inherited Frobenius divisor**: overlap must be checked in the exact unchanged production object. This finite example has no established uniform improvement of the integrated \(322^4\) result.

## Track B — genuinely multidimensional radial-block upper

Let \(I_d=\{(r,s):r-s=d\}\), \(d=-3,\dots,7\), the **same** Phase138 radial fibres. Its established gauge-invariant Fischer product is \(V_{\rm rad}=\prod_d\det G[I_d,I_d]\). The preregistered six-block partition was fixed BEFORE observing any gain:
- even \(d\): \(\{-2,0\},\{2,4\},\{6\}\);
- odd \(d\): \(\{-3,-1\},\{1,3\},\{5,7\}\).

Let \(V_6\) be the product of the six resulting principal-block determinants. Positive definiteness and Hadamard–Fischer give **the source-matched inequality**
\[
0<\det G\le V_6\le V_{\rm rad}\le \prod_i G_{ii}.
\]
The **fixed** test gives

| Bound / diagnostic | Natural log |
|---|---:|
| Raw original-row Hadamard | 626.255217765 |
| Phase137 centered monic frame diagonal product (reconstructed separately) | 585.557677543 |
| Phase137 Chebyshev monic frame diagonal product (reconstructed separately) | 579.753853408 |
| **Phase138 radial-fibre product** | 543.904300463 |
| **Fixed six-block product** | **542.616528367** |
| Exact \(\det G\) / complete parity product | 530.285191202 |

Thus the exact finite **extra** Fischer saving relative to the previously established radial-fibre product is
\[
\log(V_{\rm rad}/V_6)=1.28777209679,\quad
\frac{\log(V_{\rm rad}/V_6)}{R^2S}=0.00503035975309.
\]
This finite normalized number happens to exceed the \(0.0043\) threshold previously contemplated in a *conditional* large-D programme. **That is not evidence for a uniform production inequality**: no uniform moment upper for these growing blocks or derivative depths has been proved. The complete parity-sector product equals \(\det G\) for this symmetric ellipse and therefore cannot be offered as a non-circular new analytic bound.

The *post-registered, preregistered-before-computation* attribution across the five merged pairs yields logarithmic savings 0.154763154, 0.530005987, 0.097824074, 0.398183600 and 0.106995283 (in the displayed fixed order; singleton \(\{6\}\) contributes zero). All are nonnegative and sum to 1.287772097.

## A non-scalar jet covariance, and a deliberately weak moment-only bound

For rows \((r+t,s+t)\) inside one radial fibre with \(r\ge J-1\), use the original jet ratio
\[
a_t(j,z)=\frac{(r+t)_{\underline j}}{r_{\underline j}}\,(z\bar z)^t.
\]
With \(\mu(j,z)=2|e_{r,s;j}(z)|^2/G_{(r,s),(r,s)}\), the **entire** same-fibre subblock is the matrix of moments of \(a_0,a_1,\ldots\) under this probability measure. This is an exact identity derived from the frozen source, not a Euclidean change of observations. For an adjacent two-row subblock,
\[
\frac{\det G_{\{i,i+1\}}}{G_{ii}G_{i+1,i+1}}
=\frac{\operatorname{Var}_{\mu}(a_1)}{\mathbb E_\mu[a_1^2]}.
\]
The original rows \((3,1),(4,2)\) have \((G_{ii},G_{ik},G_{kk})=(8812968,222537328,6022596856)\), so the **exact** ratio is \(55532672116391/829327396387947\approx0.06696110\). A truly moment-only bound needs no unknown whole determinant: if \(0\le a_1\le A_{\max}=100\), then \(\mathbb E[a_1^2]\le100\,\mathbb E[a_1]\), giving the legitimate but **much weaker** ceiling \(41172467/55081050\approx0.7475\). Report that looseness; within-fibre pair covariance was already accounted for by Phase138's block product and is **not** the new six-block inter-fibre gain.

## A determinant-independent trace-coupling lower bound

**Registered before its execution** as a separate comment in [#140](https://github.com/Dojo-1/tenth-discriminant/issues/140). For each of the FIVE frozen disjoint same-parity fibre pairs \((d,e)\) listed above, split its original Gram into \(\begin{psmallmatrix}A&C\\C^T&B\end{psmallmatrix}\), with \(A,B\succ0\), and define the source-moment invariant
\[
\boxed{\tau_{d,e}:=\operatorname{tr}(A^{-1}CB^{-1}C^T)\in\mathbb Q_{\ge0}.}
\]
It is a non-scalar canonical-correlation quantity, well-defined on a *specified two-fibre partition* and invariant under independent invertible row gauges inside each fibre. The classical Schur identity and \(-\log(1-x)\ge x\) for \(0\le x<1\) imply
\[
\log\frac{\det A\det B}{\det G_{I_d\cup I_e}}\ge\tau_{d,e}\ge0.
\]
This is a **rigorous lower certificate for the ANALYTIC saving**; importantly, \(\tau\) only uses the already separately accessible **small** within/cross-fibre moment matrices and their inverses, not the determinant of the entire unknown 32-row Gram. It can therefore be a candidate for independently estimated production-scale gain, provided a uniform moment lower is proved.

The separate [exact rational trace oracle](correlation_trace_certificate.py) uses Fraction Gaussian elimination for A/B and never uses full det G to construct \(\tau\). It checks each trace against the matching exact Fischer gain and demands a zero cross-parity control:

| Frozen pair of radial fibres | \(\tau_{d,e}\), exact rational evaluated numerically | Actual log Fischer gain |
|---|---:|---:|
| \(-2,0\) | 0.148195593825 | 0.154763153555 |
| \(2,4\) | 0.470565677284 | 0.530005986853 |
| \(-3,-1\) | 0.093191578722 | 0.097824073583 |
| \(1,3\) | 0.364519820862 | 0.398183600101 |
| \(5,7\) | 0.101470088384 | 0.106995282700 |
| **Sum** | **1.177942759076** | **1.287772096792** |

The strict finite rational inequality
\[
\boxed{\sum \tau_{d,e} > \frac{43}{10000}\,R^2S=\frac{43}{10000}\cdot256}
\]
is tested **without float rounding**. Its normalized value is \(1.177942759076/256=0.004601338903\), exceeding the *conditional* Phase137 normalized target \(0.0043\), and capturing approximately 91.5% of the actual six-block improvement. This is a **single-small-D measurement**, not a production theorem, even though the generic trace inequality is P-paper. Opposite-parity fibre pair \((-2,-1)\) has \(C=0\), \(\tau=0\), as required by pre-existing parity.

**Critical next quantitative target [H]:** for the ACTUAL admissible production D,R,S,J,Q and the SAME source moments, find an explicit subset of disjoint same-parity fibre pairs and uniform, **determinant-independent** estimates of \(\tau\) whose total normalized lower exceeds the *actual certified upper-bound deficit* with all derivative orders present. It is not enough to prove the bound for fixed D19; the point-count support, conditional class-number chart, and high-j factorial weights can erase it. No new cutoff is claimed.

## Promotion boundary and next falsification

- **P:** Smith/determinant valuation factorization under genuine p-local row operations; trace-pairing radical identification; Hadamard–Fischer; same-fibre jet-covariance identities and the elementary bound on nonnegative moments. These are existing mathematics, not a novelty claim.
- **M:** exact finite 32×168 source, five-prime local levels and six fixed blocks; the compact [GitHub replay](source_spectral_pilot.py) covers the main source/rank/Smith/determinant tests. The two additional local controls (residual p^8 lifts and Phase137 radial-frame reconstruction) must not be described as GitHub-CI-backed until separately committed and replayed.
- **H:** a uniform lower bound on *unaccounted* residual local mass, and an independent **moment/slice-estimable** upper on growing radial unions beating the **previous certified production upper**. Both must concern exactly one unchanged positive integer \(\det G_D\), with original inert-prime and field hypotheses.
- **R:** treating the finite 0.00503 gain as a verified 0.0043 production saving; reusing p5 residual in a different D or a different selected minor; counting the same prime-power factor twice; interpreting the parity product \(=\det G\) as a useful independently estimable upper; conflating the chosen \(\mathbb Z[\sqrt{-D}]\) order with the full ring of integers without a source bridge.

**Independent human meaning review [#50](https://github.com/Dojo-1/tenth-discriminant/issues/50), external source comparison [#51](https://github.com/Dojo-1/tenth-discriminant/issues/51), and the Phase204 parent draft must remain distinct gates.** No merge or field cutoff promotion follows from finite experiments.
