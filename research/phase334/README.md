# Phase334 — the conductor-two obstruction

> Same quadratic field. Two integral orders. Different residue rings at the prime 2.

This phase isolates a standard commutative-algebra fact that matters for
the tenth-discriminant **original ordinary-jet** source. It does not
replace the existing Gram, prime divisor, or sampling set.

## The common arithmetic framework

For squarefree `D > 0`, `D ≡ 3 (mod 4)`, set

```math
L=\mathbb Z[\sqrt{-D}],\qquad
\mathcal O_K=\mathbb Z[\omega],\qquad
\omega=(1+\sqrt{-D})/2.
```

The index is `[O_K:L]=2`; equivalently, `L` is the quadratic order
of conductor two. The explicit inclusion `(x,y) -> (x-y,2y)` was
checked in [Phase333](../phase333/README.md). Its determinant is 2:
it is a ring isomorphism after localization at every **odd** prime,
but **not** at the prime 2.

In the maximal-order basis, multiplication is

```math
(a+b\omega)(c+d\omega)=
\left(ac-\frac{D+1}{4}bd\right)
+(ad+bc+bd)\omega.
```

[The Phase334 Lean module](../../lean/TenthDiscriminant/Phase334ConductorTwo.lean)
checks that this multiplication agrees with the original
`pairMul` under the unchanged integral inclusion.

## Why the binary source polynomial is exceptional

Because `D` is odd, the original source ring modulo two is

```math
L/2L\simeq\mathbb F_2[t]/(t^2+1)
=\mathbb F_2[\varepsilon]/(\varepsilon^2),
\quad\varepsilon=t+1.
```

It contains a **nonzero nilpotent**. Consequently, every residue
`z in L/2L` satisfies `z^4-z^2=0`.
The existing [source null-polynomial lemma](../../lean/TenthDiscriminant/BinaryNullPolynomial.lean)
already proves this value statement for all original integer-pair
source points. Phase334 recovers it without modifying the polynomial.

This assertion is not valid for all maximal-order points. For
`D=163`, the minimal polynomial of `ω` modulo 2 is

```math
X^2+X+1,
\qquad\mathcal O_K/2\mathcal O_K\simeq\mathbb F_4.
```

Therefore `ω^4=ω` while `ω^2=ω+1`, so

```math
\omega^4-\omega^2=1\quad\text{in }\mathbb F_4.
```

The exact integral witness is

```math
\omega^4-\omega^2=1681-82\omega,
```

whose first coefficient is odd. **This is a negative control: the
source binary-null polynomial is not a universal maximal-order
Frobenius polynomial.**

The behavior depends on the splitting of 2. For `D=7`,
the maximal-order quotient is split and the same exact test is

```math
\omega^4-\omega^2=4-4\omega\in2\mathcal O_K.
```

This second control prevents extrapolation from the `D=163` example.

## What this establishes — and does not

- **P (classical algebra):** the conductor-two inclusion; the
  nonreduced source residue ring; the explicit D163 and D7 identities
  in the maximal-order basis
- **P only after CI:** the exact Lean statements for multiplicativity,
  the nonzero nilpotent, original-source null-polynomial parity and
  both maximal-order controls
- **M:** [finite exact tests](test_conductor_two.py) independently enumerate
  and compare the relevant residue rings, with original source algebra
  held fixed
- **R:** any attempted transport of the source binary polynomial's
  divisibility to arbitrary maximal-order points; any inference of a
  new original-Gram valuation merely from the index-two inclusion
- **H (next):** a stronger *same-source* local jet-filtration theorem,
  compatible with the original unimodular row frame, with demonstrable
  additional valuation beyond Phase331

**Verification:** [dedicated GitHub Actions workflow](../../.github/workflows/phase334-conductor-two.yml).
The [first failed Lean run](https://github.com/Dojo-1/tenth-discriminant/actions/runs/43947209729)
is preserved in the [failure ledger](CI_FAILURES.md); it was an
elaboration problem, not an algebraic counterexample.

The two complementary research tracks remain standard mathematics:
local quadratic-order and prime-ideal arithmetic, versus real
geometric determinant bounds. The only legitimate meeting point
for a new discriminant theorem is an exact inequality on the
**same positive integer Gram determinant**.
