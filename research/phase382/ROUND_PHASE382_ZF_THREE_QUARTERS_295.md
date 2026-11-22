# Phase382 — a stronger conditional Tao cutoff at s=3/4

**22 November 2026 · AI-assisted research note · draft, isolated from Phase380/381 and the original trace-Gram.**

## Exact target, with stronger assumptions

Write `ZF(3/4)` for the following *external* premise: for every negative fundamental discriminant `D=-d`, the primitive quadratic Dirichlet L-function `L(s,chi_D)` has no **real** zero in `3/4<s<1`.

> **Conditional proposition (ordinary mathematical argument + exact rational numeric gate):** `ZF(3/4) and h(Q(sqrt D))=1 => d<=295`.

This is stronger numerically than the Phase379 `d<=652` bound but requires a **stronger zero-free hypothesis**. Its relevance is that Dirichlet GRH, as separately reported and certified in November 2026, would imply `ZF(3/4)`. The finite rational script does not establish GRH or formalize its theorem interface. No originality/record claim: Tao's challenge thread already contains Lean work on the 652 route, 190 prime witnesses and stronger comparison methods.

## Proof mechanism

Let `D=-d` be a negative fundamental discriminant with `h(D)=1` and `d>=296`. Its unit group has order two. For `a=sqrt(d)/2`, and `b=0` or `1` depending on the maximal-order parity chart, the principal Epstein identity (an imported classical analytic theorem) yields:

```text
zeta_K(3/4) =
    zeta(3/2)
  + B(1/4,1/2) * a^(-1/2) * zeta(1/2)
  + E_b(3/4,a)
```

with
```text
E_b(s,a) = (4*pi^s/Gamma(s)) * a^(1/2-s)
  * sum_{n,k>=1} n^(1/2-s) k^(s-1/2)
    * cos(pi*b*n*k) * K_(s-1/2)(2*pi*a*n*k).
```
The same expansion was used for Phase379 at `s=7/8`; its external analytic normalization and the class-number-one principal-ideal equality are unchanged.

### Fully rational finite inequalities

The script `tao_3_4_exact.py` uses Python's `Fraction`, integer square roots and exact integer-power brackets. It does **not** trust floating-point estimates in acceptance checks.

- Euler/Hasse eta expansion at `s=1/2` and `3/2`, with nonnegative inner finite differences and omitted tail `<=2^-64`. Each term is enclosed by an exact reciprocal square-root interval.
- Beta `B(1/4,1/2)` is split at `1/2`, expanded into two series with nonnegative binomial coefficients and explicit geometric rational tails; `2^-1/4, 2^-1/2` have integer-power brackets.
- At `d>=296`, `a^(-1/2)=(4/d)^(1/4)<=(1/74)^(1/4)`, exactly bracketed by fourth powers.
- For `nu=1/4`, the positive kernel satisfies `K_nu(x)<=K_(1/2)(x)=sqrt(pi/(2*x)) exp(-x)`. With `a>8`, `pi>3`, `pi^(3/4)<4`, `1/Gamma(3/4)<2` and `nk>=n+k-1`, the remainder obeys
  `|E_b(3/4,a)|<24*r/(1-r)^2`, where `r=exp(-2*pi*a)<10^-8`.
  The crude uniform rational upper bound `24*10^8/(10^8-1)^2<10^-6` is enough.

The exact comparison returns:
```text
zeta_K(3/4) > 0.0012806574336169... > 1/1000   (d >= 296).
```
The decimal is diagnostic; the accepted test is `Fraction > 1/1000`.

At `d=295`, the upper rational enclosure for the **main term only** is negative (`<-0.00092908`); this is a threshold negative control and **not** evidence that `d=295` is excluded from the hypothetical class-number-one domain. A tiny remainder is bounded separately, so avoid conflating the two.

### Arithmetic consequence

For `s=3/4`, `zeta(s)<0`. The quadratic factorization `zeta_K(s)=zeta(s)L(s,chi_D)` therefore yields `L(3/4,chi_D)<0`. By the class-number formula, `L(1,chi_D)=2*pi*h(D)/(w*sqrt d)>0`. Continuity forces a real zero of `L(s,chi_D)` in `(3/4,1)`, contradicting `ZF(3/4)`. Thus `d<296`, i.e., `d<=295`.

**This is NOT a source-level Lean theorem yet**: external analytic identities and the exact Dirichlet-character equivalence must be matched in Mathlib. Its rational finite inequalities passed locally (standard library only).

## Relationship to existing lines

- Phase379: same Epstein/Poisson mechanism; stronger ZF input, sharper cutoff. Do not claim a hypothesis-preserving improvement over 652.
- Phase380: independent 199/190/9 split-prime certificate; restricting it to `d<=295` is immediate but not novel.
- Phase381: source-matched Lean radical sieve, independently checking `d<653` candidate set, can finish this smaller `d<=295` interval **once its Lean compilation is separately confirmed**.
- Original trace-Gram: the reported **322^4** mainline bound and **301/302^4** research remain a distinct, potentially unconditional method with independent semantic review #50 open.
- Alpoge: Dirichlet GRH `=>ZF(3/4)` uses its specific primitive-character theorem, not a free Hecke or automorphic generalization.
- Masullo: his incomplete Hecke divisor statement and two false operator lemmas are not used.
- Conductor–Zero and Ihara/Selberg: no endpoint is transported between arithmetic Dirichlet zero-freeness and arbitrary spectral-gap analogues.

## Reproduce

```sh
python3 research/phase382/tao_3_4_exact.py
```

**Proof-status ledger:**
`M` — exact finite rational gate executed;
`A` — Epstein/Poisson, eta and beta integral representations, Dedekind factorization, class-number formula, and ZF(3/4);
`H` — fully source-level Lean integration and external mathematical review;
`R` — any claim that a cutoff under ZF(3/4) improves the same-hypothesis ZF(7/8) record.

## Next decisive test

Independently inspect the Epstein normalization and the bound on the Bessel tail at `s=3/4` in a primary source; then formalize the analytic sign lemma in Lean **without granting the conclusion as an axiom**. The eight-prime finite finish is already available separately in Phase381. Do not merge while these checks remain pending.
