# Phase192 — tighter source-floor arithmetic, original primes 3 and 5

*Research hypothesis until exact-head Lean CI; deliberately outside the field-theorem root.*

The previously compiled Phase190 lemma gets a uniform normalized gain of 0.0879 from $10R\le251S$. For the actual source dimensions, however, $S=\lfloor R/25\rfloor$ gives a much tighter **exact integer** inequality:

~~~math
25S\le R\le25S+24.
~~~

In the $D\ge328^4$ range, $S\ge500000$, so these imply, without approximation of the source,

~~~math
R\le\frac{250001}{10000}S,\qquad
S-1\ge\frac{499999}{500000}S.
~~~

The already established saturated rows for **primes 3 and 5**, with the same certified logarithmic weights $1.09$ and $1.6$, yield

~~~math
2\,\mathrm{small35Mass}(R,S)\ge
\frac{1399497201}{25000000}S^3,\qquad
R^2S\le\frac{62500500001}{100000000}S^3.
~~~

The exact rational budget for the proposed new uniform gain is

~~~math
\frac{1399497201}{25000000}
-\frac{895}{10000}\frac{62500500001}{100000000}
=\frac{41940539105}{1000000000000}>0.
~~~

The [proposed Lean module](../../lean/TenthDiscriminant/RecoveryGainFloorRatio.lean) therefore targets the dimension-conditional inequality

~~~math
S\ge500000,\quad25S\le R\le25S+24
\ \Longrightarrow\
\frac{\mathrm{recoveredPrimeMassLower}-\mathrm{rawPrimeMassLower}}{R^2S}
\ge0.0895.
~~~

It does **not** alter the saturated-row source, introduce an inert prime, modify trace weights, or assert a new field bound. It strengthens only the existing normalized arithmetic recovery.

If both the new gain and the old original raw mass inequality are proved at $D\ge328^4$, the proposed odd-only lower becomes

~~~math
\frac{999997}{1000000}\log D-\frac{57305}{10000},
~~~

and adding the one previously established binary factor would give the stronger *conditional same-Gram* lower with an additional $\frac14\log2$. Against the unchanged analytic-upper scalar, this raises the conservative certified separation at the $328^4$ floor to $0.001605484$, rather than $0.000005484$.

**Evidence controls:** P for the earlier original source lemmas and Phase190 certificate; H for this more aggressive bound until the focused exact-head Lean build and axiom report pass. H remains for the $328^4$ original thin support positivity, Hadamard upper, same-Gram specialization and field return. Retain negative controls at lower artificial logarithmic floors and independent semantic reconstruction in [Issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50).

**Kill:** the tight floor ratio fails for any legal $(R,S)$, the source weights are altered, a source substitute is introduced, Lean compilation fails, or the claimed scalar consequence quietly relies on an old $331^4$ geometric premise. See [Issue #113](https://github.com/Dojo-1/tenth-discriminant/issues/113) for the separate $328^4$ research target.