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

## 4. Exact controls and limitations

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

The smallest next mathematical target for a genuine bridge is a
**typed, integral, source-preserving ray action** `T_g` on the original
jet module, with `T_g^T B T_g=B` or a certified determinant-divisor
transport, and a nontrivial field-uniform estimate on its relevant
nontrivial character components. Neither is asserted here.

Implementation: `semidirect_ray_representations.py`.
Adversarial tests: `test_semidirect_ray_representations.py`.
