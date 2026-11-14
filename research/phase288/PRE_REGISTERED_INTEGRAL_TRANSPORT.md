# Phase288 — preregistered symmetry-compatible integral transverse-to-original-Gram transport

**Registered 12 November 2026 BEFORE Phase288 executable implementation.** The construction is an AI-derived elementary integral shear/Schur-complement design, not externally reviewed new mathematics. User-directed goal: preserve Noether symmetry, a higher-dimensional transverse observable, the original ordinary-jet trace Gram AND its exact integral lattice, p-adic Smith factors and no-double-counting. Phase287's four-dimensional real/geometric model is conceptually upstream but remains a *separate draft*. Do not import a guessed Phase287 API, conflate the full maximal order with the original Z[u] source, or claim the smooth real/adiabatic gauge is integral at arbitrary angles.

## Immutable original sources and evidence scope

Read the existing original helper git blobs without editing:
- `research/phase206/source_probe.py` blob `3f954b59d9f86b06ad53667c869b5b24f2e6c7f6`, whose `params(D)` gives D283: `rho31,R70,S=J2,Q169` and D403: `rho40,R100,S=J4,Q219`.
- `research/phase204/ordinary_jet_filtration.py` blob `dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8`: original **ordinary** d_Z^j of Z^r W^s holding W fixed, returning signed integer-pair channels.

For each source define the unchanged original integer E with n=RS rows and 2J|Q| observation columns (j,z,re/im); Wdiag=diag(2,2D,2,2D,...) and G=E Wdiag E^T. This is the **original** trace-Gram, NOT a dyadically weighted/maximal-order theta Gram. All numerical determinant/Smith controls run on an exact 8-row original principal submatrix for D283 and a 16-row original principal submatrix for D403; all n original rows are checked for transverse-source covariance. DO NOT claim numeric full n x n determinant certification.

## Derived four-dimensional transverse moment and its source readout

For q=(x,y) in the original integer lattice Q, let
`delta(q)=x^2-D*y^2=Re(z^2)`, `nu(q)=x^2+D*y^2=N(z)`.
The unweighted 4-real-dimensional *product-source* angular contractions on QxQ are

`C0=sum_(q,w in Q) (xq*xw + D*yq*yw)^2`,
`C90=sum_(q,w in Q) D*(yq*xw-xq*yw)^2`.

Central inversion + conjugation symmetry of Q imply the mixed xy moment vanishes; let `A=sum_Q x^2`, `B=sum_Q D*y^2` and `T=A-B=sum_Q delta`. Then
`C0=A^2+B^2`, `C90=2AB`, `C0-C90=T^2>0`.
The original Gram, with constant source row 1 and labels Z² and ZW (both legal original labels), has
`g_(1,Z²)=2T`, `g_(1,ZW)=2(A+B)`.
Therefore the exact source-observable readout is
`4*(C0-C90)=g_(1,Z²)^2`.
This is a **source-faithful unweighted specialization of Phase287's angular identity**, NOT Phase287's weighted maximal-order/t=ln(2) observable. The missing half-coset and Gaussian weights have NOT silently been discarded; they remain a separately typed analytic remainder.

Frozen precomputed hand predictions (not blind discoveries): D283 Q169 T=15,638 and C0-C90=244,547,044; D403 Q219 T=43,406 and C0-C90=1,884,080,836. A failure invalidates the instance, not a reason to change the predictions retrospectively.

## Build an integral symmetry-typed readout

Let V be the integer m x 4 observation-channel matrix, supported **only on the original j=0 REAL channels**, with four functions of q:

`v_delta(q)=delta(q)` (even), `v_nu(q)=nu(q)` (even), `v_x(q)=x` (odd), `v_xdelta(q)=x*delta(q)` (odd).

All imaginary and j>0 channels are zero. Let `X=E Wdiag V` in Z^(n x 4). The exact constant-row readouts are `X_(1,delta)=g_(1,Z²)=2T`, `X_(1,nu)=g_(1,ZW)=2(A+B)`. Define P on original row r,s by (-1)^(r+s), and S=diag(1,1,-1,-1) on transverse channels. Since Q=-Q and v have the stated parity, **P X = X S**. Caution: source conjugation is NOT automatically a full source automorphism because the rectangular rows R x S and Z-only derivatives are not conjugation symmetric; only central inversion is claimed for the whole source.

## Exact integral transport theorem target [P-paper, to be independently reconstructed]

