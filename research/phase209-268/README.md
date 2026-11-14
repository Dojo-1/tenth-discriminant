# Phase209–268 — divided Frobenius, horizontal transport and the 321⁴ candidate

> One source. One ordinary-jet convention. One original trace Gram.
>
> The horizontal contribution is not a second determinant; it is a second integral frame on the same determinant.

This line contains the original-source geometry and arithmetic behind the stronger (321^4) field-bound candidate. It is now consolidated on a research branch, separate from main and from the Phase269 finite CRT certificate.

## Phase209 — Taylor flow and ordinary-jet depth

- Exact integer Taylor-flow expansion for the ordinary derivation (delta=partial_Z+Z^{p-1}partial_T).
- Sharp depth (E_p(j)=sum_{mge2}lfloor j/p^mfloor).
- Conjugate folding of the original full Gram, with the ordinary (Z)-jet convention and W fixed.
- Exact source and capacity controls; negative controls distinguish the frozen short-jet pilot from the first nonzero depth.

The depth is not a Hasse derivative and must not be substituted by one.

## Phase210–211 — zero-exclusion comparison and rank boundary

- A class-number-free inert-prime budget for the original thin Gram is formalized under explicit inertness hypotheses.
- The separate analytic implication from an exceptional zero to sufficient inert-prime mass remains open.
- The finite column-capacity bound is quantified; on a Green-style large grid, this particular automatic depth contribution is subleading.
- The unchanged-support rank obstruction (RS\le |Q|\min(J,R)) rules out naive high-jet enlargement when the support is fixed and too small.

This is a method comparison, not a zero-free theorem.

## Phase223–228 — horizontal integral frame

- Horizontal support and residue transports.
- Joint jet transport and exact integral moving frame.
- Combined unimodular Frobenius row frame on the original ordinary-jet Gram.
- Exact same-Gram divisibility, with the odd-prime and binary factors accounted once.

The combined frame is not a product of separately truncated row operations. The proof keeps the unitriangular row change separate from the nonunimodular division by p.

## Phase259–268 — enhanced lower, upper and actual-field return

- Phase259: horizontal production floor and finite certificate.
- Phase260–262: enhanced original-Gram divisor and logarithmic bridge.
- Phase263: enhanced lower bound on the original thin Gram.
- Phase264–266: analytic upper and strict scalar separation.
- Phase267: actual totally-complex degree-two field theorem, with odd/even maximal-order chart.
- Phase268: class-number-free finite inert-prime budget at the 321⁴ source floor.

The formal declaration is
[
|\operatorname{disc}(K)|<321^4=10,617,447,681
]
for totally complex degree-two number fields of class number one, relative to the encoded definitions and standard Lean axioms.

The proof-changing head on the original PR #157 passed focused and whole-root Lean CI on 10 November. The candidate remains subject to independent semantic reconstruction in issues #50 and #51. A new exact-head replay is required on this consolidated research branch.

## Relation to the other research lines

- Phase269–270 is a separate finite CRT certificate at the accepted 322⁴ endpoint.
- Phase277–303 studies primitive pairing, Noether/Smith walls, Hermite/Frobenius and maximal-order source completion.
- Phase306–319 studies wild-ray arithmetic and D163 local/global norm-fibre realization.
- Phase320 compares D163/D187/D203 and has now passed its full exact-head finite-source gates.
- Phase321 constructs the full ideal-aware ray groups for class numbers 1, 2 and 4.

No result from this line is promoted to main by this consolidation. The (321^4) statement is a stronger candidate than the accepted (322^4) endpoint, but its independent human mathematical review remains open.

## Reproduction and evidence

The exact-head workflow runs the Phase209 source oracles, the rational 321 margin, the Taylor-flow precision tests, the focused Lean modules and the whole-root Lean proof checks.

- **P:** formal declarations and exact algebraic identities relative to their encoded definitions.
- **M:** finite source and arithmetic controls.
- **H:** independent human reconstruction of the source-to-field semantics; any general exceptional-zero/zero-free bridge.
- **R:** changing the original source, double-counting vertical and horizontal divisibility, substituting Hasse derivatives, or treating the class-one inertness hypothesis as valid for arbitrary real characters.

The review issues #50 and #51 remain open. CI is not a substitute for independent mathematical review.
