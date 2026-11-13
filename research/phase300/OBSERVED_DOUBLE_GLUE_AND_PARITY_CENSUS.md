# Phase300 — two nonintegral stages, original-lattice gluing, and a parity-limited field control

**13 November 2026 — post-result mathematical and evidence ledger.** All results are AI-authored and reproducible through GitHub Actions, with original Phase206/204/297/298/299 source files frozen by blob SHA. This is a stacked **DRAFT PR #192**, above #191 and earlier drafts. The user explicitly rejected Work mode; no Work mode, merge, main change or change to the tenth-discriminant cutoff PR #157 was made. External independent mathematical/source-to-field review remains outstanding.

The mathematical object is a *chain of actual arithmetic row lattices*, not a sequence of display frames. The original final lattice is never silently replaced by the orthogonal sublattice used to describe its discriminant pairing. More generally, the preceding Phase299's one-step gluing theorem is an application of established integral-overlattice theory (Nikulin/Shimada), not a new theorem; Phase300 examines two successive nonintegral primitive inclusions and what the join remembers.

## 1. Exact two-stage gluing: a group extension, not two added indices [P-paper]

Take the original primitive tower over `R=Z5`:

```
L0=<old rows>, L1=L0+R*y1, L2=L1+R*y2,
```

with integral symmetric Gram `G2`, and both rational orthogonal projections requiring exactly one p5 denominator. Let

```
 A a1 = 5*c1,
 G1 (a20,a21)^t = 5*(c2,e)^t.
```

The genuine ORIGINAL-lattice vectors

```
 k1 = 5*y1 - a1·old,
 k2 = 5*y2 - a20·old - a21*y1
```

are mutually orthogonal and orthogonal to the old lattice (since k2 is orthogonal to all of L1). The included orthogonal lattice `N=L0⊥Z5*k1⊥Z5*k2` has index25 in original L2. It is **not** a new replacement for L2. The gluing subgroup `H=L2/N` has the presentation

```
 H = <u=[y1],v=[y2] | 5u=0, 5v=a21*u>.
```

Thus `|H|=25` in either case, but

```
a21≢0 mod5  ⇒ H≅Z/25 (nonsplit),
a21≡0 mod5  ⇒ H≅(Z/5)^2 (split).
```

The subgroup embeds as a bilinear-isotropic subgroup of `D(N)=N^#/N` because the ORIGINAL y1 and y2 have integral pairings. The classical overlattice theorem reconstructs the unchanged original discriminant form by `D(L2)≅H^⊥/H`. The exact determinant identity includes **the square of the index25**:

```
 v5(det G_original_L2) =
 v5(det G_original_L0) + v5((k1,k1)) + v5((k2,k2)) - 4.
```

The `−4` is essential: it is not a claimed new field or source determinant gain. The abstract extension type is not determined by the cardinality25, and **a choice of noncanonical modular Smith solution is only a coordinate mechanism**. The statement about split versus cyclic is robust because all original old/intermediate Smith grades are fully resolved before K16, so the class of a21 modulo5 is invariant.

## 2. Phase300-A — two positive-definite worlds distinguish the types [M + P]

