# Phase163 — The binary lower bound and the 41,006,250,000 field target

*1 November 2026 · focused endpoint Lean CI pending at the time of this record. The previously checked actual-field cutoff is **47 billion**. All inequalities below concern the original integer ordinary-\(Z\)-jet trace Gram until the final explicitly typed number-field step.*

Our new arithmetic is worth something only if it meets the existing real upper estimate on **the same integer**, without moving the observation ellipse or replacing ordinary derivatives with Hasse jets. In fact, the production geometry already works for \(D\ge450^4=41{,}006{,}250{,}000\). The earlier odd-prime proof missed a binary factor that is now separately justified by the Phase162 source construction.

Let \(Q=\mathrm{ellipsePairs}(D,\mathrm{Tuned.rho}(D))\), \(R=\mathrm{Tuned.R}(D)\), \(S=\mathrm{Tuned.S}(D)\), and \(z=\det G_Q\). Its trace metric is the original diagonal \(2,2D\). The univariate monic row basis \(Z^{r-4k}(Z^4-Z^2)^kW^s\), \(k=\lfloor r/4\rfloor\), contributes

\[
2^{\Lambda(R,S)}\mid z,\qquad
\Lambda(R,S)=RS+2S\sum_{r<R}\lfloor r/4\rfloor.
\]

Under precisely the old class-number-one, squarefree and prime-window conditions, the existing odd-prime mass gives the **independent** coprime divisor \(P_{\mathrm{odd}}=\prod_{p<R,\ p\text{ odd prime}}p^{2F_{R,S}(p)}\). Therefore, if the original Gram is positive,

\[
\boxed{\mathrm{exactOddPrimeMass}(R,S)+\Lambda(R,S)\log2\ \le\ \log z.}
\]

This is implemented in the source-level [binary + odd-prime logarithm module](../../lean/TenthDiscriminant/BinaryMassLog.lean). No earlier factorial \(2\)-adic floor is added to \(\Lambda\); doing so would double-count the same prime.

For a deliberately conservative numerical normalization, the elementary inequality

\[
R^2\le8\sum_{r<R}\lfloor r/4\rfloor+7R
\]

implies, for \(R\ge15\),

\[
R^2S\le5\Lambda(R,S),\qquad
\frac{\Lambda(R,S)\log2}{R^2S}\ge\frac{\log2}{5}>\frac18.
\]

The source actually admits the sharper paper identity \(4\Lambda=S(R^2+t(4-t))\), \(t=R\bmod4\); the easier one-eighth bound is sufficient here and is the separate [Lean target](../../lean/TenthDiscriminant/BinaryNormalizedGain.lean).

The trusted, unchanged production analysis for \(D\ge41{,}006{,}250{,}000\) already proves

\[
\frac{\mathrm{recoveredPrimeMassLower}}{R^2S}
\ge\frac{999997}{10^6}\log D-\frac{5739}{1000},
\qquad
\frac{\log z}{R^2S}\le\frac45\log D-\frac{1649}{2000},
\]
and \(\log D\ge24\). Since recovered mass is bounded by the **same existing exact odd-prime mass**, adding the new binary certificate yields a strict contradiction. At the weakest permitted \(\log D=24\), the rational gap is

\[
\left(\frac{999997}{10^6}-\frac45\right)24
-\frac{5739}{1000}+\frac{1649}{2000}+\frac18
=\boxed{\frac{2607}{250000}=0.010428>0}.
\]

There is no new lattice-point count, no undocumented prime interval, no spin transport, and no assertion of a 5-billion theorem. The preexisting even chart and the exact field-discriminant equivalence give the expected **theorem target**

\[
\boxed{
h(K)=1,\ [K:\mathbb Q]=2,\ K\ \mathrm{totally\ complex}
\ \Longrightarrow\ |\mathrm{disc}(K)|<41{,}006{,}250{,}000.
}
\]

The source is [BinaryFortyOneBillion.lean](../../lean/TenthDiscriminant/BinaryFortyOneBillion.lean). It is **H / uncompiled candidate** until exact-head focused Lean and whole-root checks pass. Phase162's stronger four-generator exponent \(1358\) at \(D=163,R=30,S=5\) remains **P-paper/M finite**, not silently promoted into this field proof. The original 47-billion field theorem remains the accepted mainline result until these obligations close, and independent mathematical semantic reconstruction [#50](https://github.com/Dojo-1/tenth-discriminant/issues/50) is still pending.

The intended reading path is short: this page → [Phase162 source determinant construction](PHASE162_BINARY_NULL_LOWER.md) → the three named Lean files → exact-head GitHub Actions receipts. A missing proof or a failed CI run must be recorded, not replaced by a more permissive field statement.
