# Phase385 — central sign-to-real-zero bridge (draft)

**23 November 2026 · AI-assisted research; no originality claim for GRH=>199.**

## Actual Lean proof target

For an arbitrary real function L continuous on [1/2,1], assume
- zetaHalf < 0 and dedekindHalf > 0;
- dedekindHalf = zetaHalf * L(1/2);
- L(1) > 0.

Then there is a beta in (1/2,1) with L(beta)=0. The proof uses the actual Mathlib intermediate value theorem and strict endpoint exclusion. It does **not** assume GRH.

The conditional bound theorem adds explicitly: (200 <= d => dedekindHalf > 0) and no zeros of L in (1/2,1). Then d<=199. Here d is a natural number parameter, **not yet linked inside Lean** to the actual NumberField.discr; that link and the analytic definitions remain unresolved.

## Explicit scope

The Lean file proves a valid implication about real functions given precise hypotheses, **not** any analytic or number-field theorem. It does not supply the Epstein/Poisson identity; its meromorphic continuation and central limit; Euler's constant, log and Bessel bounds; positivity from the class-number-one quadratic principal form; the primitive quadratic character; Dedekind factorization; the sign of zeta(1/2); or L(1)>0. These are the next source-level lemmas.

The Phase384 exact-rational certificate `research/phase384/central_half_rational.py` passed independently in the local environment, and the classical central formula was numerically cross-checked on six known odd fundamental discriminants. Neither finite calculation is a universal analytic proof.

## Verification gates

The new source `lean/TenthDiscriminant/Phase385CentralSign.lean` is included from `lean/TenthDiscriminant.lean`. The focused GitHub workflow builds the module with pinned Lean 4.19.0 / Mathlib c44e0c8 and prints transitive axioms. The full-root workflow independently compiles and audits project imports.

Proof statuses: **P** for the Lean theorem only after compilation; **A** for all explicit analytic inputs; **M** for the exact-rational Phase384 script; **R** for claims of novelty of the known GRH-dependent 199 threshold.

The concrete next target is to replace `hfactor`, `hlarge_sign`, and the endpoint-sign hypotheses one at a time with theorem applications about the exact primitive quadratic `L(s,chi_D)` and actual number-field discriminant. The original trace-Gram and issue #50 remain independent.
