# Phase295 — no integral W-equivariant original-jet transport, even after dense mixing

**12 November 2026 — post-result evidence ledger.** AI-authored classical paper lemma plus exact frozen-original-source GitHub Actions. The mathematical lemma is elementary and not claimed novel. Code tests are internally reproducible, not external independent mathematical refereeing. This is a **stacked DRAFT PR #186** on #185 → #184 → #183 → #182, with no Work mode, no merge and no modification of the draft actual-field PR #157 or integrated 322^4 field cutoff.

## 1. The actual carrier, not a metaphorical moving frame

Two COMPLETE ORIGINAL field sources, with `params(D)` and the original ordinary Z-jets holding W fixed: D583 has rho53, R145, S=J5, Q383, **725 original polynomial rows**; D587 has rho53, R146, S=J5, the same literal Q383 but **730 original polynomial rows**. Both have five ordinary jet orders j0..4 at every original point and two signed trace-coordinate channels. Their original polynomial ROW modules do **not** have the same rank and are NOT being identified.

**The tested carrier is the common-sized OBSERVATION-side module**, not either row lattice. For k≥1 set `A_k=(Z/5^k)[u]/(u²+583)`; this is a commutative unramified quadratic local ring since -583≡2 is nonsquare modulo5. Identify the D587 local order via `phi:u587→alpha_k*u`, where `583 alpha_k²=587 (mod5^k)`, with alpha=2 mod5/17 mod25/67 mod125, and alpha=647814942 mod5^13. Let

```
 V_A(k) = direct_sum_(q∈Q) A_k^J,
 V_B(k) = direct_sum_(q∈Q) A_k^J,       J=5,
 dim_Ak(V_A)=dim_Ak(V_B)=383*5=1915.
```

Each A_k slot consists of two real/imaginary `Z/5^k` coordinates, so this is precisely 3830 original observation coordinate slots over the base ring. The observation-side operator of multiplication by `W` is

```
 M_W,A = diag_{q∈Q} [ w_A(q) * I_5 ],  w_A(x,y)=x−y u;
 M_W,B^phi = diag_{q∈Q} [ w_B^phi(q) * I_5 ],
                           w_B^phi(x,y)=x−alpha_k*y*u.
```

This scalar per-jet form is forced by the **actual original** convention `∂_Z^j(W f)=W∂_Z^j f`, with W held fixed (rather than using W-derivatives). We do NOT say multiplication by W is an operator of the finite rectangular row submodule itself; it can leave the allowed s<S range, and this is a material carrier distinction.

**Admissible test group:** arbitrary **invertible A_k-linear observation maps** `Y∈GL_1915(A_k)` allowed to densely mix points and jet orders, but required to intertwine `Y M_W,A = M_W,B^phi Y`. An observation-metric isometry would impose further conditions; absence of even this W-intertwiner is a no-go for the narrower geometry/jet-preserving category. Maps that CHANGE W or are non-A-linear are NOT covered.

## 2. Elementary theorem over ANY commutative local ring [P-paper]

**Diagonal scalar intertwiner criterion.** Let R be commutative local, `a_1,...,a_n,b_1,...,b_n∈R`. Then

```
  ∃Y ∈ GL_n(R):  Y diag(a) = diag(b) Y
  ↔ multiset(a_1,...,a_n) = multiset(b_1,...,b_n).
```

**Proof.** Entry (i,j) yields `(a_j−b_i)Y_ij=0`. If detY is a unit, its permutation expansion cannot consist entirely of nonunit products, since all nonunits form the unique maximal ideal and their sum stays in that ideal. Thus one permutation σ has **every entry** `Y_(i,σ(i))` a UNIT (a product is a unit iff every factor is a unit). Multiplying the entry equation by that unit's inverse gives `b_i=a_(σ(i))` for all i. Conversely a multiset matching supplies a permutation matrix with the required intertwining property. QED.

Note that a nonZERO but NONUNIT off-fiber entry can satisfy `(a−b)x=0` without a=b; it cannot provide the necessary perfect matching of **unit** entries. Therefore simply zero-counting off-diagonal blocks or comparing characteristic polynomials would be weaker than the argument.

The map `(x,y)↦w_A(x,y)=x−yu` is INJECTIVE as an R_k-module coordinate map because 1,u is a free basis. Likewise for w_B^phi since alpha_k is a unit. Each scalar w occurs exactly J times per sampled point. Hence W-scalar multiset equality is EQUIVALENT to the point residue multiset equality of original Q against phiQ; Phase294's point-fiber debt `d_k` is **a basis-independent necessary and sufficient invariant for the existence of a W-intertwining FULL observation-module isomorphism** in the defined category.

If extensions are restricted to appending a whole original-type five-jet point block with scalar W at each new point, the same theorem makes `d_k` the MINIMUM number of added blocks on EACH side even allowing arbitrary dense Y. Phase294's common-residue-envelope construction attains the bound in the synthetically enlarged category. Neither minimum has anything to do with the original Gram's p-valuation or independent evaluation-index factors.

## 3. Verified exact original sampling data and witness [M]

