# Phase310-B — post-A, pre-code full split-prime DVR/Smith comparison

Date: 2026-11-13. A's original-source 100×1052 reconstruction, whole-source conjugation mirror, ranks (12,12), Gram rank12, and hostile controls have PASSED hosted CI. The present **B protocol is a separate post-result follow-up written before B code**. Do not backdate its hypothesis to Phase310-A.

## Proposed exact theorem, no conjectural novelty

For a quadratic order O and a conjugation-stable set Q of original observations, the ORIGINAL coefficientwise conjugation law gives X_(r') = X_r P_tau at every p-adic precision p^k, when r and r' are the two coherent Hensel roots at a split rational prime p. P_tau is a permutation of the same original (jet,point) columns, so the local evaluation maps have EXACTLY THE SAME Smith invariant factors over the unramified/local DVR Z_p. This statement is representation-level arithmetic, not a field-discriminant bound.

The original Hermitian trace Gram is the cross pairing

    G = X_r X_r'^T + X_r' X_r^T
      = 2 X_r P_tau X_r^T  (mod p^k).

The rank12 of both X_r and G modulo3 in A establishes at first level that **ker(G mod3)=ker(X_r mod3)**, because ker(X_r) ⊆ ker(G) and both have dimension88. Thus the first-level Gram radical is exactly the source-evaluation kernel, not an additional restricted-trace radical on its 12-dimensional image. Contrast the existing D203/p5 inert examples, where trace restriction can have its own radical.

## Preregistered bounded exact computation

Freeze D203, p3 split, original Q263, original R50/S=J2, all original 100×1052 omega coefficients. Use K=10, p^K=59049, separately reconstructed original E (same frozen source policy).

- Construct the unique Hensel roots r_k and 1-r_k modulo 3^k, k=1..10. Check ring relation at each k.
- Verify **ALL 52,600 original source coefficients** under both local ring maps satisfy X1=X0 P_tau modulo 59049, then verify all 10,000 cells of original trace G modulo59049.
- Implement a DVR modular Smith routine for rectangular matrices by choosing the smallest p-adic valuation pivot and doing exact invertible row/column operations, with every pivot elimination checked. Its output is an exact exponent histogram for levels < K and explicitly CENSORED at ≥K; never report censored factors as zero or exact.
- Hostile controls: diagonal known answers [0,1,2,4], same matrix after nontrivial unimodular row/column shears, zero matrix, local root1 reconstructed as 1-root0, source-coordinate permutation, wrong-root and nonsplit-prime rejections.
- Compute the two local original-source Smith profiles and the original integer trace Gram profile at precision K. Compare all profiles, rank mod3, v3 determinant bounds, and separately report any residual source-versus-trace depth.
- If all 100 exponents resolved <K for G and X, compute exact local source index log3 and original v3(det G), then define residual R = v3(det G)-2*v3(local source index). Assert R≥0 and report it. If not all exponents resolved, report intervals/censored levels and DO NOT compute a fake exact residual.

## Semantic guard

If the local Smith profiles agree, this is a true *balanced split-prime* transport. It suggests the p-local **conjugate valuation contributions** from the whole original source are equal, but **does not compute the entire global Fitting ideal** or imply global Picard principality. Do not replace the original integer trace Gram with a new Hermitian form. Do not add this source-level weight to existing valuationWeight without checking overlap. The field D203 is non-h1; the bound 322^4 stays unchanged.

## Stop/kill conditions

One failed Hensel root, incorrect source evaluation, wrong Gram congruence, invalid DVR algorithm on tiny known cases, or an unreported ≥K censoring count retires the stronger Smith interpretation. Reject any claim of novelty or general intelligence from the algebraic picture. Keep draft, no main merge.
