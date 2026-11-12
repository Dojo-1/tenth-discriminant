# Phase285 — Noetherian disk-lens and finite-theta moment bridge

**Evidence/provenance**: 12 November 2026. This protocol freezes the scope and stop rules before committing the Phase285 CI program. The D19 two-row toy numbers were already discussed in the supplied research note; the D403 16-row minor's initial arithmetic was explored locally **before** this document. These numerical expectations are therefore retrospective regression targets, NOT blind prospective discoveries. The program and documentation are AI-authored, pending independent mathematical review. No claim about a tenth unknown class-number-one field, Siegel zero exclusion or an improved 321^4 bound.

## Immutable source and tests

- Original quadratic order Lambda_D = Z[u], u^2=-D, with original integer coordinates (x,y), Z=x+yu, W=x-yu, original **ordinary** Z derivatives holding W fixed, and trace-pairing weights **(2,2D)** on real/imaginary evaluation channels. D403 parameters from unchanged source helper: rho40, R100, S=J4, Q219, 400 original monomial rows, 1752 original observation columns. Freeze `research/phase206/source_probe.py` blob `3f954b59d9f86b06ad53667c869b5b24f2e6c7f6` and original integer-jet oracle `research/phase204/ordinary_jet_filtration.py` blob `dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8`.
- Read-only geometry: Q0(D,rho) = {(x,y) in Z^2: x^2+Dy^2 <= rho^2}; symmetric lens Qlens = Q0 intersect {(x-1)^2+Dy^2 <= rho^2} intersect {(x+1)^2+Dy^2 <= rho^2}; **asymmetric wrong-symmetry comparator** Qplus = Q0 intersect {(x-1)^2+Dy^2 <= rho^2}. Do NOT silently replace Q0 by Qlens in the proven original-Gram field bound.
- D19 pilot **only**: rho5, rows (0,0),(1,0), J1; Q0 has 21 points, Qlens 15, Qplus 18. D403 pilot: rho40 and exact ORIGINAL sample Q0 from helper, Qlens has 213 points, Qplus 216. The D403 numerical Gram comparisons use only the **16-row principal submatrix** with (r,s) in {0,1,2,3}x{0,1,2,3} of the genuine original R100,S4,J4 rows. These are NOT full-400-row determinants, Smith valuations or bounds.

## Mathematics to test (paper-level derivations, not external review)

1. **Noether C2 parity**: Under central inversion z -> -z, the j-th ordinary jet of Z^rW^s has sign (-1)^(r+s-j). If Q=-Q, each original trace-Gram cross entry between opposite monomial parities cancels pointwise in pairs. In integral monomial order, the exact even/odd block decomposition follows via an INTEGER row permutation; no (I +/- P)/2 projector and no division by two. For the entire 400-row original D403 rectangle, this is a universal identity, even though CI evaluates only a 16-row principal minor.
2. **Odd-prime integral Frobenius grading**: The already-established source change P_(r,s) = Z^(r-pk)W^s(Z^p-W)^k, with k=min(floor(r/p),S-1-s), is homogeneous in total degree modulo two when p is ODD, since every expanded term has parity r+s-(p-1)h. Verify all original 400 rows and primes 3,5,7. The p=2 analogous parity argument fails; do not use denominators 1/2 or promise 2-adic parity decomposition by projectors.
3. **Finite-theta moment identity**: For Q finite, define Theta_Q(t,xi,eta)=sum_{z in Q} exp(-t N(z)+xi z+eta conj(z)). Its derivatives at (t,xi,eta)=(0,0,0) yield mixed moments M(a,b)=sum_{z in Q} z^a conj(z)^b, with original Gram entry

   G_(r,s),(r',s') = 2 * sum_(j=0)^(J-1) (r)_j (r')_j * Re M(r-j+s',s+r'-j),

   omitting j>r or j>r'. Compare EVERY entry of the exact original weighted-trace Gram of the selected 16-row submatrix against independently computed integer pair moments. For centrally symmetric Q, all moments of odd total degree vanish, yielding the block zeros.
4. **Loewner deletion**: G(Q0)-G(Qlens)=G(Q0\Qlens) positive semidefinite, because Qlens is a subset of Q0 and every point adds a positive-semidefinite original-jets Gram. If a selected Gram is positive definite, determinant decreases (weakly) with deletion; do not infer monotonicity of p-adic valuations. Numerically check exact matrix equality, positivity of the 16-row determinants and strict determinant reduction.
5. **Maximal-order boundary**: For D=19,403 (both 3 mod4), the full maximal order is O_K = Z[u] union ((1+u)/2 + Z[u]), a second disjoint coset. The original Q moments are NOT full maximal-order theta moments; any future Mellin/L-function theorem requires the missing coset, nonzero-element convention, Gaussian cutoff and a rigorous tail estimate. No such theorem is inferred in this finite pilot.

## Frozen checks / expected reproducibility receipts

- D19 J1 rows 1,Z with Q0: G=diag(42,640), det=26880, v2=8; symmetric lens: G=diag(30,356), det=10680, v2=3; asymmetric Qplus: G=[[36,18],[18,498]], det=17604 with nonzero cross-parity terms. All are independently hand-checkable finite integer statements supplied/explored before registration.
- D403 16-row submatrix: both symmetric Q0 and Qlens must have exactly ZERO even-odd cross entries; Qplus must have nonzero parity cross entries. Exact determinant factorizations into even/odd blocks must match. Expected small-minor valuations from local exploratory computation (not blind): original (v2,v3,v5,v7,v11)=(56,7,1,1,0); symmetric lens (56,7,0,1,0); asymmetric (80,7,0,0,2). These are **NOT** the 400-row original-Gram valuations established elsewhere.
- Verify every original source point, exact integer norm inequalities, monotone inclusion, deterministic sample ordering, source blob IDs and every original jet up through j=3. Verify exact pairwise moments, selected-minor Gram entries and a nontrivial strict same-parity pair correlation for a selected-block Schur/Hadamard comparator; do not claim a global analytic upper improvement.
- Stop if a source constraint, count, original coordinate/derivative, moment equality, parity decomposition, metric, determinant relation or D19 control fails. Never change observed expected values post hoc to pass CI. Pin the Python environment and cap runtime 10 minutes. Keep CI separately tracked.

## Evidence and implication scope

[P-paper] finite symmetry/jet parity and moment identity with explicit hypotheses; [M after successful CI] source-exact D19 and original-D403-**minor** regression; [R] assumption that lens determinant decrease implies a new p-adic divisor or improved analytic constant; [H] obtaining a useful full-400-blockwise analytic bound and connecting finite/angular moments to maximal-order Gaussian theta and Mellin data with explicit tail errors.

The 321^4 source-to-field theorem PR157, semantic review #50, and other previous PRs remain separate. No Phase285 merge until exact-head focused, Markdown and whole-root Lean checks complete, plus review of source correspondence.
