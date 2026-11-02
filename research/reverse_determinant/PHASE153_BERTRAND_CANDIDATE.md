# Phase153 — Bertrand/Frobenius original-Gram comparison: a candidate 25-billion boundary

**1 November 2026. One canonical branch `main`.** This is a deliberately bounded audit with an explicit proposed new field cutoff, **NOT a proved or Lean-certified field theorem**. [P-paper candidate] for the elementary inequalities and conditional Frobenius-geometry construction; [M] for rational-constant tests and high-precision samples; [A] for the still-unformalized rank/positivity-to-Hadamard bridge; [H] for the global 25-billion endpoint; [R] for promoting a local positive gap, an old cardinality guard, or a rival triangular determinant without transport.

## The fixed object and the self-correction

Professor Tao's challenge is to obtain explicit, checkable class-number-one discriminant bounds without importing the Heegner classification. Phases144–151 constructed detailed algebraic and geometric transport around the **original rectangular ordinary-`∂Z^j` / W-held-fixed integer Gram**, but mostly did not decrease the complete prime-mass-to-metric gap. Phase152 [Frobenius graph](PHASE152_FROBENIUS_GRAPH.md) instead supplies a *rank* argument on a legitimately smaller geometric support.

The load-bearing specification/API drift is this: [`RadialDetBound.integer_log_upper`](../../lean/TenthDiscriminant/RadialDetBound.lean) **still requires the old cardinality hypothesis** `2(R−1)+(S−1)<|Q|` solely to obtain `H.PosDef`. Its actual diagonal, Hadamard and source-matched `enderUpperB` algebra can instead be reused when `H.PosDef` is certified by the Frobenius rank proof. [Phase149](PHASE149_POSITIVITY_BRIDGE.md) already separated the same positivity guard for the **prime-mass lower theorem**, with an earlier green root-Lean receipt. The new *upper* positivity-first refactor is now committed in [`RadialDetBound.integer_log_upper_of_posDef`](../../lean/TenthDiscriminant/RadialDetBound.lean), retaining the old theorem as a compatibility wrapper; it is **not compile-certified until exact-head Lean CI passes**. No existing Lean theorem can yet be invoked directly on the new reduced support.

## Proposed conditional parameter family

Assume `D≥25,000,000,000`, `D≡3 (mod 4)`, `D` squarefree, and hypothetically `h(−D)=1`. Set `m=(D+1)/4`. Bertrand's postulate provides an **odd** prime `m/2<p<m`; the existing [`ClassNumberInertBridge.smallPrime_nonsquare_of_classNumber_one`](../../lean/TenthDiscriminant/ClassNumberInertBridge.lean) gives its inertness under that class-number hypothesis. Let
\[
R=p-1,\quad S=J=\lfloor R/25\rfloor,\quad
\delta=\tfrac12\sqrt{D+1},\quad
\rho=\Big\lceil\delta+\sqrt{p\sqrt D/3}\Big\rceil,
\quad Q=\{(x,y)\in\mathbb Z^2:x^2+Dy^2\le\rho^2,\ y\ge0\}.
\]
The full rectangular lattice has covering radius `δ` and covolume `√D`. A disk-cell covering argument gives `|\Omega_D(\rho)|≥π(\rho−δ)^2/\sqrt D>p`. The same elementary estimates at `D≥25b` show `ρ/R<0.006`, hence `2ρ<p` and all conjugate residues are distinct modulo `p`. The Frobenius graph `W=Z^p` gives the original ordinary jets, with `R<p`, `J<p`, and injective exponents `r+ps`; since `J|\Omega|>pS−2`, the *actual* integer evaluation matrix has full row rank modulo `p`, so its original positive-trace Gram `G_Q` is positive definite over `ℝ`. This [P-paper] geometry is not yet Lean formalized.

The same class-number-one Frobenius/prime-mass theorem, with unchanged arithmetic assumptions `R<m`, gives `L_{\rm arith}(R,S)≤\log\det G_Q`. On the upper side, `Q` lies in the same radius-`ρ` ellipse and the elementary rectangle count is `|Q|≤4D`; after the *pending positivity-first upper refactor*, the original `enderUpperB(R,S,S,ρ,4D)` bounds **the identical** `\log\det G_Q`. No new row basis, Hasse jet, `μ_R` ring, fractional divided-power lattice, or factorial denominator is introduced.

## Two quantified normalized inequalities [P-paper target, frozen constants]

Let `L` be precisely [`NormalizedComparison.rawPrimeMassLower`](../../lean/TenthDiscriminant/NormalizedComparison.lean), with `I=FirstEnderInterval.tailBudget`, and `U=enderUpperB(R,S,S,ρ,4D)`. The existing certified chain proves `L≤exactOddPrimeMass(R,S)`. The formulas are *not* clipped or independently renormalized.

For `D≥25b`, Bertrand gives `R>D/8−1>3×10^9`, `S≥10^8`, `1/25−1/R≤S/R≤1/25` and `R/S≤25+25/S`. Writing the exact normalized raw lower from Lean and using `log x≤√x`, `log(R−1)≥log R−1/(R−1)`, and the source constants
\[
C=\mathrm{FAC}+I-\mathrm{LIN}<1.791,\quad
C_s=\mathrm{SQ}+I<0.134281,\quad \mathrm{ERR}<9893,
\]
yields the explicitly bounded loss
\[
\frac{L}{R^2S}\ge\log R -
\left[
\tfrac32+\tfrac1{3\times10^9-1}+\tfrac{15}{50000}
+1.791+\tfrac{2(9893)}{3\times10^9}
+\tfrac{25+25/10^8}{3}\,0.134281
\right]\ge\boxed{\log R-4.411}.
\]

