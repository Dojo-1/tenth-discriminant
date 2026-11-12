# Phase295 — preregister W-equivariant original-jet observation transport obstruction

**12 Nov 2026. PRE-registered before Phase295 code/results.** This is a stacked DRAFT from Phase294 #185 → Phase293 #184 → Phase292 #183 → Phase291 #182, not a merge. Latest Phase294 has successful focused exact-head CI; root Lean review is a separate gate. None of our finite-source observations is a new uniform number-field h=1 theorem or actual discriminant cutoff.

## Research question: can *dense jet mixing* defeat the 104/276 point matching debt?

Phase294 established that the ORIGINAL sampling support Q383 has max point-residue matching279/383 at p5 and107/383 at p25 and all deeper powers under the local field isometry `phi:u587 ↦ alpha u583`, with `583 alpha²=587` in Z5, alpha=2 mod5,17 mod25,67 mod125. It also constructed sharp completions by adding formal non-original points, which are forbidden as a replacement in the actual number-field Gram.

A permutation of original sample points cannot transport the observation support. But could **an arbitrary dense invertible matrix MIXING all sample points and jet orders**, without moving any original sample, still preserve the original **fixed-W** jet-algebra action?

Define p=5, k∈{1,2,3,13}, `A_k=(Z/5^k)[u]/(u²+583)`. This is a **commutative local ring**, residue field F25 because -583≡2 mod5 is not a square. The field chart from D587 to D583 uses `u587→alpha_k*u`. For each ORIGINAL sampled point (x,y) let `w_A(x,y)=x-yu` and `w_B^phi(x,y)=x-alpha_k*y*u`. They are elements of A_k, represented by ordered integer pairs (a,b) modulo p^k. The embedding (x,y)→w(x,y) is injective modulo p^k because {1,u} is an A_k base over Z/p^k.

For fixed original J=5 ORDINARY Z-jets holding W constant, define the FULL observation module over A_k
```
  V_A(k) = ⊕_(q∈Q) A_k^5,       V_B(k)=⊕_(q∈Q) A_k^5.
```
Multiplication by W on the j0..4 observation fibers is a canonical A_k-linear operator
```
  M_{W,A} = diag(w_A(q) I_5)_(q∈Q),
  M_{W,B}^phi = diag(w_B^phi(q) I_5)_(q∈Q).
```
This is forced by the original derivative convention: `∂_Z^j(W f)=W∂_Z^j f`, since **W is held fixed**. It is an OBSERVATION module operator, NOT necessarily an endomorphism of the finite rectangular polynomial-row lattice (since multiplication by W can leave s<S). Do not identify the two carriers.

**Admissible tested category:** any **A_k-linear, invertible** transport `Y∈GL_(5·383)(A_k)` mixing all point fibers and all jet orders, subject to `Y M_{W,A}=M_{W,B}^phi Y` (or equivalently its row/column transpose orientation). The metric is an ADDITIONAL constraint, so proving that **no** W-intertwiner exists rules out any metric-preserving W-intertwiner. No requirement of permutation or block-diagonality is imposed.

## Elementary exact theorem, to be tested adversarially

For any COMMUTATIVE LOCAL ring R, diagonal scalar matrices `D_a=diag(a_i)`, `D_b=diag(b_j)` in M_n(R), there is `Y∈GL_n(R)` with `Y D_a=D_b Y` **if and only if** the multisets `{a_i}` and `{b_j}` agree exactly in R.

**Proof skeleton (paper-level, no computational novelty):** For every entry, `(a_j-b_i)Y_ij=0`. Since detY is a unit, the determinant expansion has AT LEAST ONE permutation sigma for which every entry `Y_(i,sigma(i))` is a unit (the sum of nonunits lies in the local maximal ideal; one unit product must appear). At each such entry, multiply by its inverse to conclude `b_i=a_sigma(i)`. Conversely the matching permutation matrix is a valid intertwiner. This handles even dense mixing and arbitrarily repeated diagonal eigenvalues over a local ring, where characteristic polynomials alone can fail.

**Consequence for the ORIGINAL 383 point support:** each w-value is repeated J=5 times; w-coordinate equality is EQUIVALENT to full point residue equality. Therefore a W-equivariant observation-module iso exists precisely if d_k=0. Phase294's preregistered and verified values d1=104 and d_k=276 for k≥2 imply NO such Y even modulo5, and the obstruction persists at k2,3,13. The fact that full original row lattices have ranks 725 vs730 is irrelevant: their actual observation modules are both rank1915 over A_k (3830 original real/imag Z/p^k channels).

