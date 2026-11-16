# Phase324 — Characters become representations

**Scope:** exact finite ray-class representation theory for `D163`, `D187`,
and `D203`, atop the existing Phase321 ideal-aware groups and Phase322
conductor-125 dual characters. The one research branch remains the
consolidated `research/phase309-original-source-picard-minors`.
This file records intended mathematics, not a new discriminant theorem.

## 1. Ray characters and conductor projectors

Write `G = Cl_125(K)`, `G_k = Cl_(5^k)(K)`, `k=0,1,2,3`,
and `K_k=ker(G -> G_k)`. The regular representation
`rho:G -> GL(C[G])` is `rho(g)e_h=e_(gh)`. Its exact averaging
operators are

```math
P_k=\frac{1}{|K_k|}\sum_{h\in K_k}\rho(h),\quad
E_0=P_0,\quad E_k=P_k-P_{k-1}\quad(k=1,2,3).
```

The kernels shrink with `k`; the projectors are mutually compatible,
self-adjoint and idempotent. The shell operators `E_k` are orthogonal
projectors, with ranks

```math
\mathrm{rank}(E_0)=h,\qquad
\mathrm{rank}(E_1)=11h,\qquad
\mathrm{rank}(E_2)=288h,\qquad
\mathrm{rank}(E_3)=7200h.
```

These are group-theoretic identities, not analytic prime estimates.
For any finitely supported function `f:G -> C`, with
`hat f(chi)=sum_g f(g) overline{chi(g)}`, exact Parseval yields

```math
\sum_{\mathrm{cond}(\chi)=5^k}|\widehat f(\chi)|^2
= |G|\,\|E_kf\|_2^2.
```

For a finite prime-ideal catalog, with `f(g)` the number of catalog
ideals in ray class `g`, the principal count at modulus `5^k`
is **exactly** `|K_k| (P_k f)(e)`. We test this by direct kernel
membership on actual prime-ideal records. A log-weighted sum would
have the same formal identity with `log Np` weights, but this is
not a lower bound for principal primes.

## 2. Complex conjugation acts by a norm twist

For an ideal `I` coprime to 5 and `g=[I]` in the ray group,

```math
g\,\sigma(g)=[(N I)],\qquad
\sigma(g)=\nu(g)g^{-1},\quad \nu(g)=[(N I)].
```

In the Phase321 cocycle coordinates `g=(c,u)`, with distinguished
representative ideal `I_c`, the norm is computed by the exact residue
`N(I_c) N(u) mod 125`, not guessed from ordinary class inversion.

A decisive negative control: `[(2)]` is fixed by conjugation yet has
order 50 modulo 125, so `sigma` is **not** inversion on `G`.
The new group is the semidirect product

```math
H = G \rtimes_{\sigma} C_2,
```

not automatically a generalized dihedral group.

## 3. Classification of finite semidirect representations

The dual involution is `chi -> chi circ sigma`. A fixed character
has two 1D extensions to `H`, with the involution acting as `+1`
or `-1`. A two-element orbit `{chi, chi circ sigma}` induces
one irreducible complex 2D representation:

```math
\pi_\chi(g)=
\begin{pmatrix}\chi(g)&0\\0&\chi(\sigma(g))\end{pmatrix},
\qquad
\pi_\chi(\sigma)=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
```

With `F=#Fix(dual sigma)=#Fix(sigma on G)`, there are `2F` 1D
irreducibles and `(|G|-F)/2` 2D irreducibles; the sum of squared
dimensions is `2|G|=|H|`. The fixed-space equality follows from
finite Pontryagin duality. The code verifies it independently by
enumerating both group and dual fixed elements.

At D163, an elementary signed-unit count gives `F=100`,
so `H` has **200** one-dimensional irreducibles and **3,700**
two-dimensional irreducibles. The values for D187/D203 must be
measured from actual cocycle coordinates rather than inferred
by multiplying D163's fixed count by the ordinary class number.

## 4. Verified finite results and the next exact inequality

The first complete exact-head run, `43848804352` (commit
`f0a20318f22e7ec235dcdd021e80bcfedefa3659`), passed 9/9 tests.
These are **exact finite calculations**, not independent field theorems.

| D | Fixed sigma characters | 1D irreps | 2D irreps |
|---|---:|---:|---:|
| 163 | 100 | 200 | 3700 |
| 187 | 200 | 400 | 7400 |
| 203 | 200 | 400 | 14900 |

Per exact conductor 1,5,25,125 the *fixed-character* counts are:
- D163: (1,3,16,80).
- D187: (2,6,32,160).
- D203: (2,6,32,160).

