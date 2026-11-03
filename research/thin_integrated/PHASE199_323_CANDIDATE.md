# Phase 199 — The 323⁴ source bridge

**Research-only.** The 327⁴ theorem is integrated on main; [PR #122](https://github.com/Dojo-1/tenth-discriminant/pull/122) audits 324⁴ across the whole project. The 323⁴ declaration below is a theorem **candidate**, not a current field bound until focused Lean + same-root audits succeed.

## The object is unchanged

Keep $R=\lfloor D/4\rfloor$, $S=\lfloor R/25\rfloor$, the original thin integer pair set $Q_D=\mathrm{ellipsePairs}(D,\mathrm{thinRadius}(D))$, ordinary $Z$-derivative jets holding $W$ fixed, and the original trace metric with entries $2$ and $2D$. From the same integer evaluation matrix $E_D$ form one positive integer determinant:

```math
G_D=E_DB_DE_D^{\mathsf T},\qquad \Delta_D=\det G_D>0.
```

The padded ellipse controls sample **count only**. Changing its determinant into the target would change the theorem.

## Why the arithmetic threshold moves

The sound finite logarithm lemma in [Phase199Scalar323](../../lean/TenthDiscriminant/Phase199Scalar323.lean) retains the original floor inequality $249D\le1000R$ and proves

```math
\log R\ge\log D-\frac{1391}{1000}
\qquad (D\ge323^4).
```

The already existing aspect-ratio raw-odd-prime lower has intercept $4419/1000$ in $\log R$. The exact rational inequality

```math
\frac{4419}{1000}+
\frac{999997}{1000000}\frac{1391}{1000}
<\frac{5810}{1000}
```

releases one more $0.001$ of arithmetic strength compared with the 324 branch. Add the previously verified Phase192 $895/10000$ recovery from **only the existing primes 3 and 5**, subject to its exact floor guards, and count the binary divisor **once**. The intended same-original-Gram lower is

```math
\frac{999997}{1000000}\log D-\frac{57205}{10000}
+\frac14\log2
\le \frac{\log\Delta_D}{R^2S}.
```

The unchanged geometric/Hadamard analysis retains the candidate upper

```math
\frac{\log\Delta_D}{R^2S}\le\frac45\log D-\frac{1851}{2000}.
```

At $D\ge323^4$ the sound $N=5$ rational series gives $\log D\ge231104/10000$; together with $\log2\ge6931/10000$:

```math
\left(\frac{999997}{1000000}-\frac45\right)
\frac{231104}{10000}
-\frac{57205}{10000}
+\frac{1851}{2000}+\frac{6931}{40000}
=\frac{178543}{625000000}>0.
```

This positive rational comparison was separately **focused-Lean-checked** in [the Phase199 scalar workflow](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41695578641). It does **not** by itself prove a field result.

## Geometry is not just a scalar

At fourth root 323, the floor offset from 320 becomes **3**, rather than 4 at root 324. The original source's cell-covering sufficient criterion has positive rational buffer:

```math
\left(\frac{11}{25}-\frac{1001}{1000}\frac{407}{1000}\right)323-10
=\frac{527539}{1000000}>0.
```

But the proof must still reconstruct the exact support count, evaluation rank, Gram positivity, unchanged padded cardinality majorant, original arithmetic lower and same-Gram Hadamard upper. The smaller root is **not** obtained by citing a theorem whose hypothesis is $D\ge324^4$.

The final field return must preserve the maximal-order imaginary quadratic odd/even chart and field-equivalence discriminant map. The proposed statement is $|\mathrm{disc}(K)|<323^4=10{,}884{,}540{,}241$ for totally complex quadratic class-number-one fields; only a successful exact-head Lean build can promote this to a *formally checked candidate*.

## Explicit kill conditions

Do not proceed if a 323 geometry guard fails, the original determinant differs between upper and lower, p3/p5 divisibility is weakened or independently assumed, the binary divisor is duplicated, the stated numeric gap has a wrong coefficient, or a nonstandard axiom is introduced. Require a **negative control**: the unchanged conservative affine bounds do **not** separate at root 322. The 322 precision-release hypothesis in [Issue #121](https://github.com/Dojo-1/tenth-discriminant/issues/121) explicitly changes those bounds, so it does not contradict this negative control.

Independent semantic reconstruction in [Issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50) remains an obligation even after compilation. Formal verification of the encoded statement is not an independent referee's proof of mathematical fidelity or novelty.
