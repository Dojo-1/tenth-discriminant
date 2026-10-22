# Fixed determinant degree and distinct-contact budget

## Scope

Base main: `791ebf4815d8eb4be5da3b01527ca7f0877b6d0e`. This is a main-targeted, isolated continuation of the original fixed-size Sylvester construction. It does not depend on the unmerged methodology experiments or affine PR #12. No changed discriminant cutoff, no classification theorem, and no novelty claim.

The new source is imported by the root library. Read the workflow for the exact head before calling it checked. Finite Python tests do not substitute for that build or the compiled axiom audit.

## Universal degree bound

For a field K and F in K[W][Z], suppose every Z-coefficient has W-degree at most b. Let E be the determinant of the ACTUAL fixed matrix S(F,F_Z;a,a-1). Then

    natDegree(E) <= (a+(a-1))*b.

For a>=1 this is (2a-1)b. No irreducibility, characteristic-zero, nonzero specialization or nonzero determinant is needed for this degree inequality. In Lean natDegree(0)=0; the statement alone never establishes a finite root budget for zero.

The proof first bounds a polynomial matrix determinant by the sum of per-column degree limits. Every determinant term selects exactly one entry per column. Z-shifts select coefficients without changing their W-degree; Z-differentiation multiplies coefficients by constant integers. The theorem is then instantiated for the existing fixedSylvesterMatrix, not a reconstructed resultant.

## Conditional contact budget

Assume additionally deg_Z F <= a and E != 0. Let s be a finite SET of distinct parameter values w. At each w in s require a nonzero specialization F(Z,w) and an actual divisibility witness

    (Z-z(w))^m(w) divides F(Z,w).

The existing local multiplicity theorem supplies (W-w)^(m(w)-1) | E. Counting multiplicities at distinct roots gives

    sum_{w in s} (m(w)-1) <= natDegree(E) <= (a+(a-1))*b.

With a>=1, b>0 and m(w)>b at every selected point, this proves

    |s| <= 2a-1.

These are exact implications. The nonzero determinant hypothesis remains an upstream obligation. In particular, this does NOT yet prove that the determinant of an intended primitive irreducible mixed factor is nonzero. Factorization of an arbitrary invisible polynomial and global jet uniqueness also remain open in Lean.

## Declaration map

- `polynomialMatrix_det_natDegree_le_columns`: per-column degree bound.
- `polynomialMatrix_det_natDegree_le`: uniform bound, including empty/singular matrices.
- `shifted_coefficient_natDegree_le`, `derivative_coefficient_natDegree_le`: coefficient bookkeeping.
- `fixedDerivativeSylvester_natDegree_le_positive`: actual (2a-1)b bound.
- `polynomial_distinct_root_power_budget`: multiplicity count for a nonzero polynomial.
- `fixedDerivativeSylvester_contact_sum`: existing local theorem assembled with degree spending.
- `fixedDerivativeSylvester_excessive_contact_card`: at most 2a-1 excessive contacts under the named premises.

## Counterexamples and conventions

1. F=W(Z^2+Z+1) gives E=3W^3. For a=2,b=1, a universal (2a-2)b replacement is false. This example is not irreducible; no sharpness claim is made for a narrower irreducible class.
2. F=Z^2 gives E=0. Arbitrarily many distinct parameters have a double root, invalidating a finite contact budget after removing E!=0.
3. F=W(Z+1) has E=W but the specialization at W=0 is zero. Assigning it arbitrary finite multiplicity is invalid.
4. F=Z-1 with b=0 has arbitrarily many ordinary root contacts. The excessive-contact cardinality cancellation requires b>0.
5. Five copies of W=0 for F=Z^2-W are one parameter, not five distinct roots.

Four matched Lean true/false pairs and a universal single-root instantiation run through `degree_negative_controls.py`, invoked by the existing negative-control driver. Rejection by syntax/type/resource errors is not accepted as mathematical discrimination.

## Finite exact campaign

`research/degree_budget_r1/check_degree_budget.py` compares 60 general polynomial matrices, 48 bivariate cases, 144 hash-pinned production evaluations, 144 overpadding checks and 24 planted-contact families. Five explicit mutations are rejected. Rational-root contact enumeration is a bounded check, not enumeration of all complex roots. There are 15 zero general determinants; the 48 plus 24 bivariate families have nonzero determinants. Exact normal/optimized runs agree. The production helper is verified as blob `0c4ccb8f2dab99a5317f80345eae7920390fcbc0` before execution.

The protocol was frozen before this finite campaign, but after source review and the first formal draft; it is not a blind preregistration. Subsequent changes strengthened negative-test checks without changing the corpus or recorded mathematical outcomes. Python and Lean tests share authorship; the proof kernel and symbolic algebra are distinct instruments, not independent semantic reviewers.

The SymPy campaign is manual, not part of the existing Lean-only CI:

```sh
python research/degree_budget_r1/check_degree_budget.py --source lean/multiplicity_exact_controls.py --output /tmp/degree-budget.json
cd lean
lake update
lake exe cache get
python3 verify_sources.py
lake build
python3 audit.py
python3 negative_controls.py
```

## Review correction and next obligation

The initial affine draft in this branch was removed when live review found stronger PR #12 already green at `34f41c9`. Its full affine basis identity is constructed, not assumed. History preserves that superseded draft and the two natural-cast failures in this degree proof. No theorem statement was weakened to fix compilation.

Next bounded obligation: prove nonzero determinant for the SAME fixed matrix from exact global degree and derivative coprimality over K(W); then instantiate primitive irreducibility in characteristic zero. Do not replace that work with a structure field assuming nonvanishing. Only after that bridge and factor accounting should the global jet-uniqueness claim be promoted.