For arbitrary integral symmetric G (n x n), integer X (n x 4), define
`Gext=[[G+XX^T,X],[X^T,I4]]`.
Let `U=[[I_n,X],[0,I4]]` and `L=[[I_n,0],[-X^T,I4]]`. They lie in GL_(n+4)(Z), each determinant 1; indeed
`Gext=U * diag(G,I4) * U^T` and
`L^T Gext L=diag(G,I4)`.
The integral graph embedding `iota(v)=(v,-X^T*v)` is an ISOMETRIC embedding of original (Z^n,G) into the completed integral lattice; it is orthogonal to the vertical transverse Z^4. Its Schur complement along the transverse I4 block is precisely G. Thus
`coker(Gext) congruent to coker(G)` as abelian groups; no extra nontrivial Smith factors at ANY rational prime, and `det(Gext)=det(G)` exactly (also when singular). No additional 3/5/7/11 or 2-adic valuation units may be counted. This is an **integral stabilization**, not a new arithmetic class-number theorem.

With C2 acting as `Pext=diag(P,S)`, `P G P=G`, `P X S=X`, the full completion satisfies `Pext Gext Pext^T=Gext`, and the graph embedding is equivariant: `Pext*iota(v)=iota(Pv)`. This is the load-bearing Noether compatibility.

A secondary integral *moving-moving gauge* within even and odd transverse sectors is
`T=diag(T2,T2)`, `T2=[[1,1],[0,1]]` in GL4(Z), commuting with S. The frame-changed completion is
`Gext' = diag(I_n,T^T) Gext diag(I_n,T)`, with transverse block `T^T T` (NOT I unless T orthogonal) and cross block XT. The exact Schur complement is again G and its integral Smith factors are unchanged. At generic real angle, the smooth Phase287 R_phi is NOT an element of GL4(Z); it remains an analytic moving frame with an explicit transport remainder, not a continuous arithmetic unimodularity claim.

## Frozen falsifiers / low-cost numerical test

1. Verify frozen source hashes, both params and full Q, original ordinary jet evaluator, weights 2,2D, selected original source row labels and dimensions. Independent direct original signed-jet Gram oracle must agree with Phase206 `gram` on the 8-/16-row minors.
2. Compute ALL 140/400 source rows of X from cached exact integer monomials; independently replay selected rows from original `jet` at j0 and the explicit integer co-vectors V. Require P X = X S and nonzero even and odd readouts. Require X_(1,delta)=2T and X_(1,nu)=2(A+B), and exact source Gram cross entries.
3. Directly compute C0 and C90 with all 169²/219² original product pairs, separately compute A²+B² and 2AB, and verify source `4*(C0-C90)=g_(1,Z²)^2` and the frozen predictions. The separate missing half-coset/weighted Phase287 result MUST NOT be substituted.
4. For both selected original principal minors, build Gext and integer triangular U,L, verify exact integer matrix identities, determinant equality via fraction-free Bareiss, C2 invariance, graph isometry/orthogonality, and same local v_p(det) at p=2,3,5,7,11. Gext is an **n+4-dimensional** auxiliary presentation, not a newly sampled trace Gram. No extra p-adic units.
5. Apply the explicit nonorthogonal integral sector shear T with det1 and `T^T T != I`; verify transformed Gext' and Schur complement G exactly, and `coker` invariance by exhibited unimodular congruence. A wrong control that keeps transverse I while applying nonorthogonal T must FAIL the claimed gauge transformation (it would modify the completion and could create fake arithmetic mass).
6. The old GL_Q rather than GL_Z negative control: `diag(4,4)` and `diag(16,1)` have same det but different 2-adic Smith exponent multisets; smooth R_phi at generic phi is not a p-integral lattice gauge.
7. Compare against a tensor-product scalar/null control: the angular gap is completely determined by an original Gram entry (no new independent arithmetic data). The test must NEVER interpret this as extra valuation beyond the original Gram. Optionally report a strict two-row Hadamard-Fischer correction in the selected original minor, but do not claim global competitive analytic bound or universal cutoff.

STOP if any frozen prediction, source hash, coefficient identity, parity, integer congruence, determinant, Schur or wrong-gauge control fails; report it without rewriting the preregistration.

## Evidence and independence

[P-paper] elementary module/Schur identities with explicit types; [M after exact-head focused CI] finite Q283/Q403 source-observable checks and integral 8-/16-row presentations; [H] source-preserving *nontrivial* transverse arithmetic novelty, any uniform analytic strength or new valuation/lattice invariant that is not already in G; [R] belief that an isometric integral embedding itself creates fresh determinant mass. This deliberately solves the TRANSPORT/NO-DOUBLE-COUNTING problem but does **not** solve the arithmetic NEW-MASS problem. No field cutoff improvement, tenth field, or exceptional-zero theorem is claimed. Preserve PR157/issue#50 separate review obligations. Keep Phase288 DRAFT until focused, Markdown and Lean root CI pass and independent source-level review is satisfied.
