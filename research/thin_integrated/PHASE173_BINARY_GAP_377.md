# Phase173 — the binary quarter is an old exponent, not a new prime

The original univariate trace Gram supplies the **already proved**
exponent Lambda(R,S) = binaryNullGramExponent(R,S). Phase165 establishes
4*Lambda >= R^2*S for all natural R,S, exactly, not asymptotically.

With positive R,S and original comparison scale c=R^2*S,
the normalized 2-adic contribution is at least log(2)/4.
This is **not** a second counting of a prime: it is the 2-adic
contribution already paired with the exact odd-prime product in the
same integer Gram determinant (see BinaryThinLogBridge).

The lower affine expression L(u)=(999997/1000000)u-5739/1000,
the previous thin Gram analytic upper expression
U(u)=(4/5)u-1849/2000, and the merged Phase169 floor u>=23.7
yield the purely numerical gap

L(u)+log(2)/4-U(u) >= 987039/10000000 > 98/1000.

The new Lean file checks a slightly weaker strict inequality with
0.098 buffer and excludes any **single scalar g** satisfying both
g<=U(u) and L(u)+log(2)/4<=g.

**Critical typing:** this theorem does not supply the two hypotheses.
The same-original-positive-Gram arithmetic lower is candidate PR #91;
the full analytic upper on that same Gram at 377^4 is not yet proved.
Point-count and radius prerequisites are separate PRs #89/#90.
Positivity and the actual quadratic-field chart must be preserved.

**Evidence status:** H until pinned focused and whole-root Lean
CI, permitted axioms, negative controls and CodeQL pass. Even after
a pass, only this conditional statement is P; the 377^4 field bound
remains H. Human reconstruction #50 remains open.
