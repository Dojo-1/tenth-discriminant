# Independent review entry: the strict 47-billion theorem

**Open review request — no independent human reconstruction has been received.** This is a *map of obligations*, not a self-issued referee report. Read [issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50) for the question, and [the human derivation](HUMAN_RECONSTRUCTION.md) for the author's proposed mathematical route. The proofs are extensively AI-assisted.

## Freeze the external claim, not just the endpoint number

[`TightRadialEndpoint.lean`](../../lean/TenthDiscriminant/TightRadialEndpoint.lean) encodes

```lean
theorem totallyComplex_degree_two_classNumber_one_discriminant_bound_47b
    (K : Type*) [Field K] [NumberField K] [NumberField.IsTotallyComplex K]
    (hdegree : Module.finrank Rat K = 2)
    (hc : NumberField.classNumber K = 1) :
    (NumberField.discr K).natAbs < 47000000000
```

The conclusion concerns **the actual integral field discriminant**, not `det G`, not a parameter chosen by a caller, and not an enumeration of the known nine fields. Every deduction below should retain the original objects and the quantified scope of this statement.

## Four reconstruction crossings

| Independent crossing | Minimal source trail | What would break it? |
| --- | --- | --- |
| **1. Field and maximal order.** From arbitrary totally complex degree-two `K`, identify a squarefree imaginary quadratic parameter, the actual ring of integers in both parity cases, and transfer class number one without replacing the discriminant. | [Quadratic field chart](../../lean/TenthDiscriminant/QuadraticFieldChart.lean) → [class-number/inert bridge](../../lean/TenthDiscriminant/ClassNumberInertBridge.lean) → [actual-field endpoint](../../lean/TenthDiscriminant/TightRadialEndpoint.lean). | Treating `Z[sqrt(-D)]` as the maximal order for all `D`; conflating field discriminant and `det G`; using the finite nine-field classification to prove the effective bound. |
| **2. One integral ordinary-jet matrix, with two-sided prime extraction.** Construct `E` from the original complete ellipse and *ordinary* derivatives; prove the exact integer coordinate trace pairing `B`, `G=EBE^T`, and, for each eligible inert `p`, `U_p E=Delta_p C_p` with integral `C_p`. Derive `det G=p^{2F(p)}det(C_p B C_p^T)`. | [IntegerTraceGram](../../lean/TenthDiscriminant/IntegerTraceGram.lean), [row action](../../lean/TenthDiscriminant/RectangularRowAction.lean), [integral Gram factor](../../lean/TenthDiscriminant/RectangularGramFactor.lean), [Frobenius premise](../../lean/TenthDiscriminant/InertFrobenius.lean). | Inverting a factorial nonunit modulo `p`; claiming a row-only factor gives `2F`; substituting a reduced node set or a different matrix; assuming inertness without its field-level guard. |
| **3. Same determinant's real positivity and effective numerical pressure.** Under the original point-count/interpolation guard, show `G` positive definite. Reconstruct the integer radial frame, all derivative corrections, uniform rectangle savings, complete finite prime/log mass and reciprocal tail. Confirm that the lower/upper bounds use *one* `det G`. | [EllipseCellArea](../../lean/TenthDiscriminant/EllipseCellArea.lean), [LatticeEllipse](../../lean/TenthDiscriminant/LatticeEllipse.lean), [TightRadialSaving](../../lean/TenthDiscriminant/TightRadialSaving.lean), [RadialCutoff](../../lean/TenthDiscriminant/RadialCutoff.lean), [PrimeTail](../../lean/TenthDiscriminant/PrimeTail.lean). | Conditional area hypotheses left undisclosed; lost boundary nodes; treating a single selected minor's bound as an upper bound on the Cauchy–Binet *sum*; omitting prime-tail errors; changing the frame determinant. |
| **4. Contradiction and field return.** Verify the rational interval/log certificate and strictly positive separation for `D≥47000000000`; check the even chart and the arbitrary-field equivalence at the actual discriminant. | [TightRadialEndpoint](../../lean/TenthDiscriminant/TightRadialEndpoint.lean), [verification receipts](PHASE133_VERIFICATION.md). | An inequality reversed, an invalid rounding bracket, an unhandled parity case, or an equivalence that does not preserve the field discriminant. |

## Small exact arithmetic that **can** be checked without the repository

The endpoint compares, for `u=log D`,

$$
\text{lower}(u)=\frac{999997}{1000000}u-\frac{5739}{1000},
\qquad
\text{upper}(u)=\frac45u-\frac{1649}{2000}.
$$

At `u\ge 24573/1000`, the difference is at least

$$
\left(\frac{999997}{1000000}-\frac45\right)\frac{24573}{1000}
-\frac{5739}{1000}+\frac{1649}{2000}
=\frac{26281}{1000000000}>0.
$$

This is a **standalone rational calculation**; it does *not* check why the lower or upper functional inequalities apply, the logarithmic bracket `log(47000000000)≥24573/1000`, the field-level hypotheses, or the adequacy of the effective prime tail. Those are the nontrivial crossings for the referee.

## How to return a useful independent result

A strong external response is a short derivation by a mathematician who has not participated in producing these proofs, or a precise obstruction. State which of the four crossings was reconstructed, its exact source and assumptions, any finite or symbolic test used, and the first claim that would fail if the hypotheses changed. A *partial* review is valuable; it does not become a complete review merely because the rest compiles.

The [Phase133 published source receipt](PHASE133_VERIFICATION.md) identifies the checked proof version, standard-axiom audit, source/interval correspondence and negative controls. [PRs #52–#54](https://github.com/Dojo-1/tenth-discriminant/pull/54) formalize separate local compatibility lemmas and finite tests, **not** independent reconstruction of the 47-billion production proof.

The repository keeps [issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50) open until the semantic external reconstruction obligation is genuinely met. The [companion issue #51](https://github.com/Dojo-1/tenth-discriminant/issues/51) concerns comparison of normalized modular-rank methods with the original Gram and is not required to accept or reject this already encoded endpoint.
