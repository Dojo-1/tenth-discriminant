# Phase156 — Transport-relative Archimedean jets and the same integer determinant

**1 November 2026 · single canonical branch main · source commit is recorded by GitHub.** This round considers the supplied *Transport-Relative Archimedean Principle* as a proposed semantic lens. It becomes mathematically operative only when a transport specifies its domain, positive cone, determinant action, prime-local remainder and uniformity requirement. [P-paper] the elementary transport/Cauchy–Binet identities below; [M] exact finite determinants and scalar probes; [H] the uniform 6-billion field cutoff; [R] any inference of a new theorem from a coordinate transformation alone.

## What exactly is transported?

For the **unchanged original** ordinary partial-Z jets of Z^r W^s, holding W fixed, let E be the integral matrix of paired real/imaginary observations, with m=RS rows and original diagonal positive integer trace weights B=(2,2D,2,2D,...). Write G=E B E^T. The field argument compares **this same positive integer** d=det G from two places: odd-prime divisibility below and a real geometric Hadamard upper.

An admissible **row gauge** U∈GL_m(Z) gives G' = U G U^T, det G'=det G, and identical prime valuations. On the PSD cone, T_U:X↦U X U^T is an order isomorphism, but not generally an isometry in a fixed Euclidean basis. A rational row gauge T∈GL_m(Q) changes logdet by 2log|det T|, while every finite prime q changes its determinant valuation by 2v_q(det T). The rational product formula makes these shifts the **same transport budget**, not two independent improvements.

A sample-change Q→Q' is **not** a zero-remainder transport merely because its column images agree. If Q is conjugation-stable, selecting y≥0 representatives and multiplying each nonreal orbit's trace weights by two reconstructs G exactly. Omitting those multiplicities changes G. We transport the integer and the metric together, or we explicitly record the lost information.

**Matched cone-order negative control:** for U_k=[[1,k],[0,1]], G_k=U_k U_k^T has det=1 for all k; comparing G_k to the *fixed-coordinate* order unit I requires multiplier at least 1+k². When that order unit is transported correctly to U_k I U_k^T=G_k, the multiplier is exactly 1. This is a counterexample to an unqualified *uniform fixed-frame* Archimedean claim, not evidence of intrinsic noncompact holonomy or a field obstruction.

The proposed 'Archimedean ecology' from the attached note is therefore realized here by the **integral lattice, real PSD cone, and prime-local determinant line** with explicitly declared transports. Arbitrary p-adic and real magnitudes are NOT assumed to share a native total order; their common comparable real value arises only through logarithms of integer determinant divisibility.

## Jet factorial capacity — exact source-preserving divisibility [P-paper]

Let c range over effective nonzero original scalar jet channels, with ordinary derivative order j(c) and integer trace weight b_c>0. The Phase155 integer identity shows E_ord=H diag(j(c)!), where H has the integer Taylor/Hasse coefficients. This identity does not change the production Gram. For prime q and m=RS, define
\[
\beta_q(Q;B)=\min_{\substack{I\text{ effective columns}\\ |I|=m}}
\sum_{c\in I}\bigl(2v_q(j(c)!)+v_q(b_c)\bigr).
\]
Cauchy–Binet, with **the same B**, yields
\[
\det G=\sum_{|I|=m}(\det H_I)^2\prod_{c\in I}(j(c)!)^2 b_c.
\]
Every summand is divisible by q^{β_q}, so **q^{β_q}|det G**. This holds also for *oversampled rectangular E*; for insufficient capacity, d=0 and positivity must be proved elsewhere. Restricting to actually nonzero minors could sharpen β but needs a separate rank/matroid witness. Do not confuse the safe capacity lower bound with exact valuation.

For D odd, every nonzero original trace weight has v_2≥1; for Q consisting of y≥0 orbit representatives, the number N of effective channels at each derivative order is precisely the number of points of the full conjugate-symmetric disk Ω_D(ρ). Set m=RS and
\[
t_2=\min_{\sum m_j=m,\ 0\le m_j\le N}\ \sum_{j=0}^{S-1}m_j v_2(j!),\quad
\beta_2\ge m+2t_2.
\]
This is a distinct **2-primary** contribution. Since the inherited exactOddPrimeMass contains only **odd** prime divisors, the coprime product certifies, under all its existing number-field guards,
\[
\boxed{\log d\ge \mathrm{exactOddPrimeMass}(R,S)+\beta_2\log2.}
\]
At odd q, the factorial divisor may overlap the inherited Frobenius factor and must not simply be added. A joint Smith/Fitting filtration would be needed to claim extra odd-prime mass.

