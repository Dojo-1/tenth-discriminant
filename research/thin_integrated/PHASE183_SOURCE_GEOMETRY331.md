# Phase183 — the source-ellipse geometry at fourth root 331

*3 November 2026. Focused Lean source-geometry candidate; not a discriminant theorem.*

The numerical scalar preflight merged through [PR #105](https://github.com/Dojo-1/tenth-discriminant/pull/105) is not enough. The next load-bearing interface is the source-exact interpolation geometry at the **same original ordinary-Z-jet support** and its unchanged two-channel trace metric.

Fix $D\ge331^4$, the original dimensions $R=\lfloor D/4\rfloor$, $S=\lfloor R/25\rfloor$, padded radius $\rho=\lceil(13/25)D^{3/4}\rceil$, thin radius $r=\lceil(11/25)D^{3/4}\rceil$, and original $\mathrm{ellipsePairs}(D,r)$. No alternative support or jet derivatives are introduced.

The [standalone Lean candidate](Phase183SourceGeometry331.lean) targets **only** these inherited source-geometric statements:

1. $D^{1/4}\ge331$.
2. $R\ge80D^{3/4}$, using $4R\ge D-3$. The former $90D^{3/4}$ condition is false at the new floor and is *not* imported.
3. $\rho\le(521/1000)D^{3/4}$, hence $\rho/R\le521/80000$; the thin/padded radius inequality $r\le(8/9)\rho$ remains.
4. The exact original interpolation-cardinality sufficient criterion under the same $2R+S\le0.51D$ row/channel guard and the existing $\pi>3.14$ inequality. We use a conservative $407/1000$ square-root coefficient and verify that
   \[
   \left(\frac{11}{25}-\frac{1001}{1000}\frac{407}{1000}\right)331-10
   =\frac{788283}{1000000}>0.
   \]
   This coefficient is stronger than the older 412/1000 but does **not** modify the support.

**Promote to P only after** pinned Lean compilation, source-definition correspondence and axiom/proof checks. These statements remain **H (submitted proof targets)** while the focused CI is outstanding. Once green, they establish only a source-geometric input. They do *not* establish positive definiteness of the same actual trace Gram, an odd-prime plus binary lower bound, the normalized source upper, or a class-number-one field cutoff. The exact 331 scalar gap is separately checked by PR #105.

**Kill conditions:** any replacement of the original $Q_D,R,S,r,\rho$, an old $90D^{3/4}$ assumption smuggled into a new proof, an unproved interpolation premise, a Lean failure, or reliance on a new axiom. The next connected theorem must re-establish the **same-Gram** upper and lower across the entire new domain. Independent semantic reconstruction remains [Issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50).