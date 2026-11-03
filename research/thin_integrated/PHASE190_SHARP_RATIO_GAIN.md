# Phase190 — Recover more from the same two primes

*3 November 2026 · standalone Lean strengthening, not a new discriminant bound.*

The Phase188 $331^4$ actual-field theorem compiled under the permitted axioms. Its full library-root integration is still staged in PRs #110–#112. This separate investigation starts from the pre-existing, unchanged saturated ordinary-jet rows for primes **3 and 5**; it does not modify the observation support, prime set, trace metric, or binary normalization.

The old [StrongSmallPrimeRecoveryGain.lean](../../lean/TenthDiscriminant/StrongSmallPrimeRecoveryGain.lean) proves a lower bound of $0.081$ for the normalized recovered small-prime mass. Its proof already obtains

~~~math
2\,\mathrm{small35Mass}(R,S)\ge
\frac{277101}{5000}S^3,
~~~

but then loses precision by bounding $R\le 26S$. Since the original choice is $S=\lfloor R/25\rfloor$ and the source already verifies $10R\le251S$ for large $S$, the sharper ratio gives

~~~math
R^2S \le \frac{63001}{100}S^3,
~~~

with the exact positive budget

~~~math
\frac{277101}{5000}
-\frac{879}{10000}\frac{63001}{100}
=\frac{42321}{1000000}>0.
~~~

The target [RecoveryGainSharpRatio.lean](../../lean/TenthDiscriminant/RecoveryGainSharpRatio.lean) is the **generic** bounded theorem

~~~math
S\ge100,\quad 25S\le R,\quad 10R\le251S
\quad\Longrightarrow\quad
\frac{\mathrm{recoveredPrimeMassLower}(R,S,I)
-\mathrm{rawPrimeMassLower}(R,S,I)}{R^2S}
\ge\frac{879}{10000}.
~~~

The exact source proof explicitly reuses the old saturated-row weights for primes 3 and 5 and their existing certified logarithmic estimates. This is a stronger *recovery* from already present arithmetic evidence, not an auxiliary inert-prime strategy.

A separate 328-floor numerical preflight is recorded in [Issue #113](https://github.com/Dojo-1/tenth-discriminant/issues/113): $\log328\ge5793/1000$, and after the new gain, the scalar gap is precisely $1371/250000000>0$. This margin is only $0.000005484$ and is **not** a field theorem.

**Evidence classes:** P for the already compiled original saturated-weight lemmas, H for the new sharper lemma until focused Lean checks pass, H for every $328^4$ same-Gram/field transport. A failed compilation, altered arithmetic source, or counterexample to the ratio guard blocks promotion. The new module remains outside the production library root until verified and separately reviewed.

**Stop:** do not merge or claim a $328^4$ cutoff just because the source numerics look favorable; the current field-theorem integration at $331^4$ must finish first, and independent semantic review [Issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50) remains open.