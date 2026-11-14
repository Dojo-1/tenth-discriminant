# Phase290-D: preregister the rank-one primitive-pairing orbit witness

**12 November 2026; AFTER Phase290-C gradient CI PASS [#43256792781](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43256792781), BEFORE this new code.** C already measured all 37 orbit directions p-unit for p5, and 32/37 for p7. Those counts are historical **regression targets**, not prospective predictions. The aim of this additional test is a cheaper, different exact oracle applicable to a large original source if the prime-local kernel corank remains one. Independent human review is absent.

Keep original D563 rho51, R140/S=J5/Q359, full original 700 polynomial rows **unchanged**, but test only the six frozen Phase290 labels (0,0),(1,0),(2,0),(1,1),(4,0),(4,1). Qminus285, DeltaQ74, 37 inversion orbits, original ordinary Z jets and metric 2,2D. No basis/prime/source/row/derivative mutation is authorized.

## Classical rank-one adjugate lemma [P-paper]

Let p be a prime and G in M_n(Z) symmetric, with rank(G mod p)=n-1. For a nonzero v in ker(G mod p), the adjugate is nonzero of rank 1 and satisfies
  adj(G) mod p = gamma * v*v^T
for some uniquely defined gamma in Fp^× relative to that chosen v. Proof: G adj(G)=det(G)I=0 modp, so all columns of adj(G) lie in the 1D kernel; symmetry forces the outer product; rank n-1 guarantees some (n-1)-minor is nonzero. Choose the first i with v_i !=0 and set gamma=cofactor_ii * (v_i^2)^(-1) modp. Check the identity coefficientwise, not just at the determinant level.

For an inversion-symmetric added orbit O with exactly the ORIGINAL integral jet matrix E_O and metric B_O, set G_O=E_O B_O E_O^T. The wall directional derivative at the FULL original source obeys

  d_O = tr(adj(G)G_O)
      = gamma * v^T G_O v
      = gamma * (E_O^T v)^T B_O (E_O^T v)  mod p.

Thus, for p odd and gamma unit, d_O !=0 iff the **primitive null evaluation** has nonzero B_O self-pairing modulo p. This is an exact carrier-to-readout theorem that avoids a full adjugate in order to identify active directions (gamma only needed to recover the numerical derivative). It does NOT claim a nonzero B-self-pairing for every nonzero E_O^T v; finite fields permit isotropic vectors.

## Frozen tests

1. Import the already verified original six-row G from Phase290-A, the separate modular null vectors p5/p7 from Phase290-B, and 37 complete inversion-orbit source lists from Phase290-C. Check rank(G modp)=5, v≠0, Gv=0 modp; the p5 radical is in odd row parity, p7 in even row parity. Do not use p2 parity projectors; 2 is not a unit over Z2.
2. Independently compute the single diagonal 5x5 cofactor gamma and compare ALL 36 entries of adj(G) mod p to gamma vv^T. Require gamma nonzero.
3. For every orbit independently compute column contraction s=E_O^T v by **original ordinary jets**, and q_O=Σ_w B_w s_w² modp WITHOUT building the orbit Gram. Compare gamma*q_O to the separately computed full-adjugate d_O from Phase290-C for all 37 directions and both primes.
4. Historical count controls: 37/37 nonzero q_O for p5, 32/37 for p7. Keep the lexicographic first nonzero representative and local prime residues from prior CI, but do not fit a new numerical threshold.
5. No full n700 null vector or matrix cofactor is computed. The next [H] frontier is to develop an efficient *full-source* p-local kernel extraction after already-counted Frobenius factors, and find enough p-unit inversion-orbit bilinear witnesses across production-parameter wall strata to bound a determinant-locus contact order. Nothing here adds prime valuation to PR157 or proves a field cutoff.

STOP if a single cofactor, rank, source contract, bilinear identity, historical count or counterfactual null evaluation fails. A successful self-authored CI is [M], not independent mathematical review.
