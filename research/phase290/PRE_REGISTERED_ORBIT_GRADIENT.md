# Phase290-C: preregister 37-orbit p-adic discriminant wall, after Phase290-B

**Date: 2026-11-12. Registered AFTER modular-lift and determinant-polynomial CI PASS [#43255880299](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43255880299), and BEFORE this additional 37-dimensional experiment.** The previously observed data are retrospective baselines: original D563 six-row Gplus has v5(det)=2 and v7(det)=1; the formal one-parameter f(t)=det(Gminus+t Delta) has f'(1)=4 mod5, 5 mod7, both nonzero. In the new experiment the orbit gradient counts and first nonzero orbit locations are UNKNOWN in advance, so report rather than fit them.

## Typed carrier and actual source

Unchanged original D563 rho51, R140/S=J5, Qplus359, Qminus285, DeltaQ74, six preregistered original monomial rows [(0,0),(1,0),(2,0),(1,1),(4,0),(4,1)], ordinary Z-jets j0..4, trace weights 2,2D, original frozen helper blobs from Phase290-A.

The 74 added outer points in y=±2 split into precisely **37 free orbits of the central inversion** q↦−q. Choose one representative per orbit using lexicographic minimum of (q,−q), and sort the representatives lexicographically once, prior to computing gradient. For x=0 the conjugation-complete orbit has 2 points; for each 1<=|x|<=18 there are 2 inversion orbits, together yielding 2+18*4=74 points. Membership thresholds are exact **micro-walls**
  rho² >= 4D+x²
for |x|<=18; do not collapse all 74 added points into the single wall rho²=4D. Each complete central-inversion orbit preserves the P parity on the original row module. We do NOT assert conjugation is a row automorphism of the rectangular ordinary-Z-jet space.

For orbit O_a, define G_a=E_{O_a}B_{O_a}E_{O_a}^T, a 6x6 positive-semidefinite INTEGER principal Gram. Then DeltaG=Σ_a G_a on the original six-row module. Let

  F(t_1,...,t_37)=det(Gminus+Σ_a t_a G_a)∈Z[t_1,...,t_37].

The original FULL source occurs exactly at vector 1=(1,...,1). All other real/p-adic parameter values are formal deformations of the observation weights, NOT other proven field sources nor an integral moving frame. The first-order orbit derivative is the exact integer
  d_a = (∂F/∂t_a)(1) = tr(adj(Gplus)*G_a)
computed via signed **5x5 cofactors** on the SAME original six-row Gplus. No inverse of a p-singular Gplus is required. Differentiation along the diagonal t_a=t gives

  Σ_a d_a = d/dt det(Gminus+t DeltaG)|t=1.

This equality must be checked EXACTLY against Phase290-B's separately implemented full 6x6 Leibniz determinant polynomial, including at p5/p7.

## Frozen controls, predictions and stop rules

1. All frozen source hashes, Q± counts, 37 orbit partition, row/jet/metric, symmetry and all exact micro-wall membership inequalities must pass. Reconstruct every G_a through **Phase206 mixed moments** and a second original ordinary-jet oracle, then verify ΣG_a=DeltaG.
2. Construct adjugate/cofactors over Z with exact 5x5 Bareiss determinants. Verify **Gplus * adj(Gplus) = det(Gplus) I6** and its transpose. Compute all d_a with no floats and no fitted orbit selection. Check Σ d_a equals the independent one-parameter f'(1) from Phase290-B **exactly**.
3. At p5/p7, require total derivative ≠0, already observed in Phase290-B. Therefore by the sum identity there is at least one orbit with d_a !=0 modp. Output counts, first witnesses, and their exact x,y norm thresholds. Do NOT predict a favorable concentration or percentage of orbits, and do not choose a subset post-result to optimize an analytic bound.
4. The modp hypersurface has a p-unit partial derivative at the full-source point, so the classical p-adic implicit/Hensel lemma yields, **formally**, a local codimension-one smooth determinant-zero locus in Z_p^37 near vector1 (with other parameters fixed). The valuation depth of the original integer point on that local wall is p5² and p7 respectively. These are [P-paper] conditional on exact tests, but **NOT** evidence of a physical adiabatic evolution, an integral GL_Z moving gauge, a new prime factor in the unchanged field theorem, or a continuous source.
5. Include a negative control at p2: the observation ± eigenspace projector has an unavoidable factor 1/2, so the p5/p7 argument must not be exported to p2 without a separate integral proof. Include no factorization of the whole 700x700 Gram or field theorem.
6. Stop and report if any source mismatch, orbit overlap, conjugation-overclaim, incorrect adjugate identity, wrong f' comparison or falsely inferred local smoothness from a zero gradient occurs.

**Evidence:** [P-paper] orbit decomposition, Jacobi/adjugate polynomial identity, simple-root Hensel; [M after CI] frozen six-row 37-dimensional exact orbit gradient; [H] control of the actual full 700-row primitive pairing and its production-many-layer asymptotics; [R] identifying prime-local parameter weights with integral lattice symmetries or additional Smith mass. Independent mathematical review remains pending, draft PR only.
