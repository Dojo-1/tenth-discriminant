# Phase299 — original-lattice nonintegral transverse gluing, without fictitious determinant mass

**13 November 2026. Post-result mathematical/evidence ledger for DRAFT PR #191**, stacked above Phase298 #190 and its earlier drafts. All original data were left intact. Original source blobs, exact field/observation/jet metadata and dependency versions are frozen by the reproducible CI. No Work mode, no merge or changes to actual field cutoff PR #157. The installed research methods classify claims [P-paper], [M] exact bounded source verification, [H] speculation and [R] retired interpretations. All computational tests and this manuscript are AI-authored and correlated through shared helpers; external human review and source-to-field adjudication remain outstanding.

**Prior art / attribution:** The discriminant-group correspondence for integral overlattices with bilinear-isotropic subgroup `H`, including `D(L') ≅ H^⊥/H`, is an established lattice theorem; see Ichiro Shimada, *Supersingular K3 surfaces in characteristic 2 as double covers of a projective plane*, Asian J. Math. 8(3), 2004, Proposition 5.2 (attributing the theorem to Nikulin). The even-quadratic isotropy statement is a separate strengthened condition. This experiment works over `Z5` and keeps the **bilinear** form. Its novelty is NOT checked and is not being asserted. All finite-dimensional module/Gram manipulations are p5-local.

## A. Correcting the type of transport [P-paper]

Let the genuine ORIGINAL row lattice `L1=L0⊕R y` over R=Z5 have integral symmetric nondegenerate Gram `[[A,c],[c^T,b]]`. The projection `t=A^-1 c∈Q5^n` is in `L0^#`, because `A t=c∈R^n`. When its class `[t]∈D(L0)=L0^#/L0` is NONZERO, **rational orthogonal projection cannot define a natural quotient group map `D(L1)→D(L0)`**: y is a lattice vector and therefore represents 0 in `D(L1)`, but the projection of y is t and represents `[t]≠0`. It is the proposed *projection-induced* map that is invalid; this does NOT claim no abstract homomorphism can exist between the finite groups.

Put `h=min{k:5^k t∈L0}` and `a=5^h t`. Define the genuine integral vector `k=5^h y−a·old`. Then `k⊥L0` in the ORIGINAL rational ambient Gram, and `K=L1∩L0^⊥=R k` (the minimality of h ensures a primitive k). We have the finite-index orthogonal sublattice

```
M = L0 ⊥ K   ⊂   L1,   [L1:M] = 5^h.
```

**The original lattice L1 is NOT replaced by M.** It is recovered as the integral OVERLATTICE with its gluing subgroup

```
H = L1/M ≅ Z/(5^h),
  < ([t] in D(L0), [k/5^h] in D(K)) > ⊂ D(M).
```

Here both generators have exact order `5^h`. The bilinear form of `D(M)=D(L0)⊕D(K)` vanishes on `H×H` since its generator corresponds to the ORIGINAL integral row y. The standard integral-overlattice theorem gives

```
D(L1) ≅ H^⊥/H
as finite bilinear discriminant modules.
```

This is a **gluing span**, not a scalar covariance map between old/new Gram cokernels; the phrase "moving-frame transport with remainder" describes this concrete span and its exact finite-index data, not unproved higher-dimensional holonomy or sheaf gluing.

With `m=(k,k)=5^(2h)*(b−c^T A^-1 c)`,

```
v5(det G_L1) = v5(det A) + v5(m) − 2h.
```

The `−2h` is the index-square cancellation. The original determinant is independent of how we choose to orthogonalize in a finite-index sublattice. Adding either +h or +2h as extra original determinant valuation is [R].

## B. Phase299-A — complete finite toys and the real class-one field D163 [M]

