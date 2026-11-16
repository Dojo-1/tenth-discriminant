# 侘未来 · Phase335
## A filtered lattice of original ordinary jets

> One polynomial. Two integral coordinate frames. A single exceptional prime.

This phase connects the classical index-two order inclusion to a
**nonvacuous polynomial-coefficient filtration** in the original
Tenth Discriminant source. It does **not** change the original
sample set Q, integer-pair evaluations, ordinary derivatives in Z
(holding W fixed), original trace pairing, or original Gram determinant.

## The mathematical carrier

Let A be the free integer module of original rectangular polynomial
coefficients, indexed by the unchanged row-major basis
`Z^r W^s`, `0<=r<R`, `0<=s<S`:

```math
A=\bigoplus_{0\le r<R,\ 0\le s<S}\mathbb Z\,Z^rW^s.
```

For `c in A`, define the original ordinary-jet evaluation

```math
E(c)(a,j)=\sum_{r,s}c_{r,s}
  \left.\partial_Z^j(Z^rW^s)\right|_{Z=z_a,W=\bar z_a}
  \in L=\mathbb Z[\sqrt{-D}].
```

The code uses **exactly** the existing
`integerDerivativeRow` and its original row ordering. It defines
sets of *coefficient vectors*, not the false condition that every
individual monomial row is divisible by a modulus:

```math
\begin{aligned}
\mathrm{Fil}_L(m)&=\{c\in A:E(c)(a,j)\in mL
       \text{ for every }a\in Q,\ 0\le j<J\},\\
\mathrm{Fil}_{\mathcal O}(m)&=\{c\in A:E(c)(a,j)\in m\mathcal O_K
       \text{ for every }a\in Q,\ 0\le j<J\}.
\end{aligned}
```

The zero vector belongs for every modulus. Nonzero vectors can belong
as well: `H(Z,W)=Z²-W²` has all its original ordinary jets even, even
though its two coefficients are units. This shows why the whole-coefficient
carrier is essential.

## The local comparison

For squarefree `D≡3 mod 4`, classical arithmetic gives

```math
L=\mathbb Z[\sqrt{-D}]\subset\mathcal O_K
=\mathbb Z[(1+\sqrt{-D})/2],\qquad [\mathcal O_K:L]=2.
```

The coordinate map is `(x,y) -> (x-y,2y)`. Consequently, for any
odd modulus `m` (including odd prime powers), both coordinates
are `m`-divisible on one side exactly when they are on the other:

```math
\mathrm{Fil}_L(m)=\mathrm{Fil}_{\mathcal O}(m)
\qquad(m\text{ odd}).
```

For arbitrary integral `q`, the correct conductor correction is

```math
\boxed{
\mathrm{Fil}_L(2q)
\subseteq\mathrm{Fil}_{\mathcal O}(2q)
\subseteq\mathrm{Fil}_L(q).
}
```

This says that transport from maximal-order divisibility back to the
original source loses **at most one power of two**. It does not produce
a new `2`-adic lower bound for the original Gram by itself.

The loss is genuinely sharp in simple coefficient examples: for a
single original source sample `z=2^k(1+sqrt(-D))` and polynomial
`P(Z,W)=Z`, the value belongs to `2^(k+1)*O_K` but not to
`2^(k+1)*L`.

## The mixed factor and ordinary derivatives

Set `H(Z,W)=Z²-W²`. At an original point
`z=x+y sqrt(-D)`, `w=conj(z)`,

```math
H(z,w)=4xy\sqrt{-D},\quad
\partial_ZH(z,w)=2z,\quad
\partial_Z^2H(z,w)=2.
```

Thus `H(z,w)` is always divisible by 4 in L, but at `z=w=1`
the first and second ordinary derivatives are 2, **not** divisible
by 4. The full-jet power-two factor cannot be upgraded from
`2` to `4` merely by looking at order zero.

In maximal-order coordinates `omega=(1+sqrt(-D))/2`, its
conjugate has coordinates `(1,-1)` and

```math
H(\omega,\bar\omega)=2\omega-1.
```

Its first maximal-order coordinate is odd. This counterexample
explicitly prevents changing Q to maximal-order sample points while
reusing the source-specific H divisibility.

### A further *paper-level* graded bound (not yet in Lean)

Hold `W=w` fixed and expand the same polynomial in an auxiliary t:

```math
H(z+t,w)=A+2zt+t^2,\qquad A=4xy\sqrt{-D}\in4L.
```

In `(A+2zt+t²)^b`, a monomial of degree `j` in t comes from
`a+c+d=b`, `c+2d=j`, with `a` factors A, `c` factors 2zt,
and `d` factors t². It therefore contains a factor
`2^(2a+c)=2^(2b-j)`. Multiplying the coefficient by j! yields

```math
\boxed{
\left.\partial_Z^jH(Z,w)^b\right|_{Z=z}
\in j!\,2^{2b-j}L\qquad (0\le j\le2b).
}
```

All higher ordinary derivatives vanish. This elementary paper proof
still needs a dedicated Lean formalization if it is to enter the
trusted proof chain. The `j!` factor is already represented
elsewhere by the original ordinary-jet factorial filtration;
it must **not** be counted twice.

## Controlled evidence

- **P at exact-head 336a1c9:** [GitHub Actions 43956865171](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43956865171) passed full polynomial-coefficient tests, the Lean module and standard-axiom inspection; it proves equality of the two odd-modulus
  coefficient-filtration sets; index-two inclusions; zero membership;
  exact original H value and derivative counterexamples; maximal-order
  negative control
- **M:** [independent integer tests](test_jet_filtration.py) over original
  monomial jets and actual integer combinations, including the nonzero
  H witness and all sampled binary negative cases
- **H:** graded all-b powers lemma above; any upgrade of invariant
  factors or the original Gram determinant; complete `313^4` source
  comparison
- **R:** the [initial all-rows proposition](CI_FAILURES.md), which was
  proved for a too-weak (often false) antecedent, is not a polynomial
  module filtration; this semantic correction must remain visible

**Formal source:** [Phase335JetFiltration.lean](../../lean/TenthDiscriminant/Phase335JetFiltration.lean).
**CI:** [dedicated workflow](../../.github/workflows/phase335-jet-filtration.yml).
**Failed-run receipts:** [CI_FAILURES.md](CI_FAILURES.md).

## Decisive next comparison

To improve `315^4`, the stronger local profile must lead to an
**additional invariant factor of the same original integer
ordinary-jet Gram**, beyond the already certified joint binary
basis and factorial weights, under matched computational controls.
Otherwise it is useful structural information rather than a smaller
discriminant bound.

Separately, the verified sharper analytic saving at `315^4` remains
the most direct candidate for an unconditional smaller fourth-root
threshold, provided every source, geometry and scalar guard is
re-established on that smaller entire domain.
