# Phase296-C — preregister thin-row polynomial automorphism rigidity and Frobenius ghost

**13 November 2026. Registered AFTER Phase296-A/B measured [A #43373033299](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43373033299), [B #43373303089](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43373303089), BEFORE Phase296-C executable.** Phase296-A initial failed CI asserted all nonmaximal residue multiplicities <=19 although three other y0 residues have21; corrected to21 without changing the two weight22 anchors. A separate POST-result regression corrects the mod5 norm-one REAL-translation minimum to72 (previously only a broad-family lower bound64); this is not preregistered evidence. Keep failed runs and original sources intact.

## Stronger well-posed theorem [P-paper, verification and novelty scope not yet independent]

Let k be ANY FIELD; R>S>=2, integer delta with `0<=delta<S-1`. Define the ORIGINAL rectangular formal monomial row space

```
  L_(R,S) = span_k { Z^r W^s : 0<=r<R, 0<=s<S } ⊂ k[Z,W].
```

**Thin-extension rigidity:** If `sigma∈Aut_k(k[Z,W])` and `sigma(L_(R,S)) ⊆ L_(R+delta,S)`, then **necessarily**

```
  sigma(Z)=aZ+b,    sigma(W)=cW+d,
  a,c∈k^×, b,d∈k.
```

Conversely all such diagonal affine automorphisms satisfy the inclusion. This is a theorem about FORMAL polynomial automorphisms and the ENTIRE original monomial lattice, not mere agreement on a finite set of evaluation points, not a symmetric Gram equivalence, and not a theorem about arbitrary infinite-dimensional neural-network weight-space maps.

**Proof skeleton, fixed before tests:**
1. Since `Z^(R-1)∈L`, `sigma(Z)^(R-1)∈L_(R+delta,S)`. Polynomial degree over integral domain k[Z,W] obeys `deg_W(A^(R-1))=(R-1)deg_W(A)`. Because R-1>S-1, `sigma(Z)` cannot involve W. Similarly `(R-1)deg_Z(sigma Z) <=R+delta-1<2(R-1)` since delta<S-1<R-1; thus sigma(Z)=aZ+b with a≠0.
2. Compose with inverse affine Z to make sigma fix Z. An automorphism of k[Z][W] that fixes k[Z] has `sigma(W)=cW+h(Z)` with `c∈k^×`: degree_W of a polynomial and its inverse multiply to1; leading W coefficient must be a unit of k[Z], hence a nonzero field scalar. Undo the affine Z normalization.
3. In the image of the CORNER monomial `Z^(R-1)W^(S-1)`, the W-free coefficient is exactly `(aZ+b)^(R-1) h(Z)^(S-1)`. If h has positive Z-degree, its Z-degree is >=(R-1)+(S-1)=R+S-2, strictly above the allowed R+delta-1 because delta<S-1. Thus h∈k and the automorphism is diagonal affine.
4. Conversely the diagonal affine substitution maps all monomial degrees within the same bounds and is invertible.

**The threshold is SHARP in the polynomial-row-only category:** at delta=S-1, the triangular polynomial automorphism `sigma(Z)=Z, sigma(W)=W+Z` maps `L_(R,S)` into `L_(R+S-1,S)` but is NOT diagonal affine. For original R145,S5, delta1 adds five polynomial rows and retains the rigidity; delta4 adds **twenty rows**, admits W→W+Z, and necessarily violates the actual ordinary fixed-W derivative convention because `∂_Z(sigma W)=1` while `sigma(∂_Z W)=0`. Thus the threshold is for ROW inclusion ONLY, not a valid full sampler/jet transport.

When also requiring the original conjugation involution `tau(Z)=W,tau(W)=Z`, commuting with tau forces a=c, b=d (all in F5 base). If moreover requiring trace isometry across all original ordinary derivative orders (J5 contains j1), then a²=1 mod5, a=±1. Phase296-A already exhaustively showed neither +/-1 with real translations and either conjugation branch matches the original D583/587 Q residues under phi. **This conditional finite source statement is stronger than merely excluding affine coordinate changes**, but does NOT close non-automorphism/injective source maps, arbitrary observation-side operators, or deeper class-one field implications.

## Characteristic-5 adversarial *function/jet ghost* [P-paper + bounded verification]

On `k=F5`, local value field F25 has 25 elements, so `w^25=w` for EVERY original sampled coordinate w (or indeed any w in F25). The triangular map

```
  sigma_ghost(Z)=Z+(W^25-W),   sigma_ghost(W)=W
```

is a NONTRIVIAL polynomial-ring automorphism over F5 with inverse Z→Z−(W^25−W). It acts as the IDENTITY on EVERY ORIGINAL finite F25-valued observation point and, because ∂_Z(W^25-W)=0, also on EVERY ORIGINAL ordinary Z-jet order j=0,...,4 with W held fixed **mod5**. Nevertheless its formal image of `Z^(R-1)` has W-degree `25*(R-1)=3600` for R145, far exceeding S-1=4: sigma_ghost does NOT preserve the original 725-row lattice or the one-row extension. Exact finite observation/jet equality alone cannot promote it as an arithmetic source gauge.

At **mod25**, even the actual original real sample w=2 satisfies `2^25-2≡5 mod25 ≠0`, so the ghost ceases to look like the identity at the next p-adic depth. This is a new hostile test for the difference between finite-field observed function values and the integral formal polynomial source.

## Prospective tests and stop rules

1. Freeze both original helper blobs, original full R145/S5/Q383 D583 source, full R146/S5/Q383 D587 source and Phase296-A script blob. Check exact R145→R146 5-row attachment and threshold R145→R149 20-row attachment.
2. Implement a fresh FORMAL sparse polynomial support oracle over F5 and verify that diagonal affine substitutions remain inside L for the corner and a deterministic set of boundary monomials, while triangular shear W→W+Z violates L_(146,5) but fits L_(149,5). Confirm Z→Z+W, Z→Z² and W→W+Z² fail the thin target.
3. Verify the polynomial-degree proof gates symbolically from arbitrary nonzero coefficients via degrees/leading coefficients, not merely numerical sampling. Check the threshold delta=3 (no shear) versus delta=4 (shear) explicitly. Check conjugation compatibility and trace-jet norm-one implication (at p5 a=±1 for base-field units).
4. Verify ghost automorphism is invertible as a FORMAL triangular substitution (two-sided composition), its W^3600 leading term in Z^144 image is nonzero, it is identity as a FUNCTION on all 383 ORIGINAL F25 sample points and ordinary j0..4 jets modulo5, but fails at actual sampled w=2 modulo25. Include the independent finite-field identity `w^25=w` for all25 F25 elements, not merely original Q points.
5. Stop if any formal inclusion/degree threshold, characteristic-p ghost, or p25 hostile sample fails. Do not silently weaken original row structure or call the ghost a legitimate source automorphism.

**Evidence:** [P-paper] elementary polynomial degree rigidity, sharp near-row threshold, field-function evaluation kernel / jet ghost; [M after CI] checked finite original source geometry and adversarial coefficient-level cases; [H] complete transformation category allowing arbitrary non-polynomial maps, fully p-adic primitive source embeddings and uniform h1 field effect; [R] finite-sample jet agreement implies full formal `GL_(RS)(Z_p)` lattice equivalence or p-adic determinant gain. No Work/no merge.
