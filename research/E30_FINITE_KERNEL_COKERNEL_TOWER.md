# E30 — FINITE KERNELS THAT DISAPPEAR IN THE TOWER

**19 November 2026 · Research branch stacked on E29.**

> An obstruction at every depth is not necessarily an obstruction to a compatible infinite history.

## Original arithmetic carrier

Continue E24–E29's conductor-two source map on exact integer coefficient
pairs, y ↦ 2y. We do not change the derivative operator, original
integer-trace Gram, lattice, sampling set, prime-labelled witnesses, or
the public actual-field theorem.

At a finite modulus 2^n, the imaginary-coordinate observer is

    f_n : Z/2^n Z -> Z/2^n Z
    f_n([y]) = [2y].

For n≥1 its kernel has two elements. On the representative level these
are [0] and [2^(n-1)]. Crucially, the canonical transition K_(n+1)→K_n
maps both kernel elements to zero.

## What E30 Lean ACTUALLY proves

The module E30FiniteKernelTransition.lean checks the exact integer
remainder implications for the four adjacent levels:

    (2a mod 4 = 0)  => a mod 2 = 0
    (2a mod 8 = 0)  => a mod 4 = 0
    (2a mod 16 = 0) => a mod 8 = 0
    (2a mod 32 = 0) => a mod 16 = 0.

It verifies that each of the kernels mod 4/8/16/32 nevertheless has a
specific nonzero representative (2/4/8/16), each annihilated by
reduction to the preceding modulus. It also proves that equal
conductor-observations at level n imply equal underlying coefficients
at level n-1 in the selected finite cases.

The missing-target obstruction behaves differently:

    2a mod 2^n != 1  (n=1,2,3,4).

Thus finite source ambiguity is progressively invisible under
compatible deeper observations, while the target odd residue stays
unattainable.

## Paper mathematics — NOT formalized in E30

For the entire tower over every n>=1, the classical claims are

    K_n = ker(2 : Z/2^n -> Z/2^n) = {0, 2^(n-1)},
    lim K_n = 0,
    ker(2 : Z_2 -> Z_2) = 0,
    coker(2 : Z_2 -> Z_2) = Z/2Z.

Do **not** pretend that finite E30 checks prove these infinite
statements. A formal next step needs explicit inverse systems,
transition compatibility and (if comparing limit-cokernel with
cokernel-limit) care about derived inverse limits.

The most important new conceptual separation is:

    finite-time kernel size vs compatible history kernel
    missing-target cokernel vs recoverable source ambiguity.

Both are typed [R]_arith objects and are **not** a measured computational
hardness residual [R]_emp, spectral curvature [R]_coh, or semantic
remainder [R]_sem.

## Research interaction

- **Hardness Kernel HK-032/033:** multiple complementary observers
  reconstruct information and give explicit Gaussian source witnesses.
- **Tenth Discriminant E24–E29:** source-locked order embeddings,
  exact original-jet Gram on image support, labelled prime observations.
- **307^4 candidate:** completely separate field-bound proof, whose
  true root and axiom audit must close.
- **Next experiment:** compare original-witness reconstruction costs
  across n with equal-resource scalar/CRT baselines. A finite modulo
  count is not a runtime speedup or a complexity lower bound.

## Release gate

Source file: lean/TenthDiscriminant/E30FiniteKernelTransition.lean.
Focused CI: .github/workflows/e30-finite-kernel-transition.yml.
Root import: lean/TenthDiscriminant.lean.

All claims of P remain conditional on exact-head Lean compilation,
allowed-axiom review and source semantic reconstruction. Negative
controls and failed builds must remain visible.
