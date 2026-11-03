# Phase 183 — the 331⁴ guard certificate, before a new field theorem

*3 November 2026 · exact rational preflight; not a discriminant bound.*

The natural temptation is to clone nine Lean modules and replace every 375 by 331. We instead separate the **admissible numerical guards** from the **same-source determinant and maximal-order bridges**. The unchanged object is the integer ordinary-$Z$-jet trace Gram $G_D$ on the original thin observation support $Q_D$; $W$ is held fixed during differentiation, and the trace weights remain $2,2D$.

The target $331^4=12{,}003{,}612{,}721$ is conditional until the original determinant inequalities and the actual-field transport are re-established for this domain.

## A four-component guard certificate

The original dimensions and thin ellipse are

```math
R=\lfloor D/4\rfloor,\qquad S=\lfloor R/25\rfloor,\qquad
Q_D=\{(x,y)\in\mathbb Z^2:x^2+Dy^2\le\rho_{\rm thin}^2\},\qquad
\rho_{\rm thin}=\left\lceil\frac{11}{25}D^{3/4}\right\rceil.
```

**1. The geometric count.** The unchanged $2R+S\le 0.51D$ envelope and the existing $\pi>3.14$ certificate permit the tighter square-root coefficient $0.407$:

```math
\frac{51}{100}<
\frac{314}{100}\left(\frac{407}{1000}\right)^2,\qquad
\left(\frac{11}{25}-\frac{1001}{1000}\frac{407}{1000}\right)331-10
=0.788283>0.
```

The old coefficient $0.413$ *fails* that second sufficient inequality at root 331. The new coefficient concerns the existing cell-area proof, not a new support or a changed Gram.

**2. Integral rounding and radius transport.** Set $t=D^{1/4}$. The exact source definition $R=\lfloor D/4\rfloor$ gives $4R\ge t^4-3$. The sufficient inequality $R\ge80t^3$ follows for $t\ge331$ from $(t-320)t^3\ge3$. The older stronger $R\ge90t^3$ is unavailable at 331. The unchanged padded-radius ceiling $\rho_{\rm padded}\le(521/1000)t^3$ then yields

```math
\frac{\rho_{\rm padded}}{R}\le\frac{521}{80000},\qquad
\frac{521}{80000}+\frac1{9000}<\frac1{100}.
```

The second summand is the old $\log D/R$ error bound. It **still needs a new uniform Lean proof on the 331 domain**. The displayed rational inequality alone is not a determinant estimate.

**3. Sound logarithmic floor.** The same five-term odd-logarithm series, with its proven remainder, gives the proposed exact checker input

```math
\frac{5802}{1000}\le\log331\le\frac{5803}{1000}
\quad\Longrightarrow\quad\log D\ge23.208\quad(D\ge331^4).
```

**4. The strict gap without an artificial bonus.** The unchanged odd-plus-binary lower determinant bound minus the original normalized Hadamard upper has scalar difference

```math
\Delta(u)=\left(\frac{999997}{1000000}-\frac45\right)u
-\frac{5739}{1000}+\frac{1849}{2000}+\frac{\log2}{4},
\qquad u=\log D.
```

Using the certified lower $\log2\ge0.6931$, the gap at the conservative floor $u=23.208$ is **$0.000305376>0$**. This does not prove that either underlying determinant inequality holds at 331; it proves only that *if both do hold for the same original Gram*, their coexistence would be impossible.

The optional $+0.098$ strengthened separation used at the 377 and 375 anchors is **false** at 331 and must not be transported. The proof needs only $\Delta(u)>0$.

## Counterworlds

The [exact-rational preflight](phase183_331_preflight.py) uses Python fractions, the sound odd-log series bounds, and no floating-point acceptance criteria. Its negative controls explicitly reject the old $0.413$ cell coefficient and $90t^3$ rounding guard at 331, reject the extra $+0.098$ separation, and find that the *unstrengthened* gap already goes negative at $330^4$ under the same certified scalar envelopes. Consequently, 331 is a **candidate limit of this particular scalar comparison**, not a mathematical optimality statement.

## Formal obligation and promotion gate

The next Lean work should package these conditions into a reusable guard interface rather than replicate the nine-file 375 tower. Dependencies are: source-exact interpolation count, original Gram positivity, original odd-prime plus **once-counted** binary lower, same Gram normalized analytic upper, strict unstrengthened scalar gap, and the maximal-order actual-field return. The Phase181 Smith residuals are not silently added as a new uniform divisor.

Evidence labels: these exact rational calculations are **M** until reproduced in a formally connected guard lemma; the 331 actual-field endpoint remains **H**. Neither CI success for this preflight nor a Lean scalar theorem would constitute the final field-discriminant proof. The external semantic review of the larger project remains a separate gate.
