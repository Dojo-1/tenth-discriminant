# Phase301-B — preregister a short original D163 dual witness for the FIRST jointly nonintegral row

**2026-11-13. AFTER Phase301-A exact focused CI #43387766296 PASSED, BEFORE Phase301-B code/results.** This experiment is deliberately POST-result: `(n,s,t)=(13,27,31)` was the FIRST positive item in Phase301-A's fixed and complete 176-case scan, not a prespecified counterexample. Preserve that provenance. Do not change the field/source, select a different witness case after result, or promote the finite source finding to a field-uniform inequality. No Work/merge.

## Frozen original source and already observed facts

Use original D163 integer-order R40/S=J1/Q109 rho21 and trace metric diag(2,326), with all 40 monomial rows, and the parent Phase301-A script blob `acd72002911b284bea6fda100435f552756c1532`. Parent Phase300/298/297/206 frozen source guards must pass; reconstruct original G40 by TWO methods (source_probe mixed moments and actual raw original E/metric), check all1600 entries and exact parity zero.

Prior source experiment showed:
- old L14=<1,Z,...,Z^13> has BOTH original Z^27 and Z^31 separately integrally projectable over Z5; their original cross columns lie in image G(L14).
- adjoin original Z^27 to form the primitive **NONCONTIGUOUS** L15=<1,...,Z^13,Z^27>. Then the original Z^31 cross column is NOT in the image G(L15) over Z5; exact defect/order5. Its scalar Schur conditions v5(S27)=3 and v5(R27,31)=2 were source-derived and matched the independent full Gram Smith.
- all Gram Smith exponents are uncensored at p16.

## New independent linear dual target (unknown vector until execution)

Let `A15=G40[rows,rows]` with rows `[0,...,13,27]` (15 original monomials), `c31=G40[rows,[31]]`. Using the original-basis tracked Smith row matrix U for A15, identify the FIRST deterministic row `ell` at some Smith grade e<16 with
```
ell * A15 ≡ 0 (mod 5^e) IN ALL 15 original columns,
ell * c31 ≠ 0 (mod 5^e).
```
Print the FULL 15-vector modulo 5^e (small enough for human inspection), the modulus, first failing original row Z31, exact residue and valuation, and SHA256. Crosscheck from the ACTUAL source rows: build `f=Σ_i ell_i E_(original row_i)` over the original 218 observation channels and original weights (2,326); require each of the 15 pairings with original old E rows vanish modulo5^e and pairing with actual E31 is identical and nonzero. Thus the nonintegral projection is independently refutable by a short finite arithmetic certificate rather than merely histogram differences.

Also independently solve original L14 projection equations for BOTH y27 and y31 with integral coefficients modulo5^16, directly checking all original old Gram equations, so the counterexample is explicitly pairwise-integral but jointly-NONintegral. Reject a synthetic or source-normalized metric.

## Additional source bounds / stopped outcomes

If the old A15 grade≥16 and the source cannot resolve it, mark inconclusive and stop; do not increase precision post hoc. If the reported first positive Phase301 case is not reproduced or no dual witness is found, preserve failing CI and investigate the actual source. The witness may use any Smith grade e that detects the class; do NOT preclaim e=3 merely from the scalar S27 valuation3. Source exact integer > mod5 checks remain mandatory.

[P-paper] dual functional obstruction c∉A Z5^n and conditional Schur residual lemma.
[M after focused CI] concrete original 15-vector, source-native 218-channel trace pairing verification and positive original L14 projections.
[H] class-number-one maximal-order or higher-J uniform inequality.
[R] interpreting mod5 periodicity or isolated integrality as universal simultaneous saturation.
