# Phase 181 — what the binary determinant remembers after normalization

*3 November 2026 · exact finite ordinary-jet experiment. Classical Smith theory applied to the source Gram; not a new discriminant bound.*

The first binary-hull calculation (Phase 180) found extra powers of two in an integer determinant, but its unnormalized radical was **not** an additional divisor on top of Phase 162. We now answer a stricter question: after removing the binary factors already proved by Phase 162, how much 2-adic structure remains in the **same** original determinant?

## The one matrix, before and after a reversible frame

Retain the original rectangular monomials, ordinary Z derivatives (W fixed), the exact integer-pair observation support Q, and the original trace weights 2 and 2D. Let E be the original m by n jet matrix, with m=RS. For the row indexed by (r,s), put k=floor(r/4) and use the monic polynomial

```math
F_{r,s}(Z,W)=Z^{r-4k}(Z^4-Z^2)^k W^s
=\sum_{t=0}^{k}(-1)^t {k\choose t} Z^{r-2t}W^s.
```

Its leading coefficient is one and its other terms precede (r,s) in the original row order. Consequently the integral row transformation U is lower unitriangular and det(U)=1. Phase 162 proves that *every ordinary jet* of this transformed row, evaluated in the unchanged quadratic order, is divisible by 2^k. Therefore we have an integral quotient N:

```math
UE=\Delta N,\qquad
\Delta=\mathrm{diag}(2^{\lfloor r/4\rfloor}),\qquad
B=2C,\quad C=\mathrm{diag}(1,\ldots,D,\ldots).
```

Write H=NCN^{\mathsf T}. This is **not** a new number-field discriminant or a substitute observation set: it is the exact integral residual of the existing Gram under a proved source-row factorization. For the original G=EBE^{\mathsf T}:

```math
UGU^{\mathsf T}=2\Delta H\Delta,\qquad
\det G=2^{\Lambda_1(R,S)}\det H,\qquad
\Lambda_1=RS+2S\sum_{r=0}^{R-1}\lfloor r/4\rfloor.
```

Thus a residual valuation can be added to the existing Phase 162 exponent *once and only once*. This determinant identity is elementary given the Phase 162 row action. Its full statement as a new typed Lean identity is a **separate formalization obligation**, not something the finite calculations prove universally.

## A filtration rather than just a scalar bonus

For odd D the diagonal entries of C are odd; modulo two, H reduces to NN^{\mathsf T}. If V is the row space of N modulo two, r_2=dim(V), and h=dim(V intersect V-perp), then

```math
n_1=RS-\mathrm{rank}_{\mathbb F_2}(\overline H)
=(RS-r_2)+h.
```

That first-layer nullity yields v_2(det H) at least n_1. The stronger object is the **finite 2-primary Smith filtration** of A=(coker H)[2^\infty]. Its layer dimensions are

```math
n_t=\dim_{\mathbb F_2}(2^{t-1}A/2^t A),\qquad
v_2(\det H)=\sum_{t\ge1}n_t\quad(\det H\ne0).
```

These dimensions are preserved by integral unimodular row/column changes, including UHU-transpose shears. They are **not** automatically preserved by changing Q, moving a fixed lattice reference, or replacing the original metric.

## Exact, bounded source controls

The [executable Phase181 pilot](phase181_normalized_binary_filtration.py) reconstructs the original E from the Phase159 evaluator, takes exactly the Phase162 monic row transform, checks integrality of every quotient entry, compares the original and normalized Gram valuations using modular Smith reduction, and independently differentiates the source polynomials for D=3 and D=19 controls. It also tests an exact integral shear. The computation uses modulo 2^64 arithmetic with no precision-censored Smith pivots.

| Original source support | m | Existing Lambda1 | rank(N mod 2) | rank(H mod 2) | n1 | v2(det H) | v2(det G) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| D=3: A=C union {(-2,1)} | 4 | 4 | 4 | 3 | 1 | 1 | 5 |
| D=3: B=C union {(-1,0)} | 4 | 4 | 4 | 4 | 0 | 0 | 4 |
| D=19: historical six-node support | 32 | 64 | 16 | 8 | 24 | 102 | 166 |
| D=163: 26-node characteristic support | 150 | 1130 | 16 | 12 | 138 | 2057 | 3187 |
| D=163: remove (0,0) | 150 | 1130 | 16 | 8 | 142 | 2070 | 3200 |
| D=163: remove (10,0) | 150 | 1130 | 16 | 8 | 142 | 2046 | 3176 |

The D=163 source and deletions are exactly the selected historical Phase159 observation supports, **not** the asymptotic production thin ellipse. The two 25-node supports have identical first binary layer n1=142, but their deeper layers sum to 2070 versus 2046. First-layer rank alone loses this information. This is a finite structural distinction, not uniform number-theoretic savings.

For D=19 the actual first eight residual Smith layers are 24,24,24,20,4,2,2,2. Their sum is 102, whereas the first layer alone sees only 24. All original-Gram valuations are rechecked against the exact original support and weights, not inferred from the normalized computation alone.

## Where this cannot yet go

**One-layer asymptotic obstruction.** Since n1 cannot exceed m=RS, the first binary layer adds at most (log 2)/R after dividing by the field proof's R^2S scale. It cannot create a nonzero limiting leading-order improvement as R grows. Deeper layers could matter *only if* one proves a production-uniform lower bound after removing factors already known.

**No scalar-to-field leap.** These six cases are bounded experiments (M); the Smith identities are classical mathematics, and the normalization inherits the Phase162 formal row action. No new actual-field theorem, new auxiliary inert prime, full Phase181 Lean formalization, or independent semantic review is claimed. The four-generator 1358-factor proposal is also not silently added.

**Next falsifier.** Evaluate the normalized layers on the *original production* support across a controlled increasing-R sequence, with a null family of admissible supports and unchanged arithmetic hypotheses. Measure the full barcode normalized by R^2S and the component already accounted for by other proved binary factors. Stop if a proposed uniform surplus collapses under support changes or matches existing factors; preserve negative controls rather than inventing geometric decoration.

The ongoing external arithmetic/analytic reconstruction remains [Issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50), and the bounded Phase181 target is [Issue #99](https://github.com/Dojo-1/tenth-discriminant/issues/99).
