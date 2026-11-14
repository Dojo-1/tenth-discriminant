# Phase296 — preregister affine-semilinear transporter search and arithmetic source gate

**13 November 2026. Preregistered BEFORE Phase296 implementation, exact finite enumeration or CI.** Branch stacked on Phase295 draft #186, above #185→#182. No Work mode. Preserve all original helpers, avoid edits to PR #157 or main, and never promote an observation obstruction to an improved tenth-discriminant field bound.

## What must be allowed, and what remains outside scope

Earlier Phase295 [P] proved that an invertible A_k-linear observation transporter commuting with the **fixed W multiplication operator** exists only if exact W scalar multisets match. On original D583 / D587 samplers the mismatch d1=104 and d2+=276, robust under four involutions. The observation modules have rank1915 over A_k but original polynomial row lattices rank725 vs730 and cannot simply be identified.

Now permit W TO MOVE by an affine-semilinear local coordinate transformation. Fix p5 and common residue field
`F25=F5[u]/(u²+583)`, u²=2 mod5, with D587-to-D583 local quadratic algebra isometry `phi(x+y u587)=x+2 y u`. For either epsilon∈{+1,-1}, test the FULL group
```
 g_(a,b,epsilon)(z_B)=a * conj^epsilon(phi(z_B)) + b,
   a ∈ F25^× (24 possibilities), b ∈ F25 (25 possibilities),
   epsilon = +1 identity or -1 Galois conjugation.
```
Here source and target are the complete ORIGINAL 383-point ellipse Q for BOTH full D583 R145/S=J5/n725 and full D587 R146/S=J5/n730, not a 725-row D587 diagnostic. The search contains 24*25*2=1200 parameter triples (duplicate support actions may occur by Q symmetry), with an embedded norm-one subgroup of 6*25*2=300 candidates and a scalar Z/5-based subgroup. This is a PERMISSIVE category for geometry: arbitrary translation b and arbitrary unit a may violate original trace metric and formal integral row-lattice preservation. Therefore a no-go for ALL affine candidates is stronger than a no-go for its legitimate trace/row subgroups. Do not assert affine transformations exhaust nonlinear or arbitrary jet-algebra automorphisms.

Define `c_A(z)` as the ORIGINAL Q multiset of residue points z∈F25. Let `c_g(z)` be the transformed original D587 support multiset under g. For each g define maximum match `M(g)=Σ_z min(c_A(z),c_g(z))`, unmatched debt `d(g)=383−M(g)`. Preregister **NO PREDICTION** for the smallest d(g), best slope or best translation. Report an exhaustive debt histogram and all ties for the best geometry. An affine move can LOWER d from the canonical 104 without yielding a complete transport; do not conceal this.

## Exact paper-level no-go prediction BEFORE exhaustive enumeration

The full Q has y0 x∈[-53,53] (107 points), each y±1 horizontal strip 95 x-values, each y±2 strip43 x-values. At residue mod5:
- the unique global maximum point multiplicity is **22**, attained at precisely **(2,0)** and **(3,0)**, since 107=21*5+2 and x runs -53..53; y±1 residues have19 each, y±2 have8 or9.
- The already transported phi(Q) also has exactly those two heaviest points, since y=0 is fixed by phi.
- Any affine/semilinear FULL multiset equivalence must preserve the two heaviest point locations. They differ by 1 on the real axis, so the multiplier a must be exactly +1 or -1 in F25. The shift b is then necessarily 0.
- For either a=±1,b=0, including either Galois twist, the phi(Q) y±1 points occupy y±2 residues. At any x the transported multiplicity is19 whereas the ORIGINAL y±2 class has multiplicities8 or9. Contradiction.

Thus the **predicted theorem-level conclusion** is NO exact affine-semilinear support bijection already modulo5 for the whole 1200-candidate group. Any lift over A_k to k≥2 reduces modulo5, so this rules out an affine-semilinear coordinate transporter of these types at all higher p5 precisions, **without** considering trace metrics or primitive source rows. An exhaustive F25 enumeration MUST confirm the proof; if it finds an exact match, STOP and correct the paper argument rather than fit a narrower group post hoc.

