# Phase303 — genuine maximal-order bridge, residue trace, Frobenius primitive Gram, and field-theorem scope

**Research date 13 November 2026.** Stacked **DRAFT PR #195** atop Phase302 #194 and its earlier drafts. No Work mode, no merge/main modifications, no change to field-bound draft #157 or integrated actual-field theorem `|disc(K)|<322^4`. This is an AI-authored source/number theory experiment suite; GitHub Actions are reproducible and all mathematical source helpers are pinned by SHA, but this is NOT independent mathematical peer review or a new Lean-kernel theorem. Full original source field semantics and source-to-field implications remain subject to human reviewers #50/#51.

**Prospective evidence sequence, kept separate:** [A+B+C preregistration](PRE_REGISTERED_MAXIMAL_ORDER_ALL_LINES.md) commit `f3eccd010e68d71d626646a60e36fadb303e6319` BEFORE A/C code, [D prereg](PRE_REGISTERED_RESIDUE_AND_FLAG_TRANSFER.md) `7d071a9828bd94899d274862a93864b73893dbe7` AFTER A passed but BEFORE D code, and [E prereg](PRE_REGISTERED_FROBENIUS_PRIMITIVE_GRAM.md) `d3e124dab1223d7f9982144dba0f69271d13b306` AFTER A/D passed but BEFORE E code. All previously measured results are labeled historical inputs to later experiments; no post-hoc claim of an ex ante prediction.

## A. The exact source-to-field coordinate square [P-paper] and a REAL maximal-order experiment [M]

For `K=Q(sqrt(-163))`, set `ω=(1+sqrt(-163))/2`. Its **maximal integer ring** `O_K=Z[ω]` satisfies `ω²=ω−41`, `N(a+bω)=a²+ab+41b²`, and trace Gram

```
       [2  1]
 Bω =  [1 82], det Bω=163.
```

The ORIGINAL repo order `Z[sqrt(-163)]` is index2 in `O_K`, with coordinate map `(x,y)↦(a=x−y,b=2y)`, `T=[[1,-1],[0,2]]`. Exactly, `Tᵀ Bω T=diag(2,326)`. Since `det T=2` is a p5 UNIT, these orders have isomorphic p5-local rings and trace modules. **This does not equate their finite norm-ball observation supports:** maximal-order elements with b odd are NEW points. The source comparator is designed to separate these two mechanisms.

All three arms have **the original same norm cutoff ρ²=441**, ORIGINAL row labels `Z^r`, r=0..39, and the original single-jet setting `R40,S=J1`:

| Arm | Exact source Q | Original-row p5 evaluation rank | p5 Gram rank | full original `v5 det G40` |
|---|---:|---:|---:|---:|
| old integer-order source `Z[sqrt(-163)]` | 109 | 15 | 15 | **77** |
| maximal-order b-EVEN, matched via T | 109 | 15 | 15 | **77** |
| genuine maximal-order ALL b | **225** | **25** | **25** | **30** |

Maximal order b-layer population (b=-3,-2,-1,0,1,2,3): `(18,33,40,43,40,33,18)`. Thus exactly **116 NEW b-odd points** joined the old109. The exact even-coordinate arm matches all **1600 original integer Gram entries**, not just their p5 reduction, and matches **8720** original real/imag raw evaluation channel coordinates via T at K16. Each maximal arm independently constructs all1600 integer Gram entries via direct ω trace contraction AND independently coded multiplicative trace moment `Tr(z^r conj(z^s))`. All source row bases, observations and the original trace B are recorded.

