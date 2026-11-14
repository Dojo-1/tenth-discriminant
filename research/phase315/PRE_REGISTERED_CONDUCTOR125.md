# Phase315 — preregistered second 5-adic wild logarithm and SAME original Gram mod25

Date 2026-11-14 (Madrid). This document is committed BEFORE Phase315 source or measurement. Branch stacked on Phase314 PR #206 exact head a5b062937629a45a093e6922772bc06280cf12da; Phase314 candidate for research-only merge into Phase313 after green CI. No main merge or changed reported 322^4 bound.

## A. Exact conductor 125 arithmetic

For imaginary quadratic O=Z[omega] with D>3 and 5 inert, write omega²-omega+m=0, m=(D+1)/4. For every unit z modulo125, define the quadratic Frobenius defect

    d(z) = [(z^5-conj(z))/5]/conj(z)  mod25  in O/25.

All divisions by5 are performed first in O/125, exact as integer components. The final division by conj(z) is only in the unit ring O/25, using norm inverse. Predeclare:

    d(x*y) = d(x)+d(y)+5*d(x)*d(y)     mod25;
    L(z) = d(z) - (5/2)*d(z)^2         mod25;
    L(x*y) = L(x)+L(y)                 mod25;
    L(-z)=L(z), L(conj(z))=conj(L(z)).
    L(z) mod5 = Phase313 normalized delta_5(z).

Here 5/2 denotes 5 times inverse of2 in Z/25, a well-defined residue 15.

The signed conductor125 ray-unit group should have 7500 elements, and the pair
  (signed tame residue z mod5/±, L(z) mod25)
should give an explicit C12×(Z/25)^2 group isomorphism. Check all 15000 units of O/125, every group-class fiber, a full tagged inverse lookup, and unit-product hostile controls over D163 (h1), D183 (h8), D187 (h2) if execution permits. Separate field statuses and report exact checks. Conductor250 adds the inert2 C3 group, yielding 22500 signed ray classes. Do NOT claim any class-number-one theorem from these local groups.

## B. SAME original integer-order source at precision25

For D163, original Q109 rho21 R40/S=J1 lies in the suborder O'=Z[sqrt(-163)] with exact omega embedding (x-y)+2y omega. Re-evaluate the ORIGINAL 40×218 integer coordinate source modulo125, perform the SAME 15 exact integer-unimodular Frobenius25 row shears Z^r-Z^(r-24), r25..39, and /5 divided rows. The resulting primitive E and the original Hermitian trace Gram Gprim mod25 are fixed oracles, NOT substitute maximal-order sources.

Reconstruct Gprim mod25 from signed conductor125 unit ray counts:
 - for unit z, the full (tame z mod5/±, L(z) mod25) tag uniquely determines the two signed generator residues ±z modulo125 and thus all its original 40 divided primitive row values mod25;
 - for 5-divisible observations, conductor125 UNIT tags are undefined; retain a separate first-nonunit-lift u=z/5 modulo25, not merely modulo5. Reconstruct those actual original source rows directly;
 - sum signed-pair and nonunit primitive trace contributions, compare ALL 1600 entries modulo25 to the unchanged native integer-order oracle. Check reduction modulo5 against the Phase314 78-moment result, rank23 and original v5=77 remain unchanged.

Prove by a direct fixed residue pair e.g. z=1 and z=26: they have equal first-level ray25 signed tag but different second-level L modulo25, and their ORIGINAL primitive signed-pair Gram contributions differ modulo25, while agreeing modulo5. If this exact chosen witness fails, record it and seek a separate predeclared bounded sweep for an actual collision, not data manipulation.

## C. Global conductor 250 class-one ray transport

On the ACTUAL maximal-order D163 radius21 Q225, classify all principal ideals coprime10 by 2-adic F4 unit and signed conductor125 tag (22500 possible conductor250 classes). Under h1, exact full ray250 norm-shell distributions must convolve at all 270 eligible coprime norm products mn<=441. Compare each total against the independent quadratic Kronecker ideal coefficient. THEN apply mod2 residue1 selection for odd norms; add even-norm prime-to5 elements in O' and 5-divisible source observations as typed strata. The resulting counts must reconstruct the SAME original Gprim mod25. This does NOT imply extra 5-adic valuation: it is a stronger information-preserving bridge only.

## D. Negative controls, information loss and theorem gap

- The OLD 78-moment map over F5 is not asserted sufficient mod25. Compare pairs with identical first-level tags and distinct second-level Gram cells.
- Local ray group classification cannot see class number: use nonh1 D187 with primes2/5 inert and principal-only convolution failure at norms11×17=187. Optional source-matched D183 h8 remains a negative for v5=77 specificity.
- The additive L coordinate is a **corrected truncated p-adic logarithm**; at depth2 the *raw* normalized defect d is NOT additive. Check its nonzero 5*d(x)d(y) cross term for some actual units.
- If any exact source, congruence, product, signed-unit enumeration, conductor2 gate, or original 1600 Gram cell fails, STOP and retire the affected bridge.

[P-paper] truncated logarithm and ray-unit product identities under inertness, original source-row algebra; [M only after exact-head hosted CI] bounded unit/class enumeration and original Gram congruences; [H] any uniform class-one-specific determinant valuation beyond old valuationWeight. No claim of novel published math or enhanced intelligence. No main merge; 322^4 unchanged.
