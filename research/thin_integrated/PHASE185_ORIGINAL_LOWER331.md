# Phase185 — original odd-prime lower at fourth-root 331

*3 November 2026 · focused Lean candidate; no field-discriminant theorem.*

The lower bound is often mistaken for a new source object when the threshold drops. Here the source object is fixed: the original integer ordinary-$Z$-jet trace Gram on the exact original thin ellipse, with $W$ held constant during differentiation and original trace weights $2,2D$.

## Which threshold is actually needed?

The existing source lower-envelope theorem supplies, for the original dimensions $R=\lfloor D/4\rfloor$ and $S=\lfloor R/25\rfloor$, a normalized odd-prime lower provided the necessary dimension/aspect guards and $2\le\log R$ hold. The previously used $\log D\ge23.7$ was an overly strong *convenience* premise for this last condition, not a new arithmetic obstruction.

The merged Phase183 [scalar preflight PR #105](https://github.com/Dojo-1/tenth-discriminant/pull/105) supplies the sound bound $\log D\ge23.208$ whenever $D\ge331^4$. The unchanged floor estimate $\log R\ge\log D-1.4$ gives $\log R\ge21.808$, well above $2$.

## Same integer Gram, same divisors

The importable [Scalar331.lean](../../lean/TenthDiscriminant/Scalar331.lean) is a byte-for-byte copy of the previously compiled Phase183 standalone source, guarded by CI. The [Lower331.lean](../../lean/TenthDiscriminant/Lower331.lean) reuses the original odd-prime mass and comparison scale, with the old dimension guards reproved on the 331 domain.

Its stated target includes the old recovered lower:

~~~math
\frac{999997}{1000000}\log D-\frac{5739}{1000}
\le \frac{\mathrm{recoveredPrimeMassLower}(R,S)}{R^2S}.
~~~

When the original Gram's determinant is strictly positive and the existing squarefree and class-number-one hypotheses hold, the old sound integral source bridge compares this recovered mass with the *same original determinant*. The binary factor enters through the previously checked bridge; its contribution is **not** counted again as an invented auxiliary inert prime.

The lower alone gives no field bound. The original normalized analytic upper must be reproved for the **same** thin Gram at $D\ge331^4$, and the strict scalar overlap theorem must then connect to the actual field-discriminant return. Phase184 [positivity PR #108](https://github.com/Dojo-1/tenth-discriminant/pull/108) is being verified independently.

## Evidence and kill conditions

- **P (already imported):** the old source-level recovered mass inequalities and sound five-term log remainder checker, subject to their exact Lean declarations and axioms.
- **H (new):** lower-envelope module until focused exact-head Lean compilation and source check succeed.
- **R:** the statement that the 23.7 logarithmic floor was intrinsically necessary for this particular odd-prime lower.
- **Stop:** no 331 field bound or intrinsic hardness theorem; no new prime factors, jet conventions, weighted metric, or normalized surrogate.

Kill on any source mismatch, Lean elaboration or axiom failure, broken squarefree/class-number transport, or inability to link the final lower to the **same** positive Gram as the analytic upper. External [semantic reconstruction #50](https://github.com/Dojo-1/tenth-discriminant/issues/50) remains open.