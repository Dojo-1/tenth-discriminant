# Phase378 / Tao objective first: an exact 7/8 zero-free -> d < 1024 bridge

**21 November 2026. Research note (AI-assisted); source-locked analysis, not a new RH proof, not an independent referee report.**

Primary target: Tao's tenth-discriminant challenge, posed 20 October 2026:
https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/

This sidecar does **not** modify the original integer trace-Gram, arithmetic jets, Hadamard geometry, `TenthDiscriminant.lean`, or the Phase377 proof-audit governance. It supplies a **different, conditional analytic extraction**, whose assumptions must be compared with—not silently substituted for—the determinant method.

## 1. Precise result and what is assumed

**Proposition (conditional, written proof).** Assume

> **ZF(7/8):** for every negative fundamental discriminant `D`, the primitive real quadratic Dirichlet function `L(s,chi_D)` has no real zero in the open interval `7/8 < s < 1`.

Then every imaginary quadratic field `K` of class number one satisfies

`0 < |disc(K)| < 1024`.

This does not require Heegner's proof. The finite finish gives precisely the nine absolute discriminants `3,4,7,8,11,19,43,67,163`. The argument is an instance of the classical Chowla-Selberg/Epstein route; **the 1024 cutoff is not novel and not optimized**. Other participants in Tao's challenge already reported `d <= 652` from the same 7/8 input, and stronger bounds using other tools. The value of this note is short, explicit, independently reproducible *rational inequalities* and an unambiguous implication boundary.

The **external** Dirichlet GRH claim is supported by the Nov 2026 Alpöge source and independent checking, not by any new Lean construction here. See Sutherland's MIT audit (21 Nov snapshot) https://math.mit.edu/~drew/grh/ and the Lean/Mathlib joint statement https://leanprover-community.github.io/blog/posts/riemann-hypothesis/ . The public MIT summary explicitly distinguishes Dirichlet GRH from general Hecke GRH.

## 2. The principal-norm series, with exact hypotheses

Let `D=-d<0` be a negative fundamental discriminant and suppose `h(D)=1` and `d>=1024`. Its unit group has order `w=2`. Write `a=sqrt(d)/2 >=16` and choose `b=0` if `D` is divisible by four and `b=1` otherwise. The ring of integers has an integral basis `1, (b+i*sqrt(d))/2`. The principal norm form is

`Q(m,n)=(m + b*n/2)^2 + a^2*n^2`.

Because every ideal is principal and there are two units,

`zeta_K(s) = (1/2) * sum_{(m,n) != (0,0)} Q(m,n)^(-s)`, initially `Re(s)>1`.

Poisson summation in the `m` variable gives its analytically continued expansion for real `1/2<s<1`:

```
zeta_K(s) = zeta(2s)
          + C(s)*a^(1-2s)*zeta(2s-1)
          + E_b(s,a),
C(s)=sqrt(pi)*Gamma(s-1/2)/Gamma(s)=Beta(s-1/2,1/2),
E_b(s,a) = [4*pi^s/Gamma(s)] * a^(1/2-s)
           * sum_{n,k >=1} n^(1/2-s) k^(s-1/2)
             * cos(pi*b*n*k) K_(s-1/2)(2*pi*a*n*k).
```

This is a **standard analytic identity used as an external theorem**, not something proved by the attached Python script. Its normalization is essential: at `n=0`, the factor `1/2` yields `zeta(2s)`, and for `n != 0` the plus/minus terms cancel that `1/2`. Neither a factor of two nor a missing unit count may be dropped.

At `s=7/8`:

`zeta_K(7/8)=zeta(7/4)+Beta(3/8,1/2)*a^(-3/4)*zeta(3/4)+E_b(7/8,a)`.

## 3. Five transparent rational estimates

