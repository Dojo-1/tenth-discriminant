# Phase294 — exact 5-adic observation-debt tower and original trace-moment localization

**12 November 2026, post-result evidence ledger.** AI-authored paper proofs and source-exact GitHub Actions; internal checks are not independent human mathematical review. This is a DRAFT stacked on Phase293 #184, Phase292 #183, Phase291 #182. Original number-field source helpers and actual-field candidate PR #157 are unchanged.

## Precise mathematical carriers: original field source versus formal moved support

At p=5, original D583 has rho53, R145,S=J5, full integer ellipse Q383 with y-layer counts (43,95,107,95,43) and 725 original monomial rows. Original D587 has rho53, R146,S=J5, the **same literal Q383** and 730 original monomial rows. We do not identify their row lattices. The previous same-first-725-row D587 was a **diagnostic only**. Original trace Gram uses all j0..4 ordinary Z-jets with W held fixed, and the exact real/imag trace metric diag(2,2D), not an arbitrary Gaussian or a rescaled lattice.

The local quadratic ring isometry `phi: A_587 -> A_583` maps `u587 -> alpha*u583` and `583 alpha²=587` in Z5, with the root branch `alpha≡2 mod5`. Both alpha and -alpha are allowed, and Q is symmetric under y->-y. Hensel lifting to **5^13** is exact: first residues alpha 2 mod5,17 mod25,67 mod125; at k13 alpha=647814942 mod1220703125. The 5^13 cap is the conservative source-numerator precision of the prior K9 secondary plus maximum OLD Frobenius k4, not a new mathematical source.

`phi Q` is a FORMAL p-adic observation set used to test compatibility. Replacing Q by phi Q is not authorized in the actual-field original Gram construction.

## A universal elementary theorem [P-paper, not a new mathematical novelty claim]

For two equal-size finite multisets A,B in a residue space U, let a(z),b(z) be their multiplicities. The maximum matching constrained to equal-residue pairs is

```
 M(A,B) = sum_z min(a(z),b(z)).
```

Proof: each residue fiber supports at most min(a,b) pairs, and pairing arbitrary labels fiber-by-fiber attains that upper bound. Thus the minimum unmatched count on **EACH side** is

```
 d(A,B) = |A| - M(A,B)
        = (1/2) sum_z |a(z)-b(z)|.
```

The common upper envelope max(a(z),b(z)) is the smallest residue multiset containing both, with size `|A|+d`. One must **add d points to each side**, not d total, to make both multisets equal at that fixed precision. The resulting enlarged source is not the original field source.

If U_{k+1}->U_k is residue reduction, every level-(k+1) matching induces a level-k matching. Therefore `M_(k+1)<=M_k`, equivalently `d_(k+1)>=d_k`. This is a **filtration of point/observation-label compatibility**, not of Gram determinant valuations, sheaf cohomology or arithmetic mass.

## Exact test: permanent depth-two loss of 276 observation points [P-paper + M]

