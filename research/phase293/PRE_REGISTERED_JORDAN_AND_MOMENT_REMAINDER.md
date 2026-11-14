# Phase293 — preregister the missing unit-square-class test before measurement

**2026-11-12. This file precedes ALL new Phase293 code and test results.** Stacked DRAFT branch on Phase292 #183, which is stacked on Phase291 #182. No Work mode, no merge and no change to the actual-field theorem PR #157.

## Current frozen evidence and the new question

Phase292 source-exact CI established (but NOT human-reviewed) that the full ORIGINAL D583 725x3830 ordinary-Z-jet source and the **row-restricted diagnostic** consisting of the FIRST 725 original D587 rows with the full Q383/J5 source have **identical** p5 secondary source Smith exponents `{0:625,4:10,5:20,6:70}` (index560), and primitive original-metric Gram exponents `{0:690,1:35}` (residual valuation35). Their determinant valuations are each 3855. The ORIGINAL FULL D587 n730 has valuation3924 and MUST NOT be confused with the row restriction. Old inert Frobenius F5=1350 on both tested 725-row systems, counted only once.

**Question:** do the primitive trace pairing lattices agree as *quadratic/symmetric bilinear lattices over Z5*, and, independently, can any equality of such abstract invariants be strengthened to a source-preserving moving-frame square?

