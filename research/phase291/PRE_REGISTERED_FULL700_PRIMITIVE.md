# Phase291 — full 700-row original-source p-adic primitive gate (pre-registered)

**12 November 2026; committed BEFORE new experimental code or Phase291 results.** This follows the user-supplied Biswas–Petrovic *On Extended Eigenvalues of Operators* (2005), the Phase290 six-row Noether/Smith source wall, and older Phase206/208/277/278/279/280 primitive-source work. It does not import the Hilbert-space spectral results as p-integral statements. The 700-row full-source primitive pairing is still the unresolved target.

## A. Preserve exactly the number-theory source

Freeze `research/phase206/source_probe.py` blob `3f954b59d9f86b06ad53667c869b5b24f2e6c7f6` and `research/phase204/ordinary_jet_filtration.py` blob `dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8`. Original D=563, rho=51, R=140, S=J=5, Q359 full centered integer ellipse including y=0,±1,±2 (NOT the ablated Q285); all 700 rows (r,s), 0<=r<140, 0<=s<5, all five ordinary Z-jet orders j=0..4 **with W held fixed**, both real/imag observation coordinates (3590 total), and original signed field-coordinate trace weights diag(2,2D). No Gaussian weights, half-coset or differentiated W, no unrecorded diagonal rescaling.

Compare:
- inert p=5: `(-563 mod 5)=2` nonsquare, so the old UNIMODULAR row-polynomial frame
  `F_(r,s)=Z^(r-5k) W^s (Z^5-W)^k` with `k=min(floor(r/5),4-s)` has exactly `F_5=sum k=1300` already-counted p5 powers. Predicted histogram across all original 700 rows by k is `{0:160,1:150,2:140,3:130,4:120}`, checked arithmetically BEFORE code. Since each divided row is integral at all original points/jets, `C0_(r,s)=5^-k partial_Z^j F_(r,s)(z,zbar)` is integral. This is NOT a new valuation.
- split p=7: `(-563 mod 7)=4` square. It is a source-matched negative control with **no inert Frobenius division**, `F_7=0`. The p7 pairing observed on the Phase290 six-row principal Gram is not an inert-prime source lower for a class-number-one theorem.

Fixed precision caps: p5 K=8 for the secondary source-Smith profile; p7 K=2. They are intentionally finite and may return censored exponents.

## B. What counts as primitive?

The original row evaluation module E (700x3590) is acted upon by the old p5 UNIMODULAR integer polynomial row frame; its row i is then divided by p^k exactly once, giving the original-source normalized C0. The secondary p-local Smith reduction `U*C0*V` is computed modulo p^K. U and V are internal integral-unimodular row/column operations, but **V is NEVER transported into the original trace metric**.

For Smith levels e_i < K, the only legitimate primitive source is reconstructed using the original observation columns:
`C_prim[i,:]=p^-e_i (U*C0)[i,:] mod p`. Require **all** 700 levels <K, no truncation, and independent rank(Cprim modp)=700 before computing the primitive trace pairing `Hprim=Cprim B Cprim^T modp`. Its radical has dimension 700-rank Hprim, only in that fully saturated case. If any level is **censored at K**, report a lower-bound evaluation index and `PRIMITIVE_UNKNOWN`: never add `rank(C0)-rank(C0 B C0^T)` to a valuation. This exact mistake was retired by Phase277.

The old p5 budget F_5=1300 plus `sum e_i` is the complete evaluated index only when uncensored. If then Hprim modp has nullity q, the **same original Gram** has `v_p(det G)>=2(F_5+sum e_i)+q`, and equality only with a p-unit primitive H. If censored, the safe bound is `v_p(det G)>=2(F_5+sum min(e_i,K))`, with no H correction. All quantities are finite-source; D563 is not asserted to have h=1.

## C. Independent finite controls and stop rules

1. Freeze source blobs; assert exact D/R/S/J/rho/Q, positive interpolation guard, distribution across five y layers, all row labels and 3590 columns, actual original B and p5 inert/p7 split.
2. Construct C0 modulo p^K from *all* original ordinary jets, using source-exact polynomial coefficients, with enough pre-division precision `p^(K+max k)`. Compare 16 deterministic boundary/middle rows, all jet j and 3 deterministic original points with the INDEPENDENT exact integer `ordinary_jet_filtration.jet` oracle, including both coordinates. Test at least two nontrivial k.
3. For p5, check all 359 points satisfy `z^5=bar(z) mod 5`; compare the predicted old k histogram and F_5=1300. The original conjugate-paired residue-class geometric bound gives `rank(C0 mod5)<=J*125=625`, hence first secondary nullity >=75. This bound already appears in Phase208, NOT Phase291 novelty. Do NOT apply it to split p7.
4. Compute a distinct finite-field Gaussian rank of the FULL C0, its UNSATURATED original-metric Gram, and a capped secondary Smith profile at the fixed precision. Independent rank must match number of exact level-zero Smith factors. Use exact modular int64 with explicit worst-case overflow bound; no float determinant.
5. Check the capped Smith algorithm on a fixed mixed-unit diagonal toy and the historical D283/p5 140-row source with recorded exact noncensored histogram `{0:60,1:15,2:30,3:20,4:15}`; that historical test is a **regression**, not a new prediction. Require its recovered primitive row rank 140 and primitive original-metric Gram rank 140.
6. If p5 or p7 fully saturates at the fixed K, calculate Hprim original metric, modp rank by independent algorithm, parity-equivariance and an explicit original-jet dot-product replay; otherwise stop at censored index and make NO primitive radical claim. Do not increase K within the same preregistered run merely to get a desired outcome.
7. Test restricted operator-theory consequence **only over the real SPD original Gram**: finite-dimensional `GX=lambda XG` has possible lambda equal to ratios of positive eigenvalues; there is no lambda=-1 or nonzero anticommuter and `Comm(G^k)=Comm(G)` for positive integer k. This is classical Biswas/Petrovic (Theorems 2.5 and 5.6), not a new integer or modp symmetry theorem. No eigenvalues of the full 700x700 huge-integer Gram need to be computed; a short eigenvalue-free Sylvester argument suffices.
8. Require full-source modular ranks, complete row coverage, independent oracle matches, toy and historical controls, explicit nonpromotion on clipping. Keep this PR **DRAFT** regardless of CI outcome; root Lean and human semantic review #50/#51 are separate, PR157 untouched. Preserve failed runs.

## Expected outputs and epistemic status

- **P-paper / known**: Frobenius row frame, exact row index F=1300, residue class bound, Smith row reconstruction if fully uncensored, elementary Hilbert-space positive intertwiner restriction.
- **M AFTER exact-head CI**: 700-row C0 rank, unsaturated Gram rank, capped Smith histogram, censored count, possible primitive pairing rank only if fully saturated.
- **H**: full primitive pairing radical at p5/p7 if precision cap censors, a uniform production-D spectral law, or any new field-discriminant cutoff.
- **R**: adding a raw/unsaturated Gram radical to p-local valuation, transporting Smith column operations through original metric, using p7 as inert p5, assuming complex extended eigenoperators are integral moving-frame gauges.