[Full exact source and p5 CI #43395406605](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43395406605) **PASS**, and again at later commits (check exact head before merging). FULL ORIGINAL 40-row Smith at p=5,K16 (all uncensored):

```
old/even: {0:15,2:8,3:7,4:10}, v5(det)=77
max-full: {0:25,2:15},         v5(det)=30
```

All39 original consecutive row attachment cross-image indices were recomputed (both arms). The old integer-order source nonintegral new original Z powers are **13,18,22,25,33,34,38,39** (all order5); the genuine FULL maximal source powers are **2 (order25),6,16,36,37 (order5)**. The originally prior Phase298 sample stopped at n38; n39 is new and was **not** claimed by prior 38-case records. Different source supports produce different exact local row obstructions, **despite an exact p5 local order isomorphism**.

There is NO general p5 Gram monotonicity under adding observation columns: positive-definite source toy Gram10 (v5=1) becomes Gram12 (v5=0) by adding a positive weight2 observation. Real positive definiteness and p-adic valuations are different notions. The empirical drop77→30 is not a larger field discriminant cutoff or a new monotonic theorem.

## B. Independent `F25` residue multiplicity mechanism [P finite-field lemma + M]

[Source-pinned D exact finite-field CI #43396022895](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43396022895) **PASS**. Original `O_K/5 ≅F25`. Old even support occupies exactly **15** residue classes; full maximal norm ball occupies all **25**. Both sets are Frobenius-conjugation stable, and the polynomial row evaluation rank over F5 agrees with support size. On the FULL source the raw residue multiplicity `m(z)` in each of 25 classes is one of **8,9,11**, with histogram `{8:12,9:7,11:6}`. On EVEN source it is one of **6,7,8,9**, histogram `{6:4,7:6,8:2,9:3}`. Every multiplicity is NONZERO modulo5, and `m(z^5)=m(z)`.

An independently implemented F5 algebra `F5[ω]/(ω²−ω+1)`, with `Tr(a+bω)=2a+b`, reconstructs ALL1600 original p5 Gram entries in BOTH arms via

```
  G_ij = Σ_{z∈S} m(z) Tr_{F25/F5}( z^i (z^j)^5 )   mod5.
```

This is not merely counting observations: it exposes *why* the old/new Gram ranks are respectively 15/25. **[P-paper classical finite algebra]:** for Frobenius-stable residue support S, F5 polynomial evaluation realizes the full Frobenius-compatible function algebra on S; unit-valued Frobenius-stable weights m make the trace pairing perfect. The corresponding polynomial Gram has rank |S| once sufficiently many monomial rows are present. The primal sample support is part of the theorem hypotheses, not an ancillary display variable. The full source has more independent modulo5 constraints because it actually samples new residue classes.

## C. Full maximal-order flag transport, not a copied old histogram [M]

The D follow-up was preregistered AFTER the original maximal-order prefix result, using **all five** new obstructed first rows n=(2,6,16,36,37), with first coker image depths `(2,1,1,1,1)`. For ALL **47** later same-parity original row attachments `Z^s` after these n, source-native projection into that actual intermediate Gram is integral over Z5, with fully resolved p16 Gram Smith and checked ω-coordinate E/trace pairings.

For ALL **328** pairs `s<t` from these fixed later sets, the Schur splitting hypotheses therefore apply. Every case independently checks the original source-correct two-dimensional residual trace Gram, both orders' Smith-image debt and identical final original Gram under an actual row permutation. The exact transition distribution is:

| First `s→t` debt exponent → reverse `t→s` exponent | count |
|---|---:|
| 0→0 | **184** |
| 0→1, 0→2, 0→3, 0→4 | **72, 6, 3, 4** |
| 1→0, 1→1, 1→3 | **42, 7, 1** |
| 2→0, 2→1 | **6, 1** |
| 3→0 | **2** |
| **Total** | **328** |

So the forward debt histogram is `{0:269,1:50,2:7,3:2}` and reverse `{0:234,1:80,2:6,3:4,4:4}`. Exactly **137** cases differ by attachment order; the largest observed source-index depth is **4**, in the reverse direction. All are bounded finite SOURCE claims with original maximal-order Q225/J1/trace Bω, NOT actual class-number-one discrimination theorems. The first paired source obstruction is n2,s4,t6: forward debt1, reverse debt0, and the final full original Gram v5=0 in either order.

Original legacy D163 Phase301-B/C had a distinct `43` and `176` source census with different first n and support. The new `47` and `328` results are not a numerical continuation of the old 176 samples: the source points changed.

## D. Frobenius primitive Gram: source-specific FULL proof of why 30 [P conditional lemma + M]

**Preregistered AFTER A/D at `d3e124dab1223d7f9982144dba0f69271d13b306`.** [Exact source Frobenius CI #43396570744](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43396570744) **PASS**.

For every z in O_K/5=F25, `z^25=z`. Thus on the actual maximal-order norm ball, each original polynomial difference `F_r(Z)=Z^r−Z^(r−24)`, r=25..39, has BOTH ω-coordinate evaluations divisible5. The operation `Z^r↦F_r` is an integral UNIMODULAR row basis change on the original 40 monomials. Dividing the resulting 15 evaluation rows by5 is a SEPARATE **nonunimodular evaluation superlattice** `Eprim`; it does not replace the original lattice. With `U` unimodular and `D5=diag(I25,5I15)`, exact original source Gram identity:

```
  U*G_original*U^T = D5*Gprim*D5,
  Gprim = Eprim*Bω*Eprim^T.
```

On full maximal-order Q225 all **6750** actual row/channel Frobenius divisibility tests pass; all1600 factored Gram entries reconstruct original G mod5^16. **Primitive E rank40, primitive Gram rank40, first25 principal Gram rank25** modulo5. Therefore `Gprim` and its first25 block are units at p5, yielding BOTH the full original Smith profile `{0:25,2:15}` AND exact determinant valuation

```
  v5(det ORIGINAL G40)=2*15+v5(det Gprim)=30.
```

On the old matched Q109 EVEN source, all **3270** Frobenius coordinate divisibility checks also pass, but the analogous primitive evaluation rank is only **30**, primitive Gram rank **23**, and principal25 Gram rank **15**. Thus the same normalized Frobenius family does not give a unit primitive Gram there; the old spectrum is richer, v5(det original)=77. This is a **negative source-control**, not an inconvenient failure hidden from publication. The successful full result is a complete source-faithful finite-dimensional explanation of 30, not a universal field-mass theorem.

## E. Independent class-one arithmetic, source-feasibility limit and review boundary

[Arithmetic focused CI #43395406663](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43395406663) PASS. Classical split-prime obstruction: in imaginary quadratic maximal order for fundamental discr −D, D≡3mod4, if h=1 then any prime p<(D+1)/4 cannot split: otherwise its prime ideal has norm p and must be principal, but `N(a+bω)=a²+ab+((D+1)/4)b²` cannot attain that prime below the first noninteger minimal norm. For D163 all primes <41 are inert; hostile field D23 has **two** split primes p=2,3 under cutoff6, so their ideals obstruct h1. An initial run [#43395301070](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43395301070) FAILED because an AI-authored negative-control expectation incorrectly assumed D23 only had split p2; source arithmetic actually has BOTH p2 AND p3. The expected set was corrected to `[2,3]` at commit `9d9565096d99ad9296d7279e8de283e45185114a`; the successful independent run retains this original mistake visibly.

The original source uses `R=floor(D/4), S=J=floor(R/25)`. Among the nine classical class-number-one radicands `D=1,2,3,7,11,19,43,67,163`, the source is defined for D≡3mod4, and NONE reach `J≥2`; D163 alone reaches `J=1`. The original source formula requires D≥200 just to reach J2. Hence **a source-faithful high-jet / known-h1 test is impossible under the present rule**. Artificially assigning J>1 to D163 would be a different experiment, not an extension of this source-faithful comparison.

Tao's [original October 20 tenth-discriminant challenge and live discussion](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/) contain other commenters' claims of much tighter class-one bounds and Lean results. They are SOURCE-REPORTED until the exact proof statement, dependency closure, formal semantical correspondence and human review are inspected. Our proven integrated field upper cutoff remains unchanged; no new zero-free-region or Siegel-zero argument emerges from a fixed D163 source.

## F. The exact research-to-field obligation

The successful Phase303 square distinguishes three typed objects:
```
order/lattice change (index2; Z5-local isomorphism)
       !=
new finite observation support (adds 116 points)
       !=
actual intrinsic number-field class-number or L-function data.
```

The first transport is exact [P-paper]. The second changes the sampled trace Gram and is measured [M]. **The THIRD arrow remains [H]**: prove a UNIFORM, source-faithful inequality for all hypothetical large h1 quadratic fields that forces a contradiction with the analytic or arithmetic discriminant conditions. Neither source Gram v5=30 at one known h1 field, nor lower primitive rank in the old source, nor arbitrarily large moving-flag epsilon from Phase302 implies that uniform theorem.

Our concrete new structural lemma is the Frobenius+support primitive Gram criterion; it is classical algebra and experimentally verified here, but its original number-field consequences remain open. The classical norm/split-prime argument is genuinely field-arithmetic but not novel; the p5 Gram data are genuinely source-arithmetic but not (yet) a class-one test. No scalar amalgamation can bridge the two without an independently checked implication.

**Next responsible steps:** (1) independent alternate-language/code original maximal-order trace Gram and p5 Smith replay, excluding shared original source helpers; (2) formalize the simple quadratic-order coordinate identity and Frobenius primitive Gram block lemma without confusing it with field theorem; (3) if pursuing larger D/high-J, freeze a hypothetical-h1-uniform theorem statement **before** new stress data and do not claim verification from non-h1 fields; (4) human peer mathematical and formal-semantic review (#50/#51), keeping all stacked PRs DRAFT. No Work, no merge or autonomous field-cutoff promotion.