**Preregistered before code at `dd651c2b5795ba2df38bf0caf9ba03eb90cd3df8`.** [Focused original-source and exact group CI #43383144286](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43383144286) PASS. Toy group tests explicitly enumerate the bilinear orthogonal subgroup `H^⊥` and its cosets modulo H; this is not merely a determinant comparison:

| Positive-definite original rank-2 Gram | old `v5(det A)` | m=(k,k) | `v5(m)` | `v5(det original G)` | exact `H^⊥/H` |
|---|---:|---:|---:|---:|---|
| `[[10,2],[2,2]]` | 1 | 40 | 1 | 0 | trivial |
| `[[25,5],[5,10]]` | 2 | 225 | 2 | 2 | `(Z/5)^2` |

Both have h1/H order5, yet one final discriminant group is trivial while the other remains nontrivial—**the gluing relation matters beyond its scalar size**. A separate already-integral positive Gram `[[10,5],[5,10]]` has h0/trivial H/index1 and is not incorrectly placed in the nonintegral class.

**Actual D163 field:** K=Q(sqrt(-163)) has h(K)=1 by classical Minkowski plus 2,3,5,7 inertness (a field property independent of this source). Original repository sampler is `rho21/R40/S=J1/Q109` of the **integer order**, not the full maximal-order two-coset lattice. It checks all1,600 original trace Gram entries by two distinct source representations. For **ORIGINAL** L0 first13 monomials `1,Z,...,Z^12` and y=`Z^13`, the earlier exact dual witness `ell=(0,1,0,4,0,2,0,2,0,3,0,1,0)` satisfies `ell*A13=0`, `ell*c13=2 mod5`. This Phase299 run rejects the unscaled original projection, solves `A13*a=5*c13 mod5^16` in the ORIGINAL old basis, and constructs the genuine source row `k=5Z^13−sum_i a_i Z^i` with all13 original row pairings zero. The direct ORIGINAL Q109/jet/trace-B norm of k agrees with the Gram formula modulo5^16.

**Complete D163 local gluing valuation:**
```
v5(det original G_old13)       = 1
v5(m original k)               = 1
-2*v5([L1:M])                  = -2
v5(det ORIGINAL G_full14)      = 0.
```
The old and full Smith profiles are uncensored at precision16 (max grades1 and0 respectively), so their p5 determinant valuations are exact, not merely capped. Computed m modulo5^16 is `123694501390`; v5(m)=1. With h1, m/25 is NOT integral over Z5, while the old t^2 has the opposite fractional self-pairing; they cancel because original y has integral norm. This is a nontrivial bilinear anti-pairing of the two discriminant classes.

An independent **GL13(Z5) source-gauge control** permuted/sheared the original old monomial basis and sent y to y+one original old row; gluing index/order, original old/full Gram valuations and m mod5^16 remained unchanged, while the actual coordinate vector changed. The original source itself was not modified by this control. Source original coefficient vector SHA `4a5ff0922bcd16c1601f6646d22588a504140c42bb8d88a4b81fbc6ae35ad99f`.

## C. Phase299-B — D587 genuine high-jet nonintegral first stage [M]

[Focused original-source CI #43383144279](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43383144279) PASS at K16.

The original D587 source uses exactly `rho53,R146,S=J5,Q383`, original ordinary Z-jet derivatives holding W fixed, trace metric `B=(2,1174)`, and the ORIGINAL 730 monomial row lattice. Work INSIDE the original **odd parity** sector: the old 362 original rows at r<145 and y=original `Z^145 W^4` (one of the original five added r145 rows).

The Phase297 original odd dual obstruction was independently reproduced **exactly** with the SAME 362-vector SHA `b09bb9c1a2e40772932c25f8edf984898d2ed3606d7e689e135dab554504815b`: `ell Aodd=0 mod5^14` in all362 old original columns and `ell c_bad=4*5^13 mod5^14`. The old Smith grades are uncensored, max14. The unscaled projector is NONintegral, and the scaled equation `A*a=5*c_bad` is solved in the ORIGINAL 362-row basis.

The actual original source-derived orthogonal generator
```
k = 5 Z^145 W^4 − sum_(i=1)^362 a_i*old_i
```
has all 362 old **original observation/jet trace pairings ZERO modulo5^16**; both source-native and Gram-algebra computations give `m=(k,k)≡48828125000=8*5^14 mod5^16`. Hence m has exact v5=14. This differs from D163: here the k/5 component has integral bilinear self-pairing since `m/25=8*5^12`, and the old projected class is individually bilinear self-isotropic; nevertheless both classes are nonzero and H glues them. Thus identical gluing index `5` can carry different discriminant pairing data, not reducible to an index scalar.

**D587 exact odd lattice accounting:**
```
v5(det old ORIGINAL odd G_362)     = 1925
v5(m ORIGINAL orthogonal K)         =   14
-2*v5(index5 gluing)               =   -2
v5(det ORIGINAL odd G_363)         = 1937.
```

The full ORIGINAL 730-row D587 Gram remains `v5(det G730)=3924`, original 5-row Schur valuation69; no change to any prior double-counting gate. The **orthogonal index-five sublattice M** has odd local Gram valuation1939, but is not the original lattice. The ORIGINAL odd lattice is recovered by adjoining the H gluing coset, including the original generator y; the source-native code checks `5*y = k + sum_i a_i old_i mod5^16`. This is the exact sense in which the moving-frame return preserves the original arithmetic lattice with a typed remainder.

D587 source-derived orthogonal projection coefficient SHA `78f37ffb9fb6e693a9f6850e1b0b22f2bc9f21a9e2cc659a5f852b6c5edb8fc8`, full original dual SHA as above.

## D. Epistemic boundary and next test

**[P-paper, established prior art]:** primitive one-generator orthogonal complement, gluing subgroup, finite bilinear discriminant module quotient `H^⊥/H`, and index-square determinant formula. It is not independent human-reviewed here or formalized in Lean; no originality claim for the standard theorem.

**[M, exact original source scope]:** two source-pinned original D163/D587 tests at p5 K16, all source Eraw/gram/jet/metric conditions, original dual obstruction, direct orthogonal pairings and norms, complete uncensored old/full Smith grades, and explicit finite toy discriminant forms. All remain AI-authored and correlated in their source dependencies. The small toy group quotients are fully enumerated, but the huge D587 `H^⊥/H` is identified through the standard theorem and verified determinant/orthogonality/index structure; a direct full cardinality enumeration is not feasible.

**[H]:** general many-row nonintegral transport, associativity of gluing correspondences under arbitrary nested extensions, *uniform* source-to-field inequality over every genuinely h1-admissible discriminant, and a new tenth-discriminant cutoff. The D163 source has only J1 and samples the integer order, while D587 has J5 but is NOT class number one. Do not conflate them.

**[R]:** rational orthogonal projection induces a canonical quotient homomorphism D(L1)→D(L0) when the old cross class is nonzero; forcing a nonintegral first-stage direct-sum Schur composition; calling the orthogonal index-five M the unchanged L1; or adding gluing p5 index factors to ORIGINAL determinant mass.

**Next smallest mathematical target:** for TWO nonintegral attachments, construct and compare the *gluing correspondences* of their intermediate orthogonal lattices, with explicit isotropic subgroups, pushforward/pullback over a common rational ambient space, and a finite overlattice associativity diagram. Apply to D587's bad-first→safe rows, with a toy where the abstract intermediary discriminant group changes despite the original final lattice being fixed. Do not assume arbitrary discriminant quotient maps between successive L_n. Keep all PRs DRAFT pending independent field/mathematics review #50/#51.