## Exact finite cross-representation controls [M]

For original D=19,R=8,S=J=4,ρ=5, the 21-point complete Gram has **identical integer entries** to the conjugation-folded 16-node Gram with weights doubled for nonreal orbits. Source-matched arbitrary-precision results:

| Representation | Safe 2-valuation β_2 | Actual v_2(det G) |
| --- | ---: | ---: |
| Six-point Phase144 support | 56 | 166 |
| Original complete 21-point raw channels | 32 | 172 |
| **The identical complete Gram** as weighted 16-orbit descent | 42 | 172 |

The fold reveals a better divisibility *certificate*, not a new factor of the determinant. In the independent D163,R30,S5 square-channel controls, the 15 nonreal-point support gives β_2=450, β_3=120, β_163=75; the 16-point support gives β_2=410. These are **lower bounds**, not actual 150×150 determinant valuations.

## Uniform Nagura-only 6-billion candidate [H, paper proof obligations outstanding]

Under hypothetical squarefree D≡3 (mod4), D≥6×10^9, h(-D)=1, Nagura's classical prime interval supplies an inert prime 5(D+1)/24<p<(D+1)/4. Put R=p−1, S=J=floor(R/25), δ=√(D+1)/2, A=√(p√D/3), ρ=ceil(δ+A), and Q={(x,y):x²+Dy²≤ρ²,y≥0}. The established Phase152 Frobenius rank argument is a **paper-level** positivity bridge for this same original matrix, not yet compiled Lean.

The rectangular lattice has covering radius δ and covolume √D. Its Voronoi-cell upper count, together with π<22/7 and D^{1/4}>278, would give
\[
N=|\Omega_D(\rho)|\le \frac{\pi(\rho+\delta)^2}{\sqrt D}
<\frac{27}{25}p<\frac{11}{10}R.
\]
The load-bearing exact rational checks are
\[
\frac{22}{21}(1+\tfrac{19}{5\cdot278}+\tfrac4{278^3})^2<\frac{27}{25},
\qquad \frac{\delta+1}{A}<\frac1{140}.
\]

For m selected channels of capacity at most N per order, greedy rearrangement yields Σ_j j m_j≥m²/(2N)−m/2. Four floors of Legendre's formula show v_2(j!)≥15j/16−4. Therefore
\[
\beta_2\ge\frac{15}{16}\frac{m^2}{N}-\frac{127}{16}m,
\qquad
\frac{\beta_2\log2}{R^2S}
\ge(\tfrac3{88}-\tfrac9R)\log2>0.0235.
\]
The existing **same-source** odd-prime normalized lower remains L/(R²S)≥log R−4.411. The analytic upper must be re-established uniformly with the weaker 1/140 radius ceiling; the proposed relaxed source estimate is U/(R²S)≤0.24log D+0.56log R−0.594. **Only if those quantified steps and the exact original-Gram bridges are proved**, the resulting contradiction margin obeys
\[
\frac{L+\beta_2\log2-U}{R^2S}
\ge0.44\log R-0.24\log D-3.817+0.0235>0.015699.
\]
This proposes exclusion for odd fundamental D≥6 billion, not an established field theorem; the actual-field/even chart and external mathematical reconstruction remain separate.

**Finite probes** at the weak Nagura ratio (p chosen as an *analytic parameter*, not asserted prime): D5b gives old gap ≈−0.0335010, 2-primary ≥0.0256721, combined ≈−0.0078289; D6b gives +0.00328674,+0.02567210, combined +0.02895884. Exact rational gates test constants but do **not** prove the universal analytic inequalities. If independent checking breaks any geometric count, prime interval, normalizing factor, or odd/2-primary coprimality, retire the 6b claim without changing the original Lean 47b cutoff.

## Next proof, rather than another ontology

Formalize this exact Cauchy–Binet **2-adic divisibility** on the existing ordinary-jet Gram; prove the Chinese-remainder combination with the inherited odd-prime product; formalize the Frobenius graph-to-PosDef map and the uniform lattice-area and normalized estimates. At the original integer level, the new unimodular determinant transport theorem is a small Lean objective. The attached Transport-Relative Archimedean principle should supply admissibility and uniformity tests, **not an extra assumption that predetermines the field result**.

Evidence: [P-paper] algebraic identities; [M] bounded exact integer determinant and rational tests; [H] 6b conditional numerical cutoff; [S] transport-relative Archimedean/Worldlet terminology; [R] fixed-reference nonuniformity mistaken for invariant holonomy or fractional-factorial 'free gain'. The originality of the underlying Cauchy–Binet, valuation and order-cone facts is not claimed.
