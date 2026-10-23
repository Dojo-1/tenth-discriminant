# Irreducibility, fixed Sylvester nonvanishing, and contact budgets

This is an algebraic component, not a new discriminant cutoff or a full
jet-uniqueness/class-number theorem. Read the exact source head's completed
Lean workflow before assigning proof status. Finite Python checks and source
text do not establish successful Lean verification.

## Objects and statements

Let K be a field, F in K[W][Z], and a>=1 its EXACT global Z-degree. E is the
repository's original determinant `det (fixedSylvesterMatrix F F.derivative a (a-1))`.
The size a+(a-1) remains fixed under specialization.

1. An injective coefficient map into a field, with coprime images of F and its
   ordinary Z derivative, implies E is a nonzero polynomial in W.
2. In characteristic zero, irreducibility of F supplies this coprimality over
   the fraction field of K[W]. Positive Z-degree irreducibility also implies
   primitivity, so primitivity is not an extra public hypothesis.
3. Primitivity implies F(Z,w) is not the ZERO POLYNOMIAL for every w in K.
   This assertion does not require characteristic zero.
4. Combining the same E with the degree and local multiplicity results of
   PR #13: if every Z-coefficient has W-degree <= b, then for a finite SET s
   of parameter values and actual root-power divisors at z(w),

       sum_(w in s) max(m(w)-1,0) <= (2a-1)*b.

   If b>0 and m(w)>b at every selected w, then card(s)<=2a-1.
   The new public contact results do NOT assume E!=0 or nonzero fibers.

A field of characteristic zero is a genuine hypothesis for the irreducibility
argument. It is not silently replaced by a finite-field test. Irreducibility
must hold over the stated coefficient field, not merely a smaller base field.

## Coefficient-kernel proof, without a substitute resultant

The coefficient matrix of the map (A,B) -> A*F+B*G uses m shifts of F and n
shifts of G, with deg F=n and deg G<=m. Its input coefficient windows have
lengths m and n. A zero matrix image reconstructs the ZERO polynomial syzygy.
Coprimality forces F|B, the strict coefficient window forces B=0, then A=0.
The matrix is square over a field, so this injectivity yields det!=0.

`fixedSylvesterMatrix_map_to_field` identifies this field matrix entry by entry
with the mapped EXISTING fixed matrix, including the explicit finite-index
permutation. Its determinant is not an assumed resultant and its nonsingularity
is not a premise. A zero determinant over K[W] would map to zero, contradicting
the proved field determinant result.

Gauss's lemma transports primitive irreducibility to K(W)[Z]. Characteristic-zero
separability supplies derivative coprimality. The normalized-GCD structure needed
by the pinned library is constructed from its existing unique-factorization
instance using classical choice; no new axiom or assumed algebraic structure is
added to the public statement.

If F(Z,w) were the zero polynomial, W-w would divide every coefficient of F.
That would be a nonunit common coefficient factor, contradicting primitivity.

## Declaration map

- `NonzeroBridge.kernel_syzygy`: actual kernel-to-polynomial correspondence.
- `NonzeroBridge.coeffMatrix_kernel_eq_zero`, `coeffMatrix_det_ne_zero`:
  coprimality and exact degree eliminate the kernel over a field.
- `fixedSylvesterMatrix_map_to_field`: exact reindexing/transport correspondence.
- `fixedSylvester_det_ne_zero_of_coprime_map` and derivative corollary:
  reflection from the field image to the original polynomial matrix.
- `irreducible_positive_isPrimitive`: derived primitivity.
- `fixedDerivativeSylvester_ne_zero_of_irreducible`: public nonzero theorem.
- `primitive_specialization_ne_zero`, `irreducible_positive_specialization_ne_zero`:
  no zero fibers (NOT no roots of the determinant).
- `irreducible_fixedDerivativeSylvester_contact_sum`,
  `irreducible_fixedDerivativeSylvester_excessive_contact_card`:
  actual assembly with the degree/contact budget and discharged nonzero premises.

## Counterexamples retained

- F=Z^2-W has E=-4W. Nonzero polynomial does not mean nonzero at every W.
- Padding that matrix from exact degree 2 to degree bound 3 makes its determinant
  identically zero. Exact global degree is not an optional nonvanishing premise.
- F=(Z-W)^2 has zero derivative resultant. Coprimality matters.
- F=W(Z+1) has E=W but a zero fiber at W=0. Nonzero E alone does not prove primitivity.
- F=WZ+1 specializes to 1 at W=0: leading-degree loss is not a zero fiber.
- In characteristic three F=Z^3-W has zero Z derivative. The characteristic-zero
  hypothesis cannot simply be deleted from the irreducible argument.
- Degree-zero irreducible factors, e.g. W, are outside the positive-Z-degree rule.

## Integration and checks

Frozen main: 5bde735a86c93b938574128583b3396d07101093.
This draft branch preserves PR #13 head 96967b50d6479ff7e6eebc0847813ebfcfb5d4eb
as an additional parent. Its seven new files are incorporated unchanged. Root
imports retain the newer main modules and add the degree/contact/nonzero modules.
The control driver retains all existing checks, plus the upstream degree checks
and new nonzero checks. This is branch integration, not a merge into main.

The initial tactic-bullet, explicit-map/degree-argument, and coefficient-support
failures are preserved in history. Repairs did not weaken theorem statements.
A canceled intermediate workflow is not reported as an overall successful run,
even when its listed proof steps succeeded. Consult PR #14 for exact final gates.

Six matched Lean true/false pairs and three universal public API instantiations
exercise the boundaries. Syntax, type, or resource failures are not accepted as
meaningful negative-test rejection. The compiled axiom audit retains the existing
allowlist: propext, Classical.choice, Quot.sound.

The separately executed exact Python campaign contains 48 field-level pairs
(13 singular), 48 bivariate polynomials (36 reference-irreducible), 144 production
matrix/determinant specializations and 144 overpadding controls. Four identically
zero polynomial determinants remain in the corpus. Empty and degree-zero-unit
matrix boundaries are checked. Normal and optimized JSON results match exactly;
tampered production source is rejected before import. No performance claim.

## Reproduce

From the repository root, with SymPy 1.14.0:

```sh
python research/nonzero_bridge_r1/check_nonzero.py --source lean/multiplicity_exact_controls.py --output /tmp/nonzero-bridge.json
python -O research/nonzero_bridge_r1/check_nonzero.py --source lean/multiplicity_exact_controls.py --output /tmp/nonzero-bridge-optimized.json
cmp /tmp/nonzero-bridge.json /tmp/nonzero-bridge-optimized.json
cd lean
lake update
lake exe cache get
python3 verify_sources.py
lake build
python3 audit.py
python3 negative_controls.py
```

The SymPy campaign is manual; the Lean workflow does not run that campaign.
The source-correspondence check only checks interval endpoints, not Arb inequalities.
Proof selection, case generation and interpretation share authorship. Lean is a
separate checker; the symbolic and rational algorithms are different code paths,
not independent semantic or human review.

## Remaining frontier

No factorization-to-total-jet-uniqueness theorem is asserted. Repeated-factor
multiplicities, parameter-only and Z-only factors, total bidegree accounting,
coverage of the actual conjugate sampling set, and the resulting real Gram
nonvanishing still need assembly. Number-field/inert-prime arithmetic, determinant
integrality/divisibility, analytic estimates, numerical certificates and finite
classification remain separate. Nothing here proves h(-D)=1 implies D<=163.