Let `A_k=Q583 mod5^k`, `B_k=phi(Q587) mod5^k`, both as *point residue multisets*. [Phase294-A exact CI #43304251502](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43304251502) verified all 13 exact Hensel roots, all residue Counter identities and the explicit independent bipartite maximum-match oracles at k=1,2,3. The result:

| depth k | maximum matching M_k | unmatched per side d_k | smallest common upper envelope |
|---|---:|---:|---:|
| 1 (mod5) | 279 | **104** | 487 |
| 2 (mod25) | 107 | **276** | 659 |
| 3 (mod125) | 107 | **276** | 659 |
| 4 through 13 | 107 | **276** | 659 |

At k1 the 104 is the earlier Phase293 observation support imbalance, rederived as a multiset maximum matching rather than a literal set-intersection count. At k2, `alpha≡17 mod25` sends original nonzero y∈{±1,±2} to {8,9,16,17} modulo25, disjoint from original {1,2,23,24}. Only y0 survives: exactly 107 point labels. Reduction then proves **d_k=276 for all k>=2**, beyond the 13 computationally replayed levels. The second square-root branch -alpha has the same debt due to original y-symmetry. Original J5 and two trace coordinates mean unmatched coordinate-channel counts **per side** 1040 at level1 and 2760 at level2+, but these counts are NOT ranks or determinant factors.

The k1-to-k2 refinement destroys **172 additional possible point matches**. Hostile controls: trivial alpha±1 give zero debt; centerline-only support 107 always matches under any alpha; a full 5x5 residue-square toy has `d1=0` but `d2=20` for the same nontrivial root, so even a PERFECT mod5 residue support match need not survive to mod25.

## Exact 6x6 signed original-jet remainder [P-paper + M]

Fix original polynomial row labels `I=[(0,0),(1,0),(2,0),(1,1),(4,0),(4,1)]` and all FIVE original ordinary Z-jets, both trace coordinates.

For any formal p-adic point q, define its original field D583 local six-by-six trace matrix
```
 K_583(q) = sum_{j=0}^4 E_{j,q} diag(2,1166) E_{j,q}^T.
```
Here E is the exact integer-polynomial original jet evaluation and all operations occur over Z5 (or modulo a fixed power); this is a symmetric **local Gram**. The field ring isometry and trace identity imply `G587(Q) = G583(phi Q)` over Z5, in common six original monomial row labels. When q from Q and q' from phiQ agree modulo5^k, their polynomial raw original jets E and their K matrices agree modulo5^k. Hence any maximal residue matching cancels those terms modulo5^k, giving the exact entire signed remainder

```
 G587(Q) - G583(Q)
  = sum_{q' in unmatched(phiQ)} K583(q')
    - sum_{q in unmatched(Q)} K583(q)
    (mod 5^k).
```

[Phase294-B original six-row CI #43304251432](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43304251432) compared this **ALL 36 entries** at k1,2,3 against the existing Phase206 exact mixed-moment Gram on full ORIGINAL Q, and checked each matched original jet and independent single-point trace-Gram oracles. Result:

| original matrix modulus | unmatched signed local matrices from Q | unmatched signed local matrices from phiQ | total |
|---|---:|---:|---:|
| 5 | 104 | 104 | 208 |
| 25 | 276 | 276 | 552 |
| 125 | 276 | 276 | 552 |

The original six-by-six identity-frame Gram difference still has rank **5 mod5**, and for the original Z row diagonal is exactly `G587(Z,Z)-G583(Z,Z)=4272`. The localized remainder is a **signed difference** of positive local contributions and is NOT positive semidefinite in general. We do not infer v_p(det G), a Schur monotonicity law, or extra rank from these counts. At most, the result gives a rigorous finite-support localization of the original raw moment discrepancy within a *particular geometric field-value map*.

## The crucial normalization barrier [P-paper + M code]

The admissible old p5 row basis contains the divided Frobenius polynomial `f(Z,W)=(Z^5-W)/5`. On ORIGINAL sampled points q=(0,0) and q'=(5,0) with W=Z on the real axis:

```
 f(q)=0,       f(q')=(5^5-5)/5=624 ≡ 4 mod5,
 q ≡ q' mod5.
```

Both original points are in Q383. Thus **raw polynomial/ordinary-jet matching modulo5 DOES NOT imply matching the divided or fully primitive source even modulo5**. A general safe congruence lemma is: if integer jets P(q)≡P(q') mod p^(a+ell) and each value is divisible by p^a, then their quotients `P(q)/p^a` and `P(q')/p^a` agree modulo p^ell. Without the extra a digits, quotient transport is unjustified.

For our already-known D583/D587-first725 source K9 normalization, `max old k=4` and `max secondary e=6`. Therefore matching FULL original point coordinates to the conservative depth `p^(4+6+3)=p^13` would be sufficient to transport all primitive rows modulo125 under source-compatible maps, *if there were such a complete matching*. The source has **d13=276** point-fiber debt; there is not. This does NOT prove a different, more general observation-side orthogonal Y cannot exist, nor prove point matching to p13 necessary for every individual row.

## Epistemic and architectural boundary

[P-paper] elementary matching/minimum-completion and monotonicity, 25-adic transverse obstruction, raw polynomial-jet congruence, signed matrix remainder localization, division precision lemma.

[M] original Q383 and two local field structures, exact Hensel k1..13, independent matching, k1..3 exact all-36-entry raw Gram moment checks, hostile controls, pinned GitHub Actions receipts. The paper proofs were AI-authored and the tests share source helpers; independent mathematical assessment is pending.

[H] a categorical source-compatible observation map permitting point movements/controlled jet mixing, with an explicit lattice/index debt and legitimate primitive pairing extension; the uniform h1-admissible tenth-discriminant implication.

[R] interpreting `d_k` as a 5-adic determinant valuation, claiming fixed mod5 sample matches transport Frobenius-divided jets, calling formal phiQ a new valid original field source, or extrapolating the finite D583/587 matched-source diagnostics to uniform h1 arithmetic.

**Next smallest theorem/experiment:** Specify a *restricted* observation transport group whose morphisms preserve (1) the original point/jet indexing category, (2) the quadratic-order value form, (3) the old and secondary source lattice quotients. Prove a correction bound for the raw trace-Gram remainder in terms of unmatched local moment tensors **without** a monotonic determinant claim, and test whether any genuine production h1 source satisfies the hypotheses. A freely chosen dense B-orthogonal observation isometry is not a substitute for an original-sampler morphism.

No Work mode, no PR157 edits, no merge into main.
