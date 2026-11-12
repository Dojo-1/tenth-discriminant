# Phase286 — preregistered exact dyadic theta and maximal-order coset certificate

**Registered 12 Nov 2026 before Phase286 implementation.** Phase285's finite original-source Noether lens/ordinary-jet moment controls and paper-level Gaussian shell estimates are prior art in draft PR #176; this PR is a **separate exact-rational analytic test** and DOES NOT alter the original D403 trace Gram, its 400 rows, its jet convention, or the 321^4 bound candidate. Scope is fixed before code. All proposed proofs and programs are AI-assisted and have no independent human referee review.

## Frozen geometry / source

For squarefree D congruent 3 mod 4, use the embedded order Lambda=Z[u], u^2=-D, and full maximal order O=Z[(1+u)/2]=Lambda disjoint_union (((1+u)/2)+Lambda). Test exactly (D,rho)=(19,5) and (403,40). Integer disk Q0 consists of x²+D*y² <= rho²; the symmetric lens is Q0 intersect both (x+/-1)²+D*y² <=rho², as in Phase285. Half-coset elements are (a+b*u)/2 with a,b both odd, norm (a²+D*b²)/4 integer, bounded by rho².

Freeze the original integer source helper blob `research/phase206/source_probe.py = 3f954b59d9f86b06ad53667c869b5b24f2e6c7f6`. At D403 the original helper gives rho40, R100,S=J4,Q219; the Phase286 theta point set must agree *exactly* with its Q219. Fixed counts: D19 rho5 integer=21, lens=15, deleted=6, half=20; D403 rho40 integer=219, lens=213, deleted=6, half=260. Minimum half-coset norms: 5 and 101 respectively. These are inherited **known predictions**, not fresh discoveries.

## Exact rational specialization

Fix t=ln(2), so exp(-t N(z)) = 2^(-N(z)) for ALL maximal-order algebraic integers, including the half-coset. For (a,b) nonnegative integers, m=a+b, and z=x+yu define

`F_(a,b)(z) = z^a * conjugate(z)^b * 2^(-N(z)) in Q[u]`.

Compute **exactly** in a pair of Fraction coordinates (one real coefficient and one u coefficient). Do not use floating-point numbers or claim a floating-point interval certificate.

For the chosen disk, exactly verify

`Sum_(z in O, N(z)<=rho²) F =
    Sum_(z in lens) F + Sum_(z in Q0\lens) F +
    Sum_(z in half coset, N(z)<=rho²) F`.

Test angular degrees (a,b) in {(0,0),(1,0),(2,1),(2,2)} for D19 and add (6,6) for D403. Test central-inversion cancellation for all odd total degrees on each symmetric component. Check zero-term 1 at z=0 in integer component, and do not mistake it for a nonzero-term ideal zeta summand.

## Certified tail bound with only rational arithmetic

For k=a+b+2 and integer rho>=1, the Phase285 shell estimate for the two maximal-order cosets yields

`|E_(a,b)(ln2)| <= 8 * (rho+2)^k * 2^(-rho²) / (1-q)`,
`q = ((rho+3)/(rho+2))^k * 2^(-(2*rho+1))`.

All terms are positive rational. Assert `0<=q<1`; calculate the bound as exact `fractions.Fraction`. This is an upper bound for the **complex absolute value** (hence for the individual real/u coordinates after applying |ImCoefficient| <= |E|/sqrt(D)), not an equality. Assert radial tail radii meet strict dyadic targets: D19 m=0 bound < 2^(-16), D403 m=0 bound < 2^(-1500), D403 m=12 bound < 2^(-1500). If any declared target is false, FAIL, do not modify expectations after seeing results. When other degrees are tested, calculate/report their actual dyadic threshold conservatively.

The half-coset Gaussian **radial** contribution must be >=4*2^(-min_norm) and be strictly larger than the corresponding tail bound; this is a negative control against burying the omitted coset in an outer tail. Require positive radial half-coset contribution.

## Second independent proof route / negative controls

1. Check the finite lens decomposition in `Q[u]` by direct full-disk enumeration versus the three separately generated components, not just by comparing two sums over identical arrays.
2. Check inversion symmetry of the complete maximal-order disk (integer plus half coset) at each (D,rho).
3. Construct an **independent shell-count arithmetic** bound: each coset has at most `4(n+2)^2` points at integer annulus `n<=|z|<n+1`, D>=1. Its ratio is at most q for n>=rho. This is paper-level geometry behind the rational geometric-series certificate, not merely a numeric guess.
4. Show the WRONG-source control of omitting half-coset radial contribution fails (difference is strictly above the certified outer-tail radius). Show a made-up Gaussian weight `2^{-4*N}` substituted for the specified `2^{-N}` does not match the source.
5. The original full trace Gram remains untouched. In particular, do not assign the finite Gaussian moment data the old Gram determinant or assert an `L(s,chi)` zero-free theorem.

## Paper-level small-t bridge to be independently reviewed

The standard 2D Poisson summation identity on these two cosets gives, for all real t>0,

`Theta_O(t) = sum_(z in O) exp(-tN(z)) =
    (2*pi/(t*sqrt(D))) * sum_(m,n in Z, m+n even) exp(-pi²*(m²+n²/D)/t)`.

A conservative zero-mode estimate follows for `qdual=exp(-pi²/(D*t))`:

`0 <= Theta_O(t)-2*pi/(t*sqrt(D))
      <= (2*pi/(t*sqrt(D))) * 8*qdual/(1-qdual)^2`.

This is a **paper-level derivation from classical Poisson summation**, not Lean, an independently proved new theorem, or a Phase286 numeric verification of an infinite dual sum. It addresses the *radial* small-t end; weighted/angular moments require differentiation of the shifted generating theta and rigorous derivative bounds before an actual uniform Mellin argument. Even the radial theta Mellin yields the full Dedekind zeta only under class-number-one or an appropriately accounted ideal-class decomposition.

## Evidence and stop rules

[P-paper] exact rational specialization and conditional shell bound, Poisson identity inherited from classical summation; [M after CI] fixed D19/D403 finite rational moment calculations, coset and tail certificates; [H] rigorous angular small-t dual bounds, exact bridge to ideal theta/Hecke data, field theorem implications; [R] pretending missing half-coset is tail noise, treating a single t=ln2 as uniform Mellin information, or adding any new D403 Gram valuation units.

If any original-source hash, point count, coset parity, integer norm, exact moment equality, angular odd-cancellation, q<1, radial comparison, or frozen dyadic threshold fails, stop without editing expected values. Keep **DRAFT** pending focused exact-head CI + Markdown + full-root Lean checks and source review. PR #176 and PR #157/#50 remain separate.
