# E33 — THE EXACT PATH THROUGH TWO DIFFERENT WORLDS

*19 November 2026 · original modular coefficient witnesses · research draft*

## A local sequence, not a scalar slogan

At k=5, the source A_25/5 is the dual-number ring
F5[epsilon]/(epsilon²), while the Gaussian target A_1/5 is the
reduced split ring F5 x F5.

Define four **F5-linear/additive** maps on the actual E28 coefficient
pairs:

    epsilon: F5 -> A_25/5,          b -> (0,b)
    iota:    A_25/5 -> A_1/5,       (a,b) -> (a,0)
    gap:     A_1/5 -> F5,           (a,b) -> r_-(a,b)-r_+(a,b)=4b,

where the target's split-prime observations are

    r_+(a,b)=a-2b,  r_-(a,b)=a+2b.

Then there is an elementary exact sequence of additive F5 spaces:

    0 -> F5 -> A_25/5 -> A_1/5 -> F5 -> 0.

- epsilon is injective.
- image(epsilon) = kernel(iota): the **source nilpotent fiber**.
- image(iota) = kernel(gap): the **prime-label diagonal**.
- gap is surjective: every missing direction has a distinct
  prime-label disagreement.

The last map is *not* a ring homomorphism; claiming a ring exact
sequence would silently change the algebraic category.

## What is truly new at the research-interface level

E28/E29 established modular invertibility/loss; E30 distinguished
finite kernel transitions from persistent missing targets; E31
showed that ambient conductor loss does not force p-divisibility
of the ORIGINAL sampled integer trace Gram; E32 checked the
nonreduced-to-reduced obstruction at the conductor prime.

E33 closes the two-sided **witness accounting** of that specific
finite algebra regime. It retains both what the source loses
(kernel) and what the target has beyond the source's image
(cokernel), and reads the latter through HK-032's two
complementary Gaussian split-prime labels.

The E33 Lean module proves *elementwise exactness*, not a general
sheaf/derived-category theorem, not an abstract Mathlib
LinearMap exact sequence, not an intrinsic complexity lower
bound, and not an improvement to the 307^4 research field bound.

## Correctness/provenance gates

- Source: E28's residueMul, residueFrame, splitPlus and splitMinus.
- Root import: E33ConductorCRTExactness.lean.
- Focused workflow: e33-conductor-crt-exactness.yml.
- All exactness claims must survive an exact-head Lean compilation
  and transitive allowed-axiom audit. The above finite algebra is
  mathematically elementary but the GitHub proof code remains a
  draft until green.
- The complete 307^4 source-to-field certificate, human review
  (#50), and cross-method comparison (#51) are independent.
- Original sampled jets and trace Gram are never altered here.

## Next discriminating connection

Build a formal adapter to the Hardness-Kernel GaussianInt
representation, then ask whether an actual original-jet row
factorization has prime-power content not already captured by
unimodular source controls. Kill any alleged gain that disappears
under matched original support or independent integer-oracle
reconstruction.

**A moving algebra remembers two distinct remainders:
the missing source witness and the additional target direction.**
