# WordPress field → one local arithmetic object (30 October 2026)

**Status:** paper-level elementary lemma [P: mathematical argument below, *not* a new Lean declaration]; finite Phase135 Rust pilot [M: exact-source CI passed]; speculative general research programme [H]. This note makes no claim to a new bound, external endorsement or originality of the generic determinant/Smith facts. It preserves the current original field, samples, ordinary derivatives, metric and theorem boundary.

## Actual source field and attribution

- **Terence Tao, 19 Oct 2026,** [A sketch of the proof of non-existence of Siegel zeroes](https://terrytao.wordpress.com/2026/10/19/a-sketch-of-the-proof-of-non-existence-of-siegel-zeroes/). His illustrative polynomial sampling lattice has a nonzero integer squared-covolume Gram determinant, an Archimedean Hadamard upper bound, and Frobenius-induced non-Archimedean divisibility. The post discusses interpolation/nonvanishing (Masser/Laurent/resultants/Green), Stepanov's method, and the possibility of more systematic Zariski complexity. **This is source inspiration, not a novel feature of our programme.**
- **Terence Tao, 20 Oct 2026,** [Experimental tenth discriminant challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/). Beyond optimizing the numerical bound, Tao explicitly asks for comparing arrangements of existing arguments, reporting unsuccessful paths, identifying repairable failures, and producing human-verifiable explanations rather than a speed race. We should keep our independent semantic reconstruction issue open even when Lean builds.
- **Comment field, October 2026,** [Tao's 19 Oct discussion](https://terrytao.wordpress.com/2026/10/19/a-sketch-of-the-proof-of-non-existence-of-siegel-zeroes/comment-page-1/) raises intermediate-dimensional covolumes, exterior powers, Smith invariants and multiscale analogues; [20 Oct challenge discussion](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/comment-page-1/) includes *unformalized* claims that a Kerr lattice argument can be rewritten with a Gram determinant, and competing tighter bounds requiring their own source/evidence review. These are **other contributors' suggestions/claims**, not proven here and not to be attributed to Tao merely because they appear on his blog.
- Our closest concrete implementation is the original [IntegerTraceGram.lean](../../lean/TenthDiscriminant/IntegerTraceGram.lean), [RectangularRowAction.lean](../../lean/TenthDiscriminant/RectangularRowAction.lean), [RectangularGramFactor.lean](../../lean/TenthDiscriminant/RectangularGramFactor.lean) and [RankDivisorCompatibility.lean](../../lean/TenthDiscriminant/RankDivisorCompatibility.lean). The independently readable [Phase135 all-ordinary-jet pilot](../rank_divisor_interface/PHASE135_MATCHED_JETS.md) checks a single finite case, not a global theorem.

## A local Smith theorem for our *same E*

Let E be an integer n×m matrix (n≤m), p a prime, and suppose there are U∈GL_n(Z), nonnegative integers k_i, and integral C such that

    U E = Δ_p C,  Δ_p = diag(p^{k_1}, ..., p^{k_n}),
    F_p = Σ_i k_i.

Suppose C mod p has row rank n. **Claim [P, elementary paper proof; not yet Lean checked]:**

1. Every maximal minor of E is divisible by p^{F_p}, and at least one maximal minor has p-adic valuation **exactly** F_p. Thus the p-adic valuation of the *n-th determinantal divisor* gcd of all maximal minors of E equals F_p.
2. More strongly, viewed as a map E : Z_(p)^m → Z_(p)^n, its cokernel is isomorphic to the direct sum of cyclic modules Z_(p)/(p^{k_i}). In particular its p-primary Smith exponents are the multiset {k_i}, up to sorting.

**Proof.** For an n-element column subset I, the square-minor identity gives (det U)(det E_I) = (det Δ_p)(det C_I) = p^{F_p} det C_I. Since det U=±1, all minors have the stated factor. Rank_n(C mod p)=n means some det C_I is a unit modulo p, so the factor is exact for that I. Over the local ring Z_(p), that same invertible minor makes the map C : Z_(p)^m→Z_(p)^n surjective; U E has image Δ_p Z_(p)^n, hence the cokernel of E is isomorphic to coker Δ_p, the claimed direct sum. No analytic inequalities or primes-other-than-p are used. The local ring is an essential *type*: the inverse to the selected minor need not be integral globally over Z. **QED (paper argument, not yet mechanized).**

In the finite Phase135 instance D=19, rho=5, R=4, S=J=2, p=3, there are 8 rows and 84 columns; U subtracts the ZW row from the Z³ row, and Δ has seven ones and one 3, so F=1. The original full ellipse contains all 21 samples and has coincident coordinate residues mod 3. Yet the *normalized original ordinary jets* C have full F3 row rank: a displayed 8×8 maximal minor in [issue #51](https://github.com/Dojo-1/tenth-discriminant/issues/51#issuecomment-6534508273) has determinant 1 mod 3. Therefore the gcd of the original E maximal minors has v3 exactly **1**, regardless of those node collisions.

## Why this is NOT a free improvement to the Gram bound

For the SAME original factor-two real trace matrix B, set G=E B E^T, K=C B C^T. Then

    U G U^T = Δ_p K Δ_p,  det G = p^{2F_p} det K.

Over F_p, even if C has full row rank and B is invertible, the restriction of the bilinear pairing B to the row space W of C need not be nondegenerate. Equivalently (for invertible B mod p),

    det(K) != 0 mod p    iff    W ∩ W^{perp_B} = {0}.

The proof: K is the matrix of the restricted bilinear form in the independent row basis of C; its kernel corresponds to the radical W∩W^{perp_B}. **Full rank of C controls the p-Smith structure of E, not the p-adic valuation of the metric-dependent det G.**

Negative control at p=3 in the **same quadratic trace metric** D=19: C=(1,0,1,1) (one row), B=diag(2,38,2,38), so C mod 3 has rank 1 and B mod 3 is invertible, but CBC^T=42 is 0 mod 3. Therefore a universal claim 'normalized full rank forces residual Gram unit' is false. For the actual 8-row finite pilot, det K is instead 2 mod 3; there is *no* extra residual 3-valuation above the proved p^{2F} factor.

For weighted B diagonal over characteristic 0, Cauchy-Binet yields positive sums of squared maximal minors for det G; that *real* positivity does NOT transport as positivity to F_p, and the number of intermediate exterior-volume contributions depends on basis. The **Smith determinantal divisors** are basis-invariant under integer unimodular changes; the weighted sums of intermediate principal minors of G are generally **not** invariant under those same U. Do not present them as equal objects.

## Typed geometric/philosophical lift (S/H, not a theorem of sheaf theory)

One arithmetic object is observed through different local mathematical worlds:

    original integral observation lattice L = E(Z^m) ⊂ Z^n
      → at infinity: (E_R, positive B, det G > 0, Hadamard)
      → at prime p: (E_(p), coker, Smith filtration, Frobenius rows)
      → normalized p-chart: C_p = Δ_p^{-1} U_p E, with explicit defects Δ_p
      → p-fiber of the metric: det(C_p B C_p^T) modulo p.

The gluing datum is the **actual integer G and its determinant**, together with exact displayed maps. There is no canonical single matrix C valid simultaneously for every prime, and no transport of real order/positivity into finite-characteristic rank. The 'fiber' language is an accounting device unless an actual base, transition map and compatibility theorem are constructed. Likewise spin-weaving, holonomy and higher manifold vocabulary cannot buy an arithmetic exponent without a reproducible new lemma.

The interesting nested tower is *integral*: the cokernel has graded local p-power layers, its determinantal divisors encode successive exterior powers, and its archimedean observation retains the original metric. This formalizes the intuition of nesting without assuming a new geometry of primes.

## Next bounded experiment (issue #51, preregistered)

**Target:** for the fixed D=19 all-ordinary-jet E, independently reconstruct the selected 8×8 unit minor and check the equality v3(gcd of maximal minors)=1 by elementary row operations. Then promote the generic *conditional* local-Smith statement to Lean, if a well-scoped, compile-checked module can be written. A confirmed nonunit selected minor or an illegitimate division by p kills the proposed witness. A claimed extra residual factor v3(det K)>0 is already killed by the exact finite pilot.

**Stop:** once the local-Smith bridge is documented and checked, do not expand to global prime-existence, new field bounds, higher-degree Frobenius or geometric structures without a new preregistration. The present example supplies **zero** quantitative tightening of the 47.0b endpoint.

**Issue #50 remains unresolved:** no finite pilot, Smith identity or same-investigation review reconstructs the global prime-tail, geometry, number-field chart and cutoff. Ask an independent mathematician to reconstruct the actual entire field-discriminant theorem instead of treating this local instrument as its semantic proof.
