# Phase367 — exact original evaluation and trace Gram
**2026-11-20 · Preregistered research-only · stacked on Phase366 PR #277.**

## Living question
Can one write **the original** `integerTraceGramMatrix` as a product of actual ordinary-Z-derivative evaluation matrices, preserving all original source points, original row labels, trace weights and derivative observation clocks, and distinguish valid `GL_n(Z)` gauge transport from clock extension? This is an explicit source-to-matrix correspondence, not a new number-field theorem.

## Frozen data
- Full finite `Q : Finset (Int × Int)`, no deduplication outside Finset and no substitution by padded Q.
- `D : Nat`, `J : Nat`, `rows : Fin n → Nat × Nat`.
- `integerDerivativeRow D r s j p`, with W held fixed, ordinary Z derivatives and original factorials.
- Full column index `Fin J × Q` (not a chosen rank minor or compressed support).
- `A[i,(j,p)]= (integerDerivativeRow ...).1`, `B[i,(j,p)] = (...).2`.
- `G=integerTraceGramMatrix Q D J rows` with `integerPairTrace D a b = 2*(a.1*b.1 + D*a.2*b.2)`.
- Rectangular case uses `rows i=(i.val/S,i.val%S)` without changing the row order.

## Exact theorem target
```
G = 2*(A*A.transpose + D*(B*B.transpose))
```
Entrywise, `G(i,k) = 2 sum_(j,p) (A[i,(j,p)] A[k,(j,p)] + D B[i,(j,p)] B[k,(j,p)])`. This is integral and valid even at `D=0`; PSD as a real matrix is a consequence at D≥0, independently of the existing cast requiring D>0. The factorization must be proved against the named ORIGINAL source definition rather than stipulated by a new Gram name.

## Frame and clock distinctions
- An **integer unimodular row-frame** `U` acts `A → U A, B → U B`, hence `G → U G U.transpose` and `det G` is invariant for `det U=±1`. The committed initial Lean target requires `det U=1`; a det=-1 extension can follow after independent compilation.
- Observation clock `J → J+1` changes the *column carrier* `Fin J × Q` by adding new derivative observations. It is not the same operation as `GL_n(Z)` row transport.
- On Q={(0,0),(5,0)}, D=25, rows 1,Z: J1 det100, J2 det116, with PSD increment. Thus p-adic divisibility is NOT monotone even though the real Gram grows.
- At D=3,Q={(0,1)},J=2, rows 1 and ZW: original Gram [[2,6],[6,24]], det12; omitting the imaginary D-weight destroys the matrix. This is the critical non-real negative control.

## Falsification and tests
1. Reject if the exact Lean theorem cannot elaborate without new axioms, `sorry`, `admit` or changing a source definition.
2. Reject if the factorization holds only after modifying the trace, replacing W by Z, sampling a padded source or choosing a minor.
3. Reject any transfer of valuation across changed observation clock or nonunimodular rows; preserve exact integer counterexamples.
4. Run exact-head Lean on the new file, print permitted transitive axioms, then full root checks. Compare original source code and independent Prolog toy examples.
5. Independent issue #50 review remains open. The formally encoded 301^4 discriminant result is NOT independently reconstructed, and neither Phase367 nor its Prolog controls can fill that external mathematical gap.

## Evidence lattice
P only for exact-head compiled Lean statement and precisely matching syntax. M for bounded integer oracle/Prolog. H for full field arithmetic reconstruction and anything not yet compiled. None of this certifies new class-number or Siegel-zero implications.
