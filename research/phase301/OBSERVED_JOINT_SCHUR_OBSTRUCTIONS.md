# Phase301 — pairwise integral projections do not compose automatically

**13 November 2026 — post-result mathematical, source and evidence ledger for stacked DRAFT PR #193.** Preregistered Phase301-A BEFORE executable at commit `adc663e8f04f730812e0da574c324ebbe8417f25`; preregistered Phase301-B AFTER the complete 176-case A result but BEFORE B executable at commit `40e720d26c3b6269f1097c9cadad96490776f4dc`. The B case was selected RETROSPECTIVELY as the first nonzero result, explicitly recorded before its new code. No Work mode, no merge, no edits to the original source, PR #157, main branch or tenth-discriminant upper cutoff. All tests, manuscript and mathematical interpretations remain AI-authored and require independent human mathematics/source-to-field review.

## 1. What Phase300 did and did not establish

Phase300-B original D163/J1/Q109 computed 43 individually integral later same-parity projections after the seven known nonintegral initial original rows n=(13,18,22,25,33,34,38). Those were **one-new-row** tests on the unchanged old+first original row Gram. They did **not** prove that two distinct future original monomial rows could be attached in either order while all later projections remained integral. Treating single-column cokernel membership as closure under arbitrary Gram enlargement is an invalid [R] inference.

The ordinary original D163 field **has class number one**, by classical Minkowski + inertness of 2,3,5,7. The repo's actual original source, however, uses the integer-order `Z[sqrt(-163)]` sampler and has exactly `rho21,R40,S=J1,Q109` with real/imag trace B=diag(2,326), rather than the full maximal-order two-coset sampler. Its 40×40 original Gram has all 1600 entries independently checked against exact original mixed moments and direct original j0 observation evaluation. Both source and metric remain unchanged in these tests.

## 2. Conditional exact Schur test [P-paper, classical]

Let `L1` be any nonsingular integral `Z5` Gram A. Suppose BOTH later original rows `y2,y3` have old cross columns `C2,C3 ∈ A Z5^n`, with integral original-basis projection solutions `A T_i=C_i`. Under the integral unipotent first-stage change `y2↦y2−T2^T old`, its scalar Schur norm and the next residual are:

```
S2 = <y2,y2> − C2^T T2,
R23 = <y2,y3> − T2^T C3.
```

The new `y3` class in the enlarged old+first Gram's cokernel is `([C3],[R23])=(0,[R23]) ∈ coker(A)⊕Z5/(S2)`. For `S2≠0`, the exact new p5-image class has order

```
5^max(0,v5(S2)−v5(R23)).
```

This is a simple application of the Phase298 integral-first-stage Schur splitting lemma, not a new theorem of bilinear forms. **It is also not an extra original Gram determinant factor.** The source produces S2 and R23 directly from original trace pairings. Successful single-vector projections imply NOTHING about this residual without comparing its valuation to v5(S2).

### Adversarial positive-definite counterworld [P/M]

The source-INDEPENDENT symmetric positive-definite integer Gram with original row order `old x, first bad y1, individually good y2,y3` is

```
G4=[[25,5,5,25],
    [5,10,10,5],
    [5,10,15,6],
    [25,5,6,100]].
```

Its leading principal minors are **25,225,1125,84150**, all strictly positive (Sylvester). The first y1 old projection is 1/5 NONintegral. On the old+first `L1=(x,y1)`, BOTH y2 and y3 have integral projections (they are respectively original y1 and x columns of G1). But after adding y2, `S2=5` and `R23=1`, yielding a **new order5 nonintegral** y3 projection. Direct original Gram Smith tests independently agree. Therefore no unconditional pairwise→joint integrality theorem is possible even for positive-definite integral lattices.

## 3. Phase301-A — 176 source-faithful same-parity joint extensions [M]

