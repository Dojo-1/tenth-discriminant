# Phase187 — original thin-Gram analytic upper at fourth root 331

*3 November 2026 · Lean theorem target, separate from a field-discriminant bound.*

This stage is not a search for a more attractive Gram or a new observation lattice. It keeps the old $Q_D=\mathrm{ellipsePairs}(D,r)$, original integer ordinary-$Z$-jet matrix, $W$ fixed in differentiation, old trace weights $2,2D$, and exactly the original $R=\lfloor D/4\rfloor$ and $S=\lfloor R/25\rfloor$. The **padded** ellipse enters the bound *only* through the inherited cardinality majorant; its determinant is never substituted for the original thin determinant.

## Numerical question

At the new fourth-root floor 331, the already compiled original-source geometry yields

~~~math
\frac{\rho_{\mathrm{padded}}}{R}
\le\frac{521}{80000},
\qquad
\frac{521}{80000}+\frac1{9000}<\frac1{100}.
~~~

Although this loses the older stronger $521/90000$ envelope, the original normalized endpoint-error proof used only the *coarser* sum $1/100$. Thus the old additive error ceiling may still survive **without weakening the final normalized upper**.

The [rederived scalar file](../../lean/TenthDiscriminant/UpperScalars331.lean) uses the smaller 331-domain source and the Phase183 sound $\log D\ge23.208$ enclosure. Its intended unchanged scalar majorant remains

~~~math
\frac{\mathrm{enderUpperB}(R,S,S,\rho,n)}{R^2S}
\le\frac45\log D-\frac{813}{1000}.
~~~

The [same-source upper file](../../lean/TenthDiscriminant/ThinUpper331.lean) then invokes the existing geometric/Hadamard majorant with original thin $Q_D$, original node-radius and original trace metric, plus the unchanged radial saving. Its target is

~~~math
\frac{\log\det G_{\mathrm{thin}}(D)}{R^2S}
\le\frac45\log D-\frac{1849}{2000}.
~~~

These are **targets until focused Lean CI passes**, not consequences of the numerical check alone.

## Distinguish the certificates

- **P, imported:** Phase183 source count and ratio, Phase184 positivity, Phase185 lower-source dimensions, the existing same-Gram radial/Hadamard theorem and the accepted source definitions under their permitted axioms.
- **H, this branch:** reuse of the original upper-endpoint constants at $D\ge331^4$, with all range-specific scalar steps re-established.
- **H, next:** combine the Phase186 once-counted odd-plus-binary lower and this upper into the *same positive Gram* contradiction, then transport the actual class-number-one field conclusion. These latter steps are not performed in Phase187.
- **R:** equating the padded and thin Gram determinants, assuming the obsolete 90-cube radius bound at 331, or treating a smaller scalar threshold as an already proved field bound.

**Kill condition:** failure of any exact source geometry, change of original jet derivatives/metric/cardinality semantics, failed compilation, new axiom or silent import of a theorem that still assumes $D\ge375^4$. Proof acceptance is limited to what Lean actually checks; independent semantic reconstruction remains [Issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50). The latest accepted mainline field cutoff remains $375^4$.