For the original upper, the ceiling and `p>D/8` imply
\[
\rho\le A(1+\tfrac1{160}),\qquad
A=\sqrt{p\sqrt D/3},\quad
\log\rho\le\tfrac14\log D+\tfrac12\log R-\tfrac12\log3+\tfrac1{160}+\tfrac1{2R}.
\]
Indeed `D^(1/4)>395` and the exact rational ceiling correction
\[
\frac{49}{20\cdot395}\left(1+\frac1{2D}\right)
+\frac{49}{10\cdot395^3}<\frac1{160}
\]
holds throughout the range. Independently `ρ/D^{3/4}<0.293`, `ρ/R<0.006`; `|Q|≤4D`. The normalized [`upperB_normalized`](../../lean/TenthDiscriminant/NormalizedComparison.lean) expression and `S/R≤1/25` bound its small count/radius endpoint terms by `<0.001`. With `log3>1.09`, this gives
\[
\boxed{\frac{U}{R^2S}\le 0.24\log D+0.56\log R-0.596}.
\]
**Audit rule:** the numerical Python program verifies the exact rational constants and stresses both formulas, but it is NOT a universal proof engine; a competent human/Lean reconstruction of each displayed inequality remains mandatory.

Subtracting the same-source envelopes:
\[
\frac{L-U}{R^2S}
\ge 0.44\log R-0.24\log D-3.815.
\]
As `R>D/8−1`, `log8<2.08`, `log D>23.9` at `D≥25b`, the right side is greater than
\[
0.2(23.9)-0.44(2.08)-3.815-10^{-6}> \boxed{0.049}.
\]
**If** all positivity, arithmetic and geometric transports are reconstructed, this uniform positive gap would exclude every hypothetical odd squarefree class-number-one `D≥25b` without relying on the Heegner list. It could then be combined with the existing even-chart result to improve the canonical 47-billion actual-field endpoint. **This implication is still [H] and is not merged as an asserted new Lean theorem.**

## Matched controls, failure, and non-equivalence

The [bounded verifier](phase153_bertrand_budget.py) pins the four old prime-log constants and tail budget, checks **two independently written expressions** for each normalized `L` and `U`, runs exact rational gates, samples the worst allowed Bertrand ratio `p/m≈0.5` and the opposite `p/m≈1`, and records the source head. Pseudo-prime sensitivity ratios are **not asserted to be prime or inert**.

At `D=25,000,000,003`, the weakest-ratio pilot reports `L≈17.45273708`, `U≈17.38811839`, gap `≈+0.06461869`. At `D=41,006,250,003` with actual `p=10,251,562,487` merely as a parameter, `R=10,251,562,486`, `S=410,062,499`, `ρ=26,406,772`: `L≈18.64073737`, `U≈18.16982756`, gap `≈+0.47090981`. Matching `R,S,n=4D` but using the previous radius `ρ≈47,385,001` instead gives `U≈18.73128910`—**negative** lower-minus-upper. This matched control isolates the geometric saving. At `D=15b`, weak-ratio gap is negative: a legitimate kill against extrapolating the 25b candidate downward.

A generic orbit fold can retain the original Gram only with weights; here the arithmetic theorem and upper use **the new unweighted** `Q` throughout. The competitor's 331 proof employs a different triangular/Hasse normalization and larger inert prime, so no determinant equivalence or numerical parity is asserted. The proof may stand or fall on its own technical merit.

## Corrective research ledger and stop rule

| Claim | Before | Audit status |
|---|---|---|
| Phase152 Frobenius finite ranks | [M] | Retained: exact-source finite CI at [#41287933302](https://github.com/Dojo-1/tenth-discriminant/actions/runs/41287933302) |
| New all-D radius and full-rank field support | [P-paper] | Conditional proof requires independent reconstruction; not Lean |
| A small-radius `Q` can enter the old analytic theorem unchanged | [R] | **Retired**: old `hcard` cannot be silently reused |
| Same-Gram 25b gap | [H] | Exact rational constants and bounded samples support a new **proof target**, not a field result |
| Hypercomplex/sheaf geometry supplies automatic determinant saving | [R] | **Retired**: only the completed same-object lower–upper cycle can justify a bound |
| Full 25b field statement / finite finish | [H] | Not submitted; no Lean theorem, no peer-reviewed confirmation |

**Independent witness status:** the old Lean numerical definitions and prime-divisibility proofs are compiled primary artifacts, but our new Python test, proof outline and self-audit are *correlated model-generated evidence*. Only finite source-matched controls are independently executable. The global proof still needs human mathematical reconstruction and exact-head Lean compilation with allowed-axiom and negative controls.

**Next bounded experiment (freeze):** compile and independently review the new `RadialDetBound.integer_log_upper_of_posDef` and retained `hcard` wrapper, then formalize the Frobenius-rank/covering argument for `Q(D)`. Promotion rule: all hypotheses quantified, same original integer Gram on both sides, conservative envelope proved, exact-head Lean CI green, independent statement review. Kill if any rank, count, radius, prime or upper transport fails. **Stop further ontology extension** until this one bridge is proved or retired.