[Complete original-source GitHub Actions #43387766296](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43387766296) **PASS** on initial focused implementation; rerun again at final exact head. Preregistered **EVERY** fixed `n∈(13,18,22,25,33,34,38)`, and for each pair of later same-parity rows `s<t` from `{n+2,n+4,...,39}`, totaling exactly **176** ordered row triples. The original module is `span(1,Z,...,Z^(n−1),Z^n,Z^s,Z^t)`; where degrees are skipped, these are **noncontiguous** original monomial sublattices, not full increasing prefixes. Source original J1/Q109/B was never altered or supplemented.

Every case verified that BOTH original later rows individually projected integrally onto `L1=span(1,...,Z^n)`. For each first later s, the implementation built actual integral original-basis coefficients and the corrected **original observation row** `E_s−T_s^T E_L1`, checked its exact B-weighted pairings with old source rows vanish and its norm equals scalar Schur `S2`. For each later t it computed `R23` independently using the original trace observations, and compared the p-adic scalar prediction to the image-index debt computed by a separate full original Gram Smith calculation. All 176 equality gates passed at precision `5^16=152587890625`, with all relevant old Smith exponents uncensored and Schur scalars nonzero modulo p16. Frozen original helper blobs and all source-to-field/metric guards passed.

**Unexpected, decisive result: 148 jointly integral, 28 genuinely nonintegral with new group order5**. Distribution:

| First nonintegral original row n | Jointly integral | New order5 joint obstruction |
|---|---:|---:|
| 13 | 71 | 7 |
| 18 | 26 | 19 |
| 22 | 28 | 0 |
| 25 | 21 | 0 |
| 33 | 2 | 1 |
| 34 | 0 | 1 |
| 38 | 0 | 0 |
| **TOTAL** | **148** | **28** |

**No** case has a higher image-index exponent than1 in this fixed scan. This is a finite source measurement, not evidence that higher exponents cannot occur at another source, field or set of row degrees.

First detected joint counterexample, recorded prospectively for separate B follow-up AFTER A:
```
  original L14 = span(1,Z,...,Z^13);
  y2=Z^27, y3=Z^31;
  original L15 = L14 + Z^27.
  BOTH y2,y3 individually integral to L14.
  v5(S27)=3, v5(R27,31)=2,
  joint y3 class order5 in coker original Gram L15.
```

This is **not** a result of adding a second independent p5 factor to original field determinant. The obstruction is a NEW scalar residual after a real lattice inclusion, and is reported as a class in the actual enlarged original Gram's cokernel.

## 4. Phase301-B — short original D163 dual functional; independent check [M + P consequence]

[Focused original-source GitHub Actions #43388150281](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43388150281) **PASS**, at corrected code. Original source rows of the true 15-row enlarged Gram are `(Z^0,...,Z^13,Z^27)`. The new original row is `Z^31`.

A deterministic left original-Gram Smith row supplies the following compact vector modulo `5^3=125`:

```
ell = (0,10,0,29,0,5,0,75,0,80,0,115,0,10,1).
```

With `A15=G_D163[0..13,27 ; 0..13,27]` and `c31=G_D163[0..13,27 ; 31]`, the code checks directly

```
ell*A15 = (0,...,0)  mod125  (ALL15 original old columns),
ell*c31 = 75         mod125  (nonzero, v5=2).
```

This forbids any solution `A15 x=c31` in Z5^15, since multiplying by ell would give 0=75 mod125. The all15 annihilations and nonzero new pairing were *independently reconstructed* as direct source observation/trace pairings of `f=Σ ell_i E_(original row_i)` on all **109 original integer ellipse observations, 218 original real/imag channels, B=(2,326)**. Old Gram maximum Smith exponent3 is strictly below precision16. The original L14 integral projections of BOTH y27,y31 were separately solved and directly checked against every original old source row. Compact JSON 15-vector SHA256:

`cac6090e618d6936e41d0f26a3a6b7df6f4b2f0d324a41ff897e6a6f69779f46`.

**Failure provenance:** initial Phase301-B CI [#43388061800](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43388061800) FAILED due solely to a wrong parity helper import (`parent.symmetry` was defined in an adjacent frozen `same_parity_challenge` module, not the Phase301-A parent); this was an implementation/wiring error before the arithmetic portion. Corrected at commit `8e22e1263ae55898de8331064b641967a78d494a` by importing that helper without modifying any source, choice of witness case, arithmetic algorithm or expected residue. The corrected exact focused run passed. Keep the failed receipt and do not describe the first run as green.

## 5. The finite-field-period mechanism is partial, not the whole explanation

The p5 residue algebra for original D163 is the unramified quadratic field `F25=F5[u]/(u²+163)` because `u²=-163≡2 (mod5)` and 2 is nonsquare in F5. Every nonzero element of F25 has multiplicative order dividing 24. Hence on the ORIGINAL unshifted J1 sample, for **every r≥1** and every q (including q whose residue is zero),
```
   E_(r+24)(q) ≡ E_r(q) (mod5),
```
whenever both row indices lie in source R40. The code checks r1..15, all109 original observations, BOTH real/imag channels: **3,270 exact modulo5 checks** pass. At original q=(0,0), r0 and r24 do NOT match, providing a boundary control.

This is an exact **mod5 observation-level periodicity**, not an implication that (Z^{r+24}-Z^r) belongs to the integral Z5 *Gram-image* at every p-adic precision. Nor does it establish simultaneous closure, as our actual **28 higher-order obstructions show**. Treat it as a potentially explanatory finite residue symmetry to combine with the full p-adic Schur remainder, not as the reason for every observed valuation.

## 6. Evidence and next discriminating target

**[P-paper]** conditional original integral projection Schur splitting; scalar coker residual order formula; explicit dual-functional contradiction; finite field F25 power24 periodicity. These are elementary algebra with specified hypotheses, NOT a kernel-checked Lean theorem or a novelty claim.

**[M]** original D163 R40/J1/Q109 exact two-method trace Gram, 176 fixed pairwise-to-joint tests (148 zero,28 order5), short 15-component original dual witness with independent source-native evaluation, hostile positive Gram toy. All tests are AI-authored and share pinned code dependencies; independent human math/source-to-field review remains required.

**[H]** group-theoretic and p-adic *mechanism* behind precisely the 28 observed residual Schur classes; how this behaves under actual maximal-order/two-coset number-field sampling and richer ordinary jets J>1; a uniform inequality across genuine h1-admissible large discriminants; and any improvement to the tenth-discriminant bound.

**[R]** promoting 43 individually integral rows to collective/simultaneous integrality; using modulo5 finite-field periodicity as proof of p16 image membership; adding a source Gram cokernel image index as an independent determinant valuation; interpreting a noncontiguous monomial submodule as a complete field-order realization.

**Next small step:** extract the parity-resolved residual-Schur 2×2 Gram tensors for all pairs of individually projectable later rows over a fixed original L1, classify their mod5/p-adic valuation patterns *before* attaching either generator, and test whether a deterministic blockwise two-direction criterion accounts for all 28 classes without relying on pair ordering. This is likely to be more informative than adding another arbitrary field or expanding the original cutoff without mathematical source-to-field review. Keep PR #193 stacked DRAFT and unmerged; no Work.
