# Phase290: preregister Noether–Smith wall modules before implementation

**Date: 2026-11-12. This protocol is committed BEFORE Phase290 executable code.** The user supplied Emmy Noether, *Ideal Theory in Rings* (Berlyne translation of *Idealtheorie in Ringbereichen*, arXiv:1401.2577, especially §9 and §12). §12 studies integer-matrix elementary-divisor classes under U A V with unimodular U,V, prime-power components and irreducible two-sided **classes**. We use this as classical motivation, not attribution of our specific wall formula to Noether, and we do NOT identify arbitrary two-sided matrix ideals with the class theory (her own text separates them).

The source-independent mathematical problem: Phase289's original D563 centered integer ellipse Q_plus with |y|<=2 adds two outer y-layers to Q_minus with |y|<=1, and the original 700-row ordinary-jet trace Gram has a major change in its four-fiber analytic correlation. What can be transported at primes without replacing this original lattice or double-counting its elementary divisors?

## Objects and types, with exactly the ORIGINAL metric

Fix D=563, rho=51, R=140, S=J=5 from the unchanged Phase206 source `research/phase206/source_probe.py` Git blob `3f954b59d9f86b06ad53667c869b5b24f2e6c7f6`, with original ordinary Z-jet `research/phase204/ordinary_jet_filtration.py` blob `dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8` (W frozen during differentiation).

Original Q_plus: 359 integer (x,y) points, y∈{-2,-1,0,1,2}; original inner Q_minus: 285 points (|y|<=1); new Delta Q: 74 points (|y|=2), central-inversion closed. Source **ROW** module Z^(R*S)=Z^700 and *all* original row/jet/metric definitions stay fixed. Q_minus and Q_plus are DIFFERENT observation sources; no identification of their number-field theorems, local determinant valuations or prime ideals is authorized.

For exact finite testing, freeze SIX original monomial labels, in this order:
`I=[(0,0),(1,0),(2,0),(1,1),(4,0),(4,1)]`.
These exercise both central parities, ordinary jet orders j=0..4 (including j=4) and D563. Their original 6x6 principal Gram matrices must be SPD in both supports; the FULL 700x700 Gram is not numerically computed or Smith-decomposed.

For any support Q and chosen labels, let E_Q be its original (6 x 2J|Q|) **integer** ordinary-jet evaluation matrix, and B_Q=diag(2,2D) repeated for each (j,q), with no Gaussian weights and no maximal-order half coset. Then G_Q=E_Q B_Q E_Q^T. The independent Phase206 mixed-moment oracle must agree exactly with our original-jet direct Gram for Q_minus, Delta Q and Q_plus. Observation order for addition is an explicit column permutation: E_plus=[E_minus,C], B_plus=diag(B_minus,B_Delta) after permuting columns; never mistake this reordering for a row-lattice change.

## Exact module-theoretic target [P-paper, to be checked]

Set `L_minus=im(E_minus) subset Z^6`, `L_plus=im([E_minus,C])`. The identity on the codomain Z^6 induces the **canonical surjection**
`coker(E_minus) ->> coker(E_plus)`, with kernel `L_plus/L_minus`.
Thus, over every prime, maximal-minor/Fitting ideals for E can only enlarge under addition of columns, and the p-primary evaluation *index* can only stay fixed or decrease; if full row rank fails, state a rank-plus-torsion version instead. This is a theorem about E, NOT G.

The original same-row positive Gram satisfies `G_plus=G_minus+C B_Delta C^T`. A **new integral wall presentation** is

```
W = [[G_minus, C B_Delta],
     [B_Delta C^T, -B_Delta]]
U = [[I_6,-C],
     [0, I_m]]
W=U diag(G_plus,-B_Delta) U^T, U in GL_(6+m)(Z).
```

Therefore `coker(W) ≅ coker(G_plus) ⊕ coker(B_Delta)`, with all p-primary elementary divisors conserved under this integral congruence. The B_Delta part consists of known 2 and 2D torsion (once per original real/imag observation coordinate), and MUST NOT be promoted as additional valuation of G_plus. This is a stable presentation of the **new** wall Gram, NOT a unimodular identification with G_minus.

