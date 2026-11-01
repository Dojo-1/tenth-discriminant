# Phase157 — Archimedean area tightening for the SAME original ordinary jets

**1 November 2026 · canonical branch main.** Evidence: [P] the pre-existing original-jet valuation and analytic APIs, and Mathlib's explicit pi bounds (subject to exact-head source verification of the newly imported lemma); [P-paper candidate] the radius/count/capacity inequalities derived below; [M] exact-rational guards and sampled source-normalized margins; [H] a **Nagura-only 5-billion field exclusion**. No strengthened field result is declared, and the checked 47-billion theorem remains canonical.

This phase arose from applying the proposed **Transport-Relative Archimedean Principle** to our original determinant: the *same* positive integer Gram must be comparable through finitely many admissible places with **uniform**, explicitly accounted transport. The improvement here does NOT come from an abstract hyperring or an extra frame. It comes from sharpening the classical **Archimedean disk-area constant** that determines the geometric observation support itself.

## Freeze the object before changing the radius

Retain:
- The original integer-pair lattice \(\mathbb Z+\mathbb Z\sqrt{-D}\), ordinary partial-\(Z\) jets of \(Z^rW^s\) with \(W\) **held fixed**, row index \(0\le r<R,0\le s<S\), derivative order \(0\le j<S=J\), and trace weights \(2,2D\).
- The **same unweighted** positive integer Gram \(G_Q=\mathrm{integerRectangularTraceGram}(Q,D,S,R,S)\) in both lower and upper, NOT a weighted orbit reconstruction or a divided-power normalized matrix.
- Under hypothetical odd squarefree \(D\equiv3\pmod4\), \(D\ge5,000,000,000\) and class number one, Nagura's external classical theorem supplies a prime \(5(D+1)/24<p<(D+1)/4\). The existing class-number-one inert bridge makes it inert. Set \(R=p-1,\ S=\lfloor R/25\rfloor\).
- \(Q\) consists of the **single** representative \(y\ge0\) for each conjugate orbit in the ellipse.

**Change only one geometric choice:** the old coefficient 3 becomes the exact rational
\[
c=\frac{157}{50}=3.14,\quad
\delta=\frac{\sqrt{D+1}}2,\quad
A=\sqrt{\frac{p\sqrt D}{c}},\quad
\boxed{\rho_\pi=\lceil\delta+A\rceil}.
\]
Mathlib's \`Real.pi_gt_d2\` and \`Real.pi_lt_d2\` give **\(c<\pi<63/20=3.15\)**. The [new Lean pi-window artifact](../../lean/TenthDiscriminant/ArchimedeanPiWindow.lean) imports these genuine pre-existing proofs. This is a meaningfully stronger geometric constant than the earlier elementary \(\pi>3\), not an approximate substitution.

## Exactly why Frobenius rank survives

Let \(\Omega=\{(x,y)\in\mathbb Z^2:x^2+Dy^2\le\rho_\pi^2\}\), full conjugate-stable support. Rectangular lattice covolume \(=\sqrt D\), covering radius \(\delta\); the Voronoi-cell comparison gives
\[
|\Omega|\sqrt D\ge\pi(\rho_\pi-\delta)^2
\ge\pi A^2=\frac{\pi}{c}\,p\sqrt D>p\sqrt D.
\]
Thus \(N:=|\Omega|>p\). For \(t=D^{1/4}>265,\ p>5(D+1)/24\), the explicit rational bounds
\[
\frac{2\delta}{A}<\frac{39}{10t},\qquad
\frac1A<\frac4{t^3},\qquad
e:=\frac{\delta+1}{A}<\frac{39}{20t}+\frac4{t^3}
\]
hold because \((39/10)^2>24c/5\). Using the **upper** \(\pi<63/20\) and the opposite Voronoi containment,
\[
\frac{N}{p}\le\frac{\pi}{c}
  \left(1+\frac{2\delta+1}{A}\right)^2
<\frac{(63/20)}{c}\left(1+\frac{39}{10\cdot265}+\frac4{265^3}\right)^2
<\frac{26}{25}.
\]
Since \(R=p-1>10^9\), this gives \(N<(21/20)R\). Also \(A/p<5/(4t)\) and
\[
\frac{\rho_\pi}{R}<
\frac5{4\cdot265}(1+e)(1+10^{-9})<\frac1{200},
\]
hence \(2\rho_\pi<p\). Distinct lattice nodes and their conjugates therefore remain distinct in the inert residue field \(F_{p^2}\) modulo \(p\). On the Frobenius graph \(W=Z^p\), original ordinary jets \(j<S<p\) pull back faithfully to length-\(S\) directional jets, and the noncolliding monomials \(Z^rW^s\mapsto T^{r+ps}\) have maximum degree \(pS-2\). The \(SN>pS-2\) vanishing constraints force full row rank of **the same original** integer evaluation matrix modulo \(p\), hence the positive original integer Gram. **This rank-plus-geometry theorem is a [P-paper] reconstruction and has NOT been compiled as a universal Lean proof.**

For every derivative order, the effective scalar channel count in unweighted \(Q\) is exactly \(N\): real-axis nodes contribute one channel; nonreal representatives contribute two. No orbital weight factor is inserted here.

## The prime-2 divisor becomes sharper when the disk shrinks

