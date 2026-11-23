# Phase383 — near-central Epstein sign gate, cutoff 199

**22 November 2026 · AI-assisted research / review draft.** This file extends the *existing Phase382 PR*, rather than creating another unmerged independent branch. Phase379 (ZF(7/8), 652) and Phase382 (ZF(3/4), 295) remain intact.

## Exactly what is claimed

Let **ZF(33/64)** be the hypothesis that for every *negative fundamental discriminant* D the primitive quadratic Dirichlet L-function L(s, chi_D) has **no real zero** for 33/64 < s < 1.

**Conditional proposition:** If K is an imaginary quadratic number field with h(K)=1 and ZF(33/64) holds, then |disc(K)| <= 199.

This zero-free hypothesis is **strictly stronger** than ZF(3/4) and ZF(7/8). The numerical gain is not a same-assumption improvement, and no new Dirichlet GRH theorem is claimed. The existing external Dirichlet-GRH verification reports support the broader premise but are not rebuilt here. No originality or best-known bound is claimed.

## Source and exact normalization

Classical Chowla–Selberg formula: Matthew Alderson (2010), *Integral Moments of Quadratic Dirichlet L-functions: A Computational Perspective*, section 2.2, Theorems 2.2–2.3, equations (2.13), (2.17), (2.18), University of Waterloo. Primary source URL:
https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/c9b59ae1-2ec5-4404-9c91-c48ef6e60757/content

Set D=-d<0 fundamental, h(D)=1 and d>=200, so the unit group has order w=2. The unique form class is represented by the principal form (1,b,c), where b=0 for D divisible by 4 and b=1 otherwise. Let a=sqrt(d)/2. The Dedekind/Epstein expansion becomes, for 1/2<s<1,

    zeta_K(s) = zeta(2s) + Beta(s-1/2,1/2)*a^(1-2s)*zeta(2s-1) + E_b(s,a),

    E_b(s,a) = 4*pi^s/Gamma(s) * a^(1/2-s) *
       sum_{n,k>=1} n^(1/2-s) k^(s-1/2) cos(pi*b*n*k)
                      K_(s-1/2)(2*pi*a*n*k).

The **one-half unit quotient** cancels the factor two in the Epstein formula. The double-sum indexing is the divisor-sum expansion from equation (2.13). This was checked symbolically against the published normalization; it is not a Lean theorem in this project.

At s=33/64:

    2s=33/32, 2s-1=1/32, s-1/2=1/64,
    a^(1-2s)= (4/d)^(1/64).

Thus the main term has one positive zeta, one negative zeta, and a positive beta coefficient.

## Exact-arithmetic certificate

Script: research/phase383/tao_33_64_exact.py. It uses only Python Fraction and integer powers; every acceptance gate is a rational inequality, not a printed decimal.

1. **Eta intervals.** The Euler/Hasse series for eta(t) at t=1/32 and t=33/32 has nonnegative inner finite-difference terms bounded by 1 (Laplace/Gamma integral), hence the omitted tail after 64 outer indices lies in [0,2^-64]. Terms k^(-1/32) are enclosed by 32nd integer-power comparisons; t=33/32 terms divide these by k. The signed binomial sums are conservatively interval-propagated.
2. **Convert to zeta.**
   abs(zeta(1/32))=eta(1/32)/(2^(31/32)-1);
   zeta(33/32)=eta(33/32)/(1-2^(-1/32)).
   All denominators are bracketed by certified 32nd integer roots.
3. **Beta interval.** Split B(1/64,1/2) at 1/2. Two positive binomial series have individual geometric tails <= 2^(1-N)/(N+u), with N=64 and u=1/64 or 1/2; the 2^-u factors have integer-root brackets.
4. **Large-discriminant monotonicity.** For d>=200, a^(-1/32)=(4/d)^(1/64)<=(1/50)^(1/64), bracketed by 64th integer powers.
5. **Bessel tail.** For 0<=nu<=1/2, 0<K_nu(x)<=K_(1/2)(x)=sqrt(pi/(2x))e^-x. This follows from the integral with cosh(nu*t). At s=33/64, the remaining weights after the K_(1/2) bound are n^-s k^(s-1)<=1. Since d>=200, a>7 and 2*pi*a>42>30. Using pi^s<4, 1/Gamma(s)<2, a^-s<1, the prefactor is <16; 24 is a conservative upper bound. Set r=e^(-2*pi*a)<10^-8 using exp(30)>30^10/10!>10^8. The inequality nk>=n+k-1 gives
   |E_b|<24*r/(1-r)^2 < 24*10^8/(10^8-1)^2 < 10^-6.

The local exact acceptance yielded

    zeta_K(33/64) > 0.00157923885315398... > 1/1000

under the external formula, uniformly for d>=200. A negative-control enclosure bounds the **main term only** at d=199 above by -0.000972150322146986, showing why this specific test does not already exclude 199; 199 is fundamental but has class number >1 independently.

## Final arithmetic implication

For 0<s<1, zeta(s)<0. The standard factorization zeta_K(s)=zeta(s)L(s,chi_D), with chi_D primitive quadratic of conductor |D|, yields L(33/64,chi_D)<0. The class-number formula gives L(1,chi_D)>0. Continuity produces a *real* zero in (33/64,1), contradicting ZF(33/64). Thus no h=1 imaginary quadratic field has |D|>=200.

**Finite finish:** the Phase381 exact boolean sieve already excludes all but nine squarefree radicands below 653, so it covers the smaller <=199 interval once its repaired Lean build is confirmed. The nine actual absolute discriminants remain 3,4,7,8,11,19,43,67,163. Positivity of their class numbers requires the separate existing source, not just the sieve.

## Verification boundary and research directions

- **M:** exact-rational Python certificate passed locally; a separate high-precision mpmath main-term calculation at d=200 gave +0.001579481263095842..., inside the certified enclosure.
- **A:** Chowla–Selberg/Epstein formula, absolute Bessel inequality, eta/beta integral formulas, Dedekind factorization, quadratic character conductor correspondence, class-number formula, and ZF(33/64).
- **P in previous source (build pending in this round):** odd-prime and prime-two ideal/norm lifting behind the finite sieve.
- **H:** full Lean source-level analytic sign theorem with no analytic bridge granted as a custom axiom, plus review of the semantic matching to Alpöge's Dirichlet theorem.
- **Separately open:** original thin trace-Gram actual-field theorem independent semantic audit issue #50; no transport of this analytic bound into that original determinant argument.
- **Masullo/Selberg/Ihara:** no zero-free or graph-spectral assumptions imported from those lines.

Reproduce:

    python3 research/phase383/tao_33_64_exact.py

**Stop rule:** if the source's unit factor, principal-form normalization, eta tail positivity, Bessel bound, or primitive-character correspondence fails independent review, downgrade this result; do not merely tune the printed cutoff.
