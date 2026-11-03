# Phase186 — the same original thin Gram, with odd and binary lower combined

*3 November 2026 · a bounded Lean bridge at $331^4$, not a field-discriminant theorem.*

The source is still the original ordinary-$Z$-jet evaluation matrix $E_Q$, with $W$ held fixed, integer-pair thin ellipse $Q_D$, unmodified trace metric $B_Q$ carrying weights $2,2D$, and Gram $G_D=E_Q B_Q E_Q^{\mathsf T}$. The actual number-field discriminant is **not** this Gram determinant.

## What has to coincide

For $D\ge331^4$, under the original odd squarefree class-number-one chart, Phase184 proves $\det G_D>0$ for precisely this thin-Q. Phase185 separately recovers the *same-source* odd-prime mass lower from the existing exact integral divisor. The older **normalized_binary_quarter** is a generic theorem in the integer dimensions $R,S$; it does not rely on a 375 cutoff.

The [Phase186 Lean source](../../lean/TenthDiscriminant/SameGramLower331.lean) aims to combine precisely these imported proofs, so the resulting single determinant satisfies:

~~~math
\underbrace{\frac{999997}{1000000}\log D-\frac{5739}{1000}}_{\text{old recovered odd-prime mass}}
+\underbrace{\frac14\log 2}_{\text{one existing binary factor}}
\;\le\;
\frac{\log\det G_D}{R^2 S},
\qquad R=\lfloor D/4\rfloor,\quad S=\lfloor R/25\rfloor.
~~~

No new prime is inserted. The original binary exponent is used **once**, not added twice or transplanted from a different Gram. The hypothesis is *conditional* on the original odd chart and class-number-one assumption. The same original determinant must later be bounded from above analytically to obtain a contradiction.

## Evidence floor and kill gate

- **P — imported:** exact source Gram positivity and Phase185 odd mass on the 331 domain, original BinaryThinLogBridge and generic binary-quarter theorem, subject to their checked source and permitted axioms.
- **H — this branch until CI:** the combined normalized lower on the original thin Gram, with a positive comparison scale.
- **H — remains:** the $331^4$ same-Gram Hadamard upper, and then the actual-field class-number exclusion and discriminant return.
- **R:** treating a rational or normalized *different* Gram as an interchangeable source; counting an extra auxiliary binary prime; declaring the abstract scalar contradiction a field result.

The file does **not** import an old 375 actual-field theorem. Its use of the 375-named binary module is only for the dimension-generic **normalized_binary_quarter** lemma, which has no $D\ge375^4$ premise. The focused test audits this distinction and checks original source terms by name. Independent semantic reconstruction remains [Issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50).

**Kill on:** any changed observation support, derivative convention, trace metric, class-number chart, or source determinant; a new axiom or unexplained Lean admission; failed source check or exact-head compilation. No bound improvement follows before a matching analytic upper.