Write \(m=RS\). The exact original ordinary-vs-Taylor identity, plus Cauchy–Binet with diagonal trace weights \(2,2D\), gives
\[
2^{\beta_2(Q)}\mid \det G_Q,\qquad
\beta_2\ge \frac{15}{16}\frac{m^2}{N}-\frac{127}{16}m.
\]
The capacity rearrangement chooses the lowest derivative orders first; \(v_2(j!)\ge(15/16)j-4\) follows from the first four Legendre floors. Our *new* \(N<(21/20)R\), \(S\ge R/25-1\), and \(R>10^9\) yield
\[
\frac{\beta_2\log2}{R^2 S}
\ge \left(\frac1{28}-\frac9R\right)\log2
>0.0245,
\]
using \(\log2>0.69\). This q=2 factor is **coprime** to every inherited factor in \(\mathrm{exactOddPrimeMass}(R,S)\), so they may be multiplied rather than double-counted; the analogous addition at odd q is *not* licensed.

## A conservative same-Gram analytic upper [P-paper proof target]

The original source expression [\`enderUpperB\`](../../lean/TenthDiscriminant/EnderUpperB.lean) with \(n=4D,\ J=S\) has the precise normalized form
\[
\frac{U}{R^2S}=
\frac{\log(2nS)}R+
(1-S/R)\log\rho+
\frac{2(S-1)}R(\log R-1)+
\frac{2(S-1)}{R^2}\left(\rho+\log(R/\rho)\right).
\]
No new derivative norm or column metric is substituted.

For \(t>265\),
\[
e<e_0:=\frac{39}{20\cdot265}+\frac4{265^3}<0.00736,
\]
and \(p=R+1\), so
\[
\log\rho_\pi\le \tfrac14\log D+\tfrac12\log R
-\tfrac12\log c+e_0+\tfrac1{2R}.
\]
Since \(S/R\le1/25\) and \(S/R\ge1/25-1/R\), the leading log terms become \(0.24\log D+0.56\log R\). The remaining positive terms satisfy
\[
\frac{\log(2nS)}R < \frac1{50{,}000},\quad
\frac{\log R}R<\frac1{30{,}000},\quad
\frac\rho R<\frac1{200}.
\]
Here \(R>D/5,\ S\le R/25,\ 2nS\le D^2/10\) and \(\log x\le6x^{1/6}\) give the first bound; \(\log R\le\sqrt R\) gives the second. The floor correction in \((1-S/R)\) and the derivative endpoint consume altogether **less than 0.0005** in normalized units.

The remaining constant is bounded *exactly* by
\[
-\frac{12}{25}\log c-\frac2{25}+
\frac{24}{25}e_0+0.0005 < -0.62.
\]
To avoid treating the decimal logarithm as numerical oracle, put \(u=107/207=(c-1)/(c+1)\). The standard positive \(\operatorname{artanh}\)-series gives
\[
\log c=2\sum_{k\ge0}\frac{u^{2k+1}}{2k+1}
\quad\Longrightarrow\quad
\log c>
2\sum_{k=0}^{4}\frac{u^{2k+1}}{2k+1}>\frac{143}{125}=1.144.
\]
All five terms and the final strict comparison are rational. The [exact verifier](phase157_pi_tight_radius.py) tests these rational constants, but the universal logarithmic manipulations remain a separate human/Lean proof obligation.

Therefore the paper candidate has
\[
\boxed{\frac{U}{R^2S}<0.24\log D+0.56\log R-0.62.}
\]

## Combining original arithmetic, geometry and admissible transport

The existing [Phase153 source-certified-formula lower](PHASE153_BERTRAND_CANDIDATE.md) remains
\[
\frac{L_{\mathrm{odd}}}{R^2S}\ge\log R-4.411
\]
in this regime. Together with the **same original integer** \(G_Q\), the coprime 2-primary divisor and the new upper envelope give
\[
\frac{L_{\mathrm{odd}}+\beta_2\log2-U}{R^2S}
>0.44\log R-0.24\log D-3.791+0.0245.
\]
Nagura's \(p>5(D+1)/24\) gives \(\log R>\log D-\log(24/5)-10^{-6}\). Using \(\log D>22.3,\ \log(24/5)<1.57\), the strict right side is
\[
>0.2(22.3)-0.44(1.57)-3.791+0.0245-10^{-6}
=\boxed{0.002699}.
\]
Under all remaining original number-field guards and *if* the general Frobenius-positivity, q2 divisor and uniform analytic steps are reconstructed, this would yield a **Nagura-only D≥5-billion odd-field contradiction** without Costa Pereira, triangular/Hasse substitution or a new class-number axiom.

This remains **[H]** as a field theorem: no unconditional or Lean-certified 5-billion cutoff has been established. The inherited checked 47-billion result stays unchanged.

## Discriminating controls and scope of evidence

The [finite verifier](phase157_pi_tight_radius.py) independently evaluates the **same Phase153 literal normalized L/U formulas** with both c=3 and c=157/50, the conservative pi<3.15 capacity and exact prime-2 Legendre floor algorithm. It checks rational pi/area/radius/gap constants, weak Nagura-ratio endpoints, stronger prime ratios, and a true prime *parameter* (without asserting its associated field has class number one). At the weak analytic ratio, \(D=5{,}000{,}000{,}003\), the old c=3 budget is negative while the new c=3.14 budget is positive; \(D=4.5\) billion remains a negative control at k=25.

**Source-level formal target:** besides the new pi-window Lean lemma and its rational gates, formalize lattice-cell covering, count of effective original channels, the q=2 Cauchy–Binet divisor, the inert Frobenius ordinary-jet rank implication, the uniform L/U logarithmic estimates, and final actual-field/even-branch transport. Stronger than a finite CI check is independent human reconstruction of every hypothesis and step.

The historical Archimedean bound on \(\pi\) and Mathlib's refined \(3.14<\pi<3.15\) are established classical results, not new theorems. The genuinely investigable claim is whether this *specific same-Gram* coupling closes the original discriminant argument. No originality of the fundamental ingredients is claimed.
