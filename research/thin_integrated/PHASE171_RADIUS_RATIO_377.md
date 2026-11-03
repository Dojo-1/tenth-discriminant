# Phase171 — preserve the original radius-over-R constant at 377^4

**A narrowly scoped Lean candidate, not a new discriminant bound.**

Keep the *original* radius $\rho(D)=\lceil (13/25)D^{3/4}\rceil$,
dimension $R(D)=\lfloor D/4\rfloor$ and thin radius
$\rho_{\rm thin}(D)=\lceil (11/25)D^{3/4}\rceil$.

Let $t=D^{1/4}\ge377$. Euclidean division gives the exact
$4R\ge t^4-3$. Because $t^3(t-360)\ge17t^3\ge3$, we obtain
$4R\ge360t^3$, equivalently $R\ge90t^3$.
The integer-ceiling remainder is less than 1, so
$\rho <(13/25)t^3+1\le(521/1000)t^3$.
Combining yields the **existing exact constant**
```math
\frac{\rho}{R}\le\frac{521}{90000}.
```

The separate ratio $\rho_{\rm thin}\le(8/9)\rho$ also survives using
the unchanged 11/25 and 13/25 radius definitions.

These are analytic-radius input guards only. The old production
determinant upper, normalized prime-mass lower and full field theorem
remain proved on $D\ge450^4$ and cannot be transported by this result.
The original trace Gram and ordinary derivatives are unchanged.

**Verification:** pinned Lean 4.19.0+Mathlib exact-head focused build;
whole-root compilation, source/axiom/known-false checks and CodeQL.
Any stronger claim is killed by a failed proof obligation, unguarded
use of the old 450^4 theorem or a changed sampling/metric object.
Independent semantic review remains Issue #50; the threshold gates
remain Issue #82.
