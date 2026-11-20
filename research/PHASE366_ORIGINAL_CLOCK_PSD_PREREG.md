# Phase366 — source-exact observation-clock PSD and p-adic counterworld
20 November 2026. Research-only; no change to the 301^4 field bound.

## Frozen source
Use the repository's ORIGINAL `IntegerTraceGram.lean`: `integerDerivativeRow D r s j p` is the ordinary Z derivative with W held fixed, `integerPairTrace D a b = 2*(a.1*b.1 + D*a.2*b.2)`, Q is the full unchanged finite integer-pair source, `integerTraceGramMatrix` uses the same row labels, and `integerRectangularTraceGram` uses the same row-major R x S indexing. Both J and J+1 share Q,D,R,S. Do not replace Qthin by a padded sample or alter J and Q simultaneously.

## Theorem targets (H until exact-head compilation)
For every finite original Q, D>0 and any finite row family, let G_J be the real-cast original integer Gram. Prove exactly
```
G_(J+1) - G_J = 2 * sum_(p in Q)
  (a_(p,J) a_(p,J)^T + D b_(p,J) b_(p,J)^T) >=_PSD 0
```
where (a,b) are the pair coefficients of the original `integerDerivativeRow`. In `Phase366ObservationClockPSD.lean`, the real-complex version uses the existing `integerTraceGramMatrix_cast` and genuine one-clock feature matrices to show PSD; the exact integer entrywise increment is separately stated to avoid an unverified substitution.

## Falsifiers / negative controls
1. A PSD increment must **not** be promoted to p-adic monotonicity or divisibility of the full Gram.
2. Q={(0,0),(5,0)}, D=25,R=2,S=J_initial=1, rows (1,Z): integer G_1=[[4,10],[10,50]], det100, v5=2; G_2=[[4,10],[10,54]], det116, v5=0. Same Q and rows, extra derivative observation. Contrast with admissible GL_2(Z) row basis transport, which preserves determinant.
3. Existing Phase365 three-sample control Q={(1,0),(6,0),(11,0)}, J=1,2,3 has det=500000,784400,799664, valuations v5=6,2,0 and PSD increments. It is a bounded M witness, not a uniform valuation theorem.
4. At D=0 the real/complex coordinate injection assumed by the cast bridge is not covered; prove only D>0 for the integer-cast theorem.
5. A source-changed or jet-changed Gram is **not** related by this clock theorem.
6. If new Lean proof relies on unproved axioms, `sorry`, or a surrogate Gram, reject and retain the failed head.

## Evidence governance
P only for exact compiled Lean theorem with permitted transitive axioms and source correspondence. M for exact finite Prolog and integral matrix calculations. H for source-to-field semantic audit, number-theoretic novelty, and any claimed stronger cutoff. Keep Phase364 PR #275 and Phase365 PR #276 as separate research prerequisites. Keep issue #50 open. Never claim an implication for Siegel zeros.

## Practical test
```sh
cd lean
lake build TenthDiscriminant.Phase366ObservationClockPSD
lake build TenthDiscriminant
```
Check exact names and `#print axioms`, and keep original 301 comparison theorem unchanged.

## Human reconstruction
Use Q={(0,0),(5,0)} to compute G_1, G_2 directly from the derivative definition and explain why the Loewner increment is PSD but 5-adic divisibility falls. Contrast it with a single integral unimodular row change.
