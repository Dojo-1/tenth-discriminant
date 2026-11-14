# Phase318-D — POST-C, PRE-code: canonical 3⊕4⊕10 splitting of the resonance pencil

Recorded 2026-11-14 Europe/Madrid AFTER focused run 43592094267 succeeded, BEFORE the Phase318-D code. Previous C-results are OBSERVATIONS, NOT retroactively preregistered: on native D163 original mod5 Gram radical R=F5^17, B0 has rank7, N (the unique normal-image generator in a fixed deterministic basis) has rank4, and B0+3N has rank3. For lambda≠3 it has rank7; the explicit standard-coordinate 7×7 minor equals 4*(lambda-3)^4. Synthetic prime characters at 53 and227 select lambda3; actual h1 D163 generator spectrum corresponds to lambda0. No uniform field theorem or new bound.

## PRE-code theorem candidate and complete expected certificate

Let B_res=B0+3N. Under the MEASURED three exact hypotheses
  rank B_res=3, rank N=4, rank(B_res-3N)=rank B0=7
over characteristic5, the two symmetric linear maps B_res,N have disjoint images and row spaces:
  rank([B_res N])=rank B_res+rank N=7.
Their common kernel has dimension17-7=10. Since both maps are symmetric, restriction of B_res to ker N is nondegenerate modulo the common kernel (3d quotient), and restriction of N to ker B_res is nondegenerate modulo common kernel (4d quotient). Thus a common basis can split the entire 17d radical into
   W3 ⊕ W4 ⊕ W0, dim=(3,4,10),
with W3⊂ker N, W4⊂ker B_res, W0=ker N∩ker B_res,
and with both forms block diagonal:
   B_res=diag(A3,0,0), N=diag(0,A4,0)
where A3,A4 nonsingular.

Then for all lambda in F5
   B_lambda=diag(A3, (lambda-3)A4, 0_10).
This proves fixed-rank 3+4 when lambda≠3, rank3 when lambda=3, and a nonzero 7x7 block minor equal to det(A3)*det(A4)*(lambda-3)^4. This is an elementary finite-field linear-algebra consequence, not novel number theory. It is NOT a statement that B0 corresponds to the integral full original Gram at arbitrary depth.

## Frozen operations and falsifiers

1. Rebuild the SAME actual native D163 original mod25 Gram and fixed 17d radical, N using first lexicographic nonzero local normal site. Assert all three rank hypotheses (3,4,7), stacked row/column rank7, and common kernel dimension10.
2. Independently construct kernel bases ker(N) (dimension13), ker(B_res) (dimension14), and common kernel (dimension10) via the verified F5 RREF. Complete W0 to W3 inside ker(N) and to W4 inside ker(B_res) deterministically, then form an invertible 17x17 basis P.
3. Check every one of 17x17 entries of P^T B_res P, P^T N P and all FIVE P^T B_lambda P against block formulas. Confirm A3 rank3, A4 rank4, and their determinants nonzero using independent modular elimination.
4. Compare the block determinant polynomial to the earlier frozen standard 7x7 minor 4*(lambda-3)^4: the scalars may differ by change of basis, but both must have the SAME degree-four resonance factor and nonzero leading coefficient.
5. Include a deliberately NONCOMPLEMENTARY symmetric pencil as hostile control, for which ranks do not add and common splitting criterion must reject; do not silently present every pair of symmetric matrices as simultaneously block-splittable.

Any mismatch retires the claimed precise splitting. Distinguish [P-paper conditional finite-field lemma], [M] exact source, split matrix and CI, [H] any class-one-specific uniform large-D residual determinant effect. Preserve original v5=77, inherited valuationWeight, reported 322^4 bound and no-main-merge policy.
