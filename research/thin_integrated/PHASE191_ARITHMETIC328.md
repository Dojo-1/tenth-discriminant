# Phase191 — exact arithmetic at fourth-root 328

*3 November 2026 · standalone arithmetic and logarithmic bridge; **not a field-discriminant theorem**.*

The new [Phase190 recovery lemma](../../lean/TenthDiscriminant/RecoveryGainSharpRatio.lean) is now Lean-compiled and has an axiom-dependency receipt: under $S\ge100$, $25S\le R$ and $10R\le251S$, the same original saturated rows for primes $3$ and $5$ guarantee a normalized recovered gain of $879/10000$ rather than $81/1000$. No new prime, source jet, lattice, or trace weight enters.

This phase asks how far that sharper arithmetic travels while keeping the *other* normalization assumptions frozen.

## Source lower and logarithm

The [Lower328.lean](../../lean/TenthDiscriminant/Lower328.lean) proof is parameterized by an **arbitrary original support $Q$ with positive original integer trace-Gram determinant**. It re-establishes the old odd-prime tail and normalized raw mass at $D\ge328^4$, then uses precisely the new $10R\le251S$ guard to derive:

~~~math
\frac{\mathrm{recoveredPrimeMassLower}(R,S,I)}{R^2S}
\;\ge\;
\frac{999997}{1000000}\log D-\frac{57321}{10000}.
~~~

With the original class-number-one, odd-squarefree assumptions and any $Q$ whose original Gram is **already known positive**, the exact source-to-mass theorem implies this lower bound for the same Gram:

~~~math
\frac{\log\det G_Q}{R^2S}
\;\ge\;
\frac{999997}{1000000}\log D-\frac{57321}{10000}.
~~~

The additional [SourceOddBinary328.lean](../../lean/TenthDiscriminant/SourceOddBinary328.lean) reuses the dimension-generic original binary exponent **once**. For any original support $Q$ whose original Gram determinant is *already known positive*, and the same odd squarefree class-number-one assumptions, it establishes the sharper conditional bound:

~~~math
\frac{\log\det G_Q}{R^2S}
\;\ge\;
\frac{999997}{1000000}\log D-\frac{57321}{10000}
+\frac14\log 2.
~~~

This combines odd and binary arithmetic for **one and the same original positive Gram**. It deliberately does **not** prove the actual thin-ellipse Gram positive throughout the $328^4$ domain; that source-geometric premise remains open.

The independent [Scalar328.lean](../../lean/TenthDiscriminant/Scalar328.lean) certifies the exact five-term odd-log enclosure:

~~~math
\frac{5793}{1000}\le\log328\le\frac{5794}{1000},
\qquad
D\ge328^4 \Longrightarrow \log D\ge\frac{23172}{1000}.
~~~

Then the *hypothetical* original binary-quarter lower plus the unchanged old analytic upper would be strictly disjoint, with an exact certified margin:

~~~math
\left(\frac{999997}{1000000}-\frac45\right)
\frac{23172}{1000}
-\frac{57321}{10000}
+\frac{1849}{2000}
+\frac{6931}{40000}
=\frac{1371}{250000000}
=0.000005484>0.
~~~

The two negative controls reject the old gratuitous $0.098$ separator and disprove strict scalar separation at the artificial floor $u=23.16$. The latter is useful for seeing why a still lower root will need additional proof strength.

## Evidence and stop condition

- **P once exact-head focused Lean CI passes:** the sound \`log328\` enclosure and abstract scalar separator; stronger recovered original odd-prime lower and conditional once-counted binary lower on the same positive source Gram.
- **P already compiled:** the original $p=3,5$ recovery sharpening, Phase190.
- **H:** positive definiteness of the original *thin* trace Gram throughout $D\ge328^4$; specialization of the *conditional* same-Gram binary-and-odd lower to that source, the original Hadamard/radial normalized upper at this domain, and the actual-field theorem.
- **R:** treating the scalar separator as a field theorem, altering $Q$ or the trace metric, smuggling an old $331^4$ premise into a $328^4$ lemma, or counting an auxiliary inert prime.

**Kill:** any failed Lean compilation, unpermitted axiom, changed source, false logarithm certificate, or inability to close the same-Gram upper/field return. A tiny scalar margin is not enough to justify weakening the original analytic estimate.

The present published mainline theorem remains $375^4$ until the independent stacked $331^4$ integration PRs #111/#112 finish. Issue [#113](https://github.com/Dojo-1/tenth-discriminant/issues/113) tracks the $328^4$ hypothesis; [#50](https://github.com/Dojo-1/tenth-discriminant/issues/50) tracks independent mathematical reconstruction.
