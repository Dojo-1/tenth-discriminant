# Phase313-F — post-E, pre-code independent EXACT INTEGER determinant witness

2026-11-14. Phase313-E focused CI run 43567630702 passed 23 tests and produced EXACT original h1 D163 integer-order Gram v5(det)=77, primitive Smith {0:23,1:7,4:10} plus 15 exact /5 divisions. This is a NEW independent-determinant audit protocol BEFORE Phase313-F source code and before its result.

Compute the original 40x40 integer Gram EXACTLY in arbitrary-precision integers, not only modulo5^k and not through the Phase310/311 DVR algorithms. Enumerate independently the 109 original integer Q={(x,y):x²+163 y²<=441}, and recursively evaluate the exact 40 polynomial powers z^r over Z[sqrt(-163)]. For original monomials 1,Z,...,Z^39 (J=S1), form exact symmetric G_{rs}=Σ_{z∈Q}2(a_r a_s+163 b_r b_s) with z^r=a_r+b_r sqrt(-163).

Exploit the sign symmetry Q=-Q to obtain two EXACT 20x20 parity blocks. Confirm every odd-even cross entry is mathematically zero (not merely mod5). Compute both exact determinants with a DIFFERENT fraction-free integer determinant implementation (Sympy DomainMatrix/Bareiss), check nonzero and v5 of the two integers separately; require their sum to be EXACTLY77, as independently predicted from the prior mod5^6 index+Smith calculation. Do not choose different points or source to make it match.

This independently verifies the original determinant valuation, not the detailed 40-row Smith histogram, and does not replace external human mathematical review or prove a uniform class-one bound. Kill if any source, parity, exact determinant or valuation discrepancy arises. Record exact block valuations and determinant unit residues mod5, but not the vast determinant decimal expansions.
