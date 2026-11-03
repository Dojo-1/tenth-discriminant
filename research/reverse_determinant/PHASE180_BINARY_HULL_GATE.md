# Phase 180 — The binary hull of the original jet Gram

*3 November 2026 · exact-source mathematical experiment · classical finite-field duality, not a new field bound.*

## Why return to the source?

A determinant records the total prime valuation, but not why that valuation occurs. Phase 160 separated the compulsory factorial/channel floor from extra Plücker constraints and cancellation. Phase 179 added a fixed-lattice transport counterexample. We now ask a smaller question: can an exact binary **subspace intersection** diagnose when the unchanged trace Gram has one or more additional powers of two?

No invented curvature, no revised derivative, no new sample lattice. We use the original ordinary partial-$Z$ jets, $W$ held fixed, and effective nonzero integer channels from [Phase159](phase159_observation_continuum.py). This work is not a replacement for the main [Phase178 field theorem](../../lean/TenthDiscriminant/ActualField377.lean).

## Classical theorem, applied to our trace metric

Let $D$ be a positive odd integer, $Q$ a finite set of original integer-pair observations, and $E_Q$ the $m\times n$ integer ordinary-jet matrix with $m=RS$. Discard only identically zero imaginary columns at real observations. The diagonal metric has weight $2$ for a real channel and $2D$ for a nonreal imaginary channel. Therefore

```math
G_Q = E_Q B_Q E_Q^{\mathsf T}
    = 2E_Q C_Q E_Q^{\mathsf T},
\qquad
C_Q=\mathrm{diag}(1,\ldots,D,\ldots).
```

Every entry of $C_Q$ is odd; hence the reduced matrix $E=\overline{E_Q}$ over $\mathbb F_2$ satisfies

```math
\overline{G_Q/2}=EE^{\mathsf T}.
```

Let $V$ be the row space of $E$ in $\mathbb F_2^n$, write $r=\dim V$, and define its **binary hull**

```math
\mathcal H(V)=V\cap V^\perp,\qquad h=\dim\mathcal H(V).
```

The bilinear form on $V$ is the standard binary dot product. The map from the $m$ row coefficients to $V$ has kernel dimension $m-r$. Pulling back the dot product shows

```math
\dim\ker(EE^{\mathsf T})=(m-r)+h,
\qquad
\mathrm{rank}_{\mathbb F_2}(EE^{\mathsf T})=r-h.
```

**Integral valuation consequence [P-paper, elementary].** For any integer $m\times m$ matrix $M$ with mod-2 nullity $k$, the integer $\det M$ is divisible by $2^k$: choose mod-2 independent rows and subtract their combinations from the other $k$ rows, leaving $k$ integral even rows. Applied to $M=G_Q/2$, when $\det G_Q\ne0$ we obtain

```math
\boxed{v_2(\det G_Q)\ \ge\ m+(m-r)+h.}
```

There is no hidden row-rank assumption on $E$ over $\mathbb F_2$. When $r=m$, the extra term is precisely the hull dimension $h$. A row-unimodular integer gauge preserves this dimension because it changes only the generator basis of the same binary code; a change of support may change it.

**Crucial limit:** this is a lower bound starting from the raw $m$ even channel weights. It cannot be added to the much stronger pre-existing Phase162 factorial/row-action exponent $\Lambda_1(R,S)$ without a separately proved normalization that avoids double counting. Nor does one finite hull supply uniform large-$D$ control.

## Bounded original-source witnesses

Use $D=3$, $R=S=J=2$, $m=4$; define

- $C=\{(0,2)\}$;
- $A=C\cup\{(-2,1)\}$;
- $B=C\cup\{(-1,0)\}$;
- $A\cup B=C\cup\{(-2,1),(-1,0)\}$.

The executable [Phase180 binary-hull control](phase180_binary_hull.py) independently generates the ordinary jets and compares them entrywise with the existing Phase159 evaluator. It evaluates the finite-field hull both from the Gram rank and by exhaustive enumeration of the 16 binary row combinations; the two checks are intentionally different algorithms.

| Support | Effective columns $n$ | Binary rank $r$ | Hull $h$ | $m+(m-r)+h$ | Actual $v_2(\det G_Q)$ |
| --- | ---: | ---: | ---: | ---: | ---: |
| $C$ | 4 | 2 | 0 | 6 | 8 |
| $A$ | 8 | 4 | 1 | 5 | 5 |
| $B$ | 6 | 4 | 0 | 4 | 4 |
| $A\cup B$ | 10 | 4 | 1 | 5 | 5 |

The original exact determinants are, respectively, $2304$, $122656$, $74896$, $622368$. In particular, $A$ and $B$ both have *full binary row rank*. Yet $A$ has a nonzero hull, hence an extra factor of two in the same trace Gram; $B$ has zero hull and the minimal $2^m$ valuation. A coarse test asking only for full modular row rank cannot distinguish them.

The base support $C$ is a negative control against claiming the bound is always sharp: its raw mod-2 deficiency gives only $6$, while the actual valuation is $8$. The A/B comparison is a negative control against asserting a universal hull bonus for all full-rank supports.

The code also verifies invariance of the full-profile and determinant under an exact integral row shear $U$ with $\det U=1$. The control is a *gauge*; it is not a new admissible sample support.

## What is old, what might help

The hull identity and LCD/Gram characterization are established coding-theory mathematics, not discoveries of this project. See J. L. Massey, [*Linear codes with complementary duals*](https://doi.org/10.1016/0012-365X(92)90563-U) (1992), and [later explicit Gram-rank/hull treatment](https://doi.org/10.1007/s10623-025-01757-y). Our bounded contribution is to instantiate this known structure on the unchanged ordinary-jet trace Gram, including its actual channel weights and an explicit failure control.

**A useful, still-open target [H].** Transport the established Phase162 binary row factors *first*, obtaining an explicitly integral **normalized** Gram on the same $Q$. Only then ask whether that residual Gram has a uniform positive binary hull/nullity under the production dimensions and original thin-ellipse support. If it does, its extra valuation may be genuinely new **relative to that already-proved divisor**, subject to independent semantic verification and the same-Gram upper bound.

A successful tiny calculation does **not** prove that uniform claim. The null possibility is quite real: the source-matched full-rank support $B$ has zero hull. It may also happen that Phase162 already captures all production-uniform savings.

## Decision gates

1. **Must reproduce [M]:** exact original jets (no Hasse substitution), original $2,2D$ weights, the four listed determinant/valuation/rank/hull tuples, and integral-gauge invariance. Historical Phase159/160 controls must not regress.
2. **Must falsify if wrong:** reject an implementation whose raw mod-2 rank predicts the same hull for both $A$ and $B$; reject a claim of strict equality in the base support $C$.
3. **Promotion:** only promote the finite tuples after exact-head CI passes. The general lower inequality is a short classical paper proof, not yet a fresh Lean theorem or independently reviewed field-theorem bridge.
4. **Stop:** do not attach an extra $\log 2$ saving to the Phase178 discriminant argument without exact normalization, a uniform lower proof, and a matched analytic-upper check.

This preserves the distinction between a richer finite local certificate and a stronger number-field theorem.
