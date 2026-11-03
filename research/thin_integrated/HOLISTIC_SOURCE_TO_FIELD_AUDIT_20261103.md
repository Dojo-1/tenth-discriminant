# One determinant, several compatible mathematical worlds

*Independent-reconstruction packet and claim graph · 3 November 2026 · evidence labels are local to the recorded sources.*

The question is not primarily how many more units can be removed from a fourth root. It is whether the field arithmetic, integer jet lattice, finite interpolation geometry, normalized real analytic bound, and return to the field invariant **refer to one compatible mathematical object**.

## The object that must not silently change

Start from a totally complex quadratic field $K$ with class number one. The existing squarefree imaginary-quadratic chart supplies a positive squarefree parameter $D$, split into odd and even maximal-order cases. In the odd chart fix

```math
R=\lfloor D/4\rfloor,\quad S=\lfloor R/25\rfloor,\quad
Q_D=\mathrm{ellipsePairs}(D,\mathrm{thinRadius}(D)).
```

The original rectangular monomials $Z^rW^s$, with ordinary $Z$-jets **holding $W$ fixed**, determine the integral evaluation matrix $E_{Q_D}$. The original real trace-channel metric $B_{Q_D}$ has weights $2$ and $2D$. The positive integer Gram and its auxiliary determinant are

```math
G_D=E_{Q_D}B_{Q_D}E_{Q_D}^{\mathsf T},
\quad
\Delta_D=\det G_D>0,
\quad
\mathcal N(D)=R^2S.
```

Here **$\Delta_D\ne|\mathrm{disc}(K)|$ as a general identity**. $\Delta_D$ is a constructed integer on which both sides of the contradiction act; the field discriminant comes later through the original maximal-order equivalences.

A change of basis $G\mapsto UGU^{\mathsf T}$ with $U\in\mathrm{GL}_n(\mathbb Z)$ and $\det U=\pm1$ preserves the determinant and integral lattice data when the transported certificate is explicitly tracked. A determinant-one rational shear may preserve volume but not the anchored integral lattice or its modular quotient witnesses. [TransportCoherence.lean](../../lean/TenthDiscriminant/TransportCoherence.lean) formalizes a countercontrol. This is the difference between a valid transport of a proof and a numerical coincidence.

## The source-to-field claim graph

| Edge | Formal witness | What is checked | What an external reviewer must reconstruct |
|---|---|---|---|
| Field $\to$ odd/even maximal-order chart | [ActualField331](../../lean/TenthDiscriminant/ActualField331.lean), [QuadraticChartEquivalence](../../lean/TenthDiscriminant/QuadraticChartEquivalence.lean) | Encoded degree-two field and class-number transport | Exact radicand, squarefree/parity conditions, ring of integers and actual discriminant |
| Odd chart $\to$ integral prime factors | [BinaryNullTraceGram](../../lean/TenthDiscriminant/BinaryNullTraceGram.lean), [BinaryThinLogBridge](../../lean/TenthDiscriminant/BinaryThinLogBridge.lean) | Unimodular/integral divisibility and the existing binary plus odd-prime product | The original ordinary-jet quotient, valuations, inertness, and coprime multiplication without counting two twice |
| Source $Q_D$ $\to$ strictly positive $\Delta_D$ | [SourceGeometry331](../../lean/TenthDiscriminant/SourceGeometry331.lean), [SourcePositivity331](../../lean/TenthDiscriminant/SourcePositivity331.lean) | Original thin interpolation cardinality and source-Gram positivity | Why the exact original point set gives full row rank; no substitution by the padded determinant |
| Same $\Delta_D$ $\to$ arithmetic logarithmic lower | [SameGramLower331](../../lean/TenthDiscriminant/SameGramLower331.lean), [Lower331](../../lean/TenthDiscriminant/Lower331.lean) | Original odd mass plus the once-counted generic binary exponent | Identify the exact integer whose prime factors are counted and the normalization $\mathcal N(D)$ |
| Same $\Delta_D$ $\to$ real analytic upper | [ThinUpper331](../../lean/TenthDiscriminant/ThinUpper331.lean), [UpperScalars331](../../lean/TenthDiscriminant/UpperScalars331.lean) | The original thin-support Hadamard/radial majorant | Derivative convention, row norms, endpoint errors, and why the padded ellipse bounds only the count |
| Scalar contradiction $\to$ actual field bound | [Scalar331](../../lean/TenthDiscriminant/Scalar331.lean), [ActualField331](../../lean/TenthDiscriminant/ActualField331.lean) | Exact-rational strict gap and odd/even field return | Verify the chain is about all intended $K$, not a Gram-only or scalar-surrogate statement |