[Phase295-A pinned original-source focused CI #43310825762](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43310825762) PASS. The script independently computes W-value multiplicities from the full actual Q383 and checks them against x/y residue multiplicities. Original params, original ordinary-jet and Phase294 Hensel/matching helper blobs are hash-frozen; the actual field chart, conjugation, norm and source W-commutation identities are tested. There is no 725-row D587 cropping. Results:

| k | original point blocks matching exactly | d_k unmatched POINT blocks EACH SIDE | matching free A_k jet slots | unmatched free A_k jet slots EACH SIDE | unmatched real/imag Z/5^k slots EACH SIDE |
|---|---:|---:|---:|---:|---:|
| 1 | 279 | 104 | 1,395 | 520 | 1,040 |
| 2 | 107 | 276 | 535 | 1,380 | 2,760 |
| 3 | 107 | 276 | 535 | 1,380 | 2,760 |
| 13 | 107 | 276 | 535 | 1,380 | 2,760 |

All 383*5=1915 A_k observation jet slots per side are accounted for. The scalar W **multiplicity witness** is explicit: `w=(0,1)` in the chosen common field basis appears 19 times on the D583 original point support but only 9 times on the locally transported D587 support modulo5; at modulo25 it appears 3 versus 0, and at modulo125 and 5^13 it appears 1 versus 0. This one mismatched eigenvalue multiplicity suffices to disprove full W-module isomorphism. The full d_k quantifies the minimum formal point-block repair in the declared category. The other quadratic square root −alpha yields the same debt because the original ellipse is conjugation symmetric.

No conclusion here says 520 or 1380 are Smith indices, Gram ranks, cokernel dimensions of a sheaf, or p-adic valuations. They are **unmatched free observation-coordinate counts over A_k**, under a particular local-algebra-equivariant module category.

## 4. Hostile counterworlds: characteristic polynomial and Z-only jets [P-paper + M]

**Spectral shortcut FAILS.** On five jet slots over R=Z/25, `W_0=0*I5` and `W_1=5*I5` satisfy `det(TI−W_0)=T^5=det(TI−W_1)` because `(T−5)^5=T^5 mod25`. Nevertheless any intertwiner satisfies `5Y=0 mod25`, forcing **all entries of Y divisible by5**, so no invertible Y exists. Equal characteristic polynomials are not the right invariant over this local ring, especially because J=p5.

**Z-only jets CAN absorb p-adic center shifts.** On `R[t]/t^5` with `N` multiplication by t and ordinary finite jets, `(t+5)^5=0 mod25`. The upper-triangular integer Taylor substitution `T f(t)=f(t+5)` has all diagonal entries 1 and satisfies **`T N=(N+5I)T mod25`**. This is an explicit unimodular jet mixing. But if W on those fibers acts as 0 versus5, no W-equivariant invertible map survives. This is the exact reason to retain the original condition **W held fixed**, not to claim that all local jet modules forbid shifting a center by p.

A nonunit off-scalar intertwiner is possible (`(0−5)*5=0 mod25`), while a nonpermutation unimodular shear between **equal-W** fibers genuinely intertwines. These positive/negative controls were exercised in Phase295-A.

## 5. Original symmetries survive the test, not by fiat [M]

Phase295-B was **separately preregistered AFTER A**, and [focused CI #43311245677](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43311245677) passed. Original Q383 is EXACTLY invariant under central inversion (x,y)→(-x,-y), field conjugation (x,y)→(x,-y), and their composition (-x,y). The test checked **400 exact original ordinary-Z-jet inversion and conjugation identities**, including source parity `(−1)^(r+s−j)`; it also checked a nonsymmetric support where these four actions have DIFFERENT W multisets, ruling out a hardcoded-invariance artifact.

For each depth k=1,2,3,13, the four **explicitly declared** scalar pre-twists of transported W, `{w,−w,bar(w),−bar(w)}`, have identical eigenvalue multisets as the untwisted target because the ORIGINAL ellipse is symmetric under x and y sign flips. Against original D583 these each leave exactly `d1=104` and `d_k=276` for k>=2 unmatched original point blocks, so **no W-intertwining A_k-linear observation isometry exists in any of these four pre-twisted categories**. Galois conjugation was treated as a prescribed scalar *pre-twist*, not proof that arbitrary conjugate jet representations preserve ordinary ∂_Z with W fixed. Do not extend this four-element negative test to every hypothetical moving-frame action.

## 6. Mathematical and field-theorem boundary

**Proved at paper level [P]:** scalar-diagonal intertwiner criterion over an arbitrary commutative local ring, the original fixed-W jet action, and sharp original-type block-completion cardinality **conditional on that module category**. These are classical elementary constructions, novelty not claimed. The arithmetic ring identification and point-value injection are explicit.

**Measured [M]:** original sampled Q383 on BOTH full field sources, exact W-unit multiplicities modulo 5,25,125,5^13, two fully reproducible CI runs, normal/nonpermutation and pathological controls; these tests share source helpers and AI authorship and are not independently referee-verified.

**Still open [H]:** whether a different original-sampler-compatible operator algebra legitimately CHANGES W (or exchanges differentiated Z with W), and whether such a map can preserve all original jets, original trace metric, **old Frobenius and secondary source divisibility**, and ultimately yields a uniform class-number-one discriminant theorem. An arbitrary dense B-orthogonal pairing isometry remains weaker than such a source construction. Both tested D583 and D587 fail h=1, so none of their finite invariants directly strengthens the tenth-discriminant bound.

**Retired [R]:** interpreting an abstract primitive Gram isometry as an original sampler gauge, treating point/jet mismatch counts as independent determinant valuation mass, using characteristic polynomials as a complete integral similarity invariant, or identifying synthetic formal supports with original number-field observation data.

**Next smallest discriminating theorem target:** Define the maximal admissible **source-jet operator algebra** (including the complete multiplication/derivation compatibility of Z and W and the physically allowed finite observation automorphisms), determine its centralizer/transporter, and show precisely whether the only surviving symmetries are the original geometric involutions. Only then test such a theorem on a genuine h=1-admissible original source and its local neighbors; do not extrapolate from D583/D587.

Root Lean success compiles existing code and DOES NOT automatically formalize this new local-ring lemma. Independent math and source-to-field review #50/#51 remains required; keep this PR draft.
