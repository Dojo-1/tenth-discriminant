# Phase327 · 360 × 360 · orthogonal, anti-ambiguous F1-prime interleaving

> One generator. Two complete turns. Many coefficient characteristics.
> Never confuse a change of coordinates with new arithmetic evidence.

**Status:** pre-registered exact finite algebra experiment; not a
new number field, not a theorem about the original integer Gram, and
not a discriminant improvement.

## The foundational choice

A nonzero unital ring of characteristic 1 does not exist:
`char=1` implies `1=0`, hence `x=x*1=x*0=0`.
So neither a one-element ordinary field nor a new prime characteristic
called `1` can satisfy the conventional field axioms. Every finite
field has order `p^n` for a prime `p`.

Our **proposed** `F1'` is instead a *signed pointed-monoid
presentation* plus a family of base-change fibers. It borrows the
multiplicative idea and sign relation from `F1`/`F1^2`-style
blueprints, but **does not claim** that the full noncommutative
presentation is already an ordinary commutative F1-scheme or a field.

Let `H_D=Cl_125(K_D) rtimes C2`, the explicit semidirect group from
Phases324–325, and let
`Q8={+/-1,+/-i,+/-j,+/-k}`. The sign element
`s=(-1,e)` is central in `Q8 x H_D`. Define

```math
M_D=\{0\}\sqcup(Q_8\times H_D),\qquad
A_{D,\mathbb Z}
=\mathbb Z[Q_8\times H_D]/(s+1).
```

This **integral** algebra has quaternionic basis `1,i,j,k` above
each group element of `H_D`: it is the Lipschitz quaternion order
tensored with `Z[H_D]`, and has free integral rank `4|H_D|`.
The regular left module is cyclic:
`A_{D,Z} * Omega=A_{D,Z}`, `Omega=1`.
"One element" means **one cyclic generator**, not a cardinal-one
ordinary field.

The sign relation comes from a characteristic-free quotient of a
group algebra; it does **not** invent addition in the pointed monoid.

## Prime-characteristic interleaving

For each actual prime characteristic `ell`, define the fiber

```math
A_{D,\ell}=\mathbb F_\ell\otimes_\mathbb Z A_{D,\mathbb Z}.
```

The `ell=2` and `ell=7` fibers intersect through the *same*
integral source only after reduction:

```math
A_{D,\mathbb Z}/14 A_{D,\mathbb Z}
\simeq A_{D,2}\times A_{D,7}.
```

This is a CRT isomorphism of **rings**. It does not give a field of
size 14, nor recover arbitrary unbounded integral coefficients from
their residues. `Z/14Z` has nonzero zero divisors.

The original quaternionic relations are

```math
i^2=j^2=-1,\qquad ij=k=-ji.
```

Over coefficient characteristic `2`, scalar signs merge:
`+1=-1`; thus `ij=ji`, and the nonzero element `1+i`
satisfies `(1+i)^2=0`. It is a nilpotent. At `ell=7`,
`ij=-ji` remains meaningful. The two fibers are **not** two
isomorphic views preserving all the signed relationships.

The order of the group `H_D` is 15000, 30000, 60000 in our
three fields, so `7` (also `11`) does not divide it, whereas
`2,3,5` do. By Maschke's theorem, `F7[H_D]` is semisimple;
`F2[H_D]`, `F3[H_D]`, `F5[H_D]` are not. This is a
property of finite group algebras, not a proof that a quaternionic
fiber is a division field.

**Anti-ambiguity types:** denote a rational Frobenius prime by
`p`, a coefficient characteristic by `ell`, and the ray
modulus by `m`. They are three different mathematical roles.
`p=2` has Frobenius order 100 over the conductor-125 ray field in
the Phase325 examples, while `ell=2` collapses scalar quaternionic
sign. These facts must never be conflated.

## 360 × 360, spin versus frame

In the spin cover of `SO(3)`, orthogonal **half turns**
are represented by `i` and `j`. Each full 360-degree turn
lifts to `-1`; two full turns lift to `+1`.
The half turns, not the complete turns, anticommute:

```math
i j=-j i,\quad [i,j]=ij i^{-1}j^{-1}=-1,\quad
i^2=j^2=-1,\quad i^4=j^4=+1.
```

**Two 360-step sweeps:** The exact harness exhaustively checks
`(a,b) in {0,...,359}^2` for the words `i^a j^b` versus
`j^b i^a`. Here `a,b` are *counts of half-turn pulses*, not
individual physical degrees and not a claim to exactly model
continuous rotations at 1-degree resolution. It verifies

```math
i^a j^b=(-1)^{ab}j^b i^a.
```

Expected counts among 129,600 pairs:
- 32,400 anticommuting (both pulse counts odd).
- 97,200 commuting.
- In characteristic 2 all 129,600 become commuting as scalar
  quaternionic words; this is information loss, not extra symmetry
  of the original integral algebra.

A second ACAF arm constructs **2048** deterministic candidate pairs
of orthogonal pure imaginary integer quaternions. It checks
orthogonality and exact anticommutation (with degenerate axes skipped).
A third arm randomizes moving frames and integral coefficients, checking
norm, scalar pairing, ordered frame composition and base-change
covariance under `ell=2,3,5,7,11`. Fixed seeds and bounded
coefficients keep the experiment reproducible.

### Moving moving frame: an important kernel

