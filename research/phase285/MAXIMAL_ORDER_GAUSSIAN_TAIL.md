# Phase285 extension — exact maximal-order coset and a certified Gaussian-moment tail

**12 November 2026, derived after the finite pilot.** This is a paper-level elementary inequality, not a Lean theorem, independently checked proof, new class-number bound, a Mellin continuation theorem or exclusion of exceptional zeros. The original D403 source and the original 16-row minor are unchanged. The missing half-coset counts below were computed exploratorily before adding their separate pinned source regression.

## What the finite source actually leaves out

For squarefree D=3 mod4, with u^2=-D and z=x+yu, the maximal order is the disjoint union

`O_K = Lambda_D disjoint_union (delta+Lambda_D)`, with `Lambda_D=Z[u]`, `delta=(1+u)/2`.

The norm of the second coset representative `(a+bu)/2` (a and b odd) is `(a^2+D b^2)/4`. Exact numerator arithmetic finds the half-coset points in the **same norm disk**:

| D, rho | original Q0 points in Lambda_D | additional points in delta+Lambda_D | smallest second-coset norm |
|---|---:|---:|---:|
| 19, 5 | 21 | **20** | 5 |
| 403, 40 | 219 | **260** | 101 |

Thus a Q0 lattice computation omits 20 of 41 full-order points in the D19 disk, and 260 of 479 in the D403 disk. This is a **finite, exactly computable coset correction**, not a Gaussian tail. Its size is not controlled by the determinant decrease caused by an intersected lens.

## Exact finite-to-infinite angular moment decomposition [P-paper]

Let a,b be nonnegative integers, m=a+b, tau>0, and define

`F_(a,b)(z;tau) = z^a conj(z)^b exp(-tau |z|^2)`.

For an integer rho>0, write `L_rho = Lambda_D intersect {|z|<=rho}`,
`H_rho = (delta+Lambda_D) intersect {|z|<=rho}` and let
`Q_lens subset L_rho` be the symmetric disk intersection from the pilot. The full maximal-order Gaussian mixed moment (convergent for tau>0) decomposes **exactly** as

`Sum_(z in O_K) F(z;tau) =
  Sum_(z in Q_lens) F(z;tau)
  + Sum_(z in L_rho \ Q_lens) F(z;tau)
  + Sum_(z in H_rho) F(z;tau)
  + E_(a,b)(rho,tau)`,

where `E` contains only the **two infinite outer tails** with norm strictly larger than rho^2. This identity does not require h(K)=1 and does not change the original finite Gram: it is a separately typed analytic transport.

## Uniform elementary error bound at a fixed positive tau [P-paper]

For either coset `C=Lambda_D` or `delta+Lambda_D`, D>=1, the number of points in any radius-R disk is at most

`(2R+2) (2R/sqrt(D)+2) <= 4(R+1)^2`, for R>=0.

Indeed, both cosets are translates of a rectangular lattice with horizontal spacing 1 and vertical spacing sqrt(D). Divide the outer tail into shells `n <= |z| < n+1`, n>=rho. Each shell has no more than `4(n+2)^2` lattice points, and

`|F_(a,b)(z;tau)| <= (n+2)^m exp(-tau n^2)`.

Therefore the TWO-coset outer remainder satisfies

`|E_(a,b)(rho,tau)| <=
  8 * Sum_(n=rho)^(infty) (n+2)^(m+2) exp(-tau n^2)`.

Set `k=m+2` and

`q = ((rho+3)/(rho+2))^k * exp(-tau (2rho+1))`.

If `q<1`, the ratio of consecutive summands is at most q for every n>=rho. Thus the convergent tail has the **explicit closed bound**

`|E_(a,b)(rho,tau)| <=
  8 (rho+2)^k exp(-tau rho^2) / (1-q).`

All inequalities above are strict-source mathematical deductions using only integer lattice spacing and Gaussian decay; the coefficient 8 is intentionally conservative. The condition `q<1` is part of the theorem and may FAIL for small tau, high angular moment degree or small rho. For example, at fixed rho5 and m<=6, tau1 satisfies q<1; at rho40 and m<=12, tau=0.1 satisfies q<1. The latter facts are just elementary parameter checks, not uniform Mellin estimates.

## Why this is not already a zero-free theorem

- The correction for `delta+Lambda_D` **inside the disk is exact and can be large**. It cannot be hidden inside E.
- The tail estimate is for fixed positive tau satisfying q<1; it does **not** control all tau down to zero. A Mellin integral over (0,infinity), or analytic continuation of it, requires more than this fixed-parameter error control.
- The infinite radial theta `Theta_(O_K)(tau)=Sum_(alpha in O_K)exp(-tau N(alpha))` includes alpha=0. If h(K)=1, then for Re(s)>1,

  `Integral_0^infty tau^(s-1) (Theta_(O_K)(tau)-1) d tau =
     w_K Gamma(s) zeta_K(s) =
     w_K Gamma(s) zeta(s) L(s,chi_(disc K))`.

  Without h=1, the element theta Mellin transform yields the **principal-ideal partial zeta**, not automatically the full Dedekind zeta. Neither equality says anything alone about exceptional zeros.
- Mixed angular weights `z^a conj(z)^b` are exactly retained in the finite theta moment formula but do not automatically define a Hecke character on ideals; compatibility with units, ideal classes and any conductor must be proved.
- The full-source 321^4 same-Gram/analytic bridge and independent human review #50 are unaffected. The D403 parity/valuation measurements in the other Phase285 note concern only a **16-row principal minor**, not the full 400-row Gram.

**Next decisive analytic step [H]:** pick a fixed positive tau and source degree range, compute all half-coset points exactly and certify the tail inequality with interval arithmetic; then determine whether a family of such bounds suffices uniformly as tau approaches zero for an actual Mellin comparison. Stop, rather than promote to an L-zero argument, if uniformity fails.
