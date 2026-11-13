# Phase310 — full-source split-embedding mirror experiment (frozen before code)

Date: 2026-11-13. Research-branch parent: Phase309 PR #201 head 9fa55074143ea9f31cbd9fa77938ae3eb1543ed7. This document is written BEFORE new Phase310 implementation or hosted measurements. Parent Phase309 local patch results are [M] with focused CI; the whole-root Lean result must be checked separately. All PRs remain research-branch scoped and none of these experiments changes the original main-field cutoff 322^4.

## Actual source, first (no artificial Picard source)

Use the exact Phase304 original maximal-order D203 data: rho24, R50, S=J2, full norm-ball Q263, original 100 polynomial rows (r,s) sorted r-major, s-minor, and both ORIGINAL ordinary Z-derivative jets j0,j1. The original ring is O=Z[omega] with omega^2=omega-51. The original 100×1052 ω-coordinate evaluation E is frozen and independently reconstructible via Phase307's different exact ring evaluator. Compare ALL 105,200 raw modular coordinates at modulus 3^3 before examining any split embedding.

At rational p=3, f(T)=T^2-T+51 splits at simple roots r0=0 and r1=1. Write C0 and C1 for the two different residue-field projections O/3O ≅ F3×F3, and X0, X1 for the 100×526 evaluations over F3. The 263-point source ball is invariant under actual quadratic conjugation τ(a,b)=(a+b,-b).

## Predeclared exact theorem targets [P-paper candidates]

1. **Full original-source conjugation mirror:** For every row (r,s), jet j=0,1, and genuine Q point z,
   
       C1(E_row,j(z)) = C0(E_row,j(conjugate(z))).
   
   Thus X1 = X0 P_tau, where P_tau is a genuine involutive permutation of ALL 526 (jet,observation) coordinates. It is not a 2D Euclidean projection and needs no hypothetical quantum coherence.

2. **Actual trace as cross pairing:** For all rows, the ORIGINAL integer Hermitian trace Gram mod3 is

       G = X0 X1^T + X1 X0^T = 2 X0 P_tau X0^T  (mod 3).

   Consequently rank_F3(G) <= rank_F3(X0). Prove that the columns are genuinely permuted; the matrix P_tau is involutive and symmetric, not an arbitrary gauge. Verify every one of the 10,000 Gram cells against the original frozen source's independent Gram code.

3. **Jet quotient source rank bound:** In F3[x], the ordinary-jet kernel (x^3-x)^2 has degree 6. Since our source has S=2 monomials in the independent conjugate residue y and R=50 in x, every original source row Z^r W^s modulo3 is a linear combination of the first 12 rows r=0..5,s=0,1, in the *ordinary j0/j1 evaluation* at EVERY genuine point. Predeclare the upper bound rank(X0)<=12 and the independent lower-bound test rank of those 12 actual rows =12 if the 9 residue pairs (x,y) are all represented among Q263. Predicted rank(X0)=rank(X1)=12. The precise rank of G is UNKNOWN until measured; do NOT predeclare that G is nondegenerate on the 12-dimensional source image.

4. **No automatic extra source mass:** The field D203 has class number4 and p3 splits, so any observed Gram rank deficiency is not a class-number-one theorem. If det G over integers is nonzero, rank_F3(G)=r gives the elementary valuation lower bound v3(det G)>=100-r; this cannot be added to an overlapping weight or transported to inert-prime arguments without proof.

## Hostile independent controls (must fail appropriately)

- Remove a point whose conjugate no longer belongs to Q; the 263-point permutation no longer exists. The map may still have a cross trace at each point, but the **mirror permutation factorization** is invalid, so do not apply its rank bound.
- Wrong same-embedding trace x0*y0+x1*y1 must fail on explicit ring element omega with x=y=omega, p3 roots0 and1. This checks real Hermitian conjugation, not a syntax-level test.
- Reject p5 as a *split* prime in D203 (f has no F5 root).
- Reject fake source parameters / fake 100×526 shape; verify all 105,200 E entries using a separate Phase307 arithmetic code path. Do NOT silently treat F3 local source rank as O or Z row rank at a different prime.
- Verify the directly computed Frobenius quotient basis and its ordinary derivatives at each residue x; do not rely exclusively on a black-box Gaussian rank.
- Trace source compile and unrelated whole-root Lean are separate checks. No main merge until properly reviewed.

## Decision

If the complete mirror identity and trace factorization hold, this is a verified **full-original-source arithmetic transport**. If the Gram rank is smaller than 12, describe its additional radical without calling it a new field bound. If any claimed source identity fails, retire it. No new Worldlet layer is permitted merely to explain away a failure; inspect original source/jet policy first.

Claim ledger: [P-paper] conditional conjugate residue and rank-factorization identity; [M after exact-head CI] 100×526 finite checks and modular ranks; [H] original-uniform h1 prime-mass improvement; [S] two local Worldlets under conjugation; [R] "local Picard class forces nonzero Gram v3".
