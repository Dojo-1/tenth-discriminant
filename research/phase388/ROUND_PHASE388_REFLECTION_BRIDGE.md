# Phase388: Quadratic Dirichlet L-function reflection

23 November 2026. AI-assisted research draft, not a new discriminant record.

## Target

For a nontrivial quadratic Dirichlet character with chi^2=1, prove L(conj z,chi)=conj(L(z,chi)) for all complex z. Consequently, Im L(t,chi)=0 for all real t. This eliminates the explicit Phase386 imaginary-part hypothesis.

## Logic

1. Quadratic coefficients are in {-1,0,1} (Phase387, Lean verified).
2. In Re(z)>1, use LFunction_eq_LSeries, conjugation of the infinite sum, conjugation of positive-base complex powers, and exact coefficient reality.
3. Locally backport the double-conjugation differentiability principle using hasDerivAt_iff_tendsto and norm-preserving conjugation, since the pinned calculus revision does not contain the newer corresponding lemma.
4. Apply the analytic identity theorem on the connected complex plane to extend the half-plane identity.
5. Derive the reality of L on all real inputs and instantiate Phase386 without hImagZero.

## Status

This file is an unverified draft until focused Lean CI and the full-root audit are green.

Still explicit assumptions: actual K-to-chi_D primitive conductor map; Dedekind factorization; Epstein-Poisson formula and central positivity; positive endpoint L(1,chi_D); and zero-freeness or GRH for the final conditional bound. In Phase386 the natural number d is not yet tied to NumberField.discr. Original trace-Gram issue #50 remains open.

Classification labels: P only for compiler-verified exact statements, A for the external analytic/field links, M for bounded rational computations, R for new-record claims concerning the known GRH-conditional 199 result.
