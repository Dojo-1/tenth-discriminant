# Phase294 — the moved-source p-adic transport square, and its signed 40-dimensional boundary

**Final mathematical and evidence ledger for the 12 November 2026 round.** AI-authored original-source exact arithmetic with three sequential preregistrations and frozen source helpers. `research/phase294/PRE_REGISTERED_RESIDUE_BOUNDARY.md` was committed at `820ceb61` before A code; `PRE_REGISTERED_MOVING_NORMALIZED_SOURCE.md` at `44a34a5` after A, before B; `PRE_REGISTERED_MOVING_PRIMITIVE_SOURCE.md` at `e058423` after B, before C. None of the successful CI runs are independent mathematical peer review, and root Lean compilation does NOT formalize these new results. The code is a stacked DRAFT on #184 → #183 → #182; no existing original source helper or actual-field PR #157 was modified.

## The exact source carriers (do NOT flatten)

A = **full original D583/R145/S=J5/Q383**, all 725 original integer polynomial row labels `Z^r W^s`, ordinary `∂_Z^j` jets for j0..4 with W held fixed, and original metric `B_A=diag(2,1166)` repeated on all 3830 real/imag observation channels.

B = **only the first725 original polynomial rows of D587's true full n730/R146/S=J5/Q383 source**, retaining ALL D587 original Q383/jets and `B_B=diag(2,1174)`. This is a deliberately row-matched DIAGNOSTIC, not a replacement of the full D587 actual-field source or its existing v5=3924.

The original integer Q_A equals Q_B as literal 383-point sets, but the local field isometry moves its support. For inert p5 choose `alpha∈Z5^×` satisfying `583 alpha²=587` and `alpha≡2 mod5`, with computational truncation `alpha≡647814942 mod5^13` (`2 mod5,17 mod25,67 mod125`). Let `phi(a+b u587)=a+alpha*b u583`. Define the **FORMAL MOVED support** `phi Q_B`. That support is *not* the original D583 ellipse; it is a p-adic source configuration identified as such in every test.

## I. Signed residue support defect is small in rank, not in physical point count [P-paper + M]

The original Q has transverse x widths: `y0:107`, `y±1:95`, `y±2:43`. For each x residue a mod5, the inner layer has 19 points. The outer layer x counts are `c(0,1,2,3,4)=(9,9,8,8,9)`. Under the mod5 field-coordinate map `y→2y`, the exact signed INTEGER residue-multiplicity difference between `phi Q` and Q is

```
δ(a,y) = c(a)-19 for y=±1,
δ(a,y) = 19-c(a) for y=±2,
δ(a,0) = 0.
```

The total positive signed mass, also the minimal number of single-point residue-multiset replacements needed to correct this prescribed frame action, is `2*(95−43)=104`. But mod5 the ±10 deficits at a=0,1,4 vanish, leaving only the ±11 defects at a=2,3. Exactly EIGHT distinct residue points remain, organized into FOUR Galois conjugate pairs in `F25=F5[u]/(u²+583)`, represented by `(2,1),(2,2),(3,1),(3,2)`. The defect is invariant under conjugation and central inversion.

The raw original-jet Gram difference on **ALL 725 original row labels**, with each source's ORIGINAL metric, satisfies

```
ΔG := G587(Q)−G583(Q)
   = G583(phi Q)−G583(Q)  (mod5)
   = E_∂ M_∂ E_∂^T,
E_∂ in M_(725,40)(F5),
M_∂ = direct_sum_(q in 4 reps, j=0,...,4)
        4 δ(q) diag(1,583 mod5).
```

The `4` factor follows EXACTLY from the original trace metric `diag(2,2D)` and including both conjugate observation points, not an additional index. `M_∂` is nondegenerate over F5 since p5 is inert, D583 mod5=3, δ(q)=±1 mod5.

