# Phase314 — wild second jets, a smaller research surface

> A worldlet is only useful when it carries something across a boundary.  
> Here the boundary is exact: **global ray convolution → truncated wild algebra → ORIGINAL integer-order Gram**.
>
> The part that disappears is as important as the part that survives.

Phase314 is a stacked **draft** research branch on Phase313. All original rows, actual norm balls, ordinary held-W derivatives, exact source divisions, inherited valuationWeight and the reported \(322^4\) cutoff remain unchanged. Before-code protocol: PRE_REGISTERED_JET_QUOTIENT.md.

## The six-dimensional wild lens

At inert \(p=5\), the normalized conjugate Fermat quotient gives additive wild coordinates \(w=(x,y)\in(\mathbb F_5)^2\), for each signed tame ray class. The original primitive evaluations modulo5 have the form

\[
E_i(c,w,j)=a_i(c,j)+b_i(c,j)x+d_i(c,j)y.
\]

Conjugate trace pairing is quadratic in the same coordinates:

\[
G_{ik,c}(x,y)=A_{ik}+B_{ik}x+C_{ik}y+
D_{ik}x^2+E_{ik}xy+F_{ik}y^2.
\]

The wild group algebra is \(\mathbb F_5[C_5^2]\cong\mathbb F_5[U,V]/(U^5,V^5)\), where \(U=g_{(1,0)}-1\), \(V=g_{(0,1)}-1\). The third augmentation ideal power \(J^3\) is annihilated by EVERY quadratic pairing. The Gram reads only the **six-dimensional quotient** \(A/J^3\), with grades \(1,2,3\).

For each signed tame class, its original 25 wild class counts need only the **six raw moments**

\[
\bigl(\sum n,\ \sum nx,\ \sum ny,\ \sum nx^2,\
\sum nxy,\ \sum ny^2\bigr)\pmod5.
\]

There are 12 signed tame classes, so 300 raw ray classes compress to **72 second moments**. The 25 first-nonunit lifts (which must remain separate from the ray units) likewise contribute through six moments. Thus **78** is a sufficient original-primitive-Gram feature capacity, not a proof of a minimal 78-dimensional image.

~~~mermaid
flowchart TD
    A["Signed conductor25 unit spectrum<br/>12 tame × 25 wild = 300"] --> B["Wild 2-jet quotient<br/>12 × 6 = 72 F5 moments"]
    N["25 first-nonunit-lift classes"] --> C["6 nonunit moments"]
    B --> G["SAME original primitive Gram mod5"]
    C --> G
    G -. "not a full 5-adic determinant theorem" .-> GAP["Higher lifts / extra global residual: OPEN"]
~~~

The source code does not infer these formulas from the observed ray distribution. It directly computes **all 300** signed original unit Gram coefficient matrices and **all 25** first-nonunit matrices for D203 and h1 D163, fits quadratic coefficients from six basis values, checks all OTHER 19 wild values, and attacks every third coordinate finite difference at all 25 starts and each of the four symmetric triples. A nonzero second difference demonstrates why a first-order quotient would discard necessary information.

An explicit pair of distinct **nonnegative formal** ray-count vectors, \((3,3,3,3)\) and \((2,6,0,4)\), have the same first two moments and therefore the same original mod5 Gram. They are NOT claimed to be actual class-number-one ideal distributions.

## Keep h1 multiplication coherent

The real global object for h1 D163 is the full **conductor50** ray spectrum, whose signed local unit group is \(C_3\times C_{12}\times C_5^2\). Reduction modulo \(J^3\) now gives a **216-coordinate algebra**, not only a vector-space compressor. Multiplication closes in the same six moments:

\[
\begin{aligned}
M_{0}(AB)&=A_0B_0,\\
M_{x}(AB)&=A_xB_0+A_0B_x,\\
M_{y}(AB)&=A_yB_0+A_0B_y,\\
M_{xx}(AB)&=A_{xx}B_0+2A_xB_x+A_0B_{xx},\\
M_{xy}(AB)&=A_{xy}B_0+A_xB_y+A_yB_x+A_0B_{xy},\\
M_{yy}(AB)&=A_{yy}B_0+2A_yB_y+A_0B_{yy}.
\end{aligned}
\]

The separate conductor2 and signed tame classes multiply in their own finite groups. The implementation compares this moment product against every actual full conductor50 class-one coprime norm-shell convolution at native radius21. **Only after multiplication** is the conductor2 residue-1 gate applied to odd norms; even norms and 5-divisible observations have their own typed input strata. The resulting 72+6 selected moments are checked against the SAME original D163 40×40 integer-order primitive Gram, not an omega maximal-order replacement.

~~~mermaid
flowchart TD
  H["h1 maximal-order norm shells"] --> R["Conductor50: 900 signed classes"]
  R -->|"wild J³ quotient is an ALGEBRA"| Q["216 moment coordinates"]
  Q -->|"convolve shells first"| P["mod2 original-order selector"]
  P -->|"odd norm: F4 residue 1"| C["72 original-order unit moments"]
  E["Even norm prime-to5: 2-divisible stratum"] --> C
  N["5-divisible observations: z/5 first lift"] --> O["6 nonunit moments"]
  C --> G["SAME original integer-order primitive Gram mod5"]
  O --> G
