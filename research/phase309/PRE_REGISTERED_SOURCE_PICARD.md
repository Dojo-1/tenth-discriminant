# Phase309 preregistration — original-source Picard minor and the Gram-blindness control

Date: 2026-11-13. Written BEFORE Phase309 experiments, tests, Lean proofs, or claims of CI success. Draft stacked on Phase308 PR #200, pinned source head 813df66ea3d1944fd42c9b90765c2cd3d59398ac.

The user requested a creative continuation of Tendrils + Worldlets, but the exact objective is to find a *faithful, falsifiable* mathematical interface from an **unchanged ORIGINAL polynomial source** into the genuine arithmetic ideal/Picard obstruction, and to test whether the ORIGINAL trace Gram detects it.

## Frozen data and precise types

At D203 use the Phase304 frozen 100-row R50/S=J2 original maximal-order evaluation at all Q263 norm-ball observations, with omega²=omega-51 and the original ordinary Z jets. Select existing original row labels (r,s)=(0,0) and (1,0), original row indices 0 and 2. Restrict only the j=0 observation coordinates to exactly three ACTUAL points z∈{0,3,omega}. This gives an original Z-linear 2x3 omega-valued evaluation block E. Extend **coefficients** by the explicitly named scalar extension O⊗_Z Z²=O² so the restricted map is O-linear:

    A: O² -> O³,   A(a,b)=(a,a+3b,a+omega*b).

This is a faithful submap/extension of the original **E**, NOT an assertion that the original Z-source or full 100x100 integer Gram is an O-free source.

## Predicted mathematical theorem / counterworld

Let O=Z[omega] be a maximal quadratic imaginary order with omega²=omega-m, and select a rational prime p and r∈Fp such that f(r)=r²-r+m≡0 modp and f'(r)=2r-1≠0 modp. Set z=omega-r and ideal I=(p,z) (norm p). Provided all three points {0,p,z} are in the original source's ACTUAL observation set and row labels 1,Z exist, the selected original j=0 2-source/3-observation block is

    A_{p,r}=[[1,0],[1,p],[1,z]] over O.

1. The three 2x2 minors are p,z,z-p, and generate **I**. Their O-ideal's integer Z-index is p. Thus the local maximal-minor Fitting ideal has genuine Picard class [I].
2. Its K-linear image saturated inside O³ is

    Sat_O(im A) = { (a,a+pb,a+zb) : a∈O, b∈I^{-1} }
               ≅ O ⊕ I^{-1}.

   Consequently it is **nonfree** iff I is nonprincipal. In D203/p3/r0, [I] has exact class order4 by Phase308. This is a **canonical restriction of original source observations** plus explicitly typed O-linear scalar extension, not the optional fabricated direct sum I^100 of Phase308.
3. The original **integer trace-Hermitian Gram** for these TWO rows and THREE points is exactly

    G=[[6,2p+1-2r],
       [2p+1-2r,2(p²+f(r))]],

    det G = 12(p²+f(r)) - (2p+1-2r)².

   Since f(r)=0 modp and 2r-1≠0 modp, **det G modp = -(1-2r)² !=0**. Thus a genuinely nonprincipal Picard observation-patch obstruction can coexist with p-adic UNIT trace Gram determinant. This directly refutes the naive proposed bridge "Picard torsion adds positive v_p(det G)" even on the same selected patch.
4. Enlarging the actual patch by observation z=1 adds a unit 2x2 minor det[[1,0],[1,1]]=1, so the maximal-minor ideal becomes O and its saturated image becomes FREE. The **FULL original Q263 source contains z=1**, so this particular obstruction does NOT extend to the full 100-row source. Do NOT advertise an improved field theorem.

## Prediction table (frozen before tests)

- D203, p3, root r0, z=omega, N(z)=51: patch minors I=(3,omega), nonprincipal order4; G=[[6,7],[7,120]], det671=11*61; det mod3=2 (unit). Actual points {0,3,omega,1} and row indices0,2 MUST be present in frozen Phase304's actual source. Check every selected original evaluator coordinate modulo3^6 against independently evaluated O arithmetic; optionally the exact integer row-jet coordinates.
- D187, p7, root r2, z=omega-2, N(z)=49: selected native-original row 1,Z and actual norm-ball points; [I] order2 by Phase308, G=[[6,11],[11,196]], det1055, det mod7=5. Source policy rho/R/S/J from Phase206 params must contain required rows and observations. NOT a claimed frozen Phase304 full 100-row field.
- D167, p2, root r0, z=omega, N(z)=42: selected native-original row 1,Z and actual points; [I] order11 by Phase308, G=[[6,5],[5,92]], det527, det mod2=1. Check simplicity f'(0)=-1 mod2.
- D163, p41/r0, z=omega: ring-level PRINCIPAL boundary (I=(omega)), but the full original source radius is too small to include z=p41. This case MUST be explicitly rejected as an original-source subpatch (otherwise the bridge invents observations).

## Controls and proof status

- Independent integer O multiplication, conjugation and trace oracle for every patch; original Phase304 source for D203, Phase206 original params for D167/187, with unchanged source indices and j0/j1 policy. Do not silently replace original source or field-hypothesis.
- Independent ideal Z-index via gcd 2x2 minors of O-multiplication closure; compare p. Certify nonprincipality with exact norm lower bound and previous Phase308 ideal-power certificate, do not use the Gram determinant to certify class order.
- Hostile controls: add actual observation z=1; replace p by a non-root; omit field discriminant; confuse O-Ideal saturation with original integer source; attempt to read Picard class from determinant valuation. Each MUST fail or be explicitly marked a different map.
- Lean target: isolate a general field algebra lemma that the reduced 2x2 trace Gram determinant is -f'(r)^2 and nonzero for a simple root. Kernel compilation of this local polynomial identity does NOT prove an O-ideal theorem, nor the field-discriminant cutoff.
- Root Lean CI on exact PR head and focused CI must be separately reported. No merges, no edits to original source or 322^4 bound, no self-grading.

Evidence [P-paper conditional] elementary algebra and saturation proof; [M after CI] exact numerical patches and hostile controls; [H] a new globally non-overlapping Picard-to-same-Gram field bound; [R if tested] 'nonprincipal Picard class forces p-divisibility of restricted trace Gram'. All novelty claims unverified; classical determinantal ideals/Steinitz are prior mathematics.
