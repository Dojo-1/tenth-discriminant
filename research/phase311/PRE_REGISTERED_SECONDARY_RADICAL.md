# Phase311-B — staged p-adic trace-radical filtration, post-A pre-code

2026-11-13. Preregistration after Phase311-A exact-head focused CI passed at PR203; BEFORE B implementation. This is a **finite same-source proof certificate**, not a new tenth-discriminant class-number-one bound.

Object: the SAME D203 original maximal-order Q263, R50/S=J2 100-row ordinary-jet source and its 50 exact /5 Frobenius-Hermite primitive lattice from Phase307/Phase311-A. Form its exact 100x100 primitive integral trace Gram modulo 5^3=125, from original E modulo 5^4=625 to preserve all divided-row digits.

## Prediction (already implied by earlier Phase307 Smith profile, now independently checked by a DERIVED RADICAL algorithm)

1. The Gram rank over F5 is 63. Over Z/125, a symmetric unimodular congruence can eliminate exactly 63 *unit* directions, leaving a 37x37 Schur complement S with every entry divisible by5.
2. Divide S by5 to produce T1 over Z/25. Its F5 rank should be 36, yielding 36 additional valuation-one directions and a 1-dimensional radical.
3. Remove the 36 unit directions from T1 and divide its remaining scalar by5; the final 1x1 form T2 modulo5 should be NONZERO. This resolves the final valuation-two direction and proves primitive Smith exponents {0:63,1:36,2:1}, with exact primitive determinant v5=38.
4. The exact original source Gram is related to primitive one by an **integer unimodular source frame and 50 exact 5-divisions**, giving original Gram v5=2*50+38=138. Verify the exact matrix identity modulo 5^4 using the actual source, not just the valuation sum.
5. Distinguish first-stage bound v5>=137 from the second-stage exact result138. The extra unit is the single surviving secondary radical, NOT independently addable to valuationWeight45.

## Independent checks, equivalence attacks and kill

- Implement staged symmetric Schur congruences using explicit invertible unit pivots modulo p^k, including a hostile off-diagonal-only unit block that needs a congruence shear to expose a unit diagonal. Do not assume every unit appears on a diagonal.
- Verify known-answer diagonal [1×63,5×36,25] and a small off-diagonal [[0,1],[1,0]] plus a 0-matrix with censored level. Apply at least two independently chosen unitriangular source-coordinate changes and demand identical level counts.
- Cross-check with the Phase310 generic modular DVR Smith elimination as a **different algorithm**. Both code paths remain AI-authored, not an independent mathematician.
- Original source is exactly Phase304, and the primitive 50-row basis exactly Phase307; no new sample points, no altered jets.
- If any residual divided entry is not integral mod5, any pivot congruence fails, or final scalar vanishes, RETIRE the exact 38/138 stage result until corrected. Do not silently lift precision or add higher ontology.
- No h1 theorem, no original cutoff change, no main merge, no Work mode.

Evidence [P-paper] standard local DVR symmetric congruence/Schur determinant identity; [M after CI] actual 100x100 staged radical and source factorization; [S] higher tendril/derived-radical analogy (NOT actual cohomological Bockstein); [H] universal h1 field mass.
