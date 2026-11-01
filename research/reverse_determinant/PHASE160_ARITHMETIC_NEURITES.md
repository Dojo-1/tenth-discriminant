# Phase160 — Arithmetic neurites and inter-support gluing

*1 November 2026 · original ordinary-jet Gram; source baseline: Phase159 on main at `db3ecc19`. A mathematical construction with exact finite controls, **not** a new discriminant bound.*

The question is whether lattice indices, characteristic-rank failures, and prime-adic valuations can inhabit related worlds without first being collapsed to a scalar or disguised as continuous quantities. The answer is yes through **exact diagrams of integral modules and quadratic forms**, provided that we preserve the source matrix and distinguish proven transport from speculative Spin/neurite language.

## Source and types

Fix positive D, R, S=J, and a finite ground set U of integer-pair observations. Let `E_Q: Z^{N_Q} -> Z^M`, M=RS, contain precisely the original ordinary partial-Z jet columns (W held fixed), with identically zero imaginary channels of real-axis points omitted. Real channels have global weight 2 and nonreal imaginary channels global weight 2D. Each original observation has the SAME channels and weights in every support; their order can be permuted without effect.

Define `L_Q=im(E_Q)`, `C_Q=Z^M/L_Q`, and `G_Q=E_Q B_Q E_Q^T`. For real full-rank supports `G_Q` is positive definite and `d_Q=[Z^M:L_Q]` is finite. The quotient `H_Q=det(G_Q)/d_Q^2` is a positive integer. The Smith module retains more information than the index: at every prime q,
\[
\dim_{\mathbf F_q}(C_Q\otimes\mathbf F_q)=M-\mathrm{rank}_{\mathbf F_q}E_Q.
\]
In particular the Phase158 p-1-root obstruction nullity agrees with this characteristic-p dimension under the same original-jet/Frobenius rank equivalence. A bad witness-prime rank does **not** imply real Gram singularity.

## The exact observation neurite [P-paper, elementary]

For Q subset Q', the natural quotient map is surjective with an exact kernel:
\[
0\to L_{Q'}/L_Q\to C_Q\to C_{Q'}\to0.
\]
This is a composable, directed transport of arithmetic modules. It is not an isometry of real Grams. It survives base change to localizations; tensoring a full short exact sequence with a residue field may lose left exactness, so modular rank data must be recalculated.

Two supports A,B admit a stronger raw bridge. Because `L_{A union B}=L_A+L_B`, set
\[
\mathcal R(A,B)=(L_A\cap L_B)/L_{A\cap B}.
\]
The maps `x -> (x mod L_A, x mod L_B)` and `(u,v) -> u-v mod (L_A+L_B)` give the exact sequence
\[
\boxed{0\to\mathcal R(A,B)\to C_{A\cap B}
 \to C_A\oplus C_B\to C_{A\cup B}\to0.}
\]
Proof: the first kernel is `(L_A cap L_B)/L_{A cap B}`; the difference map is onto; if `x-y=a+b` for `a in L_A, b in L_B`, the common representative `x-a=y+b` gives exactness at the direct sum.

If `A cap B` is already full rank, all terms have finite order and
\[
|\mathcal R(A,B)|={d_{A\cap B}d_{A\cup B}\over d_A d_B}\in\mathbb Z_{\ge1}.
\]
In particular, for every prime q, the *gluing defect*
\[
\eta_q(A,B)=v_q(d_{A\cap B})+v_q(d_{A\cup B})-v_q(d_A)-v_q(d_B)
=v_q(|\mathcal R(A,B)|)\ge0.
\]
This is supermodularity of the index valuation on the domain of full-rank intersections. If the intersection has deficient rank, the exact sequence remains valid, but these finite-order ratios are **not** licensed.

## The opposing real curvature and normalized remainder [P-paper]

The original positive diagonal metric gives the inclusion-exclusion identity
\[
G_A+G_B=G_{A\cap B}+G_{A\cup B}.
\]
It does **not** give the same identity for determinants. For full-rank `A cap B`, log-determinant submodularity of sums of positive semidefinite observation contributions gives
\[
\kappa_\infty(A,B):=\log {\det G_A\,\det G_B\over
\det G_{A\cap B}\,\det G_{A\cup B}}\ge0.
\]
The proof uses `G_A=H+X`, `G_B=H+Y`, `G_union=H+X+Y`, where H>0 and X,Y>=0, and the decreasing marginal gain `logdet(H+X)-logdet(H)` as the baseline grows from H to H+Y.