1. **Beta coefficient.** By Cauchy-Schwarz in the beta integral,
   `Beta(3/8,1/2)^2 <= Beta(1/4,1/2)*Beta(1/2,1/2)`.
   Substitute `t=x^4`, `x=sin(theta)` in the first beta integral:

   `Beta(1/4,1/2)=4*integral_0^(pi/2) [1+sin(theta)^2]^(-1/2) dtheta`.

   The convex function `f(u)=(1+u)^(-1/2)` lies below its secant on `[0,1]`: `f(u)<=1-(1-1/sqrt(2))*u`. Since the average of `sin(theta)^2` over `[0,pi/2]` is `1/2`,
   `Beta(1/4,1/2) <= pi*(1+1/sqrt(2))`.
   Use `pi<22/7`, `1/sqrt(2)<5/7` and a fourth-grade rational comparison to get
   `Beta(3/8,1/2) < 33/8`.

2. **The negative zeta value.** The alternating-eta identity for `s=3/4` reads
   `-zeta(3/4) = eta(3/4)/(2^(1/4)-1)`.
   The 61-term odd partial sum of the alternating eta series is an upper bound, and exact fourth-power comparisons give `eta_61(3/4)<27/40`. Since `2^(1/4)>19/16`, it follows that
   `0 < -zeta(3/4)<18/5`.

3. **The positive zeta value.** Decreasing-function integral comparison gives
   `zeta(7/4) > sum_{n=1}^4 n^(-7/4) +(4/3)*5^(-3/4) > 19/10`.
   The last strict inequality is certified solely by exact fourth-power integer comparisons.

4. **The tiny Bessel tail.** For `0<nu<1/2` and `x>0`, the integral representation of `K_nu` gives
   `0 < K_nu(x) <= K_(1/2)(x) = sqrt(pi/(2x))*exp(-x)`.
   Consequently, using `pi^(7/8)<4`, `1/Gamma(7/8)<e<3`, `a>=16`, and `nk>=n+k-1`:

   `|E_b(7/8,a)| < 24*r/(1-r)^2`, where `r=exp(-2*pi*a)`.

   Since `pi>3` and `a>=16`, `2*pi*a>96>16`, while the first six Taylor terms show `e^16>10000`. Thus `r<1/10000`, giving `|E_b(7/8,a)|<1/100`.

5. **Combine without rounded decimals.** For `a>=16`, `a^(-3/4)<=1/8`. Therefore

```
zeta_K(7/8)
  > 19/10 - (33/8)*(18/5)*(1/8) - 1/100
  = 27/800
  > 0.
```

The attached script asserts all finite rational comparisons, including the Bessel-tail rational envelope. It does not verify the cited analytic identities, gamma function inequalities, the standard bound `3<pi<22/7`, nor the class number one ↔ principal-ideal equality.

## 4. From positive Dedekind zeta to the forbidden zero

For `7/8<s<1`, the Riemann zeta function is negative (`zeta(s)=eta(s)/(1-2^(1-s))`). Also `zeta_K(s)=zeta(s)L(s,chi_D)` for the quadratic fundamental character. The lower bound shows

`L(7/8,chi_D) = zeta_K(7/8)/zeta(7/8) < 0`.

The Dirichlet class number formula gives `L(1,chi_D)=2*pi*h(D)/(w*sqrt(d))>0`. Continuity on the real interval forces some `beta` with `7/8<beta<1` and `L(beta,chi_D)=0`. This contradicts ZF(7/8), proving `d<1024`.

**Reverse direction is invalid:** no tenth discriminant does **not** imply ZF(7/8), Dirichlet GRH, or an arbitrary Hecke zero-free region. In fact, the proof only used the characters of the putative class-number-one fields. The forward theorem is weaker than the entire zero-free hypothesis.

## 5. Finite classification: two independent arithmetic routes

Run `python3 research/phase378/tao_zero_free_1024.py`.

The script enumerates **all 313 negative fundamental discriminants with `0<d<1024`**. Each is checked by independent implementations:

- Gauss's primitive positive-definite binary quadratic form reduction, counting all reduced representatives including tie conventions.
- Character formula `h(D)=-(w/(2*d))*sum_{a=1}^{d-1} a*chi_D(a)`, with the Jacobi/Kronecker symbol implemented by quadratic reciprocity rather than by form reduction.

Their class numbers agree **for all 313**. The only class-number-one absolute discriminants are `3,4,7,8,11,19,43,67,163`. This is bounded integer verification: it still relies on standard theorems interpreting the two calculations as class numbers. These independent algorithms improve fault detection but do not constitute independent human review.

## 6. Masullo: put the errors in a dependency ledger, not into the premises

