# Local determinant multiplicity through Taylor coordinates

**Status: the local multiplicity theorem is checked in Lean. The global jet-uniqueness and class-number theorems remain open.** No discriminant cutoff or saved numerical certificate is changed. No novelty or independent semantic-review claim is made.

## Verified snapshot

Code and tests at `9c41b2482fc69d8e53f906c2d0dd4357dc4909ef` passed [workflow 39789129577](https://github.com/Dojo-1/tenth-discriminant/actions/runs/39789129577), job `119860130933`. The PR job built synthetic merge `b83a39e17fe29cd826959e83bf385c5559631e09`; both commits have the same tree `0eb83dc409c13a4b0e3716d78c4e8eb0d5c6fe3d`.

The successful gates were source linkage for all 250 endpoint pairs, `lake build`, the compiled transitive axiom audit, and the full expanded control suite. Lean 4.19.0 and Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` remain pinned. The audit permits only `propext`, `Classical.choice` and `Quot.sound`; its 145 compiled theorem entries include generated auxiliaries and are not a completion score. Two nonfatal tactic-style warnings remain, in `TraceGram.lean` and `SylvesterLocal.lean`.

## Exact mathematical scope

Let K be a field and write F in K[W][Z]. Choose a natural number a with degree in Z at most a. Keep the Sylvester coefficient matrix of F and its Z derivative at its original size a+(a-1). For a>=1 this is 2a-1. At a sample (z,w), assume that F(Z,w) is not the zero polynomial and that (Z-z)^m divides it. The theorem is

$$
(Z-z)^m\mid F(Z,w),\quad F(Z,w)\ne0
\quad\Longrightarrow\quad
(W-w)^{m-1}\mid\det S_a(F,\partial_ZF).
$$

Natural-number subtraction is truncated at zero. The local direction works over **any field**. Characteristic zero and irreducibility belong to the later nonzero-determinant argument, not to this local implication. There is no assumption that the leading Z coefficient remains nonzero at w.

`fixedDerivativeSylvester_multiplicity_at_nonzero` derives m<=a from nonzero specialization and degree monotonicity, then applies `fixedDerivativeSylvester_multiplicity`. The latter keeps m<=a explicit. A zero specialization is divisible by every power; it must not be assigned a finite root order in the later factor argument.

## Why Taylor coordinates remove the corank detour

Represent each output polynomial of degree less than N by its coefficient column. Translation Z -> Z+z has coefficient matrix

$$T_{ij}=[Z^i](Z+z)^j,\qquad 0\le i,j<N.$$

It is upper triangular with diagonal one, hence det(T)=1. This is an explicit matrix, not an assumed invertible transformation.

Every specialized Sylvester column is a shifted copy of F(Z,w) or its Z derivative. An m-fold root of F gives the common factor (Z-z)^(m-1) in all those columns. Their first m-1 Taylor coefficients therefore vanish. Those are m-1 **whole rows** of T*S after W=w. Before specialization, every entry in each such row is divisible by W-w. Extracting one factor per row proves the determinant divisibility. The determinant-one transformation preserves the determinant.

The proof never shrinks the matrix after specialization. It proves the particular local multiplicity implication required by the earlier fixed-size Sylvester argument; it does not claim a separately formalized theorem about every arbitrary corank normal form.

## Claim-to-declaration map

| Step | Lean declaration | Boundary |
|---|---|---|
| Extract one divisor per row | `row_divisors_dvd_det` | Arbitrary commutative ring; no nonsingularity assumed. |
| Vanishing rows supply polynomial factors | `polynomial_rows_vanish_pow_dvd_det` | Exponent is the selected row count. |
| Preserve divisor under determinant-one constant row change | `constant_row_transform_pow_dvd_det` | Determinant-one hypothesis is explicit and discharged for the actual Taylor matrix. |
| Actual Taylor matrix and coefficient action | `taylorCoefficientMatrix_det`, `taylorCoefficientMatrix_mul` | Exact determinant and coefficient identities. |
| Low Taylor coefficients vanish | `taylor_coeff_zero_of_root_power` | Actual root-power divisibility, not a Boolean rank flag. |
| Reconstruct and specialize full columns | `finiteColumnPolynomial_eq_specialization` | Explicit outer-degree bounds; W and Z are not interchanged. |
| Fixed-size Sylvester implication | `fixedSylvester_root_power_dvd_det` | Actual shifted F/G columns; leading-degree drops retained. |
| F/F_Z local multiplicity | `fixedDerivativeSylvester_multiplicity_at_nonzero` | Nonzero specialization, not nonzero determinant. |

The new files are `TenthDiscriminant/DeterminantMultiplicity.lean` and `TenthDiscriminant/SylvesterLocal.lean`.

## Controls and their limits

The exact reference cases are:

- F=Z^2-W: det S=-4W. A double root supplies one factor, not a universal exponent two. The determinant and its nonzero linear coefficient are checked in Lean.
- F=W*Z^3+Z^2+W: det S=4W^2+27W^5. At W=0 the degree falls from three to two; the original 5 by 5 matrix is retained. This example is an exact computational control, not a separate Lean example.
- F=Z^2: det S=0. Lean checks the identically zero determinant; divisibility alone cannot establish a finite contact budget.

Four new matched Lean pairs test Taylor determinant normalization, the sharp local exponent, repeated factors, and translated-root coefficients. Each valid statement must compile; each false statement must reach an arithmetic contradiction, not a parser or type error. The total is now 13 matched mathematical pairs and four proof-audit probes, with all earlier Gram and jet controls retained.

`multiplicity_exact_controls.py` uses exact rational elimination and interpolation with held-out determinant evaluations. Seed 20261022 supplies 48 planted-root cases, including 24 leading-degree drops. **Only 22 cases have m>=2 and therefore require a positive exponent; nine of those also have a degree drop.** The other 26 are boundary controls, not evidence for positive-order multiplicity. Translation, simultaneous row/column reversal, and row-swap sign are checked. Raw polynomial coefficients and orders are printed; zero-polynomial order is represented as null, not zero.

The local standard-library run, optimized `python -O` run and fresh rerun were byte-identical. SymPy 1.14.0 independently implemented the resultant calculation for the three reference formulas and agreed. This is a separate implementation check on same-authored examples, not independent semantic review. Lean ran in GitHub Actions, not the local working container.

## Corrections preserved

Failed draft runs `39786929053`, `39787658391` and `39788690233` remain in history. Repairs made binders, coefficient maps, finite-sum transport, polynomial types and concrete determinant unfolding explicit. Mathematical hypotheses and conclusions were not weakened, and no audit or control was disabled. The last of those runs already compiled the core module but failed the concrete example proofs; the successful run above includes those examples and all controls.

## Remaining obstruction and next gate

For a primitive irreducible mixed factor in characteristic zero, prove that this **same fixed determinant** is nonzero and has W-degree at most (2a-1)b. Then combine distinct-root multiplicities and the irreducible-factor budget, and connect the resulting point-count criterion to the existing jet kernel. The local theorem does not supply any of these conclusions by assumption.

Kill a proposed global promotion if a repeated factor is treated as having nonzero resultant, if a degree drop silently changes the matrix, if a necessary coprimality/characteristic-zero premise is omitted, or if a qualifying exact counterexample is found. Stop at the nonzero/degree bridge before claiming the complete jet-uniqueness criterion.

The number-field, integrality and prime-adic divisibility, analytic, numerical-certificate and finite-classification obligations also remain separate. No theorem here proves h(-D)=1 implies D<=163.

## Integration provenance

PR #6 merged into main at `157650c4b56a9fe0b8402d6f56a903abddd5811f`. PR #7 merged into `formalization/trace-gram-psd` at `4af7c4676df191beffdd7849a4a81e27a8ef28bd`, after PR #6 had already merged. PR #8 targets main and carries both histories without rewriting either. Opening this continuation does not merge it or modify main.
