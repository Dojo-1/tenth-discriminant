# Phase313-H — post-A–G pre-code: the missing conductor-2 order selector

2026-11-14. This is a correction preregistered AFTER Phase313 A-G arithmetic and exact D163/D183 5-adic matched controls succeeded, and BEFORE H code. Earlier finite map from ORIGINAL integer-order selected ray counts to its original Gram was exact, but the global h1 ray norm-shell convolution was computed in the MAXIMAL order. Passing that convolution through the suborder sample selection WITHOUT a conductor-2 gate is NOT justified. This document freezes the correction, not a retrospective rewrite.

## Exact order inclusion, field D163 h1

K=Q(sqrt(-163)), O_K=Z[omega], omega=(1+sqrt(-163))/2, m41, while the original Lean integer source uses O'=Z[sqrt(-163)]=Z+2O_K. In omega coordinates z=a+b omega, membership z∈O' iff b even. At p2, minimal polynomial omega²-omega+41 modulo2 is X²+X+1 irreducible, so O/2=F4 and its unit group has order3.

For any z of O:
 - if Norm(z) is odd (z mod2 nonzero), then z∈O' iff z mod2=1 in F4;
 - if Norm(z) is even, then 2 is inert so z divisible2 and z∈O' automatically.

At radius rho21, ORIGINAL integer ellipse Q109 must equal the subset of the 225-point maximal-order ellipse with even omega coefficient b; these are EXACTLY identical representations of the same geometric norm constraint. Verify both enumerations and complete norm-shell classifications.

## Conductor50, the correct global h1 carrier

CRT and units ±1 give

 (O/50)^× / ±1 = (O/2)^× × ((O/25)^×/±1)
               ≅ C3 × C12 × C5²,

900 signed ray-unit classes. For every maximal-order principal ideal of norm coprime10, tag its generator (up to ±) by F4 residue and the Phase313 conductor25 tame/wild tag. Under h1, all ideals are principal; full 900-component ray distributions C50_n satisfy convolution for coprime m,n with 10∤mn. Verify EVERY eligible pair mn≤441, and independently compare total coefficients to Kronecker a_K(n).

To reconstruct the ORIGINAL integer-order primitive Gram, first select the correct prime-to5 principal-ideal tag counts:
  * odd norm prime-to10: project the full 900-class ray spectrum to F4-residue1;
  * even norm prime-to5: all maximal-order elements are divisible2 and automatically lie in O', so take their full conductor25 ray count;
  * 5-divisible observations: retain the existing separate z/5 mod5 first-lift stratum, AFTER selecting O' (b even).

Compare ALL 300 selected conductor25 tag multiplicities plus the 25 nonunit counts with the previous exact selected-original Q109 census. By the existing proven-in-code linear map, the same original 40x40 primitive Gram must follow. The selection is NOT a group homomorphism; it is a projection of full ideal-shell data. This is the corrected global-to-original bridge.

## A rigorous counterexample to pushing the convolution through selection

Although K has h=1, original suborder O' does NOT satisfy the naive norm-shell convolution. Maximal-order elements omega (norm41) and 1+omega (norm43) are BOTH outside O' (odd omega coefficient), but

 omega*(1+omega)=2omega-41=-40+sqrt(-163) ∈ O',

with Norm=41*43=1763. Since 41 and43 are nonsquares below163, there are NO original integer-order elements of norm41 or43, yet an original integer-order element of norm1763. Coprimality gcd(41,43)=1 holds. This is outside the rho21 experiment but an EXACT algebraic counterexample to the invalid global transport.

## Kill / evidence / status

Stop if Q109 != {Qmax225: b even}, mod2 unit field has other than three units, any 900-ray norm-shell convolution fails, projected signed unit+nonunit census disagrees with original, or the 41*43 original-suborder counterexample fails. No field-cutoff improvement, no claim original suborder is Dedekind, and no unqualified inference h1=>convolution on suborder-selected principal ideals. All previous source-specific Gram and exact determinant77 measurements remain intact; only the meaning of the global bridge is corrected.
