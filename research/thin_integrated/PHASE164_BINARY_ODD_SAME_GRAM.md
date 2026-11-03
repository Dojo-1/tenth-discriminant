# Phase164: two arithmetic scales on one thin determinant

## What is the integer?

For squarefree $D$ with $D\equiv3\pmod4$, and class number one
in the *correct quadratic field*, choose the same thin ellipse as the
Lean-checked 41,006,250,000 field theorem. Evaluate the original integer
polynomial matrix of **ordinary** $Z$-derivatives, with $W$ held fixed,
at each integer-pair sample $Q_{\rm thin}$. Form
$G_{\rm thin}=E_{\rm thin} B E_{\rm thin}^{\mathsf T}$, where $B$
retains exactly the source weights $2,2D$.

## One elementary lemma, not a new conjectural architecture

Under the already proved class-number-one and interpolation guards, the
Phase162 source theorem says

```math
  2^{\Lambda_1(R,S)}
  \prod_{\substack{p<R\\p\text{ odd prime}}}
       p^{2v_p(R,S)}
       \mid \det G_{\rm thin}.
```

Here $\Lambda_1(R,S)=RS+2S\sum_{r<R}\lfloor r/4\rfloor$.
The odd-product excludes 2, so combining certificates is legitimate.
Since $\det G_{\rm thin}>0$ is an integer, it is at least this entire
product. The implementation makes **no change** to the sampling support,
row ordering, derivative convention, metric or field assumptions.

**What the theorem does NOT say:** $\det G_{\rm old}=\det G_{\rm thin}$,
that the four-generator $2^{1358}$ certificate is Lean-proved,
that prime 2 can be counted twice, or that the field bound improved.

## Lean in reading order

1. [ThinEllipseCount](../../lean/TenthDiscriminant/ThinEllipseCount.lean):
   the thin ellipse still has enough points **only for D>=450^4**.
2. [IntegerTraceGram](../../lean/TenthDiscriminant/IntegerTraceGram.lean):
   exact ordinary derivative observations and 2,2D trace form.
3. [BinaryNullTraceGram](../../lean/TenthDiscriminant/BinaryNullTraceGram.lean):
   the univariate binary factor on **arbitrary Q**, then the product
   with distinct odd primes.
4. [BinaryThinGramBridge](../../lean/TenthDiscriminant/BinaryThinGramBridge.lean):
   instantiate these theorems at the new **same thin Q**, prove positivity,
   and obtain the exact integer lower bound.
5. [ThinIntegratedEndpoint](../../lean/TenthDiscriminant/ThinIntegratedEndpoint.lean):
   independent real upper on the same new Gram, and actual-field transport.

## Status and the next falsifiable gate

**Formalization status — merged 2 November 2026.** [PR #83](https://github.com/Dojo-1/tenth-discriminant/pull/83) merged at [`26bd83a6`](https://github.com/Dojo-1/tenth-discriminant/commit/26bd83a6f5fa62539fa8a87eda234026cfaf0d53) after the exact combined-head [whole-library Lean, source, permitted-axiom and known-false negative-control run 41417184165](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41417184165) and both focused same-Gram [Lean runs](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41417192952) passed. The three declarations in `BinaryThinGramBridge.lean` are **P: checked as encoded**, not a new numerical discriminant theorem. Independent semantic reconstruction of the surrounding number-field argument remains open.

The next target is the *logarithmic* inequality
$\Lambda_1\log2+\mathrm{mass}_{\rm odd}\le\log\det G_{\rm thin}$
with an explicit check that the existing recovered prime estimate counts
**only odd primes**. Then test the difference against the **same**
real upper. Crucially, if an attempted better cutoff is below
41,006,250,000, the current geometric rank theorem no longer applies.
One must prove a new uniform count and radius guard rather than extrapolate.

Cross-reference: [Phase164 research issue](https://github.com/Dojo-1/tenth-discriminant/issues/82).