## Broader versus narrower controls, and genuine larger-frame escape

1. Exhaust all 24 nonzero slopes, 25 translations and both Galois pre-twists; independently compute Counter multiset matching as well as a second sorted-list matching oracle for the best candidate. Separate the best unrestricted affine debt, best norm-one (N(a)=1) debt and best R5-coefficient affine debt. Norm-one slopes should count exactly 6 elements, and `N(a)=a*bar(a)=a0²+583*a1² mod5`.
2. Check the heavy two anchors and their unique force on a,b as above in actual extracted Q, not fabricated counts. Positive controls for same-field Q preserve identity and central inversion, and q→bar(q) on original integer Q. A hostile asymmetric Qtoy should lose some of these symmetries.
3. **Deliberately overpermissive counterworld:** the general F5-linear map on the common field chart `L(x+y u)=x+3 y u` exactly reverses phi's y scaling at p5, so `L(phi(Q))=Q`. But L is NOT a ring automorphism of F25: `L(u²)=2`, while `L(u)²=(3u)²=3 mod5`; it also changes the local quadratic norm of u (3→2 mod5). This proves that an unrestricted 2D linear coordinate transformation CAN repair support but destroys multiplication/trace, so a no-go in the affine F25-SEMILINEAR group must not be advertised as no-go for all 2D maps.
4. Test the ACTUAL original ordinary `∂_Z` jet chain rule for affine substitution `(Z,W)↦(aZ+b,bar(a)W+bar(b))`: `∂_Z^j f(aZ+b,bar(a)W+bar(b)) = a^j (∂_Z^j f)(aZ+b,bar(a)W+bar(b))` on deterministic labels and source q. Use an independent polynomial-binomial expansion oracle, not just the same formula repeated. If `N(a)=1`, the j-dependent multiplication by a^j is trace-metric isometric; if `N(a)≠1`, it is NOT automatically so.
5. Test formal base row-lattice restriction: the full original one-coefficient-per-monomial `Z/5` polynomial rectangle `L_(R,S)=span{Z^r W^s}` admits a triangular/unimodular base change under real a,b∈F5 with a≠0, but if a or b has nonzero u-coordinate the image of the existing Z row `aZ+b` already needs non-base coefficients and does NOT define a `GL_(RS)(F5)` change of the original scalar coefficient lattice. General 2×2 affine polynomial substitutions mixing Z and W violate the rectangular bounds for R≫S: `Z↦aZ+cW` with c≠0 sends Z^(R−1) to a polynomial with nonzero W^(R−1) term (forbidden); `W↦dZ+bW` with d≠0 sends Z^(R−1)W^(S−1) to a term of Z-degree R+S−2 (forbidden) after a is forced nonzero. This classification is in the explicitly stated affine-linear polynomial substitution class only, not all polynomial automorphisms.
6. Require outputs preserve that full ORIGINAL sources have different row ranks 725 and730, full Q383/J5, and note D583/587 are not class number one. No Frobenius-divided row is inferred transportable by raw jet checks; Phase294's (Z^5−W)/5 counterexample remains.

## Stop/interpretation gate

If the affine search finds exact multiset match, the heavy-pair proof is WRONG; stop and record. If the independent jet chain check fails, correct its map/orientation; if a nonnorm-one map still appears metric preserving for **all** j, inspect trace metric. If the unrestricted GL2 escape fails, the field coordinate chart is wrong. Do not change D, p, Q, alpha or the enumeration group after results.

[P-paper] heavy multiplicity anchor no-go, affine substitution/jet chain identity, norm/field-multiplication counterworld and rectangular polynomial support obstruction.
[M after CI] exact 1200 element affine-semilinear enumeration, minimum d across explicitly named categories and independent controls.
[H] full maximal *nonlinear* automorphism group of original jet algebra; possible maps altering W together with differentiated direction; compatible primitive saturated row transport; any uniform h1-discriminant consequence.
[R] affine no-go means no arbitrary two-coordinate map; support-debt counts are p5 determinant valuations; a general A1 point frame is already a GL_(RS)(F5) original arithmetic lattice gauge.
