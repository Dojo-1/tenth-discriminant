# Phase341 — does the original method reach `307^4`?

> **Exact falsification controls, not a new field bound.** 
> 侘未来 · classical arithmetic rising from below, source geometry descending from above.

**Evidence:** finite exact integer/rational checks (M, for this bounded pilot), supplemented by elementary exact algebra. **Not yet Lean-formalized** at 307 and **not** a class-number-one discriminant theorem. The latest formally checked result remains [`313^4`](../phase340/VERIFIED_313.md).

The established Phase340 proof never changes its source: `Qthin = ellipsePairs D (thinRadius D)`, the original ordinary-Z jets, and one integer trace Gram. A proposed 307 extension must preserve this object and prove *new* 307-domain guards. A blanket textual substitution `313 → 307` is **mathematically false**.

## 1. First positive signal — the cell-area sufficient condition

The existing original-ellipse interpolation proof needs the rational inequality

```math
\left(\frac{11}{25}-\frac{1001}{1000}\frac{407}{1000}\right)t-10\ge0,
\qquad t=D^{1/4}.
```

The coefficient is exactly `32593/10^6`, so for integral fourth-root floors:

```math
32593\cdot306-10^7=-26542<0,\qquad
32593\cdot307-10^7=6051>0.
```

The conservative criterion therefore becomes available at `t ≥ 307`; it does **not** certify the proposed `306^4` floor by this argument. The positivity at 307 is narrow: `6051/10^6 = 0.006051`.

## 2. The decisive NEGATIVE control — old radius/R guard fails

The previous 313 proof uses

```math
R=\lfloor D/4\rfloor,\qquad R\ge78D^{3/4}.
```

At the proposed endpoint `D=307^4=8,882,874,001`, the exact original dimensions are

```text
R = 2,220,718,500
S = 88,828,740
rho = 15,045,911
thinRadius = 12,731,155
```

But the supposed copy of the old bound is false:

```math
R-78\cdot307^3=-36,168,054<0.
```

Consequently the old ratio `rho/R ≤ 521/78000` is ALSO false:

```math
521R-78000\rho=-16,586,719,500<0.
```

These are **exact counterexamples** to naive 313-domain transport.

A candidate weaker geometrical estimate *does* pass at the endpoint:

```math
R-76\cdot307^3=21,700,832>0,\qquad
521R-76000\rho=13,505,102,500>0.
```

**Open theorem:** prove for ALL `D ≥ 307^4` the analogues of
`R ≥ 76*(fourthRoot D)^3` and `rho/R ≤ 521/76000` with the original floors and ceiling. Passing at a single fourth power does not prove these universal statements.

Then independently re-evaluate the **original analytic envelope**:
`endpoint_error`, `count_log_error`, `normalized_upper`, and the final same-Gram Hadamard estimate. Reusing the old 313 analytic constant without those proofs would invalidate the field comparison.

## 3. Scalar arithmetic: promising, explicitly conditional

If an independently certified `log 307 ≥ 5726/1000` is established (so `log D ≥ 22904/1000` for `D ≥ 307^4`), **and if** the original 313 lower and upper constants survive, the exact rational conservative gap becomes:

```math
\text{lower}-\text{upper}\approx+0.014075676.
```

With the older radius saving instead, the counterfactual gap is about `-0.020924324`. The exact fractions, not floating point comparisons, are used in the [finite control tests](test_307_gate.py).

This is only a **conditional arithmetic model**. Neither the rational logarithm enclosure nor the all-domain analytic upper has yet been proved at 307, and the proven old 313 radius/R inequality definitely fails there.

## 4. Mathematical promotion checklist

- **P target:** produce a sound `log 307` enclosure from `checkPositiveLogBounds`, and prove `fourthRoot D ≥ 307`.
- **P target:** prove the new 76-cube radius/R guard and rederive all analytic inequalities on the ORIGINAL Qthin Gram.
- **P target:** rederive original dimensions, inert-prime lower and joint odd/binary valuation under the 307-domain hypotheses, with no mixed `H` bonus.
- **P target:** show strict separation for the new lower/upper coefficients over all `D≥307^4`.
- **P target:** assemble the actual quadratic-field discriminant theorem, print its exact type and allowed axioms; require independent semantic source review before public promotion.
- **Kill control:** if the repaired analytic majorant loses the ~0.014 conditional scalar margin, do not claim the 307 field bound. Record a counterexample or a mathematically explicit obstruction instead.

The 307 programme is **separate from the completed 313 formal certificate**. Neither the field-theorem source nor public `main` should be changed until these independent bridges close.
