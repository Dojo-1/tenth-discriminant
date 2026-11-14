# Phase318 — preregistered BEFORE code: complete local wild normal map and split-prime character controls

Date 2026-11-14 (Madrid). Branch based on research-only Phase312–317 consolidation merge 9bd893c9fdb893b7d75873884cc36937bb6005a4 into Phase311. Main untouched; no alteration to the reported 322^4 field bound.

## The precise missing distinction

Phase317 showed that a **single prime-41 global character** multiplied by each of the five trace-zero second-wild increments changes 363 primitive entries of the SAME original D163 Gram mod25 but lies in the congruence-tangent space, with explicit GL40(Z/25) witness. This does NOT imply that ALL norm-preserving local second-depth deformations are congruence-tangent, or that ALL multiplicative, conjugation-covariant principal-ideal characters are tangent.

We pre-register a complete local linear test and a finite family of globally multiplicative characters, keeping the inference directions distinct.

## Fixed, original source and mathematical setup

D=163, O_K=Z[omega] with omega^2-omega+41=0, 5 inert. Original order O'=Z[sqrt(-163)], rho21, Q109, R40,S=J1, 15 exact Frobenius25 /5 primitive row divisions. Fix SAME original 40x40 integer-order primitive Gram G mod25 and its mod5 radical K=ker(G mod5) of dimension17, with first radical form B=(K^T G K mod25)/5 mod5 of rank7, as independently checked in Phase317.

For every actual signed 5-unit observation z in Q109, all local lifts preserving BOTH the signed conductor25 tag and the norm mod125 have the form z' = z + 25h mod125, where h in O_K/5 and

   Tr(h conjugate(z)) = 0 (mod5).

Because 5 is inert and z is a 5-unit, the trace functional is nonzero and its kernel is a ONE-DIMENSIONAL F5 line. There should be precisely five h per signed site. We do NOT require z' to be an actual global integral generator at the same integer norm, only a locally norm-compatible residue. CRT accommodates the old conductor2 suborder selector because 2 and 125 are coprime. Every nonunit z=5u remains in its own immutable typed stratum.

## A. COMPLETE finite site-level differential and the normal map

- Enumerate all 50 actual signed unit sites and nine 5-divisible observations (2*50+9=109).
- For EACH site, enumerate all 25 residues h=(u,v) mod5, prove exactly five satisfy trace0, choose a deterministic nonzero basis h_i. Verify k=0..4 has preserved native signed first-wild tag (mod5), local norm mod125, and original per-site primitive Gram mod5.
- Define delta_i(k) = [G_site(z_i+25*k*h_i)-G_site(z_i)]/5 mod5, with both ± generators counted. Check delta_i(k)=k delta_i(1) over F5 and each 40x40 matrix symmetric.
- Restrict H_i=delta_i(1) to the FIXED original 17d radical: N_i=K^T H_i K over F5. Compute the exact rank of the span of ALL 50 normal matrices, flattened in symmetric upper triangular coordinates, and count sites with nonzero N_i. DO NOT preregister whether the rank is zero, positive, or whether a perturbation changes Smith e1.
- Build the CONJUGATION-COVARIANT subspace of the site perturbations by matching each selected site to the exactly conjugate signed site, taking care of global ± orientation. A rational self-conjugate site admits no nonzero trace-zero self-compatible local change; a purely imaginary self-conjugate class may. Compute rank of its normal image separately, with a full site-pair covariance test, not a handwave.

## B. FINITE global split-prime character family

- Independently enumerate every actual maximal-order principal prime-norm generator pi with norm p<=rho^2=441, p prime, 5∤p and pi not associate to its conjugate; this is a finite source-derived list, not an asserted complete set of global Hecke characters.
- For each such pi define exact (NON-modular) principal ideal valuation character nu_pi(z)=v_(pi)(z)-v_(conjugate pi)(z), by repeated exact integer quadratic division using z*conjugate(pi)/p. Verify multiplicativity on actual original generators times fixed controls, sign invariance, conjugation antisymmetry, and distinction from the p41 character.
- Shift the ACTUAL signed conductor125 ray tag by nu_pi(z)*t, t=5*(-1+2omega)=(20,10) mod25. Use the complete local 15,000-unit lookup to reconstruct each shifted residue modulo125. Check local norm125 preservation, unchanged first wild digit, and that its per-site perturbation belongs to the above 1d trace-zero lift line.
- For EACH active pi (nonzero character on native Q109), reconstruct the SAME original 1600-cell primitive Gram mod25, calculate the first radical form and the normal restriction; record whether the synthetic Gram differs and whether e1 changes from7. Compare the global normal matrix exactly against the linear combination of the 50 independent site normal directions.
- Verify FULL global conductor250 norm-shell convolution for a frozen, deterministic subset of up to the first THREE active split primes at native radius21, and the 41-prime control; check all270 eligible norm pairs and all177 independent ideal mass coefficients per tested character. For other primes, valuation multiplicativity is exact algebra, but no blanket 270-pair replay is claimed.
- Distinguish:
  * arbitrary locally admissible site shifts;
  * those respecting conjugation;
  * globally multiplicative split-prime valuation characters;
  * ACTUAL integral generators of exact norm.
  Neither of the first three automatically satisfies the fourth.

## C. Stop rules and evidence

Reject any mismatch in original G, Q109, exact /5 divisions, local 5-element lift line, norm residue, signed pairing, conjugation covariance, exact ideal valuation or rank computation. If ALL local or all global character normal directions vanish, preserve that negative result; do not manufacture a class-number-one valuation gain. If a global synthetic character changes first radical form/e1, that is a coherent NO-GO for earlier incomplete constraints, NOT a new real field or h1 theorem.

[P] quadratic norm-differential formula and tangent congruence linear algebra (elementary, not novel); [M after exact-head CI] complete 50-site normal spectrum and finite prime character family; [A] h1 for D163 imported to identify all ideals as principal in the norm shells; [H] truly uniform class-one-specific new primitive Gram valuation beyond valuationWeight; [R] previous gauge family as exhaustive of admissible perturbations.

No direct leap to p-adic depth3, no new field cutoff, and no main merge.
