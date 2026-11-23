# Phase386 — Dirichlet L-function source-matched reality gate

**23 November 2026 | AI-assisted draft | no new discriminant bound claimed**

## Scope

At pinned Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b`, `DirichletCharacter.LFunction` is the analytically continued complex Dirichlet L-function and `DirichletCharacter.differentiable_LFunction` yields complex differentiability for nontrivial characters. The Phase386 Lean module proves continuity of `realDirichletL χ s := (χ.LFunction (s:ℂ)).re` from this existing analytic theorem. It instantiates the Phase385 intermediate-value theorem to force a **complex L-function zero**, using an explicitly assumed reality hypothesis `hImagZero` for real inputs.

A zero of the real part is NOT a complex zero: `I.re=0` and `I≠0`. The hostile control is formally stated.

## Precisely what is not proved

`hImagZero`: show the actual primitive quadratic character has real L-values on the real axis. `hfactor`: show the Dedekind-to-Dirichlet product identity with the canonical primitive quadratic character of `K`. `hzeta`, `hone`: zeta(1/2) is negative and L(1,χ_D)>0. `hlarge_sign`: source-formalize Phase384's Epstein/Poisson central identity plus analytic bounds, and connect `d` to `(NumberField.discr K).natAbs`. `hZF`: a primitive quadratic real zero-free hypothesis, e.g. from a separately matched Dirichlet GRH theorem. None is hidden as a custom axiom, and the Lean theorem has all of these as explicit arguments.

The existing unconditional nine-field classification already establishes the final list in the mainline. This new chain is designed for independent proof comprehension and comparison of analytic assumptions, NOT numerical discovery.

## Verification and next gate

Run `lake build TenthDiscriminant.Phase386ComplexDirichlet` and check theorem types and `#print axioms`. This module is imported into the audited project root. Treat it as P only after actual CI success and after inspecting the printed statement; at present this is an uncompiled draft.

Next independent target: a precise `χ_D` construction and proof that its values are real and its analytically continued L-function satisfies `hImagZero`. Keep review issue #50 for the original trace-Gram proof open.
