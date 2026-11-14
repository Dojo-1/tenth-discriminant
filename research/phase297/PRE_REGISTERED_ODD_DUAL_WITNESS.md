# Phase297-C — preregister explicit original-Gram annihilator witness for the odd transverse denominator

**2026-11-13. After Phase297-B exact-head focused GitHub CI #43375446953 PASSED, before Phase297-C code or results.** This is a NEW independent certificate target, not a revision to the preregistered K16 outcome. AI-authored finite-source research; no outside review or new class-number-one field bound. All D587 original Q383/J=S5/R146 source helpers remain unchanged.

## Frozen findings to explain, not assumptions about the witness

The Phase297-A source-exact mod5^9 test produced zero image enlargement in both sectors, but censored 125 elementary directions. Phase297-B increased to mod5^16 and **reproduced every mod5^9 source entry and Smith invariant** while fully resolving ALL old-725 Gram elementary divisors, maximum exponent14<16. Thus the mod5^16 old cokernel IS the true p5 old Gram cokernel, since `5^16 Z5^n ⊂ A Z5^n`.

- EVEN old363 →new2: original old Gram Smith sum1930 with all e≤14, appended cross Smith profile IDENTICAL, so **the actual orthogonal projection of these two new rows is integral over Z5**.
- ODD old362→new3: original old Smith sum1925, appending C lowers exactly one elementary exponent14→13 (sum1924), giving subgroup `im([A|C])/im(A) ≅ Z/5`. Therefore the odd projection is NONintegral, but multiplying EVERY odd new-row projection coefficient by5 makes it integral. This conclusion is stronger than earlier B's cautious 'finite zero may be inconclusive' because K16 completely resolved the old matrix.
- Consequently the full projection `T=A725^-1 C725×5` is NOT integral over Z5, and has **exact denominator exponent1**: `5T∈Mat_(725×5)(Z5)`, `T∉Mat_(725×5)(Z5)`. We do NOT add this index 5 to `v5 det G730=3924` or the Schur ratio valuation69.

These are retrospective, machine-reported facts to INDEPENDENTLY validate using a dual vector rather than just comparing two Smith histograms. Parent code pinned:
`research/phase297/original_schur_integrality_k16.py` blob `aa3678001c69a7235dca638638d2dab4c55b05b3`, and Phase297-A blob `6ce23a8136ddd6208ef70d00a2bca419a105fdbb`.

## Precise dual obstruction target — unknown witness before code

Let `A_odd` be the **ORIGINAL D587 odd 362×362 Gram**, and `C_odd` be the 362×3 ORIGINAL cross Gram to the r145 rows of odd parity. All entries modulo 5^16, with original j0..4/Q383/metric diag(2,1174) and FULL original undivided monomial rows.

Find `ell ∈(Z/5^14)^362`, preferably a row of an EXACT p-adic Smith ROW transformation of original A_odd, with:

```
 ell * A_odd ≡ 0          (mod 5^14)    [all 362 columns]
 ell * C_odd ≠ 0          (mod 5^14)    [at least one of 3 columns].
```

Such a certificate proves no integral X can satisfy `A_odd X=C_odd`: if C=A X then ell C=(ell A)X=0 mod5^14. The proof depends ONLY on row arithmetic of original Gram, not the augmented Smith histogram. The source-normalized Frobenius/Smithed columns are NOT allowed in the witness return map. Pick the FIRST deterministic witness from p^14-grade row transforms; do not preselect a convenient new row/prime/precision. Print its full 362-component vector (or a losslessly encoded compressed vector with a self-checking decoder and SHA256), its exact pairing residues, the first nonzero cross-column and v5 of that residue. The CI must RECHECK the 362 original Gram linear combinations directly from the verified high-precision original Gram A and C. This is an independently checkable MODULE obstruction witness for that finite original source, not external peer review.

## Positive check for exact *one* denominator power

At full precision5^16, independently compare the Smith image of original A_odd with that of `[A_odd | 5*C_odd]` using the high-precision bigint Smith code. Require ALL capped elementary exponents equal and no censored old directions, hence `5 C_odd∈A_odd Z5^362`. Verify EVEN [A_even|C_even] has the same Smith profile as A_even with all grades resolved. These replays are intentionally redundant with Phase297-B and must not be used to tune the witness. They establish the exact power5 sufficiency, in addition to the dual failure at power1.

## Toy negative/positive controls and stop conditions

- Negative positive-definite Gram toy A=[10], C=[2]: with `ell=5^13 mod5^14`, `ell A=0 mod5^14` but `ell C=2*5^13≠0 mod5^14`. Multiplying C by5 makes it integral.
- Positive toy A=[10], C=[5] (full Gram [[10,5],[5,10]] positive): ell A≡0 implies ell C≡0 mod5^14, so no false obstruction.
- FULL k16 source and original-jet recovery must replay the existing K9 source and 6x6 exact original trace Gram; any row/index drift, dual annihilation failure or p*C membership failure stops the run.
- If there is NO such row-of-Smith-U witness, do not invent one; diagnose algorithm/basis and preserve failure. This is permitted as a test of the already observed proof, not authority to adjust original arithmetic source.

[P-paper] cokernel dual witness criterion; full-resolved finite Smith equals p-adic cokernel; exact exponent1 from order5 class and p*C inclusion.
[M after CI] explicit deterministic original odd-sector linear functional and direct original-Gram pairing residue certificate.
[H] any uniform bound across h1-admissible field discriminants or integral transverse projection at another D.
[R] treating the newly discovered image-index as an independent determinant factor or claiming Phase297 paper code is kernel-formal Lean.
