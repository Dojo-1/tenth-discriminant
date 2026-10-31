# Phase138 — graded Gram volumes and multiscale block estimates

**31 October 2026. Status: classical linear-algebra consequences [P, paper derivations], exploratory finite arithmetic [M until exact-head CI], and new production-bound conjectures [H].** No improvement of the strict 47-billion actual-field result is claimed.

This study is motivated by the [CMSA Report of the Summit on Math Research in the Age of AI, 22–23 October 2026](https://cmsa.fas.harvard.edu/media/2026/10/Summit-on-Math-Research-in-the-Age-of-AI.pdf), especially pp. 3 (conjecture formulation, exposition and diverse scholarly contributions), 5 (versioned conjecture/experiment repositories), and 9 (verification versus semantic validation). We use the report's *research-evaluation distinction*, not the report as authority for the new algebra. The exploratory process also asks for small counterexamples, missing cases, exact compatibility maps and a human-reconstructible question. Classical Hadamard–Fischer, Schur complement, canonical correlations and integral basis reduction supply mathematical prior art. Originality of a production inequality has **not** been established.

## Frozen object and higher-dimensional decomposition

Keep the original complete ellipse \`Q=ellipsePairs D rho\`, every ordinary derivative \`j<J\`, original rectangular monomial observations \`E\` with \`n=R*S\` rows, and integral positive trace metric \`B\`. Set \`G=E B E^T\`, positive definite under the original point-count guard.

Index rows by \`i=(r,s)\`, \`0<=r<R,0<=s<S\`. Define graded radial fibers

    I_d = {(r,s) : r-s=d},   -(S-1) <= d <= R-1.

Each fiber is a space of dimension \`|I_d|\`, NOT a two-dimensional point or a single scalar. The original centered frame, the Phase137 Chebyshev-like frame and any family

    F_(r,s)(Z,W) = Z^(r-m) W^(s-m) P_m(ZW),
    m=min(r,s),  P_m monic in Z[u],

have an integral row action \`H\` that is block diagonal **by d=r-s** and determinant one on every fiber. (The terms \`Z^(r-m+t)W^(s-m+t)\` all have the same r-s.) Therefore:

    H in product_d GL_{|I_d|}(Z), det H_d = 1,
    G' = H G H^T,
    det(G'_{I_d,I_d}) = det(G_{I_d,I_d}) for each d.

The same arithmetic integer is retained: \`det G'=det G\`. If the guarded original inert-prime extraction is \`U_p E=Delta_p C_p\`, then \`(U_p H^{-1}) E'=Delta_p C_p\`; no new p-power is claimed. The actual field and its discriminant are never replaced.

This is an exact **within-fiber gauge invariance** (paper proof), not a claim that any arbitrary unimodular H respects each fiber block: an H mixing fibers can alter each block determinant even though it preserves the whole det G.

## The nested block-volume hierarchy

Let \`P\` partition the row indices into unions of complete fibers. The positive block product is

    V_P(G) = product_(A in P) det(G[A,A]).

For the singleton partition, \`V=product_i G_ii\` is the ordinary Hadamard ceiling. For the radial-fiber partition \`P_rad\`, each factor is a genuine higher-dimensional volume. If \`P'\` is COARSER than \`P\`, Hadamard–Fischer gives

    0 < det G <= V_(P') (G) <= V_P(G) <= product_i G_ii.

All these block products are unchanged by integral monic radial frames: each union of fibers remains invariant under H, with determinant-one restriction. **This is a stronger representation-invariant object than the individual diagonal ceiling.**

At the coarsest partition \`P={all rows}\`, \`V_P=det G\` by definition, which is a tautological bound and supplies no practical analytic certificate. Improvement requires a **uniformly estimable intermediate block-volume bound**, not replacing the desired determinant by itself.

Central symmetry of the actual original ellipse gives an existing stronger selection rule, [CentralSymmetry.lean](../../lean/TenthDiscriminant/CentralSymmetry.lean): the off-parity Gram entries are exactly zero. Because \`r+s mod2 = r-s mod2\`, all odd-d fibers are orthogonal to all even-d fibers. [ParityCompatibility.lean](../../lean/TenthDiscriminant/ParityCompatibility.lean) already checks compatibility with guarded odd-prime row operations; do not present parity separation as a new theorem. Merging an odd fiber with an even fiber yields **zero new coupling gain**; this is an important negative control.

For TWO positive blocks, write

    G_AB = [A  C; C^T  D],    A,D positive definite.

The block determinant formula gives

    det G_AB = det A det D det(I-K^T K),
    K = A^(-1/2) C D^(-1/2).

All singular values \`sigma_j(K)\` lie in \`[0,1)\`. Hence the **canonical-correlation spectrum** (a vector, not just one scalar) governs the gain on merging two fibers:

    log det A + log det D - log det G_AB
      = sum_j -log(1-sigma_j(K)^2) >= 0.

These canonical correlations are invariant under invertible changes of basis INSIDE either block. They are candidate non-scalar observables for the interactions among radial fibers. The spectral statement is elementary linear algebra, not a new theorem.

## Exploratory exact 32-row example — not a uniform bound

Freeze the original D=19, rho=5, R=8, S=J=4, all 21 ellipse nodes, 32 rows and all 168 original ordinary-jet coordinates. The row interpolation guard \`2*(R-1)+(S-1)=17<21\` holds. The 11 fibers have sizes:

    [1,2,3,4,4,4,4,4,3,2,1].

An in-session arbitrary-precision integer probe predicted the following *logarithms of exact positive integer products* (rounding occurs only for presentation). The [executable source](phase138_exact_fibers.py) is the required reproducibility gate; the tabulated numbers remain provisional until source-matched CI passes.

| Observation | Centered powers | Chebyshev-type | Shared c=-83 for P2 |
|:--|--:|--:|--:|
| log product of all 32 diagonal entries | 585.557677543 | 579.753853408 | 579.806638232 |
| log product of 11 radial-fiber determinants | 543.904300463 | 543.904300463 | 543.904300463 |
| log product of the two full parity-sector determinants | 530.285191202 | 530.285191202 | 530.285191202 |

The fiber product is independent of the radial monic frame even though its diagonal product is not. The **intra-fiber gap** from centered diagonals is 41.653377079, and for the Chebyshev frame 35.849552945 (in this finite example). The **inter-fiber gap within parity sectors** is 13.619109262. Odd-even cross-sector entries vanish exactly, so the final two-block parity product equals the actual full determinant in this particular symmetry setting.

**Critical counterexample:** the original Phase137 unique row-optimal \`c=-83\` has cost 378274 versus the Chebyshev \`c=-86\` cost 378688 **for row (2,2)**, but applying the same modified \`P_2\` to *every* eligible row worsens the TOTAL diagonal product by about 5.42% relative to Chebyshev. The globally shared family and one-row shear are different mathematical actions; local optimality cannot be silently promoted to family optimality.

A trivial different H mixing two one-dimensional fibers, \`G=I_2\` and \`H=[[1,1],[0,1]]\`, preserves det G=1 but changes the product of singleton block determinants from 1 to 2. This **kills the overstrong conjecture** that arbitrary integer row frames preserve every radial-block product.

## Three distinct research directions (all H)

**H1, productive upper-bound target:** For the SAME production \`G_D\`, can one bound the radial-fiber block product from above, uniformly over all admissible \`D>=46,000,000,000\`, with an extra normalized saving of at least 43/10000 relative to the existing certified upper envelope? That would combine with the unchanged prime lower and a *new* independently checked logarithm bracket to yield a conditional strict 46-billion result. The finite 32-row gap is not evidence for the full asymptotic range. **Counterworld:** all accessible block estimates lose the gain through the highest ordinary-derivative slots, even if the exact block product would be smaller.

**H2, coupling-spectrum conjecture:** Within the SAME parity sector, can one prove explicit lower bounds on the *number and size* of nonzero canonical correlations for a controlled family of unions of radial fibers, uniformly under original integer node and high-jet conditions? The potential gain has multiple singular values per merge. The counterworld includes parity-forbidden couplings (already zero by Lean), decoupled fibers and rapidly vanishing correlations in the production scaling. No blanket positive lower bound is asserted.

**H3, controlled integral block-transport:** Can a sequence of **integer** inter-fiber shears and nested block decompositions give a short, verifiable certificate that improves the bound while preserving the original p-local extraction via the corrected map \`U_p H^{-1}\`? Unlike within-fiber frames, inter-fiber shears can change \`V_P\`; their cost and parity effects must be counted. Search with explicit coefficient-height budgets and test noncommuting path diagrams, instead of treating their product as automatically commutative. The counterworld is that every cheap inter-fiber gain is offset by a harder block estimate or parameter guard.

## The moving-frame / breathing distinction

An integral frame change belongs to discrete `GL_n(Z)`; there is no nonconstant smooth path of integral frames. Nevertheless, **continuous real determinant-one row frames are admissible for the Archimedean upper bound**. For any explicitly specified `H(t) in SL_n(R)`, the real positive Gram `G(t)=H(t) G H(t)^T` satisfies `det G(t)=det G` exactly. Hadamard/Fischer estimates on `G(t)` therefore constrain the SAME original integer determinant, even if `H(t)` has noninteger coefficients. The original inert-prime divisibility remains attached to the original integral `G`; we do NOT assert that `H(t)E` is an integral lattice or carries the original p-local normalization. An integer return is needed only for that extra lattice interpretation, not for the determinant-one real upper comparison.

The analytic constraint is *non-circularity*: optimizing a frame through unknown entries of the entire Gram can reproduce `det G` tautologically. A useful bound needs a frame and row/block majorants derived from explicit, independently estimable moments. Discrete refinement/coarsening of block covers may alternate with continuous real shears, but any claimed new upper must still be costed on the original full ordinary-jet system. Changing D alters the field and often matrix dimension, so no canonical cross-D transport is presumed.

We have separate integer structure, real positive forms, p-local filtrations, and semantic proof obligations. A map between these is named and checked when it exists. There is no assertion of ambient hyperbolic curvature or topological holonomy merely from this organization.

## Validation, semantic alignment and contributor practice

- [P/paper] Fiber-gauge determinant invariance, block Fischer monotonicity, positive-definite canonical correlation formula and the discrete nature of GL_n(Z). Classical tools, with exact hypotheses shown; these generic theorems are **not yet new Lean declarations**.
- [P/existing Lean] The centrally symmetric original integer Gram's parity orthogonality and odd-p compatibility: [CentralSymmetry.lean](../../lean/TenthDiscriminant/CentralSymmetry.lean), [ParityCompatibility.lean](../../lean/TenthDiscriminant/ParityCompatibility.lean).
- [M pending] Exact complete-node ordinary-jet finite calculation in [phase138_exact_fibers.py](phase138_exact_fibers.py), with all-fiber determinant equalities and false generalization controls.
- [H] Any production 46-billion gain, quantitative canonical-correlation estimate, or optimal cross-fiber integer frame.
- [R] 'Chebyshev minimizes the whole discrete Sobolev cost'; already killed at one row in Phase137. Also reject 'the row-optimal shared P2 minimizes the family product'; killed by the current finite example.
- [R_transport] No bridge from arbitrary real moving frames, new fields or changed derivative supports to the original p-integral Gram without an exact integer return.
- [R_sem] A kernel-checked proof does not replace an independently verified *intended* theorem. [Issue #50](https://github.com/Dojo-1/tenth-discriminant/issues/50) remains open; [issue #51](https://github.com/Dojo-1/tenth-discriminant/issues/51) still needs global same-matrix transport.

The CMSA report explicitly distinguishes theorem verification from validation of the encoded mathematical statement. The public repository uses ordinary mathematical vocabulary and per-claim evidence status; AI involvement, roles, attribution and the first counterexample are disclosed. No external submission, endorsement or independent referee is implied.

**Next bounded discriminating experiment:** independently recompute the full 32-row \`G\` from all original jets, verify each radial-fiber determinant exactly under three monic frames, check parity orthogonality, measure the two nested block products, and falsify the shared-coefficient global-optimality claim. Then seek an analytic *uniform block estimate*, not another numerical adjustment to the already proved cutoff. Stop if the gain disappears once all j<S are included.
