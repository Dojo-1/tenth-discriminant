# Phase182 — the 375⁴ candidate, not yet a bound

*3 November 2026 · a proposed same-source Lean sharpening; conditional on exact-head verification and independent semantic review.*

Our current checked theorem has fourth-root anchor 377. This candidate lowers **only the numerical domain** to 375, without changing the sampled integer lattice, polynomial basis, derivative meaning, trace pairing or number-field discriminant.

## Where 377 was genuinely needed

Write t=D^(1/4). The thin support and fixed rectangular dimensions are unchanged:

```math
Q_D=\bigl\{(x,y)\in\mathbb Z^2:
x^2+Dy^2\le\rho_D^2\bigr\},\quad
\rho_D=\left\lceil\frac{11}{25}D^{3/4}\right\rceil,
\quad R=\left\lfloor\frac D4\right\rfloor,\quad
S=\left\lfloor\frac R{25}\right\rfloor.
```

The original 377 proof used a deliberately loose square-root envelope for the 2R+S interpolation count, namely 413/1000 times t cubed. The sharpened coefficient 412/1000 is still valid because

```math
\frac{51/100}{\pi}\le
\frac{51/100}{3.14}
<
\left(\frac{412}{1000}\right)^2.
```

Hence the same established cell-area sufficient criterion follows if

```math
\left(\frac{11}{25}
-\frac{1001}{1000}\frac{412}{1000}\right)t\ge10.
```

Already at t=375 the left-hand side exceeds 10 by 0.3455. This is an analytic **slack recovery**, not a new support or new Gram.

The integer remainder of R=floor(D/4) also gives 4R>=D-3, which suffices for R>=90 t³ when t>=375: the excess t³(t-360) is far larger than 3. This retains the same 521/90000 radius/R envelope and the original padded node-count majorant. Every required radius positivity and logarithmic upper estimate is reproved on the new domain rather than reusing a theorem whose input still says D>=377⁴.

## The scalar arithmetic comparison also survives

A *rational* certificate produced by the already checked odd-log-series remainder framework establishes

```math
\frac{5926}{1000}\le\log 375\le\frac{5927}{1000}.
```

In particular, for D>=375⁴, log D>=23.704>23.7, retaining exactly the lower logarithmic guard needed for the existing odd-prime estimate. The same-source determinant sandwich remains

```math
\left(\frac{999997}{1000000}\right)\log D
-\frac{5739}{1000}+\frac14\log 2
\le\frac{\log\det G_D}{R^2S}
\le\frac45\log D-\frac{1849}{2000}.
```

Here G_D is *still* the original positive integer ordinary-Z-jet Gram on the exact original Q_D, with W fixed during differentiation and original trace weights 2,2D. No new prime is inserted and the already proved binary factor is counted exactly once.

The strict difference at the conservative guard 23.7 is at least 0.0987039 using the repository's existing certified log(2) lower bound. The resulting **target theorem**, if Lean and audit checks pass, is

```math
\left|\mathrm{disc}(K)\right|<
375^4=19{,}775{,}390{,}625
```

for a totally complex quadratic number field K of class number one, using the unchanged odd/even maximal-order field bridges.

## Reconstructability and falsification

- [Log375Certificate.lean](../../lean/TenthDiscriminant/Log375Certificate.lean): exact rational certificate and false-24-log negative control.
- [ThinEllipseCount375.lean](../../lean/TenthDiscriminant/ThinEllipseCount375.lean): stricter cell-area square-root envelope and actual thin-support count.
- [RadiusRatio375.lean](../../lean/TenthDiscriminant/RadiusRatio375.lean) and [UpperScalars375.lean](../../lean/TenthDiscriminant/UpperScalars375.lean): original radius, count, log and normalized upper guard reconstruction.
- [Lower375.lean](../../lean/TenthDiscriminant/Lower375.lean) and [BinaryGap375.lean](../../lean/TenthDiscriminant/BinaryGap375.lean): existing odd-prime and single binary divisor, exact affine strict gap.
- [SourcePositivity375.lean](../../lean/TenthDiscriminant/SourcePositivity375.lean), [ThinUpper375.lean](../../lean/TenthDiscriminant/ThinUpper375.lean), and [ActualField375.lean](../../lean/TenthDiscriminant/ActualField375.lean): the common Gram and transport to the actual field discriminant.

**Kill condition:** any failed rational checker, missing cell-area inequality, mismatch of Q, R, S, or trace/derivative convention, failed Lean theorem, new axiom or violation of the original field chart blocks promotion. Retain the checked 377⁴ bound until the 375 target passes the formal checks. Even then [Issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50) remains the separate external semantic gate.

The classical nine-field classification is much stronger; this candidate is a test of the proof architecture and its economical numerical constants, not priority over that classification.
