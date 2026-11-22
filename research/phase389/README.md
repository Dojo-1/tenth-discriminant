# Phase389 — Formal cubic translation and quadratic source shifts

**22 November 2026 · Research draft, stacked on Phase388.**

## Exact theorem boundary

The new Lean module lean/TenthDiscriminant/Phase389CubicTranslation.lean contains a characteristic-3 cubic identity formulated for an arbitrary commutative ring A with the explicit assumption (3:A)=0:

\[
g(q)=a_0+a_1q+a_2q^2+a_3q^3,\qquad
g'(q)=a_1+2a_2q+3a_3q^2.
\]

It proves

\[
g(q)+g(q-1)+g(q-2)=2a_2,
\quad 2(g'(q-t)-g'(q))=2ta_2
\]

and hence the exact three-point translation law. A quartic counterexample in ZMod 3 rejects unqualified promotion to degree four (the S=5,k=4 failure).

The same module also proves exact integer division identities for the literal quadratic-source quotient coordinates

\[
Q_{\rm re}(D,x,y)=(x^3-3Dxy^2-x)/3,\quad
Q_{\rm im}(D,x,y)=(3x^2y-Dy^3+y)/3
\]

under the source shift x→x+3t, and their reductions modulo 3:
Qre→Qre−t, Qim→Qim.

For the original inert quadratic source D≡1 mod3, the underlying Frobenius source theorem guarantees that both component numerators are divisible by 3. The new coordinate-shift statements as integer division equations do not themselves assert that divisibility outside the inert domain.

## The crucial missing interface

This module does **not** formalize the statement that the abstract polynomial g' is the original source-normalized THIRD ordinary Z derivative divided by two. That requires a derivation with W held fixed and delta Z=1, delta W=0, delta q=Z², then delta³=2 partial_q in characteristic 3 for the particular polynomial frame

\[
P_{r,s}(Z,W)=Z^{r-3k}W^s(Z^3-W)^k,\qquad k\le3.
\]

Its connection to the original row-major matrix, signed source coordinates and 219 actual ellipse points is a separate proof obligation. Phase388's rank90 and nine sparse fourth-jet subspace certificate remain finite computational results plus paper arguments until a Lean theorem supplies that source intertwining.

## Independent controls and negative cases

The Python standard-library script research/phase389/finite_controls.py checks the source coordinate shift on six inert parameters D=7,19,43,283,403,412 and 6,750 source point/shift combinations; the cubic law is independently evaluated in F9, including coefficients outside the embedded F3. The quartic-degree and non-inert (D=2) source-integrality failures are explicit countercontrols.

The focused GitHub workflow compiles the Lean file under the repository-pinned Lean 4.19.0 and Mathlib commit c44e0c8, then runs the Python controls. The inherited full root audit imports the new module and reruns whole-root checks. Do not report compile success before exact-head CI shows it.

## Evidence and claims

- P (conditional on successful kernel compilation): characteristic-three cubic translation, quartic counterexample and literal integer-source quotient shift statements, with exact source hypotheses.
- M: finite test results, once exact-head controls pass; not a proof of uniform number-field bounds.
- A: existing source Frobenius/ordinary-jet semantics, needed to apply the abstract identity.
- H: exact Lean transport from cubic formal derivative to original normalized ordinary source jets; nine sparse rows; full rank90; source-to-actual-field reviewer issue #50.
- R: treating cubic derivative as automatically the original Z third derivative, additive p-adic Smith valuation or a new unconditional tenth-discriminant endpoint.

No merges. No change to separately scoped Masullo/Hecke, Discriminant–Conductor–Zero or Selberg–Ihara research.