~~~

## Do not make convolution into a rank theorem

The abstract counterexperiment uses formal shells with labels \(n=1,9,49,441\). Their zeroth ideal masses match the actual D163 total counts in those four shells. Two different wild ray assignments preserve the correct tame and conductor2 parts and **all coprime convolution relations internal to those four formal shells**, but yield different quadratic moments and different Gram contributions. The altered wild assignment violates actual field-generator arithmetic. This is NOT a counterexample to the full class-number-one problem. It only demonstrates that **total counts and convolution equations alone** cannot determine the wild moment data.

Previous counterworlds remain binding: D163 h1 and D183 h8 share the entire exact original Q109 Smith spectrum and original valuation77 under matched R40. Any future h1-specific extra valuation must involve an arithmetic constraint that survives both that control and the old valuationWeight subtraction.

## Evidence and research frontier

- **[P-paper]** affine source evaluation implies quadratic Gram, annihilation of wild \(J^3\), closed moment algebra, and conditional h1 ideal-shell convolution. The elementary truncated group-algebra fact is established literature, not claimed new; see [elementary abelian group algebra](https://doi.org/10.1016/j.jalgebra.2016.06.002).
- **[M only after exact-head CI]** full 300+25 coefficient checks, 10,000 original D203 and 1,600 original h1 D163 Gram entries, third finite differences, 216-jet conductor50 convolution and original order gate.
- **[H]** a uniform class-number-one-only higher-lift congruence that forces a non-overlapping residual valuation of the SAME native large-field integer-order Gram.
- **[R]** wild information beyond degree2 affects the current primitive mod5 Gram, or selected suborder norm-shell counts convolve directly.

Narrow Lean file Phase314WildSecondJet checks two-variable third differences and atomic six-moment convolution. It does **not** formalize the class group, 900 signed ray classes, or determinant. Source files and hostile tests are under this directory. No main merge, no improved tenth-discriminant cutoff and no external mathematical peer review claimed.


## Held-out F: 60-radius genuinely nontrivial ideal tests

The frozen native radius21 conductor50 check contained only four nonzero nonidentity coprime products, despite 270 eligible formal pairs. Phase314-F therefore preregistered a HELD-OUT radius60 test BEFORE execution, without replacing the native original Gram or changing any field theorem parameter.

At radius60 the full maximal-order h1 ray spectra have 900 signed classes and their **216-moment wild second-jet** quotient preserves **230** genuine nonidentity products in D43 and **59** in D163. For each field, all **1440** positive norm shells coprime to10 up to3600 match independently computed Dedekind zeta ideal-count coefficients. Full ray product and compressed moment product agree on all these positive pair cases; tests also count nonzero distribution and moment coefficients, not just pass/fail booleans. See heldout_global_ray.py and the earlier-frozen PRE_REGISTERED_HELDOUT_RADIUS60.md.

The negative control is D187, with class number2 by classical reduced positive definite forms, 2 and5 inert just like D43/D163, and the SAME ABSTRACT local ray50 unit group C3×C12×C5². The maximal-order element sqrt(-187)=2omega-1 has norm187=11×17, yet neither 11 nor17 is an element norm (both less than (D+1)/4=47 and nonsquares); the principal norm11 and norm17 distributions are zero while the principal norm187 distribution is nonzero. Full principal-only ray convolution therefore fails on a genuine coprime product due to nonprincipal ideal-class cancellation.

~~~mermaid
flowchart TD
  K["Same local quadratic completions at 2 and 5"] --> W["Same ABSTRACT 900-class local ray-unit structure"]
  W --> A["h1 D43: 230 genuine coprime products"]
  W --> B["h1 D163: 59 genuine coprime products"]
  W --> X["h2 D187: principal-only 11 ×17 fails at 187"]
  A --> T["Full 900 ray products = truncated 216-moment products"]
  B --> T
  T -. "does NOT force a Gram rank defect" .-> H["Uniform h1 residual valuation: OPEN"]
~~~

This is substantial evidence for the arithmetic *interface* and for the global/nonlocal distinction, not a claim of a new discriminant bound. Held-out radius60 is not a native source for the analytic comparison. We did NOT transport its counts into the native integer-order Gram at a different radius.

## Read the information boundary as a theorem target

The image of a **linear map** from at most 78 moments to symmetric matrices can certainly contain full-rank matrices. Therefore "78 features" must NOT be turned into "rank at most78," or a new Gram determinant exponent. The missing class-one input would need to force specific relations among the actual 78 moments under the native source, so that a relevant residual minor vanishes or is 5-divisible. A successful h1 convolution identity does not supply such a relation on its own.

A precise next direction is to compute the symbolic Gram coefficient maps of the six wild moments, identify their **determinantal degeneracy loci** over F5, and then ask whether actual conductor50 h1 principal-shell conditions PLUS a native norm cutoff force those loci. Matched h2 D183 and held-out h2 D187 remain mandatory counterworlds. Deep 5-adic digits are a distinct typed line.

The audit manifest records AI-generated tests, failures/corrections and what the available Lean proofs actually assert. No independent human review and no improved 322^4 claim.