The mainline theorem in [PR #112](https://github.com/Dojo-1/tenth-discriminant/pull/112) is **P relative to its encoded declarations and the three permitted standard axioms** (`propext`, `Classical.choice`, `Quot.sound`). Whole-library source checks and executable known-false strengthening controls passed. That does **not** complete the independent human mathematical reconstruction; [Issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50) remains open.

The scalar comparison at fourth root 331 is

```math
\frac{999997}{1000000}\log D-\frac{5739}{1000}
+\frac14\log2
\;\le\;\frac{\log\Delta_D}{R^2S}
\;\le\;\frac45\log D-\frac{1849}{2000}.
```

The certified floor $\log D\ge23.208$ and $\log2\ge0.6931$ give the exact gap $9543/31250000=0.000305376>0$. It is a rigorous scalar separator **only after** the two inequalities are established on that same positive Gram.

## At fourth root 328, where the proof really stands

- **P in focused branch, not a field bound:** [Phase191](https://github.com/Dojo-1/tenth-discriminant/tree/research/phase191-328-arithmetic-preflight) compiled the rational $\log328$ enclosure, the improved original odd-prime lower, the once-counted binary lower **for an explicitly positive original source Gram**, and the scalar non-overlap with exact axiom receipts.
- **P in focused branch:** [Phase192](https://github.com/Dojo-1/tenth-discriminant/tree/research/phase192-tight-floor-recovery) compiled the stronger $0.0895$ gain for the old primes 3 and 5 using $25S\le R\le25S+24$ and $S\ge500000$. This strengthening has not yet been propagated through the entire field proof.
- **H until its exact-head Lean checks pass:** [Phase193 original geometry](https://github.com/Dojo-1/tenth-discriminant/tree/research/phase193-original-geometry328) lowers the thin-ellipse count and strict Gram positivity to the 328 domain with the **unchanged** support and trace matrix.
- **H beyond geometry:** the source-matched normalized Hadamard/radial upper at 328 and then the field-return theorem. Importing a 331-domain statement and changing the number would be an invalid shortcut.

The current **fixed** sufficient cell-covering guard

```math
\left(\frac{11}{25}-\frac{1001}{1000}\frac{407}{1000}\right)t-10\ge0
```

still has $+0.690504$ at $t=328$ but fails at $t=306$. Its failure at 306 is **not** a proof that the original interpolation matrix loses rank there. The exact $328^4$ scalar margin from Phase191 is $1371/250000000=0.000005484$; the stronger Phase192 gain would give $401371/250000000=0.001605484$ *if* correctly transported into the same source lower. These quantities are not interchangeable.

## A certificate-design space rather than a single scalar

Consider a typed feasible object

```math
\mathcal C_D=(K,D,Q,R,S,J,E_Q,B_Q,U_p,\Delta_Q;\text{certificates}).
```

The feasible set consists only of those configurations where: the field chart is sound; $Q$ is the intended original source or is linked by a **proved** admissible transport; $E_Q,B_Q$ remain integral and metric-faithful; the $p$-adic quotient witnesses and binary divisor refer to the same $\Delta_Q$; $\Delta_Q>0$; and the analytic row bounds refer to that same $\Delta_Q$.

Then optimize a *certificate margin*, not an arbitrary determinant:

```math
\Gamma_D(\mathcal C)
=\mathrm{arithLower}_D(\mathcal C)
-\mathrm{analyticUpper}_D(\mathcal C).
```

The observed scalar $\Gamma_D$ is the final one-dimensional report of a highly constrained geometric/arithmetic construction. Treating its magnitude as the whole architecture conceals rank loss, integral lattice debt, and illegal transport. Non-Euclidean and higher-dimensional analogies are **S** until they supply an exact compatible operator or a falsifiable new inequality.

## Minimal reproducibility and falsification packet

Run against a pinned source head:

```sh
cd lean
lake build
python3 verify_sources.py
python3 audit.py
python3 negative_controls.py
```

A separate mathematician should be able to reproduce *at least one* integral $p$-power divisor from the original jets, rederive one thin-support rank/positivity step and one Hadamard row bound, and check the maximal-order field return **without relying on the author-written human guide as authority**. External computer replays and multiple AI agents sharing the same source are useful controls but are not independent referee reports.

**Stop rule:** if an interpretation requires a modified $Q$, a rational-only lattice change, a repeated binary factor, a missing class-number hypothesis, a false source norm bound, or a new axiom, label that implication H or R and do not advance the field cutoff. Previous proof failures and matched negative controls remain in the repository history, rather than being erased.
