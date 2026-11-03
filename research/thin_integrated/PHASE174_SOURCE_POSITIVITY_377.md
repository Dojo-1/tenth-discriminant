# Phase174 — positivity without importing an invalid larger-ellipse certificate

**Status: Lean candidate, not a field-discriminant bound.**

The geometry is frozen. Write the two original finite sets of integer
pairs as
$Q_{\rm thin}(D)=\mathrm{ellipsePairs}(D,\rho_{\rm thin}(D))$
and $Q_{\rm old}(D)=\mathrm{ellipsePairs}(D,\rho(D))$.
The ordinary-jet trace Gram of either support is always the
existing **integerRectangularTraceGram** with dimensions
$R=\lfloor D/4\rfloor$ and $S=\lfloor R/25\rfloor$.
No new observations, derivative convention, row metric or field chart
are introduced.

At fourth-root floor 377, the source-exact ceilings show
$\rho_{\rm thin}(D)\le\rho(D)$. The already proved
ellipsePairs radius monotonicity and the merged Phase170 original
thin interpolation theorem give
```math
2(R-1)+(S-1)<|Q_{\rm thin}(D)|\le|Q_{\rm old}(D)|.
```
Consequently, **both original integer trace Grams have strictly
positive determinant** by the existing generic
RadialCutoff.integer_det_positive theorem.

Moreover, the previously proved padded cardinality majorant gives
```math
|Q_{\rm thin}(D)|
 \le |Q_{\rm old}(D)|
 \le \mathrm{ellipsePaddedUpperCount}
      (D,\rho(D),\mathrm{ellipseVerticalBound}(D,\rho(D))).
```
Its strict positivity follows from the thin count. The padded majorant
is only a **number-of-nodes upper bound**. It is not the determinant
of a second matrix, and must never replace $\det G_{\rm thin}$ in an
arithmetic-to-analytic comparison.

This avoids the old stronger $3R+S$ sufficient cell-area-radius
certificate, which does not transport to 377 because its rounding
margin is negative there. It does not show the larger radius is
optimal or that the final Hadamard/analytic bound survives.

See [SourcePositivity377.lean](../../lean/TenthDiscriminant/SourcePositivity377.lean).
Exact-head pinned Lean, whole-root source/axiom/negative controls and
CodeQL are required before promotion. A failed guard, source mismatch,
use of a different Gram, or change of derivative kills the claim.
The next upper bound must be rederived on $Q_{\rm thin}$, while the
old padded count may only bound its cardinality.

Evidence tags: Phase170 count P (exact-head checked and merged).
Phase174 source-positive claim H (pending CI).
Same-Gram normalized upper and 377^4 field cutoff H.
Independent semantic reconstruction is still open in Issue #50.
