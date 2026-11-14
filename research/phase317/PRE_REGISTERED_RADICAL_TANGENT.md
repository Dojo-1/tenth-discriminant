# Phase317-C — frozen before code: radical first-lift form versus tangent Gram congruence

2026-11-14 Europe/Madrid. This protocol is recorded AFTER Phase317-A/B exact-head arithmetic CI first passed: native original D163 Gram mod25 and all five synthetic shifts k*(20,10) have SAME Smith depth counts (e0,e1,e>=2)=(23,7,10), despite 363 changed mod25 Gram cells for k=1,2,3,4. BEFORE Phase317-C code. This is not a new uniform field theorem.

## The invariant the two-digit Smith algorithm did not independently inspect

For the exact SAME original 40x40 integer-order source Gram G over Z/25, let \bar G = G mod5, rank23, with radical R=ker(\bar G) over F5 of dimension17. Choose any integral lift K (40x17) of an F5 basis for R. Then the 17x17 bilinear form

   B_G = ( K^T G K mod25 ) / 5  mod5

is well-defined: \bar G K=0, hence all entries are divisible5; changing K by 5 times an integral matrix does not change B_G mod5. The rank_F5(B_G) is exactly the number e1 of 5-adic Smith elementary divisors of valuation1, independent of the unit-pivot Schur method. Verify equality to e1=7 for EACH of the five native synthetic Grams, with a separate Gaussian-elimination nullspace implementation. Guard R dimension17, symmetry of B, rank basis17, and all entries of K^T G K divisible5.

For each gauge deformation Δ_k=(G_k-G_actual)/5 mod5 compute

   H_k = K^T Δ_k K  over F5.

Then B_{G_k}=B_{G_actual}+H_k, so H_k measures exactly the normal component of the gauge perturbation on the mod5 radical. Register the following ALTERNATIVES before inspecting numerical results:
 - If H_k=0: the deformation is tangent to the congruence orbit under U=I+5X (X over F5); demonstrate this by an independent constructive solvability test or a valid general lemma. No new first-lift form.
 - If H_k≠0: this synthetic perturbation changes the first radical-lift form even though its rank remains7; no claim it is a change of basis or a new Smith valuation.

## General paper-level linear algebra identity (5 !=2)

For symmetric G0 over F5 and its radical R, a symmetric H is in the image of

   T_G0(X)=X G0 + G0 X^T

if and only if H restricted to R×R vanishes. Necessity is obvious because G0 R=0. For sufficiency split V=U⊕R with G0=diag(A,0), A invertible. A symmetric H has blocks H11,H12,H21,0. Set X11=(1/2)H11 A^{-1}, X21=H21 A^{-1}, remaining X blocks zero. This constructs T(X)=H. This is classical tangent-orbit linear algebra; recording a working computational bridge is not a novelty claim.

Test the iff against hostile 2x2 and 3x3 singular symmetric matrices and a family of actual 40x40 G0 deformations; do not assert a complete general Lean theorem unless formally proved.

## Numerical evidence and stop rule

- Compute all 17 radical vectors by independent RREF and check their linear independence and G0 annihilation.
- Compute B_k and H_k for all five synthetic shifts, classify each as tangent or non-tangent from H_k=0 and record rank and first nonzero entry.
- Confirm B_k rank7 agrees with the prior independent 40x40 unit-pivot Smith e1=7.
- Apply an explicit invertible congruence U=I+5X to the ACTUAL G; confirm B_U= B_G and original Smith profile. This is a mandatory positive tangent control.
- Make a separate, deliberately non-tangent H with support on R×R, assert nonzero restriction; do NOT claim any forced rank change without computing it.
- Remain within fixed original D163 Q109/R40/S=J1; no alternate field, no new cutoff, no field-global uniform determinant theorem.

If any claimed radical size, lift independence, Smith rank, tangent iff control, or source equality fails, retire the relevant conclusion. [P-paper] tangent lemma and first-lift rank identity; [M] fixed finite field arithmetic if CI passes; [H] h1-only uniform residual valuation beyond inherited valuationWeight.