Source: Alessandro Maria Masullo, *The Music of the Primes*, 940-page circulated 20 November 2026 version supplied by the user.

- **R (explicit counterexample):** Appendix C, Lemma C.3.4.1(2), printed p. 697, falsely asserts basis independence of `sum |<T e,e>|` for trace-class `T`. On `C^2`, take `T=diag(1,-1)`. Standard ONB gives 2; the 45-degree ONB gives 0. The usual trace `sum <T e,e>` is basis-independent, as in (3). This may be locally repairable; it does *not* by itself refute the main trace formula.
- **H (proof obligation unclosed in draft):** Ch. 13, p. 522, invokes `Theorem ??` and leaves `Theorem 13.3.1.2 (Divisor of L(s,chi))` with footnotes `Insert statement` and `State and prove the Main Theorems`. Therefore the source does not yet supply a usable GRH/zero-free certificate.
- **H (scope and spectral bridge):** Thm. 12.5.1.1 p. 519-520 is an asserted adelic trace identity in a test-function subspace; Ch. 13 passes to a truncated spectral multiplicity `Nspec(c)=min(N(c),[F:Q])` and imposes a finite-codimensional test-function condition. One must establish the precise bridge to Weil's positivity criterion and the **whole** required test family before claiming all Hecke zeros are central. No such bridge is assumed here.
- **S (useful conceptual relation):** Masullo's Mellin trace/idele orbit view and the present Epstein/Poisson sign bridge both translate analytic spectral data into arithmetic constraints. That analogy does not transport his unproved theorem into our assumptions.

**Gate:** accept a Masullo-derived zero-free input only if the relevant theorem is proved from valid premises with all positivity/density/completeness bridges discharged. Until then, its broad Hecke-GRH claim stays unverified. Prefer the independently checked Alpöge **Dirichlet** GRH source for the limited `ZF(7/8)` hypothesis.

## 7. Comparison with the original Tenth Discriminant repository

- The previous project theorem `d<322^4` and its prospective `302^4/301^4` refinements belong to the **original integer trace-Gram/ordinary-jet** route. Their Lean proof status, research branch status and external semantic limitations must remain unchanged.
- This `d<1024` route uses the considerably stronger *external analytic* input `ZF(7/8)`. It must not be described as a sharpening **of the same unconditional method** or merged into its mathematical proof dependencies without provenance.
- The published challenge discussion already reports a sharper bound `d<=652` derived from `ZF(7/8)`, and a reported `d<565` with additional tools. Thus `d<1024` is an explanatory, reproducible baseline rather than a contribution to the currently best known bound.
- If exploring Selberg-Ihara zeta functions later, first define which Dirichlet/Hecke zero-free statement is actually implied, with quantifier scope and transfer theorem; no generic "graph RH" implies the present arithmetic hypothesis automatically.

### Evidence labels and stop conditions

| Claim | Evidence class | Scope |
|---|---|---|
| Exact rational inequalities and 313-case dual enumeration | M | Executable Python checks in this sidecar; independently re-run in CI to promote reproducibility |
| Epstein/Poisson expansion; beta/gamma/Bessel and class-number formulas | P (classical, external) | Used but not formalized in this repository |
| `ZF(7/8) => d<1024` | P (written conditional argument), pending expert review | Not Lean-checked; no new Siegel-zero elimination theorem |
| Dirichlet GRH as an external source of `ZF(7/8)` | External verification report | Scope is Dirichlet characters, *not* every Hecke/automorphic L-function |
| Masullo's Lemma C.3.4.1(2) as written | R | Explicit 2x2 counterexample |
| Masullo's main Hecke GRH consequence | H | Manuscript Chapter 13 still missing theorem/proof bridge |
| External arithmetic interpretation of prior 301^4 Lean field transport | H | Remains open per original review issue #50 |

**Next stop rule:** do not spend another research round creating geometric lifts unless it either (i) improves an explicitly bounded, rigorously certified `ZF(sigma) -> d` inequality **with the same sigma**, (ii) reconstructs a missing Masullo positivity/completeness bridge with a valid proof, or (iii) resolves one actual semantic gap in the original determinant approach. Preserve negative results and source lineage.