Combining arithmetic and real transport produces the exact identity
\[
\boxed{\log {H_AH_B\over H_{A\cap B}H_{A\cup B}}
=\kappa_\infty(A,B)+2\log|\mathcal R(A,B)|\ge0.}
\]
Thus `log H_Q` is submodular on this full-rank domain. This is a derived combination of classical integral-lattice and determinant facts, **not a claimed original general theorem**. The two curvatures are discrete inclusion-exclusion defects, not evidence of nontrivial holonomy around an intrinsically flat support-poset connection.

## Plucker weaving: a more discriminating 2-adic observable [P-paper]

For each effective scalar channel i, let `a_i` be the original integral column and `b_i>0` its exact trace weight. Cauchy-Binet gives
\[
\det G_Q=\sum_{I,\ |I|=M}(\det E_I)^2\prod_{i\in I}b_i.
\]
The vector of signed maximal minors is the oriented exterior/Plucker weave. For prime q define
\[
\mu_q(Q)=\min_{\det E_I\ne0}\left[
  2v_q(\det E_I)+\sum_{i\in I}v_q(b_i)\right].
\]
Let `beta_q(Q)` be the original ordinary-jet factorial/weight **capacity floor** obtained by ignoring whether a maximal minor vanishes and minimizing the forced column valuations. Then the nonnegative integers
\[
\sigma_q=\mu_q-\beta_q,\qquad
\epsilon_q=v_q(\det G_Q)-\mu_q
\]
give the exact decomposition
\[
\boxed{v_q(\det G_Q)=\beta_q+\sigma_q+\epsilon_q.}
\]
Here `sigma` detects constraints and extra divisibility of actual Plucker coordinates beyond the naive factorial minimum. `epsilon` measures prime-adic cancellation among minimal-weight nonzero minor terms. Neither can be inferred from the jet channel count alone.

At q=2, every minimal-weight term divided by \(2^{\mu_2}\) is odd. Therefore **the bound \(\mu_2\) is sharp if and only if the number of minimizing nonzero minors is odd**. With an even number, \(\epsilon_2\ge1\). For odd q one needs the actual q-unit residues, not just parity. This is a precise algebraic "phase weave," and it does not require invoking physical spin.

## Tests on the canonical original-jet convention [M]

The [bounded verifier](phase160_arithmetic_neurites.py) imports the Phase159 ordinary-jet evaluator and keeps the unchanged source weights `2,2D`.

For D=3, R=S=J=2, let the overlap support be `C={(0,2)}`; its original evaluation matrix has Smith invariants `(1,1,2,2)`. Extend along two separate branches
`A=C union {(-2,1)}` and `B=C union {(-1,0)}`. Exact integer data:

| support | d_Q | det(G_Q) | H_Q | minimum 2-adic minor weight | number of minimizers | actual v2(det G) |
|---|---:|---:|---:|---:|---:|---:|
| C | 4 | 2,304 | 144 | 8 | 1 | 8 |
| A | 1 | 122,656 | 122,656 | 4 | 6 | 5 |
| B | 1 | 74,896 | 74,896 | 4 | 1 | 4 |
| A union B | 1 | 622,368 | 622,368 | 4 | 34 | 5 |

Hence `R(A,B)=C_C isomorphic to (Z/2)^2` (not merely an order-4 ambiguity). The 2-adic cancellation rule identifies which branches add one valuation beyond their minimum. Across the 91 one-observation-extension diamonds with `x in [-2,2], y in [0,2], x^2+3y^2<=20`, **36** have nontrivial gluing remainders. Another 98 deterministic full-rank random two-dimensional diamonds validate the coupled index/determinant identity (not a universal proof).

An independent one-dimensional example with columns 12,2,4 and weights 2 gives indices (intersection, A, B, union) = (12,2,4,2), `|R|=3`, real determinant curvature ratio `370/369` and normalized curvature ratio `370/41=(370/369)*9`.

**Failed preflight retained:** The first random diamond test incorrectly reassigned weights to a shared observation after reordering columns and violated the real submodularity check. Correcting weights by global observation identity restored the invariants. The first standalone source adapter also accidentally transposed its effective-channel matrix; fixing the row/column typing made the source controls agree. Neither failed attempt is evidence against the correctly typed claims. Both errors are precisely the sort of illegal transport this protocol should expose.

## Spin, not by metaphor alone [S/H and exact no-go]

Each nondegenerate Gram defines a rational quadratic form `q_Q(x)=x^T G_Q x` and its Clifford algebra; Spin is meaningful only after specifying the quadratic space, orientation and intended isometries. Two supports need not admit a rational quadratic-form isometry, even when their cokernels agree.

