# Phase203 — two registered research lines, one common integral source

**4 November 2026.** Registered **before** the additional experiments and proof edits as [A: Issue #133](https://github.com/Dojo-1/tenth-discriminant/issues/133) and [B: Issue #134](https://github.com/Dojo-1/tenth-discriminant/issues/134). Baseline is the existing Phase202 branch (root-import fix \`e9ca6ba\`) and the integrated [322⁴ actual-field theorem PR #126](https://github.com/Dojo-1/tenth-discriminant/pull/126), not a new number-field assertion.

All stated jets use the *original* integer-pair source of [IntegerTraceGram.lean](../../lean/TenthDiscriminant/IntegerTraceGram.lean): ordinary Z-derivatives with W held fixed, rectangular monomial row order, selected order Z[sqrt(-D)], paired trace weights 2 and 2D. The field discriminant is NOT the Gram determinant.

## A. Integral source and one-characteristic kernel/radical transport

**Formal target:** for each field k, E in Mat_(n×m)(k) and B in Mat_m(k), let G=EBEᵀ and let Rad_B(im Eᵀ) be the subset of image vectors killed by E B. The elementwise kernel sequence is
\[
0 \longrightarrow \ker E^{T}
\longrightarrow \ker G
\xrightarrow{E^{T}}
\operatorname{Rad}_B(\operatorname{im}E^{T})
\longrightarrow0.
\]
Its fieldwise dimension consequence is
\[
\operatorname{rank}_k G=\operatorname{rank}_k E-
\dim_k\operatorname{Rad}_B(\operatorname{im}E^{T}).
\]
These are classical linear algebra, not new mathematics. No assumption that B is nondegenerate is needed. **Do not** identify different places or infer modular positivity from real positivity.

**Baseline correction:** Phase202's scoped \`PlacewiseTransport.lean\` compiled and exposed only standard axioms, but the previous full-root audit complained \`UNAUDITED_PROJECT_MODULES: TenthDiscriminant.PlacewiseTransport\`. The repair added this module to \`lean/TenthDiscriminant.lean\`, preserving the audit itself, in the parent Phase202 branch \`e9ca6ba\`. This is a repository integration correction, not a new mathematical theorem.

**New Phase203 artifact:** [PlacewiseExactSequence.lean](../../lean/TenthDiscriminant/PlacewiseExactSequence.lean) imports the previous module and adds explicit kernel inclusion, exact radical image, the three elementwise exactness conditions and an equivalence between no additional Gram-kernel vectors and radical triviality. It is included in the Phase203 root import list. **At writing, this new module is a Lean candidate pending scoped and whole-root receipt.** We DO NOT claim a dimension formula is yet formalized in Lean, nor that a sorry-free file has been verified merely by committing it.

Controls retained: the previous p=5 full-evaluation/modular-Gram rank split (4 vs 3); the p=2 trace-factor degeneration; the D215 p=7 radical0/2 on separate Q16/Q25 supports. Changed observation supports imply different integer Gram determinants; no transfer of previous field-lower valuation is claimed.

## B. One fixed finite-place intertwiner beyond determinant coincidences

**Experiment freeze:** p=7, D=215 (only D mod7=5 matters to source reduction), rows 0<=r<14, 0<=s<2, jets j=0,1, and original integer-pair observations. Equivalently these are the FIRST 28 original row-major rows of the D215,R53,S2 source used in Phase202. These are *not* arbitrary R53 rows and are *not* the whole 106-row original field Gram. Parity is r+s mod2, with 14 even and 14 odd rows. For p7, -D=2 and \(\sqrt{-D}\mapsto\pm3\), so the selected quadratic order splits into two F7 components. The result is typed entirely in **one** residue characteristic.

**Preregistered falsification and its negative findings.** Central negation alone never forces equal parity determinants: already over Z with R=2,S=J=1 and Q={-2,+2} the two blocks have entries 4 and 16. Nevertheless, all 50 F7 symmetric residue-multiset controls (29 nonsingular), then all 30 F49 scalar-extension controls (28 nonsingular), preserved equality of the two 14x14 determinants. These trials were evidence **M**, not proof. A generator bug in the first draft (different weight per orbit member) triggered the parity check; it was corrected *before* accepting any results. The 11 orbit contribution ranks and pairwise kernel-intersection dimensions matched, but those were only necessary for an intertwiner.

**Decisive finite exact certificate.** Solving the 2,156 homogeneous equations for a simultaneous intertwiner among the 11 original source orbits left a **3-dimensional** linear solution space over F7. Of 343 coefficient combinations, four matrices satisfied the full congruence and were invertible. A 49-nonzero-entry \(14\times14\) representative U with \(\det U=1\) was then checked independently using TWO arithmetic paths:
- integer-pair multiplication \( (a+ub)(c+ud)\) with \(u^2=-D\) and direct trace \(2(ac+Dbd)\), with the precise source ordinary derivatives;
- independently, split finite-field embeddings \(z=x+3y,\;w=x-3y\) and the trace \(e_+f_-+e_-f_+\), with ordinary derivative order and W held fixed.

The independent oracles agree **entrywise** on ALL 25 central-inversion orbits of the entire \(\mathbb F_7^2\) residue-pair space (one singleton and 24 pairs). For **every** one of these orbits \(\omega\), the same explicit \(U\) satisfies
\[
\boxed{U^{T}H_{\mathrm{even}}(\omega)U=H_{\mathrm{odd}}(\omega),\qquad
\det_{\mathbb F_7}U=1.}
\]
See [check_intertwiner_f7.py](check_intertwiner_f7.py), containing all 49 nonzero matrix coefficients and independent exact checks.

**Consequent finite theorem [P relative to finite explicit certificate; not Lean P].** Let Q be ANY finite centrally symmetric set (or centrally symmetric integer multiset) of integer pairs, for the original \((R,S,J)=(14,2,2)\) source and ANY \(D\equiv5\bmod7\). Reducing its integer-coordinate Gram modulo7 and separating the 14 even/14 odd source rows gives
\[
G(Q)\bmod7=\begin{pmatrix}H_e(Q)&0\\0&H_o(Q)\end{pmatrix}
\quad\text{after the fixed parity permutation},\qquad
H_o(Q)=U^{T}H_e(Q)U.
\]
**Why it follows:** each residue class belongs to exactly one of 25 inversion orbits; symmetry implies equal multiplicities for the two points of every orbit. The Gram is linear in residue multiplicities, and the 25 explicit orbit congruences sum to the displayed identity. The off-parity zeros are the **pre-existing Lean-proved central-negation symmetry**, not a new symmetry theorem. Therefore \(\det H_o(Q)=\det H_e(Q)\) and \(\det G(Q)=(\det H_e(Q))^2\) in F7. At the original two supports, Q16 and Q25, det H_e are respectively 2 and 0 mod7. The earlier degree-28 square determinant-polynomial factorization is now *explained* by a fixed congruence, not merely interpolation coincidence.

### A deeper operator, tested outside central symmetry

**Prospectively registered extension, after the U construction:** [Issue #134](https://github.com/Dojo-1/tenth-discriminant/issues/134) separately froze tests of a graded source symmetry and its Hermitian refinement; the asymmetry negative-control correction is preserved there.

Let \(V=V_e\oplus V_o\simeq\mathbb F_7^{28}\), using the existing 14+14 parity row permutation. Define two explicit endomorphisms from the *same* certified matrix \(U\):
\[
P=\begin{pmatrix}I&0\\0&-I\end{pmatrix},\quad
J=\begin{pmatrix}0&U\\ U^{-1}&0\end{pmatrix},\quad
C=PJ.
\]
The identities \(P^2=J^2=I\), \(PJ=-JP\), and \(C^2=-I\) are purely matrix algebra. The two involutions \(P,J\) are isometries for **centrally symmetric** Q, because central symmetry removes off-parity Gram terms and U is a congruence of its blocks.

The proposed negative control, an **asymmetric** single observation, did break the *P and J* isometries but **not** the \(C\) isometry. This was an informative falsification of the narrower prediction, not a reason to change or discard the source. The follow-up test was registered BEFORE broadening Q: for **each of all 49 individual residues** \(z\in\mathbb F_7^2\), direct exact arithmetic confirms
\[
\boxed{C^{T}\overline{G}_{z}C=\overline{G}_{z}}.
\]
By source linearity in residue multiplicities, \(C^T\overline G(Q)C=\overline G(Q)\) for **every** finite integer-pair Q at the frozen source dimensions and characteristic, **whether or not Q is centrally symmetric**. At the 49 singleton residues the \(\mathbb F_7\)-Gram ranks are 2 for seven \(y=0\) points and 4 for forty-two non-real-coordinate points.

Because \(-1\) is NOT square in \(\mathbb F_7\), the operator \(C^2=-I\) makes V a rank-14 module over
\[
\mathbb F_{49}=\mathbb F_7[i]/(i^2+1),\qquad i\cdot v=Cv.
\]
This new **row-space algebra** must not be identified with the reduction of the selected **integral order** \(\mathbb Z[\sqrt{-D}]\otimes_{\mathbb Z}\mathbb F_7\cong\mathbb F_7\times\mathbb F_7\). It is essential to reduce an integral order: the characteristic-zero field itself tensored over \(\mathbb Z\) with \(\mathbb F_7\) gives the zero ring, not this residue algebra.

For any source Gram B over \(\mathbb F_7\), define the **typed Hermitian refinement**
\[
h_B(x,y)=B(x,y)+iB(x,Cy)\in\mathbb F_{49}.
\]
The tested \(C^TBC=B\), symmetry of B and \(C^{-1}=-C\) yield \(B(Cx,y)=-B(x,Cy)\). Therefore h is \(\mathbb F_{49}\)-linear in its first argument, conjugate-linear in its second, and Hermitian. It need not be nondegenerate. Its radical is the same underlying kernel as B; in particular,
\[
\boxed{\operatorname{rank}_{\mathbb F_7}B
=2\operatorname{rank}_{\mathbb F_{49}}h_B.}
\]
Hence the Gram's \(\mathbb F_7\)-rank is **even** for every source Q. For nondegenerate B its determinant in \(\mathbb F_7\) is a **square**: diagonalize the Hermitian form over \(\mathbb F_{49}\), choose a basis \((e_j,ie_j)\) over \(\mathbb F_7\), and observe paired real diagonal entries \(a_j,a_j\) with \(a_j\in\mathbb F_7\); a change of \(\mathbb F_7\)-basis only multiplies the determinant by a square.

**Exact evidence [M / algebraic P, source-specific Lean open]:** [verify_hermitian_f49.py](verify_hermitian_f49.py) independently checks all 49 original source singleton matrices, the C-adjoint identities, F49-Hermitian matrix and its rank, plus 30 preregistered asymmetric-weight controls (seed 1). Twenty-six controls are nonsingular, with mod-7 determinants 2 nine times, 4 thirteen times, 1 four times, and 0 four times; full \(\mathbb F_7\) ranks are 28 in 26 cases and 26 in four cases. The symmetric pencil's ranks 28,26,28,18,28,28,28 refine to **F49 ranks 14,13,14,9,14,14,14**. The new script is subject to a fresh exact-head scoped CI receipt. No F49 structure is claimed at \(p=11\) or over \(\mathbb Z,\mathbb R\).

**What this buys:** a pointwise isometric *graded/Hermitian operator* preserving more information than an isolated determinant, with a clear carrier, source action, finite characteristic and two distinct symmetry levels. The claim is stronger than parity separation, but remains **specific to p=7, D mod7=5, R=14, S=J=2**. It does not transfer the prime-divisibility or Archimedean upper of the full production Gram.

**Boundaries and controls:** The same *centered integer lift* of U fails to preserve orbit forms modulo11 (a DIFFERENT residue characteristic), so do not identify those fibres or claim an integral universal isometry. This failure does **not** exclude the possibility of a different U for p11. Removing one point without its negation gives a nonzero cross-parity Gram entry, so the symmetry hypothesis is load-bearing. No same-object analytic gain, arithmetic local-valuation lift, or stronger tenth-discriminant bound is derived. The source R14 result is not the R53 full Gram and cannot be silently substituted in the Phase200 proof.

**Novelty boundary:** no global novelty claim or independent external validation. Previous integrated [CentralSymmetry.lean](../../lean/TenthDiscriminant/CentralSymmetry.lean) and [ParityCompatibility.lean](../../lean/TenthDiscriminant/ParityCompatibility.lean) already prove parity separation and compatible odd-prime Frobenius row actions; Phase203's specific new contribution is the fixed finite-characteristic congruence for the 14+14 source rows, requiring independent mathematical review.

## Reproduce / do not promote prematurely

\`\`\`sh
python3 research/phase203/check_intertwiner_f7.py
cd lean
lake build TenthDiscriminant.PlacewiseExactSequence
lake env lean TenthDiscriminant/PlacewiseExactSequence.lean
\`\`\`

Scoped exact arithmetic, Lean compilation, standard-axiom inspection and complete-root audit are separate receipts. Do not merge while any of these fails. Preserve issues [#133](https://github.com/Dojo-1/tenth-discriminant/issues/133), [#134](https://github.com/Dojo-1/tenth-discriminant/issues/134), external-bridge [#51](https://github.com/Dojo-1/tenth-discriminant/issues/51) and independent human semantic-review [#50](https://github.com/Dojo-1/tenth-discriminant/issues/50) as distinct obligations.

**Next testable mathematical opportunity [H]:** can the explicit mod7 U be given a simple functorial description on the Hermite-jet quotient, and is any analogous place-typed isometry useful for bounding source-minor valuations/Archimedean volumes for the actual large-D full Gram? The first is structural explanation; the second demands new matched original-object bounds and may fail entirely. Stop at the exact finite theorem if it does.