Smith levels alone do NOT classify quadratic lattices. For **odd p=5**, a nondegenerate symmetric integral p-adic lattice admits an orthogonal Jordan decomposition `L = ⊥_e 5^e U_e` with each U_e unimodular. Its local isometry class is determined by `(rank U_e, Legendre(det U_e mod5))` for each exponent e. We will test these *graded signs*, in BOTH central-inversion row parities. Sources: [Magma pAdicJordanDecomposition](https://docs.magma-maths.org/LatticesQuadraticForms/Lattices/genus.html), [Peters, Quadratic Forms, §10.2](https://www-fourier.univ-grenoble-alpes.fr/~peters/Books/QuadraticForms/QuadForms.pdf). These are classical mathematical tools; no novelty is claimed.

## Source/oracle fixed BEFORE results

- D583 and D587 each have the SAME literal centered original Q383, rho53, J=S=5, y-layer count (43,95,107,95,43), and first 725 monomial row labels `(r,s), 0<=r<145, 0<=s<5`. However `D583` is the entire original 725-row source, while `D587[:725]` is ONLY a diagnostic slice of its original 730-row source.
- Original finite trace metric `B_D=diag(2,2D)` at EVERY original j0..4 ordinary Z-jet and q point; W is held fixed, no Hasse jets or Gaussian weights, original 3830 observation channels preserved.
- Fix p5 inert and secondary source Smith K9, so prior max source e6 permits exactly primitive `H mod125`. Both systems must reproduce source profile `{0:625,4:10,5:20,6:70}`, original fixed 725-row rank 725 after saturation, primitive `H mod125` profile `{0:690,1:35,2:0,>=3:0}`; no changes to source or post-result precision.
- Freeze Phase292-A source builder blob `9216de10f311cf301413de663738804b5fbec203`, Phase292-B diagnostic oracle blob `eaa5d2ca3bf5833285cad062110cd612adb1cbb3`, original Phase206 helper `3f954b59d9f86b06ad53667c869b5b24f2e6c7f6`, original Phase204 jet `dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8`, independent Phase281 `d28b1420a371ca3a8a0297a19ecec75feedfc978`.

## Experiment A: exact small trace-moment remainder [predicted algebraically]

For row Z=(r,s)=(1,0), original J>=2 has only j0,j1. With Q the exact common 383-point ORIGINAL support,

`G_D(Z,Z) = 2 sum_Q(x² + D y²) + 2|Q|`.

Because `sum_Q y²=2*95 + 8*43=534`, the identity-row-frame difference is exactly

`G_587(Z,Z)-G_583(Z,Z)=2*(587−583)*534=4272 ≡ 2 mod5`.

This immediately disproves equality of the two full same-row-label Grams modulo5 in the identity frame, **without** disproving a nontrivial congruence.

The local unramified order isometry `phi: u587 -> alpha*u583` has `alpha=2 mod5, 17 mod25, 67 mod125`, with `alpha²*583=587` modulo the respective power. On the SAME six frozen original monomial labels `I=((0,0),(1,0),(2,0),(1,1),(4,0),(4,1))`, test the EXACT ORIGINAL jet Gram relation:
`G_587(Q) ≡ G_583(phi(Q)) mod 5^k`, `k=1,2,3`;
and `G_587(Q) NOT ≡ G_583(Q) mod5`.
The transformed `phi(Q)` is a **formal Z5 observation support**, not the real integer ellipse used by the D583 field theorem. Recheck all 383 original y points and the previously measured 104-point residue-support escape. No claim that `phi(Q)=Q` over Z5.

Define the signed moment-matrix defect `R_k=G_583(phi(Q))−G_583(Q) mod 5^k`. The identity `G587(Q)−G583(Q)=R_k` is a rigorous *typed remainder*, not a PSD observation increment or an extra prime valuation.

## Experiment B: genuine odd-p Jordan symbols, with outcome unknown

For EACH of these two 725-row systems separately:

1. Split the original 725 row labels into even `r+s` 363 and odd 362, a Z5-integral direct sum; **never** use a binary `(I±T)/2` projector. Keep ALL 3830 original observation columns and original B, and verify every row's central inversion covariance modulo25.
2. Saturate each parity sector independently using the preexisting Phase292 K9 source Smith, tracking ONLY original row operations. Require all levels <9, reconstruct `Cprim125` in original observation columns, rank = n_sector mod5, original trace-metric `H_sector=Cprim125 B_D Cprim125^T mod125`. Source index, old F and primitive H grade histograms for two sectors must combine to the known full results. All primitive even×odd pairings must vanish modulo125.
3. Implement an **independent symmetric congruence algorithm** over Z/125 using minimum-valuation pivots and, if necessary, a pair sum `e_i+e_j` to expose a diagonal unit when p is odd. It must remove cross entries by SIMULTANEOUS row and column shears, never Smith-only independent left/right operations. For every pivot, store `(e, u mod5)` where diagonal entry is `5^e u`. Return the grade histogram and Legendre sign of the UNIT determinant for each e. Reproduce the original Phase281 K3 Smith histogram exactly.
4. Before running on the source, check hostile toys: `<1>` and `<2>` have identical p5 Smith valuations but opposite Legendre determinant signs (2 non-square mod5); a symmetric OFF-DIAGONAL unit block [[0,1],[1,0]] must be diagonalizable for p odd; a fixed unimodular symmetric congruence shear must preserve all grade ranks and signs. Check a second shear on an actual parity-sector H.
5. DO NOT preregister which of the two source Jordan grade signs match. If different, **no parity-equivariant integral p5 isometry exists between their primitive pairings**; if their combined *ungraded* signs differ, no unrestricted p5 primitive-pairing isometry exists either. If all signs agree, the standard odd-p classification gives existence of an **abstract Z5 pairing isometry**, still NOT a source-compatible observation/row transport. Record exactly which conclusion holds; either result is useful.
6. A Jordan pairing isometry must NOT be applied to the raw, unnormalized original lattice as though OLD Frobenius factors or SECONDARY Smith index vanished; no new `v5` factor is earned. The change of discriminant alters the underlying field and B; only typed maps may be compared.

## Stop and promotion rules

STOP on any changed source hash, Q/jet/row mismatch, wrong local alpha, false 4272 identity, expected original-K9 history mismatch, rank/Smith inconsistency, parity cross-term mismatch, invalid symmetric-congruence toy or non-invariance under an elementary congruence shear. If the new Jordan comparison differs from intuition, preserve the outcome rather than choose another prime, basis, D, or precision.

**[P-classical]** odd-p Jordan classification, local quadratic-order isometry under `alpha`, explicit Z-row moment and congruence identities.
**[M once CI passes]** actual 363+362-dimensional primitive Jordan grades and transport remainder at finite D583/D587.
**[H]** source-preserving row/observation intertwiner, uniform many-D bound, number-field class-one implication.
**[R]** any implicit claim that equal Smith valuations alone force integral quadratic isometry, or that a p-adic local field isometry preserves the literal Q without a remainder.