The actual bounded catalog of prime ideals over rational p <= 441 has
the following numbers in the **principal ray class after reduction**:

| D | Ordinary class | Mod 5 | Mod 25 | Mod 125 |
|---|---:|---:|---:|---:|
| 163 | 118 | 25 | 4 | 0 |
| 187 | 78 | 19 | 6 | 0 |
| 203 | 55 | 17 | 2 | 0 |

Prime ideals above 5 are excluded. In particular, *none* of these
bounded catalogs supplies a ray-principal prime at modulus 125.
This is a negative control against extracting existence or positive
density from conductor filtration alone.

Here is the exact inequality that representation theory **does**
deliver. For a finite nonnegative prime-ideal weight function, let
`A_c(x)` denote the total weights in class `c in G_k`,
`W(x)=sum_c A_c(x)`, and
`S_chi(x)=sum_c A_c(x) chi(c)`. Character orthogonality and
Cauchy--Schwarz give

```math
A_e(x) \ge
\frac{W(x)}{|G_k|}
-\frac{\sqrt{|G_k|-1}}{|G_k|}
 \left(\sum_{\chi\neq1}|S_\chi(x)|^2\right)^{1/2}.
```

The second moment is exactly
`|G_k| sum_c |A_c(x)|^2 - W(x)^2` by Parseval.
To force a **positive** lower bound using this estimate, one needs a
*new*, genuinely arithmetic control
`sum_(chi != 1) |S_chi|^2 < W(x)^2/(|G_k|-1)`.
This is **not** established by the finite character tables or by
orthogonality. It is a falsifiable analytic target, not an assumption
silently added to the original Gram bound.

The integer-lattice danger is concrete. For `G=C2`, the integral
Fourier matrix
`H=[[1,1],[1,-1]]` has `det(H)=-2`, not `+/-1`.
If the original Gram is `I_2`, the transformed Gram is `2I_2`
with determinant `4`, although the original determinant is `1`.
The apparent additional factor `2^2` belongs to `det(H)^2`,
not to the original Gram. A negative-control test now records this
failure mode explicitly.

## 5. Exact controls and limitations

The computational test:
- checks the actual cocycle-based norm action on every group element;
- checks involutivity, automorphism law, and conjugate split-prime ideals;
- verifies the involution on every dual character and preservation of
  exact conductor;
- verifies the 1D/2D irreducible dimension identity and exact
  principal/nonprincipal bounded prime-ideal shell counts;
- checks exact rational subgroup projectors on a hostile toy group;
- retains the rational-principal-(2) non-inversion negative control.

**What this does not establish:**

1. A nontrivial uniform estimate for the prime-ideal sums in the
   nonprincipal character sectors. Orthogonality and Parseval cannot
   force principal primes: arbitrary finite mass can be concentrated
   on a nonprincipal ray class.
2. An integral action of `G` or `H` on the **original** ordinary-Z
   jet lattice and trace Gram. Fourier projectors have denominators
   `|K_k|`; these are generally not integer-unimodular row changes.
3. An improved 315^4 bound. That candidate independently requires
   the joint binary original-jet divisor, the complete odd-prime
   logarithmic bridge, same-Gram geometry, and field reconstruction.
4. A global Euler product, zero-free region, Chebotarev error term,
   or an exceptional-zero exclusion.

Two source-compatibility counterexamples sharpen the boundary:

- An inert rational ideal `(p)` is fixed by complex conjugation. Hence
  **every induced 2D block is scalar on it**,
  `pi_chi([(p)]) = chi([(p)]) I_2`. The ten selected Phase323
  small inert primes cannot create an extra independent 2D
  determinant factor merely through these ray representations.
- Conjugation swaps the two polynomial variables. On `P(Z,W)=Z`,
  `partial_Z(sigma P)=partial_Z W=0`, but
  `sigma(partial_Z P)=1`. Therefore the original **ordinary-Z jets**
  are not conjugation-equivariant. The original `R by S` rectangle
  is also not generally invariant under swapping the monomial
  exponents when `R != S`. Enlarging the jet space or symmetrizing
  the rectangle would change the original Gram and require a new
  correspondence proof.

The smallest next mathematical target for a genuine bridge is a
**typed, integral, source-preserving ray action** `T_g` on the original
jet module, with `T_g^T B T_g=B` or a certified determinant-divisor
transport, and a nontrivial field-uniform estimate on its relevant
nontrivial character components. Neither is asserted here.

Implementation: `semidirect_ray_representations.py`.
Adversarial tests: `test_semidirect_ray_representations.py`.
