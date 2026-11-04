# Phase210-D — an exceptional zero at the conductor-scale thin ellipse

*4 November 2026. Paper-level analysis only; not a Lean theorem, zero-free region, or independently certified numerical bound. Issue [#158](https://github.com/Dojo-1/tenth-discriminant/issues/158).*

## Sources and notation

Primary analytical mechanism: [OpenAI, *Uniform exclusion of Landau–Siegel zeros*, 1 October 2026](https://github.com/openai/math/tree/main/preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026), Section 2 (the logarithmic-derivative prime-bias lemma); [Tao, *A sketch of the proof of non-existence of Siegel zeroes*, 19 October 2026](https://terrytao.wordpress.com/2026/10/19/a-sketch-of-the-proof-of-non-existence-of-siegel-zeroes/). For elementary auxiliary prime sums, use explicit Mertens/Rosser–Schoenfeld bounds (their exact constants are stated below as input hypotheses). **Do not confuse this source with the unrelated class-number-one finite-field return.**

Let q=D be the conductor of a primitive real quadratic character chi, with fundamental discriminant -D; put ell=log D. Hypothetically let beta∈(0,1) be a real zero of L(s,chi), eta=1-beta, delta=eta*ell≤c. For X≥3, L=log X. Define split, inert and ramified logarithmic prime mass

    M_+(X) = Σ_{p≤X, chi(p)=+1} log(p)/p,
    M_-(X) = Σ_{p≤X, chi(p)=-1} log(p)/p,
    M_0(X) = Σ_{p≤X, p|D} log(p)/p.

The original accepted source uses R=floor(D/4), S=floor(R/25), J=S, Q=ellipsePairs D (thinRadius D) and G=integerRectangularTraceGram Q D J R S. This **same** G is the one bounded by ThinUpper322 at D≥322^4.

## Explicit prime-bias inequality, with named analytic inputs

The source paper's bound is

    M_+(X) ≪ ell + eta*(log X)^2,

with an **unspecified absolute implied constant**. It alone does *not* provide a certified numerical threshold. The following sharpened paper calculation spells out the constants and the extra inputs that a reproducible numeric statement must check:

1. The completed L-function zero-sum for 1<s≤2, retaining the hypothetical beta, gives
   -L'/L(s,chi) ≤ (1/2)ell + 1 - 1/(s-beta).
   Here the "+1" safely covers the digamma term for both parities; verifying the exact completed-zero identity is an explicit analytic prerequisite.
2. Use the elementary auxiliary bound -zeta'/zeta(s) ≤ 1/(s-1)+1 for 1<s≤2. Combining yields
   Σ_{n≥1} Lambda(n)*(1+chi(n))/n^s
        ≤ (1/2)ell + 2 + 1/(s-1)-1/(s-beta).
3. Set s=1+1/L. For p≤X with chi(p)=+1, p^{-1-1/L}≥(e*p)^{-1}, so the left side dominates (2/e)M_+(X). Thus the **explicit conditional estimate**
   M_+(X) ≤ (e/4)ell + e + (e/2)*eta*L²/(1+eta*L).
   This is a transparent paper derivation from (1),(2); no claim that the numerical constants have been externally audited.
4. For X≥3, use the explicit Mertens first-prime lower estimate Σ_{p≤X}log(p)/p ≥ log X−4. One convenient route is the elementary lower bound for the von Mangoldt form together with the convergent prime-power tail E_1<2; verify the exact published or standalone source constants before promoting them as an independently certified numerical lemma.
5. The ramified mass satisfies, for ell≥2,
   M_0(X) ≤ log ell+1:
   split ramified primes into p≤ell and p>ell. For the first set, use Rosser–Schoenfeld's Σ_{p≤y}log(p)/p<log y; for the second, Σ_{p|D,p>ell} log(p)/p ≤ (1/ell)log D=1.

Conditional on the precisely stated inputs (1),(2),(4),(5), the resulting **inert-prime lower bound with explicit coefficients** is

    M_-(X) ≥ L − (e/4)ell
                 − (e/2)*eta*L²/(1+eta*L)
                 − log ell − (5+e).       (PB)

With delta≤c, replace eta by c/ell on the negative term to obtain a universal lower bound over that proposed zero window:

    M_-(X) ≥ L − (e/4)ell
                 − (e/2)*(c*L²/ell)/(1+c*L/ell)
                 − log ell − (5+e).       (PB-c)

These are *lower bounds*, not asymptotic equalities or claims that a zero exists. The source paper already announces a uniform exclusion theorem, so Phase210 treats beta as a hypothetical input to test method transfer, not as an observed real zero.

## Typed transfer from log(p)/p to our ORIGINAL rectangular weight

At R=floor(D/4), S=floor(R/25), the finite-gram normalized arithmetic contribution is

    W_inert(R,S) =
      (2/(R² S))*Σ_{odd p≤R,chi(p)=-1} F_p(R,S)*log p

where F_p=Σ_{r<R}Σ_{s<S}min(floor(r/p),S-1-s). This is NOT identical termwise to M_-(R).

The algebraic identity already formalized in PrimeMassLower under the guard p≥R/S (e.g. p>100 here) is

    F_p=(S-1/2)*Σ_{r<R}floor(r/p)
          - (1/2)*Σ_{r<R}floor(r/p)^2.

Use floor(r/p)≥r/p−1, floor(r/p)^2≤(r/p)^2 and the exact first and second moments of r. For p>100, R/S≤26, this yields the paper lower

    2F_p/(R²S) ≥ 1/p − 1/(R*p) − 1/(2S*p) − 2/R − 26/(3p²).  (W)

Summing over inert p>100 and discarding small primes incurs at most

* Σ_{p≤100} log(p)/p < log 100 < 5;
* (1/R+1/(2S))*Σ_{p≤R}log(p)/p < 1 at the accepted D range;
* (2/R)*theta(R) < 3, using the classical explicit theta(x)≤psi(x)≤1.03883*x;
* (26/3)*Σ_{p>100}log(p)/p² ≤ (26/3)*(log100+1)/100 < 1.

Therefore, under these named elementary estimates,

    W_inert(R,S) ≥ M_-(R)−10.        (W-LB)

Together with (PB-c), a **paper conditional bound for precisely the accepted source** is

    W_inert(R,S) ≥ log R − (e/4)log D
      − (e/2)*(c*(log R)²/log D)/(1+c*log R/log D)
      − log log D − (15+e).         (PB-G)

No class-number-one hypothesis appears in this argument, but neither (PB-G) nor the exceptional-zero hypothesis has been imported into Lean. The constants and all transitions must be independently checked before any promotion.

## Can a conductor-scale zero force a contradiction?

The formally accepted original thin-gram upper reads

    W_inert(R,S) ≤ (4/5) log D − 1853/2000

for every finite odd inert prime set, once the Phase210 aggregate theorem has itself passed CI. Since R=floor(D/4), log R=log D−log4+o(1). Even in the strongest limiting thought experiment eta→0 (c→0), (PB-G) gives leading coefficient

    1−e/4 ≈ 0.32043

instead of the coefficient 0.8 required to overtake the analytic upper. Thus **the present *derived lower-bound estimate* does not exclude the proposed zero at conductor scale**. This is a failure of the certified comparison strength, NOT a counterexample to zero exclusion or a theorem that no sharper local argument exists.

The source OpenAI paper and Tao's exposition instead compare inert-prime mass at scales substantially larger than the conductor. In the hypothetical calculation where the old 0.8 coefficient of the Gram upper would remain unchanged (it will NOT do so automatically), setting X=D^A would require A>0.8+e/4≈1.47957 even when eta≈0, before accounting for finite constants. For eta≤c/ell the conditional requirement is roughly

    A−e/4−(e/2)*c*A²/(1+c*A)>0.8,

subject to positive margin against the explicit constants. This is **not** an admissible substitution into the current Lean theorem.

## Structural rank obstruction to naive range extension

The newly checked Phase209 exact conjugation folding has **N=|Q| effective real columns at each ordinary derivative order** (one for a real point, two for each nonreal conjugate pair). With J=S, the full Gram is built from at most S*N observation columns, while it has R*S rows. Its positivity therefore requires

    R*S≤S*N  =>  R≤N     (S>0).

The original thin-radius count gives N≤(31/50)D in the 321-domain paper/count certificate. Therefore with the **unchanged Q and J=S**, positivity cannot survive R>(31/50)D, irrespective of better arithmetic. In particular one cannot replace R≈D/4 with R≈D^A (any fixed A>1) for all large D while keeping the old source. This is a rank/dimension no-go, not an issue of constants.

A viable enlarged-range argument would need to enlarge the sample set Q until N≥R, increase the derivative budget J relative to S (with its own rank guard), or use an entirely new interpolation source. For an ellipse of the same shape, the heuristic count N~pi*rho²/sqrt(D) would require rho at least on the order of D^{A/2+1/4} for R~D^A; the old thin radius is of order D^{3/4}. Any such change **invalidates** the currently accepted positivity, trace/analytic upper, and numerical certificate until reconstructed on that new source. Green's N×N grid is a distinct geometry, not a free modification of our 322^4 theorem.

## Honest decision and smallest next test

**Decision:** The off-the-shelf exceptional-zero prime-bias lemma, even made coefficient-explicit as above, is too weak at conductor scale to contradict our accepted Gram upper. Changing R alone violates source rank. Phase210 should **close this specific direct-transport route as a failed quantitative bridge**, leaving open any stronger character-sum input or source redesign.

**Smallest decisive follow-up:** independently verify the explicit analytic inputs (1),(2),(4) and the (W) loss bound with original constants; then seek a source-preserving inequality that improves the *0.32043* leading coefficient to at least *0.8*, or prove a clean no-go under a named restricted family of estimates. Preserve the exact failure rather than upgrading to a zero-free theorem.

### Evidence status

- P Lean: old Frobenius per-prime divisor, folded original Gram, original 322 source positivity and upper. The newly introduced Phase210 finite-prime corollary is **pending exact-head CI**, not yet promoted.
- P paper conditional: (PB), (W), (PB-G) with the explicitly enumerated analytic input inequalities; formal and independent validation still absent.
- H: full Phase209 delta depth on the actual normalized jets, new weighted Gram valuation, 321 field conclusion, and any stronger general-character zero-exclusion method.
- R: direct substitution R=D^A for A>1 while keeping the unchanged Q and J=S; assumption that the class-number-one inertness proof is a general-character prime-bias theorem.
