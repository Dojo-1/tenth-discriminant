# Phase 198 — transporting the original determinant to fourth root 324

*Research note — 3 November 2026. This is a theorem target [H] until exact-head Lean and whole-root audits succeed.*

The [326→324 arithmetic preflight](https://github.com/Dojo-1/tenth-discriminant/issues/120) found that the older $-1.400$ estimate for $\log R-\log D$ was a **bound on coordinates**, not an obstruction in the underlying arithmetic. This branch tests whether that repaired transport is compatible with the **original** thin ellipse and ordinary-jet trace Gram. No auxiliary inert prime, additional binary count, altered support or substitute determinant is introduced.

## Start with the integer, not the threshold

The one object that must receive both inequalities is the integer determinant

```math
\Delta_D=\det G_D,\qquad
G_D=E_D B_D E_D^{\mathsf T}>0.
```

Here $E_D$ is the original integer evaluation matrix from pair observations in $Q_D=\mathrm{ellipsePairs}(D,\mathrm{thinRadius}(D))$, rectangular monomials and ordinary $Z$-derivatives **holding $W$ fixed**. The bilinear trace weights in $B_D$ are the same $2,2D$ as before. Keep $R=\lfloor D/4\rfloor,\ S=\lfloor R/25\rfloor$ and the original $\rho=\lceil(13/25)D^{3/4}\rceil$. The padded ellipse is only a node-count majorant; its determinant is never substituted.

## Three independent source obligations

**Geometry.** Repeat the original thin-radius interpolation sufficient condition at fourth root 324. In the $R$-to-fourth-root floor argument, the correct gap to 320 is **4**, not 7 (327) or 8 (328). The cell-covering sufficient-condition buffer at 324 is the positive rational

```math
\left(\frac{11}{25}-\frac{1001}{1000}\frac{407}{1000}\right)324-10
=\frac{140033}{250000}>0.
```

Positivity of this buffer is only one guard; Lean must still compile the actual cardinality and Gram positivity source.

**Arithmetic.** The improved *same-floor* logarithmic estimate, independently focused-Lean-checked in [Phase197](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41693676927), is

```math
\log R\ge\log D-\frac{1391}{1000}\quad(D\ge324^4).
```

The already existing aspect-ratio raw-prime lemma then supplies the proposed conservative lower $\frac{999997}{1000000}\log D-\frac{5811}{1000}$. Recover an additional $895/10000$ using the **same** odd primes 3 and 5 and exact $25S\le R\le25S+24$; apply the original binary exponent **once**, obtaining the intended same-Gram lower

```math
\frac{999997}{1000000}\log D
-\frac{57215}{10000}+\frac14\log 2
\le \frac{\log\Delta_D}{R^2S}.
```

**Analysis.** Retain the old radius, cardinality and row estimate, and use $\log(521/1000)\le -651/1000$ rather than rounding it to $-650/1000$. The radial and contraction savings are unchanged. The intended original-Gram upper is

```math
\frac{\log\Delta_D}{R^2S}
\le\frac45\log D-\frac{1851}{2000}.
```

Neither an upper on the padded Gram nor a lower on an arbitrary replacement support proves this: both statements must use precisely the same $G_D$.

## Arithmetic collision versus mathematical theorem

The independently focused-Lean-checked rational certificate at $D\ge324^4=11{,}019{,}960{,}576$ is

```math
\left(\frac{999997}{1000000}-\frac45\right)\frac{231228}{10000}
-\frac{57215}{10000}+\frac{1851}{2000}
+\frac{6931}{40000}
=\frac{4414079}{2500000000}>0.
```

The statement checked in the preflight is a **conditional scalar implication**, not a field theorem. A neighboring negative control shows that these fixed conservative affine bounds fail to separate at 323; this does not ban a stronger future 323 argument.

The final return, once the same original Gram has both incompatible inequalities, should preserve the maximal-order odd/even chart split and use the field equivalence to conclude for totally complex degree-two fields of class number one that $|\mathrm{disc}(K)|<324^4$. That field claim remains [H] until the source-exact Lean and whole-root verification passes.

## Evidence and kill conditions

- [P] The separate Phase197 scalar/log-floor lemmas have an exact-head Lean build, a statement/axiom report, and a 323 negative control.
- [H] The 324 geometry, integer Gram positivity, original-prime lower, analytic upper, and field return are separate proof targets. A source file, positive rational margin or good-looking chain is not proof of them.
- [H] External mathematical fidelity still requires the independent reconstruction requested in [Issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50).

Kill or demote this branch if the root-324 source ellipse fails interpolation, the exact floor-ratio gain loses a premise, a stale 327 guard enters, the odd and analytic inequalities use different determinants, the binary factor is duplicated, the field equivalence is weakened, or an extra axiom appears. A mathematical disagreement must be kept as an explicit obstruction, not hidden by another layer of algebra.
