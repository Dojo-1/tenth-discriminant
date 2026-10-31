# Phase143 — close the *same thin-Gram* discriminant diagram

**31 October 2026. Integration attempt, not an accepted new field bound until exact-head Lean/axiom/source/negative-control checks pass.** This phase deliberately adds no new sample geometry or prime. It composes the checked Phase140 and Phase141 statements with the pre-existing arbitrary-\(Q\) arithmetic lower bound. The original strict 47-billion actual-field theorem is left unchanged.

The central requirement is that **both inequalities compare the determinant of the same new integer**:

\[
\begin{array}{ccccc}
Q_\mathrm{thin}=\operatorname{ellipsePairs}(D,\rho_\mathrm{thin}) &
\overset{\text{ordinary jets}}{\longrightarrow}&
E_{Q_\mathrm{thin}}\in\mathbf Z^{RS\times 2J|Q_\mathrm{thin}|}&
\overset{B>0}{\longmapsto}&
G_\mathrm{thin}=E_{Q_\mathrm{thin}}B E_{Q_\mathrm{thin}}^{\mathsf T}\in M_{RS}(\mathbf Z),\\
 & \swarrow \text{arithmetical class-number-one prime factors} &&
 \searrow\text{real high-derivative analytic upper}&\\[-2pt]
\text{recovered mass}\;\le\log\det G_\mathrm{thin}& &
&&\log\det G_\mathrm{thin}\le\text{upper}_B(\rho_\mathrm{thin},N_\mathrm{old})-\text{jet gain}.
\end{array}
\]

The old larger ellipse is used **only** to provide a valid common cardinality majorant \(N_\mathrm{old}\) and an already-certified analytic upper *expression*, not as an equality of the two Gram determinants. This is the exact semantic interface missing from earlier radius-only conjectures.

## Four bridges and their evidence

1. **Geometry [P in main].** [Phase140 ThinEllipseCount](../../lean/TenthDiscriminant/ThinEllipseCount.lean) proves for all integers \(D\ge450^4=41,006,250,000\), with the original tuned row dimensions, that \(2(R-1)+(S-1)<|Q_\mathrm{thin}|\), with \(\rho_\mathrm{thin}=\lceil(11/25)D^{3/4}\rceil\). This is a sufficient interpolation guard for the **same** original ordinary-jet trace Gram; it is not a converse. The original radius used coefficient \(13/25\).

2. **Analytic radius comparison [P in main].** [Phase141 ThinRadiusAnalyticGain](../../lean/TenthDiscriminant/ThinRadiusAnalyticGain.lean) proves \(\rho_\mathrm{thin}\le8\rho_\mathrm{old}/9\) and
\[
 \frac{\operatorname{upper}_B(R,S,S,\rho_\mathrm{thin},N)
  -\operatorname{upper}_B(R,S,S,\rho_\mathrm{old},N)}{R^2S}
 \le-1/10
\]
with the **same valid** \(N\) and production guards. The existing [tight ordinary-jet majorant](../../lean/TenthDiscriminant/TightRadialSaving.lean) supplies the \(-23/2000\) diagonal saving for any eligible \(Q\). The old certified padded upper expression is bounded by \((4/5)\log D-813/1000\). Together, if the thin \(Q\) majorant is correctly instantiated, these yield
\[
\frac{\log\det G_\mathrm{thin}}{R^2S}
\le\frac45\log D-\frac{1849}{2000}.
\tag{U}
\]

3. **Arithmetic [P pre-existing generic theorem; new application being compiled].** [RadialCutoff.prime_mass_log_lower](../../lean/TenthDiscriminant/RadialCutoff.lean) is quantified over *arbitrary finite* integer \(Q\) satisfying the original interpolation count, under the exact squarefree, mod-4, inert-prime and class-number-one assumptions. The previously certified recovered prime mass therefore bounds \(\log\det G_\mathrm{thin}\) **directly**, with no deduction from divisibility of \(\det G_\mathrm{old}\). The normalized recovered lower is
\[
\frac{\log\det G_\mathrm{thin}}{R^2S}
\ge\frac{999997}{1000000}\log D-\frac{5739}{1000}.
\tag{L}
\]