For real positive Gram, `det(G_plus)>=det(G_minus)` (same size) but p-local valuations and Gram elementary divisors need NOT be monotone. Two fixed **genuinely integral trace-metric** 1x1 counterworlds, with every observation weight 2 and constant evaluation 1:
- one old column -> add two columns: G_minus=2, G_plus=6, v3 increases 0 -> 1 despite unchanged coker(E)=0;
- three old columns -> add one column: G_minus=6, G_plus=8, v3 decreases 1 -> 0 despite unchanged coker(E)=0.
Neither toy is the D563 field source. A claimed p-local Gram monotonicity must be rejected on these countermodels.

## C2 symmetry across the actual layer wall

For any original row (r,s), define P_(r,s)=(-1)^(r+s). For an observation channel (j,q,ch), define the signed permutation T which sends its basis vector to (-1)^j times the corresponding channel at -q. The elementary identity `jet_(r,s,j)(-q)=(-1)^(r+s-j)*jet_(r,s,j)(q)` gives **P E = E T**, and T B T^T=B for any centrally symmetric Q. Thus P G P=G; both the wall presentation W and its unimodular shear are equivariant with diag(P,T) for Delta Q. Only claims on the selected six rows are numerically tested; the algebra applies to the full unchanged original row module.

**Critical binary negative control**: two exchanged observation basis vectors have Tswap=[[0,1],[1,0]]. Its eigenvector columns [[1,1],[1,-1]] have determinant -2, so the even/odd eigenspace decomposition of the OBSERVATION lattice is not generally a direct unimodular Z_2 splitting, even though original row parity makes G block diagonal. No extra 2-adic mass may arise from the fake projection (I±T)/2.

## Exact frozen experiment and stop conditions

1. Verify both frozen Git source blob hashes, exact D563 parameters, Q counts 285/74/359 and central inversion of both supports. Preserve ordinary-j=4 jets and positive weights 2,2D.
2. Compute the 6x6 principal Grams by two algorithms (direct original jets and existing Phase206 mixed moments), check G_plus=G_minus+G_delta EXACTLY.
3. Across p in {2,3,5,7,563} check `rank_Fp E_minus <= rank_Fp E_plus` with an independent row-elimination oracle. Compute exact all-ranks determinantal divisors of the 6x6 Grams (gcd of all kxk minors), recover Smith invariant factors, check their divisibility chain/product det, and compare (without prespecifying direction) p-adic valuation profiles across the wall.
4. Use just ONE centrally paired new orbit `Delta Q_orbit={(0,-2),(0,2)}` (20 original signed-metric observation columns) to build the 26x26 coupled integral wall presentation W; verify the exact U diag(G_orbit,-B_orbit) U^T identity, exact inverse-transpose graph congruence, Noether equivariance P C=C T and T B T^T=B. Do not claim a 26x26 check is a 700x700 Smith computation.
5. Verify BOTH counterworlds above, the binary nonunimodular eigenbasis det=-2, and the rule that at p=2 or p|D metric factors must remain distinct from inferred Gram torsion.
6. Any mismatch of source/count, original jets, independent original Gram, canonical symmetry, exact integral congruence, Smith divisibility, or counterworlds is a **STOP**, not permission to rewrite a prediction post-result. The measured p-local profile of D563 is intentionally not preregistered to a favorable outcome.
7. Keep the result DRAFT even with focused, Markdown and root Lean CI passes; require an independent source-to-field review before merge. Do not modify PR157, Phase287/288/289, source helper files or historical failed CI artifacts.

## What this can establish and what remains open

[P-paper] classical finite abelian groups, Smith/Fitting ideals, exact cokernel sequence and integral wall congruence; [M after exact CI] original 6-row finite D563 local and inversion tests; [H] nontrivial *uniform* p-local valuation law for 700/full production rows and its connection to the four-fiber analytic entropy; [R] monotonicity of Gram p-adic divisibility under addition of real-PSD observation layers. The NEXT theorem target is a quantitative comparison of (a) decreasing evaluation index and (b) changing primitive restricted trace-pairing radical, with original prime factors counted once. The paper itself does not prove this proposed new quantitative comparison.
