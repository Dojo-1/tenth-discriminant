# Factor assembly, jet separation, and the actual trace-Gram matrix

## Exact scope

Let P be a finite set of distinct complex points. Let R,S be positive integers, J >= S, and let the monomial row labels (r_i,s_i) be distinct with r_i<R and s_i<S. If

`2*(R-1)+(S-1) < P.card`,

then the repository's existing `traceGramMatrix P J rows` is positive definite and has strictly positive determinant. This is a sufficient criterion; it is not asserted necessary, sharp, novel, or a new discriminant bound. No lattice, symmetry, origin-exclusion, Gram-positivity, jet-injectivity, or nonzero-resultant hypothesis is assumed by the public point-count theorem.

The ordinary Z derivatives hold W fixed. Complex jet uniqueness is sufficient for the real trace-Gram conclusion; real and complex linear independence are not identified.

## A multiplicative exceptional set

For a nonzero F in K[W][Z], a characteristic-zero field K, an injective map z:K->K, and a finite parameter set s, define B(F) to contain w in s when either F(Z,w) is the zero polynomial, or its root multiplicity at z(w) exceeds deg_W F.

1. `B(F*G) subset B(F) union B(G)` for nonzero factors. Nonzero fibers use multiplicity additivity and exact W-degree additivity; zero fibers are retained explicitly.
2. Parameter-only factors are bounded by their W-root count. Z-only factors are bounded by their Z-root count using injectivity of z.
3. Mixed irreducible factors invoke the checked irreducible-contact bound. Their nonzero determinant and nonzero fibers are derived by the inherited proofs, not postulated.
4. Factor induction, retaining repeated factors, gives `card B(F) <= 2*deg_Z F+deg_W F`.
5. Vanishing jets of orders below J, with J>deg_W F, place every selected sample in B(F). More than the budget forces F=0.
6. Conjugation is injective, so the graph w=conj(z) satisfies the general sampling contract.
7. The actual monomial row polynomial specializes exactly to the existing `rowSection`. Distinct labels recover each coefficient. Existing `realJet` and kernel/energy theorems then yield positive definiteness of the same matrix.

No squarefree replacement is made. No multiplicity of the zero polynomial is used as a finite order.

## Declaration map

- `BivariateDegree.lean`: exact variable-exchange ring homomorphism, involution, transposed coefficients, W-degree, degree additivity and coefficient-degree correspondence.
- `FactorJetBudget.lean`: explicit zero-fiber/contact exceptional set, pure-factor bounds, product cover, irreducible-factor induction, and `polynomial_eq_zero_of_jet_count` over any characteristic-zero field.
- `JetCountGram.lean`: conjugate sampling, actual row-polynomial specialization and coefficient recovery, `traceGramMatrix_posDef_of_point_count`, and `traceGramMatrix_det_pos_of_point_count`.

All modules are imported by the library root. The proof revision `3b57cb6` passed workflow 39860662159 (job 120110211065): build, transitive axiom audit and inherited controls. Later commits add targeted controls and evidence; consult the final-head workflow and PR #15 for their exact verification status.

## Controls and correspondence

`assembly_negative_controls.py` includes three universal public API instantiations (general polynomial jets, actual Gram positivity, and Ender's stronger 3R+S count guard) and eight matched true/false mathematical controls. It is called by the existing negative-control driver along with all inherited tests and the affine checks from current main. A malformed or ill-typed negative example does not count as a mathematical rejection.

The finite comparator in `research/jet_assembly_r1/` independently computes multiplicities by polynomial division and compares them with symbolic ordinary derivatives. It also compares the hash-pinned pure production Gram functions with symbolic differentiation. It does not execute the full Arb/PARI verifier entrypoint and does not establish universal Python-Lean equivalence. Thirty-eight distinct polynomials occur among the 48 base cases; this is a fixed same-author control campaign, not a held-out generalization study. All raw outputs are retained in the conversation evidence bundle.

The characteristic-three control uses F_27 and F=Z^3-W. Eight distinct pairs (z,z^3), J=2, violate a false characteristic-free version of the bound 2*3+1=7. Circle powers protect the derivative-depth condition. Duplicate rows/samples, noninjective first coordinates, pure factors, zero fibers and repeated multiplicities remain visible.

## Reproduce

From `lean/`, with the pinned Lean/Mathlib dependencies:

```bash
lake build
lake env lean Audit.lean
python negative_controls.py
```

From the repository root, with SymPy 1.14.0:

```bash
python research/jet_assembly_r1/check_assembly.py --source tools/verify_exact.py --output /tmp/jet-assembly.json
python -O research/jet_assembly_r1/check_assembly.py --source tools/verify_exact.py --output /tmp/jet-assembly-optimized.json
cmp /tmp/jet-assembly.json /tmp/jet-assembly-optimized.json
```

The source hash gate rejects drift before executing the selected production functions. Keep fresh outputs separate from saved evidence.

## Integration and remaining boundary

The new branch retains PR #14 and current main 5f43c18 as parents, combining the already-proved contact/nonvanishing chain with affine transport. No previous proof bodies, numerical certificates, production guards, or cutoff claims are modified. No main merge is performed. Early failed drafts remain in history; fixes concern elaboration, finite-set decidability and pinned APIs, not weakened assumptions.

The abstract interpolation/nonvanishing criterion is closed. The concrete ellipse sampling set, its distinctness/cardinality bounds, integer Gram correspondence, prime-adic divisibility, remaining analytic estimates, numerical certification and finite classification still require their own connected proofs. The new theorem alone is not the class-number theorem.

Shared authorship remains. The Lean kernel checks formal proofs; separate exact calculations are implementation checks, not independent semantic peer review. The identity perspective motivates the separation question but is not an additional proof premise or authority.