The 2-row control with source weights all 2, columns e1,e2 and optional e1+e2, has both integral cokernels zero. But its determinants change from 4 to 12, ratio 3, **not** a square in Q. A rational isometry would force a square determinant ratio; therefore there is no source-preserving rational isometric Spin port here. A real isometry can be chosen, but does not transport the integral data for free.

Spin/Witt/Clifford information may be added **only** for paths whose local quadratic-form comparisons and squareclass/Hasse invariants make it useful. The exterior/Plucker and local-module layers are already sufficient for the exact gluing theorem and parity rule. A claim of nontrivial holonomy, spinor-genus gain, or an improved discriminant endpoint would require a new falsifiable invariant.

## Raw intermanifold bridges [H, typed]

Changing D changes the arithmetic parameter and trace metric. For fixed formal observation coordinates and dimensions, integer multiplication and ordinary-jet entries are polynomial in an indeterminate d. We can define a universal presentation over `Z[d]` and specialize to D0 or D1, obtaining cokernel modules at both values by base change. This is an honest *common ancestor*, not a canonical isomorphism between distinct specializations. A changing ellipse needs additional support labels/maps. Rank may jump after specialization; those jump loci are detected by Fitting ideals. Likewise varying R or S requires typed truncation/extension maps; a determinant cannot simply be carried across dimensions.

A useful neurite is therefore a diagram with explicit source/target, cokernel morphism or correspondence, positive-metric contribution, Plucker data, localization, and typed remainder. Growth, pruning and rerouting are operations on this diagram. Real continuity is one fiber; q-adic rank and valuation data are different fibers. There is no automatic equivalence or scalar collapse.

## Production relevance and strict next gate

The existing [arbitrary-Q odd-prime lower theorem](../../lean/TenthDiscriminant/RadialCutoff.lean) still needs positivity, field assumptions and the inert-prime range. The present gluing identity alone does **not** strengthen its valuation. Its value is in giving a precise language for combining characteristic supports, detecting hidden q-primary overlap, and testing whether factorial minima or q-adic cancellation improve the same-Gram lower argument.

1. Formalize the exact two-support cokernel sequence and index defect (prefer a standalone small Lean theorem, without touching the existing 47-billion root).
2. Prove the weighted Cauchy-Binet minimum/parity lemma against the **original source matrix** and exhibit source-matched negative controls.
3. Search for a uniformly competitive-radius support family with a certificate of witness-prime rank and quantitative q-primary gains, then re-establish same-support odd-prime mass, q=2 divisor and analytic upper. No numerical threshold promotion before those bridges close.

**Evidence:** elementary exact algebra [P-paper, not formalized], finite integer tests [M], proposed spin/neurite architecture [S/H], all-`D` observation selection [H]. The established field cutoff remains **47 billion**. The hoped-for 5-billion route remains open.

## Sources and attribution

- [Terence Tao, Tenth Discriminant challenge (2026)](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/) and the distinct work of Green, van Dijk, Pratt and challenge contributors catalogued in [prior art](../../PRIOR_ART.md).
- [Miguel N. Walsh, *Characteristic subsets and the polynomial method* (ICM 2018)](https://www.mathunion.org/fileadmin/ICM/Proceedings/uploads/ICM-2018-vol2-ver1-eb.pdf), inspiration for Phase158's characteristic support, not an asserted source for the present cokernel formula.
- [M. D'Adderio and L. Moci, *Arithmetic matroids, the Tutte polynomial and toric arrangements*, Advances in Mathematics 232 (2013)](https://doi.org/10.1016/j.aim.2012.09.001).
- [A. Fink and L. Moci, *Matroids over a ring*, Journal of the European Mathematical Society 18 (2016)](https://ems.press/journals/jems/articles/13725).
- [Stacks Project, Fitting ideals, Tag 07Z6](https://stacks.math.columbia.edu/tag/07Z6).
- [Submodularity of log determinants of PSD observation sums](https://doi.org/10.1016/j.dam.2012.07.016), established work, not a new universal assertion here.
- [Ojanguren and Parimala, *Clifford algebras and the universal invariant* (2018)](https://doi.org/10.1016/j.exmath.2018.07.004), quadratic-form/Clifford perspective; no direct theorem imported into the discriminant bound.

The specialised mathematical formulation and finite tests were developed in Jesús Vilela Jato's Dojo-1 AI-assisted research process. No originality, citation-based endorsement, independent referee or stronger field theorem is claimed.
