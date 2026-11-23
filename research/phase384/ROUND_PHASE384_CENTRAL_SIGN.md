# Phase384: central-point sign certificate (research draft)

**23 November 2026. AI-assisted, not a claim of numerical novelty.** This is an exact rational simplification of the classical GRH-dependent discriminant bound 199, already discussed in Terence Tao's October 2026 challenge. It is stacked on the Phase382–383 analytic branch and does **not** alter the original integer trace-Gram, mainline 322^4 proof, research 301/302^4, or review issue #50.

## The actual theorem target

For any negative fundamental discriminant D=-d with d>=200, let K be the imaginary quadratic field with character chi_D. Under h(K)=1, the classical Epstein identity and the exact sign certificate below imply

    exists beta: 1/2 < beta < 1 and L(beta,chi_D)=0.

This zero-existence statement uses no assumed GRH. Its consequence is that no-real-zero on (1/2,1) for primitive quadratic characters (e.g. Dirichlet GRH) forces d<=199.

## Analytic source and central limit

For h(K)=1 and d>4, the two units give the principal Epstein series

    zeta_K(s) = 1/2 sum_{(m,n)!=(0,0)}
        ((m+b*n/2)^2 + (d/4)*n^2)^(-s),

where b=0 for even fundamental discriminants and b=1 for odd. Put a=sqrt(d)/2. Poisson summation gives the established meromorphic identity

    zeta_K(s) = zeta(2s)
      + Beta(s-1/2,1/2)*a^(1-2s)*zeta(2s-1)
      + E_b(s,a).

The Bessel term is

    E_b(s,a) = 4*pi^s/Gamma(s)*a^(1/2-s)
      sum_{n,k>=1} n^(1/2-s)*k^(s-1/2)*cos(pi*b*n*k)
                      *K_{s-1/2}(2*pi*a*n*k).

At s=1/2+e, use zeta(1+2e)=1/(2e)+gamma+O(e),
zeta(2e)=-1/2-e*log(2pi)+O(e^2),
Beta(e,1/2)=1/e+2log2+O(e), and a^(-2e)=1-2e*log a+O(e^2).
The poles cancel, and the exponentially convergent Bessel remainder has a termwise central limit:

    zeta_K(1/2) = gamma + log(sqrt(d)/(8pi)) + E_b(d)
    E_b(d) = 4 sum_{n,k>=1} cos(pi*b*n*k)*K_0(pi*sqrt(d)*n*k).

## Fully rational finite bound

For d>=200, the integral representation yields K_0(x)<=K_{1/2}(x)
= sqrt(pi/(2x))*exp(-x). For x=pi*sqrt(d)*n*k this is <=exp(-x).
Using pi>3 and sqrt(d)>14, the quantity r=exp(-pi*sqrt(d)) satisfies
r<10^-8 (as exp(30)>30^10/10!>10^8). Since n*k>=n+k-1,

    |E_b(d)| <= 4*r/(1-r)^2 < 4*10^-8/(1-10^-8)^2 < 10^-6.

For x>1, z=(x-1)/(x+1), the four-term atanh expansion and geometric tail
give rational lower/upper bounds L_4(x)<log(x)<U_4(x), with

    L_4(x)=2*sum_{k=0}^3 z^(2k+1)/(2k+1)
    U_4(x)=L_4(x)+2*z^9/(9*(1-z^2)).

The sequence H_n-log(n)-1/(2n) strictly increases to Euler's constant:
its increment equals the trapezoidal-rule error for the convex function
1/t on [n,n+1]. Therefore

    gamma > H_128 - 7*U_4(2) - 1/256.

The classical pi<22/7 and sqrt(200)>707/50 imply
8*pi/sqrt(d)<8800/4949 for d>=200. Hence

    zeta_K(1/2)
      > H_128-7*U_4(2)-1/256
         -U_4(8800/4949) -4*10^-8/(1-10^-8)^2
      > 0.0016423 > 1/1000.

The executable acceptance is **exact Fraction arithmetic**, not any
rounded decimal. Run:

    python3 research/phase384/central_half_rational.py

## Sign-to-zero, converse and evidence boundary

zeta(1/2)<0, so zeta_K(1/2)>0 gives L(1/2,chi_D)<0.
The quadratic class-number formula gives L(1,chi_D)>0; continuity
forces a real zero in (1/2,1). Reverse direction does not hold:
class-number-one classification does not imply GRH.

**Proof-status protocol:** M: locally executed exact rational inequalities;
P (ordinary mathematics using external standard analytic theorems):
Epstein normalization, central limit, Bessel and sign argument;
A: GRH / no real zeros (1/2,1) only for the corollary;
H: source-level Lean analytic identity and independent mathematical review;
R: any claim that 199 is a newly discovered bound.

Prior art: Terence Tao's challenge comments discuss GRH=>d<=199 and
64*pi^2*exp(-2*EulerGamma)=199.120770..., alongside other approaches:
https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/

Phase381 already has focused and whole-root Lean CI green at 41f84954,
providing the *finite* candidate list under <=652. No new Lean build
of the Phase384 analytic identities is claimed here.
