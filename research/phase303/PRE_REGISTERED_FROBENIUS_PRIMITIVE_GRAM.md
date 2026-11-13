# Phase303-E — preregister exact Frobenius primitive-Gram explanation of p5 mass30

**2026-11-13, AFTER Phase303-A/D both passed and BEFORE Phase303-E code/results.** Separate preregistration, not an ex ante prediction of Phase303-A's full maximal-order Smith `{0:25,2:15}`. Keep D163, rho21=norm≤441, J=S1, original 40 Z^r monomial labels, maximal-full Q225 and original-even Q109 matched, p5 K16, frozen code. No Work, merges, cutoff edits, hidden source resampling or extra arithmetic factor.

## Exact classical Frobenius identity and proposed mechanism [P-paper]

At inert p5, residue `O_K/5 ≅F25`, every residue z satisfies `z^25=z`. Consequently for 25≤r≤39 and **EVERY ACTUAL maximal-order sample z**, the polynomial evaluation
```
  F_r(z)=z^r−z^(r−24)
```
is divisible by5 in both integer ω coordinates. The row operation `Z^r↦F_r` is an integral **UNIMODULAR** change on the ORIGINAL 40 monomial row lattice, while dividing those 15 rows by5 is a separate NON-unimodular evaluation-lattice saturation. Let `Eprim` consist of first25 original monomial evaluation rows and last15 divided difference rows `F_r/5`; let `D5=diag(I25,5I15)` and U the unipotent row subtraction matrix. Then the EXACT original observation/trace Gram satisfies
```
  U*G_original*U^T = D5 * Gprim * D5,
  Gprim = Eprim * Bω * Eprim^T.
```
The primitive Gram is on a NEW evaluation superlattice, not the original arithmetic row basis. Therefore
```
v5(det G_original)=2*15 + v5(det Gprim).
```
If Gprim is unimodular modulo5, the determinant is EXACTLY 30. To explain ALSO the Smith profile `{0:25,2:15}`, require additionally the first25 principal primitive Gram mod5 be nondegenerate; then Schur integration over that unit block proves precisely 25 exponent0 and15 exponent2. This is a small classical linear algebra lemma, not a novel number field theorem. A code path that only checks a determinant and not primitive rank is insufficient.

## Source-faithful implementation gates

1. Pin `research/phase303/maximal_order_source.py` blob `e68f66dac1c914a97c0fe93655a693053f80386f` plus its existing frozen original source/jet helpers. Rebuild BOTH actual maximal-even Q109 and maximal-full Q225 source Grams (all1600 entries) with the exact original Bω and independent moment oracle. Check even mapped old source equals original integer-order Gram as in A.
2. For EVERY one of 15 Frobenius differences and every actual sample (both EVEN and FULL arms), verify z^r−z^(r−24) divisible5 in BOTH ω coefficients: 15×2×225 (full) and 15×2×109 (even) raw-coordinate checks. Preserve field/Frobenius identity; no on-the-fly adjustment of which 15 rows to divide.
3. Define Eprim modulo5^15 by dividing those actual original modular differences by5, and keep first25 undivided. Independently compute rank over F5 of Eprim and Gprim and rank of its 25×25 leading principal Gram via standalone F5 Gaussian elimination. On FULL Q225, **predict** both ranks40 and leading block rank25 from the observed previous Smith profile; verify or REFUTE this explanation. On EVEN Q109, record whatever ranks occur: the previous spectrum `{0:15,2:8,3:7,4:10}` implies extra degeneracies, but do not preregister their values.
4. Direct original source trace contraction recomputes every Gprim entry modulo5^15 with Bω=[[2,1],[1,82]], without using Smith-column changes to the observation metric. Rebuild U G_original U^T on the ORIGINAL 40-row Gram, then check all1600 entries against D5 Gprim D5 modulo5^16; for the top25 block (not scaled) compute with original full precision modulo5^16 to avoid precision loss in Eprim. No changed support/metric.
5. Reconfirm full ORIGINAL Gram p16 Smith profile `{0:25,2:15}`, original v5=30 and prime determinant unit of Gprim. Verify old EVEN still matches old integer-order v5=77 with its own recorded primitive rank deficiency. Do NOT promote a different Eprim Gram as a new original field determinant, and do not interpret the 15 Frobenius row factors as new field cutoff mass.
6. A hostile control that only checks mod5 divisibility but not Gprim unimodularity is insufficient: reuse EVEN support, where the 15 Frobenius divisions exist but the primitive rank is not automatically40. Report that source-dependent failure of rank recovery rather than forcing original spectrum to 0^25/2^15.

[P-paper] inert Frobenius + unimodular source-row subtraction + diagonal p5 saturation determinant and Smith proof if unit blocks; [M after CI] exact original Q225/Q109 source and primitive Gram rank/metric checks. [H] uniform high-J/h1 class-number-one arithmetic constraint; [R] equating divided observation rows to the original arithmetic row lattice, adding p5 factors as new cutoff improvements.