**Rank proof (a small conditional theorem, not an unexplained 725×725 output):** On residue field F25, `W=z^5`. For 0≤j<5, ordinary Z-jets of `Z^r W^s` coincide at residues with ordinary j-jets of the single F5 polynomial `Z^(r+5s)` because the derivative of `Z^(5s)` vanishes in characteristic5. The first **40 original rows** `Z^0,...,Z^39` form the complete Hermite/CRT interpolation basis at the four distinct irreducible quadratic conjugate pairs, each to multiplicity five: dimension `4*2*5=40` over F5. The exact CRT evaluation matrix is invertible, the signed trace metric is invertible, so one ORIGINAL 40×40 principal Gram-defect minor is nonzero mod5; the 725-row defect factors through 40 columns and therefore has EXACT rank40. Central inversion exchanges the four conjugate-orbit channels in two pairs; its ± eigensectors have equal dimension20, with no off-parity blocks. Hence

```
rank_F5 ΔG_full_raw = 40 = rank_even 20 + rank_odd 20.
```

[Phase294-A CI #43313214413](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43313214413) PASSED: source hash guards, full n725×40 residue evaluation, four original minimal quadratics, invertible original 40-row minor, parity20+20, original Phase293 six-row defect rank5 replay, independent direct original integer-Gram oracles also testing high-degree rows, and hostile alpha1 / alpha−2 / equal-width rectangle / single-pair J1 / too-few-rows / J>p / p-division controls.

### Reusable general odd-prime lemma [P-paper, not a novel global claim]

Fix odd p with `F_p[u]/(u²+D)` a FIELD (−D nonsquare modp). Let two conjugation-stable finite observation multisets have signed residue multiplicity defect δ. Suppose δ modp is nonzero precisely on f distinct **conjugate pairs** of non-real F_(p²) elements, with nonzero δ values, and zero on Fp-fixed points. For original ordinary Z-jet orders 0≤j<J≤p and polynomial source rows including `1,Z,...,Z^(2Jf−1)`, the modp difference of original trace Grams has exact rank `2Jf`. The proof is the CRT/Hermite evaluation rank `2Jf` and nondegenerate signed field trace form. If central inversion pairs the f Galois orbits with no fixed orbit, ranks of the even/odd defect blocks are each `Jf`. This lemma applies only to the RAW modp trace Gram; p-adic saturation changes the question.

## II. Positive full normalized source chart when observations MOVE [P-paper + M]

[Phase294-B CI #43313818640](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43313818640) PASS used the Hensel root `alpha=647814942 mod 5^13`. The old Frobenius row frame is identical on the row-matched A/B sources:

```
F_(r,s)=Z^(r−5k) W^s (Z^5−W)^k,
k=min(floor(r/5),4−s),      Σ k=1350.
```

It is unimodular before dividing the r,s source row by `5^k`, with k<=4. The associated normalized original observation matrices `C0` were both built to `5^9` precision using a `5^13` numerator, all 725 original rows, all j0..4, all 383 original q **indices**, both original coordinate channels per q and original field multiplication tables. The numeric field map `Y=diag(1,alpha)` on each value pair satisfies

```
C0_A(phi Q_B) = C0_B(Q_B)*Y  (mod5^9),
Y B_A Y^T = B_B              (mod5^9).
```

ALL **2,776,750 matrix entries** matched, with **960** independent original integer-jet coordinate checks. A bounded 9×9 original-weighted trace Gram replay matched modulo5^9. This is a transport of the *normalized source with MOVED observation support*, not of actual Q_A held fixed. It spends p^13 numerator precision to avoid losing four digits through old Frobenius division, rather than pretending a mod5 identity suffices.

## III. Construct a true source-compatible p-primitive pairing square with MOVED Q [P-paper + M]

[Phase294-C CI #43314426708](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43314426708) PASS independently saturated the 363 even and 362 odd row modules using the SAME OLD p5-source EVALUATION columns for B, and applied the SAME p-adic unimodular row map U_B to B and the FORMAL MOVED A. This deliberately avoids transporting internal Smith COLUMN operations into the metric. The already-certified secondary Smith grades over all 725 rows are `{0:625,4:10,5:20,6:70}`, exact index560 and maximum exponent e6. Since the old C0 identity holds mod p^9, the row quotient by `p^e` still holds modulo at least `p^(9−6)=p^3`. In synchronized primitive row frames,

```
C_prim,A(phi Q) = C_prim,B(Q) * Y   (mod125).
```

**Every one of 2,776,750 primitive entries** matched; both primitive source evaluations have full rank725 mod5, split as 363+362, and all 131,406 even×odd cross-sector pairings vanish modulo125 on BOTH sides. Full primitive H parity blocks match under their respective ORIGINAL B metrics entrywise modulo125. Their old (already counted!) primitive H Smith grades are `{0:690,1:35,2:0,>=3:0}` (even grade0 345/grade1 18, odd grade0 345/grade1 17). The field-trace evaluation transport is implemented **without** an arbitrary postselected primitive pairing matrix X: in the synchronized saturated bases X=identity and the column field-coordinate map Y is explicit. SHA256 receipts of each parity's primitive observation matrices are in the CI output.

This proves a FINITE **positive** existence result for source-compatible p5-primitive transport over `Z/125` whenever Q itself is allowed to move to phiQ. It uses the same already-counted p5 factors: old F5=1350, secondary560, primitive H residual35, consistent with v5(det n725 original/diagnostic)=`2*(1350+560)+35=3855`. That 3855 is NOT a new factor. The transported A sample points are NOT the original field D583 ellipse, and no conclusion about h(K)=1 or the full D587 730-row source is drawn.

## IV. The surviving noncommuting square and its honest debt

The two natural operations must not be conflated:

```
  (D587, Q_B, 725 diagnostic rows)
                |
                | phi on quadratic field + phi on OBSERVATION SUPPORT
                v
  (D583, phi Q_B, 725 rows)  --- TRUE primitive source square mod125
                |
                | support correction / "boundary surgery" to ORIGINAL Q_A
                v
  (D583, Q_A, 725 ORIGINAL rows) --- NO canonical fixed-label source square
```

- Positive **top arrow**: full p5^9 normalized and mod125 primitive field transport with actual moved observations, tracked row maps and original metric. Valid as a local field-coordinate statement at finite p-precision.
- Nonzero **bottom support remainder**: 104 signed residue units but only 40 RAW mod5 Gram rank, 20+20. This is NOT a bound on the p-primitive trace-pairing difference after Frobenius and secondary source row divisions.
- Phase293-D previously proved that the canonical field-value map with all actual original Q labels FIXED admits NO row map even modulo5, despite abstract primitive pairing isometries between the two original fixed-support 725-row forms. Our new positive result does not supersede that negative result: the domains differ.

**Precision debt lemma [P-paper]:** If a rowwise source relation is known modulo `p^N` and both corresponding rows are divisible by `p^d`, division gives a relation only modulo `p^(N−d)`. Certifying all divided rows modulo `p^k` requires N≥k+max d. In this matched source, old k≤4, secondary e≤6; primitive p³ comparison can require up to **13** digits of an underlying compatible raw source map. More importantly, different ORIGINAL supports need not admit compatible row maps U at all; extra precision alone does not prove such a map exists. Toy `5≡10 mod5` but `5/5=1 != 2=10/5 mod5` explicitly kills any shortcut.

### Source-to-field / priority boundary

**[P-paper conditional]** ring and original-jet naturality with a MOVED support, signed residue-trace factorization and CRT/Hermite rank formula, p-adic row-division lemma. **[M]** exact original Q383 discrepancy, four-orbit signed rank40/20+20, all 725×3830 normalized and p-primitive moving support source maps, independent frozen original-jet oracles and controls. **[H]** an admissible original-support replacement with effective p-primitive rank/Smith bounds, a uniform production-D estimate and an actual h1 number-field implication. **[R]** moving observation covariance automatically implies fixed original Q covariance; raw modp remainder rank40 can be promoted to additional primitive valuation; a finite p-adic chart is a real adiabatic one-parameter dynamics.

**No field D563/D583/D587 in these stress tests is assumed class-number-one; the number-field target is still open.** The local 5-adic chart is a discrete algebraic equivalence, not a real-time adiabatic physical evolution. Root Lean checks are separate, the PR stack is DRAFT pending human independent mathematical/source-to-field review #50/#51, and no Work mode was invoked.
