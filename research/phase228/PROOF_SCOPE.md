# Phase228 — one combined integral Frobenius frame on the original Gram

**Verified scope (10 November 2026).** The combined-basis source theorems and their downstream $321^4$ field application compile on [Phase209 PR #157](https://github.com/Dojo-1/tenth-discriminant/pull/157) at commit [4c3dc08](https://github.com/Dojo-1/tenth-discriminant/commit/4c3dc08e791d9835355f012a3e88b67cedf57884). Both the [focused workflow](https://github.com/Dojo-1/tenth-discriminant/actions/runs/42820526500) and [full-library Lean audit](https://github.com/Dojo-1/tenth-discriminant/actions/runs/42820526708) passed, with no unexpected axioms. The PR remains distinct from independent human mathematical reconstruction ([Issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50)).

## The source object and its exact dimensions

Keep the **same** original integer ordinary-$Z$-derivative observation matrix $E$, full thin-ellipse support $Q$, and trace metric $B$. The original positive integer trace-Gram is

$$
G=EBE^{\mathsf T}.
$$

For row-major labels $i=rS+s$, an odd inert prime $p$, and

$$
k=\min\!\left(\left\lfloor\frac rp\right\rfloor,S-1-s\right),
\qquad
\ell=\left\lfloor\frac{s}{p^2}\right\rfloor,
$$

the integral combined source row is

$$
P_{r,s}(Z,W)
=Z^{r-pk}W^{s-p^2\ell}(Z^p-W)^k(W^{p^2}-W)^\ell.
$$

The binomial expansion has indices $0\le t\le k$, $0\le u\le\ell$, with target monomials

$$
Z^{r-pt}W^{s+t-(p^2-1)u}
$$

and coefficient $(-1)^{t+u}\binom{k}{t}\binom{\ell}{u}$. The combined row-major matrix $U_p$ uses **one joint sum**, not a product of separately truncated row matrices. Its leading coefficient is $1$ and every other active term has a lower row-major index, so $\det U_p=1$.

## The source-to-determinant bridge

[Phase228CombinedBasis.lean](../../lean/TenthDiscriminant/Phase228CombinedBasis.lean) proves the combined polynomial/ordinary-jet action and the same-original-Gram factorization

$$
U_p G U_p^{\mathsf T}=\Delta_p K_p\Delta_p,
\qquad
K_p\in M_{RS}(\mathbb Z),
\qquad
(\Delta_p)_{ii}=p^{k_i+\ell_i}.
$$

Consequently, for each odd inert $p$ covered by the hypotheses,

$$
p^{\,2\sum_i(k_i+\ell_i)}\mid\det G.
$$

This is a **lower divisibility statement**, not an exact Smith valuation. The old vertical exponent and the new horizontal exponent are each counted once in the **same** determinant. [Phase260EnhancedOriginalGram321.lean](../../lean/TenthDiscriminant/Phase260EnhancedOriginalGram321.lean) assembles the enhanced odd-prime factor with the binary divisor; [Phase261](../../lean/TenthDiscriminant/Phase261EnhancedLog321.lean) and [Phase262](../../lean/TenthDiscriminant/Phase262HorizontalLogBridge321.lean) convert it to a logarithmic lower bound.

[Phase259Horizontal321.lean](../../lean/TenthDiscriminant/Phase259Horizontal321.lean) proves the conservative production floor-mass estimate for $R=\lfloor D/4\rfloor$, $S=\lfloor R/25\rfloor$:

$$
\frac{\operatorname{horizontalPrimeMass}(R,S)}{500R^2S}
\ge \frac{4659}{625000}-\frac{16895455}{625000D}.
$$

The bound is **not** added to a separate Gram's prime mass. [Phase263](../../lean/TenthDiscriminant/Phase263EnhancedLower321.lean) proves the enhanced lower on the original thin Gram, [Phase265](../../lean/TenthDiscriminant/Phase265ThinUpper321.lean) proves its analytic upper, [Phase266](../../lean/TenthDiscriminant/Phase266ScalarOverlap321.lean) proves strict separation, and [Phase267](../../lean/TenthDiscriminant/Phase267ActualField321.lean) transports the result to the actual field discriminant:

$$
|\operatorname{disc}(K)|<321^4=10\,617\,447\,681
$$

for totally complex degree-two number fields of class number one, under the theorem's formalized assumptions.

## Negative controls and review boundary

The original row $(3,9)$ at $R=4,S=11,p=3$ has old monomial columns $42,34,10,2$ with coefficients $+1,-1,-1,+1$. The $p=1$ degeneration is excluded from structural claims. Neither a second determinant, a Hasse derivative, nor an unproved extra prime valuation may replace the original source.

The older Phase228 submission checklist listed the polynomial action, original-jet identity, same-Gram factorization, exponent sum and field return as **unproved targets at that historical head**. Those source and field obligations are now formalized and compiled at the head linked above. Lean verification establishes the encoded statements; an independent human semantic audit is still open.