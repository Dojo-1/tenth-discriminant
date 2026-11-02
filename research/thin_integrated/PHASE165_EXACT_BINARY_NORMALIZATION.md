# Phase165 — the binary factor has an exact normalized size

The [Phase162 univariate source theorem](../../lean/TenthDiscriminant/BinaryNullTraceGram.lean) already proves that `2^Lambda1(R,S)` divides the original integer ordinary-jet Gram, for any finite source sampling set. The Phase164 [same thin-Q bridge](../../lean/TenthDiscriminant/BinaryThinGramBridge.lean) puts that univariate divisor alongside the *odd-only* prime mass without double counting.

This small phase answers a different question: **how large is the certified exponent once the determinant inequalities are normalized by R²S?**

Write R=4q+t, with 0<=t<4. Counting the floors in blocks of four gives

```
sum(r/4 for r=0,...,R-1) = 2q(q-1)+tq
Lambda1 = R*S + 2*S*sum(r/4)
4*Lambda1 = S*(R^2 + t*(4-t))
```

Consequently, for R,S>0, `Lambda1/(R^2*S) >= 1/4`, with equality when 4 divides R. The next normalization step is **not** to claim a new field cutoff, but to combine the *correct* odd-only log-mass and the verified `log 2` lower bracket on precisely the same positive thin Gram.

The Lean module [BinaryExponentNormalization](../../lean/TenthDiscriminant/BinaryExponentNormalization.lean) targets three statements: an exact integer identity, an integer quarter bound, and its order-preserving multiplication by `Real.log 2`. The source input has not been altered. At the historical configuration R=30,S=5, it checks `Lambda1=1130`; the four-generator paper/finite exponent 1358 remains an entirely distinct, unproved Gram theorem.

**Promotion gate:** run the focused Lean test, full-root source/axiom/negative controls and CodeQL on the exact branch head. **Stop condition:** if the scaled identity fails at any R,S (including 0 or small remainders), preserve the failure and fix the finite algebra rather than changing source objects or quietly adding asymptotic assumptions. No genuine field improvement follows until the lower-threshold geometry, analytic upper, prime-tail and field transports are re-certified.