For a norm-one quaternion `u` let `Phi_u(x)=u x u^{-1}`.
This acts covariantly:

```math
\Phi_u\circ\Phi_v=\Phi_{uv}.
```

But the **adjoint** action forgets the central sign:
`Phi_{-1}=id`, whereas left **spinor** multiplication by
`-1` is not the identity over characteristic zero. Even before
prime reduction, the adjoint and spinor representations cannot be
interchanged. This is a permanent negative control on any moving
frame programme.

## New obstruction: some original jet rectangles cannot carry the quaternion algebra

The characteristic interleaving reveals a **module-rank obstruction**,
independent of spin-sign loss.

Over `Q`, the Hamilton quaternion algebra
`H_Q=Q+Qi+Qj+Qk` is a **division algebra**: for a nonzero
quaternion, the rational norm is the strictly positive sum of four
squares, and the inverse is `conjugate(x)/norm(x)`. A finite-dimensional
unital left `H_Q`-module is free over that division algebra.
Consequently,

```math
\mathbb H_{\mathbb Q}\curvearrowright \mathbb Q^N
\quad\Longrightarrow\quad 4\mid N.
```

This necessary condition applies to **any** unital action of
`A_D tensor Q` on the unchanged original jet row space
`Q^{R(D) S(D)}`, because its quaternionic coefficient subalgebra
must also act unitaly.

The proposed Phase323 dimensions use
`R(D)=floor(D/4)`, `S(D)=floor(R(D)/25)`.
An exact counterdomain witness above the proposed cutoff is

```text
D = 315^4 + 6 = 9,845,600,631  (squarefree, D mod 4 = 3)
R = 2,461,400,157              (R mod 4 = 1)
S =    98,456,006              (S mod 4 = 2)
R*S mod 4 = 2.
```

There can therefore be **no universal unital quaternion action**
on every original `RS`-dimensional rational jet space in the
proposed discriminant domain. This does not invalidate the
existing determinant argument; it rejects a particular *new*
geometric transport route. It also does not assert this D has class
number one.

There is a sharp opposite control in **characteristic 7**.
Two `2x2` matrices over `F7` give a faithful representation
of the coefficient quaternion algebra:

```math
I=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad
J=\begin{pmatrix}3&2\\2&-3\end{pmatrix}\pmod7.
```

They satisfy `I^2=J^2=-1`, `IJ=-JI` over `F7`.
The flattened four matrices `1,I,J,IJ` have determinant
`-45 = 4 mod 7`, so they form a basis of `M2(F7)`.
Thus the characteristic-7 coefficient quaternion algebra is
`M2(F7)`, not a division field, and its two-dimensional module
cannot be lifted to an unchanged two-dimensional rational
Hamilton-quaternion module.

**Consequence for the programme:** a common cyclic integral
*carrier* is coherent, but a same-rank quaternionic
*representation on the original ordinary-Z jets* is not globally
available. The viable alternatives are to keep quaternionic
structure in an external coefficient bundle, to restrict the
frame action to subgroups that genuinely act integrally, or to
construct a typed stabilization/descent with an explicit Gram
determinant comparison. None is licensed to change the original
discriminant inequality silently.

## Falsification and evidence discipline

- **M / finite exact:** pulse sweep, random orthogonal families,
  quaternion algebra laws, signed/char-2/odd reduction,
  CRT, typed prime roles, toy one-generator group algebra, and the squarefree jet-rank witness.
- **P / mathematical identities:** the algebra presentation,
  CRT and group-theoretic spin relations, subject to the stated
  definitions. The code is finite verification, not an external proof.
- **H / open:** a globally glued one-generator bundle spanning all
  discriminants and conductors, and a nontrivial moving-frame
  geometric connection rather than discrete inner automorphisms.
- **R / rejected inference:** treating `F1'` as a new ordinary field,
  treating the two prime fibers as the same field, interpreting
  integer pulse counts as 1-degree physical rotations, claiming
  noncommutation for two complete 360-degree spin lifts, or
  inferring extra 2-adic determinant valuation from characteristic-2
  nilpotence.

The original source integer Gram only acquires new arithmetic
content if there is an independently established integral,
source-preserving representation

```math
\rho_D:A_{D,\mathbb Z}\longrightarrow
\operatorname{End}_{\mathbb Z}(J_D)
```

that preserves the original ordinary-Z jet domain and provides a
verified integer row transformation with determinant `+/-1`.
No such representation is constructed or assumed here. In particular
modular degeneration does not prove a discriminant bound.

## Execute

```bash
python3 -m unittest discover -s research/phase327 -p 'test_*.py' -v
```

No non-standard Python dependencies. The CI workflow runs these
same exact tests only on changes in `research/phase327/`.

Mathematical references:
- Oliver Lorscheid, *The geometry of blueprints*, Advances in
  Mathematics 229 (2012), 1804–1846,
  https://doi.org/10.1016/j.aim.2011.12.018
- Lorscheid, *Lectures on F1*, signed monoids and cyclotomic
  F1-extensions, https://www.lorscheid.org/notes/Lectures_on_F1.pdf
- Standard finite-group theory: Maschke's theorem and the
  `Spin(3)=SU(2)` double cover of `SO(3)`.

**Next falsifier:** build an explicit integral action on a small
*original* ordinary-Z jet rectangle and check preservation of
its Gram before proposing any new arithmetic valuation.