**Preregistered BEFORE code** at commit `ef74ac1d7664a5dfff7c7cdeac670a3616bba5d5`. [Exact source-and-toy CI #43385578942](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43385578942) **PASS**.

Both 3×3 symmetric integral Gram examples are positive definite by direct leading-principal-minor checks. Their first projection equals 1/5, and their second projection also needs one factor5. They have the SAME total gluing subgroup order25, but radically different torsion extension type:

| Toy ORIGINAL Gram | Rational scaled coefficient a21=5*t2_(y1) | H total | v5 old | v5(k1²) | v5(k2²) | v5 original final |
|---|---|---|---:|---:|---:|---:|
| `[[25,5,1],[5,10,0],[1,0,10]]` | `−1/9` (p5 unit) | **Z/25** | 2 | 2 | 1 | 1 |
| `[[25,5,0],[5,10,1],[0,1,10]]` | `5/9` (divisible5) | **(Z/5)^2** | 2 | 2 | 2 | 2 |

Their full original integer determinants are respectively **2,240** and **2,225**. Exact Fraction arithmetic separately confirms rational projections, the finite 25-coset quotient is explicitly enumerated and closed under addition, the original y1,y2 are reconstructed in the rational orthogonal frame with denominator25, and bilinear isotropy plus original pairing equality are checked at K16. A filtration-preserving `GL3(Z5)` gauge changes projection coefficients but not the torsion group type, index or original determinant. A hostile first-nonintegral/second-integral toy is rejected by the double-nonintegral setup instead of being coerced into it.

## 3. Phase300-A — genuine original class-number-one D163 source, TWO consecutive obstructions [M]

The imaginary quadratic **field** K=Q(sqrt(-163)) has class number one by classical Minkowski and inertness of 2,3,5,7; that theorem is separate from the source simulation. The repository's ORIGINAL `Z[sqrt(-163)]` sampler has `rho21,R40,S=J1,Q109,B=(2,326)`, not the full maximal-order two-coset lattice. The 40×40 original Gram was independently constructed and all1,600 entries checked by source_probe.gram/mixed moment and direct raw ordinary-jet E/B methods.

The earlier [exhaustive Phase298-B 38-chain census](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43379240150) had already recorded consecutive nonintegral chains n33 and n38 with two *exact* order-five projection obstructions. Their selection was explicitly **RETROSPECTIVE** and recorded in Phase300 preregistration; there were NO preregistered group-type predictions. All old/intermediate/full Smith profiles in Phase300 remain uncensored (max<16). The source gives:

| UNCHANGED original chain | old v5 det | after first v5 det | final v5 det | v5(k1²) | v5(k2²) | gluing group |
|---|---:|---:|---:|---:|---:|---|
| `L33⊂L34⊂L35`, add original Z^33 then Z^34 | 51 | 54 | **57** | 5 | 5 | **(Z/5)^2** |
| `L38⊂L39⊂L40`, add original Z^38 then Z^39 | 71 | 74 | **77** | 5 | 5 | **(Z/5)^2** |

The original trace metric and all actual Q109 observations are retained. Actual original monomial/jet E rows are used to check every old–k1 pairing, every L1–k2 pairing, k1–k2 orthogonality, both original trace norms and the complete included orthogonal Gram `B_N^T G_original B_N`. The full original rows y1 and y2 are recovered from the rational N-frame coordinates, bilinear gluing isotropy is verified, and all25 quotient cosets are enumerated, in both examples. Determinant identities:

```
 51 + 5 + 5 − 4 = 57,
 71 + 5 + 5 − 4 = 77.
```

**Crucial qualification:** both observed original-source examples are split. The source did NOT produce a cyclic Z/25 example; that possibility remains demonstrated by the separate positive-definite toy only.

## 4. Phase300-B — why the consecutive examples split, and the hostile same-parity census [P-paper + M]

AFTER the Phase300-A results, separately preregistered [PRE_REGISTERED_PARITY_AND_SAME_SECTOR_SEARCH.md](PRE_REGISTERED_PARITY_AND_SAME_SECTOR_SEARCH.md) at commit `b96ab2184e68a6e3fb10f2438351dab94d75c18a`, BEFORE Phase300-B code and CI. A NEW study, not retroactive preregistration of A.

[Source-exact Phase300-B CI #43385937496](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43385937496) **PASS**. It proves the actual ORIGINAL D163 Q109/J1 centrally symmetric sampler induces exact integer parity orthogonality `G_(r,s)=0` for all r+s odd; ALL **800** such 40×40 original entries are checked, and all raw evaluation observations obey `E_r(-q)=(-1)^r E_r(q)`. Consecutively added monomials Z^n and Z^(n+1) therefore occupy OPPOSITE parity sectors. The rational second projection coefficient on the first new row is **exactly zero** (not just zero modulo5); the code constructs a valid scaled second projection solution with coefficient a21=0 for BOTH n33 and n38. This algebraically EXPLAINS the split H=(Z/5)^2 previously observed in A.

To challenge the temptation to universalize parity, Phase300-B then exhausts **ALL 43 later ORIGINAL same-parity second-row attachments** following the already recorded seven nonintegral first-stage rows n=13,18,22,25,33,34,38. These are `L_n→L_n+Z^n→L_n+Z^n+Z^s` for `s=n+2,n+4,...,39`, i.e. source-faithful but NONCONTIGUOUS original monomial sublattices. We did NOT change the field/prime/Q/metric based on observed results.

Exact result: `{second-stage image-index log5: 0 for ALL43}`. All second stages already project integrally onto their old+first stage; there are **zero** further order-five gluing classes and therefore NO same-parity double-nonintegral source instance. Their full original Smith cokernels are uncensored at K16. This result is stronger than simply observing the two original splits, but is finite-source evidence for this exact D163 sampler only.

This produces a useful *hypothesis to test elsewhere* rather than a theorem about all imaginary quadratic fields: the original D163 J1 row process seems to have already exhausted its p5 transverse obstruction within each parity sector once a nonintegral generator has been attached. A proof, mechanism and field-uniform interpretation are OPEN. The cyclic positive-definite counterworld remains essential: general integral Gram towers do not obey universal splitting.

## 5. Honest boundary and next question

**[P-paper, classical / proof sketch]** Two-stage primitive orthogonal sublattice N, isotropic gluing subgroup H⊂D(N), finite abelian group presentation criterion for split versus cyclic order25, index-square determinant formula; central inversion implies exact parity orthogonality and forces split for the two consecutive opposite-parity original D163 source cases.

**[M]** Two separately preregistered exact source/CI tests, 1) real original h1-field D163 n33/n38 two-nonintegral chains with reconstructible index25 gluing sublattices, 2) exhaustive 43-case same-parity negative search. Two source-independent positive-definite cyclic/split counterexamples, source-invariant basis gauge, full original source 40×40 Gram/jet/trace checks, original field/source distinction. All code/results remain AI-authored, not independent mathematical replication.

**[H]** A uniform one-obstruction-per-parity statement for D163 or a family of fields; general multi-stage gluing associativity and possible cyclic extensions in higher-J exact original samplers; field-theorem influence on actual class-number-one discriminant cutoff.

**[R]** Treating all order25 gluing groups as `(Z/5)^2` or all as `Z/25`, double-counting orthogonal index25 as extra v5 source determinant gain, extrapolating from an integer-order D163/J1 sampler to the full maximal-order or D587/J5 regime.

**Next discriminating step:** identify the precise source-side structural invariant (parity-resolved `Z5` evaluation/trace Gram cokernel filtration) responsible for the 43-case same-parity disappearance; compare it with a larger *actual* h1-admissible source ONLY after a preregistered cutoff and independent field/source review. The tenth-discriminant upper bound is unchanged; no new original arithmetic mass was proved.
