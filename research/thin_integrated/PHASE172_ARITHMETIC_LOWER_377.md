# Phase172 — the original lower pressure at the 377 fourth-root floor

**A source-preserving Lean candidate, not a new field bound.**

The only changed premise is the lower numerical domain: \(D\ge377^4\).
All source dimensions, odd-prime weights, prime-tail budget, binary exponent,
class-number-one condition, integer-pair observation support, ordinary jets
and trace metric remain exactly as before.

## The smaller arithmetic bridge

The original \(R=\lfloor D/4\rfloor,\ S=\lfloor R/25\rfloor\)
still satisfies the production dimension and aspect-ratio bounds at
\(377^4\). The existing ratio lemma
\(\log D-1.4\le\log R\le\log D-1.38\) can be reconstructed from
\(249D\le1000R\) for \(D\ge1000\), with no 450-root assumption.

Phase169 supplies the **true** new premise \(\log D\ge23.7\), so the
recovered odd-prime mass admits the original normalized affine lower:
\[
L(D)=\frac{999997}{1000000}\log D-\frac{5739}{1000}.
\]

The source-level inequality is even more useful. For *any* finite
original integer-pair observation set \(Q\), assuming the original
integer ordinary-jet trace Gram \(G_Q\) is positive and the squarefree,
odd-chart, class-number-one hypotheses hold, one can seek to prove
\[
L(D)\le\frac{\log\det G_Q}{R^2 S}.
\]

Its proof uses exactly the existing odd-prime product and its
univariate \(2\)-adic factor. The latter is nonnegative and may be
discarded for this narrow lemma; including its sharper quarter
contribution is a separate future theorem. No new prime is counted
twice and no old larger-ellipse determinant is substituted.

The planned Lean file is [Lower377.lean](../../lean/TenthDiscriminant/Lower377.lean).
It separates the original dimensions/log-R estimates, the
normalized recovered-mass lower, the exact odd-product comparison,
and the final same-source-Gram lower.

## Promotion and failure rules

Promote a statement only after focused pinned Lean compilation,
full-root source/axiom/known-false controls and CodeQL at the exact
commit. A successful algebraic theorem does **not** re-prove
positivity for a particular support or the analytic determinant
upper at \(377^4\). These remain the load-bearing missing bridges.
Do not weaken the premise of any theorem already proved only on
\(D\ge450^4\).

The corresponding source \(Q\) must be the identical one used in
the future upper bound, and the full theorem must target the
**actual field discriminant**, not just \(\det G_Q\).
Human semantic audit stays open in Issue #50; the threshold
mathematics is tracked in Issue #82.