**Minimal completion, strengthened from Phase294:** Within the category where every new original-type observation point adds a **whole J=5 jet block** carrying scalar W at the new point, to make the two observation modules W-equivariantly isomorphic after *APPENDING* blocks, one must append at least d_k point blocks to EACH side. Phase294's explicit residue-multiset completion attains that bound. This is minimal even if the completed intertwiner is allowed to mix every jet/point block densely, because the diagonal intertwiner theorem recovers its eigenvalue multiset. It is **NOT** an absolute minimality claim under arbitrary R_k-linear ambient orthogonal maps that do not commute with W, or under adding exotic modules not decomposed into original-type point-jet blocks.

## Falsification / controls — essential because J=p creates deception

1. Freeze source helper blobs: `research/phase206/source_probe.py` SHA `3f954b59d9f86b06ad53667c869b5b24f2e6c7f6`; `research/phase204/ordinary_jet_filtration.py` SHA `dd8b00547ec09a5d9baec15ad34c9ee3e6e4f6b8`; `research/phase294/support_debt_tower.py` blob to be pinned after retrieving it. Check true D583 rho53/R145/S=J5/Q383 and D587 rho53/R146/S=J5/Q383 **complete ORIGINAL field sources**; both Q literal equal; alpha Hensel k1..13.
2. Independently compute full `W_A` and `W_B^phi` scalar-pair *multiplicity counters*, and their maximal exact value matching, WITHOUT using the previous Q residue matching function as its only implementation. Verify counts `279/107/107/107` at k1,2,3,13. A new bijective rank-2 coordinate check proves that W-value counter and original point-residue counter are equivalent (not assumed).
3. Scale by J5 and report the exact maximal common ORIGINAL jet fibers over A_k and the deficit per side: `5*279=1395`, deficit `520` A_1 jet coordinates at k1 (1040 real/imag Z/5 channels), and `5*107=535`, deficit `1380` A_k coordinates at k≥2 (2760 Z/p^k channels). These are MATCHING/COMPLETION module ranks, **NOT** Gram ranks, primitive row indices, source valuation factors or proof of nonexistence for larger Y lacking W equivariance.
4. Hostile toy: over Z/25 with J=p5, the diagonal scalar matrices `W_A=0*I5`, `W_B=5*I5` have the SAME characteristic polynomial `T^5=(T-5)^5 (mod25)`, yet NO invertible intertwiner `YW_A=W_B Y`. This kills a spectral/characteristic-polynomial shortcut even though the two W are non-similar. Check direct obstruction: `5Y≡0 mod25` forces all entries divisible5, hence no GL5.
5. A different, deliberately LESS restrictive toy: take only the truncated `Z` jet-thickening `M=Z/25[t]/t^5` with `N` multiplication by t. The translation `T f(t)=f(t+5)` gives a UNIMODULAR change of jet basis `T N=(N+5I)T mod25` because `(t+5)^5=0 mod25`. Therefore **Z-only** jet mixing CAN absorb a center shift by5, but **W-fixed** jet transport cannot absorb the corresponding W-scalar shift. This is why original ∂_Z (W held fixed) is load bearing; do not invoke a generic jet-space no-go lacking W.
6. Positive controls: for repeated identical W scalars, nontrivial unimodular shears mixing jet slots within each repeated-value block must intertwine W; a point-permutation along equal W also succeeds. For actual original A_k support under alpha=+1/-1, all W-value multisets match (at -1 via conjugation symmetry), allowing explicit permutations.
7. An invertible A-linear W-intertwiner is REQUIRED by this category; if the user's moving-frame category allows automorphisms of W, arbitrary mixing of value field coordinates not A-linear, or general B-orthogonal transformations not intertwining W, this theorem does NOT settle that larger category. Declare the distinction; do not promote to a universal "no source transport" claim.

## Stop rules / evidence

STOP if source hashes drift, -D not inert, J not five, Q not 383, field-alpha identity fails, W-to-point correspondence fails, counterexample charpoly check fails, Z-only translation fails, or the common-fiber counts disagree with the independently established Phase294 support debt. Keep test results even if a tempting general theorem is refuted.

[P-paper] scalar diagonal intertwiner lemma over commutative local rings, W-multiplication action on ordinary Z-jets, jet-translation toy, minimal completion conditional on original-type point-jet blocks.
[M once focused CI green] exact 1915-dimensional scalar W-value histograms and finite local field chart at p5 k1,2,3,13 with hostile controls.
[H] a permissible larger moving-frame group changing W, plus compatibility of original fully saturated row lattice and source-to-actual-field arithmetic.
[R] any claim that characteristic polynomial equality implies integral similarity over Z/25, that raw jet transport automatically transports divided Frobenius rows, or that these module deficits are additive p-adic Gram valuation factors.