4. **Actual field / strict numerical endpoint [H until compiled].** The existing maximal-order and totally complex degree-two representation theorems carry contradictions from (U) and (L) to the true field discriminant \(\operatorname{disc}(K)\), rather than the sample Gram. At the geometric floor \(\log D\ge 241/10\), the lower-minus-upper margin exceeds \(1/500\). The new [ThinIntegratedEndpoint.lean](../../lean/TenthDiscriminant/ThinIntegratedEndpoint.lean) attempts to formally prove
\[
\boxed{\left|\operatorname{disc}(K)\right|<41\,006\,250\,000}
\quad
\left(
[K:\mathbf Q]=2,\;K\text{ totally complex},\; h_K=1
\right).
\]
This remains a **proposed Lean result** until exact-head compilation, axioms and source-level semantic correspondence have been inspected. It is not presented as a record in algebraic number theory: imaginary quadratic class-number-one fields are already classically classified much more strongly, and Tao's challenge is about exploring proof methods and transparent computational certification.

The proof strategy contains no new auxiliary inert or split primes and no hidden replacement of ordinary derivatives with Hasse jets. The normalization scale \(R^2S\) and comparison are kept identical across (U) and (L).

## The lower-dimensional / higher-order consequences, properly scoped

The [Phase142 leverage programme](../ellipsoid_trimming/PHASE142_LEVERAGE_AND_UNISOLVENCE.md) is a separate, useful *geometry-selection* frontier. A small finite \(D=19,R=8,S=J=4\) model admits full-rank original ordinary jets using eight real-axis nodes or only four nonreal nodes; the latter achieves the elementary channel-count minimum but has a **larger** Gram determinant. Classical determinant-lemma leverage and a paper-level Fourier-root real-axis unisolvence argument explain the finite rank transitions. No lower support-cardinality theorem for the uniform production ellipse follows, and no higher-order construct is needed in Phase143's proof closure. This prevents rank efficiency, Archimedean volume efficiency and \(p\)-local divisor efficiency from being conflated.

The geometrical language is deliberately austere: the nontrivial structure is the family of finite **integer observation lattices**, their ordinary-jet maps, a positive trace pairing and its top exterior volume. Their determinant is not the number-field discriminant. The proof must explicitly transport an obstruction from the former to the latter via class-number and field charts.

## Failure modes, controls, promotion

- **R_sem:** a compiled statement about \(\det G_\mathrm{thin}\) is not automatically about \(\operatorname{disc}(K)\). Require final theorem with quantified arbitrary field \(K\) and its actual \(\operatorname{discr}\).
- **R_transport:** \(\det G_\mathrm{old}\ne\det G_\mathrm{thin}\) in general. Never transfer its \(p\)-adic divisibility through Loewner monotonicity. Reapply the arbitrary-\(Q\) prime lemma at \(Q_\mathrm{thin}\).
- **R_formal:** if a Lean tactic, log-rational certificate, axiom audit or source equivalence fails, record the exact failing declaration and keep the PR draft. Do not replace it with a stronger-sounding paper claim.
- **R_emp:** the four-nonreal-point finite rank witness cannot prove a production \(D\to\infty\) improvement, nor establish computational hardness.

Accept only after: exact-head whole-root Lean, explicit theorem source, axiom/dependency controls, known-false negative controls, security checks, and an independently readable theorem statement. Issues [#50](https://github.com/Dojo-1/tenth-discriminant/issues/50) (human external reconstruction) and [#51](https://github.com/Dojo-1/tenth-discriminant/issues/51) (original same-E modular rank research) remain open even if the new field endpoint compiles. The classical absolute field bound is not claimed novel.
