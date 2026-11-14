# Phase317 · the fibre, the lift, and the direction that did not count

> Not every changed matrix is a changed invariant.
>
> The norm-164 obstruction remained genuine. Its first two Smith digits did not move. We followed that failure down to the radical itself.

Stacked DRAFT research on the consolidated Phase312 branch; no main merge, no altered tenth-discriminant theorem, no change to the reported bound \(322^4\). Three timestamped research protocols were frozen before the corresponding work: PRE_REGISTERED_FIBRE_SMITH.md, PRE_REGISTERED_RADICAL_TANGENT.md and PRE_REGISTERED_EXPLICIT_CONGRUENCE.md.

## First nonrational norm fibre: exact, classical, not enough

For \(D=4m-1>3\) and the ORIGINAL integer suborder \(\mathbb Z[\sqrt{-D}]\),

\[
N(x+y\sqrt{-D})=x^2+Dy^2,\qquad N=D+1=4m.
\]

Exactly four nonrational elements occur, \((x,y)=(\pm1,\pm1)\). If and only if \(m\) is square there are also the two rational generators \((\pm 2\sqrt m,0)\). Hence there are exactly \(4+2\,\mathbf 1_{\{m\text{ square}\}}\) integer solutions and \(2+\mathbf 1_{\{m\text{ square}\}}\) signed generator classes.

Class number one in the FUNDAMENTAL maximal order implies \(m\) is prime by the small norm obstruction: a proper prime factor \(p\mid m\) gives an ideal of norm \(p<m\) from the residue map \(\omega\mapsto0\pmod p\); principalization would yield an element of norm \(p\), whereas the norm-gap lemma forces a rational-square norm. This is classical. The prior Phase316 Lean theorem proves only the norm-gap inequality; no Lean class-group-to-ideal bridge is claimed in Phase317.

The independent reduced-form control suite checks h1 \(D=7,11,19,43,67,163\) (all four), but crucially h2 \(D=187\), with \(m=47\) prime, ALSO has four. Class-number-two \(D=35\), \(m=9\) square, has six; class-number-four \(D=203\), \(m=51\) composite nonsquare, still has four. Fibre size **cannot** classify class number.

Narrow Lean module Phase317NormFibre proves, without h1 hypotheses, that every nonrational element of original norm \(D+1\) has \(x^2=y^2=1\), checks all four explicit points, and constructs the two extra rational points when \(m\) is square. The last two implications are not a formalized class-number-one classification.

## From changed entries to actual 5-adic information

Freeze the SAME native D163 ORIGINAL integer-order source: \(Q_{109}\), \(R=40\), \(S=J=1\), fifteen exact Frobenius25 /5 row divisions. Phase316's conjugation-covariant norm-preserving SYNTHETIC conductor125 ray shifts \(k\cdot t\), where \(t=(20,10)\pmod{25}\) and \(k=0,\dots,4\), differ only on the two signed norm-164 generator tags.

At \(k\ne0\), all **363** of the affected primitive Gram cells change modulo25; not a single entry changes modulo5. The independent exact first TWO Smith layers of all five resulting 40x40 matrices over \(\mathbb Z/25\) agree:

\[
\boxed{(e_0,e_1,e_{\ge2})=(23,\ 7,\ 10).}
\]

Here \(e_0\) counts unit Smith factors, \(e_1\) counts factors divisible by exactly one 5, and \(e_{\ge2}\) counts factors divisible by25. The first two digits do NOT determine the full determinant valuation \(v_5(\det G)\). A separate unimodular pivot/Schur calculation and hostile row-column shears check the counts.

## The 17-dimensional radical knows exactly what changed

Put \(G_0=G\bmod5\) and \(R=\ker G_0\), so \(\dim_{\mathbb F_5}R=17\). Let \(K\in\operatorname{Mat}_{40\times17}(\mathbb F_5)\) be a basis lifted to integer coordinates. Define the FIRST radical-lift bilinear form

\[
B_G=\frac{K^\mathsf{T}GK}{5}\pmod5.
\]

Its rank is exactly \(e_1=7\), independently of the Smith elimination. Every synthetic gauge yields the same \(B_G\) entry by entry. Its difference \(H=(G_k-G)/5\bmod5\) has

\[
K^\mathsf{T} H K=0.
\]

This is the complete first-order obstruction to lying in the tangent space of the congruence orbit. Over characteristic different from2, for symmetric \(G_0,H\),

\[
H=XG_0+G_0X^\mathsf{T}\ \text{for some }X
\quad\Longleftrightarrow\quad
H|_{R\times R}=0.
\]

The necessity follows from \(G_0R=0\). For sufficiency split the carrier into a nondegenerate complement and radical, \(G_0=\operatorname{diag}(A,0)\), and solve the upper-left and off-diagonal blocks using \(A^{-1}\) and \(2^{-1}\). This is elementary congruence-orbit linear algebra, not a novel global number-field theorem.

In Phase317-D, a constructive test attempts something STRICTER than tangent membership: recover each original-coordinate \(X_k\), form an exact invertible \(U_k=I+5X_k\) modulo25, and verify every cell of

\[
\boxed{G_k=U_k G U_k^\mathsf{T}\pmod{25}.}
\]

The stronger step **has now passed**: focused hosted run 43590228744, with **20 adversarial tests**, constructs all five exact matrices \(U_k\), checks their inverses \(I-5X_k\), and verifies EVERY ONE of the 1,600 matrix entries for each gauge. The synthetic and actual matrices are **congruent bilinear forms over \(\mathbb Z/25\)**, despite the 363 changed coordinate entries for nonzero shifts. The \(X_k\) coefficients are linear in \(k\) modulo5. This is ONLY a modulus25 congruence; it does NOT imply their full integral Gram determinants or deeper 5-adic Smith profiles coincide.

~~~mermaid
flowchart TD
  E["Native original D163 primitive Gram<br/>mod25; rank mod5 =23"] --> R["17-dimensional mod5 radical"]
  E --> T["Synthetic norm164 wild gauges k=0..4"]
  T --> D["363 cells change modulo25<br/>none change modulo5"]
  R --> B["First radical-lift form B<br/>rank7"]
  D --> B
  B --> H["Gauge difference vanishes on R × R"]
  H --> X["Tangent congruence XG0+G0Xᵀ"]
  X --> U["Explicit U=I+5X mod25<br/>verify whole 40x40 equality"]
  U -. "does not prove deeper Smith or new cutoff" .-> O["Uniform h1 residual theorem still OPEN"]
~~~

## What survived: a much narrower theorem target

The data now rejects not only the naive source-selection convolution and the claim that 363 changed cells imply a new valuation. It also shows that the tested trace-zero synthetic ray gauges lie in the **tangent null directions** of the first radical-lift invariant.

To improve the tenth-discriminant bound, a true h1-specific norm-constrained ray-realizability condition would need to force the actual first radical-lift \(B_G\) onto a stricter **determinantal degeneracy locus**, or establish higher-digit Smith constraints beyond this congruence. It must survive the D187 h2 and D183 h8 controls, be uniform in the native large-field \(R,S,J\), and contribute beyond the previously counted valuationWeight. That remains unproved.

Evidence hierarchy: [P-paper] exact norm-fibre and tangent linear algebra identities; [P-narrow Lean] only the nonrational norm-fibre equation on its successful CI; [M] finite native source and five synthetic gauge checks at exact green heads; [H] uniform field gain; [R] four-fibre class-one detector, Gram entry change => valuation gain, or tangent versus matrix equivalence without actual congruence verification. The synthetic tags are NOT new quadratic fields, and no human mathematical referee has validated this research.
