# Phase202 continuation — residue moments and two typed degeneracy mechanisms

**4 November 2026.** This is a source-constrained, finite mathematical experiment. Original baseline: merged [322^4 field theorem PR #126](https://github.com/Dojo-1/tenth-discriminant/pull/126). Advance registered **before execution** in [#130](https://github.com/Dojo-1/tenth-discriminant/issues/130); the F7 form-pencil experiment registered before probing in [#131](https://github.com/Dojo-1/tenth-discriminant/issues/131). No new field cutoff, no direct identification with twinheterodox v0.7.0, no human peer review, no automatic archimedean/finite-place equivalence.

## 1. The source-typed residue-moment map

The carrier is the ORIGINAL integer-pair ordinary-Z-jet evaluation family, W held fixed. At fixed integers D,R,S,J and prime p, let Q be a finite subset of Z^2 and let
\[
c_Q(\xi)=\#\{(x,y)\in Q:(x,y)\bmod p=\xi\}\bmod p,
\qquad \xi\in(\mathbb F_p)^2.
\]
For a reduced residue pair \(\xi\) and jet depth j, let \(a_{\xi,j},b_{\xi,j}\in\mathbb F_p^{RS}\) be the two coordinate vectors of the **same** original derivative rows. Then
\[
\boxed{\overline{G_Q}=\sum_{\xi\in(\mathbb F_p)^2}c_Q(\xi)\,
  2\sum_{j<J}\left(a_{\xi,j}a_{\xi,j}^{T}
    +(D\bmod p)b_{\xi,j}b_{\xi,j}^{T}\right).}
\]
**[P, elementary exact finite sum identity; independent source-specific Lean still an open obligation].** This follows simply by reducing integer jet polynomials modulo p and grouping the summands by their reduced integer-pair residues. It holds whether p is inert, split or ramified, including characteristic 2. It does NOT assert that distinct residue characteristics are the same base.

The target's kernel/radical short exact sequence retains two distinct mechanisms for a Gram rank deficit:
\[
0\longrightarrow\ker(E_t^T)\longrightarrow\ker(G_t)
\longrightarrow\operatorname{Rad}_{B_t}(\operatorname{im} E_t^T)
\longrightarrow0.
\]
The matrix \(\overline G_Q\) is an integral-source reduction; the Archimedean positive order is not imported.

## 2. Exact matched-support observation at p=7

Take D=215, R=53,S=J=2 and **p=7**, which is a **split** prime since \(-215\equiv2=3^2\bmod7\). This is **not** the inert p=53 used in the separate Frobenius-rank witness. The original integer-pair supports are Q16 (trimmed radius16, 59 points) and Q25 (canonical radius25, 133 points).

Both supports reduce to the *same 21 residue classes* \((x\bmod7,y\bmod7)\), but their multiplicities differ. On Q16 all 21 classes carry a nonzero coefficient modulo7. On Q25, **5 classes have coefficient zero** (x residues 0,1,2,5,6 with y=0). The row-wise source evaluation rank is 28 for either support, yet the trace-Gram rank drops from 28 to26. The exact grouped-residue oracle and the original direct jet oracle agree **entry by entry** for both supports and for matched p=11 controls. The p=11 controls have 33 occupied classes with no zero residue weights; Gram rank remains44 at both radii.

**The mechanism:** reducing a larger integer support at a finite prime changes its *multiplicity-weighted bilinear form*, not necessarily the rank of its polynomial evaluation module. Some repeated points cancel modulo p although they add nonnegative squared norms over the real embedding.

The [residue grouping regression](residue_count_transport.py) also verifies a metamorphic property: inserting p identical copies of a reduced residue does not change the modular Gram, but does add nonnegative contributions to the real Gram. This synthetic multiset control is NOT a new finite subset of the original ellipse.

## 3. A finite algebraic pencil on the same 28D quotient

Since Q16 is contained in Q25, the smaller evaluation map's transpose kernel contains the larger one's. Both have rank28, so the kernels are equal: a common 78D subspace of \(\mathbb F_7^{106}\). The canonical common quotient \(V\) has dimension28. The two induced forms \(\beta_{16},\beta_{25}\) are not isometric because their radicals have dimensions0 and2.

Freeze the form pencil **over the single field F7**
\[
\beta_t=(1-t)\beta_{16}+t\beta_{25},\qquad t\in\mathbb F_7.
\]
Only \(t=0,1\) are the two actual ellipse supports. Others are formal *residue-weight* interpolations, not physical/radical radius values or additional quadratic fields. An independent DomainMatrix/GF(7) elimination confirmed the quotient rank profile.

| t | active reduced classes | effective eval rank | Gram rank | eval kernel in V | restricted-pairing radical |
|--:|--:|--:|--:|--:|--:|
| 0 | 21 | 28 | 28 | 0 | 0 |
| 1 | 16 | 28 | 26 | 0 | 2 |
| 2 | 21 | 28 | 28 | 0 | 0 |
| 3 | 9 | 18 | 18 | 10 | 0 |
| 4 | 21 | 28 | 28 | 0 | 0 |
| 5 | 19 | 28 | 28 | 0 | 0 |
| 6 | 19 | 28 | 28 | 0 | 0 |

At t=1 the information loss is **pairing radical**: eval rank28 but Gram rank26. At t=3 it is **effective sample collapse**, not a pairing radical: 12 of the 21 classes cancel modulo7, leaving nine active, eval rank18 and Gram rank18. More specifically, for t=3 only the y=0 residues (all seven x) and the two (x=0,y=+/-1) residues remain active. These two mechanisms would be conflated by reporting only a determinant or Gram rank.

The exact **crossing form** \((\beta_{25}-\beta_{16})|_{\operatorname{Rad}(\beta_{25})}\) is the zero 2-by-2 matrix. Hence the t=1 degeneracy is non-transverse for this particular affine direction: in the polynomial determinant of the 28D form pencil, the root t=1 has multiplicity at least 4. The t=3 rank defect10 implies multiplicity at least10. These lower multiplicity bounds follow from block determinants in a basis adapted to the radicals; their source-specific polynomial-factor identity is a separate verification target.

**Controls:** full 106D Gram and reduced 28D quotient ranks agree for every t. Two explicit radical vectors at t=1 are given in [Issue #131](https://github.com/Dojo-1/tenth-discriminant/issues/131) and the earlier [certificate](certify_mod7_rank_drop.py). No lifting of the formal parameter t to a compatible family of actual number fields has been asserted.

## 4. Formalization targets and stop rules

A separate [Lean source file](../../lean/TenthDiscriminant/PlacewiseTransport.lean) attempts, without axioms/sorries, four restrained steps: original trace 2/2D decomposition, source Gram-entry decomposition, base-change under any ring hom, and typed kernel-to-radical preimage. Its compilation and axiom status require an exact-head GitHub Actions receipt; do not elevate the source merely because it was committed.

Subsequent theorem targets:
- Formalize original-integer-source residue grouping for each p, **without** a false inter-prime map.
- Formalize the kernel/radical short exact sequence and dimension formula, including the possibility of degenerate ambient trace weight at p=2 or ramified p.
- Formalize a fixed-quotient symmetric-form pencil with the distinct rank-drop strata; classify crossing multiplicities only after a source-typed determinant polynomial certificate.

**Kill condition:** if an independently recomputed entry, rank, radical witness, or quotient kernel is inconsistent, retire that claim. **Stop:** no claimed new 322^4 cutoff until an improved arithmetic divisor AND Archimedean upper concern precisely one unchanged, positive integer determinant under the same field hypotheses. External v0.7.0 still uses different Q,R,S,J and a selected minor, not this Gram. Human review [#50](https://github.com/Dojo-1/tenth-discriminant/issues/50) remains open.

Reproduce at low cost, no GPU/Work:
\`\`\`sh
python3 research/phase202/residue_count_transport.py
python3 research/phase202/form_pencil_f7.py
\`\`\`
