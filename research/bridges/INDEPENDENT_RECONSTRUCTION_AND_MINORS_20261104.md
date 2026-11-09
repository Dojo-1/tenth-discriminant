# Phase201 — independent reconstruction and a bounded cross-construction test

**4 November 2026 · mathematical review record.** This is a reconstruction by an AI assistant from the checked Lean *definitions and dependencies*, not an independent human referee report. It is not a formal Lean certificate of any new cross-investigator bridge. The 322^4 field theorem was integrated in [PR #126](https://github.com/Dojo-1/tenth-discriminant/pull/126) at [f41ce45b](https://github.com/Dojo-1/tenth-discriminant/commit/f41ce45b9dd7d722faa682d3f1dc1c204fb571da); its full-root exact-head CI passed. The original source-meaning review [#50](https://github.com/Dojo-1/tenth-discriminant/issues/50) remains **OPEN**.

## 1. Reconstruct the theorem before comparing any external construction

For a positive squarefree D congruent to 3 modulo 4, assume class number one of K=Q(sqrt(-D)). Set
- R=floor(D/4), S=floor(R/25), J=S, rho=ceil((11/25)D^(3/4)).
- Q={(x,y) in Z^2 : x^2+D*y^2 <= rho^2}; z=x+i sqrt(D)y.
- The row indexed (r,s), 0<=r<R, 0<=s<S, evaluated at (z,j), 0<=j<J, is **ordinary** d^j/dZ^j (Z^r W^s) with W held fixed and W=conj(z) afterward. No divided-derivative convention is substituted.

Write each jet value a+i sqrt(D)b with a,b integral. Define the **one** integer trace Gram G by
\[
G_{(r,s),(t,u)}=2\sum_{z\in Q}\sum_{j<J}\left(a_{r,s;j,z}a_{t,u;j,z}+D b_{r,s;j,z}b_{t,u;j,z}\right).
\]
This is precisely the integer coordinate convention in [IntegerTraceGram.lean](../../lean/TenthDiscriminant/IntegerTraceGram.lean), with **no claim** that this matrix determinant is the field discriminant.

The checked geometric path proves |Q|>2(R-1)+(S-1) from an ellipse-cell-area estimate, then interpolation implies G positive definite; the larger radius ellipse is used **only for a cardinality upper majorant**, not as a substitute determinant. [SourceGeometry322.lean](../../lean/TenthDiscriminant/SourceGeometry322.lean), [EllipseCellArea.lean](../../lean/TenthDiscriminant/EllipseCellArea.lean), [JetCountGram.lean](../../lean/TenthDiscriminant/JetCountGram.lean) and [ThinUpper322.lean](../../lean/TenthDiscriminant/ThinUpper322.lean) are the source path.

The checked arithmetic path uses class-number-one maximal-order norm arguments to force the relevant small odd primes inert. Original ordinary-jet integral triangular transformations give divisors p^(2F_p) of det G. One separate binary-source divisor is 2^(RS+2S sum_{r<R} floor(r/4)), combined **once** by coprimality. See [BinaryNullTraceGram.lean](../../lean/TenthDiscriminant/BinaryNullTraceGram.lean), [BinaryThinLogBridge.lean](../../lean/TenthDiscriminant/BinaryThinLogBridge.lean), [Phase200PrimeRecovery322.lean](../../lean/TenthDiscriminant/Phase200PrimeRecovery322.lean). The 0.0901 recovery uses original primes 3 and 5, not additional primes.

For \(\gamma=\log\det(G)/(R^2 S)\), source-checked bounds are
\[
0.999997\log D-5.7193+\tfrac14\log2\le\gamma
\le 0.8\log D-0.9265.
\]
They are incompatible whenever D>=322^4. The **certified conservative rational** margin is 2853/500000000; an unrestricted numerical floating-point evaluation is not the proof. [ActualField322.lean](../../lean/TenthDiscriminant/ActualField322.lean) then handles odd/even maximal-order charts and arbitrary totally complex quadratic fields via algebra equivalence to bound the **actual absolute discriminant** strictly below 322^4=10,750,371,856.

This source-derived reconstruction is materially stronger than an inference from CI alone. It is **not** a human referee's independent rederivation of every deep local lemma; source fidelity and novelty remain separate questions in #50.

## 2. External source is a distinct determinant

[twinheterodox v0.7.0](https://github.com/twinheterodox/tenth-discriminant/blob/v0.7.0/versions/v7/proof.tex), §3, chooses R=p0 an **auxiliary inert prime**, S=floor(3R/64), J=ceil(R/9), and evaluates ordinary derivatives at points of a disk in the full maximal-order lattice O_K. The modulo-p0 Frobenius W=Z^p0 rank proof uses 2T<R and J<=p0. It chooses **one nonzero RS-square complex minor M** and defines Delta=|det M|^2. Their much sharper reported q<570 cutoff is numerically not comparable as a proof mechanism to ours. Their v7 review ledger does **not** claim Lean/human verification of v7; a reported external Lean development concerns a *different elementary companion*. Do not silently transfer their parameters, field chart, sampling lattice, prime supply, rank proof or determinant to ours.

## 3. An exact finite negative control for a tempting false inference

Use our **original ordinary-Z-jet convention** with D=3, rho=2, R=S=J=2. The original thin-support definition gives the 11 integer pairs with x^2+3 y^2<=4, and the row labels are (0,0),(0,1),(1,0),(1,1). Evaluating all 22 complex derivative columns and the real trace pairing yields exactly
\[
G=\begin{pmatrix}
22&0&0&64\\
0&64&-8&0\\
0&-8&86&0\\
64&0&0&296
\end{pmatrix},\qquad \det G=13143040\equiv0\pmod5.
\]
But the four columns (j=0,z=0), (j=1,z=0), (j=0,z=1), (j=1,z=1) give
\[
M=\begin{pmatrix}
1&0&1&0\\
0&0&1&0\\
0&1&1&1\\
0&0&1&1
\end{pmatrix},\qquad\det M=-1\not\equiv0\pmod5.
\]
The rank defect is **quadratic**, not observational. The selected minor is an invertible *real-coordinate* submatrix, so the original integer-channel evaluation matrix has row rank 4 over F_5. Yet the odd-parity source vector x=(0,1,-2,0) satisfies Gx=0 (mod 5), while its original evaluation at the (j=0,z=1) channel is -1 (mod 5), hence E^T x is nonzero. The principal 3x3 Gram minor on rows (0,3,1) equals 2416*64, a unit modulo 5, proving rank(G mod 5)=3. Thus the restricted quadratic-pairing radical is exactly one-dimensional. These are bounded exact assertions in the dedicated regression, not a new global claim.

So **complex full row rank modulo 5 does not imply real trace-Gram determinant nonzero modulo 5**. This disproves that proposed general inference only. Here D=3 is outside the 322^4 analytic domain and R=2 does not give a positive p=5 source valuation; do NOT describe this test as a counterexample to the inert-prime valuation theorem or to twinheterodox. The calculation was independently evaluated from the exact derivative and trace formulas; the standalone [exact-integer Python regression](phase201_minor_gram_control.py) now reproduces the same 11-point source, 22 observation columns, two matrices, determinants and mod-5 assertions (its dedicated [Phase201 exact-source CI workflow](../../.github/workflows/phase201-original-minor-control.yml) checks this bounded witness; consult the exact-head workflow result before calling it verified). It is a finite computational witness, not yet committed as Lean.

## 4. What actually can be transported

For any correctly typed **shared** complex ordinary-jet evaluation matrix A (n rows, m columns), set G_A=2 Re(A A*), a real symmetric matrix. Selecting any n columns produces square M. Positivity yields, in characteristic zero,
\[
\det G_A\ge 2^n|\det M|^2.
\]
Sketch: A A*=M M*+N N* (complex Hermitian PSD); Re preserves real PSD. Determinants on real PSD matrices are monotone under Loewner order. Moreover det Re(H)>=det H for complex Hermitian PSD H, by log-det concavity applied to Re(H)=(H+conj(H))/2 and continuity for singular H. This is an **abstract, one-way lower** inequality, not a checked Lean instantiation, nor an upper bound. For the toy above 2^4|det M|^2=16<13143040.

Alternatively, letting E be the integer matrix of real and sqrt(-D) coefficients, G=E diag(2,2D,2,2D,...) E^T and weighted Cauchy–Binet expresses det G as a **sum of squared real-coordinate maximal minors**. These are *not* automatically the selected complex determinant from v7. This identity suggests a formal, source-typed interface, not a substitution.

## 5. Stop and promotion rules

1. **Do not** identify the two evaluation arrays until row/column index sets, ordinary derivative depth, maximal-order lattice versus selected sublattice, weights and a field/integer change of coordinates are explicitly mapped.
2. **Do not** transfer mod-p0 rank to mod-p invertibility of G. Distinguish a complex minor's nonvanishing, the real trace Gram's positivity, and integral divisibility.
3. **Do not** use a bound on one minor to upper-bound the sum of squared minors.
4. A new theorem needs a typed shared evaluation matrix; exact source-identity lemmas and honest local valuation transport; independent prime-existence proof; both bounds about the **same** positive integer; new Lean/negative-control audit and external semantic reconstruction.
5. Keep collaborator attribution, [#51](https://github.com/Dojo-1/tenth-discriminant/issues/51), and human review [#50](https://github.com/Dojo-1/tenth-discriminant/issues/50) open. No other investigator has been contacted and no external theorem has been imported.

**Outcome:** 322^4 Lean source theorem integrated [P relative to formal definitions]; reconstructed explanation [A, still awaiting human semantic review]; general determinant inequality [mathematical sketch, not Lean]; explicit finite rank/Gram counterexample [exact arithmetic, not Lean]; cross-project rank/valuation transport [H, unestablished].
